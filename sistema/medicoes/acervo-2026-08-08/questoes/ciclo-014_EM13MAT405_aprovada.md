# Ciclo 014 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento cobra a conta de água residencial de acordo com faixas de consumo mensal $m$, medido em metros cúbicos (m³), sendo o serviço válido para consumos de até $50\,m^3$. As regras de cobrança, em reais, são as seguintes:

| Faixa de consumo | Regra de cobrança |
|---|---|
| $0 \le m \le 10$ | Taxa fixa de manutenção de R\$5,00 mais R\$1,50 por m³ consumido |
| $10 < m \le 30$ | R\$20,00 fixos (referentes aos primeiros 10 m³) mais R\$2,00 por m³ que exceder 10 m³ |
| $30 < m \le 50$ | R\$60,00 fixos (referentes aos primeiros 30 m³) mais R\$4,00 por m³ que exceder 30 m³ |

Seja $C(m)$ o valor da conta, em reais, para um consumo de $m$ metros cúbicos.

a) Escreva a lei algébrica de $C(m)$, definida por partes, especificando o domínio de validade de cada sentença.

b) Determine a imagem da função $C$ considerando todo o intervalo de consumo válido, de $0$ a $50\,m^3$.

c) Em certo mês, uma família pagou uma conta de R\$74,00. Determine o consumo desse mês, indicando claramente por que sentença da função esse valor deve ser calculado.

d) A conta de água é uma função crescente, decrescente ou constante no intervalo de consumo considerado? Justifique sua resposta levando em conta as três sentenças da função.

## Gabarito

a) $C(m) = 1{,}5m+5$ para $0\le m\le10$; $C(m)=20+2(m-10)$ para $10<m\le30$; $C(m)=60+4(m-30)$ para $30<m\le50$. b) Imagem $=[5,140]$. c) $m=33{,}5\,m^3$ (calculado na terceira sentença, pois $74>60$). d) A função é crescente em todo o domínio $[0,50]$.

## Resolução

**a) Lei algébrica por partes**

Traduzindo cada faixa da tabela:

$$C(m) = \begin{cases} 1{,}5m + 5, & 0 \le m \le 10 \\ 20 + 2(m-10), & 10 < m \le 30 \\ 60 + 4(m-30), & 30 < m \le 50 \end{cases}$$

Verificando a coerência nas transições: em $m=10$, a primeira sentença dá $1{,}5\times10+5=20$, que coincide com o valor inicial da segunda sentença. Em $m=30$, a segunda sentença dá $20+2\times20=60$, que coincide com o valor inicial da terceira. A função é, portanto, contínua.

**b) Imagem da função**

Cada sentença tem coeficiente angular positivo ($1{,}5$; $2$; $4$), logo $C$ é crescente em cada um dos três intervalos. Como os valores se encaixam continuamente nas transições, $C$ é crescente em todo o domínio $[0,50]$. Assim, o valor mínimo ocorre em $m=0$:
$$C(0) = 1{,}5(0)+5 = 5$$
e o valor máximo ocorre em $m=50$:
$$C(50) = 60+4(50-30) = 60+80 = 140$$

Como a função é contínua e crescente, sua imagem é todo o intervalo entre esses extremos:
$$\text{Im}(C) = [5, 140]$$

**c) Consumo correspondente a $C(m) = 74$**

Precisamos identificar em qual sentença esse valor ocorre. Na primeira sentença, $C(m)$ varia de $5$ a $20$ (pois $m \in [0,10]$); na segunda, de $20$ a $60$ (pois $m \in (10,30]$). Como $74 > 60$, o valor $74$ só pode pertencer à imagem da terceira sentença, válida para $30 < m \le 50$.

Resolvendo nessa sentença:
$$60 + 4(m-30) = 74$$
$$4(m-30) = 14$$
$$m - 30 = 3{,}5$$
$$m = 33{,}5$$

Como $33{,}5 \in (30, 50]$, a solução é válida: o consumo foi de $33{,}5\,m^3$.

**d) Crescimento**

Como cada uma das três sentenças é estritamente crescente (coeficientes $1{,}5$, $2$ e $4$, todos positivos) e os valores coincidem exatamente nos pontos de transição $m=10$ e $m=30$, a função $C(m)$ é **crescente** em todo o intervalo $[0,50]$: quanto maior o consumo, maior a conta. Note, porém, que a *taxa* de aumento por metro cúbico cresce a cada faixa ($1{,}5 \to 2 \to 4$ reais por m³), caracterizando uma tarifa progressiva.

## Formalização verificável

- `funcao` — expressão `Piecewise((Rational(3,2)*m + 5, (m>=0)&(m<=10)), (20 + 2*(m-10), (m>10)&(m<=30)), (60 + 4*(m-30), (m>30)&(m<=50)))`, esperado `Interval(0, 50)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((Rational(3,2)*m + 5, (m>=0)&(m<=10)), (20 + 2*(m-10), (m>10)&(m<=30)), (60 + 4*(m-30), (m>30)&(m<=50)))`, esperado `Interval(5, 140)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, 50)'}`
- `funcao` — expressão `Piecewise((Rational(3,2)*m + 5, (m>=0)&(m<=10)), (20 + 2*(m-10), (m>10)&(m<=30)), (60 + 4*(m-30), (m>30)&(m<=50)))`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(Piecewise((Rational(3,2)*m + 5, (m>=0)&(m<=10)), (20 + 2*(m-10), (m>10)&(m<=30)), (60 + 4*(m-30), (m>30)&(m<=50))), 74)`, esperado `[Rational(67,2)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 1 de 4 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((3*m/2 + 5, (m >= 0) & (m <= 10)), (2*m, (m <= 30) & (m > 10)), (4*m - 60, (m <= 50) & (m > 30))). Conferir manualmente. | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((3*m/2 + 5, (m >= 0) & (m <= 10)), (2*m, (m <= 30) & (m > 10)), (4*m - 60, (m <= 50) & (m > 30))). Conferir manualmente. | (3) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((3*m/2 + 5, (m >= 0) & (m <= 10)), (2*m, (m <= 30) & (m > 10)), (4*m - 60, (m <= 50) & (m > 30))). Conferir manualmente. | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=nao_verificavel
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, tabela explícita com faixas e regras de cobrança, domínio de cada sentença bem delimitado. Não há ambiguidade sobre o que é dado (regras de cobrança) nem sobre o que é pedido em cada item (lei algébrica, imagem, consumo específico, crescimento).
  - adequacao_nivel: 4/5 — A maioria das tarefas (traduzir tabela em lei algébrica, identificar imagem, converter valor em consumo) é compatível com 'entender/aplicar'. Contudo, o item (d) exige justificativa analítica comparando taxas de variação entre as três sentenças, o que se aproxima mais de 'analisar' na taxonomia de Bloom e de um nível relacional na SOLO, ligeiramente acima do nível declarado. O conteúdo é plenamente adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — Atende a todas as exigências: função com três sentenças em contexto real (conta de água), exige conversão da tabela para lei algébrica, determinação de domínio, imagem e comportamento de crescimento, e o item (c) obriga o aluno a identificar a sentença correta antes de resolver a equação, mobilizando efetivamente a mudança de sentença — não é uma avaliação pontual da função.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — O contexto de tarifa progressiva de água é um cenário já comum em livros didáticos, mas a articulação entre os quatro subitens (lei, imagem, resolução inversa com justificativa da sentença, e análise comparativa das taxas) confere originalidade estrutural e evita o efeito Topaze, pois não há pistas óbvias sobre qual sentença usar em (c) — o aluno precisa deduzir isso a partir da imagem parcial de cada faixa.
