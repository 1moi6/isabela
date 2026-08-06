"""Testes do acesso por convite e do isolamento entre bancos.

O ponto crítico aqui não é o convite funcionar — é a pessoa A não conseguir
ver, avaliar nem exportar as questões da pessoa B.
"""

import pytest
from fastapi.testclient import TestClient

from api import main as api_main
from questoes.banco import BancoQuestoes
from questoes.convites import Convites, identificador_de

from test_api import ESPECIFICACAO, LLMFake, gerar_ciclo


@pytest.fixture
def ambiente(tmp_path, monkeypatch):
    """API isolada, com arquivo de convites próprio."""
    monkeypatch.setattr(api_main, "_banco", BancoQuestoes(tmp_path / "banco.db"))
    monkeypatch.setattr(api_main.config_app, "ARQUIVO", tmp_path / "config.json")
    monkeypatch.setattr(api_main, "LOG_DIR", tmp_path / "logs")
    monkeypatch.setattr(api_main, "criar_provedor", lambda *a, **k: LLMFake())
    convites = Convites(tmp_path / "convites.json")
    monkeypatch.setattr(api_main, "_convites", convites)
    return TestClient(api_main.app), convites, tmp_path


def _gerar_e_salvar(cliente, cabecalhos):
    ciclo = gerar_ciclo(cliente, headers=cabecalhos)["resultado"]
    return cliente.post("/api/banco", json=ciclo, headers=cabecalhos).json()["id"]


def test_identificador_e_estavel_entre_reemissoes():
    """Revogar e reemitir convite não pode custar o banco da pessoa."""
    assert identificador_de("Maria Silva") == identificador_de("maria silva")
    assert identificador_de("José da Conceição") == "jose-da-conceicao"


def test_sem_convites_o_sistema_e_local(ambiente):
    cliente, _, _ = ambiente
    estado = cliente.get("/api/estado").json()
    assert estado["compartilhado"] is False
    assert cliente.post("/api/gerar", json=ESPECIFICACAO).status_code == 200


def test_com_convites_o_acesso_passa_a_ser_exigido(ambiente):
    cliente, convites, _ = ambiente
    convites.criar("Maria Silva")

    assert cliente.get("/api/estado").status_code == 401
    assert cliente.post("/api/gerar", json=ESPECIFICACAO).status_code == 401
    assert cliente.get("/api/estado", headers={"X-Convite": "inventado"}).status_code == 401


def test_convite_valido_identifica_a_pessoa(ambiente):
    cliente, convites, _ = ambiente
    maria = convites.criar("Maria Silva")

    estado = cliente.get("/api/estado", headers={"X-Convite": maria["codigo"]}).json()
    assert estado["compartilhado"] is True
    assert estado["nome"] == "Maria Silva"


def test_bancos_sao_isolados_entre_pessoas(ambiente):
    cliente, convites, _ = ambiente
    maria = {"X-Convite": convites.criar("Maria Silva")["codigo"]}
    joao = {"X-Convite": convites.criar("João Souza")["codigo"]}

    id_maria = _gerar_e_salvar(cliente, maria)
    _gerar_e_salvar(cliente, joao)
    _gerar_e_salvar(cliente, joao)

    assert len(cliente.get("/api/banco", headers=maria).json()) == 1
    assert len(cliente.get("/api/banco", headers=joao).json()) == 2
    assert cliente.get("/api/estado", headers=maria).json()["total_no_banco"] == 1
    assert cliente.get("/api/estado", headers=joao).json()["total_no_banco"] == 2

    # João não avalia questão da Maria, mesmo sabendo o número dela
    recusa = cliente.post(
        f"/api/banco/{id_maria}/avaliacao", json={"decisao": "recusada"}, headers=joao
    )
    assert recusa.status_code == 404

    # nem a inclui numa lista
    lista = cliente.post(
        "/api/lista", json={"ids": [id_maria], "formato_arquivo": "markdown"}, headers=joao
    )
    assert lista.status_code == 404


def test_chave_de_cada_um_vai_na_propria_requisicao(ambiente, monkeypatch):
    """Duas pessoas ao mesmo tempo: cada geração usa a chave de quem pediu.

    Antes a chave era global no processo, e a segunda pessoa a configurar
    sobrescrevia a primeira — cobrando dela o uso alheio, sem erro visível.
    """
    cliente, convites, _ = ambiente
    usadas = []

    def registrar(nome, modelo=None, api_key=None, url=None):
        usadas.append(api_key)
        return LLMFake()

    monkeypatch.setattr(api_main, "criar_provedor", registrar)

    cliente.post("/api/gerar", json=ESPECIFICACAO, headers={
        "X-Convite": convites.criar("Maria Silva")["codigo"], "X-Chave-API": "chave-da-maria",
    })
    cliente.post("/api/gerar", json=ESPECIFICACAO, headers={
        "X-Convite": convites.criar("João Souza")["codigo"], "X-Chave-API": "chave-do-joao",
    })

    assert usadas == ["chave-da-maria", "chave-do-joao"]


def test_tarefa_de_uma_pessoa_nao_e_vista_por_outra(ambiente):
    """O identificador da tarefa não pode servir de atalho para o ciclo alheio."""
    cliente, convites, _ = ambiente
    maria = {"X-Convite": convites.criar("Maria Silva")["codigo"]}
    joao = {"X-Convite": convites.criar("João Souza")["codigo"]}

    tarefa = cliente.post("/api/gerar", json=ESPECIFICACAO, headers=maria).json()["tarefa"]
    assert cliente.get(f"/api/gerar/{tarefa}", headers=joao).status_code == 404
    assert cliente.get(f"/api/gerar/{tarefa}", headers=maria).status_code == 200


def test_convidado_nao_altera_configuracao_do_servidor(ambiente, tmp_path):
    """Senão um convidado redireciona o espelho do dono para outro lugar."""
    cliente, convites, _ = ambiente
    maria = {"X-Convite": convites.criar("Maria Silva")["codigo"]}

    resposta = cliente.post(
        "/api/config", json={"pasta_sincronizada": "/tmp/sequestrada"}, headers=maria
    )
    assert resposta.status_code == 403


def test_espelho_separa_as_pastas_por_pessoa(ambiente):
    cliente, convites, tmp_path = ambiente
    pasta = tmp_path / "Drive"
    pasta.mkdir()
    cliente.post("/api/config", json={"pasta_sincronizada": str(pasta)})  # modo local ainda

    maria = {"X-Convite": convites.criar("Maria Silva")["codigo"]}
    _gerar_e_salvar(cliente, maria)

    assert (pasta / "maria-silva" / "_indice.csv").exists()
    assert not (pasta / "_indice.csv").exists()


def test_revogar_convite_corta_o_acesso_e_preserva_o_banco(ambiente):
    cliente, convites, _ = ambiente
    convite = convites.criar("Maria Silva")
    maria = {"X-Convite": convite["codigo"]}
    _gerar_e_salvar(cliente, maria)

    convites.remover(convite["codigo"])
    assert cliente.get("/api/estado", headers=maria).status_code == 401

    # reemitir para a mesma pessoa devolve o banco dela
    novo = {"X-Convite": convites.criar("Maria Silva")["codigo"]}
    assert len(cliente.get("/api/banco", headers=novo).json()) == 1
