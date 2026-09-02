"""Exportação para Word: a lista que o professor abre e edita.

O `.docx` era o único destino que não lia o Markdown do Gerador. O professor
recebia `$$C(x) = \\begin{cases}…$$` e `**Modelando a situação**` escritos como
código, com a), b) e c) coladas numa linha só — porque o Word engole a quebra
de linha que vem dentro de um run.

Os testes olham o XML do arquivo, e não a aparência: é lá que se vê se a
fórmula virou equação de verdade (`m:oMath`) ou se ficou como texto.
"""

from __future__ import annotations

import json
import re
import zipfile
from io import BytesIO

import pytest

from questoes.listas import para_docx
from questoes.modelos import Questao

pytest.importorskip("docx")


def _questao(**campos) -> Questao:
    from test_orquestrador import _questao_json

    dados = json.loads(_questao_json())
    dados["especificacao"] = {
        "habilidade_bncc": "EM13MAT405", "temas": ["funcao_por_partes"],
        "nivel_bloom": "aplicar", "dificuldade": "media",
        "natureza": "aplicada", "formato": "discursiva",
    }
    dados.update(campos)
    return Questao.model_validate(dados)


def _documento(questao: Questao, com_gabarito: bool = False) -> str:
    bytes_docx = para_docx("Lista 1", [questao], com_gabarito=com_gabarito)
    with zipfile.ZipFile(BytesIO(bytes_docx)) as z:
        return z.read("word/document.xml").decode("utf-8")


def _textos(xml: str) -> list[str]:
    """Só o texto comum (`w:t`) — a equação vive em `m:t` e fica de fora."""
    return re.findall(r"<w:t[^>]*>(.*?)</w:t>", xml)


def test_formula_vira_equacao_do_word():
    xml = _documento(_questao(enunciado=r"A lei é $C(x) = 15 + 2x$ no trecho."))
    assert "<m:oMath>" in xml
    assert not any("$" in t for t in _textos(xml))


def test_formula_em_display_tambem():
    xml = _documento(_questao(
        enunciado="A lei é:\n\n$$C(x) = \\begin{cases} 15 + 2x, & x \\le 10 \\\\ 35, & x > 10 \\end{cases}$$"))
    assert xml.count("<m:oMath>") >= 1
    assert not any("cases" in t for t in _textos(xml))


def test_negrito_vira_negrito():
    xml = _documento(_questao(enunciado="**Atenção:** leia o enunciado."))
    assert "Atenção:" in _textos(xml)
    assert not any("**" in t for t in _textos(xml))


def test_tabela_de_markdown_vira_tabela_do_word():
    xml = _documento(_questao(enunciado=(
        "Segundo a tabela:\n\n| Consumo | Regra |\n|---|---|\n"
        "| até 10 | taxa fixa |\n| acima de 10 | R$ 3,00 por m³ |")))
    assert "<w:tbl>" in xml
    assert not any(t.strip().startswith("|") for t in _textos(xml))


def test_itens_em_linhas_diferentes_nao_colam():
    """Sem a quebra explícita, o Word junta a), b) e c) num parágrafo só."""
    xml = _documento(_questao(enunciado="a) primeiro\nb) segundo"))
    assert "<w:br/>" in xml


def test_moeda_continua_texto():
    xml = _documento(_questao(enunciado="Um cliente pagou R$ 13,00 pela corrida."))
    assert any("R$" in t for t in _textos(xml))


def test_resolucao_so_aparece_com_gabarito():
    q = _questao(enunciado="Enunciado.", resolucao="Passo a passo secreto.")
    assert "secreto" not in _documento(q, com_gabarito=False)
    assert "secreto" in _documento(q, com_gabarito=True)


def test_formula_invalida_nao_derruba_a_exportacao():
    """LaTeX que as bibliotecas não leem cai para texto — a lista sai assim mesmo."""
    xml = _documento(_questao(enunciado=r"Considere $\zzz{[[$ nesta linha."))
    assert "Considere" in "".join(_textos(xml))
