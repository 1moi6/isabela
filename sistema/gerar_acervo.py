"""Gera o acervo estratificado de questões (Fase A do plano de avaliação).

15 habilidades x 2 formatos x 3 dificuldades = 90 questões, com a natureza
alternando dentro de cada habilidade e o nível cognitivo sorteado entre os
`bloom_sugerido`. Serve a dois fins de uma vez: o banco do produto educacional
(o projeto pede 60-100 questões) e a fonte de onde se tira o material da
avaliação --- inclusive os espécimes de erro, que ficam no log toda vez que o
Verificador reprova uma primeira tentativa.

    python gerar_acervo.py [destino] [--parte i/n] [--apenas COD,COD]
                           [--provedor anthropic|openai|ollama] [--modelo ID]

`--parte` divide a lista entre processos paralelos, cada um com o seu log. Os
ciclos são independentes; só o Orquestrador é sequencial dentro de um ciclo.

`--apenas` restringe às habilidades listadas. Serve para regerar um recorte
depois de corrigir o Verificador: uma habilidade inteira de cada vez, para que
as seis questões dela tenham a mesma procedência.

`--provedor` e `--modelo` trocam quem gera. Como a semente e o plano são fixos,
duas execuções com modelos diferentes recebem exatamente as mesmas 90
especificações --- é o que torna a comparação entre modelos justa
(ver `comparar_execucoes.py`).

O cabeçalho de execução (data, provedor, modelo, SHA do commit) é gravado em
`execucao.json`: sem isso o acervo não é reproduzível e não serve de material
de dissertação.
"""

from __future__ import annotations

import json
import random
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))

from questoes.agentes import (  # noqa: E402
    CriticoDidatico, Gerador, Orquestrador, VerificadorSimbolico,
)
from questoes.especificacao import (  # noqa: E402
    Dificuldade, Especificacao, Formato, Natureza, NivelBloom, carregar_habilidades,
    contextos_para,
)
from questoes.llm import criar_provedor  # noqa: E402

SEMENTE = 20260808  # sorteio do nível cognitivo reprodutível


def plano() -> list[dict]:
    """As 90 especificações, ordenadas para que os primeiros ciclos sejam diversos.

    A ordem é um rodízio pelas habilidades: os 15 primeiros cobrem as 15
    habilidades. Assim uma conferência precoce vê o sistema inteiro, e não
    quinze variações do mesmo caso.
    """
    catalogo = carregar_habilidades()
    codigos = sorted(catalogo)
    celulas = [(f, d) for f in Formato for d in Dificuldade]

    sorteio = random.Random(SEMENTE)
    # Um embaralhamento por tema, consumido em ordem pelas seis células. Sorteio
    # COM reposição pareceria mais natural e seria pior: com 5 a 9 contextos por
    # tema, a chance de repetir dentro das seis questões vai de 89% a 100% —
    # exatamente o problema que o catálogo veio resolver. Embaralhar dá as duas
    # coisas: ordem imprevisível e nenhuma repetição.
    embaralhados: dict[str, list[str]] = {}
    especificacoes = []
    for i, (formato, dificuldade) in enumerate(celulas):
        for j, codigo in enumerate(codigos):
            h = catalogo[codigo]
            temas = h["temas"] if h["relacao_temas"] == "conjuntiva" else h["temas"][:1]
            contexto = sorteio_de_contexto(codigo, temas[0], i, sorteio, embaralhados)
            especificacoes.append({
                "habilidade_bncc": codigo,
                "temas": temas,
                "nivel_bloom": NivelBloom(sorteio.choice(h["bloom_sugerido"])),
                "dificuldade": dificuldade,
                "natureza": Natureza.APLICADA if (i + j) % 2 == 0 else Natureza.TEORICA,
                "formato": formato,
                "contexto": contexto,
            })
    return especificacoes


# Em quantas células o contexto vem em par. Um terço: o par amplia muito o
# espaço (35 contextos dão 595 pares), mas nem toda combinação fecha, e questão
# de contexto forçado é pior que questão de contexto comum --- a rubrica penaliza
# justamente o cenário artificial. O Gerador recebe permissão explícita de usar
# só o primeiro quando o par não colar.
_PROPORCAO_EM_PAR = 3


def sorteio_de_contexto(codigo, tema, indice, sorteio, embaralhados) -> str | None:
    """Um contexto por célula, sem repetir dentro do tema; a cada três, um par.

    Quando o tema tem menos contextos que células, a lista dá a volta --- e aí a
    repetição é inevitável, não descuido.
    """
    # A fila é por HABILIDADE, não por tema: 302, 401 e 501 são todas de função
    # afim e, com fila compartilhada, sairiam com os mesmos contextos na mesma
    # ordem — repetição de outro tipo, e igualmente visível para quem folheia.
    if codigo not in embaralhados:
        disponiveis = list(contextos_para(tema))
        sorteio.shuffle(disponiveis)
        embaralhados[codigo] = disponiveis
    fila = embaralhados[codigo]
    if not fila:
        return None
    principal = fila[indice % len(fila)]
    if indice % _PROPORCAO_EM_PAR != 2 or len(fila) < 2:
        return principal
    segundo = fila[(indice + len(fila) // 2) % len(fila)]
    return principal if segundo == principal else f"{principal} + {segundo}"


def main(
    destino: Path,
    parte: int,
    de: int,
    apenas: set[str] | None = None,
    provedor_nome: str = "anthropic",
    modelo: str | None = None,
) -> int:
    especificacoes = plano()
    if apenas:
        especificacoes = [e for e in especificacoes if e["habilidade_bncc"] in apenas]
    minhas = [e for i, e in enumerate(especificacoes) if i % de == parte - 1]
    destino.mkdir(parents=True, exist_ok=True)
    log = destino / (f"ciclos-{parte}.jsonl" if de > 1 else "ciclos.jsonl")

    provedor = criar_provedor(provedor_nome, modelo=modelo)
    modelo_usado = getattr(provedor, "_modelo", modelo or "?")
    if parte == 1:
        sha = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=RAIZ
        ).stdout.strip()
        (destino / "execucao.json").write_text(json.dumps({
            "gerado_em": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "provedor": provedor_nome, "modelo": modelo_usado, "commit": sha,
            "total_planejado": len(especificacoes), "semente": SEMENTE,
            "apenas": sorted(apenas) if apenas else None,
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    orq = Orquestrador(
        Gerador(provedor), VerificadorSimbolico(), CriticoDidatico(provedor),
        log_dir=None,
    )
    inicio, feitos, aprovadas = time.time(), 0, 0
    for n, bruta in enumerate(minhas, 1):
        spec = Especificacao(**bruta)
        t0 = time.time()
        try:
            resultado = orq.produzir(spec)
        except Exception as exc:
            print(f"[{parte}] {n}/{len(minhas)} {spec.habilidade_bncc}: "
                  f"ERRO {type(exc).__name__}: {exc}", flush=True)
            continue
        feitos += 1
        aprovadas += bool(resultado.aprovada)
        registro = {
            **resultado.model_dump(mode="json"),
            "bloom_divergente": spec.bloom_diverge(),
            "bloom_sugerido": spec.bloom_sugerido(),
        }
        with open(log, "a", encoding="utf-8") as f:
            f.write(json.dumps(registro, ensure_ascii=False) + "\n")
        ultima = resultado.iteracoes[-1].verificacao
        print(
            f"[{parte}] {n}/{len(minhas)} {spec.habilidade_bncc} "
            f"{spec.formato.value[:4]}/{spec.dificuldade.value[:4]}: "
            f"{'ok' if resultado.aprovada else 'DESCARTADA'} "
            f"{len(resultado.iteracoes)}it {time.time()-t0:.0f}s {ultima.veredicto.value}",
            flush=True,
        )

    print(f"[{parte}] fim: {feitos} ciclos, {aprovadas} aprovadas, "
          f"{(time.time()-inicio)/60:.0f} min", flush=True)
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fatia = next((a for a in sys.argv[1:] if a.startswith("--parte")), "--parte=1/1")
    parte, de = (int(x) for x in fatia.split("=")[1].split("/"))
    recorte = next((a for a in sys.argv[1:] if a.startswith("--apenas")), None)
    apenas = set(recorte.split("=")[1].split(",")) if recorte else None

    def opcao(nome, padrao=None):
        achado = next((a for a in sys.argv[1:] if a.startswith(f"--{nome}=")), None)
        return achado.split("=", 1)[1] if achado else padrao

    alvo = Path(args[0]) if args else RAIZ / "medicoes" / "acervo"
    raise SystemExit(
        main(alvo, parte, de, apenas, opcao("provedor", "anthropic"), opcao("modelo"))
    )
