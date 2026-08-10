"""Provedor Ollama (modelos abertos locais — qwen, llama). Sem chave de API.

Viabiliza o uso do sistema pelo professor sem dependência de API paga,
requisito explícito do projeto da dissertação, e é o braço aberto da comparação
entre modelos (`plano_teste_modelos.md`).
"""

from __future__ import annotations

from .base import TEMPERATURA_PADRAO, ProvedorLLM

MODELO_PADRAO = "qwen2.5:14b"
URL_PADRAO = "http://localhost:11434"

# O Ollama trunca em 128 tokens por omissão — um valor pensado para conversa,
# não para as ~2.300 tokens de JSON que o Gerador produz. Sem isto, toda questão
# saía cortada no meio e o modelo aberto parecia incapaz da tarefa quando o
# problema era de configuração.
NUM_PREDICT = 8000


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
                # Restringe a amostragem a JSON bem-formado. É o que permite a um
                # modelo pequeno cumprir o contrato de saída: sem isto, a
                # disciplina de formato depende só da instrução em prosa, e é o
                # primeiro lugar onde um modelo menor falha.
                "format": "json",
                "options": {"temperature": temperature, "num_predict": NUM_PREDICT},
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            },
        )
        resposta.raise_for_status()
        corpo = resposta.json()
        conteudo = corpo.get("message", {}).get("content")

        # Truncar vira exceção porque o Orquestrador sabe reagir a exceção
        # pedindo concisão (`_gerar_com_folga`); a um JSON pela metade, não.
        if corpo.get("done_reason") == "length":
            raise RuntimeError(
                f"O modelo '{self._modelo}' esgotou o limite de {NUM_PREDICT} tokens "
                "antes de fechar o JSON."
            )
        if not conteudo:
            raise RuntimeError(f"O modelo '{self._modelo}' devolveu resposta vazia.")
        return conteudo
