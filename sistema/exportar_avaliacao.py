"""Monta o material que vai para o professor avaliar — e só o que ele pode ver.

`exportar_medicao.py` produz o dossiê completo de cada ciclo: resolução,
garantia obtida, veredicto do Verificador e o parecer do Crítico com nota por
critério. Aquilo é para **nós** analisarmos. Mandado a um avaliador, mede se ele
concorda com uma crítica que acabou de ler, não o julgamento dele — e torna o P3
do plano do painel (o rótulo de garantia significa alguma coisa?) impossível de
testar, porque o rótulo estaria impresso na página.

Este script produz o outro lado: enunciado, alternativas quando houver, gabarito
proposto e a habilidade declarada. **Sem** resolução, sem garantia, sem
veredicto, sem parecer, e sem o `erro_representado` de cada distrator.

    python exportar_avaliacao.py <ciclos.jsonl> [pasta] [--avaliadores N]
                                 [--ancora N] [--semente N] [--incluir-descartadas]

Produz um documento por avaliador, uma planilha de respostas por avaliador e um
`_chave.csv` que **não se envia a ninguém** — é ele que liga cada código de item
de volta ao ciclo, à garantia e à habilidade, na hora de analisar.

## Por que distribuir, e quando NÃO distribuir

O acervo tem 90 questões e o instrumento leva 3 a 4 minutos por item: avaliar
tudo sozinho passa de cinco horas. O que volta não são 90 avaliações — são umas
vinte boas e setenta apressadas, sem marcador de qual é qual.

A saída é distribuir: um bloco-âncora que todos veem, mais um lote próprio para
cada um. Isso serve à **curadoria do acervo** (esta questão entra no banco?),
que é entregável do produto e precisa das 90 vistas uma vez cada.

Não serve ao **painel formal** da Rodada 2, que exige os mesmos itens para todo
mundo: concordância entre avaliadores (Kendall's W, Krippendorff's α) não se
calcula sobre lotes diferentes. Para aquilo, rode com `--avaliadores=1` e use o
documento único com todos, recortando a amostra antes.
"""

from __future__ import annotations

import csv
import json
import random
import sys
from pathlib import Path

SEMENTE = 20260810  # distribuição reprodutível, como em gerar_acervo.py

# Minutos por item, para o aviso de duração. Vem de ler um enunciado de ~700
# caracteres com atenção, conferir o gabarito e justificar a decisão.
MINUTOS_POR_ITEM = 3.5
LIMITE_RAZOAVEL = 75  # acima disto, participação voluntária começa a decair

COLUNAS_RESPOSTA = ["item", "tem_erro", "onde", "decisao", "por_que"]
COLUNAS_CHAVE = [
    "item", "avaliadores", "ciclo", "habilidade", "temas", "dificuldade",
    "natureza", "formato", "nivel_bloom", "garantia", "aprovada",
]

GARANTIA = {
    "aprovado": "conferido",
    "aprovado_ressalva_numerica": "conferido_em_parte",
    "aprovado_parcial": "conferido_em_parte",
    "nao_verificavel": "sem_conferencia",
    "rejeitado": "sem_conferencia",
}

INSTRUCOES = """\
## Como responder

São {n} questões de Matemática do Ensino Médio. Leia cada uma como leria uma
questão que você pensasse em usar com a sua turma, e responda às três perguntas
que vêm logo abaixo dela.

**A amostra tem qualidade variável, e pode conter questões com erro matemático.**
Se encontrar algum, aponte onde.

Não há resposta certa sobre você: o que está sendo avaliado é o sistema que
produziu estas questões, não quem as lê. Um "recusada" bem justificado vale mais
para este trabalho do que um "aceita" por gentileza.

Você pode responder direto neste documento ou na planilha `{planilha}`, que já
vem com os códigos dos itens nas linhas. O que for mais cômodo.

Tempo estimado: cerca de {minutos} minutos.
"""

ITENS_DE_ANALISE = """\
**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>
"""

FECHAMENTO = """\
---

## Para terminar

**1. Você usaria um sistema assim no seu planejamento? Por quê?**

>

**2. O que faltou nas questões que você viu?**

>

**3. O que atrapalhou — na questão, no enunciado, no formato deste material?**

>

Obrigado. Se quiser saber quais itens tinham erro e qual era, é só pedir.
"""


def carregar(caminho: Path) -> list[dict]:
    linhas = [l for l in caminho.read_text(encoding="utf-8").splitlines() if l.strip()]
    return [json.loads(l) for l in linhas]


def _questao(ciclo: dict) -> dict:
    """A questão que o ciclo entregou — a última, já revisada."""
    return ciclo.get("questao_final") or ciclo["iteracoes"][-1]["questao"]


def _garantia(ciclo: dict) -> str:
    return GARANTIA.get(ciclo["iteracoes"][-1]["verificacao"]["veredicto"], "sem_conferencia")


def _fila_de_estratos(por_estrato: dict, sorteio: random.Random) -> list:
    """Ordem de visita dos estratos, alternando o último eixo da chave.

    Sortear os estratos soltos deixava a âncora enviesada --- na primeira
    execução saíram cinco itens difíceis e um fácil, porque nada impedia que os
    seis primeiros estratos sorteados fossem quase todos da mesma dificuldade.
    Como é sobre o bloco comum que se compara um avaliador com o outro, ele
    precisa parecer com o acervo, e não com um canto dele.
    """
    grupos: dict = {}
    for chave in por_estrato:
        grupos.setdefault(chave[-1], []).append(chave)
    for grupo in grupos.values():
        sorteio.shuffle(grupo)

    ordem = sorted(grupos)
    sorteio.shuffle(ordem)
    fila = []
    while any(grupos.values()):
        for eixo in ordem:
            if grupos[eixo]:
                fila.append(grupos[eixo].pop())
    return fila


def distribuir(itens: list[str], avaliadores: int, ancora: int, sorteio: random.Random,
               chave_de_estrato) -> tuple[list[str], list[list[str]]]:
    """Um bloco comum a todos, e o resto repartido em lotes diversos.

    A âncora é escolhida percorrendo os estratos (habilidade, dificuldade), e não
    sorteada solta: seis itens da mesma habilidade não diriam nada sobre
    divergência entre avaliadores, que é a única coisa que o bloco comum permite
    afirmar quando os lotes são diferentes.

    O resto é distribuído em rodízio depois de embaralhado, para que nenhum lote
    concentre uma habilidade ou uma dificuldade.
    """
    por_estrato: dict = {}
    for item in itens:
        por_estrato.setdefault(chave_de_estrato(item), []).append(item)
    for grupo in por_estrato.values():
        sorteio.shuffle(grupo)

    comuns: list[str] = []
    fila = _fila_de_estratos(por_estrato, sorteio)
    while len(comuns) < ancora and any(por_estrato.values()):
        for e in fila:
            if len(comuns) >= ancora:
                break
            if por_estrato[e]:
                comuns.append(por_estrato[e].pop())

    restantes = [i for grupo in por_estrato.values() for i in grupo]
    sorteio.shuffle(restantes)
    lotes: list[list[str]] = [[] for _ in range(avaliadores)]
    for n, item in enumerate(restantes):
        lotes[n % avaliadores].append(item)
    return comuns, lotes


def redigir_item(codigo: str, ciclo: dict, catalogo: dict) -> str:
    """Uma questão como o avaliador a vê. Tudo que não está aqui é de propósito."""
    q = _questao(ciclo)
    spec = q["especificacao"]
    codigo_bncc = spec["habilidade_bncc"]
    descricao = (catalogo.get(codigo_bncc) or {}).get("descricao", "")

    partes = [f"### {codigo}\n", q["enunciado"].strip(), ""]

    if q.get("alternativas"):
        # Sem marcar a correta e sem `erro_representado`: o primeiro entrega a
        # resposta, o segundo é anotação interna do Gerador sobre o distrator.
        for letra, alt in zip("abcde", q["alternativas"]):
            partes.append(f"({letra}) {alt['texto'].strip()}")
        partes.append("")

    partes += [
        f"**Gabarito proposto:** {q['gabarito'].strip()}",
        "",
        f"**Habilidade declarada:** {codigo_bncc} — {descricao}",
        "",
        ITENS_DE_ANALISE,
        "---",
        "",
    ]
    return "\n".join(partes)


def main(origem: Path, destino: Path, avaliadores: int, ancora: int, semente: int,
         incluir_descartadas: bool) -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
    from questoes.especificacao import carregar_habilidades

    catalogo = carregar_habilidades()
    ciclos = carregar(origem)

    # Ciclos descartados não entram por omissão: o sistema os recusou, e
    # oferecê-los como candidatos ao banco mediria outra coisa. Ficam disponíveis
    # atrás da opção porque servem de espécime de erro para o Bloco I.
    codigos = {
        f"Q{n:03d}": c
        for n, c in enumerate(ciclos, 1)
        if c["aprovada"] or incluir_descartadas
    }
    if not codigos:
        raise SystemExit("Nenhum ciclo aproveitável em " + str(origem))
    if ancora >= len(codigos):
        raise SystemExit(f"Âncora de {ancora} não cabe em {len(codigos)} itens.")

    def estrato(codigo: str) -> tuple:
        spec = _questao(codigos[codigo])["especificacao"]
        return (spec["habilidade_bncc"], spec["dificuldade"])

    sorteio = random.Random(semente)
    comuns, lotes = distribuir(sorted(codigos), avaliadores, ancora, sorteio, estrato)

    destino.mkdir(parents=True, exist_ok=True)
    quem_recebeu: dict[str, list[int]] = {c: [] for c in codigos}
    for n, lote in enumerate(lotes, 1):
        meus = comuns + lote
        sorteio.shuffle(meus)  # a âncora não fica sempre no início
        for c in meus:
            quem_recebeu[c].append(n)

        planilha = f"respostas-avaliador-{n}.csv"
        corpo = [
            f"# Avaliação de questões — avaliador {n}\n",
            INSTRUCOES.format(
                n=len(meus), planilha=planilha,
                minutos=round(len(meus) * MINUTOS_POR_ITEM / 5) * 5,
            ),
            "---\n",
        ]
        corpo += [redigir_item(c, codigos[c], catalogo) for c in meus]
        corpo.append(FECHAMENTO)
        (destino / f"avaliador-{n}.md").write_text("\n".join(corpo), encoding="utf-8")

        with open(destino / planilha, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(COLUNAS_RESPOSTA)
            for c in meus:
                escritor.writerow([c, "", "", "", ""])

    # A chave fica de fora do material: é ela que permite ler as respostas por
    # garantia obtida (P3) sem que o avaliador tenha visto o rótulo.
    with open(destino / "_chave.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS_CHAVE)
        escritor.writeheader()
        for c, ciclo in sorted(codigos.items()):
            spec = _questao(ciclo)["especificacao"]
            escritor.writerow({
                "item": c,
                "avaliadores": " ".join(str(a) for a in quem_recebeu[c]),
                "ciclo": ciclos.index(ciclo) + 1,
                "habilidade": spec["habilidade_bncc"],
                "temas": "+".join(spec.get("temas") or []),
                "dificuldade": spec["dificuldade"],
                "natureza": spec["natureza"],
                "formato": spec["formato"],
                "nivel_bloom": spec["nivel_bloom"],
                "garantia": _garantia(ciclo),
                "aprovada": ciclo["aprovada"],
            })

    por_pessoa = len(comuns) + max(len(l) for l in lotes)
    minutos = por_pessoa * MINUTOS_POR_ITEM
    print(f"{len(codigos)} itens em {avaliadores} lote(s), {len(comuns)} comuns a todos.")
    print(f"Até {por_pessoa} itens por avaliador — cerca de {minutos:.0f} minutos.")
    if minutos > LIMITE_RAZOAVEL:
        print(f"  AVISO: acima de {LIMITE_RAZOAVEL} min. Aumente --avaliadores ou "
              f"reduza --ancora; sessão longa devolve resposta apressada no fim.")
    if not incluir_descartadas:
        fora = len(ciclos) - len(codigos)
        if fora:
            print(f"{fora} ciclo(s) descartado(s) ficaram de fora (--incluir-descartadas).")
    print(f"Material em {destino}/ — NÃO envie o _chave.csv junto.")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        raise SystemExit(2)

    def opcao(nome, padrao):
        achado = next((a for a in sys.argv[1:] if a.startswith(f"--{nome}=")), None)
        return type(padrao)(achado.split("=", 1)[1]) if achado else padrao

    origem = Path(args[0])
    destino = Path(args[1]) if len(args) > 1 else origem.parent / "avaliacao"
    raise SystemExit(main(
        origem, destino,
        avaliadores=opcao("avaliadores", 5),
        ancora=opcao("ancora", 6),
        semente=opcao("semente", SEMENTE),
        incluir_descartadas="--incluir-descartadas" in sys.argv[1:],
    ))
