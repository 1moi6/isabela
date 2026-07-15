from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar


def _ev(expressao, resposta, **params):
    return ExpressaoVerificavel(
        tipo="equacao", expressao=expressao, resposta_esperada=resposta, parametros=params
    )


def test_quadratica_gabarito_correto():
    r = verificar(_ev("Eq(2*x**2 - 5*x + 3, 0)", "[1, Rational(3,2)]"))
    assert r.veredicto == Veredicto.APROVADO


def test_quadratica_gabarito_errado_e_rejeitado():
    r = verificar(_ev("Eq(2*x**2 - 5*x + 3, 0)", "[1, 2]"))
    assert r.veredicto == Veredicto.REJEITADO
    assert "Divergência" in r.justificativa


def test_gabarito_incompleto_e_rejeitado():
    # gabarito com só uma das duas raízes: erro clássico de LLM
    r = verificar(_ev("Eq(x**2 - 4, 0)", "[2]"))
    assert r.veredicto == Veredicto.REJEITADO


def test_afim_com_raiz_fracionaria():
    r = verificar(_ev("Eq(3*x + 2, 0)", "[Rational(-2,3)]"))
    assert r.veredicto == Veredicto.APROVADO


def test_solucao_irracional_comparada_simbolicamente():
    # sqrt(2) deve casar simbolicamente, não numericamente
    r = verificar(_ev("Eq(x**2 - 2, 0)", "[sqrt(2), -sqrt(2)]"))
    assert r.veredicto == Veredicto.APROVADO


def test_expressao_malformada_vira_nao_verificavel():
    r = verificar(_ev("Eq(2*x** - , 0)", "[1]"))
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL


def test_tipo_desconhecido_vira_nao_verificavel():
    ev = ExpressaoVerificavel(tipo="geometria", expressao="x", resposta_esperada="1")
    r = verificar(ev)
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL
