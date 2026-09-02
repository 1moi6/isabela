"""Converte o Markdown-com-matemática que o Gerador escreve em LaTeX compilável.

O Gerador devolve enunciado e gabarito em Markdown, com a matemática em `$...$`.
Injetar isso direto num `.tex` — que é o que `listas.py` fazia — não compila. As
três armadilhas, todas medidas no acervo de 90 questões:

1. **`R$` abre modo matemático.** O acervo traz 88 ocorrências cruas de `R$` e
   28 já escapadas como `R\\$`: o LLM não é consistente, e pedir consistência no
   prompt não é garantia. Em 32 dos 360 campos os `$` ficam desbalanceados por
   causa disso — e aí *toda* a separação entre texto e fórmula desanda. Por isso
   a moeda é normalizada **antes** de procurar matemática.
2. **Texto e fórmula pedem tratamento oposto.** Fora da matemática, `_ ^ & % #
   { } \\` são caracteres especiais e precisam ser escapados; dentro, são a
   própria notação e precisam passar intactos.
3. **Tabela de Markdown não existe em LaTeX.** As questões de tarifa por faixa
   somam 348 pipes; sem conversão, saem como texto corrido cheio de barras.

Símbolos fora do modo matemático: com `T1`+`utf8`+`textcomp`, `² ³ · × – —`
compilam sozinhos. Os de `SIMBOLOS` derrubam o pdflatex ("Unicode character not
set up for use with LaTeX") e por isso viram matemática; o que não estiver em
nenhuma das duas listas cai em `_sobreviventes`, porque o erro é fatal.

A expressão que separa moeda de fórmula mora em `marcacao.py`, com os outros
leitores desse mesmo Markdown — aqui ela é só importada.
"""

from __future__ import annotations

import re

from .marcacao import MOEDA_OU_MATEMATICA as _MOEDA_OU_MATEMATICA

# Marcadores que não podem aparecer no texto de origem. Caracteres de controle
# servem: o JSON do LLM nunca os traz, e o `\x00` sequer é válido em JSON.
_MARCA_MATEMATICA = "\x00M{}\x00"
_MARCA_MOEDA = "\x00R\x00"

SIMBOLOS = {
    "≤": r"\le", "≥": r"\ge", "≠": r"\neq", "≈": r"\approx", "∞": r"\infty",
    "±": r"\pm", "→": r"\to", "∈": r"\in", "∉": r"\notin", "⊂": r"\subset",
    "∪": r"\cup", "∩": r"\cap", "√": r"\surd", "∑": r"\sum", "∏": r"\prod",
    "ℝ": r"\mathbb{R}", "ℕ": r"\mathbb{N}", "ℤ": r"\mathbb{Z}", "ℚ": r"\mathbb{Q}",
    "π": r"\pi", "α": r"\alpha", "β": r"\beta", "γ": r"\gamma", "θ": r"\theta",
    "λ": r"\lambda", "μ": r"\mu", "σ": r"\sigma", "ω": r"\omega",
    "Δ": r"\Delta", "Σ": r"\Sigma", "Ω": r"\Omega", "°": r"^\circ",
    # A resolução usa ✓ para marcar a conferência de cada passo — 41 ocorrências
    # no acervo, em 16 questões, e cada uma derrubava o pdflatex. O sinal de
    # menos tipográfico (U+2212) vem colado no número e engana os olhos: parece
    # o hífen do teclado e não é.
    "✓": r"\checkmark", "✗": r"\times", "−": "-", "⇒": r"\Rightarrow",
    "⇔": r"\Leftrightarrow", "≡": r"\equiv", "≅": r"\cong", "∅": r"\emptyset",
    "∀": r"\forall", "∃": r"\exists", "∫": r"\int", "∂": r"\partial",
    "∠": r"\angle", "⊆": r"\subseteq", "⊃": r"\supset", "⊇": r"\supseteq",
    "∧": r"\wedge", "∨": r"\vee", "∼": r"\sim", "∝": r"\propto",
    "δ": r"\delta", "ε": r"\varepsilon", "ζ": r"\zeta", "η": r"\eta",
    "ι": r"\iota", "κ": r"\kappa", "ν": r"\nu", "ξ": r"\xi", "ρ": r"\rho",
    "τ": r"\tau", "υ": r"\upsilon", "φ": r"\varphi", "χ": r"\chi", "ψ": r"\psi",
    "Γ": r"\Gamma", "Λ": r"\Lambda", "Ξ": r"\Xi", "Π": r"\Pi", "Φ": r"\Phi",
    "Ψ": r"\Psi", "Θ": r"\Theta",
}

# Já compilam sozinhos com T1+utf8+textcomp (ver o cabeçalho do módulo), junto
# de todo o alfabeto latino acentuado — que é o que a prosa em português usa.
_TIPOGRAFICOS = "²³·×÷–—°ºª«»“”‘’…§¶€£¢¡¿†‡•‰"

ESPECIAIS = {
    "\\": r"\textbackslash{}",  # antes dos demais: senão escaparia as próprias barras
    "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "$": r"\$",
    "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def _sobreviventes(texto: str) -> str:
    """Descarta o que sobrou fora de `SIMBOLOS` e derrubaria o pdflatex.

    A tabela acima é uma lista, e lista fica para trás: o Gerador escolhe os
    símbolos, e nenhum prompt garante que ele fique dentro do previsto. Sem esta
    rede, um glifo novo vira erro **fatal** ("Unicode character not set up for
    use with LaTeX") e o professor recebe um `.tex` que não abre — foi o que
    aconteceu com o ✓ em 16 das 85 questões do acervo. Um caractere decorativo a
    menos é perda pequena; um arquivo que não compila é perda total.
    """
    return "".join(
        c for c in texto
        if ord(c) < 0x180 or c in _TIPOGRAFICOS  # latino + acentos + tipografia
    )


def _escapar(texto: str) -> str:
    """Escapa o que é especial em LaTeX. Só se aplica a trecho FORA da matemática."""
    for bruto, escapado in ESPECIAIS.items():
        texto = texto.replace(bruto, escapado)
    for simbolo, comando in SIMBOLOS.items():
        texto = texto.replace(simbolo, f"${comando}$")
    return _sobreviventes(texto)


def _tabela(linhas: list[str]) -> str:
    """Bloco de tabela em Markdown para `tabular`.

    A linha de separação (`|---|---|`) é descartada; ela existe no Markdown só
    para marcar o cabeçalho. Colunas em `p{}` e não em `l` porque a segunda
    coluna das tabelas de tarifa é uma frase inteira, e com `l` a tabela estoura
    a margem sem avisar — o pdflatex trata isso como advertência, não erro.
    """
    def celulas(linha: str) -> list[str]:
        return [c.strip() for c in linha.strip().strip("|").split("|")]

    corpo = [celulas(l) for l in linhas if not re.fullmatch(r"[\s|:-]+", l)]
    if not corpo:
        return ""
    n = max(len(l) for l in corpo)
    largura = 0.86 / n
    formato = "|" + f"p{{{largura:.3f}\\linewidth}}|" * n

    partes = [r"\begin{center}", rf"\begin{{tabular}}{{{formato}}}", r"\hline"]
    for i, linha in enumerate(corpo):
        linha = linha + [""] * (n - len(linha))
        conteudo = " & ".join(rf"\textbf{{{c}}}" for c in linha) if i == 0 else " & ".join(linha)
        partes += [conteudo + r" \\", r"\hline"]
    partes += [r"\end{tabular}", r"\end{center}"]
    return "\n".join(partes)


def _blocos(texto: str) -> str:
    """Listas e tabelas do Markdown, que são estrutura e não marcação inline."""
    saida: list[str] = []
    linhas = texto.split("\n")
    i = 0
    while i < len(linhas):
        linha = linhas[i]
        if linha.lstrip().startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].lstrip().startswith("|"):
                bloco.append(linhas[i])
                i += 1
            saida.append(_tabela(bloco))
            continue
        if re.match(r"^\s*[-*+]\s+\S", linha):
            bloco = []
            while i < len(linhas) and re.match(r"^\s*[-*+]\s+\S", linhas[i]):
                bloco.append(re.sub(r"^\s*[-*+]\s+", "", linhas[i]))
                i += 1
            saida.append(r"\begin{itemize}[nosep,leftmargin=*]")
            saida += [rf"\item {item}" for item in bloco]
            saida.append(r"\end{itemize}")
            continue
        saida.append(linha)
        i += 1
    return "\n".join(saida)


def para_tex(texto: str) -> str:
    """Markdown com matemática → corpo LaTeX pronto para incluir num documento."""
    if not texto:
        return ""

    formulas: list[str] = []

    def guardar(m: re.Match) -> str:
        trecho = m.group(0)
        if trecho.startswith("R"):
            return _MARCA_MOEDA
        formulas.append(trecho)
        return _MARCA_MATEMATICA.format(len(formulas) - 1)

    texto = _MOEDA_OU_MATEMATICA.sub(guardar, texto)

    # O que sobrou é texto de verdade, e só ele é escapado.
    texto = _escapar(texto)
    texto = _blocos(texto)
    texto = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", texto, flags=re.S)

    # Devolve a matemática — quase intacta: dentro dela o símbolo solto derruba o
    # pdflatex do mesmo jeito, só que já em modo matemático, e aí vai sem os `$`.
    for n, formula in enumerate(formulas):
        for simbolo, comando in SIMBOLOS.items():
            if simbolo in formula:
                formula = formula.replace(simbolo, f"{comando} ")
        texto = texto.replace(_MARCA_MATEMATICA.format(n), _sobreviventes(formula))
    # Espaço fino inseparável: o LLM escreve ora "R$ 20,00" ora "R$20,00", e a
    # quebra de linha entre o símbolo e o valor é feia justamente na prova.
    return texto.replace(_MARCA_MOEDA, r"R\$\,")


PREAMBULO = r"""\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[brazil]{babel}
\usepackage{amsmath,amssymb,textcomp}
\usepackage[margin=2.2cm]{geometry}
\usepackage{enumitem}
\usepackage{array}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
"""


def compilar(tex: str, destino, nome: str) -> bool:
    """Compila para PDF ao lado do `.tex`. Devolve se o PDF saiu.

    Não levanta exceção: sem toolchain de LaTeX na máquina — que é o caso comum
    no computador do professor — o `.tex` continua servindo, e é melhor entregar
    a fonte com um aviso do que interromper a geração do material inteiro.
    """
    import shutil
    import subprocess
    from pathlib import Path

    destino = Path(destino)
    fonte = destino / f"{nome}.tex"
    fonte.write_text(tex, encoding="utf-8")
    if not shutil.which("pdflatex"):
        return False

    for _ in range(2):  # duas passagens: a tabela precisa da segunda para medir
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", f"{nome}.tex"],
            cwd=destino, capture_output=True,
        )
    for lixo in (".aux", ".log", ".out"):
        (destino / f"{nome}{lixo}").unlink(missing_ok=True)
    return (destino / f"{nome}.pdf").exists()
