"""Camada de acesso a LLMs: interface única, múltiplos provedores.

O restante do sistema depende apenas de `ProvedorLLM` (base.py); trocar de
provedor (Anthropic, OpenAI, Gemini, DeepSeek, Ollama local) é uma decisão de
configuração, não de código — requisito do projeto para viabilizar uso sem API
paga, e o que torna comparável o custo entre modelos (ver `plano_teste_modelos.md`).
"""

from .base import COMPATIVEIS_OPENAI, PROVEDORES, ProvedorLLM, criar_provedor

__all__ = ["COMPATIVEIS_OPENAI", "PROVEDORES", "ProvedorLLM", "criar_provedor"]
