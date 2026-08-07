"""Verificação de equações e sistemas: comparação de conjuntos-solução.

Cobre equações de 1º e 2º graus e exponenciais do recorte. O critério é
igualdade simbólica exata entre o conjunto-solução calculado pelo SymPy e o
gabarito proposto pelo Gerador.
"""

from __future__ import annotations

import sympy as sp

from ..modelos import ExpressaoVerificavel, ResultadoVerificacao, Veredicto
from ._parse import parse, parse_lista, simbolo


def verificar(ev: ExpressaoVerificavel) -> ResultadoVerificacao:
    equacao = parse(ev.expressao, ev.incognitas)
    incognitas = [simbolo(n, ev.incognitas) for n in ev.incognitas]
    esperadas = parse_lista(ev.resposta_esperada, ev.incognitas)

    calculadas = sp.solve(equacao, incognitas if len(incognitas) > 1 else incognitas[0])
    if isinstance(calculadas, dict):  # sistemas retornam dict {simbolo: valor}
        calculadas = [calculadas[s] for s in incognitas]

    faltantes = [e for e in esperadas if not _pertence(e, calculadas)]
    excedentes = [c for c in calculadas if not _pertence(c, esperadas)]

    if not faltantes and not excedentes:
        return ResultadoVerificacao(
            veredicto=Veredicto.APROVADO,
            justificativa="Conjunto-solução do gabarito coincide exatamente com o calculado.",
            resultado_calculado=str(calculadas),
        )
    partes = []
    if faltantes:
        partes.append(f"soluções do gabarito não confirmadas: {faltantes}")
    if excedentes:
        partes.append(f"soluções calculadas ausentes do gabarito: {excedentes}")
    return ResultadoVerificacao(
        veredicto=Veredicto.REJEITADO,
        justificativa="Divergência no conjunto-solução — " + "; ".join(str(p) for p in partes) + ".",
        resultado_calculado=str(calculadas),
    )


def _pertence(valor, colecao) -> bool:
    """Igualdade simbólica exata: simplify(a - b) == 0 (Seção 2.4.2 da dissertação)."""
    return any(sp.simplify(valor - outro) == 0 for outro in colecao)
