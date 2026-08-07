# Ciclo 008 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento cobra a tarifa mensal de água residencial segundo a seguinte tabela, válida para consumos de 0 a 30 m³ por mês:

- Se o consumo for de até 10 m³ (inclusive), o usuário paga uma tarifa mínima fixa de R$ 30,00.
- Se o consumo for maior que 10 m³ e até 20 m³, paga-se R$ 30,00 mais R$ 4,00 por cada m³ que exceder 10 m³.
- Se o consumo for maior que 20 m³ e até 30 m³, paga-se R$ 70,00 mais R$ 6,00 por cada m³ que exceder 20 m³.

Seja $x$ o consumo mensal (em m³) e $f(x)$ o valor pago (em reais).

a) Escreva a lei algébrica de $f(x)$, especificando o domínio de validade de cada sentença.

b) Calcule quanto pagarão dois usuários que consumiram, respectivamente, 12 m³ e 27 m³ no mês.

c) Determine a imagem de $f$ considerando todo o intervalo de consumo de 0 a 30 m³.

d) Indique em que intervalo do domínio o gráfico de $f$ é uma reta horizontal e em que intervalo ele é estritamente crescente, justificando com base nas taxas de variação de cada sentença.

## Gabarito

f(x) = 30 se 0≤x≤10; 30+4(x-10) se 10<x≤20; 70+6(x-20) se 20<x≤30. f(12)=R$38,00; f(27)=R$112,00. Imagem = [30,130]. Constante em [0,10]; estritamente crescente em (10,30], com inclinação maior a partir de x=20.

## Resolução

**a) Lei algébrica e domínios de validade**

Cada faixa de consumo corresponde a uma sentença, e os domínios de validade são delimitados pelos limites de consumo dados:

$$f(x)=\begin{cases} 30, & 0\le x\le 10 \\ 30+4(x-10), & 10< x\le 20 \\ 70+6(x-20), & 20< x\le 30 \end{cases}$$

O domínio de validade de toda a função é $[0,30]$, dividido nos três subintervalos indicados.

**b) Valores pagos**

Para $x=12$, como $10<12\le 20$, usa-se a segunda sentença:
$$f(12)=30+4(12-10)=30+8=38$$
O usuário paga R$ 38,00.

Para $x=27$, como $20<27\le 30$, usa-se a terceira sentença:
$$f(27)=70+6(27-20)=70+42=112$$
O usuário paga R$ 112,00.

Observe que é necessário identificar corretamente em qual sentença cada valor de $x$ se enquadra antes de calcular.

**c) Imagem de $f$ em $[0,30]$**

Como cada trecho é constante ou crescente, o menor valor de $f$ ocorre em $x=0$: $f(0)=30$. O maior valor ocorre em $x=30$: $f(30)=70+6(10)=130$. Como a função é contínua nas junções ($f(10)=30$, $f(20)=70$) e nunca decresce, todos os valores entre 30 e 130 são atingidos. Logo:
$$\mathrm{Im}(f)=[30,130]$$

**d) Comportamento gráfico**

- No intervalo $[0,10]$, $f(x)=30$ é constante (taxa de variação igual a 0): o gráfico é um segmento de reta horizontal.
- No intervalo $(10,20]$, a taxa de variação é $4$ reais por m³ (coeficiente positivo), logo $f$ é estritamente crescente.
- No intervalo $(20,30]$, a taxa de variação é $6$ reais por m³ (coeficiente positivo, e maior que na faixa anterior), logo $f$ continua estritamente crescente, com inclinação ainda maior.

Portanto, o gráfico é horizontal em $[0,10]$ e estritamente crescente (com aumento de inclinação) em $(10,30]$.

## Formalização verificável

- `funcao` — expressão `Piecewise((30, (x>=0) & (x<=10)), (30+4*(x-10), (x>10) & (x<=20)), (70+6*(x-20), (x>20) & (x<=30)))`, esperado `38`, parâmetros `{'consulta': 'valor', 'ponto': '12'}`
- `funcao` — expressão `Piecewise((30, (x>=0) & (x<=10)), (30+4*(x-10), (x>10) & (x<=20)), (70+6*(x-20), (x>20) & (x<=30)))`, esperado `112`, parâmetros `{'consulta': 'valor', 'ponto': '27'}`
- `funcao` — expressão `Piecewise((30, (x>=0) & (x<=10)), (30+4*(x-10), (x>10) & (x<=20)), (70+6*(x-20), (x>20) & (x<=30)))`, esperado `Interval(0,30)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((30, (x>=0) & (x<=10)), (30+4*(x-10), (x>10) & (x<=20)), (70+6*(x-20), (x>20) & (x<=30)))`, esperado `Interval(30,130)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `Piecewise((30, (x>=0) & (x<=10)), (30+4*(x-10), (x>10) & (x<=20)), (70+6*(x-20), (x>20) & (x<=30)))`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 2 de 5 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (f(12) = 38). | (2) aprovado: Gabarito confirmado (f(27) = 112). | (3) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((30, (x >= 0) & (x <= 10)), (4*x - 10, (x <= 20) & (x > 10)), (6*x - 50, (x <= 30) & (x > 20))). Conferir manualmente. | (4) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((30, (x >= 0) & (x <= 10)), (4*x - 10, (x <= 20) & (x > 10)), (6*x - 50, (x <= 30) & (x > 20))). Conferir manualmente. | (5) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((30, (x >= 0) & (x <= 10)), (4*x - 10, (x <= 20) & (x > 10)), (6*x - 50, (x <= 30) & (x > 20))). Conferir manualmente.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=nao_verificavel
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define x e f(x) com precisão, delimita as faixas de consumo sem sobreposição ou lacuna (limites 'até 10 inclusive', '>10 e ≤20', '>20 e ≤30'), e cada item (a-d) pede algo específico e verificável. Não há ambiguidade lexical nem dados faltantes.
  - adequacao_nivel: 3/5 — O nível declarado é 'entender', mas a questão como um todo exige processos mais elevados: o item (a) é compreensão/tradução de representação, o item (b) é aplicação direta, e os itens (c) e (d) exigem análise (justificar crescimento com base em taxas de variação, argumentar continuidade para obter a imagem). A estrutura de resposta é relacional/estendida (SOLO), coerente com a complexidade real do problema, mas isso não corresponde ao rótulo único 'entender' informado na especificação — há um descompasso entre o nível cognitivo declarado e o efetivamente mobilizado, que é superior.
  - alinhamento_bncc: 5/5 — A questão atende integralmente às exigências: função com três sentenças em contexto real (tarifa de água), articuladas num único problema (não justapostas como itens isolados, pois usam a mesma lei em todos os itens); exige explicitar domínios de validade (a), determinar a imagem (c) e identificar crescimento/constância com justificativa via taxa de variação (d). O item (b), que avalia em pontos específicos, não seria suficiente isoladamente, mas está complementado pelos demais itens que efetivamente mobilizam a mudança de sentença e a análise global da função, cumprindo a habilidade EM13MAT405.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — O contexto de tarifa de água por faixas de consumo é um clássico recorrente em livros didáticos (análogo a 'conta de luz' e 'Imposto de Renda' citados na própria habilidade), o que reduz a originalidade contextual. Por outro lado, a exigência de justificar o crescimento via taxas de variação e determinar a imagem evita o efeito Topaze simples de 'substitua e calcule', adicionando algum valor pedagógico ao enunciado tradicional.
