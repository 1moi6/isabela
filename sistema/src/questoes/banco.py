"""Banco curado de questões aprovadas (SQLite) — Seção 5.4 da dissertação.

Guarda a questão aprovada, seus metadados de especificação (para filtragem
na montagem de listas) e o histórico completo de iterações (rastreabilidade).
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from .convites import DONO_LOCAL
from .modelos import AvaliacaoProfessor, Questao, ResultadoCiclo, Veredicto, garantia_de

# Questões gravadas antes do modo compartilhado têm dono NULL e pertencem ao
# uso local. Todo acesso passa por este filtro: ninguém enxerga o banco de outro.
_FILTRO_DONO = "COALESCE(dono, 'local') = ?"

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

# Colunas acrescentadas depois da primeira versão do banco. Bancos já existentes
# na máquina do professor são migrados na abertura, sem perder o conteúdo.
_COLUNAS_NOVAS = {
    "avaliacao_json": "TEXT",
    "nota_minima_critico": "INTEGER",
    "iteracoes": "INTEGER",
    # Quem é dono da questão, quando o sistema roda em modo compartilhado.
    # Linhas antigas ficam com NULL e pertencem ao dono local (ver DONO_LOCAL).
    "dono": "TEXT",
    # Uma questão pode articular mais de um tema (habilidades conjuntivas como
    # a EM13MAT507). A coluna `tema`, singular, continua existindo com o
    # primeiro tema: ela é NOT NULL desde a primeira versão do esquema e ainda
    # serve de rótulo curto. A busca por tema usa esta coluna.
    "temas": "TEXT",
    # Que conferência automática a questão recebeu de fato ('conferido',
    # 'conferido_em_parte', 'sem_conferencia'). Derivada do veredicto, guardada
    # para poder filtrar o banco sem reabrir o histórico de cada questão.
    "garantia": "TEXT",
}

# Sentinelas em volta de cada valor: sem elas, `LIKE '%funcao_afim%'` casaria
# com qualquer tema que o contivesse como pedaço. Guardar ",a,b," e buscar
# ",a," mantém a comparação exata mesmo dentro de um LIKE.
def _empacotar_temas(valores: list[str]) -> str:
    return "," + ",".join(valores) + ","


def _desempacotar_temas(bruto: str | None, tema: str) -> list[str]:
    """Lê a coluna nova; cai no `tema` singular para linhas anteriores à migração."""
    if not bruto:
        return [tema] if tema else []
    return [t for t in bruto.split(",") if t]


class BancoQuestoes:
    def __init__(self, caminho: Path | str = "banco_questoes.db"):
        # check_same_thread=False: o servidor atende cada requisição numa thread do
        # pool, e o banco é aberto uma vez só — sem isto, a segunda requisição
        # encontra a conexão presa à thread da primeira. É seguro porque o SQLite
        # aqui é serializado (sqlite3.threadsafety == 3).
        self._conn = sqlite3.connect(str(caminho), check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_SCHEMA)
        self._migrar()
        self._conn.commit()

    def _migrar(self) -> None:
        existentes = {c["name"] for c in self._conn.execute("PRAGMA table_info(questoes)")}
        for coluna, tipo in _COLUNAS_NOVAS.items():
            if coluna not in existentes:
                self._conn.execute(f"ALTER TABLE questoes ADD COLUMN {coluna} {tipo}")
        # Linhas gravadas antes da multisseleção têm um tema só: preenche a
        # coluna nova a partir dele, para que a busca por tema continue achando
        # as questões antigas.
        self._conn.execute(
            "UPDATE questoes SET temas = ',' || tema || ',' WHERE temas IS NULL"
        )
        # A garantia é função do veredicto, que as linhas antigas já guardam:
        # dá para preenchê-la sem reabrir o histórico. O mapeamento vem de
        # `garantia_de`, e não é repetido em SQL, para não divergir dele.
        pendentes = self._conn.execute(
            "SELECT id, veredicto_verificacao FROM questoes WHERE garantia IS NULL"
        ).fetchall()
        for linha in pendentes:
            self._conn.execute(
                "UPDATE questoes SET garantia = ? WHERE id = ?",
                (garantia_de(Veredicto(linha["veredicto_verificacao"])).value, linha["id"]),
            )

    def salvar(self, resultado: ResultadoCiclo, dono: str = DONO_LOCAL) -> int:
        """Persiste um ciclo aprovado; retorna o id da questão."""
        if not resultado.aprovada or resultado.questao_final is None:
            raise ValueError("Apenas ciclos aprovados entram no banco curado.")
        q = resultado.questao_final
        spec = q.especificacao
        ultima = resultado.iteracoes[-1]
        cur = self._conn.execute(
            "INSERT INTO questoes (criada_em, tema, temas, habilidade_bncc, nivel_bloom, dificuldade,"
            " natureza, formato, veredicto_verificacao, garantia, questao_json, historico_json,"
            " nota_minima_critico, iteracoes, dono)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                resultado.criada_em,
                spec.temas[0].value,
                _empacotar_temas([t.value for t in spec.temas]),
                spec.habilidade_bncc,
                spec.nivel_bloom.value,
                spec.dificuldade.value,
                spec.natureza.value,
                spec.formato.value,
                ultima.verificacao.veredicto.value,
                garantia_de(ultima.verificacao.veredicto).value,
                q.model_dump_json(),
                json.dumps([i.model_dump(mode="json") for i in resultado.iteracoes], ensure_ascii=False),
                ultima.parecer.nota_minima() if ultima.parecer else None,
                len(resultado.iteracoes),
                dono,
            ),
        )
        self._conn.commit()
        return cur.lastrowid

    def avaliar(
        self, questao_id: int, avaliacao: AvaliacaoProfessor, dono: str = DONO_LOCAL
    ) -> None:
        """Registra o julgamento do professor sobre uma questão do banco dele."""
        cur = self._conn.execute(
            f"UPDATE questoes SET avaliacao_json = ? WHERE id = ? AND {_FILTRO_DONO}",
            (avaliacao.model_dump_json(), questao_id, dono),
        )
        if cur.rowcount == 0:
            raise KeyError(f"Questão #{questao_id} não está no banco.")
        self._conn.commit()

    def obter(
        self, questao_id: int, dono: str = DONO_LOCAL
    ) -> tuple[ResultadoCiclo, AvaliacaoProfessor | None]:
        """Reconstrói o ciclo completo de uma questão e sua avaliação, se houver.

        Usado para reexportar o arquivo na pasta sincronizada quando o professor
        registra uma avaliação depois de a questão já estar salva.
        """
        r = self._conn.execute(
            "SELECT criada_em, questao_json, historico_json, avaliacao_json"
            f" FROM questoes WHERE id = ? AND {_FILTRO_DONO}",
            (questao_id, dono),
        ).fetchone()
        if r is None:
            raise KeyError(f"Questão #{questao_id} não está no banco.")
        resultado = ResultadoCiclo(
            aprovada=True,
            questao_final=Questao.model_validate_json(r["questao_json"]),
            iteracoes=json.loads(r["historico_json"]),
            criada_em=r["criada_em"],
        )
        bruta = json.loads(r["avaliacao_json"] or "null")
        return resultado, (AvaliacaoProfessor.model_validate(bruta) if bruta else None)

    def registros(self, dono: str = DONO_LOCAL) -> list[dict]:
        """Uma linha por questão, com metadados e avaliação — base do índice exportado."""
        linhas = self._conn.execute(
            "SELECT id, criada_em, tema, temas, habilidade_bncc, nivel_bloom, dificuldade, natureza,"
            " formato, veredicto_verificacao, garantia, nota_minima_critico, iteracoes, avaliacao_json,"
            f" questao_json FROM questoes WHERE {_FILTRO_DONO} ORDER BY id",
            (dono,),
        ).fetchall()
        registros = []
        for r in linhas:
            reg = dict(r)
            reg["temas"] = _desempacotar_temas(reg["temas"], reg["tema"])
            avaliacao = json.loads(reg.pop("avaliacao_json") or "null")
            reg["decisao_professor"] = (avaliacao or {}).get("decisao", "")
            reg["comentario_professor"] = (avaliacao or {}).get("comentario", "") or ""
            reg["questao"] = Questao.model_validate_json(reg.pop("questao_json"))
            registros.append(reg)
        return registros

    def buscar(
        self,
        tema: str | None = None,
        dificuldade: str | None = None,
        habilidade_bncc: str | None = None,
        formato: str | None = None,
        garantia: str | None = None,
        limite: int | None = None,
        dono: str = DONO_LOCAL,
    ) -> list[tuple[int, Questao]]:
        """Filtra o banco pelos metadados; retorna pares (id, Questao).

        `tema` casa com questões em que ele é *um dos* temas, não só o primeiro:
        uma questão que articula PA e função afim aparece na busca por qualquer
        um dos dois.
        """
        clausulas, valores = [_FILTRO_DONO], [dono]
        if tema is not None:
            clausulas.append("temas LIKE ?")
            valores.append(f"%{_empacotar_temas([tema])}%")
        for coluna, valor in (
            ("garantia", garantia),
            ("dificuldade", dificuldade),
            ("habilidade_bncc", habilidade_bncc),
            ("formato", formato),
        ):
            if valor is not None:
                clausulas.append(f"{coluna} = ?")
                valores.append(valor)
        sql = "SELECT id, questao_json FROM questoes WHERE " + " AND ".join(clausulas)
        sql += " ORDER BY id"
        if limite:
            sql += f" LIMIT {int(limite)}"
        linhas = self._conn.execute(sql, valores).fetchall()
        return [(r["id"], Questao.model_validate_json(r["questao_json"])) for r in linhas]

    def total(self, dono: str = DONO_LOCAL) -> int:
        return self._conn.execute(
            f"SELECT COUNT(*) FROM questoes WHERE {_FILTRO_DONO}", (dono,)
        ).fetchone()[0]

    def fechar(self) -> None:
        self._conn.close()
