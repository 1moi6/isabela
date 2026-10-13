"""Compara os pares fácil/básico de `medir_basico.py` e confere o sorteio das alternativas.

    python analisar_basico.py [pasta]

Indicadores de simplicidade, todos tirados do texto da questão aprovada:
palavras do enunciado, itens encadeados ("a)", "b)" ...), números citados,
números não inteiros e palavras da resolução (proxy do número de passos). Nenhum
deles é "dificuldade" --- quem diz isso é o professor ---, mas um básico que não
encurta, não desencadeia e não arredonda em relação ao fácil não é básico.

A referência é a questão fácil do acervo de mesma especificação, que o painel
da Seção 6.1 avaliou: é contra ela que os professores disseram "difícil".
"""

from __future__ import annotations

import json
import re
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))

from questoes.alternativas import (  # noqa: E402
    _CITACAO, _GABARITO_COM_LETRA, _GABARITO_SO_LETRA,
)

_ITEM = re.compile(r"^\s*\(?[a-h]\)\s", re.MULTILINE)
_NUMERO = re.compile(r"(?<![\w.,])\d+(?:[.,]\d+)?")
_NAO_INTEIRO = re.compile(r"(?<![\w.,])\d+[.,]\d+|\\frac|\d+\s*/\s*\d+")


def _sem_formula(texto: str) -> str:
    return re.sub(r"\$[^$]*\$", " F ", texto)


def indicadores(q: dict) -> dict:
    enunciado = q["enunciado"]
    return {
        "palavras": len(_sem_formula(enunciado).split()),
        "itens": len(_ITEM.findall(enunciado)),
        "numeros": len(_NUMERO.findall(enunciado)),
        "nao_inteiros": len(_NAO_INTEIRO.findall(enunciado)),
        "resolucao": len(_sem_formula(q["resolucao"]).split()),
    }


def _chave(spec: dict) -> tuple:
    return (spec["habilidade_bncc"], spec["formato"])


def letras_consistentes(q: dict) -> tuple[str, bool] | None:
    """Posição da correta e se toda letra citada aponta para ela."""
    alternativas = q.get("alternativas")
    if not alternativas:
        return None
    certa = "abcd"[[a["correta"] for a in alternativas].index(True)]
    citadas = [m.group(3).lower() for t in (q["gabarito"], q["resolucao"]) for m in _CITACAO.finditer(t)]
    for padrao in (_GABARITO_SO_LETRA, _GABARITO_COM_LETRA):
        m = padrao.match(q["gabarito"])
        if m:
            citadas.append(m.group(2).lower())
            break
    return certa, all(c == certa for c in citadas)


def main(pasta: Path) -> int:
    ciclos = [json.loads(l) for f in sorted(pasta.glob("ciclos*.jsonl")) for l in open(f)]
    acervo = [json.loads(l) for l in open(RAIZ / "medicoes/acervo-consolidado/ciclos.jsonl")]
    referencia = {
        _chave(c["questao_final"]["especificacao"]): c["questao_final"]
        for c in acervo
        if c.get("aprovada") and c["questao_final"]["especificacao"]["dificuldade"] == "facil"
    }

    por_nivel: dict[str, dict] = {"facil": {}, "basico": {}}
    print(f"{len(ciclos)} ciclos\n")
    print(f"{'nível':<7} {'aprov.':>6} {'iter. médias':>12}")
    for nivel in por_nivel:
        meus = [c for c in ciclos if c["iteracoes"][0]["questao"]["especificacao"]["dificuldade"] == nivel]
        aprovados = [c for c in meus if c["aprovada"]]
        print(f"{nivel:<7} {len(aprovados):>3}/{len(meus):<2} "
              f"{statistics.mean(len(c['iteracoes']) for c in meus):>12.1f}")
        for c in aprovados:
            por_nivel[nivel][_chave(c["questao_final"]["especificacao"])] = c["questao_final"]

    pares = sorted(set(por_nivel["facil"]) & set(por_nivel["basico"]))
    print(f"\n{len(pares)} pares com as duas questões aprovadas\n")
    nomes = ["palavras", "itens", "numeros", "nao_inteiros", "resolucao"]
    print(f"{'indicador':<13} {'acervo':>7} {'fácil':>7} {'básico':>7}   básico < fácil   básico > fácil")
    for nome in nomes:
        ref = [indicadores(referencia[k])[nome] for k in pares if k in referencia]
        f = [indicadores(por_nivel["facil"][k])[nome] for k in pares]
        b = [indicadores(por_nivel["basico"][k])[nome] for k in pares]
        menor = sum(y < x for x, y in zip(f, b))
        maior = sum(y > x for x, y in zip(f, b))
        print(f"{nome:<13} {statistics.median(ref) if ref else float('nan'):>7.1f} "
              f"{statistics.median(f):>7.1f} {statistics.median(b):>7.1f}   "
              f"{menor:>6}/{len(pares):<8} {maior:>6}/{len(pares)}")
    print("(medianas; 'acervo' = a questão fácil de mesma especificação que o painel avaliou)")

    print("\nOrdem das alternativas (múltipla escolha aprovada):")
    posicoes, inconsistentes, total = {}, [], 0
    for c in ciclos:
        q = c["questao_final"]
        if not (c["aprovada"] and q and q.get("alternativas")):
            continue
        certa, ok = letras_consistentes(q)
        total += 1
        posicoes[certa] = posicoes.get(certa, 0) + 1
        if not ok:
            inconsistentes.append(q["especificacao"]["habilidade_bncc"])
    print(f"  posição da correta: {dict(sorted(posicoes.items()))} em {total} questões")
    print(f"  letra citada que não aponta para a correta: {len(inconsistentes)} {inconsistentes}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "medicoes" / "basico"))
