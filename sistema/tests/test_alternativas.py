"""Testes do sorteio da ordem das alternativas.

O defeito que motivou o sorteio foi visto por um professor do painel: a correta
era a (a) em 38 das 43 questões de múltipla escolha. O risco do conserto é outro,
e pior: trocar a ordem sem trocar a letra citada no gabarito, que passaria a
apontar para um distrator sem que nada acusasse.
"""

import json
from collections import Counter

from questoes.agentes import Gerador
from questoes.alternativas import embaralhar
from questoes.especificacao import (
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema,
)
from questoes.modelos import Alternativa, Questao

from test_orquestrador import LLMFake

SPEC = Especificacao(
    tema=Tema.FUNCAO_AFIM,
    habilidade_bncc="EM13MAT302",
    nivel_bloom=NivelBloom.APLICAR,
    dificuldade=Dificuldade.FACIL,
    natureza=Natureza.APLICADA,
    formato=Formato.MULTIPLA_ESCOLHA,
)


def _questao(enunciado="Quanto custa uma revisão de 8 horas?", gabarito="R$ 450,00",
             resolucao="Taxa de R$ 50,00 por hora mais R$ 50,00 fixos."):
    return Questao(
        enunciado=enunciado,
        resolucao=resolucao,
        gabarito=gabarito,
        alternativas=[
            Alternativa(texto="R$ 450,00", correta=True),
            Alternativa(texto="R$ 400,00", erro_representado="esqueceu o fixo"),
            Alternativa(texto="R$ 600,00", erro_representado="proporcionalidade direta"),
            Alternativa(texto="R$ 500,00", erro_representado="contou uma hora a mais"),
        ],
        especificacao=SPEC,
    )


def _letra_da_correta(q: Questao) -> str:
    return "abcd"[[a.correta for a in q.alternativas].index(True)]


def test_a_correta_deixa_de_ficar_sempre_na_primeira_posicao():
    posicoes = Counter(
        _letra_da_correta(embaralhar(_questao(enunciado=f"Questão número {i}.")))
        for i in range(200)
    )
    assert set(posicoes) == set("abcd")
    assert posicoes["a"] < 100  # sem o sorteio, seriam as 200


def test_a_mesma_questao_sai_sempre_na_mesma_ordem():
    """Semente do enunciado, não do relógio: testes e medições continuam reproduzíveis."""
    assert embaralhar(_questao()).alternativas == embaralhar(_questao()).alternativas


def test_conteudo_das_alternativas_nao_muda():
    original = _questao()
    sorteada = embaralhar(original)
    chave = lambda a: a.texto  # noqa: E731
    assert sorted(sorteada.alternativas, key=chave) == sorted(original.alternativas, key=chave)


def test_letra_citada_no_gabarito_e_na_resolucao_acompanha_a_correta():
    for i in range(40):
        q = embaralhar(_questao(
            enunciado=f"Questão {i}.",
            gabarito="R$ 450,00 (alternativa A)",
            resolucao="Logo, a resposta é a alternativa (a); a letra B esquece o fixo.",
        ))
        certa = _letra_da_correta(q)
        assert f"(alternativa {certa.upper()})" in q.gabarito
        assert f"alternativa ({certa})" in q.resolucao
        # a (b) original, que esquecia o fixo, também é renumerada
        esquece = "abcd"[[a.texto for a in q.alternativas].index("R$ 400,00")]
        assert f"letra {esquece.upper()}" in q.resolucao


def test_gabarito_que_e_so_a_letra_ou_comeca_por_ela():
    """No acervo havia gabaritos como "A" e "D) Domínio = ...": são os mais fáceis de quebrar."""
    for i in range(40):
        so_letra = embaralhar(_questao(enunciado=f"Questão {i}.", gabarito="A"))
        assert so_letra.gabarito == _letra_da_correta(so_letra).upper()

        com_letra = embaralhar(_questao(enunciado=f"Questão {i}.", gabarito="A) R$ 450,00"))
        assert com_letra.gabarito == f"{_letra_da_correta(com_letra).upper()}) R$ 450,00"


def test_item_de_questao_e_expressao_nao_sao_confundidos_com_alternativa():
    """"Item a)" e "(7-2a)" têm a cara de letra de alternativa e não são."""
    resolucao = "**Item a)** Calcule $f(7-2a)$ e depois $(b)$ como parâmetro."
    for i in range(20):
        q = embaralhar(_questao(enunciado=f"Questão {i}.", resolucao=resolucao))
        assert q.resolucao == resolucao


def test_discursiva_passa_intacta():
    q = _questao().model_copy(update={"alternativas": None})
    assert embaralhar(q) == q


def test_gerador_entrega_a_questao_ja_sorteada():
    """A ordem é sorteada antes do Crítico, para ele ver o que o professor verá."""
    posicoes = Counter()
    for i in range(40):
        resposta = json.dumps({
            "enunciado": f"Quanto custa uma revisão de 8 horas? (variante {i})",
            "resolucao": "Por isso a alternativa A.",
            "gabarito": "R$ 450,00 (alternativa A)",
            "alternativas": [
                {"texto": "R$ 450,00", "correta": True, "erro_representado": None},
                {"texto": "R$ 400,00", "correta": False, "erro_representado": "x"},
                {"texto": "R$ 600,00", "correta": False, "erro_representado": "y"},
                {"texto": "R$ 500,00", "correta": False, "erro_representado": "z"},
            ],
            "verificaveis": [],
        })
        q = Gerador(LLMFake([resposta])).gerar(SPEC)
        certa = _letra_da_correta(q)
        posicoes[certa] += 1
        assert f"alternativa {certa.upper()}" in q.gabarito
        assert f"alternativa {certa.upper()}" in q.resolucao
    assert posicoes["a"] < 40
