"""Teste da descoberta do endereço da API, executando o JavaScript de verdade.

A lógica vive no navegador, então testá-la em Python seria testar uma imitação.
Aqui o `comum.js` é carregado num interpretador mínimo com `fetch` e
`localStorage` falsos — o suficiente para exercitar as decisões que importam.

O caso que motivou este arquivo: um endereço guardado que deixou de existir
prendia a pessoa a um túnel morto para sempre, porque a descoberta desistia
cedo demais.
"""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

COMUM = Path(__file__).resolve().parents[2] / "docs" / "comum.js"

pytestmark = pytest.mark.skipif(
    shutil.which("node") is None, reason="requer node para executar o JavaScript"
)

AMBIENTE = """
const guardadoBruto = %s;
const respostas = %s;

globalThis.localStorage = {
  _d: { ...guardadoBruto },
  getItem(k) { return this._d[k] ?? null; },
  setItem(k, v) { this._d[k] = String(v); },
  removeItem(k) { delete this._d[k]; },
};
globalThis.sessionStorage = { getItem: () => null, setItem() {}, removeItem() {} };
globalThis.document = { getElementById: () => null, createElement: () => ({ append() {}, remove() {} }), body: { append() {} } };
globalThis.setTimeout = () => {};

const tentativas = [];
globalThis.fetch = async (url) => {
  tentativas.push(url);
  const chave = Object.keys(respostas).find((k) => url.startsWith(k));
  if (chave === undefined) throw new Error("sem rota: " + url);
  const r = respostas[chave];
  if (r === null) throw new Error("falha de rede");
  return { ok: r.ok !== false, json: async () => r.corpo };
};
"""

RELATORIO = """
await descobrirApi(%s);
console.log(JSON.stringify({
  api: localStorage.getItem("questoes.api"),
  tentativas,
}));
"""


def executar(guardado, respostas, raiz='""'):
    programa = (
        AMBIENTE % (json.dumps(guardado), json.dumps(respostas))
        + COMUM.read_text(encoding="utf-8")
        + RELATORIO % raiz
    )
    saida = subprocess.run(
        ["node", "--input-type=module", "-e", programa],
        capture_output=True, text=True, timeout=30,
    )
    assert saida.returncode == 0, saida.stderr
    return json.loads(saida.stdout.strip().splitlines()[-1])


VIVO = {"ok": True, "corpo": {"responsavel": "X"}}


def test_endereco_guardado_que_responde_e_mantido():
    r = executar(
        {"questoes.api": "https://vivo.exemplo"},
        {"https://vivo.exemplo/api/identificacao": VIVO},
    )
    assert r["api"] == "https://vivo.exemplo"


def test_endereco_guardado_morto_e_substituido_pelo_publicado():
    """O caso real: o túnel mudou de endereço e o navegador ficou para trás."""
    r = executar(
        {"questoes.api": "https://morto.exemplo"},
        {
            "https://morto.exemplo/api/identificacao": None,   # não responde
            "/api/identificacao": None,                        # nem a mesma origem
            "backend.json": {"ok": True, "corpo": {"endereco": "https://novo.exemplo"}},
            "https://novo.exemplo/api/identificacao": VIVO,
        },
    )
    assert r["api"] == "https://novo.exemplo"


def test_mesma_origem_tem_precedencia_sobre_o_backend_json():
    """Servida pelo próprio servidor, a página não pode seguir um endereço alheio."""
    r = executar(
        {},
        {
            "/api/identificacao": VIVO,
            "backend.json": {"ok": True, "corpo": {"endereco": "https://outro.exemplo"}},
        },
    )
    assert r["api"] in (None, "")


def test_subpagina_busca_o_backend_json_um_nivel_acima():
    r = executar(
        {},
        {
            "/api/identificacao": None,
            "../backend.json": {"ok": True, "corpo": {"endereco": "https://novo.exemplo"}},
            "https://novo.exemplo/api/identificacao": VIVO,
        },
        raiz='".."',
    )
    assert r["api"] == "https://novo.exemplo"


def test_servidor_fora_do_ar_nao_grava_endereco_invalido():
    r = executar(
        {},
        {
            "/api/identificacao": None,
            "backend.json": {"ok": True, "corpo": {"endereco": "https://tambem-morto.exemplo"}},
            "https://tambem-morto.exemplo/api/identificacao": None,
        },
    )
    assert not r["api"]
