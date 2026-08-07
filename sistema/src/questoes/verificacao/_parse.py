"""Parsing controlado de expressões SymPy vindas do Agente Gerador.

Usa sympify com dicionário local restrito: a string vem de um LLM e não deve
ter acesso a nomes arbitrários do ambiente Python.
"""

from __future__ import annotations

import sympy as sp

# Símbolos e funções que o Gerador está autorizado a usar nas formalizações.
_LOCAIS = {
    "x": sp.Symbol("x"),
    "y": sp.Symbol("y"),
    "t": sp.Symbol("t"),
    "n": sp.Symbol("n", integer=True, positive=True),
    "Eq": sp.Eq,
    "sqrt": sp.sqrt,
    "Rational": sp.Rational,
    "pi": sp.pi,
    "exp": sp.exp,
    "log": sp.log,
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "Abs": sp.Abs,
    # Domínios e imagens são conjuntos: o gabarito de uma consulta de domínio
    # chega como "Interval.open(0, oo)" ou "S.Reals".
    "Interval": sp.Interval,
    "Union": sp.Union,
    "oo": sp.oo,
    "S": sp.S,
    "EmptySet": sp.S.EmptySet,
    # Funções definidas por mais de uma sentença (EM13MAT405).
    "Piecewise": sp.Piecewise,
}


def _locais(incognitas=None) -> dict:
    """Namespace de parsing com as incógnitas declaradas ligadas a símbolos.

    Sem isto, `sympify` resolve nomes não listados contra os globais do SymPy ---
    onde `E` é o número de Euler, `I` a unidade imaginária, `N` uma função, `S` o
    registro de singletons e `O` a notação de Landau. São justamente as letras que
    um enunciado de Ensino Médio usa para energia, intensidade, população, área.

    A consequência não é ficar sem verificar: é **verificar errado**. Uma questão
    cuja incógnita é `E` faz `Eq(E**2, 4)` simplificar para `False`, e o gabarito
    correto `[-2, 2]` seria reprovado --- o sistema mandaria o Gerador corrigir o
    que estava certo. Encontrado numa medição com provedor real, em que o Gerador
    escolheu `I` para a intensidade de um abalo sísmico.

    Os símbolos curados em `_LOCAIS` (como o `n` inteiro e positivo das
    progressões) têm precedência: só os nomes que lá não são símbolo é que passam
    a ser ligados.
    """
    locais = dict(_LOCAIS)
    for nome in incognitas or ():
        if not isinstance(locais.get(nome), sp.Symbol):
            locais[nome] = sp.Symbol(nome)
    return locais


def parse(texto: str, incognitas=None):
    """Converte a string em objeto SymPy com namespace restrito."""
    return sp.sympify(texto, locals=_locais(incognitas), evaluate=True)


def parse_lista(texto: str, incognitas=None) -> list:
    """Aceita '[1, 3/2]' ou '1' e retorna sempre uma lista de objetos SymPy."""
    resultado = parse(texto, incognitas)
    if isinstance(resultado, (list, tuple, set, sp.FiniteSet)):
        return list(resultado)
    return [resultado]


def simbolo(nome: str, incognitas=None) -> sp.Symbol:
    """O símbolo que `parse` usará para este nome --- os dois têm de concordar."""
    return _locais(incognitas).get(nome) or sp.Symbol(nome)
