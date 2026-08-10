"""Provedores que falam o protocolo de chat da OpenAI: OpenAI, Gemini, DeepSeek.

Gemini e DeepSeek publicam endpoints compatíveis com a API de chat da OpenAI,
então o mesmo cliente serve aos três: o que muda é `base_url`, a variável de
ambiente da chave e o modelo padrão. Um provedor só, e não três cópias que
divergiriam na primeira correção.

Sem o `base_url` estes serviços eram inalcançáveis: `openai.OpenAI()` só apontava
para a OpenAI, e desviar pela variável global `OPENAI_BASE_URL` quebraria o
provedor OpenAI na mesma sessão.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from .base import TEMPERATURA_PADRAO, ProvedorLLM

MODELO_PADRAO = "gpt-4o-mini"  # sugestão do projeto para desenvolvimento (custo baixo)


@dataclass(frozen=True)
class Servico:
    """O que distingue um serviço compatível do outro."""

    base_url: str | None  # None = a própria OpenAI (o SDK já sabe o endereço)
    variavel_chave: str
    modelo_padrao: str


SERVICOS = {
    "openai": Servico(None, "OPENAI_API_KEY", MODELO_PADRAO),
    "gemini": Servico(
        "https://generativelanguage.googleapis.com/v1beta/openai/",
        "GEMINI_API_KEY",
        "gemini-2.5-flash-lite",
    ),
    "deepseek": Servico("https://api.deepseek.com", "DEEPSEEK_API_KEY", "deepseek-v4-flash"),
}

# Teto de saída. O Gerador produz cerca de 2.300 tokens de JSON por questão; sem
# teto declarado, a DeepSeek avisa que o JSON sai truncado. Truncar levanta
# exceção, e o Orquestrador já sabe reagir a isso pedindo concisão
# (`_gerar_com_folga`) --- por isso a folga aqui é generosa, não apertada.
MAX_TOKENS = 8000

# Os modelos de raciocínio da OpenAI recusam `temperature` diferente de 1 (erro
# 400) e trocam `max_tokens` por `max_completion_tokens`. Mesmo problema que
# `FAMILIAS_COM_TEMPERATURA` resolve do lado da Anthropic: o padrão é enviar, a
# exceção é a lista.
FAMILIAS_DE_RACIOCINIO = ("gpt-5", "o1", "o3", "o4")


class ProvedorOpenAI(ProvedorLLM):
    """Cliente de chat da OpenAI, ou de qualquer serviço que fale o mesmo protocolo.

    `servico` escolhe o endereço e o modelo padrão; `base_url` sobrepõe o
    endereço para um serviço compatível que ainda não esteja em `SERVICOS`
    (Groq, Together, OpenRouter, um vLLM da universidade).
    """

    def __init__(
        self,
        modelo: str | None = None,
        api_key: str | None = None,
        servico: str = "openai",
        base_url: str | None = None,
    ):
        import openai  # dependência opcional: pip install questoes-em[openai]

        cfg = SERVICOS.get(servico) or SERVICOS["openai"]
        endereco = base_url or cfg.base_url
        # A chave da requisição vence; sem ela, a variável do serviço. Os SDKs
        # compatíveis não conhecem GEMINI_API_KEY nem DEEPSEEK_API_KEY, então
        # buscá-la aqui é o que evita cair silenciosamente na OPENAI_API_KEY.
        chave = api_key or os.environ.get(cfg.variavel_chave)
        if not chave and cfg.base_url:
            raise RuntimeError(
                f"Falta a chave do serviço '{servico}': informe-a na requisição "
                f"ou defina {cfg.variavel_chave} no ambiente."
            )

        argumentos = {"api_key": chave} if chave else {}
        if endereco:
            argumentos["base_url"] = endereco
        self._cliente = openai.OpenAI(**argumentos)
        self._modelo = modelo or cfg.modelo_padrao
        self._servico = servico

    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        raciocinio = self._modelo.startswith(FAMILIAS_DE_RACIOCINIO)
        parametros: dict = {
            "model": self._modelo,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            # Os dois prompts pedem JSON e trazem a palavra "json" no texto, que
            # é o que a OpenAI e a DeepSeek exigem para aceitar este modo. É o
            # que faz um modelo pequeno servir: sem ele, a disciplina de formato
            # depende só da instrução em prosa.
            "response_format": {"type": "json_object"},
        }
        if raciocinio:
            parametros["max_completion_tokens"] = MAX_TOKENS
        else:
            parametros["max_tokens"] = MAX_TOKENS
            parametros["temperature"] = temperature

        resposta = self._cliente.chat.completions.create(**parametros)
        escolha = resposta.choices[0]
        conteudo = escolha.message.content

        # As duas falhas silenciosas deste caminho, ambas documentadas pelos
        # provedores: saída truncada no limite, e conteúdo vazio no modo JSON da
        # DeepSeek. Sem estas verificações, `extrair_json(None)` devolveria um
        # erro que não diz nada sobre a causa.
        if escolha.finish_reason == "length":
            raise RuntimeError(
                f"O modelo '{self._modelo}' esgotou o limite de {MAX_TOKENS} tokens "
                "antes de fechar o JSON."
            )
        if not conteudo:
            raise RuntimeError(
                f"O modelo '{self._modelo}' devolveu resposta vazia "
                f"(motivo: {escolha.finish_reason})."
            )
        return conteudo
