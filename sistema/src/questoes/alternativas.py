"""Ordem das alternativas de múltipla escolha.

O Gerador escreve a alternativa correta primeiro: no acervo de 85 questões, ela
era a (a) em 38 das 43 de múltipla escolha, e um professor do painel notou que
"a resposta [está] sempre na letra A". Pedir ao modelo que varie a posição não
resolve --- modelo de linguagem não sorteia ---, então a ordem é sorteada aqui,
depois da geração e antes de a questão seguir para o Crítico.

A semente vem do enunciado, e não do relógio: a mesma questão sai sempre com a
mesma ordem, o que mantém reproduzíveis os testes e as medições.

O cuidado que não pode faltar é a **renumeração**. O gabarito e a resolução às
vezes citam a alternativa pela letra ("Mês 216 (alternativa A)", ou um gabarito
que é só "A"). Trocar a ordem sem trocar a letra faria o gabarito apontar para um
distrator --- um erro criado pelo próprio conserto, e silencioso, porque o
Verificador confere a formalização e não a letra.
"""

from __future__ import annotations

import hashlib
import random
import re

from .modelos import Questao

LETRAS = "abcd"

# "alternativa A", "Alternativa (b)", "letra C", "opção d". O nome na frente é o
# que separa a referência à alternativa de um "a)" de item ou de um "(7-2a)".
_CITACAO = re.compile(
    r"\b(alternativa|letra|op[çc][ãa]o)(\s*\(?\s*)([a-d])(?![\w])", re.IGNORECASE
)
# Gabarito que começa pela letra: "D) Domínio = ..." ou "(b) Parábola B".
_GABARITO_COM_LETRA = re.compile(r"^(\s*\(?)([a-d])(\))", re.IGNORECASE)
# Gabarito que é só a letra: "A", "(b)", "C."
_GABARITO_SO_LETRA = re.compile(r"^(\s*\(?)([a-d])(\)?\.?\s*)$", re.IGNORECASE)


def _trocar(letra: str, nova_posicao: dict[str, str]) -> str:
    nova = nova_posicao.get(letra.lower(), letra.lower())
    return nova.upper() if letra.isupper() else nova


def _renumerar(texto: str, nova_posicao: dict[str, str], gabarito: bool) -> str:
    texto = _CITACAO.sub(
        lambda m: m.group(1) + m.group(2) + _trocar(m.group(3), nova_posicao), texto
    )
    if gabarito:
        for padrao in (_GABARITO_SO_LETRA, _GABARITO_COM_LETRA):
            if padrao.match(texto):
                return padrao.sub(
                    lambda m: m.group(1) + _trocar(m.group(2), nova_posicao) + m.group(3),
                    texto, count=1,
                )
    return texto


def embaralhar(questao: Questao) -> Questao:
    """Devolve a questão com as alternativas em ordem sorteada e as letras corrigidas."""
    alternativas = questao.alternativas
    if not alternativas or len(alternativas) < 2 or len(alternativas) > len(LETRAS):
        return questao

    semente = int.from_bytes(hashlib.sha256(questao.enunciado.encode("utf-8")).digest()[:8], "big")
    ordem = list(range(len(alternativas)))
    random.Random(semente).shuffle(ordem)

    # ordem[nova] = antiga; a renumeração precisa do caminho inverso.
    nova_posicao = {LETRAS[antiga]: LETRAS[nova] for nova, antiga in enumerate(ordem)}
    return questao.model_copy(update={
        "alternativas": [alternativas[i] for i in ordem],
        "gabarito": _renumerar(questao.gabarito, nova_posicao, gabarito=True),
        "resolucao": _renumerar(questao.resolucao, nova_posicao, gabarito=False),
    })
