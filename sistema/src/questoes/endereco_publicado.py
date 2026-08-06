"""Publica o endereço da API num arquivo que o GitHub Pages serve.

O túnel rápido sorteia um endereço novo a cada subida. Se o link de convite
carregasse esse endereço, todo reinício invalidaria os links já distribuídos.
A saída é inverter a direção: o link aponta sempre para a interface publicada,
e ela descobre onde a API está lendo um `backend.json` ao lado dela.

A escrita é feita pela API de conteúdo do GitHub --- não é preciso ter o
repositório clonado na máquina do servidor, apenas um token com permissão de
escrita em conteúdo. O token vem do ambiente (`QUESTOES_GITHUB_TOKEN`), nunca
de arquivo de configuração.
"""

from __future__ import annotations

import base64
import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"
VARIAVEL_TOKEN = "QUESTOES_GITHUB_TOKEN"


class PublicacaoIndisponivel(RuntimeError):
    """Falta configuração ou o GitHub recusou. Nunca deve derrubar o servidor."""


def _pedir(metodo: str, url: str, token: str, corpo: dict | None = None) -> dict:
    dados = json.dumps(corpo).encode() if corpo else None
    req = urllib.request.Request(url, data=dados, method=metodo, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30) as resposta:
        return json.load(resposta)


def publicar(endereco: str, repositorio: str, caminho: str, ramo: str = "main") -> str:
    """Grava `{caminho}` no repositório com o endereço atual da API.

    Devolve a URL do commit. Levanta `PublicacaoIndisponivel` com mensagem
    legível se faltar token ou o GitHub recusar.
    """
    token = os.environ.get(VARIAVEL_TOKEN)
    if not token:
        raise PublicacaoIndisponivel(
            f"Defina {VARIAVEL_TOKEN} no ambiente para publicar o endereço automaticamente."
        )
    if not repositorio or "/" not in repositorio:
        raise PublicacaoIndisponivel(
            "Configure 'repositorio_frontend' como 'usuario/repositorio'."
        )

    conteudo = json.dumps({
        "endereco": endereco.rstrip("/"),
        "atualizado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }, ensure_ascii=False, indent=2) + "\n"

    url = f"{API}/repos/{repositorio}/contents/{caminho}"

    # A atualização exige o sha do arquivo atual; sua ausência significa que o
    # arquivo ainda não existe, e aí a mesma chamada o cria.
    sha = None
    try:
        atual = _pedir("GET", f"{url}?ref={ramo}", token)
        sha = atual.get("sha")
        if base64.b64decode(atual.get("content", "")).decode() == conteudo:
            return "sem mudança: o endereço publicado já é este"
    except urllib.error.HTTPError as erro:
        if erro.code != 404:
            raise PublicacaoIndisponivel(f"GitHub respondeu {erro.code} ao ler {caminho}.") from erro
    except (urllib.error.URLError, ValueError) as erro:
        raise PublicacaoIndisponivel(f"Não consegui falar com o GitHub: {erro}") from erro

    corpo = {
        "message": f"Publica endereço da API: {endereco}",
        "content": base64.b64encode(conteudo.encode()).decode(),
        "branch": ramo,
    }
    if sha:
        corpo["sha"] = sha

    try:
        resposta = _pedir("PUT", url, token, corpo)
    except urllib.error.HTTPError as erro:
        detalhe = "token sem permissão de escrita" if erro.code in (403, 404) else f"HTTP {erro.code}"
        raise PublicacaoIndisponivel(f"GitHub recusou a publicação ({detalhe}).") from erro
    except urllib.error.URLError as erro:
        raise PublicacaoIndisponivel(f"Não consegui falar com o GitHub: {erro}") from erro

    return resposta.get("commit", {}).get("html_url", "commit criado")
