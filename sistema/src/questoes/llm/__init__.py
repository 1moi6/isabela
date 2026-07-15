"""Camada de acesso a LLMs: interface única, múltiplos provedores.

O restante do sistema depende apenas de `ProvedorLLM` (base.py); trocar de
provedor (Anthropic, OpenAI, Ollama local) é uma decisão de configuração,
não de código — requisito do projeto para viabilizar uso sem API paga.
"""

from .base import ProvedorLLM, criar_provedor

__all__ = ["ProvedorLLM", "criar_provedor"]
