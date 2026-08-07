"""Agente Gerador (Seção 4.3 da dissertação).

Recebe a especificação do professor (e, em revisões, o feedback estruturado
do Orquestrador) e produz uma Questao completa em JSON.
"""

from __future__ import annotations

from pathlib import Path

from ..especificacao import Especificacao, Formato
from ..llm import ProvedorLLM
from ..modelos import Questao
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


class Gerador:
    def __init__(self, llm: ProvedorLLM):
        self._llm = llm
        self._system = _PROMPT.read_text(encoding="utf-8")

    def gerar(self, spec: Especificacao, feedback: str | None = None) -> Questao:
        pedido = self._montar_pedido(spec, feedback)
        resposta = self._llm.completar(system=self._system, user=pedido)
        dados = extrair_json(resposta)
        dados["especificacao"] = spec
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
            linhas.append(f"- Contexto temático: {spec.contexto}")
        if spec.restricoes:
            linhas.append(f"- Restrições: {spec.restricoes}")
        if feedback:
            linhas += ["", "FEEDBACK DA TENTATIVA ANTERIOR (corrija exatamente isto):", feedback]
        return "\n".join(linhas)
