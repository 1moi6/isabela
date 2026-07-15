from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar


def _ev(expressao, resposta, **params):
    return ExpressaoVerificavel(
        tipo="funcao", expressao=expressao, resposta_esperada=resposta, parametros=params
    )


def test_zeros_quadratica():
    r = verificar(_ev("x**2 - 5*x + 6", "[2, 3]", consulta="zeros"))
    assert r.veredicto == Veredicto.APROVADO


def test_vertice_quadratica():
    # f(x) = x^2 - 4x + 1 -> vértice (2, -3)
    r = verificar(_ev("x**2 - 4*x + 1", "[2, -3]", consulta="vertice"))
    assert r.veredicto == Veredicto.APROVADO


def test_vertice_errado_rejeitado():
    r = verificar(_ev("x**2 - 4*x + 1", "[2, 3]", consulta="vertice"))
    assert r.veredicto == Veredicto.REJEITADO


def test_valor_em_ponto():
    r = verificar(_ev("2*x + 1", "7", consulta="valor", ponto="3"))
    assert r.veredicto == Veredicto.APROVADO


def test_minimo_da_parabola():
    r = verificar(_ev("x**2 - 4*x + 1", "-3", consulta="minimo"))
    assert r.veredicto == Veredicto.APROVADO


def test_extremo_de_funcao_afim_nao_verificavel():
    r = verificar(_ev("2*x + 1", "0", consulta="minimo"))
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL
