"""Incógnitas com nomes que o SymPy reserva.

Encontrado numa medição com provedor real: o Gerador escolheu `I` para a
intensidade de um abalo sísmico (EM13MAT305), e `sympify` resolveu o nome
contra os globais do SymPy — onde `I` é a unidade imaginária. A expressão
virou uma constante complexa.

O caso perigoso não é esse, que degradou para não-verificável, e sim o `E`:
como `E` é o número de Euler, `Eq(E**2, 4)` simplifica para `False` e o
gabarito correto `[-2, 2]` seria REPROVADO. O sistema mandaria o Gerador
corrigir uma questão certa — erro silencioso com autoridade.

São justamente as letras que um enunciado de Ensino Médio usa: E de energia,
I de intensidade ou corrente, N de população, S de área.
"""

import pytest

from questoes.modelos import ExpressaoVerificavel, Veredicto
from questoes.verificacao import verificar
from questoes.verificacao._parse import parse, simbolo


@pytest.mark.parametrize("nome", ["E", "I", "N", "S", "O", "beta", "gamma"])
def test_incognita_declarada_vira_simbolo_livre(nome):
    expressao = parse(f"2*{nome} + 1", incognitas=[nome])
    assert expressao.free_symbols == {simbolo(nome, [nome])}


def test_equacao_com_incognita_E_nao_e_reprovada():
    """O caso que produziria falso negativo: E é o número de Euler no SymPy."""
    r = verificar(ExpressaoVerificavel(
        tipo="equacao", expressao="Eq(E**2, 4)", incognitas=["E"], resposta_esperada="[-2, 2]",
    ))
    assert r.veredicto == Veredicto.APROVADO


def test_funcao_com_incognita_I_e_verificavel():
    """O caso real: intensidade de abalo sísmico na escala Richter."""
    r = verificar(ExpressaoVerificavel(
        tipo="funcao", expressao="log(I, 10)", incognitas=["I"],
        resposta_esperada="crescente", parametros={"consulta": "crescimento"},
    ))
    assert r.veredicto == Veredicto.APROVADO


def test_incognita_declarada_perde_as_assuncoes_curadas():
    """A regra oposta valia até a geração do acervo de 8 de agosto mostrar o custo.

    `n` é inteiro e positivo em `_LOCAIS`, o que é certo enquanto ele é índice de
    progressão. Quando o Gerador batiza de `n` a incógnita do problema, a mesma
    restrição faz `solve(5*n + 17 = 150)` devolver vazio — não existe inteiro — e
    o gabarito correto `133/5` é reprovado. Impor integralidade que o enunciado
    não pediu é o verificador arbitrando pelo enunciado.
    """
    assert simbolo("n").is_integer            # continua curado quando não é declarado
    assert simbolo("n", ["n"]).is_integer is None   # declarado, é símbolo livre


def test_equacao_cuja_incognita_se_chama_n_nao_e_reprovada():
    r = verificar(ExpressaoVerificavel(
        tipo="equacao", expressao="Eq(5*n + 17, 150)", incognitas=["n"],
        resposta_esperada="[Rational(133,5)]",
    ))
    assert r.veredicto == Veredicto.APROVADO
