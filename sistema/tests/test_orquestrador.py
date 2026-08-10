"""Testes da política de decisão do Orquestrador usando um provedor LLM fake.

O fake devolve respostas pré-programadas em sequência, permitindo testar os
caminhos do ciclo (aprovação direta, revisão por verificador, revisão por
crítico, descarte) de forma determinística e sem chave de API.
"""

import json

from questoes.agentes import CriticoDidatico, Gerador, Orquestrador, VerificadorSimbolico
from questoes.especificacao import (
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, Tema,
)
from questoes.llm.base import ProvedorLLM
from questoes.modelos import Veredicto


class LLMFake(ProvedorLLM):
    """Devolve respostas da fila na ordem; registra os pedidos recebidos."""

    def __init__(self, respostas: list[str]):
        self.respostas = list(respostas)
        self.pedidos: list[str] = []

    def completar(self, system, user, temperature=0.3):
        self.pedidos.append(user)
        return self.respostas.pop(0)


SPEC = Especificacao(
    tema=Tema.FUNCAO_QUADRATICA,
    habilidade_bncc="EM13MAT302",
    nivel_bloom=NivelBloom.APLICAR,
    dificuldade=Dificuldade.MEDIA,
    natureza=Natureza.TEORICA,
    formato=Formato.DISCURSIVA,
)


def _questao_json(resposta_esperada="[1, Rational(3,2)]"):
    return json.dumps({
        "enunciado": "Resolva a equação 2x² - 5x + 3 = 0.",
        "resolucao": "Por Bhaskara: $\\Delta = 25 - 24 = 1$; $x = (5 \\pm 1)/4$.",
        "gabarito": "x = 1 ou x = 3/2",
        "alternativas": None,
        "verificavel": {
            "tipo": "equacao",
            "expressao": "Eq(2*x**2 - 5*x + 3, 0)",
            "incognitas": ["x"],
            "resposta_esperada": resposta_esperada,
            "parametros": {},
        },
    })


def _parecer_json(aprovado=True, nota=4, sugestoes=None):
    criterios = ["clareza", "adequacao_nivel", "alinhamento_bncc", "distratores", "originalidade"]
    return json.dumps({
        "notas": [{"criterio": c, "nota": nota, "comentario": "ok"} for c in criterios],
        "aprovado": aprovado,
        "sugestoes_revisao": sugestoes,
    })


def _orquestrador(llm):
    return Orquestrador(Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm))


def test_aprovacao_na_primeira_iteracao():
    llm = LLMFake([_questao_json(), _parecer_json(aprovado=True)])
    resultado = _orquestrador(llm).produzir(SPEC)
    assert resultado.aprovada
    assert len(resultado.iteracoes) == 1
    assert resultado.iteracoes[0].verificacao.veredicto == Veredicto.APROVADO


def test_gabarito_errado_gera_revisao_e_aprova_na_segunda():
    llm = LLMFake([
        _questao_json(resposta_esperada="[1, 2]"),   # it.1: gabarito errado -> verificador rejeita
        _questao_json(),                              # it.2: corrigido
        _parecer_json(aprovado=True),                 # crítico aprova
    ])
    resultado = _orquestrador(llm).produzir(SPEC)
    assert resultado.aprovada
    assert len(resultado.iteracoes) == 2
    assert resultado.iteracoes[0].verificacao.veredicto == Veredicto.REJEITADO
    assert resultado.iteracoes[0].parecer is None      # reprovado antes do crítico
    # o feedback da 2ª geração menciona o veredito do verificador
    assert "REPROVOU o gabarito" in llm.pedidos[1]


def test_reprovacao_didatica_gera_revisao_com_sugestoes():
    llm = LLMFake([
        _questao_json(),
        _parecer_json(aprovado=False, nota=2, sugestoes="Remova a ambiguidade do enunciado."),
        _questao_json(),
        _parecer_json(aprovado=True),
    ])
    resultado = _orquestrador(llm).produzir(SPEC)
    assert resultado.aprovada
    assert len(resultado.iteracoes) == 2
    assert "Remova a ambiguidade" in llm.pedidos[2]  # sugestão chegou ao gerador


def test_descarte_apos_tres_iteracoes():
    ruim = _questao_json(resposta_esperada="[7]")
    llm = LLMFake([ruim, ruim, ruim])
    resultado = _orquestrador(llm).produzir(SPEC)
    assert not resultado.aprovada
    assert resultado.questao_final is None
    assert len(resultado.iteracoes) == 3


def test_nao_verificavel_segue_ao_critico():
    questao_sem_formalizacao = json.dumps({
        "enunciado": "Justifique por que o discriminante determina o número de raízes reais.",
        "resolucao": "Argumentação sobre o sinal de Delta...",
        "gabarito": "Argumentação",
        "alternativas": None,
        "verificavel": None,
    })
    llm = LLMFake([questao_sem_formalizacao, _parecer_json(aprovado=True)])
    resultado = _orquestrador(llm).produzir(SPEC)
    assert resultado.aprovada
    assert resultado.iteracoes[0].verificacao.veredicto == Veredicto.NAO_VERIFICAVEL
    assert resultado.iteracoes[0].parecer is not None  # crítico foi consultado


def test_log_jsonl_gravado(tmp_path):
    llm = LLMFake([_questao_json(), _parecer_json(aprovado=True)])
    orq = Orquestrador(
        Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm), log_dir=tmp_path
    )
    orq.produzir(SPEC)
    linhas = (tmp_path / "ciclos.jsonl").read_text().strip().splitlines()
    assert len(linhas) == 1
    assert json.loads(linhas[0])["aprovada"] is True


def test_gerador_recebe_as_exigencias_da_habilidade():
    """A habilidade tem de chegar ao Gerador como requisito, não como rótulo.

    Antes ela entrava no prompt só como uma linha de descrição, e o único
    guardião do alinhamento curricular era o julgamento em prosa do Crítico.
    """
    llm = LLMFake([_questao_json(), _parecer_json(aprovado=True)])
    orq = Orquestrador(Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm))
    orq.produzir(SPEC)

    pedido_ao_gerador = llm.pedidos[0]
    for exigencia in SPEC.exigencias_habilidade():
        assert exigencia in pedido_ao_gerador


def test_pedido_multitema_instrui_a_articular():
    """Dois temas devem virar UMA questão que os articule, não dois itens colados."""
    spec = Especificacao(
        habilidade_bncc="EM13MAT302",
        temas=[Tema.FUNCAO_AFIM, Tema.FUNCAO_QUADRATICA],
        nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.APLICADA, formato=Formato.DISCURSIVA,
    )
    llm = LLMFake([_questao_json(), _parecer_json(aprovado=True)])
    Orquestrador(Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm)).produzir(spec)

    pedido = llm.pedidos[0]
    assert "funcao afim, funcao quadratica" in pedido
    assert "articulando os temas" in pedido


def test_divergencia_de_bloom_vai_para_o_log(tmp_path):
    """Não barra o pedido — registra, para a avaliação empírica poder analisar."""
    spec = Especificacao(
        habilidade_bncc="EM13MAT302", temas=[Tema.FUNCAO_QUADRATICA],
        nivel_bloom=NivelBloom.LEMBRAR, dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.TEORICA, formato=Formato.DISCURSIVA,
    )
    llm = LLMFake([_questao_json(), _parecer_json(aprovado=True)])
    orq = Orquestrador(
        Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm), log_dir=tmp_path
    )
    assert orq.produzir(spec).aprovada

    registro = json.loads((tmp_path / "ciclos.jsonl").read_text(encoding="utf-8").strip())
    assert registro["bloom_divergente"] is True
    assert registro["bloom_sugerido"] == ["aplicar", "criar"]


def test_formalizacao_malformada_nao_derruba_a_questao():
    """Encontrado numa medição real: o LLM devolveu {"ponto": {"d": 2}}.

    O contrato pede texto, a validação estourou e o ciclo inteiro morreu —
    perdendo enunciado, gabarito e resolução que estavam bons, além do custo da
    chamada. Uma formalização inutilizável deve custar a conferência daquela
    afirmação, e nada mais.
    """
    bruto = json.dumps({
        "enunciado": "Resolva 2x = 8.", "resolucao": "x = 4.", "gabarito": "4",
        "verificaveis": [
            {"tipo": "funcao", "expressao": "2*x", "incognitas": ["x"],
             "resposta_esperada": "8",
             "parametros": {"consulta": "valor", "ponto": {"d": 2}}},
            {"tipo": "equacao", "expressao": "Eq(2*x, 8)", "incognitas": ["x"],
             "resposta_esperada": "[4]", "parametros": {}},
        ],
    })
    llm = LLMFake([bruto, _parecer_json(aprovado=True)])
    resultado = Orquestrador(
        Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm)
    ).produzir(SPEC)

    assert resultado.aprovada
    questao = resultado.questao_final
    assert questao.enunciado  # a questão sobreviveu
    assert [v.tipo for v in questao.verificaveis] == ["equacao"]  # a boa foi mantida


def test_falha_de_geracao_ganha_segunda_tentativa_pedindo_concisao():
    """Um ciclo do acervo morreu com max_tokens: o modelo não fechou o JSON.

    A exceção subia e derrubava o ciclo inteiro. Uma segunda tentativa pedindo
    economia resolve o caso observado sem mexer no contrato.
    """
    class Instavel(LLMFake):
        def completar(self, system, user, temperature=0.3):
            self.pedidos.append(user)
            if len(self.pedidos) == 1:
                raise RuntimeError("O modelo não devolveu texto (motivo: max_tokens).")
            return self.respostas.pop(0)

    llm = Instavel([_questao_json(), _parecer_json(aprovado=True)])
    resultado = Orquestrador(
        Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm)
    ).produzir(SPEC)

    assert resultado.aprovada
    assert "mais econômica" in llm.pedidos[1]


def test_par_de_contextos_vem_com_permissao_de_usar_so_um():
    """Contexto forçado é pior que contexto comum — a rubrica penaliza o artificial.

    O par amplia muito o espaço de cenários (35 contextos dão 595 pares), mas
    nem toda combinação fecha. O Gerador precisa poder recuar para um só.
    """
    spec = Especificacao(
        habilidade_bncc="EM13MAT302", temas=[Tema.FUNCAO_AFIM],
        nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.APLICADA, formato=Formato.DISCURSIVA,
        contexto="Desmatamento e recuperação de área florestal + Densidade demográfica",
    )
    pedido = Gerador._montar_pedido(spec, None)
    assert "Contextos sugeridos" in pedido
    assert "Se soar forçada, use apenas o primeiro" in pedido

    simples = Especificacao(
        habilidade_bncc="EM13MAT302", temas=[Tema.FUNCAO_AFIM],
        nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
        natureza=Natureza.APLICADA, formato=Formato.DISCURSIVA,
        contexto="Desmatamento e recuperação de área florestal",
    )
    assert "Contexto temático" in Gerador._montar_pedido(simples, None)
    assert "use apenas o primeiro" not in Gerador._montar_pedido(simples, None)
