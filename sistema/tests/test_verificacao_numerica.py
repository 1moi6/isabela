from questoes.modelos import Veredicto
from questoes.verificacao.numerica import equivalentes


def test_identidade_confirmada_com_ressalva():
    r = equivalentes("(x**2 - 1)/(x - 1)", "x + 1")
    assert r.veredicto == Veredicto.APROVADO_RESSALVA_NUMERICA


def test_expressoes_diferentes_rejeitadas():
    r = equivalentes("x + 1", "x + 2")
    assert r.veredicto == Veredicto.REJEITADO


def test_identidade_trigonometrica():
    r = equivalentes("sin(x)**2 + cos(x)**2", "1")
    assert r.veredicto == Veredicto.APROVADO_RESSALVA_NUMERICA
