"""Verificação de propriedades de uma expressão, em vez de comparação de gabarito.

As demais estratégias respondem "o resultado que o Gerador afirmou é o que o
SymPy calcula?". Há habilidades em que essa pergunta não cabe. A EM13MAT501
pede investigar uma tabela e *expressar algebricamente a generalização*: não há
"a resposta" a comparar --- há uma expressão que precisa reproduzir os pontos
dados e ter o grau declarado. A EM13MAT507 pede associar uma PA à função afim
correspondente: o verificável é a coincidência entre as duas, não um número.

Aqui `resposta_esperada` é a expressão que o estudante deve produzir, e
`parametros` declara os predicados que ela precisa satisfazer:

  - 'pontos'      -> "[(1,5),(2,8)]": f(x_i) deve valer y_i em cada par
  - 'grau'        -> "1": grau do polinômio
  - 'forma'       -> "a*x**2": só o termo declarado (nenhum de grau menor)
  - 'sequencia'   -> "pa"|"pg" com 'a1' e 'razao': f(n) deve coincidir com a
                     progressão nos primeiros termos

Predicado ausente não é verificado. Nenhum predicado declarado devolve
NAO_VERIFICAVEL --- afirmar uma propriedade vazia não é conferir nada.
"""

from __future__ import annotations

import sympy as sp

from ..modelos import ExpressaoVerificavel, ResultadoVerificacao, Veredicto
from ._parse import parse, simbolo

# Quantos termos da progressão conferir. A coincidência de uma afim com uma PA é
# determinada por dois pontos; conferir cinco custa nada e pega o caso em que o
# Gerador acerta o início e erra a lei.
_TERMOS_CONFERIDOS = 5


def verificar(ev: ExpressaoVerificavel) -> ResultadoVerificacao:
    f = parse(ev.resposta_esperada, ev.incognitas)
    x = simbolo(ev.incognitas[0] if ev.incognitas else "x", ev.incognitas)
    conferidos: list[str] = []

    if "pontos" in ev.parametros:
        for ponto in _pares(ev.parametros["pontos"], ev.incognitas):
            xi, yi = ponto
            obtido = sp.simplify(f.subs(x, xi))
            if sp.simplify(obtido - yi) != 0:
                return _rejeitado(
                    f"a expressão {f} vale {obtido} em {x}={xi}, mas a tabela dá {yi}"
                )
        conferidos.append(f"reproduz os {len(_pares(ev.parametros['pontos']))} pontos dados")

    if "grau" in ev.parametros:
        esperado = int(parse(ev.parametros["grau"], ev.incognitas))
        obtido = sp.degree(sp.Poly(f, x))
        if obtido != esperado:
            return _rejeitado(f"a expressão {f} tem grau {obtido}, e não {esperado}")
        conferidos.append(f"grau {esperado}")

    if "forma" in ev.parametros:
        erro = _conferir_forma(f, x, ev.parametros["forma"], ev.incognitas)
        if erro:
            return _rejeitado(erro)
        conferidos.append(f"forma {ev.parametros['forma']}")

    if "sequencia" in ev.parametros:
        erro = _conferir_sequencia(f, x, ev.parametros, ev.incognitas)
        if erro:
            return _rejeitado(erro)
        conferidos.append(f"coincide com a {ev.parametros['sequencia'].upper()} declarada")

    if not conferidos:
        return ResultadoVerificacao(
            veredicto=Veredicto.NAO_VERIFICAVEL,
            justificativa="Nenhuma propriedade declarada para verificar. "
            "Preencher 'pontos', 'grau', 'forma' ou 'sequencia' em parametros.",
        )

    return ResultadoVerificacao(
        veredicto=Veredicto.APROVADO,
        justificativa=f"Propriedades confirmadas para {f}: {'; '.join(conferidos)}.",
        resultado_calculado=str(f),
    )


def _pares(bruto: str, incognitas=None) -> list[tuple]:
    """Lê "[(1,5),(2,8)]" como pares de expressões SymPy."""
    lido = parse(bruto, incognitas) if not isinstance(bruto, (list, tuple)) else bruto
    return [tuple(sp.sympify(c) for c in par) for par in lido]


def _conferir_forma(f, x, forma: str, incognitas=None) -> str | None:
    """Confere que só os termos da forma declarada aparecem.

    Distingue y = ax² (EM13MAT502, "diretamente proporcional ao quadrado") de uma
    quadrática qualquer: o que a habilidade pede é justamente a ausência dos
    termos de grau menor.
    """
    graus_permitidos = {sp.degree(sp.Poly(t, x)) for t in parse(forma, incognitas).as_ordered_terms()}
    for termo in sp.expand(f).as_ordered_terms():
        grau = sp.degree(sp.Poly(termo, x))
        if grau not in graus_permitidos:
            return f"a expressão {f} tem termo de grau {grau} ({termo}), fora da forma {forma}"
    return None


def _conferir_sequencia(f, n, parametros: dict, incognitas=None) -> str | None:
    """Confere que f(n) reproduz a progressão declarada nos primeiros termos."""
    tipo = str(parametros["sequencia"]).lower()
    a1 = parse(parametros["a1"], incognitas)
    razao = parse(parametros["razao"], incognitas)
    for k in range(1, _TERMOS_CONFERIDOS + 1):
        termo = a1 + (k - 1) * razao if tipo == "pa" else a1 * razao ** (k - 1)
        obtido = sp.simplify(f.subs(n, k))
        if sp.simplify(obtido - termo) != 0:
            return (
                f"a expressão {f} vale {obtido} em {n}={k}, mas o {k}º termo da "
                f"{tipo.upper()} é {sp.simplify(termo)}"
            )
    return None


def _rejeitado(detalhe: str) -> ResultadoVerificacao:
    return ResultadoVerificacao(
        veredicto=Veredicto.REJEITADO,
        justificativa=f"Propriedade não confirmada: {detalhe}.",
        resultado_calculado=detalhe,
    )
