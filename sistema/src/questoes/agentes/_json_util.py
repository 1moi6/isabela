"""Extração tolerante de JSON de respostas de LLM.

Mesmo instruídos a responder só JSON, modelos ocasionalmente envolvem a
resposta em cercas de código ou texto. Extrai o primeiro objeto plausível.
"""

from __future__ import annotations

import json
import re


def extrair_json(texto: str) -> dict:
    texto = texto.strip()
    # remove cercas ```json ... ```
    cercas = re.match(r"^```(?:json)?\s*(.*?)\s*```$", texto, re.DOTALL)
    if cercas:
        texto = cercas.group(1)
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        pass
    # fallback: maior trecho entre a primeira '{' e a última '}'
    inicio, fim = texto.find("{"), texto.rfind("}")
    if inicio >= 0 and fim > inicio:
        return json.loads(texto[inicio : fim + 1])
    raise ValueError(f"Resposta do LLM não contém JSON válido: {texto[:200]}...")
