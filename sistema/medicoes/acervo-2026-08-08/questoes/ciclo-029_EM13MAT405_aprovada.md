# Ciclo 029 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** sem_conferencia
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento cobra a conta mensal de água residencial segundo a tabela abaixo, válida apenas para consumos entre 0 e 35 m³ por mês, pois essa é a capacidade máxima de registro do hidrômetro residencial utilizado:

- Consumo de 0 até 10 m³: tarifa mínima fixa de R$ 25,00, independente do volume efetivamente consumido.
- Consumo acima de 10 m³ e até 25 m³: R$ 25,00 mais R$ 3,50 por m³ que exceder 10 m³.
- Consumo acima de 25 m³ e até 35 m³: o valor cobrado na faixa anterior no limite de 25 m³ (ou seja, R$ 77,50) mais R$ 5,00 por m³ que exceder 25 m³.

Seja $x$ o consumo mensal em metros cúbicos, com $0 \le x \le 35$, e $C(x)$ o valor da conta, em reais, correspondente a esse consumo.

Qual das alternativas a seguir descreve corretamente o gráfico de $C$ e a imagem dessa função no domínio de validade dado?

## Alternativas

- (a) O gráfico é um segmento horizontal em $C=25$ para $0 \le x \le 10$; em seguida uma semirreta de coeficiente angular $3{,}5$ unindo $(10;25)$ a $(25;77{,}5)$; e por fim uma semirreta de coeficiente angular $5$ unindo $(25;77{,}5)$ a $(35;127{,}5)$. A função é constante em $[0,10]$ e crescente em $(10,35]$, com imagem $[25;\,127{,}5]$.  ← correta
- (b) A função é crescente em todo o domínio $[0,35]$, sem nenhum trecho constante, já que o valor da conta aumenta proporcionalmente ao consumo desde $x=0$; a imagem é $[25;\,127{,}5]$.
  - *erro representado:* Ignora a existência da tarifa mínima fixa (trecho constante em $[0,10]$), tratando a função como estritamente crescente em todo o domínio.
- (c) O gráfico é constante em $[0,10]$ e depois crescente, mas como a tarifa de R$ 3,50 e a de R$ 5,00 incidem sobre todo o consumo da faixa (e não apenas sobre o excedente), o valor máximo é $C(35) = 162{,}5$, de modo que a imagem é $[25;\,162{,}5]$.
  - *erro representado:* Aplica a tarifa marginal de cada faixa sobre o consumo total, e não apenas sobre o volume que excede o limite inferior da faixa.
- (d) Como a última faixa de cobrança (acima de 25 m³) não tem um valor de tarifa diferente após um certo ponto, o consumo pode crescer indefinidamente e a imagem da função é o intervalo ilimitado $[25, +\infty)$.
  - *erro representado:* Desconsidera a restrição contextual do domínio de validade (o hidrômetro registra no máximo 35 m³/mês), tratando o domínio como ilimitado superiormente.

## Gabarito

Alternativa A — $C$ é constante ($=25$) em $[0,10]$, crescente em $(10,35]$ (inclinação $3{,}5$ até $x=25$ e depois $5$), com imagem $[25;\,127{,}5]$.

## Resolução

**Passo 1 — Escrever a expressão algébrica por partes.**

Para $0 \le x \le 10$: $C(x) = 25$.

Para $10 < x \le 25$: $C(x) = 25 + 3{,}5\,(x-10) = 3{,}5x - 10$.

Para $25 < x \le 35$: $C(x) = 77{,}5 + 5\,(x-25) = 5x - 47{,}5$.

**Passo 2 — Verificar a continuidade nas mudanças de sentença.**

Em $x=10$: a 1ª sentença dá $25$; a 2ª dá $3{,}5(10)-10 = 25$. Coincidem.

Em $x=25$: a 2ª sentença dá $3{,}5(25)-10 = 77{,}5$; a 3ª dá $5(25)-47{,}5 = 77{,}5$. Coincidem.

Logo o gráfico não tem saltos: é um segmento horizontal seguido de duas semirretas com inclinações crescentes ($3{,}5$ e depois $5$), unidas continuamente.

**Passo 3 — Analisar crescimento.**

No trecho $[0,10]$, $C$ é constante. No trecho $(10,35]$, as inclinações $3{,}5$ e $5$ são positivas, logo $C$ é estritamente crescente nesse intervalo.

**Passo 4 — Determinar a imagem no domínio $[0,35]$.**

O valor mínimo ocorre em $x=0$ (ou em qualquer ponto de $[0,10]$): $C=25$.

O valor máximo ocorre em $x=35$: $C(35) = 5(35) - 47{,}5 = 175 - 47{,}5 = 127{,}5$.

Como $C$ é contínua e não decrescente em todo o domínio, ela assume **todos** os valores entre $25$ e $127{,}5$. Portanto a imagem é o intervalo $[25;\,127{,}5]$.

**Passo 5 — Comparar com as alternativas.**

A alternativa que descreve corretamente o trecho constante em $[0,10]$, o crescimento em $(10,35]$ com as inclinações corretas e a imagem $[25;\,127{,}5]$ é a alternativa **A**.

As demais alternativas cometem erros: ignorar o trecho de tarifa fixa (constante), aplicar a tarifa marginal sobre o consumo total em vez de apenas sobre o excedente, ou desconsiderar o limite superior do domínio de validade (35 m³) imposto pelo hidrômetro.

## Formalização verificável

- `funcao` — expressão `Piecewise((25, x<=10), (Rational(7,2)*x - 10, x<=25), (5*x - Rational(95,2), True))`, esperado `Interval(25, Rational(255,2))`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0,35)'}`
- `funcao` — expressão `Piecewise((25, x<=10), (Rational(7,2)*x - 10, x<=25), (5*x - Rational(95,2), True))`, esperado `crescente`, parâmetros `{'consulta': 'crescimento', 'dominio': 'Interval.open(10,35)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** nao_verificavel — Nenhuma das 2 afirmações pôde ser verificada. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((25, x <= 10), (7*x/2 - 10, x <= 25), (5*x - 95/2, True)). Conferir manualmente. | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((25, x <= 10), (7*x/2 - 10, x <= 25), (5*x - 95/2, True)). Conferir manualmente.
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=nao_verificavel
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta a tabela de tarifas de forma completa e sem ambiguidade, define claramente o domínio de validade (0 a 35 m³) e explicita o que é pedido (descrição do gráfico e da imagem de C). Os dados são suficientes para resolver sem suposições adicionais.
  - adequacao_nivel: 3/5 — O processo cognitivo real exigido (montar a expressão algébrica por partes, verificar continuidade nos pontos de transição, analisar crescimento em cada trecho e determinar a imagem combinando os resultados) corresponde mais a 'aplicar/analisar' do que a 'entender', nível declarado na especificação. A estrutura de resposta é relacional (SOLO), integrando vários aspectos em uma única conclusão coerente — o que é positivo em si, mas incoerente com o nível cognitivo rotulado como 'entender'.
  - alinhamento_bncc: 5/5 — Cumpre integralmente as exigências: função definida por mais de uma sentença em contexto real (conta de água), exige converter a tabela em representação algébrica e gráfica, e articula em um único problema a identificação de domínio de validade, crescimento e imagem — não há justaposição de itens independentes, e a mudança de sentença é efetivamente mobilizada.
  - distratores: 5/5 — Cada distrator representa um erro conceitual plausível e comum: ignorar a tarifa fixa constante, aplicar a tarifa marginal sobre o consumo total em vez do excedente, e desconsiderar a restrição de domínio imposta pelo contexto. Nenhum é absurdo ou trivialmente descartável sem cálculo.
  - originalidade: 4/5 — O contexto de conta de água é tradicional em livros didáticos, mas a introdução do limite físico do hidrômetro como justificativa para a restrição de domínio é um elemento não convencional que evita o efeito Topaze parcialmente, exigindo do aluno perceber essa restrição por si mesmo.
