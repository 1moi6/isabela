"""Verificação de progressões aritméticas e geométricas: termo geral e soma.

`parametros` esperados:
  - 'tipo_progressao': 'pa' | 'pg'
  - 'a1': primeiro termo   - 'razao': razão   - 'n': índice/quantidade
  - 'consulta': 'termo' (a_n) | 'soma' (S_n)
"""

from __future__ import annotations

import sympy as sp

from ..modelos import ExpressaoVerificavel, ResultadoVerificacao, Veredicto
from ._parse import parse


def verificar(ev: ExpressaoVerificavel) -> ResultadoVerificacao:
    p = ev.parametros
    tipo = p.get("tipo_progressao", "pa")
    a1, razao, n = parse(p["a1"]), parse(p["razao"]), parse(p["n"])
    consulta = p.get("consulta", "termo")
    esperado = parse(ev.resposta_esperada)

    if tipo == "pa":
        calculado = a1 + (n - 1) * razao if consulta == "termo" else n * (2 * a1 + (n - 1) * razao) / 2
    elif tipo == "pg":
        if consulta == "termo":
            calculado = a1 * razao ** (n - 1)
        elif sp.simplify(razao - 1) == 0:
            calculado = a1 * n
        else:
            calculado = a1 * (razao**n - 1) / (razao - 1)
    else:
        return ResultadoVerificacao(
            veredicto=Veredicto.NAO_VERIFICAVEL,
            justificativa=f"Tipo de progressão desconhecido: '{tipo}'.",
        )

    calculado = sp.simplify(calculado)
    if sp.simplify(calculado - esperado) == 0:
        return ResultadoVerificacao(
            veredicto=Veredicto.APROVADO,
            justificativa=f"Gabarito confirmado ({consulta} da {tipo.upper()} = {calculado}).",
            resultado_calculado=str(calculado),
        )
    return ResultadoVerificacao(
        veredicto=Veredicto.REJEITADO,
        justificativa=f"Divergência: {consulta} calculado = {calculado}, gabarito = {esperado}.",
        resultado_calculado=str(calculado),
    )
