"""Montagem e exportação de listas de exercícios a partir do banco curado.

Exporta em Markdown (uso direto/conversão) e LaTeX (impressão via pdflatex),
com versão do aluno (sem gabarito) e do professor (com resolução).
"""

from __future__ import annotations

from .modelos import Questao

_CABECALHO_LATEX = r"""\documentclass[12pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazil]{babel}
\usepackage{amsmath,amssymb}
\usepackage{enumitem}
\begin{document}
"""


def para_markdown(
    titulo: str, questoes: list[Questao], com_gabarito: bool = False
) -> str:
    """Lista em Markdown. `com_gabarito=True` gera a versão do professor."""
    partes = [f"# {titulo}", ""]
    for i, q in enumerate(questoes, start=1):
        partes.append(f"**Questão {i}.** {q.enunciado}")
        if q.alternativas:
            for letra, alt in zip("abcd", q.alternativas):
                partes.append(f"- ({letra}) {alt.texto}")
        partes.append("")
    if com_gabarito:
        partes += ["---", "", "## Gabarito e resoluções", ""]
        for i, q in enumerate(questoes, start=1):
            partes.append(f"**Questão {i}.** {q.gabarito}")
            partes.append("")
            partes.append(q.resolucao)
            partes.append("")
    return "\n".join(partes)


def para_latex(titulo: str, questoes: list[Questao], com_gabarito: bool = False) -> str:
    """Lista em LaTeX pronta para pdflatex."""
    partes = [_CABECALHO_LATEX, rf"\section*{{{titulo}}}", r"\begin{enumerate}[label=\textbf{\arabic*.}]"]
    for q in questoes:
        partes.append(rf"\item {q.enunciado}")
        if q.alternativas:
            partes.append(r"\begin{enumerate}[label=(\alph*)]")
            partes += [rf"\item {alt.texto}" for alt in q.alternativas]
            partes.append(r"\end{enumerate}")
    partes.append(r"\end{enumerate}")
    if com_gabarito:
        partes += [r"\newpage", r"\section*{Gabarito e resoluções}",
                   r"\begin{enumerate}[label=\textbf{\arabic*.}]"]
        for q in questoes:
            partes.append(rf"\item {q.gabarito}")
            partes.append("")
            partes.append(q.resolucao)
        partes.append(r"\end{enumerate}")
    partes.append(r"\end{document}")
    return "\n".join(partes)
