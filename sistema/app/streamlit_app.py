"""Interface web do professor (Streamlit).

Executar a partir de sistema/:
    streamlit run app/streamlit_app.py

Configuração do LLM por variáveis de ambiente:
    QUESTOES_PROVEDOR = anthropic | openai | ollama   (padrão: anthropic)
    QUESTOES_MODELO   = nome do modelo (opcional; usa o padrão do provedor)
    + a chave do provedor escolhido (ANTHROPIC_API_KEY / OPENAI_API_KEY)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import streamlit as st

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

from questoes.agentes import CriticoDidatico, Gerador, Orquestrador, VerificadorSimbolico  # noqa: E402
from questoes.banco import BancoQuestoes  # noqa: E402
from questoes.especificacao import (  # noqa: E402
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema, carregar_habilidades,
)
from questoes.listas import para_latex, para_markdown  # noqa: E402
from questoes.llm import criar_provedor  # noqa: E402

st.set_page_config(page_title="Gerador de Questões — Matemática EM", layout="wide")

BANCO_PATH = RAIZ / "banco_questoes.db"
LOG_DIR = RAIZ / "logs"

ROTULO_TEMA = {
    Tema.FUNCAO_AFIM: "Função afim",
    Tema.FUNCAO_QUADRATICA: "Função quadrática",
    Tema.FUNCAO_EXPONENCIAL: "Função exponencial",
    Tema.PROGRESSAO_ARITMETICA: "Progressão aritmética (PA)",
    Tema.PROGRESSAO_GEOMETRICA: "Progressão geométrica (PG)",
}


@st.cache_resource
def _banco() -> BancoQuestoes:
    return BancoQuestoes(BANCO_PATH)


def _config_llm() -> dict:
    """Painel de configuração do LLM na barra lateral.

    A chave digitada vive apenas na sessão do navegador (st.session_state);
    não é gravada em disco. Variáveis de ambiente funcionam como padrão.
    """
    with st.sidebar:
        st.header("⚙️ Configuração do LLM")
        provedores = ["anthropic", "openai", "ollama"]
        padrao = os.environ.get("QUESTOES_PROVEDOR", "anthropic")
        provedor = st.selectbox(
            "Provedor",
            provedores,
            index=provedores.index(padrao) if padrao in provedores else 0,
            help="Anthropic/OpenAI exigem chave de API. Ollama roda modelos abertos localmente, sem chave.",
        )
        modelo = st.text_input(
            "Modelo (opcional)",
            value=os.environ.get("QUESTOES_MODELO", ""),
            placeholder={"anthropic": "claude-sonnet-5", "openai": "gpt-4o-mini", "ollama": "qwen2.5:14b"}[provedor],
            help="Vazio = modelo padrão do provedor.",
        )
        api_key, url = None, None
        if provedor in ("anthropic", "openai"):
            var = "ANTHROPIC_API_KEY" if provedor == "anthropic" else "OPENAI_API_KEY"
            api_key = st.text_input(
                "Chave de API",
                type="password",
                value="",
                help=f"Fica apenas nesta sessão do navegador. Se vazia, usa a variável de ambiente {var}.",
            ) or None
            if api_key is None and not os.environ.get(var):
                st.warning(f"Informe a chave acima ou defina {var} no ambiente.")
        else:
            url = st.text_input("URL do Ollama", value="http://localhost:11434")
        return {"nome": provedor, "modelo": modelo or None, "api_key": api_key, "url": url}


def _orquestrador(cfg: dict) -> Orquestrador:
    provedor = criar_provedor(cfg["nome"], modelo=cfg["modelo"], api_key=cfg["api_key"], url=cfg["url"])
    return Orquestrador(
        Gerador(provedor), VerificadorSimbolico(), CriticoDidatico(provedor), log_dir=LOG_DIR
    )


def _mostrar_questao(q, verificacao=None, parecer=None):
    st.markdown(f"**Enunciado.** {q.enunciado}")
    if q.alternativas:
        for letra, alt in zip("abcd", q.alternativas):
            marca = " ✅" if alt.correta else ""
            st.markdown(f"({letra}) {alt.texto}{marca}")
    with st.expander("Resolução e gabarito"):
        st.markdown(q.resolucao)
        st.markdown(f"**Gabarito:** {q.gabarito}")
    if verificacao is not None:
        st.info(f"**Verificador simbólico:** {verificacao.veredicto.value} — {verificacao.justificativa}")
    if parecer is not None:
        with st.expander("Parecer didático (por critério)"):
            for n in parecer.notas:
                st.markdown(f"- **{n.criterio}**: {n.nota}/5 — {n.comentario}")


st.title("Gerador assistido de questões de Matemática — Ensino Médio")
st.caption(
    "Sistema multiagente (LLM gerador + verificador simbólico SymPy + crítico didático). "
    "Produto educacional — PROFMAT/UFMT."
)

cfg_llm = _config_llm()

aba_gerar, aba_banco, aba_lista = st.tabs(["✏️ Gerar questão", "🗂️ Banco", "📄 Montar lista"])

# ------------------------------------------------------------------ Gerar
with aba_gerar:
    habilidades = carregar_habilidades()
    col1, col2, col3 = st.columns(3)
    with col1:
        tema = st.selectbox("Tema", list(Tema), format_func=lambda t: ROTULO_TEMA[t])
        compativeis = [c for c, h in habilidades.items() if tema.value in h["temas"]] or list(habilidades)
        habilidade = st.selectbox(
            "Habilidade BNCC", compativeis,
            format_func=lambda c: f"{c} — {habilidades[c]['descricao'][:70]}…",
        )
    with col2:
        nivel = st.selectbox("Nível cognitivo (Bloom)", list(NivelBloom), index=2,
                             format_func=lambda n: n.value)
        dificuldade = st.select_slider("Dificuldade", list(Dificuldade),
                                       format_func=lambda d: d.value)
    with col3:
        natureza = st.radio("Natureza", list(Natureza), horizontal=True,
                            format_func=lambda n: "Teórica" if n == Natureza.TEORICA else "Aplicada")
        formato = st.radio("Formato", list(Formato), horizontal=True,
                           format_func=lambda f: "Discursiva" if f == Formato.DISCURSIVA else "Múltipla escolha")
    contexto = st.text_input("Contexto temático (opcional)", placeholder="ex.: esportes, finanças pessoais")
    restricoes = st.text_input("Restrições (opcional)", placeholder="ex.: apenas coeficientes inteiros")

    if st.button("Gerar questão", type="primary"):
        spec = Especificacao(
            tema=tema, habilidade_bncc=habilidade, nivel_bloom=nivel,
            dificuldade=dificuldade, natureza=natureza, formato=formato,
            contexto=contexto or None, restricoes=restricoes or None,
        )
        with st.spinner("Ciclo de geração-verificação-crítica em andamento…"):
            try:
                resultado = _orquestrador(cfg_llm).produzir(spec)
            except Exception as exc:
                st.error(f"Falha no ciclo: {exc}")
                st.stop()
        st.session_state["ultimo_resultado"] = resultado

    resultado = st.session_state.get("ultimo_resultado")
    if resultado is not None:
        st.divider()
        if resultado.aprovada:
            ultima = resultado.iteracoes[-1]
            st.success(f"Questão aprovada em {len(resultado.iteracoes)} iteração(ões).")
            _mostrar_questao(resultado.questao_final, ultima.verificacao, ultima.parecer)
            if st.button("💾 Salvar no banco curado"):
                qid = _banco().salvar(resultado)
                st.session_state.pop("ultimo_resultado")
                st.success(f"Salva como questão #{qid}.")
                st.rerun()
        else:
            st.error(
                f"Questão descartada após {len(resultado.iteracoes)} iterações sem aprovação. "
                "Veja o histórico abaixo e ajuste a especificação."
            )
        with st.expander("Histórico completo de iterações (rastreabilidade)"):
            for it in resultado.iteracoes:
                st.markdown(f"**Iteração {it.numero}** — verificador: `{it.verificacao.veredicto.value}`")
                if it.feedback_para_gerador:
                    st.markdown(f"> feedback: {it.feedback_para_gerador}")

# ------------------------------------------------------------------ Banco
with aba_banco:
    banco = _banco()
    st.metric("Questões no banco curado", banco.total())
    colf1, colf2 = st.columns(2)
    with colf1:
        filtro_tema = st.selectbox("Filtrar por tema", [None] + list(Tema),
                                   format_func=lambda t: "(todos)" if t is None else ROTULO_TEMA[t])
    with colf2:
        filtro_dif = st.selectbox("Filtrar por dificuldade", [None] + list(Dificuldade),
                                  format_func=lambda d: "(todas)" if d is None else d.value)
    achadas = banco.buscar(
        tema=filtro_tema.value if filtro_tema else None,
        dificuldade=filtro_dif.value if filtro_dif else None,
    )
    for qid, q in achadas:
        with st.expander(f"#{qid} · {ROTULO_TEMA[q.especificacao.tema]} · {q.especificacao.dificuldade.value} · {q.enunciado[:80]}…"):
            _mostrar_questao(q)

# ------------------------------------------------------------------ Lista
with aba_lista:
    banco = _banco()
    titulo = st.text_input("Título da lista", value="Lista de exercícios")
    colg1, colg2, colg3 = st.columns(3)
    with colg1:
        lt = st.selectbox("Tema da lista", [None] + list(Tema), key="lt",
                          format_func=lambda t: "(todos)" if t is None else ROTULO_TEMA[t])
    with colg2:
        ld = st.selectbox("Dificuldade", [None] + list(Dificuldade), key="ld",
                          format_func=lambda d: "(todas)" if d is None else d.value)
    with colg3:
        n = st.number_input("Quantidade de questões", min_value=1, max_value=30, value=5)
    com_gabarito = st.toggle("Incluir gabarito e resoluções (versão do professor)", value=False)

    selecionadas = banco.buscar(
        tema=lt.value if lt else None, dificuldade=ld.value if ld else None, limite=int(n)
    )
    st.caption(f"{len(selecionadas)} questão(ões) atendem aos filtros.")
    if selecionadas:
        questoes = [q for _, q in selecionadas]
        md = para_markdown(titulo, questoes, com_gabarito=com_gabarito)
        tex = para_latex(titulo, questoes, com_gabarito=com_gabarito)
        st.download_button("⬇️ Baixar Markdown", md, file_name="lista.md")
        st.download_button("⬇️ Baixar LaTeX (compilar com pdflatex)", tex, file_name="lista.tex")
        with st.expander("Pré-visualização (Markdown)"):
            st.markdown(md)
