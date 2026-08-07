"""Testes da página de convites: criar, listar e revogar pela API.

O ponto sensível é a portaria: estes endpoints criam acesso ao sistema, então
uma falha aqui não vaza dados — dá o sistema inteiro.
"""

import pytest
from fastapi.testclient import TestClient

from api import main as api_main
from questoes.banco import BancoQuestoes
from questoes.convites import Convites

from test_api import LLMFake

SENHA = "senha-de-teste-longa"


@pytest.fixture
def admin(tmp_path, monkeypatch):
    monkeypatch.setattr(api_main, "_banco", BancoQuestoes(tmp_path / "banco.db"))
    monkeypatch.setattr(api_main.config_app, "ARQUIVO", tmp_path / "config.json")
    monkeypatch.setattr(api_main, "_convites", Convites(tmp_path / "convites.json"))
    monkeypatch.setattr(api_main, "criar_provedor", lambda *a, **k: LLMFake())
    api_main.config_app.salvar({
        "chave_admin": SENHA,
        "endereco_frontend": "https://exemplo.github.io/isabela",
    })
    return TestClient(api_main.app)


CABECALHO = {"X-Chave-Admin": SENHA}


def test_sem_senha_configurada_os_endpoints_ficam_fechados(tmp_path, monkeypatch):
    """Omissão não pode abrir a porta: sem senha, ninguém administra."""
    monkeypatch.setattr(api_main.config_app, "ARQUIVO", tmp_path / "vazio.json")
    monkeypatch.setattr(api_main, "_convites", Convites(tmp_path / "convites.json"))
    cliente = TestClient(api_main.app)

    resposta = cliente.get("/api/convites")
    assert resposta.status_code == 403
    assert "gerenciar_convites.py senha" in resposta.json()["detail"]


def test_senha_errada_ou_ausente_e_recusada(admin):
    assert admin.get("/api/convites").status_code == 401
    assert admin.get("/api/convites", headers={"X-Chave-Admin": "chute"}).status_code == 401
    assert admin.post("/api/convites", json={"nome": "Intruso"}).status_code == 401


def test_criar_listar_e_revogar(admin):
    criado = admin.post("/api/convites", json={"nome": "Maria Silva"}, headers=CABECALHO).json()
    assert criado["nome"] == "Maria Silva"
    assert criado["identificador"] == "maria-silva"
    assert criado["link"].endswith(f"?convite={criado['codigo']}")

    lista = admin.get("/api/convites", headers=CABECALHO).json()["convites"]
    assert [c["codigo"] for c in lista] == [criado["codigo"]]

    # o convite criado aqui vale de fato para entrar no sistema
    estado = admin.get("/api/estado", headers={"X-Convite": criado["codigo"]}).json()
    assert estado["nome"] == "Maria Silva"

    assert admin.delete(f"/api/convites/{criado['codigo']}", headers=CABECALHO).status_code == 200
    assert admin.get("/api/convites", headers=CABECALHO).json()["convites"] == []
    # e revogado, deixa de valer
    assert admin.get("/api/estado", headers={"X-Convite": criado["codigo"]}).status_code == 401


def test_nome_vazio_e_recusado(admin):
    assert admin.post("/api/convites", json={"nome": "   "}, headers=CABECALHO).status_code == 422


def test_revogar_inexistente(admin):
    assert admin.delete("/api/convites/naoexiste", headers=CABECALHO).status_code == 404


def test_a_senha_nunca_volta_em_resposta_alguma(admin):
    """Nem por descuido num endpoint de configuração ou estado."""
    admin.post("/api/convites", json={"nome": "Maria"}, headers=CABECALHO)
    corpos = [
        admin.get("/api/convites", headers=CABECALHO).text,
        admin.get("/api/identificacao").text,
        admin.get("/api/estado", headers=CABECALHO).text,
    ]
    for corpo in corpos:
        assert SENHA not in corpo
