"""Lê o Markdown-com-matemática do Gerador como estrutura, não como string.

O Gerador devolve prosa em Markdown com a matemática em `$...$` e `$$...$$`,
mais tabelas de faixa, listas e negrito. Cada destino precisa dessa estrutura de
um jeito diferente — o LaTeX vira `tabular`, o Word vira `w:tbl`, a página vira
`<table>` — e é a *leitura* que os três têm em comum. Sem um dono para ela, cada
destino reinventava a sua: a página não lia nada (o enunciado saía como código
corrido), o `.docx` não lia nada, e só o `.tex` sabia o que era uma tabela.

A ordem em que moeda e fórmula são reconhecidas é a parte delicada e está
explicada em `MOEDA_OU_MATEMATICA` — `tex.py` importa a mesma expressão daqui,
porque duas cópias de uma regra sutil garantem que uma delas fique para trás.

O que se lê aqui é o subconjunto que o Gerador de fato escreve, medido no acervo
de 90 questões: parágrafo, fórmula em display, lista com marcador, tabela com
barra vertical e negrito com asteriscos. Nada de links, imagens ou títulos —
questão de prova não tem.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# Moeda e fórmula reconhecidas numa varredura só, e a ordem das alternativas é
# o que resolve o caso difícil: a moeda aparece **dentro** da matemática
# (`$M(10) \approx R\$\,8.881$`) e também fora dela (`pagou R$ 13,00`).
#
# Separar em dois passos falha nos dois sentidos. Normalizar a moeda antes
# estraga a fórmula que a contém; extrair a matemática antes tropeça no `R$`
# cru, que desbalanceia os delimitadores. Varrendo da esquerda para a direita,
# a fórmula é consumida inteira a partir do `$` que a abre — então o `R\$` de
# dentro nunca chega a ser testado como moeda — e o `R$` solto do texto casa
# com a primeira alternativa.
#
# `(?:[^$\\]|\\.)` é o que faz a fórmula não terminar num cifrão escapado.
MOEDA_OU_MATEMATICA = re.compile(
    r"R\\?\$\s*(?=\d)"                     # moeda: R$ só antes de número
    r"|\$\$(?:[^$\\]|\\.)+?\$\$"           # display
    r"|\\\[(?:[^\\]|\\.)+?\\\]"
    r"|\$(?:[^$\n\\]|\\.)+?\$"             # inline
    r"|\\\((?:[^\\]|\\.)+?\\\)",
    re.S,
)

_ITEM_DE_LISTA = re.compile(r"^\s*[-*+]\s+\S")
_SEPARADOR_DE_TABELA = re.compile(r"^[\s|:-]+$")


@dataclass(frozen=True)
class Trecho:
    """Pedaço de uma linha. `tipo`: "texto", "negrito" ou "matematica"."""

    tipo: str
    conteudo: str
    display: bool = False  # só para matemática: veio de `$$...$$` ou `\[...\]`


@dataclass(frozen=True)
class Bloco:
    """Bloco de conteúdo. `tipo`: "paragrafo", "formula", "lista" ou "tabela".

    `linhas` guarda as linhas do parágrafo e os itens da lista; `celulas` guarda
    a tabela, linha a linha; `formula` guarda o LaTeX já sem os delimitadores.
    """

    tipo: str
    linhas: list[list[Trecho]] = field(default_factory=list)
    celulas: list[list[list[Trecho]]] = field(default_factory=list)
    formula: str = ""


def _sem_delimitadores(trecho: str) -> tuple[str, bool]:
    """Tira os `$`, `$$`, `\\(` ou `\\[` e diz se a fórmula era de display."""
    for abre, fecha, display in (("$$", "$$", True), (r"\[", r"\]", True),
                                 (r"\(", r"\)", False), ("$", "$", False)):
        if trecho.startswith(abre) and trecho.endswith(fecha):
            return trecho[len(abre):-len(fecha)].strip(), display
    return trecho, False


def _matematica(texto: str, negrito: bool) -> list[Trecho]:
    """Separa fórmula de prosa numa faixa de texto já classificada."""
    prosa = "negrito" if negrito else "texto"
    trechos: list[Trecho] = []
    pos = 0
    for m in MOEDA_OU_MATEMATICA.finditer(texto):
        if m.start() > pos:
            trechos.append(Trecho(prosa, texto[pos:m.start()]))
        achado = m.group(0)
        if achado.startswith("R"):
            # A moeda é texto, e o LLM escreve ora "R$ 20,00" ora "R$20,00".
            trechos.append(Trecho(prosa, "R$ "))
        else:
            formula, display = _sem_delimitadores(achado)
            trechos.append(Trecho("matematica", formula, display))
        pos = m.end()
    if pos < len(texto):
        trechos.append(Trecho(prosa, texto[pos:]))
    return trechos


def inline(texto: str) -> list[Trecho]:
    """Uma linha de Markdown-com-matemática nos seus trechos.

    O negrito é lido **antes** da matemática porque ele a contém, e não o
    contrário: `**R$ 35,00**` e `**b) Valores em $x=10$**` são o formato normal
    do Gerador. Lendo a matemática primeiro, os dois asteriscos caíam em faixas
    diferentes e o negrito nunca fechava — apareciam crus na tela. O inverso não
    acontece: nas 90 questões do acervo não há um único `**` dentro de fórmula.
    """
    trechos: list[Trecho] = []
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*", texto, flags=re.S):
        if m.start() > pos:
            trechos += _matematica(texto[pos:m.start()], negrito=False)
        trechos += _matematica(m.group(1), negrito=True)
        pos = m.end()
    if pos < len(texto):
        trechos += _matematica(texto[pos:], negrito=False)
    return trechos


def _celulas(linha: str) -> list[list[Trecho]]:
    return [inline(c.strip()) for c in linha.strip().strip("|").split("|")]


def analisar(texto: str) -> list[Bloco]:
    """O texto do Gerador nos seus blocos, na ordem em que aparecem."""
    blocos: list[Bloco] = []
    linhas = (texto or "").split("\n")
    i = 0
    while i < len(linhas):
        linha = linhas[i]

        if not linha.strip():
            i += 1
            continue

        if linha.lstrip().startswith("|"):
            corpo = []
            while i < len(linhas) and linhas[i].lstrip().startswith("|"):
                # A linha `|---|---|` existe no Markdown só para marcar o
                # cabeçalho: vira formatação, não vira uma linha da tabela.
                if not _SEPARADOR_DE_TABELA.fullmatch(linhas[i].strip()):
                    corpo.append(_celulas(linhas[i]))
                i += 1
            if corpo:
                largura = max(len(l) for l in corpo)
                corpo = [l + [[]] * (largura - len(l)) for l in corpo]
                blocos.append(Bloco("tabela", celulas=corpo))
            continue

        if _ITEM_DE_LISTA.match(linha):
            itens = []
            while i < len(linhas) and _ITEM_DE_LISTA.match(linhas[i]):
                itens.append(inline(re.sub(r"^\s*[-*+]\s+", "", linhas[i])))
                i += 1
            blocos.append(Bloco("lista", linhas=itens))
            continue

        # Fórmula sozinha na linha vira bloco próprio — pode abrir numa linha e
        # fechar em outra, e é assim que o `\begin{cases}` costuma chegar.
        if linha.strip().startswith("$$") or linha.strip().startswith(r"\["):
            bloco = [linhas[i]]
            fecha = "$$" if linha.strip().startswith("$$") else r"\]"
            enquanto_abre = linha.strip() == "$$" or not linha.strip().endswith(fecha)
            while enquanto_abre and i + 1 < len(linhas):
                i += 1
                bloco.append(linhas[i])
                if linhas[i].strip().endswith(fecha):
                    break
            i += 1
            formula, _ = _sem_delimitadores("\n".join(bloco).strip())
            blocos.append(Bloco("formula", formula=formula))
            continue

        paragrafo = []
        while i < len(linhas) and linhas[i].strip():
            atual = linhas[i]
            if (atual.lstrip().startswith("|") or _ITEM_DE_LISTA.match(atual)
                    or atual.strip().startswith("$$")):
                break
            paragrafo.append(inline(atual))
            i += 1
        if paragrafo:
            blocos.append(Bloco("paragrafo", linhas=paragrafo))

    return blocos
