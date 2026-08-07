"""Tolerância a tipos na fronteira com o LLM.

O Gerador devolve JSON, e em JSON número é número: `{"ponto": -2}` é tão provável
quanto `{"ponto": "-2"}`. O contrato de dados aceita as duas formas e normaliza
para texto, que é o que o núcleo simbólico consome.
"""

import pytest
from pydantic import ValidationError

from questoes.especificacao import (
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema,
)
from questoes.modelos import ExpressaoVerificavel, Questao
from questoes.verificacao import verificar


def _spec():
    return Especificacao(
        habilidade_bncc="EM13MAT507",
        temas=[Tema.PROGRESSAO_ARITMETICA, Tema.FUNCAO_AFIM],
        nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.TEORICA, formato=Formato.DISCURSIVA,
    )


def test_parametro_numerico_vira_texto():
    ev = ExpressaoVerificavel(
        tipo="funcao", expressao="x**2 - 4", resposta_esperada="0",
        parametros={"consulta": "valor", "ponto": -2},
    )
    assert ev.parametros["ponto"] == "-2"


def test_expressao_e_resposta_numericas_viram_texto():
    ev = ExpressaoVerificavel(tipo="equacao", expressao=42, resposta_esperada=-1.5)
    assert (ev.expressao, ev.resposta_esperada) == ("42", "-1.5")


def test_gabarito_numerico_vira_texto():
    q = Questao(
        enunciado="Quanto é 2 + 3?", resolucao="2 + 3 = 5", gabarito=5,
        especificacao=_spec(),
    )
    assert q.gabarito == "5"


def test_booleano_continua_recusado():
    """`True` não é expressão matemática — coerção aqui esconderia erro do Gerador."""
    with pytest.raises(ValidationError):
        ExpressaoVerificavel(tipo="equacao", expressao="x - 1", resposta_esperada=True)


def test_verificacao_funciona_com_parametros_numericos():
    """O caso que quebrou o ciclo: PA com a1, razao e n como números."""
    ev = ExpressaoVerificavel(
        tipo="progressao", expressao="a_n = a_1 + (n-1)*r", resposta_esperada="29",
        parametros={"tipo_progressao": "pa", "a1": 2, "razao": 3, "n": 10, "consulta": "termo"},
    )
    assert verificar(ev).veredicto.value == "aprovado"
