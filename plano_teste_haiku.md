# Plano: testar a arquitetura com um modelo mais fraco

Preparado, **não executado**. Este documento é o roteiro para rodar sozinho.

## Por que fazer isto

A pergunta que parece estar em jogo — "dá para usar um modelo mais barato?" — não é a
interessante. A diferença de custo é de poucos dólares e não decide nada nesta dissertação.

A pergunta que importa é outra, e testa a hipótese arquitetural **pelo lado oposto**:

> Se a verificação simbólica faz o que a tese afirma, então um modelo mais fraco deve ser
> *tolerável*. Ele erra mais, o Verificador pega, o ciclo corrige. A arquitetura compra
> confiabilidade que o modelo sozinho não tem.

Isso é medível com o que já existe, e os dois resultados possíveis são publicáveis:

- **Converge com mais iterações** → a arquitetura funciona como anunciado. É evidência direta
  para o Capítulo 6, e sustenta o produto educacional como algo que roda sem depender do modelo
  mais caro.
- **Não converge** → você descobriu o **piso de capacidade** da arquitetura, que é um limite
  honesto a declarar no texto.

O mesmo desenho serve, sem alteração, para testar um modelo aberto local depois (Ollama).

## O problema metodológico que este plano resolve

As corridas do Sonnet que já existem **não servem de referência**:

| Corrida | Commit | Problema |
|---|---|---|
| `acervo-2026-08-08` | `996020b` | Verificador ainda tinha os quatro defeitos de extremo/sequência |
| `acervo-2026-08-08-refeito` | `16dfec9` | Anterior às correções de raiz complexa, float e domínio de equação |
| `acervo-consolidado` | mistura dos dois | procedência dupla |

Comparar Haiku (Verificador corrigido) contra qualquer uma delas confundiria **modelo** com
**correção do Verificador** — as métricas são todas baseadas em veredicto, e o veredicto mudou.

**Por isso as duas pernas do teste rodam no mesmo commit**, uma depois da outra. Custa o dobro e
é a única forma de o resultado significar alguma coisa.

## O que já está pronto

- `gerar_acervo.py` aceita `--provedor` e `--modelo`. Plano e semente são fixos, então as duas
  execuções recebem **exatamente as mesmas especificações**, na mesma ordem, com os mesmos
  contextos sorteados. É o que torna a comparação justa.
- `comparar_execucoes.py` põe duas execuções lado a lado: aprovação, descarte, iterações, garantia
  obtida, e a taxa de não-verificável **por tipo de formalização** — que é o indicador direto de
  "este modelo sabe escrever SymPy?".
- `analisar_logs.py` e `exportar_medicao.py` funcionam igual para qualquer execução.

Nada precisa ser alterado no código: Haiku 4.5 já consta de `FAMILIAS_COM_TEMPERATURA` em
`anthropic_llm.py`, e o sistema não usa `effort` nem thinking adaptativo, que Haiku não suporta.
Contexto de 200K e saída de 64K sobram para os ~2.300 tokens de uma questão.

## Como rodar

Da pasta `sistema/`, com `ANTHROPIC_API_KEY` no ambiente.

**Escolha o tamanho primeiro.** O recorte de 5 habilidades dá sinal suficiente para as taxas por
tipo e custa um terço:

```sh
HABS=EM13MAT302,EM13MAT304,EM13MAT402,EM13MAT501,EM13MAT507   # 30 ciclos por perna
# ou, para o teste completo, omita --apenas nos dois comandos abaixo (90 ciclos por perna)
```

**Perna 1 — referência (Sonnet, commit atual):**

```sh
DEST=medicoes/comparativo-sonnet
mkdir -p $DEST
for i in 1 2 3; do
  ./.venv/bin/python gerar_acervo.py $DEST --parte=$i/3 --apenas=$HABS >> $DEST/worker.log 2>&1 &
done; wait
```

**Perna 2 — alternativa (Haiku):**

```sh
DEST=medicoes/comparativo-haiku
mkdir -p $DEST
for i in 1 2 3; do
  ./.venv/bin/python gerar_acervo.py $DEST --parte=$i/3 --apenas=$HABS \
    --modelo=claude-haiku-4-5 >> $DEST/worker.log 2>&1 &
done; wait
```

**Comparar:**

```sh
./.venv/bin/python comparar_execucoes.py medicoes/comparativo-sonnet medicoes/comparativo-haiku
```

**Guardar as questões para leitura humana:**

```sh
./.venv/bin/python exportar_medicao.py medicoes/comparativo-haiku/ciclos.jsonl \
                                        medicoes/comparativo-haiku/questoes
```

Cada pasta ganha um `execucao.json` com data, provedor, modelo e commit — o comparador lê o nome
do modelo daí, e é o que torna a execução reproduzível.

## Custo e tempo

Tokens medidos com `count_tokens` sobre uma amostra real do acervo, incluindo iterações de revisão
e as chamadas ao Crítico:

| | por questão | 30 ciclos | 90 ciclos |
|---|---|---|---|
| Sonnet 5 (US$ 3/15 por milhão) | US$ 0,077 | US$ 2,31 | US$ 6,93 |
| Sonnet 5 promocional (US$ 2/10, até 31/08/2026) | US$ 0,051 | US$ 1,54 | US$ 4,62 |
| Haiku 4.5 (US$ 1/5 por milhão) | US$ 0,021 | US$ 0,62 | US$ 1,84 |

**Teste de 30 ciclos por perna: cerca de US$ 3.** Completo, cerca de US$ 9.

Tempo: o Sonnet fez 48 ciclos em 39 minutos com 3 processos. Estime ~25 min por perna no recorte
de 30, ~75 min no completo. Haiku tende a ser mais rápido.

Haiku usa um tokenizador mais antigo e converte o mesmo texto em ~21% menos tokens — por isso sai
por 27% do custo do Sonnet, e não por 33% como a razão de preço sugeriria.

## O que olhar, e o que cada resultado significa

Em ordem de importância:

**1. Taxa de não-verificável por tipo.** É o indicador central. Mede se o modelo sabe escrever
`Interval.open(0, oo)`, `Piecewise(...)`, `Rational(21,20)`. Se Haiku disparar em algum tipo
específico, o problema é daquele tipo no *prompt*, não do modelo em geral — e é corrigível.

**2. Descartes.** Quantas questões não sobreviveram a três iterações. É o teste de convergência.

**3. Iterações até aprovar.** Se Haiku converge em 2 ou 3 onde o Sonnet converge em 1, **a
arquitetura está fazendo exatamente o que a tese diz.**

**4. Reprovações por tipo.** Se o Verificador reprova mais com Haiku, ele está pegando erro de
verdade — o que é bom sinal para a arquitetura, não mau sinal para o modelo.

O que **não** se decide aqui: qual modelo escreve questões melhores. Isso é julgamento didático, e
quem responde é o painel docente. As duas colunas do comparador só falam de formalização e
convergência.

## Ressalvas

**A arquitetura protege o Gerador, não o Crítico.** Um erro do Gerador o SymPy pega; um erro de
julgamento do Crítico ninguém pega. Este teste troca o modelo nos **dois** papéis ao mesmo tempo,
então um resultado ruim não distingue qual dos dois degradou. Se der ruim, a rodada seguinte é
Haiku só no Gerador, mantendo o Crítico no Sonnet — hoje `gerar_acervo.py` usa o mesmo provedor
para os dois, e separá-los é uma linha.

**Não regenere o acervo com o resultado.** O acervo de 90 questões já está fechado e é o material
da Rodada 1 de avaliação. As execuções deste teste vão para pastas próprias e não substituem nada.

**As questões geradas por Haiku não entram no material do painel** sem decisão explícita — mudar o
modelo no meio muda a procedência do acervo.

## Depois

O mesmo par de comandos, trocando `--provedor=ollama --modelo=<o-que-estiver-instalado>`, roda o
teste com modelo aberto local, sem custo de API. Antes disso é preciso corrigir dois pontos do
`ollama_llm.py` — ele não define `num_predict` (a saída de ~2.300 tokens seria truncada) nem usa
`format: "json"` — e escrever um teste dele, que hoje não existe.
