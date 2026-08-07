"""API HTTP do gerador de questões (interface descrita no Capítulo 7 da dissertação).

A interface do professor é uma página web servida por este mesmo processo: não
há segundo servidor, não há passo de compilação, e o navegador conversa apenas
com `localhost`. A API é fina de propósito — toda a política de decisão continua
no Orquestrador, e todo o cálculo continua no núcleo simbólico.

Uma chamada a `/api/gerar` produz **uma** questão. A geração em lote é o cliente
repetindo a chamada: assim o professor vê cada questão chegar em vez de esperar
um bloco só, e nenhuma requisição fica pendurada por minutos.
"""

from __future__ import annotations

import os
import secrets
import sys
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid4

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

from fastapi import Body, Depends, FastAPI, Header, HTTPException, Request  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware  # noqa: E402
from fastapi.responses import Response  # noqa: E402
from fastapi.staticfiles import StaticFiles  # noqa: E402
from pydantic import BaseModel  # noqa: E402

from questoes import config_app  # noqa: E402
from questoes.agentes import (  # noqa: E402
    CriticoDidatico, Gerador, Orquestrador, VerificadorSimbolico,
)
from questoes.banco import BancoQuestoes  # noqa: E402
from questoes.convites import DONO_LOCAL, Convites  # noqa: E402
from questoes.especificacao import (  # noqa: E402
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema, carregar_habilidades,
)
from questoes.listas import para_docx, para_latex, para_markdown  # noqa: E402
from questoes.llm import criar_provedor  # noqa: E402
from questoes.modelos import AvaliacaoProfessor, ResultadoCiclo  # noqa: E402
from questoes.sincronizacao import PastaSincronizada  # noqa: E402

# A interface vive em `docs/` na raiz do repositório, não dentro de `sistema/`:
# é a pasta que o GitHub Pages publica. Assim existe uma cópia só, servida de
# dois jeitos — por este processo no uso local, e pelo Pages no uso remoto.
WEB = RAIZ.parent / "docs"
BANCO_PATH = RAIZ / "banco_questoes.db"
LOG_DIR = RAIZ / "logs"

ROTULO_TEMA = {
    "funcao_afim": "Função afim",
    "funcao_quadratica": "Função quadrática",
    "funcao_exponencial": "Função exponencial",
    "progressao_aritmetica": "Progressão aritmética (PA)",
    "progressao_geometrica": "Progressão geométrica (PG)",
}
ROTULO_NATUREZA = {"teorica": "Teórica", "aplicada": "Aplicada"}
ROTULO_FORMATO = {"discursiva": "Discursiva", "multipla_escolha": "Múltipla escolha"}
ROTULO_DIFICULDADE = {"facil": "Fácil", "media": "Média", "dificil": "Difícil"}
ROTULO_DECISAO = {
    "aceita": "Aceita",
    "aceita_com_ajuste": "Aceita com ajuste",
    "recusada": "Recusada",
}

VARIAVEL_CHAVE = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY"}

app = FastAPI(title="Gerador de questões de Matemática", docs_url=None, redoc_url=None)
_banco = BancoQuestoes(BANCO_PATH)
_convites = Convites()

# Quando a interface é servida pelo GitHub Pages, o navegador trata a API como
# outra origem e exige CORS. A lista vem da configuração e é vazia por padrão:
# liberar tudo permitiria que qualquer site chamasse esta API com um convite
# vazado. Só as origens que o dono declarar entram.
_origens = [
    o.strip() for o in config_app.carregar()["origens_permitidas"].split(",") if o.strip()
]
if _origens:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=_origens,
        allow_methods=["GET", "POST", "DELETE"],
        allow_headers=["Content-Type", "X-Convite", "X-Chave-API", "X-Provedor", "X-Chave-Admin"],
        expose_headers=["Content-Disposition"],  # a interface lê o nome do arquivo da lista
    )


# ------------------------------------------------------- quem está chamando
def identificar(
    x_convite: str | None = Header(default=None),
    x_chave_api: str | None = Header(default=None),
    x_provedor: str | None = Header(default=None),
) -> dict:
    """Identifica o chamador e recolhe as credenciais que vieram com a requisição.

    A chave de API **viaja em cada requisição** e é usada e descartada: o servidor
    não guarda credencial de ninguém. Antes isto era uma variável global do
    processo, o que, com duas pessoas usando ao mesmo tempo, fazia a segunda
    chave sobrescrever a primeira --- e as requisições de uma serem cobradas da
    outra, sem erro visível.

    Sem convites cadastrados o sistema roda em modo local, sem autenticação.
    """
    if not _convites.modo_compartilhado:
        quem = {"dono": DONO_LOCAL, "nome": "", "compartilhado": False}
    else:
        convite = _convites.identificar(x_convite)
        if convite is None:
            raise HTTPException(
                status_code=401,
                detail="Convite inválido ou ausente. Peça um link de acesso a quem administra.",
            )
        quem = {
            "dono": convite["identificador"],
            "nome": convite["nome"],
            "compartilhado": True,
        }
    return {**quem, "chave": x_chave_api or None, "provedor": x_provedor or None}


def exigir_admin(x_chave_admin: str | None = Header(default=None)) -> None:
    """Portaria da página de convites.

    A senha é sempre exigida, inclusive em modo local: quem administra convites
    pode criar acesso ao sistema, e isso não deve depender de o servidor estar
    ou não compartilhado no momento. Sem senha configurada, os endpoints ficam
    fechados --- é mais seguro impedir do que abrir por omissão.
    """
    esperada = config_app.carregar()["chave_admin"]
    if not esperada:
        raise HTTPException(
            status_code=403,
            detail="Nenhuma senha de administração configurada. "
                   "Defina-a com: python gerenciar_convites.py senha",
        )
    # compare_digest: a comparação comum vaza o tamanho do prefixo correto pelo
    # tempo de resposta, o que permite descobrir a senha caractere a caractere.
    if not x_chave_admin or not secrets.compare_digest(x_chave_admin, esperada):
        raise HTTPException(status_code=401, detail="Senha de administração incorreta.")


# --------------------------------------------------------------------- infra
def _pasta(dono: str = DONO_LOCAL) -> PastaSincronizada:
    """Pasta do espelho. Em modo compartilhado, cada pessoa tem a sua subpasta."""
    raiz = config_app.carregar()["pasta_sincronizada"]
    if not raiz or dono == DONO_LOCAL:
        return PastaSincronizada(raiz)
    pasta = PastaSincronizada(Path(raiz).expanduser() / dono)
    if pasta.pasta.parent.is_dir():
        pasta.pasta.mkdir(exist_ok=True)
    return pasta


def _sincronizar(dono: str, questao_id: int | None = None) -> str | None:
    """Exporta a questão indicada e regrava o índice. Silencioso se não configurado.

    A sincronização é um espelho: falhar aqui não pode impedir o professor de
    salvar no banco, então o erro volta como aviso e não como exceção.
    """
    pasta = _pasta(dono)
    if not pasta.configurada:
        return None
    try:
        if questao_id is not None:
            resultado, avaliacao = _banco.obter(questao_id, dono=dono)
            pasta.exportar(questao_id, resultado, avaliacao)
        pasta.regravar_indice(_banco.registros(dono=dono))
        return None
    except (OSError, ValueError) as exc:
        return str(exc)


def _orquestrador(quem: dict, url: str | None, ao_progredir=None) -> Orquestrador:
    """Monta o ciclo com o provedor e a chave que vieram na requisição."""
    cfg = config_app.carregar()
    provedor = criar_provedor(
        quem["provedor"] or cfg["provedor"],
        modelo=cfg["modelo"] or None,
        api_key=quem["chave"],
        url=url or None,
    )
    return Orquestrador(
        Gerador(provedor), VerificadorSimbolico(), CriticoDidatico(provedor),
        log_dir=LOG_DIR, ao_progredir=ao_progredir,
    )


# ------------------------------------------------------------------ opções
@app.get("/api/opcoes")
def opcoes() -> dict:
    """Tudo que o formulário precisa para se montar: enums rotulados e o catálogo BNCC."""
    habilidades = carregar_habilidades()
    return {
        "temas": [{"valor": t.value, "rotulo": ROTULO_TEMA[t.value]} for t in Tema],
        "bloom": [{"valor": n.value, "rotulo": n.value.capitalize()} for n in NivelBloom],
        "dificuldades": [
            {"valor": d.value, "rotulo": ROTULO_DIFICULDADE[d.value]} for d in Dificuldade
        ],
        "naturezas": [{"valor": n.value, "rotulo": ROTULO_NATUREZA[n.value]} for n in Natureza],
        "formatos": [{"valor": f.value, "rotulo": ROTULO_FORMATO[f.value]} for f in Formato],
        "decisoes": [{"valor": v, "rotulo": r} for v, r in ROTULO_DECISAO.items()],
        # O formulário monta os temas a partir da habilidade escolhida, e não o
        # contrário: por isso cada habilidade carrega seus temas, como eles se
        # combinam, o que a questão precisa cumprir e que níveis de Bloom os
        # verbos dela sugerem.
        "habilidades": [
            {
                "codigo": c,
                "descricao": h["descricao"],
                "temas": h["temas"],
                "relacao_temas": h["relacao_temas"],
                "bloom_sugerido": h["bloom_sugerido"],
                "exigencias": h["exigencias"],
            }
            for c, h in sorted(habilidades.items())
        ],
    }


@app.get("/api/identificacao")
def identificacao() -> dict:
    """Quem mantém este servidor. **Aberto de propósito**, sem exigir convite.

    É a informação que a pessoa precisa *antes* de decidir se confia: ela verá
    esta tela justamente quando ainda não tem acesso, e vai digitar a própria
    chave de API aqui. Um endereço anônimo pedindo credencial é indistinguível
    de golpe --- e com razão.
    """
    cfg = config_app.carregar()
    return {
        "responsavel": cfg["responsavel"],
        "instituicao": cfg["instituicao"],
        "contato": cfg["contato"],
    }


@app.get("/api/estado")
def estado(quem: dict = Depends(identificar)) -> dict:
    """Situação do aplicativo: banco, credencial e pasta sincronizada."""
    cfg = config_app.carregar()
    provedor = quem["provedor"] or cfg["provedor"]
    variavel = VARIAVEL_CHAVE.get(provedor)
    pasta = _pasta(quem["dono"])
    # Em modo compartilhado a chave vem do navegador de cada pessoa; a variável
    # de ambiente do servidor só vale para o uso local.
    chave_do_ambiente = bool(variavel and os.environ.get(variavel))
    return {
        "total_no_banco": _banco.total(dono=quem["dono"]),
        "provedor": provedor,
        "modelo": cfg["modelo"],
        "chave_presente": bool(quem["chave"]) or (not quem["compartilhado"] and chave_do_ambiente),
        "variavel_chave": variavel,
        "pasta_sincronizada": str(pasta.pasta) if pasta.configurada else "",
        "pasta_acessivel": pasta.configurada and pasta.pasta.is_dir(),
        "compartilhado": quem["compartilhado"],
        "nome": quem["nome"],
    }


class Configuracao(BaseModel):
    pasta_sincronizada: str | None = None
    provedor: str | None = None
    modelo: str | None = None
    responsavel: str | None = None
    instituicao: str | None = None
    contato: str | None = None


@app.post("/api/config")
def salvar_config(cfg: Configuracao, quem: dict = Depends(identificar)) -> dict:
    """Grava as preferências do servidor.

    Só no modo local. Estas preferências (pasta sincronizada, provedor padrão)
    são da máquina, não de quem está conectado: deixar um convidado alterá-las
    seria deixá-lo redirecionar o espelho do dono para outro lugar.
    """
    if quem["compartilhado"]:
        raise HTTPException(
            status_code=403,
            detail="As configurações do servidor só podem ser alteradas na máquina onde ele roda.",
        )
    gravaveis = {c: v for c, v in cfg.model_dump().items() if v is not None}
    if gravaveis:
        config_app.salvar(gravaveis)
    return estado(quem)


# ------------------------------------------------------------------ geração
class PedidoGeracao(BaseModel):
    habilidade_bncc: str
    # `tema` no singular continua aceito: a Especificação converte. Assim um
    # cliente antigo (ou um script da aluna) não quebra com a multisseleção.
    temas: list[Tema] | None = None
    tema: Tema | None = None
    nivel_bloom: NivelBloom
    dificuldade: Dificuldade
    natureza: Natureza
    formato: Formato
    contexto: str | None = None
    restricoes: str | None = None
    url_ollama: str | None = None


# ------------------------------------------------------ tarefas de geração
# Um ciclo real leva de 80 a 250 segundos. Proxies reversos derrubam requisições
# muito mais cedo que isso (a Cloudflare corta em 100s), e a falha cairia
# justamente nas questões que precisam de revisão --- as mais interessantes.
# Por isso a geração vira tarefa: o pedido volta na hora com um identificador e
# a interface pergunta o andamento. Cada requisição dura milissegundos.
_tarefas: dict[str, dict] = {}
_trava_tarefas = threading.Lock()
RETENCAO_TAREFAS = timedelta(hours=1)


def _limpar_tarefas() -> None:
    limite = datetime.now(timezone.utc) - RETENCAO_TAREFAS
    for chave in [c for c, t in _tarefas.items() if t["criada_em"] < limite]:
        del _tarefas[chave]


def _executar_ciclo(tarefa_id: str, spec: Especificacao, quem: dict, url: str | None) -> None:
    def progresso(evento: dict) -> None:
        with _trava_tarefas:
            if tarefa_id in _tarefas:
                _tarefas[tarefa_id]["progresso"] = evento

    try:
        orq = _orquestrador(quem, url, ao_progredir=progresso)
        resultado = orq.produzir(spec)
        with _trava_tarefas:
            _tarefas[tarefa_id].update(estado="concluida", resultado=resultado)
    except ModuleNotFoundError as exc:
        with _trava_tarefas:
            _tarefas[tarefa_id].update(
                estado="erro",
                detalhe=f"Falta instalar a biblioteca do provedor ({exc.name}).",
            )
    except Exception as exc:
        with _trava_tarefas:
            _tarefas[tarefa_id].update(estado="erro", detalhe=f"{type(exc).__name__}: {exc}")


@app.post("/api/gerar")
def gerar(pedido: PedidoGeracao, quem: dict = Depends(identificar)) -> dict:
    """Inicia um ciclo e devolve o identificador para acompanhar."""
    campos = pedido.model_dump(exclude={"url_ollama", "tema", "temas"})
    temas = pedido.temas or ([pedido.tema] if pedido.tema else [])
    if not temas:
        raise HTTPException(status_code=422, detail="Escolha ao menos um tema da habilidade.")
    try:
        spec = Especificacao(**campos, temas=temas)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    tarefa_id = uuid4().hex
    with _trava_tarefas:
        _limpar_tarefas()
        _tarefas[tarefa_id] = {
            "dono": quem["dono"],
            "estado": "executando",
            "progresso": {"iteracao": 1, "etapa": "gerando"},
            "resultado": None,
            "detalhe": None,
            "criada_em": datetime.now(timezone.utc),
        }

    threading.Thread(
        target=_executar_ciclo, args=(tarefa_id, spec, quem, pedido.url_ollama), daemon=True
    ).start()
    return {"tarefa": tarefa_id}


@app.get("/api/gerar/{tarefa_id}")
def acompanhar(tarefa_id: str, quem: dict = Depends(identificar)) -> dict:
    """Andamento da tarefa. O resultado vem junto quando ela termina."""
    with _trava_tarefas:
        tarefa = _tarefas.get(tarefa_id)
        if tarefa is None or tarefa["dono"] != quem["dono"]:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
        # A tarefa **não** é apagada ao ser lida. GET precisa ser idempotente:
        # proxies repetem requisições, e apagar na primeira leitura faria a
        # segunda devolver 404 --- perdendo um ciclo já concluído e pago. A
        # limpeza é por tempo (RETENCAO_TAREFAS), na criação da próxima.
        return {
            "estado": tarefa["estado"],
            "progresso": tarefa["progresso"],
            "detalhe": tarefa["detalhe"],
            "resultado": tarefa["resultado"],
        }


# -------------------------------------------------------------------- banco
@app.post("/api/banco")
def salvar_no_banco(resultado: ResultadoCiclo, quem: dict = Depends(identificar)) -> dict:
    """Guarda o ciclo aprovado e espelha na pasta sincronizada."""
    try:
        questao_id = _banco.salvar(resultado, dono=quem["dono"])
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {
        "id": questao_id,
        "aviso_sincronizacao": _sincronizar(quem["dono"], questao_id),
    }


@app.get("/api/banco")
def listar_banco(
    tema: str | None = None,
    dificuldade: str | None = None,
    quem: dict = Depends(identificar),
) -> list[dict]:
    """Questões curadas de quem está conectado, da mais recente para a mais antiga."""
    registros = []
    for reg in reversed(_banco.registros(dono=quem["dono"])):
        # Basta ser um dos temas: uma questão que articula PA e função afim
        # aparece no filtro de qualquer um dos dois.
        if tema and tema not in reg["temas"]:
            continue
        if dificuldade and reg["dificuldade"] != dificuldade:
            continue
        questao = reg.pop("questao")
        registros.append({**reg, "questao": questao.model_dump(mode="json")})
    return registros


@app.post("/api/banco/{questao_id}/avaliacao")
def avaliar(
    questao_id: int, avaliacao: AvaliacaoProfessor, quem: dict = Depends(identificar)
) -> dict:
    """Registra o julgamento do professor e atualiza o espelho na nuvem."""
    try:
        _banco.avaliar(questao_id, avaliacao, dono=quem["dono"])
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {
        "id": questao_id,
        "aviso_sincronizacao": _sincronizar(quem["dono"], questao_id),
    }


# ---------------------------------------------------------------- convites
class PedidoConvite(BaseModel):
    nome: str


def _link(codigo: str, cfg: dict, origem: str = "") -> str:
    """Link pronto para enviar.

    Com `endereco_frontend` configurado, a interface está publicada noutro lugar
    (o GitHub Pages) e é para lá que o link aponta. Sem ele, quem serve a
    interface é este mesmo processo — então o endereço certo é o da própria
    requisição, e não um caminho solto que ninguém consegue abrir.
    """
    base = cfg["endereco_frontend"].rstrip("/") or origem.rstrip("/")
    return f"{base}/?convite={codigo}" if base else f"?convite={codigo}"


@app.get("/api/convites", dependencies=[Depends(exigir_admin)])
def listar_convites(request: Request) -> dict:
    cfg = config_app.carregar()
    origem = str(request.base_url)
    return {
        "convites": [
            {**c, "link": _link(c["codigo"], cfg, origem)} for c in _convites.listar()
        ],
        "publicacao_automatica": bool(cfg["repositorio_frontend"]) or bool(cfg["endereco_api"]),
    }


@app.post("/api/convites", dependencies=[Depends(exigir_admin)])
def criar_convite(pedido: PedidoConvite, request: Request) -> dict:
    """Cria um convite. Nomes iguais compartilham o mesmo banco, de propósito."""
    nome = pedido.nome.strip()
    if not nome:
        raise HTTPException(status_code=422, detail="Informe o nome da pessoa.")
    convite = _convites.criar(nome)
    return {**convite, "link": _link(convite["codigo"], config_app.carregar(), str(request.base_url))}


@app.delete("/api/convites/{codigo}", dependencies=[Depends(exigir_admin)])
def remover_convite(codigo: str) -> dict:
    """Revoga o acesso. O banco da pessoa continua guardado."""
    if not _convites.remover(codigo):
        raise HTTPException(status_code=404, detail="Convite não encontrado.")
    return {"removido": codigo}


# -------------------------------------------------------------------- lista
class PedidoLista(BaseModel):
    titulo: str = "Lista de exercícios"
    ids: list[int] = []
    com_gabarito: bool = False
    formato_arquivo: str = "markdown"  # markdown | latex | docx


_TIPOS = {
    "markdown": ("text/markdown; charset=utf-8", "md"),
    "latex": ("application/x-tex; charset=utf-8", "tex"),
    "docx": (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "docx"
    ),
}


@app.post("/api/lista")
def montar_lista(
    pedido: PedidoLista = Body(...), quem: dict = Depends(identificar)
) -> Response:
    """Monta a lista com as questões escolhidas e devolve o arquivo."""
    if pedido.formato_arquivo not in _TIPOS:
        raise HTTPException(status_code=422, detail=f"Formato desconhecido: {pedido.formato_arquivo}")
    if not pedido.ids:
        raise HTTPException(status_code=422, detail="Escolha ao menos uma questão para a lista.")

    por_id = {reg["id"]: reg["questao"] for reg in _banco.registros(dono=quem["dono"])}
    faltando = [i for i in pedido.ids if i not in por_id]
    if faltando:
        raise HTTPException(status_code=404, detail=f"Questões não encontradas: {faltando}")
    questoes = [por_id[i] for i in pedido.ids]  # respeita a ordem escolhida

    tipo, extensao = _TIPOS[pedido.formato_arquivo]
    if pedido.formato_arquivo == "docx":
        try:
            corpo: bytes = para_docx(pedido.titulo, questoes, pedido.com_gabarito)
        except ModuleNotFoundError as exc:
            raise HTTPException(
                status_code=503,
                detail="Falta instalar a biblioteca python-docx para exportar em Word.",
            ) from exc
    else:
        gerar_texto = para_markdown if pedido.formato_arquivo == "markdown" else para_latex
        corpo = gerar_texto(pedido.titulo, questoes, pedido.com_gabarito).encode("utf-8")

    sufixo = "professor" if pedido.com_gabarito else "aluno"
    return Response(
        content=corpo,
        media_type=tipo,
        headers={"Content-Disposition": f'attachment; filename="lista-{sufixo}.{extensao}"'},
    )


# ----------------------------------------------------------------- interface
# Montado na raiz e por último: as rotas /api/* acima têm precedência, e os
# arquivos ficam acessíveis por caminho relativo (app.css, app.js) — os mesmos
# que o GitHub Pages usa, o que permite uma cópia só da interface.
app.mount("/", StaticFiles(directory=WEB, html=True), name="interface")
