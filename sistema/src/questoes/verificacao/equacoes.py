"""Verificação de equações e sistemas: comparação de conjuntos-solução.

Cobre equações de 1º e 2º graus e exponenciais do recorte. O critério é
igualdade entre o conjunto-solução calculado pelo SymPy e o gabarito proposto
pelo Gerador --- com três acomodações que a geração do acervo mostrou serem
necessárias, todas para não reprovar gabarito correto:

  - **só as soluções reais contam**, salvo se o próprio gabarito trouxer
    complexas. `solve(x**2 - 8*x + 20)` devolve `[4-2i, 4+2i]`, e o gabarito
    `[]` --- "não há raízes reais" --- estava certo;
  - **o domínio da questão restringe o conjunto**, quando declarado em
    `parametros['dominio']`: `2cos(pi(t-3)/6)+3 = 4` tem soluções `[1, 5]`, e a
    questão que se limita a `[0, 3]` acerta ao responder `[1]`;
  - **diferença numericamente desprezível não é divergência**: o Gerador escreve
    `1.08` numa questão de juros, e `800*1.08**10` difere do racional exato em
    1e-12. Aí o veredicto é aprovado com ressalva numérica, nunca reprovação.
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

    calculadas = _restringir(calculadas, esperadas, ev, incognitas[0] if incognitas else None)

    faltantes = [e for e in esperadas if not _pertence(e, calculadas)]
    excedentes = [c for c in calculadas if not _pertence(c, esperadas)]

    if not faltantes and not excedentes:
        # 'aproximado' é o que casou SÓ numericamente: se a igualdade exata
        # vale, o veredicto continua sendo aprovação plena.
        aproximado = any(
            not _exato(e, calculadas) and _apenas_ruido(e, calculadas) for e in esperadas
        )
        return ResultadoVerificacao(
            veredicto=(
                Veredicto.APROVADO_RESSALVA_NUMERICA if aproximado else Veredicto.APROVADO
            ),
            justificativa=(
                "Conjunto-solução do gabarito coincide com o calculado, a menos de "
                "arredondamento (o gabarito usa decimais)."
                if aproximado
                else "Conjunto-solução do gabarito coincide exatamente com o calculado."
            ),
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


# Abaixo disso, a diferença é ruído de representação e não erro de matemática:
# 800*1.08**10 e 800*(27/25)**10 diferem em 1e-12 e são a mesma coisa.
_TOLERANCIA = 1e-9


def _restringir(calculadas, esperadas, ev, incognita):
    """Fica com o que a questão de fato considera solução.

    Descarta as complexas quando o gabarito só traz reais --- o caso do
    discriminante negativo, em que responder "nenhuma raiz real" é o certo --- e
    aplica o domínio declarado, quando houver.
    """
    if not any(e.is_real is False for e in esperadas if hasattr(e, "is_real")):
        calculadas = [c for c in calculadas if getattr(c, "is_real", None) is not False]

    bruto = ev.parametros.get("dominio") or ev.parametros.get("dominio_considerado")
    if bruto and incognita is not None:
        try:
            dominio = parse(bruto, ev.incognitas)
            if isinstance(dominio, sp.Set):
                calculadas = [c for c in calculadas if dominio.contains(c) == sp.true]
        except (TypeError, ValueError, AttributeError, sp.SympifyError):
            pass  # domínio ilegível não pode custar a verificação
    return calculadas


def _pertence(valor, colecao) -> bool:
    """Igualdade simbólica, com o arredondamento do gabarito tolerado.

    A comparação exata (Seção 2.4.2 da dissertação) continua sendo a primeira; a
    numérica só entra quando ela falha, e o veredicto que ela permite é o de
    ressalva, nunca aprovação plena.
    """
    return _exato(valor, colecao) or _apenas_ruido(valor, colecao)


def _exato(valor, colecao) -> bool:
    return any(sp.simplify(valor - outro) == 0 for outro in colecao)


def _apenas_ruido(valor, colecao) -> bool:
    """A diferença cabe na tolerância numérica?"""
    for outro in colecao:
        try:
            if abs(complex(sp.N(valor - outro))) <= _TOLERANCIA:
                return True
        except (TypeError, ValueError):
            continue
    return False
