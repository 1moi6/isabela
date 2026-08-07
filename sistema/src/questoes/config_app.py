"""Preferências locais do aplicativo, gravadas ao lado do banco.

Guarda apenas o que é escolha da máquina do professor: a pasta sincronizada
onde as questões são depositadas e o provedor de LLM preferido. **Chave de API
nunca entra aqui** — vive em variável de ambiente ou apenas na memória do
processo (ver `api/main.py`).
"""

from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ARQUIVO = RAIZ / "config_local.json"

PADRAO: dict[str, str] = {
    "pasta_sincronizada": "",
    "provedor": "anthropic",
    "modelo": "",
    # Quem mantém este servidor. Aparece para quem recebe um convite: sem isso,
    # um endereço desconhecido pedindo chave de API é indistinguível de golpe.
    "responsavel": "",
    "instituicao": "",
    "contato": "",
    # Origens autorizadas a chamar esta API de outro endereço (o GitHub Pages,
    # tipicamente), separadas por vírgula. Vazio = ninguém: a API só atende a
    # página que ela mesma serve. É restritivo de propósito — um convite que
    # vaze não deve poder ser usado a partir de qualquer site.
    "origens_permitidas": "",
    # Endereço onde a interface está publicada. Usado só para montar os links
    # de convite prontos ao publicar.
    "endereco_frontend": "",
    # Túnel nomeado da Cloudflare: nome do túnel e o endereço fixo que ele
    # atende. Preenchidos, `publicar.py` usa este túnel em vez do túnel rápido,
    # e os links de convite deixam de mudar a cada subida.
    "tunel_nomeado": "",
    "endereco_api": "",
    # Publicação automática do endereço: onde gravar o backend.json que a
    # interface lê para descobrir a API. Com isso, os links de convite ficam
    # permanentes mesmo com o endereço do túnel mudando a cada reinício.
    # O token vai no ambiente (QUESTOES_GITHUB_TOKEN), nunca aqui.
    # Senha de administração: libera a página de convites. Fica só aqui, num
    # arquivo fora do controle de versão, e nunca é devolvida por nenhuma rota.
    "chave_admin": "",
    "repositorio_frontend": "",
    "caminho_backend_json": "docs/backend.json",
    "ramo_frontend": "main",
}


def carregar() -> dict[str, str]:
    """Preferências gravadas, completadas com os padrões."""
    cfg = dict(PADRAO)
    if ARQUIVO.exists():
        try:
            cfg.update(json.loads(ARQUIVO.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            pass  # arquivo corrompido não deve impedir o app de abrir
    return cfg


def salvar(novos: dict[str, str]) -> dict[str, str]:
    """Grava apenas as chaves conhecidas e devolve a configuração completa."""
    cfg = carregar()
    cfg.update({c: str(v) for c, v in novos.items() if c in PADRAO})
    ARQUIVO.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
    return cfg
