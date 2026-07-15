"""Provedor Ollama (modelos abertos locais — qwen, llama). Sem chave de API.

Viabiliza o uso do sistema pelo professor sem dependência de API paga,
requisito explícito do projeto da dissertação.
"""

from __future__ import annotations

from .base import TEMPERATURA_PADRAO, ProvedorLLM

MODELO_PADRAO = "qwen2.5:14b"
URL_PADRAO = "http://localhost:11434"


class ProvedorOllama(ProvedorLLM):
    def __init__(self, modelo: str | None = None, url: str = URL_PADRAO):
        import httpx  # dependência opcional: pip install questoes-em[ollama]

        self._http = httpx.Client(base_url=url, timeout=300)
        self._modelo = modelo or MODELO_PADRAO

    def completar(self, system: str, user: str, temperature: float = TEMPERATURA_PADRAO) -> str:
        resposta = self._http.post(
            "/api/chat",
            json={
                "model": self._modelo,
                "stream": False,
                "options": {"temperature": temperature},
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            },
        )
        resposta.raise_for_status()
        return resposta.json()["message"]["content"]
