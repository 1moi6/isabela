"""Camada de provedores: o que muda entre serviços, e o que não pode falhar calado.

Nenhum teste aqui chama a rede. O que se verifica é o que a requisição carrega —
endereço, chave, teto de saída, modo JSON — porque foi exatamente aí que os
defeitos estavam: sem `base_url`, Gemini e DeepSeek eram inalcançáveis; com
`temperature` sempre enviado, a família de raciocínio da OpenAI devolvia 400.
"""

from __future__ import annotations

import sys
import types

import pytest

from questoes.llm import COMPATIVEIS_OPENAI, criar_provedor
from questoes.llm.openai_llm import MAX_TOKENS, SERVICOS, ProvedorOpenAI


class _Escolha:
    def __init__(self, conteudo, motivo="stop"):
        self.message = types.SimpleNamespace(content=conteudo)
        self.finish_reason = motivo


class _ClienteFalso:
    """Registra os argumentos em vez de falar com o serviço."""

    ultima_construcao: dict = {}

    def __init__(self, **kwargs):
        _ClienteFalso.ultima_construcao = kwargs
        self.chamada: dict = {}
        self.resposta = _Escolha('{"ok": true}')
        self.chat = types.SimpleNamespace(
            completions=types.SimpleNamespace(create=self._create)
        )

    def _create(self, **kwargs):
        self.chamada = kwargs
        return types.SimpleNamespace(choices=[self.resposta])


@pytest.fixture(autouse=True)
def _openai_falso(monkeypatch):
    """Substitui o módulo `openai`, que é dependência opcional e pode faltar."""
    modulo = types.ModuleType("openai")
    modulo.OpenAI = _ClienteFalso
    monkeypatch.setitem(sys.modules, "openai", modulo)
    for cfg in SERVICOS.values():
        monkeypatch.delenv(cfg.variavel_chave, raising=False)
    yield


def _provedor(servico, **kwargs):
    p = ProvedorOpenAI(servico=servico, api_key="k", **kwargs)
    p.completar("system diz json", "user")
    return p


# --- endereço: o defeito que tornava Gemini e DeepSeek inalcançáveis ---------


@pytest.mark.parametrize("servico", ["gemini", "deepseek"])
def test_servico_compativel_recebe_o_proprio_endereco(servico):
    _provedor(servico)
    assert _ClienteFalso.ultima_construcao["base_url"] == SERVICOS[servico].base_url


def test_openai_nao_recebe_endereco():
    """Sem base_url o SDK usa o endereço dele; passar None explodiria."""
    _provedor("openai")
    assert "base_url" not in _ClienteFalso.ultima_construcao


def test_endereco_pode_ser_sobreposto():
    """Serviço compatível fora da lista (Groq, OpenRouter, vLLM da universidade)."""
    _provedor("openai", base_url="http://servidor.local/v1")
    assert _ClienteFalso.ultima_construcao["base_url"] == "http://servidor.local/v1"


# --- chave: cada serviço tem a sua variável ---------------------------------


def test_cada_servico_le_a_propria_variavel(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "chave-deepseek")
    ProvedorOpenAI(servico="deepseek").completar("json", "u")
    assert _ClienteFalso.ultima_construcao["api_key"] == "chave-deepseek"


def test_servico_compativel_sem_chave_recusa_em_vez_de_cair_na_da_openai(monkeypatch):
    """O SDK não conhece GEMINI_API_KEY: sem esta recusa, ele usaria OPENAI_API_KEY."""
    monkeypatch.setenv("OPENAI_API_KEY", "chave-da-openai")
    with pytest.raises(RuntimeError, match="GEMINI_API_KEY"):
        ProvedorOpenAI(servico="gemini")


def test_chave_da_requisicao_vence_a_do_ambiente(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "do-ambiente")
    ProvedorOpenAI(servico="gemini", api_key="da-requisicao").completar("json", "u")
    assert _ClienteFalso.ultima_construcao["api_key"] == "da-requisicao"


# --- parâmetros da requisição ----------------------------------------------


def test_modo_json_e_teto_de_saida_sempre_presentes():
    """Sem teto o JSON sai truncado; sem modo JSON a disciplina de formato é só prosa."""
    p = _provedor("deepseek")
    chamada = p._cliente.chamada
    assert chamada["response_format"] == {"type": "json_object"}
    assert chamada["max_tokens"] == MAX_TOKENS


def test_familia_de_raciocinio_nao_recebe_temperature():
    """gpt-5 e o-series devolvem 400 com temperature != 1 e exigem max_completion_tokens."""
    p = _provedor("openai", modelo="gpt-5-nano")
    chamada = p._cliente.chamada
    assert "temperature" not in chamada
    assert "max_tokens" not in chamada
    assert chamada["max_completion_tokens"] == MAX_TOKENS


def test_modelo_comum_recebe_temperature():
    p = _provedor("openai", modelo="gpt-4o-mini")
    assert p._cliente.chamada["temperature"] == pytest.approx(0.3)


def test_modelo_padrao_e_o_do_servico():
    assert ProvedorOpenAI(servico="gemini", api_key="k")._modelo == "gemini-2.5-flash-lite"
    assert ProvedorOpenAI(servico="deepseek", api_key="k")._modelo == "deepseek-v4-flash"


# --- as duas falhas que os provedores documentam ----------------------------


def test_saida_truncada_levanta_erro_dizendo_o_motivo():
    """O Orquestrador reage a exceção pedindo concisão; um JSON pela metade, não."""
    p = ProvedorOpenAI(servico="openai", api_key="k")
    p._cliente.resposta = _Escolha('{"enunciado": "come', "length")
    with pytest.raises(RuntimeError, match="limite"):
        p.completar("json", "u")


def test_resposta_vazia_levanta_erro():
    """A DeepSeek avisa que o modo JSON às vezes devolve conteúdo vazio."""
    p = ProvedorOpenAI(servico="deepseek", api_key="k")
    p._cliente.resposta = _Escolha("")
    with pytest.raises(RuntimeError, match="vazia"):
        p.completar("json", "u")


# --- fábrica ----------------------------------------------------------------


@pytest.mark.parametrize("nome", COMPATIVEIS_OPENAI)
def test_fabrica_cria_todos_os_compativeis(nome, monkeypatch):
    for cfg in SERVICOS.values():
        monkeypatch.setenv(cfg.variavel_chave, "k")
    assert isinstance(criar_provedor(nome), ProvedorOpenAI)


def test_fabrica_repassa_url_como_base_url():
    criar_provedor("openai", api_key="k", url="http://vllm.local/v1")
    assert _ClienteFalso.ultima_construcao["base_url"] == "http://vllm.local/v1"


def test_fabrica_recusa_provedor_desconhecido():
    with pytest.raises(ValueError, match="deepseek"):
        criar_provedor("gpt")


# --- Ollama: o braço aberto, que não tinha teste nenhum ---------------------


class _HttpFalso:
    def __init__(self, corpo):
        self.corpo = corpo
        self.enviado: dict = {}

    def post(self, caminho, json):
        self.enviado = json
        corpo = self.corpo
        return types.SimpleNamespace(raise_for_status=lambda: None, json=lambda: corpo)


def _ollama(corpo, monkeypatch):
    from questoes.llm import ollama_llm

    monkeypatch.setitem(
        sys.modules, "httpx", types.ModuleType("httpx")
    )
    sys.modules["httpx"].Client = lambda **kwargs: _HttpFalso(corpo)
    p = ollama_llm.ProvedorOllama()
    return p


def test_ollama_pede_json_e_teto_de_saida(monkeypatch):
    """O padrão do Ollama é 128 tokens: sem num_predict a questão sai cortada."""
    from questoes.llm.ollama_llm import NUM_PREDICT

    p = _ollama({"message": {"content": "{}"}}, monkeypatch)
    p.completar("json", "u")
    assert p._http.enviado["format"] == "json"
    assert p._http.enviado["options"]["num_predict"] == NUM_PREDICT


def test_ollama_truncado_levanta_erro(monkeypatch):
    p = _ollama({"message": {"content": "{"}, "done_reason": "length"}, monkeypatch)
    with pytest.raises(RuntimeError, match="limite"):
        p.completar("json", "u")


# --- o modelo pertence ao provedor -----------------------------------------
#
# Provedor é escolha de quem usa (cabeçalho, por navegador); o modelo era só do
# servidor. Em modo compartilhado bastava escolher outro provedor para receber
# um nome de modelo da família errada — e o serviço recusar sem explicar.


def _cfg(provedor, modelo):
    return {"provedor": provedor, "modelo": modelo}


def test_modelo_do_servidor_vale_quando_o_provedor_e_o_mesmo():
    from api.main import _provedor_e_modelo

    quem = {"provedor": None, "modelo": None}
    assert _provedor_e_modelo(quem, _cfg("anthropic", "claude-haiku-4-5")) == (
        "anthropic", "claude-haiku-4-5",
    )


def test_modelo_do_servidor_e_ignorado_ao_trocar_de_provedor():
    from api.main import _provedor_e_modelo

    quem = {"provedor": "gemini", "modelo": None}
    assert _provedor_e_modelo(quem, _cfg("anthropic", "claude-sonnet-5")) == ("gemini", None)


def test_modelo_pedido_vence_o_do_servidor():
    from api.main import _provedor_e_modelo

    quem = {"provedor": "gemini", "modelo": "gemini-2.5-flash"}
    assert _provedor_e_modelo(quem, _cfg("anthropic", "claude-sonnet-5")) == (
        "gemini", "gemini-2.5-flash",
    )


def test_todo_provedor_da_interface_tem_rotulo_e_sugestao():
    """A lista da interface vem da API: um provedor sem rótulo apareceria vazio."""
    from api.main import MODELOS_SUGERIDOS, ROTULO_PROVEDOR
    from questoes.llm import PROVEDORES

    assert set(MODELOS_SUGERIDOS) == set(PROVEDORES) == set(ROTULO_PROVEDOR)
    assert all(MODELOS_SUGERIDOS[p] for p in PROVEDORES)
