# Ciclo 008 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento calcula o valor mensal da conta de água residencial, em reais, de acordo com o consumo mensal $x$ (em metros cúbicos), conforme a tabela abaixo:

| Faixa de consumo | Valor cobrado |
|---|---|
| $0 \le x \le 10$ | Taxa mínima fixa de R\$ 25,00 |
| $10 < x \le 25$ | R\$ 25,00 mais R\$ 2,50 por cada $m^3$ que exceder 10 $m^3$ |
| $x > 25$ | R\$ 62,50 mais R\$ 4,00 por cada $m^3$ que exceder 25 $m^3$ |

Seja $V(x)$ o valor da conta, em reais, para um consumo de $x$ $m^3$, com $x \ge 0$. Qual das alternativas descreve corretamente o gráfico de $V(x)$?

## Alternativas

- (a) Para $0\le x\le10$, o gráfico é um segmento horizontal na altura $25$. Para $10<x\le25$, um segmento crescente que parte do ponto $(10;25)$ e chega ao ponto $(25;62{,}5)$, com inclinação $2{,}5$. Para $x>25$, uma semirreta crescente que parte de $(25;62{,}5)$, com inclinação $4$, sem limite superior.  ← correta
- (b) Para $0\le x\le10$, segmento horizontal em $25$. Para $10<x\le25$, segmento crescente que parte do ponto $(10;0)$ e chega a $(25;37{,}5)$, com inclinação $2{,}5$. Para $x>25$, semirreta que parte de $(25;37{,}5)$, com inclinação $4$.
  - *erro representado:* Não soma o valor já acumulado da faixa anterior: trata cada trecho como se recomeçasse do zero em vez de continuar a partir do valor pago até ali.
- (c) Para $0\le x\le10$, segmento horizontal em $25$. Para $10<x\le25$, segmento crescente que parte de $(10;25)$ e chega a $(25;85)$, com inclinação $4$. Para $x>25$, semirreta que parte de $(25;85)$, com inclinação $2{,}5$.
  - *erro representado:* Inverte as taxas de R$ 2,50 e R$ 4,00 entre as faixas de consumo.
- (d) Para $0\le x\le10$, o gráfico é um segmento crescente que parte da origem $(0;0)$ até $(10;25)$, com inclinação $2{,}5$; a partir daí, o gráfico segue como nas demais faixas descritas na tabela.
  - *erro representado:* Ignora a existência da taxa mínima fixa, tratando o valor da conta como diretamente proporcional ao consumo desde o início (desconsidera o trecho constante).

## Gabarito

A

## Resolução

**Passo 1 — Escrever a função por partes.**

A partir da tabela:
$$V(x)=\begin{cases}25, & 0\le x\le 10\\[2pt] 25+2{,}5(x-10), & 10<x\le 25\\[2pt] 62{,}5+4(x-25), & x>25\end{cases}$$

**Passo 2 — Verificar os pontos de transição (continuidade).**

Em $x=10$: a primeira sentença dá $V(10)=25$. A segunda sentença, calculada em $x=10$, dá $25+2{,}5\cdot 0=25$. As duas coincidem, então o segundo trecho **parte do ponto $(10;25)$**, e não de $(10;0)$.

Em $x=25$: $V(25)=25+2{,}5\cdot(25-10)=25+37{,}5=62{,}5$. A terceira sentença, em $x=25$, dá $62{,}5+4\cdot0=62{,}5$. Logo o terceiro trecho **parte do ponto $(25;62{,}5)$**.

**Passo 3 — Identificar as inclinações de cada trecho.**

- Para $0\le x\le10$: $V$ é constante (inclinação $0$) — segmento horizontal em $y=25$.
- Para $10<x\le25$: coeficiente de $x$ é $2{,}5$ — segmento crescente de $(10;25)$ até $(25;62{,}5)$.
- Para $x>25$: coeficiente de $x$ é $4$ — semirreta crescente a partir de $(25;62{,}5)$, com inclinação maior que a do trecho anterior (a conta fica mais cara por m³ para quem consome mais).

**Passo 4 — Comparar com as alternativas.**

Apenas a alternativa que mostra o segmento horizontal em $25$ até $x=10$, seguido do segmento que **parte de $(10;25)$** com inclinação $2{,}5$ até $(25;62{,}5)$, e depois a semirreta que **parte de $(25;62{,}5)$** com inclinação $4$, está correta. As demais erram ao ignorar a taxa fixa acumulada, ao trocar as inclinações ou ao tratar a primeira faixa como proporcional ao consumo.

**Conclusão:** a descrição correta é a da alternativa A.

## Formalização verificável

- `funcao` — expressão `Piecewise((25, x<=10), (25 + Rational(5,2)*(x-10), (x>10) & (x<=25)), (Rational(125,2) + 4*(x-25), x>25))`, esperado `25`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `funcao` — expressão `Piecewise((25, x<=10), (25 + Rational(5,2)*(x-10), (x>10) & (x<=25)), (Rational(125,2) + 4*(x-25), x>25))`, esperado `Rational(125,2)`, parâmetros `{'consulta': 'valor', 'ponto': '25'}`
- `funcao` — expressão `Piecewise((25, x<=10), (25 + Rational(5,2)*(x-10), (x>10) & (x<=25)), (Rational(125,2) + 4*(x-25), x>25))`, esperado `Rational(165,2)`, parâmetros `{'consulta': 'valor', 'ponto': '30'}`
- `funcao` — expressão `Piecewise((25, x<=10), (25 + Rational(5,2)*(x-10), (x>10) & (x<=25)), (Rational(125,2) + 4*(x-25), x>25))`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((25, x<=10), (25 + Rational(5,2)*(x-10), (x>10) & (x<=25)), (Rational(125,2) + 4*(x-25), x>25))`, esperado `Interval(25, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 3 de 5 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (f(10) = 25). | (2) aprovado: Gabarito confirmado (f(25) = 125/2). | (3) aprovado: Gabarito confirmado (f(30) = 165/2). | (4) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((25, x <= 10), (5*x/2, x <= 25), (4*x - 75/2, True)). Conferir manualmente. | (5) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((25, x <= 10), (5*x/2, x <= 25), (4*x - 75/2, True)). Conferir manualmente.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta a tabela de forma completa e sem ambiguidade, define claramente o domínio de cada faixa e o que é pedido (identificar a descrição correta do gráfico de V(x)). As condições estão bem delimitadas com desigualdades explícitas.
  - adequacao_nivel: 4/5 — O processo exigido (traduzir a tabela em sentenças algébricas, verificar continuidade nos pontos de transição e identificar inclinações) é compatível com 'entender' (tradução entre representações), embora exija também pequenos cálculos que se aproximam de 'aplicar'. A resposta esperada é relacional (integrar os três trechos coerentemente), coerente com a taxonomia SOLO para esse nível. Conteúdo plenamente adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — Cumpre integralmente as exigências: função definida por mais de uma sentença em contexto real (conta de água); exige converter a representação tabular/algébrica para a gráfica, mobilizando a mudança de sentença nos pontos de transição (10 e 25), não bastando avaliar um único ponto. Também trabalha crescimento (inclinações diferentes) de forma articulada, não apenas justaposta.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: (B) desconsiderar o valor acumulado das faixas anteriores, (C) inverter as taxas de R$2,50 e R$4,00, (D) tratar a conta como proporcional desde o início ignorando a taxa fixa. Nenhum é absurdo ou trivialmente eliminável sem compreender a função por partes.
  - originalidade: 3/5 — O contexto de conta de água por faixas de consumo é um clássico recorrente em materiais didáticos sobre função por partes (análogo ao IR e conta de luz citados na própria habilidade). A estrutura da questão (comparar descrições textuais de gráfico) é razoavelmente original em relação ao formato usual (gráficos visuais), mas o cenário em si é pouco inovador e previsível.
