"""Mede, com provedor real, se o nível "básico" sai de fato mais simples que o "fácil".

O nível veio do painel docente (Seção 6.1 da dissertação), e a suíte não diz
nada sobre ele: o LLM fake devolve o que lhe mandam. O desenho é pareado ---
para cada uma das 15 habilidades, a especificação "fácil" do plano do acervo
é gerada duas vezes na mesma execução, uma como fácil e outra como básico, com
tudo o mais igual (habilidade, temas, Bloom, natureza, formato, contexto). O
formato alterna entre as habilidades, para que os dois apareçam.

    python medir_basico.py [destino] [--parte i/n] [--provedor P] [--modelo ID]

Os indicadores de simplicidade saem de `analisar_basico.py`, que lê o log.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))

import gerar_acervo  # noqa: E402
from questoes.agentes import (  # noqa: E402
    CriticoDidatico, Gerador, Orquestrador, VerificadorSimbolico,
)
from questoes.especificacao import Dificuldade, Especificacao, Formato  # noqa: E402
from questoes.llm import criar_provedor  # noqa: E402


def plano() -> list[dict]:
    """30 especificações: 15 pares (fácil, básico), um par por habilidade."""
    faceis = [e for e in gerar_acervo.plano() if e["dificuldade"] == Dificuldade.FACIL]
    codigos = sorted({e["habilidade_bncc"] for e in faceis})
    pares = []
    for j, codigo in enumerate(codigos):
        formato = Formato.MULTIPLA_ESCOLHA if j % 2 == 0 else Formato.DISCURSIVA
        base = next(e for e in faceis if e["habilidade_bncc"] == codigo and e["formato"] == formato)
        for nivel in (Dificuldade.FACIL, Dificuldade.BASICO):
            pares.append({**base, "dificuldade": nivel})
    return pares


def main(destino: Path, parte: int, de: int, provedor_nome: str, modelo: str | None) -> int:
    especificacoes = plano()
    minhas = [e for i, e in enumerate(especificacoes) if i % de == parte - 1]
    destino.mkdir(parents=True, exist_ok=True)
    log = destino / (f"ciclos-{parte}.jsonl" if de > 1 else "ciclos.jsonl")

    provedor = criar_provedor(provedor_nome, modelo=modelo)
    if parte == 1:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=RAIZ
        ).stdout.strip()
        (destino / "execucao.json").write_text(json.dumps({
            "gerado_em": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "provedor": provedor_nome, "modelo": getattr(provedor, "_modelo", modelo or "?"),
            "commit": sha, "total_planejado": len(especificacoes),
            "desenho": "15 pares facil/basico sobre as especificações fáceis do plano do acervo",
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    orq = Orquestrador(
        Gerador(provedor), VerificadorSimbolico(), CriticoDidatico(provedor), log_dir=None,
    )
    for n, bruta in enumerate(minhas, 1):
        spec = Especificacao(**bruta)
        t0 = time.time()
        try:
            resultado = orq.produzir(spec)
        except Exception as exc:
            print(f"[{parte}] {n}/{len(minhas)} {spec.habilidade_bncc}: ERRO {exc}", flush=True)
            continue
        with open(log, "a", encoding="utf-8") as f:
            f.write(json.dumps(resultado.model_dump(mode="json"), ensure_ascii=False) + "\n")
        print(f"[{parte}] {n}/{len(minhas)} {spec.habilidade_bncc} {spec.formato.value[:4]}/"
              f"{spec.dificuldade.value}: {'ok' if resultado.aprovada else 'DESCARTADA'} "
              f"{len(resultado.iteracoes)}it {time.time()-t0:.0f}s", flush=True)
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fatia = next((a for a in sys.argv[1:] if a.startswith("--parte")), "--parte=1/1")
    parte, de = (int(x) for x in fatia.split("=")[1].split("/"))

    def opcao(nome, padrao=None):
        valor = next((a for a in sys.argv[1:] if a.startswith(f"--{nome}=")), None)
        return valor.split("=", 1)[1] if valor else padrao

    destino = Path(args[0]) if args else RAIZ / "medicoes" / "basico"
    raise SystemExit(main(destino, parte, de, opcao("provedor", "anthropic"), opcao("modelo")))
