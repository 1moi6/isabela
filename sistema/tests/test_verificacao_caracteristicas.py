"""Domínio, imagem, período e crescimento (Fase 2a/2b do plano de expansão).

São as consultas que atendem às funções logarítmicas, trigonométricas e
definidas por várias sentenças — EM13MAT305, 306, 403, 404 e 405.

O princípio que estes testes protegem: quando o SymPy não conclui, o veredicto
é `nao_verificavel`, nunca `rejeitado`. Reprovar um gabarito correto é pior do
que não conferir, porque manda o Gerador "corrigir" o que já estava certo.
"""

from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar


def _ev(expressao, consulta, resposta, **extra):
    return verificar(ExpressaoVerificavel(
        tipo="funcao", expressao=expressao, incognitas=["x"],
        resposta_esperada=resposta, parametros={"consulta": consulta, **extra},
    ))


def test_dominio_de_logaritmo():
    assert _ev("log(x-2)", "dominio", "Interval.open(2, oo)").veredicto == Veredicto.APROVADO
    assert _ev("log(x-2)", "dominio", "S.Reals").veredicto == Veredicto.REJEITADO


def test_imagem_e_periodo_de_funcao_trigonometrica():
    assert _ev("3*sin(2*x)+1", "imagem", "Interval(-2, 4)").veredicto == Veredicto.APROVADO
    assert _ev("3*sin(2*x)+1", "periodo", "pi").veredicto == Veredicto.APROVADO
    assert _ev("3*sin(2*x)+1", "periodo", "2*pi").veredicto == Veredicto.REJEITADO


def test_crescimento_e_avaliado_no_dominio_e_nao_nos_reais():
    """log(x) é crescente onde existe. Avaliada sobre R, a resposta certa seria reprovada."""
    assert _ev("log(x)", "crescimento", "crescente").veredicto == Veredicto.APROVADO
    assert _ev("(1/2)**x", "crescimento", "decrescente").veredicto == Veredicto.APROVADO
    assert _ev("2**x", "crescimento", "decrescente").veredicto == Veredicto.REJEITADO


def test_imagem_inconclusiva_nao_reprova_gabarito_correto():
    """`function_range(2**x)` devolve EmptySet — o SymPy desistindo, não a imagem.

    Tratar isso como cálculo válido reprovaria "(0, +oo)", que está certo. O
    veredicto tem de ser não-verificável.
    """
    r = _ev("2**x", "imagem", "Interval.open(0, oo)")
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL
    assert "imagem" in r.justificativa
    # a mesma função com coeficiente o SymPy resolve, e aí confere de verdade
    assert _ev("3*2**x", "imagem", "Interval.open(0, oo)").veredicto == Veredicto.APROVADO


def test_funcao_por_partes():
    """EM13MAT405: tabela do IR, conta de luz — a mudança de sentença é o ponto."""
    pw = "Piecewise((2*x, x < 10), (3*x - 10, True))"
    assert _ev(pw, "valor", "50", ponto="20").veredicto == Veredicto.APROVADO
    assert _ev(pw, "valor", "10", ponto="5").veredicto == Veredicto.APROVADO
    assert _ev(pw, "valor", "40", ponto="20").veredicto == Veredicto.REJEITADO


def test_dominio_indeterminavel_degrada_sem_reprovar():
    """`continuous_domain` não trata Piecewise: não pode virar reprovação."""
    r = _ev("Piecewise((2*x, x < 10), (3*x - 10, True))", "dominio", "S.Reals")
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL


def test_crescimento_com_resposta_fora_do_vocabulario():
    assert _ev("2*x+1", "crescimento", "sobe sempre").veredicto == Veredicto.NAO_VERIFICAVEL


def test_dominio_restrito_pelo_contexto_nao_e_reprovado():
    """Encontrado numa medição com provedor real: quatro falsos negativos.

    Uma questão restringe legitimamente o domínio ao que o contexto admite —
    `t` é tempo e não pode ser negativo, `n` conta termos e é natural. Exigir
    igualdade com o domínio máximo reprovava gabaritos corretos, e nas
    EM13MAT507/508 isso era sistemático: elas tratam de funções de domínios
    discretos, então declarar o domínio como os naturais é o que a habilidade
    pede — e era exatamente o que reprovava.
    """
    assert _ev("5*n + 7", "dominio", "S.Naturals").veredicto == Veredicto.APROVADO
    assert _ev("8 - 6*cos(pi*t/15)", "dominio", "Interval(0, oo)").veredicto == Veredicto.APROVADO
    assert _ev("500*2**x", "dominio", "Interval(0, oo)").veredicto == Veredicto.APROVADO


def test_dominio_que_afirma_pontos_inexistentes_continua_reprovado():
    """A tolerância é para restrição, não para erro: log(x-2) não existe em x=0."""
    r = _ev("log(x-2)", "dominio", "S.Reals")
    assert r.veredicto == Veredicto.REJEITADO
    assert "não está definida" in r.justificativa
    assert _ev("log(x-2)", "dominio", "Interval.open(2, oo)").veredicto == Veredicto.APROVADO


def test_imagem_calculada_sobre_o_dominio_de_contexto():
    """`500*2**x` com x contando períodos tem imagem [500, oo), não (0, oo)."""
    r = _ev("500*2**x", "imagem", "Interval(500, oo)", dominio="Interval(0, oo)")
    assert r.veredicto == Veredicto.APROVADO
