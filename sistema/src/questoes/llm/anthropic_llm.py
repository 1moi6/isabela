"""Provedor Anthropic (Claude). Requer ANTHROPIC_API_KEY no ambiente."""

from __future__ import annotations

from .base import TEMPERATURA_PADRAO, ProvedorLLM

MODELO_PADRAO = "claude-sonnet-5"


class ProvedorAnthropic(ProvedorLLM):
    def __init__(self, modelo: str | None = None, api_key: str | None = None):
        import anthropic  # dependência opcional: pip install questoes-em[anthropic]

        # api_key=None deixa o SDK buscar ANTHROPIC_API_KEY no ambiente
        self._cliente = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
        self._modelo = modelo or MODELO_PADRAO

    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        resposta = self._cliente.messages.create(
            model=self._modelo,
            max_tokens=4096,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return resposta.content[0].text
