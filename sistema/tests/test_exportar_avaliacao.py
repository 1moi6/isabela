"""O material do avaliador: cobertura, distribuição e — sobretudo — sigilo.

O risco que estes testes cobrem não dá erro nem aparece na tela: um documento
que carregue a resolução, o rótulo de garantia ou o parecer do Crítico continua
sendo um documento bonito. Só que o professor lê a crítica antes de julgar, e a
sessão inteira passa a medir concordância com o Crítico. Quando isso se descobre,
já se gastou o tempo de cinco pessoas que não voltam.
"""

from __future__ import annotations

import csv
import json
import random
import re

import pytest

import exportar_avaliacao as exp

from test_orquestrador import _questao_json


def _ciclo(n: int, habilidade="EM13MAT302", dificuldade="media", aprovada=True) -> dict:
    q = json.loads(_questao_json())
    q["enunciado"] = f"Enunciado da questão {n}."
    q["resolucao"] = f"RESOLUCAO SECRETA {n}: primeiro isole a incógnita e some tudo."
    q["gabarito"] = f"x = {n}"
    q["alternativas"] = [
        {"texto": f"opção {letra} do item {n}", "correta": letra == "a",
         "erro_representado": None if letra == "a" else f"ERRO SECRETO {letra}{n}"}
        for letra in "abcd"
    ]
    q["especificacao"] = {
        "habilidade_bncc": habilidade, "temas": ["funcao_afim"], "nivel_bloom": "aplicar",
        "dificuldade": dificuldade, "natureza": "aplicada", "formato": "multipla_escolha",
    }
    return {
        "aprovada": aprovada,
        "questao_final": q if aprovada else None,
        "iteracoes": [{
            "numero": 1,
            "questao": q,
            "verificacao": {
                "veredicto": "aprovado" if aprovada else "rejeitado",
                "justificativa": f"JUSTIFICATIVA SECRETA {n} do verificador simbólico.",
                "afirmacoes": [],
            },
            "parecer": {
                "aprovado": True,
                "criterios": [{"nome": "clareza", "nota": 5,
                               "comentario": f"PARECER SECRETO {n} sobre a clareza."}],
            },
        }],
    }


@pytest.fixture
def acervo(tmp_path):
    """15 habilidades × 3 dificuldades, como o acervo real, mais um descartado."""
    ciclos = []
    for h in range(15):
        for d in ("facil", "media", "dificil"):
            ciclos.append(_ciclo(len(ciclos) + 1, f"EM13MAT{300+h}", d))
    ciclos.append(_ciclo(999, "EM13MAT302", "media", aprovada=False))
    caminho = tmp_path / "ciclos.jsonl"
    caminho.write_text(
        "\n".join(json.dumps(c, ensure_ascii=False) for c in ciclos), encoding="utf-8"
    )
    return caminho


def _gerar(acervo, tmp_path, **kwargs):
    destino = tmp_path / "avaliacao"
    opcoes = {"avaliadores": 5, "ancora": 6, "semente": 1, "incluir_descartadas": False}
    exp.main(acervo, destino, **{**opcoes, **kwargs})
    docs = {p.name: p.read_text(encoding="utf-8") for p in sorted(destino.glob("avaliador-*.md"))}
    return destino, docs


def _itens(texto: str) -> list[str]:
    return re.findall(r"^### (Q\d{3})$", texto, re.M)


# --- sigilo: o que NÃO pode estar no documento -------------------------------


@pytest.mark.parametrize("segredo", [
    "RESOLUCAO SECRETA", "JUSTIFICATIVA SECRETA", "PARECER SECRETO", "ERRO SECRETO",
])
def test_documento_nao_carrega_o_que_o_avaliador_nao_pode_ver(acervo, tmp_path, segredo):
    _, docs = _gerar(acervo, tmp_path)
    for nome, texto in docs.items():
        assert segredo not in texto, f"{nome} vazou {segredo}"


def test_documento_nao_mostra_a_garantia_obtida(acervo, tmp_path):
    """P3 pergunta se o rótulo muda o julgamento; impresso na página, não dá para saber."""
    _, docs = _gerar(acervo, tmp_path)
    for texto in docs.values():
        for rotulo in ("conferido", "sem_conferencia", "nao_verificavel", "aprovado_parcial"):
            assert not re.search(rf"\b{rotulo}\b", texto)


def test_alternativa_correta_nao_vem_marcada(acervo, tmp_path):
    _, docs = _gerar(acervo, tmp_path)
    for texto in docs.values():
        assert "correta" not in texto


def test_a_chave_fica_fora_do_material(acervo, tmp_path):
    """O _chave.csv liga item a garantia; é o único arquivo que não se envia."""
    destino, docs = _gerar(acervo, tmp_path)
    chave = (destino / "_chave.csv").read_text(encoding="utf-8")
    assert "garantia" in chave and "conferido" in chave
    assert not any("_chave" in texto for texto in docs.values())


# --- cobertura e distribuição -----------------------------------------------


def test_todo_item_aprovado_chega_a_alguem(acervo, tmp_path):
    destino, docs = _gerar(acervo, tmp_path)
    vistos = {i for texto in docs.values() for i in _itens(texto)}
    da_chave = {linha["item"] for linha in csv.DictReader(open(destino / "_chave.csv"))}
    assert vistos == da_chave and len(vistos) == 45


def test_ninguem_recebe_o_mesmo_item_duas_vezes(acervo, tmp_path):
    _, docs = _gerar(acervo, tmp_path)
    for nome, texto in docs.items():
        itens = _itens(texto)
        assert len(itens) == len(set(itens)), nome


def test_a_ancora_vai_para_todos(acervo, tmp_path):
    _, docs = _gerar(acervo, tmp_path)
    comuns = set.intersection(*(set(_itens(t)) for t in docs.values()))
    assert len(comuns) == 6


def test_a_ancora_equilibra_a_dificuldade(acervo, tmp_path):
    """Saiu 5 difíceis e 1 fácil na primeira versão: é sobre a âncora que se
    compara um avaliador com o outro, então ela precisa parecer com o acervo."""
    destino, docs = _gerar(acervo, tmp_path)
    comuns = set.intersection(*(set(_itens(t)) for t in docs.values()))
    por = {l["item"]: l for l in csv.DictReader(open(destino / "_chave.csv"))}
    dificuldades = {por[i]["dificuldade"] for i in comuns}
    assert len(dificuldades) == 3


def test_descartadas_ficam_de_fora_por_omissao(acervo, tmp_path):
    destino, _ = _gerar(acervo, tmp_path)
    linhas = list(csv.DictReader(open(destino / "_chave.csv")))
    assert all(l["aprovada"] == "True" for l in linhas)
    assert len(linhas) == 45  # o 46º ciclo foi descartado


def test_descartadas_entram_quando_pedidas(acervo, tmp_path):
    """Servem de espécime de erro para o Bloco I do painel."""
    destino, _ = _gerar(acervo, tmp_path, incluir_descartadas=True)
    assert len(list(csv.DictReader(open(destino / "_chave.csv")))) == 46


# --- a planilha e a chave precisam bater com o documento --------------------


def test_planilha_repete_os_itens_do_documento_na_ordem(acervo, tmp_path):
    destino, docs = _gerar(acervo, tmp_path)
    for n, texto in enumerate(docs.values(), 1):
        linhas = [l["item"] for l in csv.DictReader(open(destino / f"respostas-avaliador-{n}.csv"))]
        assert linhas == _itens(texto)


def test_chave_registra_quem_recebeu_cada_item(acervo, tmp_path):
    """Sem isso não dá para ler as respostas por estrato depois."""
    destino, docs = _gerar(acervo, tmp_path)
    nomes = list(docs)
    for linha in csv.DictReader(open(destino / "_chave.csv")):
        esperado = sorted(
            n for n, nome in enumerate(nomes, 1) if linha["item"] in _itens(docs[nome])
        )
        assert sorted(int(x) for x in linha["avaliadores"].split()) == esperado


def test_mesma_semente_produz_a_mesma_distribuicao(acervo, tmp_path):
    """O material precisa ser reproduzível para constar da dissertação."""
    _, a = _gerar(acervo, tmp_path / "a", semente=7)
    _, b = _gerar(acervo, tmp_path / "b", semente=7)
    assert [_itens(t) for t in a.values()] == [_itens(t) for t in b.values()]


def test_semente_diferente_produz_distribuicao_diferente(acervo, tmp_path):
    _, a = _gerar(acervo, tmp_path / "a", semente=7)
    _, b = _gerar(acervo, tmp_path / "b", semente=8)
    assert [_itens(t) for t in a.values()] != [_itens(t) for t in b.values()]


def test_ancora_maior_que_o_acervo_e_recusada(acervo, tmp_path):
    with pytest.raises(SystemExit, match="não cabe"):
        _gerar(acervo, tmp_path, ancora=99)


def test_um_avaliador_recebe_o_acervo_inteiro(acervo, tmp_path):
    """O modo do painel formal: mesmos itens para todos, sem lotes."""
    _, docs = _gerar(acervo, tmp_path, avaliadores=1, ancora=0)
    assert len(_itens(next(iter(docs.values())))) == 45


def test_distribuir_nao_perde_nem_duplica_item():
    itens = [f"Q{n:03d}" for n in range(1, 91)]
    comuns, lotes = exp.distribuir(
        itens, 5, 6, random.Random(3), lambda i: (i[-1], i[-2])
    )
    todos = [i for lote in lotes for i in lote]
    assert len(todos) == 84 and len(set(todos)) == 84
    assert set(todos) | set(comuns) == set(itens)
    assert not set(todos) & set(comuns)
