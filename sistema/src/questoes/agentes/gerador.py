"""Agente Gerador (Seção 4.3 da dissertação).

Recebe a especificação do professor (e, em revisões, o feedback estruturado
do Orquestrador) e produz uma Questao completa em JSON.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import ValidationError

from ..especificacao import Especificacao, Formato
from ..llm import ProvedorLLM
from ..modelos import ExpressaoVerificavel, Questao
from ._json_util import extrair_json

_PROMPT = Path(__file__).resolve().parents[3] / "prompts" / "gerador.md"

_ROTULOS_DIFICULDADE = {
    "facil": "fácil — aplicação direta de um conceito, poucos passos",
    "media": "média — exige articular dois ou mais passos ou conceitos",
    "dificil": "difícil — exige estratégia não evidente ou análise de casos",
}

_ROTULOS_NATUREZA = {
    "teorica": "teórica: manipulação e propriedades matemáticas, sem contexto externo",
    "aplicada": "aplicada: situação-problema com contexto realista e dados verossímeis",
}


def _formalizacoes_utilizaveis(dados: dict) -> list[ExpressaoVerificavel]:
    """Fica com as formalizações válidas e descarta as malformadas.

    O Verificador já degrada em vez de estourar quando a expressão não faz
    sentido; a *leitura* da saída do Gerador não degradava. Numa medição com
    provedor real, o LLM devolveu `parametros: {"ponto": {"d": 2}}` --- um objeto
    onde o contrato pede texto --- e a exceção de validação derrubou o ciclo
    inteiro, perdendo um enunciado, um gabarito e uma resolução que estavam bons,
    além do custo da chamada.

    Uma formalização inutilizável deve custar a conferência daquela afirmação, e
    nada mais: as demais seguem, e a questão chega ao professor com a garantia
    rebaixada em vez de não chegar.
    """
    brutas = dados.get("verificaveis")
    if brutas is None:
        unico = dados.get("verificavel")
        brutas = [] if unico is None else (unico if isinstance(unico, list) else [unico])
    if isinstance(brutas, dict):  # o LLM às vezes manda um objeto onde o contrato pede lista
        brutas = [brutas]

    utilizaveis = []
    for bruta in brutas or []:
        try:
            utilizaveis.append(ExpressaoVerificavel.model_validate(bruta))
        except ValidationError:
            continue
    return utilizaveis


class Gerador:
    def __init__(self, llm: ProvedorLLM):
        self._llm = llm
        self._system = _PROMPT.read_text(encoding="utf-8")

    def gerar(self, spec: Especificacao, feedback: str | None = None) -> Questao:
        pedido = self._montar_pedido(spec, feedback)
        resposta = self._llm.completar(system=self._system, user=pedido)
        dados = extrair_json(resposta)
        dados["especificacao"] = spec
        dados["verificaveis"] = _formalizacoes_utilizaveis(dados)
        dados.pop("verificavel", None)
        return Questao.model_validate(dados)

    @staticmethod
    def _montar_pedido(spec: Especificacao, feedback: str | None) -> str:
        temas = [t.value.replace("_", " ") for t in spec.temas]
        linhas = [
            "ESPECIFICAÇÃO DA QUESTÃO:",
            f"- Habilidade BNCC {spec.habilidade_bncc}: {spec.descricao_habilidade()}",
            f"- Tema{'s' if len(temas) > 1 else ''}: {', '.join(temas)}",
        ]
        if len(temas) > 1:
            linhas.append(
                "  ATENÇÃO: são vários temas. A questão deve ser UMA só, articulando os temas "
                "num mesmo problema — nunca dois itens independentes emendados."
            )
        linhas += [
            "- A questão só realiza a habilidade se cumprir TODAS as exigências abaixo:",
            *(f"  * {e}" for e in spec.exigencias_habilidade()),
            f"- Nível cognitivo (Bloom): {spec.nivel_bloom.value}",
            f"- Dificuldade: {_ROTULOS_DIFICULDADE[spec.dificuldade.value]}",
            f"- Natureza: {_ROTULOS_NATUREZA[spec.natureza.value]}",
            f"- Formato: {'múltipla escolha (4 alternativas)' if spec.formato == Formato.MULTIPLA_ESCOLHA else 'discursiva'}",
        ]
        if spec.contexto:
            partes = [c.strip() for c in spec.contexto.split("+") if c.strip()]
            if len(partes) > 1:
                linhas.append(f"- Contextos sugeridos: {' + '.join(partes)}")
                linhas.append(
                    "  Combine os dois num único cenário SE a combinação for natural. "
                    "Se soar forçada, use apenas o primeiro — contexto artificial é pior "
                    "que contexto comum."
                )
            else:
                linhas.append(f"- Contexto temático: {spec.contexto}")
        if spec.restricoes:
            linhas.append(f"- Restrições: {spec.restricoes}")
        if feedback:
            linhas += ["", "FEEDBACK DA TENTATIVA ANTERIOR (corrija exatamente isto):", feedback]
        return "\n".join(linhas)
