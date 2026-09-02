"""Leitura do Markdown-com-matemática que o Gerador escreve.

Os casos saíram do acervo de 90 questões. O que se testa aqui é o que a página
e o `.docx` precisavam e não tinham: saber onde termina um parágrafo, o que é
tabela, o que é fórmula e o que é moeda. Sem isso o enunciado chegava ao
professor como uma linha corrida cheia de cifrões e barras verticais.
"""

from __future__ import annotations

from questoes.marcacao import analisar, inline


def tipos(trechos):
    return [(t.tipo, t.conteudo) for t in trechos]


# --- moeda contra fórmula: a mesma armadilha do LaTeX ------------------------


def test_moeda_nao_abre_formula():
    assert tipos(inline("pagou R$ 13,00 pela corrida")) == [
        ("texto", "pagou "), ("texto", "R$ "), ("texto", "13,00 pela corrida"),
    ]


def test_moeda_dentro_da_formula_fica_na_formula():
    trechos = inline(r"o montante $M \approx R\$\,8.881$ ao fim")
    assert [t.tipo for t in trechos] == ["texto", "matematica", "texto"]
    assert trechos[1].conteudo == r"M \approx R\$\,8.881"


def test_formula_inline_e_display():
    inl = inline(r"seja $x^2$ aqui")
    assert (inl[1].conteudo, inl[1].display) == ("x^2", False)
    disp = inline(r"vale $$x^2$$ sempre")
    assert (disp[1].conteudo, disp[1].display) == ("x^2", True)


# --- negrito: lido antes da matemática, porque a contém ----------------------


def test_negrito_atravessando_a_moeda():
    """`**R$ 35,00**` era o caso que deixava os asteriscos crus na tela."""
    assert tipos(inline("custará **R$ 35,00**.")) == [
        ("texto", "custará "), ("negrito", "R$ "), ("negrito", "35,00"), ("texto", "."),
    ]


def test_negrito_atravessando_a_formula():
    trechos = inline("**b) Valores em $x = 10$**")
    assert [t.tipo for t in trechos] == ["negrito", "matematica"]


# --- blocos ------------------------------------------------------------------


def test_paragrafos_separados_por_linha_em_branco():
    blocos = analisar("Primeira frase.\n\nSegunda frase.")
    assert [b.tipo for b in blocos] == ["paragrafo", "paragrafo"]


def test_linhas_do_mesmo_paragrafo_nao_se_perdem():
    """a), b) e c) chegam em linhas seguidas — e colavam numa linha só."""
    blocos = analisar("a) primeiro item\nb) segundo item")
    assert len(blocos) == 1 and len(blocos[0].linhas) == 2


def test_tabela_de_faixa_de_tarifa():
    texto = ("| Consumo | Regra |\n|---|---|\n"
             r"| $0 \le x \le 10$ | taxa fixa de R$ 20,00 |")
    (tabela,) = analisar(texto)
    assert tabela.tipo == "tabela"
    assert len(tabela.celulas) == 2                      # a linha `|---|` não conta
    assert tabela.celulas[0][0][0].conteudo == "Consumo"
    assert tabela.celulas[1][0][0].tipo == "matematica"


def test_tabela_com_linha_incompleta_vira_retangulo():
    (tabela,) = analisar("| a | b |\n|---|---|\n| só uma |")
    assert [len(l) for l in tabela.celulas] == [2, 2]


def test_lista_com_marcador():
    (lista,) = analisar("- primeiro\n- segundo")
    assert lista.tipo == "lista" and len(lista.linhas) == 2


def test_formula_em_display_vira_bloco_proprio():
    blocos = analisar("A lei é:\n\n$$C(x) = 15 + 2x$$\n\nvalendo sempre.")
    assert [b.tipo for b in blocos] == ["paragrafo", "formula", "paragrafo"]
    assert blocos[1].formula == "C(x) = 15 + 2x"


def test_formula_que_abre_numa_linha_e_fecha_noutra():
    """O `\\begin{cases}` das funções por partes costuma chegar assim."""
    texto = "$$\nC(x) = \\begin{cases} 15 + 2x, & x \\le 10 \\\\ 35, & x > 10 \\end{cases}\n$$"
    (formula,) = analisar(texto)
    assert formula.tipo == "formula" and "cases" in formula.formula


def test_texto_vazio_nao_gera_bloco():
    assert analisar("") == [] and analisar(None) == []
