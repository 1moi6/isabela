"""Banco curado de questões aprovadas (SQLite) — Seção 5.4 da dissertação.

Guarda a questão aprovada, seus metadados de especificação (para filtragem
na montagem de listas) e o histórico completo de iterações (rastreabilidade).
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .modelos import Questao, ResultadoCiclo

_SCHEMA = """
CREATE TABLE IF NOT EXISTS questoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    criada_em TEXT NOT NULL,
    tema TEXT NOT NULL,
    habilidade_bncc TEXT NOT NULL,
    nivel_bloom TEXT NOT NULL,
    dificuldade TEXT NOT NULL,
    natureza TEXT NOT NULL,
    formato TEXT NOT NULL,
    veredicto_verificacao TEXT NOT NULL,
    questao_json TEXT NOT NULL,
    historico_json TEXT NOT NULL
);
"""


class BancoQuestoes:
    def __init__(self, caminho: Path | str = "banco_questoes.db"):
        self._conn = sqlite3.connect(str(caminho))
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_SCHEMA)
        self._conn.commit()

    def salvar(self, resultado: ResultadoCiclo) -> int:
        """Persiste um ciclo aprovado; retorna o id da questão."""
        if not resultado.aprovada or resultado.questao_final is None:
            raise ValueError("Apenas ciclos aprovados entram no banco curado.")
        q = resultado.questao_final
        spec = q.especificacao
        ultima = resultado.iteracoes[-1]
        cur = self._conn.execute(
            "INSERT INTO questoes (criada_em, tema, habilidade_bncc, nivel_bloom, dificuldade,"
            " natureza, formato, veredicto_verificacao, questao_json, historico_json)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                resultado.criada_em,
                spec.tema.value,
                spec.habilidade_bncc,
                spec.nivel_bloom.value,
                spec.dificuldade.value,
                spec.natureza.value,
                spec.formato.value,
                ultima.verificacao.veredicto.value,
                q.model_dump_json(),
                json.dumps([i.model_dump(mode="json") for i in resultado.iteracoes], ensure_ascii=False),
            ),
        )
        self._conn.commit()
        return cur.lastrowid

    def buscar(
        self,
        tema: str | None = None,
        dificuldade: str | None = None,
        habilidade_bncc: str | None = None,
        formato: str | None = None,
        limite: int | None = None,
    ) -> list[tuple[int, Questao]]:
        """Filtra o banco pelos metadados; retorna pares (id, Questao)."""
        clausulas, valores = [], []
        for coluna, valor in (
            ("tema", tema),
            ("dificuldade", dificuldade),
            ("habilidade_bncc", habilidade_bncc),
            ("formato", formato),
        ):
            if valor is not None:
                clausulas.append(f"{coluna} = ?")
                valores.append(valor)
        sql = "SELECT id, questao_json FROM questoes"
        if clausulas:
            sql += " WHERE " + " AND ".join(clausulas)
        sql += " ORDER BY id"
        if limite:
            sql += f" LIMIT {int(limite)}"
        linhas = self._conn.execute(sql, valores).fetchall()
        return [(r["id"], Questao.model_validate_json(r["questao_json"])) for r in linhas]

    def total(self) -> int:
        return self._conn.execute("SELECT COUNT(*) FROM questoes").fetchone()[0]

    def fechar(self) -> None:
        self._conn.close()
