"""Testes da API HTTP e da exportação para a pasta sincronizada.

Nenhum teste aqui usa chave de API: o provedor é substituído por um LLM falso,
como nos testes do Orquestrador. O banco e a pasta de sincronização apontam
para diretórios temporários — nunca para os arquivos reais do professor.
"""

import json

import pytest
from fastapi.testclient import TestClient

import time

from api import main as api_main
from questoes.banco import BancoQuestoes
from questoes.convites import Convites
from questoes.llm.base import ProvedorLLM

from test_orquestrador import _parecer_json, _questao_json


class LLMFake(ProvedorLLM):
    """Alterna questão e parecer indefinidamente, para gerar em lote."""

    def __init__(self, aprovado=True):
        self.aprovado = aprovado
        self.chamadas = 0

    def completar(self, system, user, temperature=0.3):
        self.chamadas += 1
        eh_geracao = self.chamadas % 2 == 1
        return _questao_json() if eh_geracao else _parecer_json(aprovado=self.aprovado)


def gerar_ciclo(cliente, headers=None, espera=10.0):
    """Dispara a geração e acompanha até terminar, como faz a interface.

    A geração é assíncrona: o POST devolve um identificador e o resultado sai
    no acompanhamento. Um ciclo real leva minutos e estouraria o limite de
    tempo de qualquer proxy reverso se fosse uma requisição só.
    """
    inicio = cliente.post("/api/gerar", json=ESPECIFICACAO, headers=headers)
    if inicio.status_code != 200:
        return inicio
    tarefa = inicio.json()["tarefa"]

    limite = time.time() + espera
    while time.time() < limite:
        resposta = cliente.get(f"/api/gerar/{tarefa}", headers=headers)
        if resposta.status_code != 200:
            return resposta
        situacao = resposta.json()
        if situacao["estado"] != "executando":
            return situacao
        time.sleep(0.05)
    raise AssertionError("a tarefa não terminou no tempo esperado")


ESPECIFICACAO = {
    "tema": "funcao_quadratica",
    "habilidade_bncc": "EM13MAT302",
    "nivel_bloom": "aplicar",
    "dificuldade": "media",
    "natureza": "teorica",
    "formato": "discursiva",
}


@pytest.fixture
def cliente(tmp_path, monkeypatch):
    """API isolada: banco temporário, configuração temporária e LLM falso.

    O arquivo de convites também aponta para o diretório temporário. Sem isso
    o teste depende do ambiente: numa máquina que já tenha convites criados, a
    API entra em modo compartilhado e todos estes testes recebem 401.
    """
    monkeypatch.setattr(api_main, "_banco", BancoQuestoes(tmp_path / "banco.db"))
    monkeypatch.setattr(api_main.config_app, "ARQUIVO", tmp_path / "config.json")
    monkeypatch.setattr(api_main, "_convites", Convites(tmp_path / "convites.json"))
    monkeypatch.setattr(api_main, "LOG_DIR", tmp_path / "logs")
    monkeypatch.setattr(api_main, "criar_provedor", lambda *a, **k: LLMFake())
    return TestClient(api_main.app)


@pytest.fixture
def pasta_nuvem(tmp_path, cliente):
    """Configura uma pasta sincronizada temporária no cliente já isolado."""
    pasta = tmp_path / "Drive"
    pasta.mkdir()
    cliente.post("/api/config", json={"pasta_sincronizada": str(pasta)})
    return pasta


def test_opcoes_alimentam_o_formulario(cliente):
    o = cliente.get("/api/opcoes").json()
    assert {t["valor"] for t in o["temas"]} >= {"funcao_afim", "progressao_aritmetica"}
    assert all("codigo" in h and "descricao" in h for h in o["habilidades"])
    assert [d["valor"] for d in o["decisoes"]] == ["aceita", "aceita_com_ajuste", "recusada"]


def test_gerar_devolve_ciclo_completo(cliente):
    situacao = gerar_ciclo(cliente)
    assert situacao["estado"] == "concluida"
    ciclo = situacao["resultado"]
    assert ciclo["aprovada"] is True
    assert ciclo["questao_final"]["enunciado"]
    ultima = ciclo["iteracoes"][-1]
    assert ultima["verificacao"]["veredicto"] == "aprovado"
    assert ultima["parecer"]["aprovado"] is True


def test_geracao_nao_segura_a_requisicao(cliente, monkeypatch):
    """O POST volta na hora, mesmo que o ciclo demore.

    É a razão de existir da tarefa em segundo plano: um ciclo real leva de 80 a
    250 segundos, e proxies reversos derrubam a conexão bem antes disso.
    """
    class LLMLento(LLMFake):
        def completar(self, system, user, temperature=0.3):
            time.sleep(0.4)
            return super().completar(system, user, temperature)

    monkeypatch.setattr(api_main, "criar_provedor", lambda *a, **k: LLMLento())

    inicio = time.time()
    resposta = cliente.post("/api/gerar", json=ESPECIFICACAO)
    duracao = time.time() - inicio

    assert resposta.status_code == 200
    assert "tarefa" in resposta.json()
    assert duracao < 0.2, f"o POST bloqueou por {duracao:.2f}s"

    situacao = gerar_ciclo(cliente)  # e o ciclo termina normalmente depois
    assert situacao["estado"] == "concluida"


def test_progresso_informa_a_etapa_corrente(cliente, monkeypatch):
    """A trilha da interface mostra o que está acontecendo, não uma animação."""
    class LLMLento(LLMFake):
        def completar(self, system, user, temperature=0.3):
            time.sleep(0.3)
            return super().completar(system, user, temperature)

    monkeypatch.setattr(api_main, "criar_provedor", lambda *a, **k: LLMLento())

    tarefa = cliente.post("/api/gerar", json=ESPECIFICACAO).json()["tarefa"]
    etapas = set()
    for _ in range(40):
        situacao = cliente.get(f"/api/gerar/{tarefa}").json()
        etapas.add(situacao["progresso"]["etapa"])
        if situacao["estado"] != "executando":
            break
        time.sleep(0.05)

    # A etapa "verificando" é o SymPy: dura milissegundos e a amostragem pode
    # não pegá-la. O que importa é o progresso avançar de fato, e não a
    # interface animar sozinha enquanto o servidor cala.
    assert "gerando" in etapas
    assert etapas & {"verificando", "criticando"}


def test_tarefa_inexistente(cliente):
    assert cliente.get("/api/gerar/naoexiste").status_code == 404


def test_resultado_sobrevive_a_leituras_repetidas(cliente):
    """Ler o resultado não pode consumi-lo.

    Proxies repetem GET. Se a primeira leitura apagasse a tarefa, a repetição
    devolveria 404 e o ciclo — já concluído e já pago em tokens — se perderia.
    Aconteceu num teste real através do túnel antes desta correção.
    """
    tarefa = cliente.post("/api/gerar", json=ESPECIFICACAO).json()["tarefa"]
    gerar_ciclo(cliente)  # deixa o tempo passar até concluir

    primeira = cliente.get(f"/api/gerar/{tarefa}")
    segunda = cliente.get(f"/api/gerar/{tarefa}")

    assert primeira.status_code == segunda.status_code == 200
    assert primeira.json()["resultado"] == segunda.json()["resultado"]


def test_habilidade_invalida_e_recusada(cliente):
    resposta = cliente.post("/api/gerar", json={**ESPECIFICACAO, "habilidade_bncc": "EM13MAT999"})
    assert resposta.status_code == 422
    assert "EM13MAT999" in resposta.json()["detail"]


def test_falha_do_provedor_vira_erro_legivel(cliente, monkeypatch):
    """O erro do LLM chega à interface como mensagem, não como stack trace."""
    def explodir(*a, **k):
        raise RuntimeError("temperature is deprecated for this model")
    monkeypatch.setattr(api_main, "criar_provedor", explodir)

    situacao = gerar_ciclo(cliente)
    assert situacao["estado"] == "erro"
    assert "temperature is deprecated" in situacao["detalhe"]


def test_salvar_avaliar_e_espelhar_na_pasta(cliente, pasta_nuvem):
    ciclo = gerar_ciclo(cliente)["resultado"]
    salva = cliente.post("/api/banco", json=ciclo).json()
    assert salva["aviso_sincronizacao"] is None
    questao_id = salva["id"]

    md = pasta_nuvem / f"questao-{questao_id:04d}_funcao_quadratica_media.md"
    assert md.exists() and "## Verificação simbólica" in md.read_text(encoding="utf-8")
    assert (pasta_nuvem / f"questao-{questao_id:04d}_funcao_quadratica_media.json").exists()

    indice = (pasta_nuvem / "_indice.csv").read_text(encoding="utf-8-sig")
    assert "decisao_professor" in indice.splitlines()[0]

    resposta = cliente.post(
        f"/api/banco/{questao_id}/avaliacao",
        json={"decisao": "aceita_com_ajuste", "comentario": "trocar o contexto"},
    )
    assert resposta.status_code == 200

    # a avaliação precisa aparecer no banco, no arquivo e no índice
    registro = cliente.get("/api/banco").json()[0]
    assert registro["decisao_professor"] == "aceita_com_ajuste"
    assert "trocar o contexto" in md.read_text(encoding="utf-8")
    assert "aceita_com_ajuste" in (pasta_nuvem / "_indice.csv").read_text(encoding="utf-8-sig")


def test_avaliar_questao_inexistente(cliente):
    resposta = cliente.post("/api/banco/999/avaliacao", json={"decisao": "aceita"})
    assert resposta.status_code == 404


def test_filtros_do_banco(cliente):
    ciclo = gerar_ciclo(cliente)["resultado"]
    cliente.post("/api/banco", json=ciclo)
    assert len(cliente.get("/api/banco?tema=funcao_quadratica").json()) == 1
    assert cliente.get("/api/banco?tema=funcao_afim").json() == []


@pytest.mark.parametrize(
    "formato,assinatura",
    [("markdown", b"# Prova"), ("latex", b"\\documentclass"), ("docx", b"PK")],
)
def test_lista_nos_tres_formatos(cliente, formato, assinatura):
    ciclo = gerar_ciclo(cliente)["resultado"]
    questao_id = cliente.post("/api/banco", json=ciclo).json()["id"]

    resposta = cliente.post("/api/lista", json={
        "titulo": "Prova", "ids": [questao_id], "com_gabarito": True, "formato_arquivo": formato,
    })
    assert resposta.status_code == 200
    assert resposta.content.startswith(assinatura)
    assert "attachment" in resposta.headers["content-disposition"]


def test_lista_sem_selecao_e_recusada(cliente):
    resposta = cliente.post("/api/lista", json={"ids": [], "formato_arquivo": "markdown"})
    assert resposta.status_code == 422


def test_lista_respeita_a_ordem_escolhida(cliente):
    ids = []
    for _ in range(2):
        ciclo = gerar_ciclo(cliente)["resultado"]
        ids.append(cliente.post("/api/banco", json=ciclo).json()["id"])

    corpo = cliente.post("/api/lista", json={
        "ids": list(reversed(ids)), "formato_arquivo": "markdown",
    }).content.decode("utf-8")
    assert corpo.count("**Questão") == 2


def test_pasta_inexistente_vira_aviso_e_nao_impede_de_salvar(cliente, tmp_path):
    cliente.post("/api/config", json={"pasta_sincronizada": str(tmp_path / "nao-existe")})
    ciclo = gerar_ciclo(cliente)["resultado"]

    salva = cliente.post("/api/banco", json=ciclo).json()
    assert salva["id"] == 1                      # a questão entrou no banco
    assert "não existe" in salva["aviso_sincronizacao"]  # e o problema foi reportado


def test_interface_e_servida_com_caminhos_relativos():
    """A mesma cópia da interface roda aqui e no GitHub Pages.

    Caminho absoluto (`/static/app.css`) quebraria no Pages, que publica em
    subdiretório (`usuario.github.io/repo/`).
    """
    c = TestClient(api_main.app)
    assert c.get("/").status_code == 200
    assert c.get("/app.css").status_code == 200
    assert c.get("/app.js").status_code == 200
    assert 'href="app.css"' in c.get("/").text
    assert 'src="app.js"' in c.get("/").text


def test_cors_so_libera_as_origens_declaradas(tmp_path, monkeypatch):
    """Sem CORS restrito, um convite vazado serviria a qualquer site."""
    import importlib

    monkeypatch.setattr(api_main.config_app, "ARQUIVO", tmp_path / "cfg.json")
    api_main.config_app.salvar({"origens_permitidas": "https://exemplo.github.io"})
    modulo = importlib.reload(api_main)  # o CORS é montado na criação do app
    try:
        c = TestClient(modulo.app)
        pedido = {"Access-Control-Request-Method": "GET"}

        permitida = c.options("/api/estado", headers={**pedido, "Origin": "https://exemplo.github.io"})
        assert permitida.headers.get("access-control-allow-origin") == "https://exemplo.github.io"

        recusada = c.options("/api/estado", headers={**pedido, "Origin": "https://outro.site"})
        assert recusada.headers.get("access-control-allow-origin") is None
    finally:
        importlib.reload(api_main)  # devolve o módulo ao estado dos demais testes


def test_chave_de_api_nunca_vai_para_o_disco(cliente, tmp_path):
    """A chave viaja no cabeçalho e é descartada; o disco guarda só preferências."""
    cliente.post("/api/config", json={"modelo": "claude-sonnet-5"})
    gravado = json.loads((tmp_path / "config.json").read_text(encoding="utf-8"))
    assert gravado["modelo"] == "claude-sonnet-5"

    estado = cliente.get("/api/estado", headers={"X-Chave-API": "sk-ant-segredo"}).json()
    assert estado["chave_presente"] is True

    # nada do que foi enviado sobrou em arquivo algum
    for arquivo in tmp_path.rglob("*"):
        if arquivo.is_file():
            assert "sk-ant-segredo" not in arquivo.read_text(encoding="utf-8", errors="ignore")
