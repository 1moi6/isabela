"""Verificação de propriedades de funções: zeros, vértice, valor em ponto, extremos,
domínio, imagem, período e crescimento.

O campo `parametros['consulta']` indica qual propriedade o gabarito afirma:
  - 'zeros'          -> resposta_esperada é a lista de raízes
  - 'vertice'        -> resposta_esperada é o par '(xv, yv)'
  - 'valor'          -> parametros['ponto'] dá x; resposta_esperada é f(x)
  - 'maximo'/'minimo'-> resposta_esperada é o valor extremo de f
  - 'dominio'        -> resposta_esperada é um conjunto, ex.: 'Interval.open(0, oo)'.
                        O declarado precisa CABER no domínio máximo, não coincidir com
                        ele: a questão pode restringi-lo ao que o contexto admite.
  - 'imagem'         -> idem, ex.: 'Interval(-2, 4)'. Aceita parametros['dominio'] para
                        calcular a imagem sobre o domínio de contexto.
  - 'periodo'        -> resposta_esperada é o período fundamental, ex.: '2*pi'
  - 'crescimento'    -> resposta_esperada é 'crescente' ou 'decrescente'

As quatro últimas atendem às funções logarítmicas, trigonométricas e definidas por
várias sentenças (EM13MAT305, 306, 403, 404 e 405).

**Princípio destas consultas**: quando o SymPy não conclui, o veredicto é
NAO_VERIFICAVEL --- nunca REJEITADO. A distinção não é acadêmica. `function_range`
devolve `EmptySet` para `2**x` (mas acerta `3*2**x`): tratar essa resposta como
cálculo válido faria o sistema **reprovar um gabarito correto** e mandar o Gerador
"corrigir" o que estava certo. Errar para o lado de não conferir é recuperável;
errar para o lado de reprovar o certo destrói a confiança do professor no
verificador.
"""

from __future__ import annotations

import sympy as sp
from sympy.calculus.singularities import is_decreasing, is_increasing
from sympy.calculus.util import continuous_domain, function_range

from ..modelos import ExpressaoVerificavel, ResultadoVerificacao, Veredicto
from ._parse import parse, parse_lista, simbolo


def verificar(ev: ExpressaoVerificavel) -> ResultadoVerificacao:
    consulta = ev.parametros.get("consulta", "zeros")
    f = parse(ev.expressao, ev.incognitas)
    x = simbolo(ev.incognitas[0], ev.incognitas)

    if consulta in ("dominio", "imagem", "periodo", "crescimento"):
        return _verificar_caracteristica(
            consulta, f, x, ev.resposta_esperada, ev.incognitas, ev.parametros
        )

    if consulta == "zeros":
        return _comparar_conjunto(sp.solve(f, x), parse_lista(ev.resposta_esperada, ev.incognitas), "zeros da função")

    if consulta == "vertice":
        xv = sp.solve(sp.diff(f, x), x)[0]
        yv = f.subs(x, xv)
        esperado = parse_lista(ev.resposta_esperada, ev.incognitas)
        if len(esperado) == 2 and sp.simplify(esperado[0] - xv) == 0 and sp.simplify(esperado[1] - yv) == 0:
            return _aprovado(f"vértice calculado ({xv}, {yv})")
        return _rejeitado(f"vértice calculado ({xv}, {yv})", f"gabarito {esperado}")

    if consulta == "valor":
        ponto = parse(ev.parametros["ponto"], ev.incognitas)
        calculado = sp.simplify(f.subs(x, ponto))
        esperado = parse(ev.resposta_esperada, ev.incognitas)
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
        esperado = parse(ev.resposta_esperada, ev.incognitas)
        if sp.simplify(valor - esperado) == 0:
            return _aprovado(f"extremo calculado {valor}")
        return _rejeitado(f"extremo calculado {valor}", f"gabarito {esperado}")

    return ResultadoVerificacao(
        veredicto=Veredicto.NAO_VERIFICAVEL,
        justificativa=f"Consulta de função desconhecida: '{consulta}'.",
    )


def _verificar_caracteristica(
    consulta, f, x, resposta: str, incognitas=None, extras=None
) -> ResultadoVerificacao:
    """Domínio, imagem, período e crescimento — as características que as habilidades
    de funções logarítmicas e trigonométricas pedem comparar entre representações.

    O domínio é calculado primeiro porque as outras dependem dele: `log(x)` só é
    crescente *no seu domínio*, e avaliá-lo sobre os reais devolveria `False` para
    uma função que é crescente onde existe.
    """
    dominio = _tentar(lambda: continuous_domain(f, x, sp.S.Reals))
    if dominio is None:
        return _inconclusivo(f"não foi possível determinar o domínio de {f}")

    if consulta == "dominio":
        return _conferir_dominio(dominio, resposta, f, incognitas)

    if consulta == "imagem":
        # A imagem depende do domínio que a questão adota: `500*2**x` com x
        # contando períodos tem imagem [500, oo), não (0, oo). Quando o Gerador
        # declara o domínio de contexto, é sobre ele que a imagem é calculada.
        sobre = dominio
        if "dominio" in (extras or {}):
            declarado = _tentar(lambda: parse(extras["dominio"], incognitas))
            if isinstance(declarado, sp.Set) and declarado.is_subset(dominio):
                sobre = declarado
        imagem = _tentar(lambda: function_range(f, x, sobre))
        # EmptySet aqui quase nunca é a imagem real: é o SymPy desistindo.
        if imagem is None or imagem == sp.S.EmptySet:
            return _inconclusivo(f"não foi possível determinar a imagem de {f}")
        return _comparar_conjuntos(imagem, resposta, f, "imagem", incognitas)

    if consulta == "periodo":
        periodo = _tentar(lambda: sp.periodicity(f, x))
        if periodo is None:
            return _inconclusivo(f"{f} não é periódica ou o período não foi determinado")
        esperado = parse(resposta, incognitas)
        if sp.simplify(periodo - esperado) == 0:
            return _aprovado(f"período {periodo}")
        return _rejeitado(f"período calculado {periodo}", f"gabarito {esperado}")

    # crescimento
    declarado = str(resposta).strip().lower()
    if declarado not in ("crescente", "decrescente"):
        return _inconclusivo(
            f"resposta '{resposta}' não é 'crescente' nem 'decrescente'"
        )
    cresce = _tentar(lambda: bool(is_increasing(f, dominio, x)))
    decresce = _tentar(lambda: bool(is_decreasing(f, dominio, x)))
    if cresce is None or decresce is None or cresce == decresce:
        # Iguais significa ou indeterminação, ou função não monótona: em nenhum
        # dos casos dá para afirmar que o gabarito está errado.
        return _inconclusivo(f"não foi possível decidir a monotonicidade de {f} em {dominio}")
    obtido = "crescente" if cresce else "decrescente"
    if obtido == declarado:
        return _aprovado(f"{obtido} em {dominio}")
    return _rejeitado(f"calculada como {obtido} em {dominio}", f"gabarito '{declarado}'")


def _conferir_dominio(calculado, resposta: str, f, incognitas) -> ResultadoVerificacao:
    """O domínio declarado precisa **caber** no domínio máximo --- não coincidir com ele.

    Uma questão restringe legitimamente o domínio da função ao que o contexto
    admite: `t` é tempo e não pode ser negativo, `n` conta termos e é natural. Foi
    exigindo igualdade que o verificador reprovou, numa medição com provedor real,
    quatro gabaritos corretos --- entre eles os das habilidades EM13MAT507 e 508,
    que tratam justamente de **funções de domínios discretos**: declarar o domínio
    como os naturais é o que a habilidade pede, e era exatamente o que reprovava.

    O erro genuíno continua barrado, porque é de outra natureza: declarar que
    `log(x-2)` está definida em todos os reais afirma pontos onde a função não
    existe, e aí o declarado não cabe no calculado.
    """
    esperado = parse(resposta, incognitas)
    if not isinstance(esperado, sp.Set):
        return _inconclusivo(f"o gabarito '{resposta}' não descreve um conjunto")
    if esperado == calculado:
        return _aprovado(f"domínio de {f}: {calculado}")
    contido = _tentar(lambda: bool(esperado.is_subset(calculado)))
    if contido is None:
        return _inconclusivo(f"não foi possível comparar {esperado} com o domínio {calculado}")
    if contido:
        return _aprovado(
            f"domínio {esperado} — restrição de contexto dentro do domínio máximo {calculado}"
        )
    return _rejeitado(
        f"domínio máximo calculado: {calculado}",
        f"gabarito {esperado} inclui pontos onde a função não está definida",
    )


def _tentar(calculo):
    """Devolve None quando o SymPy não conclui, em vez de propagar a exceção.

    `continuous_domain` levanta NotImplementedError para Piecewise, e várias
    dessas rotinas falham em casos legítimos. Cada falha vira NAO_VERIFICAVEL.
    """
    try:
        resultado = calculo()
    except (NotImplementedError, TypeError, ValueError, AttributeError):
        return None
    return resultado


def _comparar_conjuntos(calculado, resposta: str, f, rotulo: str, incognitas=None) -> ResultadoVerificacao:
    esperado = parse(resposta, incognitas)
    if not isinstance(esperado, sp.Set):
        return _inconclusivo(f"o gabarito '{resposta}' não descreve um conjunto")
    if calculado == esperado:
        return _aprovado(f"{rotulo} de {f}: {calculado}")
    return _rejeitado(f"{rotulo} calculado: {calculado}", f"gabarito: {esperado}")


def _inconclusivo(detalhe: str) -> ResultadoVerificacao:
    return ResultadoVerificacao(
        veredicto=Veredicto.NAO_VERIFICAVEL,
        justificativa=f"Verificação inconclusiva: {detalhe}. Conferir manualmente.",
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
