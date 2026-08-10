"""Compara duas execuções do acervo — tipicamente dois modelos.

A comparação é justa porque `gerar_acervo.py` tem plano e semente fixos: duas
execuções recebem exatamente as mesmas especificações, na mesma ordem, com os
mesmos contextos. O que varia é só quem gera.

    python comparar_execucoes.py <referencia/> <alternativa/>

O que interessa não é qual modelo escreve questões mais bonitas — isso quem
julga é o professor. O que se mede aqui é o que a arquitetura promete: se a
verificação simbólica compensa um modelo mais fraco, o modelo alternativo deve
**convergir**, ainda que gastando mais iterações. Um modelo que converge em três
iterações onde o outro converge em uma é evidência a favor da hipótese
arquitetural; um que não converge marca o piso de capacidade da arquitetura.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


def carregar(pasta: Path) -> tuple[list[dict], dict]:
    caminho = pasta / "ciclos.jsonl"
    if not caminho.exists():  # execução paralela: um log por processo
        partes = sorted(pasta.glob("ciclos-*.jsonl"))
        if not partes:
            raise SystemExit(f"Sem ciclos.jsonl nem ciclos-*.jsonl em {pasta}")
        linhas = [l for p in partes for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        linhas = [l for l in caminho.read_text(encoding="utf-8").splitlines() if l.strip()]
    execucao = {}
    if (pasta / "execucao.json").exists():
        execucao = json.loads((pasta / "execucao.json").read_text(encoding="utf-8"))
    return [json.loads(l) for l in linhas], execucao


def por_tipo(ciclos: list[dict]) -> dict[str, Counter]:
    """Veredictos por tipo/consulta de formalização."""
    tabela: dict[str, Counter] = defaultdict(Counter)
    for c in ciclos:
        for it in c["iteracoes"]:
            for a in it["verificacao"].get("afirmacoes", []):
                chave = a["tipo"] + (f"/{a['consulta']}" if a.get("consulta") else "")
                tabela[chave][a["veredicto"]] += 1
    return tabela


def resumo(ciclos: list[dict]) -> dict:
    iteracoes = [len(c["iteracoes"]) for c in ciclos]
    return {
        "ciclos": len(ciclos),
        "aprovadas": sum(c["aprovada"] for c in ciclos),
        "descartadas": sum(not c["aprovada"] for c in ciclos),
        "iteracoes_media": sum(iteracoes) / len(iteracoes) if iteracoes else 0,
        "primeira_tentativa": sum(n == 1 for n in iteracoes),
        "garantia": Counter(
            c["iteracoes"][-1]["verificacao"]["veredicto"] for c in ciclos if c["aprovada"]
        ),
    }


def _linha(rotulo: str, a, b, formato="{:.0f}") -> str:
    return f"  {rotulo:26s} {formato.format(a):>12s} {formato.format(b):>12s}"


def main(ref: Path, alt: Path) -> int:
    ciclos_ref, exec_ref = carregar(ref)
    ciclos_alt, exec_alt = carregar(alt)
    nome_ref = exec_ref.get("modelo", ref.name)
    nome_alt = exec_alt.get("modelo", alt.name)

    r, a = resumo(ciclos_ref), resumo(ciclos_alt)
    print(f"\n{'':28s} {nome_ref:>12s} {nome_alt:>12s}")
    print("  " + "-" * 52)
    print(_linha("ciclos", r["ciclos"], a["ciclos"]))
    print(_linha("aprovadas", r["aprovadas"], a["aprovadas"]))
    print(_linha("descartadas", r["descartadas"], a["descartadas"]))
    print(_linha("aprovadas de primeira", r["primeira_tentativa"], a["primeira_tentativa"]))
    print(_linha("iterações (média)", r["iteracoes_media"], a["iteracoes_media"], "{:.2f}"))
    print()
    for v in ("aprovado", "aprovado_parcial", "nao_verificavel"):
        print(_linha(f"garantia: {v}", r["garantia"][v], a["garantia"][v]))

    tr, ta = por_tipo(ciclos_ref), por_tipo(ciclos_alt)
    print(f"\n  taxa de NÃO-VERIFICÁVEL por tipo — sabe escrever a formalização?")
    print(f"  {'tipo/consulta':26s} {nome_ref:>12s} {nome_alt:>12s}")
    print("  " + "-" * 52)
    for chave in sorted(set(tr) | set(ta)):
        def taxa(t):
            total = sum(t[chave].values())
            return t[chave]["nao_verificavel"] / total if total else 0.0
        print(f"  {chave:26s} {taxa(tr):11.1%} {taxa(ta):11.1%}")

    print(f"\n  reprovações por tipo — o Verificador pegou erro de verdade?")
    for chave in sorted(set(tr) | set(ta)):
        print(f"  {chave:26s} {tr[chave]['rejeitado']:12d} {ta[chave]['rejeitado']:12d}")

    print(f"""
  Leitura: se {nome_alt} aprova quase tudo, ainda que com mais iterações e mais
  não-verificáveis, a verificação simbólica compensou o modelo mais fraco — e
  isso é resultado a favor da hipótese arquitetural. Se descarta muito, o piso
  de capacidade da arquitetura está acima deste modelo, o que também é resultado.
  Nenhuma das duas colunas diz qual questão é melhor: isso é o painel docente.
""")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(Path(sys.argv[1]), Path(sys.argv[2])))
