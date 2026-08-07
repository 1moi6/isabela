"""Agregação de várias afirmações verificáveis numa questão (Fase 0 do plano).

Uma questão que articula dois temas faz duas afirmações. Antes, o contrato
guardava uma só: o SymPy conferia metade e a outra passava sem conferência
nenhuma — silenciosamente. Aqui se testa a conjunção que fecha esse buraco.
"""

from questoes.agentes import VerificadorSimbolico
from questoes.especificacao import (
    Dificuldade, Especificacao, Formato, Garantia, Natureza, NivelBloom, Tema,
)
from questoes.modelos import ExpressaoVerificavel, Questao, Veredicto, garantia_de

SPEC = Especificacao(
    habilidade_bncc="EM13MAT507",
    temas=[Tema.PROGRESSAO_ARITMETICA, Tema.FUNCAO_AFIM],
    nivel_bloom=NivelBloom.ANALISAR, dificuldade=Dificuldade.MEDIA,
    natureza=Natureza.TEORICA, formato=Formato.DISCURSIVA,
)

TERMO_CERTO = ExpressaoVerificavel(
    tipo="progressao", expressao="-", resposta_esperada="23",
    parametros={"tipo_progressao": "pa", "a1": "5", "razao": "2", "n": "10", "consulta": "termo"},
)
TERMO_ERRADO = ExpressaoVerificavel(
    tipo="progressao", expressao="-", resposta_esperada="99",
    parametros={"tipo_progressao": "pa", "a1": "5", "razao": "2", "n": "10", "consulta": "termo"},
)
AFIM_ASSOCIADA = ExpressaoVerificavel(
    tipo="propriedade", expressao="-", incognitas=["n"], resposta_esperada="2*n + 3",
    parametros={"sequencia": "pa", "a1": "5", "razao": "2"},
)
SEM_PREDICADO = ExpressaoVerificavel(
    tipo="propriedade", expressao="-", incognitas=["n"], resposta_esperada="2*n + 3",
)


def _questao(*verificaveis):
    return Questao(
        enunciado="...", resolucao="...", gabarito="23",
        verificaveis=list(verificaveis), especificacao=SPEC,
    )


def test_todas_conferidas_aprova():
    r = VerificadorSimbolico().verificar(_questao(TERMO_CERTO, AFIM_ASSOCIADA))
    assert r.veredicto == Veredicto.APROVADO
    assert garantia_de(r.veredicto) == Garantia.CONFERIDO


def test_uma_reprovada_reprova_o_conjunto():
    """Não adianta o termo da PA estar certo se a função afim associada está errada."""
    r = VerificadorSimbolico().verificar(_questao(TERMO_ERRADO, AFIM_ASSOCIADA))
    assert r.veredicto == Veredicto.REJEITADO
    assert "1 de 2" in r.justificativa


def test_metade_conferida_vira_parcial_e_nao_aprovacao_plena():
    """O caso que motivou a Fase 0: antes isso passaria como se tudo estivesse conferido."""
    r = VerificadorSimbolico().verificar(_questao(TERMO_CERTO, SEM_PREDICADO))
    assert r.veredicto == Veredicto.APROVADO_PARCIAL
    assert garantia_de(r.veredicto) == Garantia.CONFERIDO_EM_PARTE


def test_nenhuma_verificavel_nao_e_parcial():
    r = VerificadorSimbolico().verificar(_questao(SEM_PREDICADO, SEM_PREDICADO))
    assert r.veredicto == Veredicto.NAO_VERIFICAVEL
    assert garantia_de(r.veredicto) == Garantia.SEM_CONFERENCIA


def test_lista_vazia_nao_e_verificavel():
    assert VerificadorSimbolico().verificar(_questao()).veredicto == Veredicto.NAO_VERIFICAVEL


def test_questao_antiga_com_verificavel_no_singular_continua_lendo():
    """O banco do professor guarda o campo antigo — não pode ficar ilegível."""
    antiga = Questao.model_validate({
        "enunciado": "...", "resolucao": "...", "gabarito": "23",
        "verificavel": TERMO_CERTO.model_dump(),
        "especificacao": SPEC.model_dump(),
    })
    assert len(antiga.verificaveis) == 1
    assert VerificadorSimbolico().verificar(antiga).veredicto == Veredicto.APROVADO

    nula = Questao.model_validate({
        "enunciado": "...", "resolucao": "...", "gabarito": "x",
        "verificavel": None, "especificacao": SPEC.model_dump(),
    })
    assert nula.verificaveis == []
