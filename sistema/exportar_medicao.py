"""Transforma um log de ciclos em material legível para análise.

`analisar_logs.py` responde "que tipo de formalização está falhando?". Este
script responde "o que o sistema produziu, exatamente?" — para leitura humana,
que é o que a avaliação empírica do Cap. 6 exige.

Exporta **todos** os ciclos, inclusive os descartados: uma questão que não
passou em três iterações costuma dizer mais sobre os limites do sistema do que
uma aprovada de primeira.

    python exportar_medicao.py <ciclos.jsonl> [pasta_de_saida]

Produz um `.md` por ciclo, com a trilha de verificação completa, e um
`_indice.csv` com as colunas que interessam à análise — inclusive quais
formalizações ficaram sem conferência.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

COLUNAS = [
    "arquivo", "habilidade", "temas", "nivel_bloom", "bloom_divergente", "dificuldade",
    "natureza", "formato", "aprovada", "iteracoes", "veredicto", "garantia",
    "nota_minima_critico", "tipos", "sem_conferencia",
]

GARANTIA = {
    "aprovado": "conferido",
    "aprovado_ressalva_numerica": "conferido_em_parte",
    "aprovado_parcial": "conferido_em_parte",
    "nao_verificavel": "sem_conferencia",
    "rejeitado": "sem_conferencia",
}


def _afirmacoes(verificacao: dict) -> list[str]:
    return [
        a["tipo"] + (f"/{a['consulta']}" if a.get("consulta") else "")
        + f"={a['veredicto']}"
        for a in verificacao.get("afirmacoes", [])
    ]


def _markdown(indice: int, ciclo: dict) -> tuple[str, dict]:
    iteracoes = ciclo["iteracoes"]
    ultima = iteracoes[-1]
    questao = ciclo.get("questao_final") or ultima["questao"]
    spec = questao["especificacao"]
    veredicto = ultima["verificacao"]["veredicto"]
    temas = spec.get("temas") or [spec.get("tema", "")]

    linhas = [
        f"# Ciclo {indice:03d} — {spec['habilidade_bncc']}",
        "",
        f"- **Situação:** {'aprovada' if ciclo['aprovada'] else 'DESCARTADA após 3 iterações'}",
        f"- **Temas:** {', '.join(temas)}",
        f"- **Nível cognitivo:** {spec['nivel_bloom']}"
        + (" *(fora dos verbos da habilidade)*" if ciclo.get("bloom_divergente") else ""),
        f"- **Dificuldade:** {spec['dificuldade']} | **Natureza:** {spec['natureza']}"
        f" | **Formato:** {spec['formato']}",
        f"- **Garantia obtida:** {GARANTIA.get(veredicto, veredicto)}",
        f"- **Iterações:** {len(iteracoes)}",
        "",
        "## Enunciado",
        "",
        questao["enunciado"],
        "",
    ]

    if questao.get("alternativas"):
        linhas += ["## Alternativas", ""]
        for letra, alt in zip("abcd", questao["alternativas"]):
            linhas.append(f"- ({letra}) {alt['texto']}" + ("  ← correta" if alt["correta"] else ""))
            if alt.get("erro_representado") and not alt["correta"]:
                linhas.append(f"  - *erro representado:* {alt['erro_representado']}")
        linhas.append("")

    linhas += ["## Gabarito", "", str(questao["gabarito"]), "",
               "## Resolução", "", questao["resolucao"], ""]

    linhas += ["## Formalização verificável", ""]
    for v in questao.get("verificaveis", []):
        linhas.append(f"- `{v['tipo']}` — expressão `{v['expressao']}`, "
                      f"esperado `{v['resposta_esperada']}`"
                      + (f", parâmetros `{v['parametros']}`" if v.get("parametros") else ""))
    if not questao.get("verificaveis"):
        linhas.append("- *(nenhuma — o Gerador julgou a questão não formalizável)*")
    linhas.append("")

    linhas += ["## Trilha do ciclo", ""]
    for it in iteracoes:
        v = it["verificacao"]
        linhas.append(f"### Iteração {it['numero']}")
        linhas.append("")
        linhas.append(f"- **Verificador:** {v['veredicto']} — {v['justificativa']}")
        for a in _afirmacoes(v):
            linhas.append(f"  - {a}")
        if it.get("parecer"):
            p = it["parecer"]
            linhas.append(f"- **Crítico:** {'aprovou' if p['aprovado'] else 'reprovou'}")
            for nota in p["notas"]:
                linhas.append(f"  - {nota['criterio']}: {nota['nota']}/5 — {nota['comentario']}")
            if p.get("sugestoes_revisao"):
                linhas.append(f"  - *sugestões:* {p['sugestoes_revisao']}")
        else:
            linhas.append("- **Crítico:** não chegou a avaliar")
        if it.get("feedback_para_gerador"):
            linhas.append(f"- **Devolvido ao Gerador:** {it['feedback_para_gerador']}")
        linhas.append("")

    sem_conferencia = [
        a for a in _afirmacoes(ultima["verificacao"]) if a.endswith("=nao_verificavel")
    ]
    registro = {
        "arquivo": "",
        "habilidade": spec["habilidade_bncc"],
        "temas": "; ".join(temas),
        "nivel_bloom": spec["nivel_bloom"],
        "bloom_divergente": ciclo.get("bloom_divergente", ""),
        "dificuldade": spec["dificuldade"],
        "natureza": spec["natureza"],
        "formato": spec["formato"],
        "aprovada": ciclo["aprovada"],
        "iteracoes": len(iteracoes),
        "veredicto": veredicto,
        "garantia": GARANTIA.get(veredicto, veredicto),
        # `parecer` existe com valor nulo quando o Verificador reprovou e o
        # Crítico não chegou a avaliar — `.get(..., {})` devolveria None ali.
        "nota_minima_critico": min(
            (n["nota"] for n in (ultima.get("parecer") or {}).get("notas", [])), default=""
        ),
        "tipos": "; ".join(_afirmacoes(ultima["verificacao"])),
        "sem_conferencia": "; ".join(sem_conferencia),
    }
    return "\n".join(linhas), registro


def main(origem: Path, destino: Path) -> int:
    if not origem.exists():
        print(f"Sem log em {origem}.")
        return 1
    destino.mkdir(parents=True, exist_ok=True)

    registros = []
    with open(origem, encoding="utf-8") as f:
        ciclos = [json.loads(linha) for linha in f if linha.strip()]

    for i, ciclo in enumerate(ciclos, 1):
        texto, registro = _markdown(i, ciclo)
        situacao = "aprovada" if ciclo["aprovada"] else "descartada"
        nome = f"ciclo-{i:03d}_{registro['habilidade']}_{situacao}.md"
        (destino / nome).write_text(texto, encoding="utf-8")
        registro["arquivo"] = nome
        registros.append(registro)

    # utf-8-sig: sem o BOM, o Excel em português abre os acentos errados.
    with open(destino / "_indice.csv", "w", encoding="utf-8-sig", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(registros)

    aprovadas = sum(r["aprovada"] for r in registros)
    sem_conf = sum(bool(r["sem_conferencia"]) for r in registros)
    print(f"{len(registros)} ciclos exportados para {destino}")
    print(f"  {aprovadas} aprovadas, {len(registros) - aprovadas} descartadas")
    print(f"  {sem_conf} com alguma formalização sem conferência")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    saida = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(sys.argv[1]).parent / "questoes"
    raise SystemExit(main(Path(sys.argv[1]), saida))
