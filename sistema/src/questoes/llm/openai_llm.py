"""Provedor OpenAI. Requer OPENAI_API_KEY no ambiente."""

from __future__ import annotations

from .base import TEMPERATURA_PADRAO, ProvedorLLM

MODELO_PADRAO = "gpt-4o-mini"  # sugestão do projeto para desenvolvimento (custo baixo)


class ProvedorOpenAI(ProvedorLLM):
    def __init__(self, modelo: str | None = None, api_key: str | None = None):
        import openai  # dependência opcional: pip install questoes-em[openai]

        # api_key=None deixa o SDK buscar OPENAI_API_KEY no ambiente
        self._cliente = openai.OpenAI(api_key=api_key) if api_key else openai.OpenAI()
        self._modelo = modelo or MODELO_PADRAO

    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        resposta = self._cliente.chat.completions.create(
            model=self._modelo,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        return resposta.choices[0].message.content
