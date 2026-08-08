"""As três últimas famílias de reprovação falsa, achadas no acervo consolidado.

Todas do mesmo tipo das anteriores: o verificador reprovando gabarito correto.
A diferença é que estas só apareceram depois de corrigidas as primeiras — cada
rodada de geração com provedor real revela a camada seguinte.

O que NÃO pode acontecer: afrouxar a ponto de deixar passar erro. Cada teste
aqui tem o seu par negativo.
"""

from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar


def _eq(expressao, resposta, incognita="x", **parametros):
    return verificar(ExpressaoVerificavel(
        tipo="equacao", expressao=expressao, incognitas=[incognita],
        resposta_esperada=resposta, parametros=parametros,
    ))


def _fn(expressao, consulta, resposta, incognita="x", **parametros):
    return verificar(ExpressaoVerificavel(
        tipo="funcao", expressao=expressao, incognitas=[incognita],
        resposta_esperada=resposta, parametros={"consulta": consulta, **parametros},
    ))


# ---------------------------------------------- raízes complexas x raízes reais
def test_sem_raizes_reais_e_resposta_valida():
    """x² - 8x + 20 tem discriminante -16. `solve` devolve [4-2i, 4+2i]."""
    assert _eq("Eq(x**2 - 8*x + 20, 0)", "[]").veredicto == Veredicto.APROVADO
    assert _fn("x**2 - 8*x + 20", "zeros", "[]").veredicto == Veredicto.APROVADO


def test_apenas_a_raiz_real_de_uma_cubica():
    """(1+i)³ = 1,331 tem três raízes; a questão de juros quer a real."""
    assert _eq("Eq(1000*(1+i)**3, 1331)", "[Rational(1,10)]", "i").veredicto == Veredicto.APROVADO
    assert _eq("Eq(r**3, 3)", "[3**(Rational(1,3))]", "r").veredicto == Veredicto.APROVADO


def test_gabarito_que_inventa_raiz_continua_reprovado():
    assert _eq("Eq(x**2 - 8*x + 20, 0)", "[4]").veredicto == Veredicto.REJEITADO
    assert _eq("Eq(x**2 - 5*x + 6, 0)", "[2]").veredicto == Veredicto.REJEITADO


# ------------------------------------------------- domínio declarado na questão
def test_equacao_restrita_ao_dominio_da_questao():
    """2cos(pi(t-3)/6) + 3 = 4 tem soluções [1, 5]; a questão vai só até t=3."""
    r = _eq("Eq(2*cos(pi*(t-3)/6) + 3, 4)", "[1]", "t", dominio="Interval(0,3)")
    assert r.veredicto == Veredicto.APROVADO
    # sem a restrição, faltar uma solução continua sendo divergência
    assert _eq("Eq(2*cos(pi*(t-3)/6) + 3, 4)", "[1]", "t").veredicto == Veredicto.REJEITADO


# ------------------------------------------------- ponto flutuante x exato
def test_taxa_escrita_como_decimal_nao_reprova():
    """800*1.08**10 difere de 800*(27/25)**10 em 1e-12: representação, não erro."""
    r = _fn("800*(1.08)**t", "valor", "800*(Rational(27,25))**10", "t", ponto="10")
    assert r.veredicto == Veredicto.APROVADO_RESSALVA_NUMERICA
    assert _fn("800*1.08**t", "valor", "1727.13999781823", "t", ponto="10").veredicto \
        == Veredicto.APROVADO_RESSALVA_NUMERICA


def test_erro_de_verdade_nao_cabe_na_tolerancia():
    assert _fn("800*1.08**t", "valor", "1800", "t", ponto="10").veredicto == Veredicto.REJEITADO


def test_coincidencia_exata_continua_sendo_aprovacao_plena():
    """A ressalva é para quem casou só numericamente — não pode contaminar o resto."""
    assert _eq("Eq(x**2 - 5*x + 6, 0)", "[2, 3]").veredicto == Veredicto.APROVADO
    assert _fn("2*x + 1", "valor", "7", ponto="3").veredicto == Veredicto.APROVADO
