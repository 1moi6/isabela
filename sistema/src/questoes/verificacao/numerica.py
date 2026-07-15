"""Verificação numérica complementar (Seção 4.4.3 da dissertação).

Quando a verificação simbólica não é conclusiva, avalia duas expressões em
pontos aleatórios: concordância em k pontos independentes é evidência
probabilística forte de equivalência (não prova). O veredito nunca é
APROVADO pleno — no máximo APROVADO_RESSALVA_NUMERICA.
"""

from __future__ import annotations

import random

import sympy as sp

from ..modelos import ResultadoVerificacao, Veredicto
from ._parse import parse, simbolo

_PONTOS = 12
_TOLERANCIA = 1e-9
_SEMENTE = 42  # reprodutibilidade (requisito do projeto)


def equivalentes(expr_a: str, expr_b: str, incognita: str = "x") -> ResultadoVerificacao:
    a, b = parse(expr_a), parse(expr_b)
    x = simbolo(incognita)
    rng = random.Random(_SEMENTE)

    testados = 0
    for _ in range(_PONTOS * 3):  # sorteia mais pontos que o alvo p/ tolerar domínios restritos
        ponto = rng.uniform(-10, 10)
        try:
            va = complex(sp.N(a.subs(x, ponto)))
            vb = complex(sp.N(b.subs(x, ponto)))
        except (TypeError, ValueError, ZeroDivisionError):
            continue  # ponto fora do domínio de uma das expressões
        if abs(va - vb) > _TOLERANCIA:
            return ResultadoVerificacao(
                veredicto=Veredicto.REJEITADO,
                justificativa=f"Expressões divergem em x = {ponto:.4f} ({va} != {vb}).",
            )
        testados += 1
        if testados >= _PONTOS:
            break

    if testados < _PONTOS // 2:
        return ResultadoVerificacao(
            veredicto=Veredicto.NAO_VERIFICAVEL,
            justificativa=f"Apenas {testados} pontos avaliáveis — domínio restrito demais para conclusão numérica.",
        )
    return ResultadoVerificacao(
        veredicto=Veredicto.APROVADO_RESSALVA_NUMERICA,
        justificativa=f"Expressões concordam em {testados} pontos aleatórios (tolerância {_TOLERANCIA}). "
        "Equivalência verificada empiricamente, não simbolicamente.",
    )
