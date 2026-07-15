import pytest
from pydantic import ValidationError

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
