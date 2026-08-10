"""Interface comum dos provedores de LLM e fábrica por nome."""

from __future__ import annotations

from abc import ABC, abstractmethod

# Temperatura baixa por padrão: reprodutibilidade em tarefas matemáticas
# (Seção 5.5 do projeto; discussão em 2.1.2 da dissertação).
TEMPERATURA_PADRAO = 0.3

# Serviços atendidos pelo mesmo cliente, porque falam o protocolo de chat da
# OpenAI. Declarados aqui, e não importados de `openai_llm`, para que a lista de
# provedores possa ser consultada (pela API, pelos testes) sem exigir que a
# biblioteca `openai` esteja instalada.
COMPATIVEIS_OPENAI = ("openai", "gemini", "deepseek")
PROVEDORES = ("anthropic", *COMPATIVEIS_OPENAI, "ollama")


class ProvedorLLM(ABC):
    """Contrato mínimo: um método de completação de texto."""

    @abstractmethod
    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        """Envia (system, user) e retorna o texto da resposta."""


def criar_provedor(
    nome: str,
    modelo: str | None = None,
    api_key: str | None = None,
    url: str | None = None,
) -> ProvedorLLM:
    """Fábrica: 'anthropic' | 'openai' | 'gemini' | 'deepseek' | 'ollama'.

    `api_key` sobrepõe a variável de ambiente (permite configuração pela UI);
    `url` aplica-se ao Ollama e, como `base_url`, aos serviços compatíveis com a
    OpenAI. Importa sob demanda para que cada provedor exija apenas a sua
    dependência.

    'gemini' e 'deepseek' não têm módulo próprio: falam o protocolo de chat da
    OpenAI e são o mesmo cliente com outro endereço (ver `openai_llm.SERVICOS`).
    """
    if nome == "anthropic":
        from .anthropic_llm import ProvedorAnthropic

        return ProvedorAnthropic(modelo=modelo, api_key=api_key)
    if nome in COMPATIVEIS_OPENAI:
        from .openai_llm import ProvedorOpenAI

        return ProvedorOpenAI(modelo=modelo, api_key=api_key, servico=nome, base_url=url)
    if nome == "ollama":
        from .ollama_llm import ProvedorOllama

        if url:
            return ProvedorOllama(modelo=modelo, url=url)
        return ProvedorOllama(modelo=modelo)
    raise ValueError(f"Provedor desconhecido: '{nome}'. Use um de: {', '.join(PROVEDORES)}.")
