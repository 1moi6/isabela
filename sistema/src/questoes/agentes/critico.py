"""Agente Crítico Didático (Seção 4.5 da dissertação).

Avalia a questão com a rubrica de qualidade (Seção 3.4) traduzida em prompt
(prompts/critico.md) e devolve parecer estruturado em JSON.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..llm import ProvedorLLM
from ..modelos import ParecerDidatico, Questao
from ._json_util import extrair_json

_PROMPT = Path(__file__).resolve().parents[3] / "prompts" / "critico.md"


class CriticoDidatico:
    def __init__(self, llm: ProvedorLLM):
        self._llm = llm
        self._system = _PROMPT.read_text(encoding="utf-8")

    def avaliar(self, questao: Questao) -> ParecerDidatico:
        spec = questao.especificacao
        pedido = "\n".join(
            [
                "QUESTÃO A AVALIAR:",
                json.dumps(
                    questao.model_dump(exclude={"especificacao", "verificavel"}),
                    ensure_ascii=False,
                    indent=2,
                ),
                "",
                "ESPECIFICAÇÃO DECLARADA PELO PROFESSOR:",
                f"- Habilidade BNCC {spec.habilidade_bncc}: {spec.descricao_habilidade()}",
                f"- Nível cognitivo (Bloom): {spec.nivel_bloom.value}",
                f"- Dificuldade: {spec.dificuldade.value} | Natureza: {spec.natureza.value} "
                f"| Formato: {spec.formato.value}",
            ]
        )
        resposta = self._llm.completar(system=self._system, user=pedido)
        return ParecerDidatico.model_validate(extrair_json(resposta))
