"""Convites de acesso: identificam quem está usando, sem exigir senha.

Cada pessoa convidada recebe um link com um código único. O código identifica
a pessoa e dá a ela um banco de questões próprio. Não há cadastro, não há senha
e o sistema não guarda credencial alguma --- a chave de API de cada um fica no
navegador dela (ver `api/main.py`).

**Sem convites cadastrados, o sistema roda em modo local**: uso individual na
própria máquina, sem autenticação, exatamente como antes. Criar o primeiro
convite é o que liga o modo compartilhado.

O identificador do dono é derivado do nome, não do código: revogar um convite e
emitir outro para a mesma pessoa preserva o banco dela.
"""

from __future__ import annotations

import json
import re
import secrets
import threading
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ARQUIVO = RAIZ / "convites.json"

DONO_LOCAL = "local"

# O arquivo é lido, alterado e reescrito inteiro. Sem a trava, dois pedidos
# simultâneos leem o mesmo estado e o segundo apaga a contagem do primeiro ---
# que é exatamente o cenário de dez convidados testando ao mesmo tempo.
_TRAVA = threading.Lock()


def identificador_de(nome: str) -> str:
    """'Maria Silva' -> 'maria-silva'. Estável entre reemissões de convite."""
    sem_acento = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", sem_acento.lower()).strip("-") or "sem-nome"


class Convites:
    def __init__(self, caminho: Path | str = ARQUIVO):
        self.caminho = Path(caminho)

    def _ler(self) -> dict[str, dict]:
        if not self.caminho.exists():
            return {}
        try:
            return json.loads(self.caminho.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}

    def _gravar(self, convites: dict[str, dict]) -> None:
        self.caminho.write_text(
            json.dumps(convites, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    @property
    def modo_compartilhado(self) -> bool:
        """O modo depende da **existência** do arquivo, não de ele ter convites.

        Se dependesse do conteúdo, revogar o último convite desligaria a
        autenticação e devolveria acesso livre a quem acabou de ser revogado ---
        o oposto do pretendido. Com o arquivo vazio, ninguém entra. Para voltar
        ao modo local, apague `convites.json` deliberadamente.
        """
        return self.caminho.exists()

    def identificar(self, codigo: str | None) -> dict | None:
        """Devolve {nome, identificador} do convite, ou None se o código não vale."""
        if not codigo:
            return None
        convite = self._ler().get(codigo)
        return dict(convite, codigo=codigo) if convite else None

    def criar(self, nome: str) -> dict:
        with _TRAVA:
            convites = self._ler()
            codigo = secrets.token_urlsafe(8)
            convites[codigo] = {
                "nome": nome,
                "identificador": identificador_de(nome),
                "criado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "usos_da_chave_do_servidor": 0,
            }
            self._gravar(convites)
            return dict(convites[codigo], codigo=codigo)

    def remover(self, codigo: str) -> bool:
        with _TRAVA:
            convites = self._ler()
            if codigo not in convites:
                return False
            del convites[codigo]
            self._gravar(convites)
            return True

    def usos(self, codigo: str) -> int:
        """Quantas gerações este convite já pagou com a chave do servidor."""
        return int(self._ler().get(codigo, {}).get("usos_da_chave_do_servidor", 0))

    def registrar_uso(self, codigo: str) -> int:
        """Conta mais uma geração paga pelo servidor; devolve o total.

        Só é chamado quando é a chave do dono que banca a requisição. Quem traz
        a própria chave não é contabilizado: a cota existe para limitar gasto,
        não para limitar uso.
        """
        with _TRAVA:
            convites = self._ler()
            if codigo not in convites:
                return 0
            atual = int(convites[codigo].get("usos_da_chave_do_servidor", 0)) + 1
            convites[codigo]["usos_da_chave_do_servidor"] = atual
            self._gravar(convites)
            return atual

    def listar(self) -> list[dict]:
        return [dict(c, codigo=k) for k, c in sorted(
            self._ler().items(), key=lambda kv: kv[1].get("nome", "")
        )]
