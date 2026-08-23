"""Conversão do Markdown-com-matemática do Gerador para LaTeX.

Os casos aqui não são hipotéticos: cada um saiu do acervo de 90 questões, e
quase todos derrubavam o pdflatex antes de existir `tex.py`. Onde houver
`pdflatex` na máquina, o teste final compila de verdade — é a única forma de
saber que o resultado serve, já que uma string plausível não prova nada.
"""

from __future__ import annotations

import shutil

import pytest

from questoes.tex import PREAMBULO, compilar, para_tex


# --- moeda: a armadilha central ---------------------------------------------
#
# O acervo traz 88 `R$` crus e 28 já escapados. O cru desbalanceia os
# delimitadores de matemática, e aí a separação entre texto e fórmula desanda no
# campo inteiro.


def test_moeda_crua_e_escapada():
    assert para_tex("pagou R$ 13,00") == r"pagou R\$\,13,00"
    assert para_tex(r"pagou R\$ 13,00") == r"pagou R\$\,13,00"
    assert para_tex("custou R$6.000,00") == r"custou R\$\,6.000,00"


def test_moeda_dentro_da_matematica_nao_quebra_a_formula():
    """`$M(10) \\approx R\\$\\,8.881$` derrubava a compilação: a regex parava no
    cifrão escapado e o resto do campo virava texto escapado."""
    entrada = r"b) $M(10) \approx R\$\,8.881{,}47$; c) $t = 18$"
    assert para_tex(entrada) == entrada


def test_variavel_R_nao_e_confundida_com_moeda():
    """`$R$` termina em `R$`. Só é moeda o que vem antes de um número."""
    assert para_tex(r"o domínio de $R$ é $\mathbb{R}$") == r"o domínio de $R$ é $\mathbb{R}$"


# --- texto e fórmula pedem tratamento oposto --------------------------------


def test_especiais_do_texto_sao_escapados():
    assert para_tex("50% de 3_4 & 5 # 6") == r"50\% de 3\_4 \& 5 \# 6"


def test_matematica_passa_intacta():
    entrada = r"Considere $f(x) = 3\sin(x) - 1$ e $[0,+\infty)$"
    assert para_tex(entrada) == entrada


def test_display_e_delimitadores_alternativos():
    assert para_tex(r"logo $$x^2 = 4$$ segue") == r"logo $$x^2 = 4$$ segue"
    assert para_tex(r"seja \(y = 2\) fim") == r"seja \(y = 2\) fim"


@pytest.mark.parametrize("simbolo,comando", [("≤", r"\le"), ("∞", r"\infty"), ("ℝ", r"\mathbb{R}")])
def test_simbolo_solto_vira_matematica(simbolo, comando):
    """Fora do modo matemático, o pdflatex recusa estes com 'Unicode character
    not set up' — erro fatal, não advertência."""
    assert para_tex(f"valor {simbolo} 5") == f"valor ${comando}$ 5"


def test_superscrito_unicode_fica_como_esta():
    """`m³` e `²` compilam sozinhos com T1+utf8+textcomp; não há o que converter."""
    assert para_tex("consumo em m³ e área em m²") == "consumo em m³ e área em m²"


# --- estrutura ---------------------------------------------------------------


def test_tabela_vira_tabular():
    entrada = "| Consumo | Regra |\n|---|---|\n| $x \\le 10$ | R$ 20,00 |"
    saida = para_tex(entrada)
    assert r"\begin{tabular}" in saida and r"\end{tabular}" in saida
    assert r"\textbf{Consumo} & \textbf{Regra}" in saida
    assert r"$x \le 10$ & R\$\,20,00" in saida
    assert "|---|" not in saida


def test_lista_vira_itemize():
    saida = para_tex("- primeiro\n- segundo $x^2$")
    assert saida.startswith(r"\begin{itemize}")
    assert r"\item segundo $x^2$" in saida


def test_negrito():
    assert para_tex("**Atenção:** leia") == r"\textbf{Atenção:} leia"


def test_texto_vazio():
    assert para_tex("") == ""


# --- a prova real ------------------------------------------------------------


@pytest.mark.skipif(not shutil.which("pdflatex"), reason="requer pdflatex")
def test_o_resultado_compila_de_verdade(tmp_path):
    """Reúne num documento só todas as armadilhas medidas no acervo."""
    trechos = [
        r"Marina investiu R$6.000,00 com taxa de 4% ao mês (3_4 & 5 # 6).",
        r"b) $M(10) \approx R\$\,8.881{,}47$; c) $t = 18$",
        "Consumo em m³, com valor ≤ 35 e domínio ℝ, tendendo a ∞.",
        "| Consumo mensal | Regra de cobrança |\n|---|---|\n"
        r"| $0 \le x \le 10$ | taxa fixa de R\$ 20,00 |" + "\n"
        r"| $x > 20$ | R$ 50,00 mais R$ 5,00 por m³ |",
        "- primeiro item\n- segundo item com $\\dfrac{1}{2}$",
        r"**Atenção:** o gráfico de $f$ tem imagem $[-4, 2]$ e período $2\pi$.",
    ]
    corpo = "\n\n".join(para_tex(t) for t in trechos)
    tex = PREAMBULO + "\\begin{document}\n" + corpo + "\n\\end{document}"
    assert compilar(tex, tmp_path, "prova"), (tmp_path / "prova.tex").read_text()


@pytest.mark.skipif(not shutil.which("pdflatex"), reason="requer pdflatex")
def test_lista_de_exercicios_compila(tmp_path):
    """O botão 'LaTeX' da interface entregava arquivo que não compilava."""
    from questoes.listas import para_latex

    from test_orquestrador import _questao_json
    import json

    from questoes.modelos import Questao

    dados = json.loads(_questao_json())
    dados["enunciado"] = "Um cliente pagou R$ 13,00 por 4 km, com desconto de 10%."
    dados["gabarito"] = r"$C(d) = 2d + 5$, com $d \ge 0$"
    dados["especificacao"] = {
        "habilidade_bncc": "EM13MAT302", "temas": ["funcao_afim"],
        "nivel_bloom": "aplicar", "dificuldade": "media",
        "natureza": "aplicada", "formato": "discursiva",
    }
    q = Questao.model_validate(dados)
    assert compilar(para_latex("Lista 1", [q], com_gabarito=True), tmp_path, "lista")
