"""Verificação de propriedades de funções: zeros, vértice, valor em ponto, imagem.

O campo `parametros['consulta']` indica qual propriedade o gabarito afirma:
  - 'zeros'          -> resposta_esperada é a lista de raízes
  - 'vertice'        -> resposta_esperada é o par '(xv, yv)'
  - 'valor'          -> parametros['ponto'] dá x; resposta_esperada é f(x)
  - 'maximo'/'minimo'-> resposta_esperada é o valor extremo de f
"""

from __future__ import annotations

import sympy as sp

from ..modelos import ExpressaoVerificavel, ResultadoVerificacao, Veredicto
from ._parse import parse, parse_lista, simbolo


def verificar(ev: ExpressaoVerificavel) -> ResultadoVerificacao:
    consulta = ev.parametros.get("consulta", "zeros")
    f = parse(ev.expressao)
    x = simbolo(ev.incognitas[0])

    if consulta == "zeros":
        return _comparar_conjunto(sp.solve(f, x), parse_lista(ev.resposta_esperada), "zeros da função")

    if consulta == "vertice":
        xv = sp.solve(sp.diff(f, x), x)[0]
        yv = f.subs(x, xv)
        esperado = parse_lista(ev.resposta_esperada)
        if len(esperado) == 2 and sp.simplify(esperado[0] - xv) == 0 and sp.simplify(esperado[1] - yv) == 0:
            return _aprovado(f"vértice calculado ({xv}, {yv})")
        return _rejeitado(f"vértice calculado ({xv}, {yv})", f"gabarito {esperado}")

    if consulta == "valor":
        ponto = parse(ev.parametros["ponto"])
        calculado = sp.simplify(f.subs(x, ponto))
        esperado = parse(ev.resposta_esperada)
        if sp.simplify(calculado - esperado) == 0:
            return _aprovado(f"f({ponto}) = {calculado}")
        return _rejeitado(f"f({ponto}) = {calculado}", f"gabarito {esperado}")

    if consulta in ("maximo", "minimo"):
        candidatos = sp.solve(sp.diff(f, x), x)
        if not candidatos:
            return ResultadoVerificacao(
                veredicto=Veredicto.NAO_VERIFICAVEL,
                justificativa="Função sem ponto crítico — consulta de extremo não se aplica.",
            )
        valor = f.subs(x, candidatos[0])
        esperado = parse(ev.resposta_esperada)
        if sp.simplify(valor - esperado) == 0:
            return _aprovado(f"extremo calculado {valor}")
        return _rejeitado(f"extremo calculado {valor}", f"gabarito {esperado}")

    return ResultadoVerificacao(
        veredicto=Veredicto.NAO_VERIFICAVEL,
        justificativa=f"Consulta de função desconhecida: '{consulta}'.",
    )


def _comparar_conjunto(calculados, esperados, rotulo) -> ResultadoVerificacao:
    iguais = len(calculados) == len(esperados) and all(
        any(sp.simplify(e - c) == 0 for c in calculados) for e in esperados
    )
    if iguais:
        return _aprovado(f"{rotulo}: {calculados}")
    return _rejeitado(f"{rotulo} calculados: {calculados}", f"gabarito: {esperados}")


def _aprovado(detalhe: str) -> ResultadoVerificacao:
    return ResultadoVerificacao(
        veredicto=Veredicto.APROVADO,
        justificativa=f"Gabarito confirmado ({detalhe}).",
        resultado_calculado=detalhe,
    )


def _rejeitado(calculado: str, esperado: str) -> ResultadoVerificacao:
    return ResultadoVerificacao(
        veredicto=Veredicto.REJEITADO,
        justificativa=f"Divergência: {calculado}; {esperado}.",
        resultado_calculado=calculado,
    )
