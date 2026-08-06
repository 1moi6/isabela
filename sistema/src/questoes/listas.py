"""Montagem e exportação de listas de exercícios a partir do banco curado.

Exporta em Markdown (uso direto/conversão), LaTeX (impressão via pdflatex) e
Word (.docx, para quem prefere editar antes de imprimir), com versão do aluno
(sem gabarito) e do professor (com resolução).
"""

from __future__ import annotations

from io import BytesIO

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


def para_docx(titulo: str, questoes: list[Questao], com_gabarito: bool = False) -> bytes:
    """Lista em Word (.docx), pronta para editar antes de imprimir.

    Devolve os bytes do arquivo — quem chama decide se grava em disco ou envia
    pelo navegador.
    """
    from docx import Document  # dependência opcional: pip install questoes-em[docx]
    from docx.shared import Pt

    doc = Document()
    doc.add_heading(titulo, level=1)

    for i, q in enumerate(questoes, start=1):
        p = doc.add_paragraph()
        p.add_run(f"Questão {i}. ").bold = True
        p.add_run(q.enunciado)
        for letra, alt in zip("abcd", q.alternativas or []):
            item = doc.add_paragraph(f"({letra}) {alt.texto}")
            item.paragraph_format.left_indent = Pt(24)
            item.paragraph_format.space_after = Pt(2)

    if com_gabarito:
        doc.add_page_break()
        doc.add_heading("Gabarito e resoluções", level=1)
        for i, q in enumerate(questoes, start=1):
            p = doc.add_paragraph()
            p.add_run(f"Questão {i}. ").bold = True
            p.add_run(q.gabarito)
            doc.add_paragraph(q.resolucao)

    buffer = BytesIO()
    doc.save(buffer)
    return buffer.getvalue()
