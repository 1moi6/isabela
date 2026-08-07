"""Taxa de não-verificável por tipo de formalização, a partir do log de ciclos.

O risco de acrescentar tipos de verificação é o Gerador não saber preenchê-los:
a formalização sai errada, o veredicto vira `nao_verificavel` --- que **não
reprova a questão**, apenas a deixa passar sem conferência. O sintoma é
invisível na interface. Este relatório o torna visível.

Leitura: taxa alta num tipo denuncia descrição malfeita em `prompts/gerador.md`,
não habilidade difícil.

    python analisar_logs.py [logs/ciclos.jsonl]
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


def main(caminho: Path) -> int:
    if not caminho.exists():
        print(f"Sem log em {caminho}. Gere algumas questões primeiro.")
        return 1

    por_tipo: dict[str, Counter] = defaultdict(Counter)
    ciclos = 0
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            ciclos += 1
            for iteracao in json.loads(linha).get("iteracoes", []):
                for a in iteracao.get("verificacao", {}).get("afirmacoes", []):
                    chave = a["tipo"] + (f"/{a['consulta']}" if a.get("consulta") else "")
                    por_tipo[chave][a["veredicto"]] += 1

    if not por_tipo:
        print(f"{ciclos} ciclo(s) no log, nenhum com afirmações registradas.")
        print("O campo `afirmacoes` só existe nos ciclos gerados a partir da Fase 2.")
        return 0

    print(f"{ciclos} ciclo(s) analisado(s).\n")
    print(f"{'tipo/consulta':28s} {'total':>6s} {'ñ-verif.':>9s} {'taxa':>7s}  {'reprov.':>8s}")
    print("-" * 64)
    for chave, contagem in sorted(por_tipo.items(), key=lambda kv: -_taxa(kv[1])):
        total = sum(contagem.values())
        nv = contagem["nao_verificavel"]
        print(
            f"{chave:28s} {total:6d} {nv:9d} {_taxa(contagem):6.1%}  "
            f"{contagem['rejeitado']:8d}"
        )
    return 0


def _taxa(contagem: Counter) -> float:
    total = sum(contagem.values())
    return contagem["nao_verificavel"] / total if total else 0.0


if __name__ == "__main__":
    alvo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "logs" / "ciclos.jsonl"
    raise SystemExit(main(alvo))
