from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar


def _ev(resposta, **params):
    return ExpressaoVerificavel(
        tipo="progressao", expressao="-", resposta_esperada=resposta, parametros=params
    )


def test_termo_geral_pa():
    # PA: a1=2, r=3 -> a10 = 2 + 9*3 = 29
    r = verificar(_ev("29", tipo_progressao="pa", a1="2", razao="3", n="10", consulta="termo"))
    assert r.veredicto == Veredicto.APROVADO


def test_soma_pa():
    # S10 da PA(2, 5, 8, ...) = 10*(2*2 + 9*3)/2 = 155
    r = verificar(_ev("155", tipo_progressao="pa", a1="2", razao="3", n="10", consulta="soma"))
    assert r.veredicto == Veredicto.APROVADO


def test_termo_geral_pg():
    # PG: a1=3, q=2 -> a6 = 3*2^5 = 96
    r = verificar(_ev("96", tipo_progressao="pg", a1="3", razao="2", n="6", consulta="termo"))
    assert r.veredicto == Veredicto.APROVADO


def test_soma_pg():
    # S5 da PG(1, 2, 4, ...) = (2^5 - 1)/(2-1) = 31
    r = verificar(_ev("31", tipo_progressao="pg", a1="1", razao="2", n="5", consulta="soma"))
    assert r.veredicto == Veredicto.APROVADO


def test_soma_pg_razao_um_caso_degenerado():
    r = verificar(_ev("35", tipo_progressao="pg", a1="7", razao="1", n="5", consulta="soma"))
    assert r.veredicto == Veredicto.APROVADO


def test_gabarito_errado_rejeitado():
    r = verificar(_ev("30", tipo_progressao="pa", a1="2", razao="3", n="10", consulta="termo"))
    assert r.veredicto == Veredicto.REJEITADO
