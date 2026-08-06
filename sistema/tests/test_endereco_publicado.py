"""Testes da publicação automática do endereço da API.

Nenhum teste aqui fala com o GitHub: as chamadas HTTP são substituídas. O que
importa é o contrato — criar quando não existe, atualizar com o sha quando
existe, e nunca derrubar o servidor quando algo falha.
"""

import base64
import json
import urllib.error

import pytest

from questoes import endereco_publicado as ep


@pytest.fixture
def sem_token(monkeypatch):
    monkeypatch.delenv(ep.VARIAVEL_TOKEN, raising=False)


@pytest.fixture
def com_token(monkeypatch):
    monkeypatch.setenv(ep.VARIAVEL_TOKEN, "token-de-teste")


def _erro_http(codigo):
    return urllib.error.HTTPError("url", codigo, "erro", {}, None)


def test_sem_token_falha_com_instrucao(sem_token):
    with pytest.raises(ep.PublicacaoIndisponivel, match=ep.VARIAVEL_TOKEN):
        ep.publicar("https://x.trycloudflare.com", "user/repo", "docs/backend.json")


def test_repositorio_mal_formado_falha_cedo(com_token):
    with pytest.raises(ep.PublicacaoIndisponivel, match="usuario/repositorio"):
        ep.publicar("https://x.trycloudflare.com", "sem-barra", "docs/backend.json")


def test_cria_o_arquivo_quando_ainda_nao_existe(com_token, monkeypatch):
    chamadas = []

    def falso(metodo, url, token, corpo=None):
        chamadas.append((metodo, corpo))
        if metodo == "GET":
            raise _erro_http(404)
        return {"commit": {"html_url": "https://github.com/commit/abc"}}

    monkeypatch.setattr(ep, "_pedir", falso)
    onde = ep.publicar("https://novo.trycloudflare.com", "user/repo", "docs/backend.json")

    assert onde == "https://github.com/commit/abc"
    metodo, corpo = chamadas[-1]
    assert metodo == "PUT"
    assert "sha" not in corpo  # criação não leva sha
    gravado = json.loads(base64.b64decode(corpo["content"]))
    assert gravado["endereco"] == "https://novo.trycloudflare.com"


def test_atualiza_usando_o_sha_do_arquivo_atual(com_token, monkeypatch):
    antigo = json.dumps({"endereco": "https://velho.trycloudflare.com"}) + "\n"
    chamadas = []

    def falso(metodo, url, token, corpo=None):
        chamadas.append((metodo, corpo))
        if metodo == "GET":
            return {"sha": "sha-antigo", "content": base64.b64encode(antigo.encode()).decode()}
        return {"commit": {"html_url": "https://github.com/commit/def"}}

    monkeypatch.setattr(ep, "_pedir", falso)
    ep.publicar("https://novo.trycloudflare.com", "user/repo", "docs/backend.json")

    metodo, corpo = chamadas[-1]
    assert metodo == "PUT"
    assert corpo["sha"] == "sha-antigo"  # sem o sha, o GitHub recusa a atualização


def test_endereco_igual_nao_gera_commit(com_token, monkeypatch):
    """Reiniciar sem mudar de endereço não deve sujar o histórico do repositório."""
    conteudo = None

    def falso(metodo, url, token, corpo=None):
        nonlocal conteudo
        if metodo == "GET":
            return {"sha": "s", "content": base64.b64encode(conteudo.encode()).decode()}
        raise AssertionError("não deveria escrever")

    # descobre o conteúdo que o módulo geraria, para devolvê-lo como "atual"
    def capturar(metodo, url, token, corpo=None):
        nonlocal conteudo
        if metodo == "GET":
            raise _erro_http(404)
        conteudo = base64.b64decode(corpo["content"]).decode()
        return {"commit": {"html_url": "x"}}

    monkeypatch.setattr(ep, "_pedir", capturar)
    ep.publicar("https://igual.trycloudflare.com", "user/repo", "docs/backend.json")

    monkeypatch.setattr(ep, "_pedir", falso)
    resultado = ep.publicar("https://igual.trycloudflare.com", "user/repo", "docs/backend.json")
    assert "sem mudança" in resultado


def test_token_sem_permissao_vira_mensagem_legivel(com_token, monkeypatch):
    def falso(metodo, url, token, corpo=None):
        if metodo == "GET":
            raise _erro_http(404)
        raise _erro_http(403)

    monkeypatch.setattr(ep, "_pedir", falso)
    with pytest.raises(ep.PublicacaoIndisponivel, match="permissão de escrita"):
        ep.publicar("https://x.trycloudflare.com", "user/repo", "docs/backend.json")


def test_github_fora_do_ar_nao_explode_com_stack_trace(com_token, monkeypatch):
    def falso(metodo, url, token, corpo=None):
        raise urllib.error.URLError("conexão recusada")

    monkeypatch.setattr(ep, "_pedir", falso)
    with pytest.raises(ep.PublicacaoIndisponivel, match="falar com o GitHub"):
        ep.publicar("https://x.trycloudflare.com", "user/repo", "docs/backend.json")
