"""Provedor Anthropic (Claude). Requer ANTHROPIC_API_KEY no ambiente."""

from __future__ import annotations

from .base import TEMPERATURA_PADRAO, ProvedorLLM

MODELO_PADRAO = "claude-sonnet-5"

# Os modelos atuais da Anthropic (Sonnet 5, Opus 5/4.8/4.7) removeram os parâmetros de
# amostragem: enviar `temperature` devolve erro 400. Só as famílias abaixo ainda os aceitam;
# qualquer modelo fora desta lista — inclusive os futuros — recebe a requisição sem o
# parâmetro (ver a seção de reprodutibilidade do Capítulo 5).
FAMILIAS_COM_TEMPERATURA = (
    "claude-3",
    "claude-haiku-4-5",
    "claude-sonnet-4-0",
    "claude-sonnet-4-5",
    "claude-sonnet-4-6",
    "claude-opus-4-0",
    "claude-opus-4-1",
    "claude-opus-4-5",
    "claude-opus-4-6",
)

# Generoso porque os modelos atuais raciocinam antes de responder e o limite cobre
# raciocínio + resposta: um teto apertado trunca o JSON da questão no meio.
MAX_TOKENS = 16000


class ProvedorAnthropic(ProvedorLLM):
    def __init__(self, modelo: str | None = None, api_key: str | None = None):
        import anthropic  # dependência opcional: pip install questoes-em[anthropic]

        # api_key=None deixa o SDK buscar ANTHROPIC_API_KEY no ambiente
        self._cliente = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
        self._modelo = modelo or MODELO_PADRAO

    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        parametros = {
            "model": self._modelo,
            "max_tokens": MAX_TOKENS,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }
        if self._modelo.startswith(FAMILIAS_COM_TEMPERATURA):
            parametros["temperature"] = temperature

        resposta = self._cliente.messages.create(**parametros)

        # A resposta pode trazer blocos de raciocínio antes do texto; pegar o primeiro
        # bloco cegamente devolveria um bloco sem `.text`.
        for bloco in resposta.content:
            if bloco.type == "text":
                return bloco.text
        raise RuntimeError(
            f"O modelo '{self._modelo}' não devolveu texto (motivo: {resposta.stop_reason})."
        )
