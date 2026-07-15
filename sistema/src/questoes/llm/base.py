"""Interface comum dos provedores de LLM e fábrica por nome."""

from __future__ import annotations

from abc import ABC, abstractmethod

# Temperatura baixa por padrão: reprodutibilidade em tarefas matemáticas
# (Seção 5.5 do projeto; discussão em 2.1.2 da dissertação).
TEMPERATURA_PADRAO = 0.3


class ProvedorLLM(ABC):
    """Contrato mínimo: um método de completação de texto."""

    @abstractmethod
    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        """Envia (system, user) e retorna o texto da resposta."""


def criar_provedor(nome: str, modelo: str | None = None) -> ProvedorLLM:
    """Fábrica: 'anthropic' | 'openai' | 'ollama'.

    Importa sob demanda para que cada provedor exija apenas a sua dependência.
    """
    if nome == "anthropic":
        from .anthropic_llm import ProvedorAnthropic

        return ProvedorAnthropic(modelo=modelo)
    if nome == "openai":
        from .openai_llm import ProvedorOpenAI

        return ProvedorOpenAI(modelo=modelo)
    if nome == "ollama":
        from .ollama_llm import ProvedorOllama

        return ProvedorOllama(modelo=modelo)
    raise ValueError(f"Provedor desconhecido: '{nome}'. Use 'anthropic', 'openai' ou 'ollama'.")
