import pytest
from pydantic import ValidationError

from questoes.especificacao import carregar_habilidades

from questoes.especificacao import (
    Dificuldade,
    Especificacao,
    Formato,
    Natureza,
    NivelBloom,
    Tema,
    carregar_habilidades,
)


def _spec(**kw):
    base = dict(
        tema=Tema.FUNCAO_QUADRATICA,
        habilidade_bncc="EM13MAT302",
        nivel_bloom=NivelBloom.APLICAR,
        dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.APLICADA,
        formato=Formato.MULTIPLA_ESCOLHA,
    )
    base.update(kw)
    return Especificacao(**base)


def test_especificacao_valida():
    spec = _spec()
    assert spec.descricao_habilidade().startswith("Construir modelos")


def test_codigo_bncc_invalido_rejeitado():
    with pytest.raises(ValidationError, match="Habilidade BNCC desconhecida"):
        _spec(habilidade_bncc="EM13MAT999")


def test_catalogo_tem_recorte_completo():
    catalogo = carregar_habilidades()
    assert {"EM13MAT302", "EM13MAT507", "EM13MAT508"} <= set(catalogo)


def test_tema_incompativel_com_a_habilidade_e_recusado():
    """Pedido incoerente falha em milissegundos, não depois de três iterações.

    PG com uma habilidade de PA passava pela validação e só era barrado pelo
    Crítico Didático — ao custo de ~5 minutos e seis chamadas ao LLM.
    """
    with pytest.raises(ValidationError) as erro:
        Especificacao(
            tema=Tema.PROGRESSAO_GEOMETRICA, habilidade_bncc="EM13MAT507",
            nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
            natureza=Natureza.TEORICA, formato=Formato.DISCURSIVA,
        )
    mensagem = str(erro.value)
    assert "EM13MAT507" in mensagem
    assert "EM13MAT508" in mensagem  # sugere a habilidade certa para o tema


def test_todo_tema_tem_ao_menos_uma_habilidade():
    """Senão a validação nova tornaria um tema inteiro inalcançável."""
    habilidades = carregar_habilidades()
    for tema in Tema:
        assert any(tema.value in h["temas"] for h in habilidades.values()), tema
