# Ciclo 009 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento calcula o valor mensal da conta de água de acordo com o consumo $x$ (em m³) do cliente, segundo a tabela abaixo:

| Consumo mensal | Regra de cobrança |
|---|---|
| $0 \le x \le 10$ | taxa mínima fixa de R\$ 20,00 |
| $10 < x \le 20$ | R\$ 20,00 mais R\$ 3,00 por cada m³ que exceder 10 |
| $x > 20$ | R\$ 50,00 mais R\$ 5,00 por cada m³ que exceder 20 |

Seja $f(x)$ o valor, em reais, da conta de água correspondente a um consumo de $x$ m³.

a) Escreva a lei de formação algébrica de $f(x)$, especificando a expressão válida em cada uma das três faixas de consumo.

b) Qual é o domínio de validade de $f$, isto é, o conjunto de valores de $x$ para os quais a regra de cobrança faz sentido?

c) Uma família definiu que pode gastar, no máximo, R\$ 41,00 por mês com água, e sabe que seu consumo está entre 10 m³ e 20 m³. Qual é o maior consumo mensal, em m³, que essa família pode ter sem ultrapassar esse orçamento?

d) Esboce o gráfico de $f$ para $0 \le x \le 30$ e classifique o comportamento de $f$ (crescente, decrescente ou constante) em cada um dos três trechos.

e) Determine a imagem de $f$ restrita ao intervalo $0 \le x \le 30$.

## Gabarito

a) $f(x)=20$ se $0\le x\le 10$; $f(x)=3x-10$ se $10<x\le 20$; $f(x)=5x-50$ se $x>20$. b) $D(f)=[0,+\infty)$. c) 17 m³. d) constante em $[0,10]$; crescente em $(10,20]$ e em $(20,30]$ (com inclinação maior nesse último trecho). e) Imagem $=[20,100]$.

## Resolução

**a) Lei de formação**

Diretamente da tabela, escrevendo as expressões em função de $x$:

$$f(x)=\begin{cases}20, & 0\le x\le 10\\[2pt] 20+3(x-10), & 10< x\le 20\\[2pt] 50+5(x-20), & x> 20\end{cases}$$

Simplificando as duas últimas sentenças: $20+3(x-10)=3x-10$ e $50+5(x-20)=5x-50$.

$$f(x)=\begin{cases}20, & 0\le x\le 10\\ 3x-10, & 10< x\le 20\\ 5x-50, & x> 20\end{cases}$$

Verificação de continuidade: em $x=10$, $3(10)-10=20$ (coincide com a 1ª sentença); em $x=20$, $3(20)-10=50$ e $5(20)-50=50$ (coincidem). A função é contínua.

**b) Domínio de validade**

Como $x$ representa um consumo de água, não pode ser negativo, e não há limite superior estabelecido pela tarifação (a terceira faixa vale para qualquer consumo acima de 20 m³). Logo:

$$D(f) = \{x \in \mathbb{R} \mid x \ge 0\} = [0, +\infty)$$

**c) Consumo máximo dentro do orçamento**

Como o consumo da família está entre 10 e 20 m³, usa-se a segunda sentença:

$$20+3(x-10)=41$$
$$3(x-10)=21 \;\Rightarrow\; x-10=7 \;\Rightarrow\; x=17$$

Como $17 \in (10,20]$, a solução é válida nessa faixa. O consumo máximo é **17 m³**.

**d) Gráfico e comportamento**

- Para $0\le x\le 10$: o gráfico é um segmento horizontal na altura $y=20$ — $f$ é **constante**.
- Para $10< x\le 20$: o gráfico é um segmento de reta com coeficiente angular 3, subindo de $(10,20)$ até $(20,50)$ — $f$ é **crescente**.
- Para $20< x\le 30$: o gráfico é um segmento de reta com coeficiente angular 5, subindo de $(20,50)$ até $(30,100)$ — $f$ é **crescente**, e mais inclinado que no trecho anterior.

O gráfico completo é uma linha poligonal contínua: um patamar horizontal seguido de dois segmentos crescentes com inclinações diferentes.

**e) Imagem no intervalo $[0,30]$**

No trecho constante, $f$ assume apenas o valor $20$. A partir de $x=10$, $f$ cresce continuamente (sem saltos, pois a função é contínua) até atingir, em $x=30$:

$$f(30)=5(30)-50=100$$

Como $f$ é contínua e não decresce em nenhum ponto de $[0,30]$, todos os valores entre $20$ e $100$ são atingidos, e nenhum valor fora desse intervalo é atingido. Logo:

$$\text{Im}(f|_{[0,30]}) = [20, 100]$$

## Formalização verificável

- `funcao` — expressão `Piecewise((20, x<=10), (20+3*(x-10), (x>10)&(x<=20)), (50+5*(x-20), x>20))`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((20, x<=10), (20+3*(x-10), (x>10)&(x<=20)), (50+5*(x-20), x>20))`, esperado `Interval(20, 100)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, 30)'}`
- `funcao` — expressão `Piecewise((20, x<=10), (20+3*(x-10), (x>10)&(x<=20)), (50+5*(x-20), x>20))`, esperado `crescente`, parâmetros `{'consulta': 'crescimento', 'intervalo': 'Interval.open(10, 30)'}`
- `equacao` — expressão `Eq(20+3*(x-10), 41)`, esperado `[17]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 1 de 4 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((20, x <= 10), (3*x - 10, x <= 20), (5*x - 50, True)). Conferir manualmente. | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((20, x <= 10), (3*x - 10, x <= 20), (5*x - 50, True)). Conferir manualmente. | (3) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((20, x <= 10), (3*x - 10, x <= 20), (5*x - 50, True)). Conferir manualmente. | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=nao_verificavel
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é bem estruturado, com tabela precisa, condições de fronteira explícitas (uso de ≤ e <) e perguntas objetivas em cada item. Não há ambiguidade sobre o que é dado (regra de tarifação) nem sobre o que se pede em cada subitem.
  - adequacao_nivel: 3/5 — Há descompasso entre o nível declarado ('entender') e o processamento cognitivo real exigido. Os itens a) e b) são de fato compreensão/tradução de representações, mas o item c) exige resolver uma equação (nível 'aplicar'), e o item e) exige articular continuidade e monotonicidade para inferir a imagem (nível 'analisar', SOLO relacional/estendido). A questão como um todo mobiliza processos acima de 'entender', o que não invalida a questão, mas indica que o nível de Bloom declarado está subestimado em relação à demanda cognitiva efetiva.
  - alinhamento_bncc: 5/5 — Atende integralmente às exigências da EM13MAT405: função com três sentenças em contexto real (conta de água); item a) exige a conversão da tabela para lei algébrica; item d) exige conversão para representação gráfica e classificação de crescimento/decrescimento; itens b) e e) exigem identificação explícita de domínio e imagem. Os itens articulam-se em torno da mesma função, mobilizando efetivamente a mudança de sentença (não há avaliação isolada em ponto único como única tarefa).
  - distratores: 5/5 — não se aplica
  - originalidade: 3/5 — O contexto de tarifação escalonada de água é um clássico recorrente em livros didáticos para função definida por partes, análogo ao imposto de renda. A estrutura de subitens (a-e) é didaticamente eficiente, mas previsível e sem elementos que diferenciem o problema de exemplos-padrão já amplamente disseminados.
