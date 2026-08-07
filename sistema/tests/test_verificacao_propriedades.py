"""Verificação por propriedade (Fase 1 do plano de expansão).

O que se confere aqui não é um valor, mas uma expressão que o estudante deve
produzir — o caso das habilidades EM13MAT501/502 (generalizar um padrão) e da
metade antes não verificada de EM13MAT507/508 (associar progressão a função).
"""

import pytest

from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar


def _ev(**parametros):
    resposta = parametros.pop("resposta")
    return ExpressaoVerificavel(
        tipo="propriedade", expressao="-", incognitas=["n"],
        resposta_esperada=resposta, parametros=parametros,
    )


def test_generalizacao_que_reproduz_a_tabela_e_aprovada():
    r = verificar(_ev(resposta="3*n + 2", pontos="[(1,5),(2,8),(3,11)]", grau="1"))
    assert r.veredicto == Veredicto.APROVADO


def test_generalizacao_que_erra_um_ponto_e_rejeitada():
    r = verificar(_ev(resposta="3*n + 1", pontos="[(1,5),(2,8),(3,11)]"))
    assert r.veredicto == Veredicto.REJEITADO
    assert "tabela" in r.justificativa


def test_grau_errado_e_rejeitado():
    """Reproduzir os pontos não basta se a habilidade pede função de 1º grau."""
    r = verificar(_ev(resposta="n**2 + 1", pontos="[(1,2),(2,5)]", grau="1"))
    assert r.veredicto == Veredicto.REJEITADO
    assert "grau" in r.justificativa


def test_forma_ax2_recusa_termo_de_grau_menor():
    """EM13MAT502 pede y = ax², não uma quadrática qualquer."""
    assert verificar(_ev(resposta="3*n**2", forma="a*n**2")).veredicto == Veredicto.APROVADO
    r = verificar(_ev(resposta="3*n**2 + 5", forma="a*n**2"))
    assert r.veredicto == Veredicto.REJEITADO


def test_funcao_afim_que_coincide_com_a_pa_e_aprovada():
    """O que a EM13MAT507 cobra: a associação entre a PA e a função de domínio discreto."""
    r = verificar(_ev(resposta="2*n + 3", sequencia="pa", a1="5", razao="2"))
    assert r.veredicto == Veredicto.APROVADO


def test_funcao_que_nao_coincide_com_a_pa_e_rejeitada():
    r = verificar(_ev(resposta="2*n + 4", sequencia="pa", a1="5", razao="2"))
    assert r.veredicto == Veredicto.REJEITADO


def test_exponencial_que_coincide_com_a_pg_e_aprovada():
    r = verificar(_ev(resposta="3*2**(n-1)", sequencia="pg", a1="3", razao="2"))
    assert r.veredicto == Veredicto.APROVADO


def test_sem_predicado_declarado_nao_e_verificavel():
    """Afirmar uma propriedade vazia não é conferir nada — e não pode passar por conferência."""
    r = verificar(_ev(resposta="3*n + 2"))
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL
