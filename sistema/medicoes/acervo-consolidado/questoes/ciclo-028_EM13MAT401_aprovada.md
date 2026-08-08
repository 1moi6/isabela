# Ciclo 028 — EM13MAT401

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Duas empresas de transporte por aplicativo, TáxiJá e MoveCar, calculam o valor da corrida em função da distância percorrida, em quilômetros.

- A TáxiJá cobra R$ 2,50 por quilômetro rodado, sem qualquer taxa adicional.
- A MoveCar cobra uma taxa fixa de R$ 4,00 pela chamada do carro, mais R$ 1,50 por quilômetro rodado.

Considere $x$ a distância percorrida, em quilômetros ($x \geq 0$), e $y$ o valor pago, em reais.

a) Escreva a lei de formação que representa o valor cobrado por cada empresa, em função de $x$.

b) Represente, num mesmo plano cartesiano, os gráficos das duas funções, indicando claramente o ponto em que cada reta corta o eixo $y$.

c) Uma dessas funções representa uma grandeza diretamente proporcional à distância percorrida, e a outra não. Identifique qual delas é a proporcional e explique, a partir do gráfico (ou da lei algébrica), como reconhecer esse comportamento.

d) Determine algebricamente a distância a partir da qual a corrida pela MoveCar passa a ser mais barata que pela TáxiJá, e indique as coordenadas do ponto em que os dois gráficos se cruzam.

## Gabarito

a) $f_T(x)=2{,}5x$ e $f_M(x)=1{,}5x+4$. b) Retas crescentes: $f_T$ passa pela origem $(0,0)$; $f_M$ corta o eixo $y$ em $(0,4)$. c) $f_T$ é diretamente proporcional (passa pela origem, $b=0$); $f_M$ não é proporcional ($b=4\neq 0$). d) A partir de $x=4$ km a MoveCar fica mais barata; o ponto de intersecção das retas é $(4,10)$.

## Resolução

**a) Leis de formação**

TáxiJá: valor proporcional à distância, sem taxa fixa:
$$f_T(x) = 2{,}5x$$

MoveCar: taxa fixa de R\$4,00 mais R\$1,50 por km:
$$f_M(x) = 1{,}5x + 4$$

**b) Representação gráfica**

Ambas são retas crescentes (coeficientes angulares positivos: $2{,}5$ e $1{,}5$).

- $f_T$ passa pela origem $(0,0)$, pois $f_T(0)=0$.
- $f_M$ corta o eixo $y$ no ponto $(0,4)$, pois $f_M(0)=4$.

Como $f_T$ tem inclinação maior, sua reta "sobe" mais rápido do que a de $f_M$, embora comece mais abaixo.

**c) Identificando o caso proporcional**

Uma função é diretamente proporcional quando tem a forma $y=ax$, ou seja, quando seu gráfico é uma reta que passa pela origem $(0,0)$.

- $f_T(x)=2{,}5x$ tem $b=0$: é diretamente proporcional à distância.
- $f_M(x)=1{,}5x+4$ tem $b=4 \neq 0$: sua reta não passa pela origem (corta o eixo $y$ em $4$), logo é apenas afim, não proporcional — mesmo que $x=0$, ainda se paga a taxa fixa de R\$4,00.

**d) Comparando os valores cobrados**

Igualando as duas expressões para achar o ponto de intersecção das retas:
$$2{,}5x = 1{,}5x + 4$$
$$2{,}5x - 1{,}5x = 4$$
$$x = 4$$

Substituindo em qualquer uma das leis:
$$f_T(4) = 2{,}5 \cdot 4 = 10$$

Logo, as retas se cruzam no ponto $(4, 10)$: para 4 km, ambas cobram R\$10,00.

Para $x>4$ (por exemplo, $x=5$): $f_T(5)=12{,}5$ e $f_M(5)=11{,}5$, ou seja, $f_M(x) < f_T(x)$.

Como o coeficiente angular de $f_T$ é maior, a partir de $x=4$ km a MoveCar torna-se mais barata que a TáxiJá.

## Formalização verificável

- `equacao` — expressão `Eq(Rational(5,2)*x, Rational(3,2)*x + 4)`, esperado `[4]`
- `funcao` — expressão `Rational(5,2)*x`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `Rational(3,2)*x + 4`, esperado `4`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `Rational(5,2)*x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `Rational(3,2)*x + 4`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (zeros da função: [0]). | (3) aprovado: Gabarito confirmado (f(0) = 4). | (4) aprovado: Gabarito confirmado (crescente em Reals). | (5) aprovado: Gabarito confirmado (crescente em Reals).
  - equacao=aprovado
  - funcao/zeros=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (taxas, coeficientes) e comandos claros em cada item (a, b, c, d). Não há ambiguidade sobre o que é pedido em cada etapa.
  - adequacao_nivel: 4/5 — O nível 'aplicar' é majoritariamente respeitado: os itens a) e d) são aplicação direta de modelagem e resolução de equação. O item c) exige uma justificativa conceitual (por que uma é proporcional e outra não), o que se aproxima de 'analisar/compreender', mas isso é coerente e até enriquece a resposta sem descaracterizar o nível declarado. Estruturalmente, a resposta esperada é multiestrutural evoluindo para relacional (o aluno conecta lei algébrica, gráfico e conceito de proporcionalidade), compatível com o Bloom declarado. Conteúdo plenamente adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão atende integralmente às exigências da habilidade: exige trânsito entre forma algébrica (item a) e representação geométrica (item b, com identificação dos interceptos), e explicitamente pede a distinção entre o caso proporcional e o caso afim (item c), fundamentando essa distinção tanto algebricamente quanto graficamente. O item d) não é mero cálculo de raiz isolado — está articulado ao contexto de comparação entre as duas retas e reforça a leitura geométrica (ponto de intersecção). Os itens não são justapostos: todos dialogam com o mesmo par de funções e constroem uma compreensão integrada.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de aplicativos de transporte é relevante e atual, mas a estrutura (comparar duas tarifas com taxa fixa e taxa variável) é um clássico recorrente em livros didáticos sob nova roupagem. O item c) tem viés de 'efeito Topaze' leve, pois praticamente entrega a definição de proporcionalidade (y=ax, b=0) dentro do próprio enunciado da resolução esperada, reduzindo o desafio de o aluno construir esse raciocínio por si mesmo. Poderia explorar uma situação menos convencional ou pedir que o aluno formule a definição sem fornecer tantas pistas.
