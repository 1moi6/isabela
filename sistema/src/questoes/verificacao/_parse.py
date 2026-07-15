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
}


def parse(texto: str):
    """Converte a string em objeto SymPy com namespace restrito."""
    return sp.sympify(texto, locals=_LOCAIS, evaluate=True)


def parse_lista(texto: str) -> list:
    """Aceita '[1, 3/2]' ou '1' e retorna sempre uma lista de objetos SymPy."""
    resultado = parse(texto)
    if isinstance(resultado, (list, tuple, set, sp.FiniteSet)):
        return list(resultado)
    return [resultado]


def simbolo(nome: str) -> sp.Symbol:
    return _LOCAIS.get(nome, sp.Symbol(nome))
