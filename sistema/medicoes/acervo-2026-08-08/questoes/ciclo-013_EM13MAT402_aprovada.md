# Ciclo 013 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma equipe de engenharia de trânsito testou o desempenho de frenagem em duas pistas experimentais, registrando a distância total percorrida pelo veículo até a parada completa, d (em metros), em função da velocidade v (em km/h) no instante em que o motorista aciona o freio. Os resultados estão nas tabelas a seguir.

Pista 1 (pavimento seco, sem qualquer obstáculo antes da área de frenagem):

| v (km/h) | 0 | 10 | 20 |
|---|---|---|---|
| d (m) | 0 | 20 | 80 |

Pista 2 (pavimento molhado, com uma barreira de segurança fixa instalada antes do início da área de frenagem):

| v (km/h) | 0 | 10 | 20 |
|---|---|---|---|
| d (m) | 8 | 48 | 128 |

Sabe-se que, em cada pista, a distância d é dada por uma função polinomial do 2º grau na variável v.

a) Determine as leis $d_1(v)$ e $d_2(v)$ que descrevem, respectivamente, a Pista 1 e a Pista 2.

b) Determine as coordenadas do vértice da parábola que representa o gráfico de cada função no plano cartesiano, com eixo horizontal v e eixo vertical d.

c) Uma dessas duas relações mostra que a distância percorrida é diretamente proporcional ao quadrado da velocidade. Identifique qual delas é essa relação, justificando sua resposta a partir da posição do vértice encontrado no item (b) e da simetria do gráfico em relação ao eixo d.

d) Descreva como o gráfico de $d_2$ pode ser obtido a partir do gráfico de $d_1$ por meio de translações no plano cartesiano (indique o sentido e a quantidade de unidades deslocadas na horizontal e na vertical).

## Gabarito

a) $d_1(v)=\frac{1}{5}v^2$ e $d_2(v)=\frac{1}{5}v^2+2v+8$. b) Vértices: $(0,0)$ para $d_1$ e $(-5,3)$ para $d_2$. c) A Pista 1 ($d_1$) representa proporcionalidade direta ao quadrado, pois seu vértice está na origem e o eixo de simetria coincide com o eixo d. d) O gráfico de $d_2$ é o de $d_1$ deslocado 5 unidades para a esquerda e 3 unidades para cima.

## Resolução

**a) Determinação das leis**

Como cada função é do 2º grau, escrevemos $d(v) = av^2+bv+c$ e usamos os três pontos de cada tabela.

*Pista 1:* pontos $(0,0), (10,20), (20,80)$.

De $(0,0)$: $c_1=0$.

De $(10,20)$: $100a_1+10b_1=20 \Rightarrow 10a_1+b_1=2$.

De $(20,80)$: $400a_1+20b_1=80 \Rightarrow 20a_1+b_1=4$.

Subtraindo as duas últimas: $10a_1=2 \Rightarrow a_1=\frac{1}{5}$, e então $b_1=2-10\cdot\frac{1}{5}=0$.

Logo, $d_1(v)=\dfrac{1}{5}v^2$.

*Pista 2:* pontos $(0,8), (10,48), (20,128)$.

De $(0,8)$: $c_2=8$.

De $(10,48)$: $100a_2+10b_2+8=48 \Rightarrow 10a_2+b_2=4$.

De $(20,128)$: $400a_2+20b_2+8=128 \Rightarrow 20a_2+b_2=6$.

Subtraindo: $10a_2=2 \Rightarrow a_2=\frac{1}{5}$, e $b_2=4-10\cdot\frac{1}{5}=2$.

Logo, $d_2(v)=\dfrac{1}{5}v^2+2v+8$.

**b) Vértices**

Para $d_1(v)=\frac{1}{5}v^2$: $v_0=-\dfrac{b_1}{2a_1}=-\dfrac{0}{2/5}=0$, e $d_1(0)=0$. Vértice: $(0,0)$.

Para $d_2(v)=\frac{1}{5}v^2+2v+8$: $v_0=-\dfrac{b_2}{2a_2}=-\dfrac{2}{2/5}=-5$, e $d_2(-5)=\frac{1}{5}(25)+2(-5)+8=5-10+8=3$. Vértice: $(-5,3)$.

**c) Identificação da proporcionalidade direta ao quadrado**

A relação $d_1(v)=\frac{1}{5}v^2$ tem $b_1=c_1=0$, isto é, $\dfrac{d_1(v)}{v^2}=\dfrac{1}{5}$ é constante para todo $v\neq 0$: trata-se de uma proporcionalidade direta ao quadrado. Geometricamente, isso corresponde a uma parábola cujo vértice coincide exatamente com a origem $(0,0)$ do plano cartesiano e cujo eixo de simetria é o próprio eixo d (reta $v=0$).

Já $d_2$ tem vértice em $(-5,3)$, fora da origem, e eixo de simetria $v=-5$, diferente do eixo d. Além disso, $\dfrac{d_2(10)}{10^2}=\dfrac{48}{100}=0{,}48 \neq \dfrac{1}{5}$, confirmando que a razão não é constante. Portanto, **a Pista 1** é a que representa d diretamente proporcional ao quadrado de v.

**d) Translação do gráfico**

Completando o quadrado em $d_2$: 
$d_2(v)=\frac{1}{5}v^2+2v+8=\frac{1}{5}(v^2+10v)+8=\frac{1}{5}\left[(v+5)^2-25\right]+8=\frac{1}{5}(v+5)^2+3$.

Como $d_1(v+5)=\frac{1}{5}(v+5)^2$, temos $d_2(v)=d_1(v+5)+3$.

Isso significa que o gráfico de $d_2$ é obtido a partir do gráfico de $d_1$ por uma translação horizontal de 5 unidades para a esquerda seguida de uma translação vertical de 3 unidades para cima — coerente com a mudança do vértice de $(0,0)$ para $(-5,3)$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `Rational(1,5)*v**2`, parâmetros `{'pontos': '[(0,0),(10,20),(20,80)]', 'grau': '2', 'forma': 'a*v**2'}`
- `propriedade` — expressão `-`, esperado `Rational(1,5)*v**2 + 2*v + 8`, parâmetros `{'pontos': '[(0,8),(10,48),(20,128)]', 'grau': '2'}`
- `funcao` — expressão `Rational(1,5)*v**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `Rational(1,5)*v**2 + 2*v + 8`, esperado `[-5, 3]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para v**2/5: reproduz os 3 pontos dados; grau 2; forma a*v**2. | (2) aprovado: Propriedades confirmadas para v**2/5 + 2*v + 8: reproduz os 3 pontos dados; grau 2. | (3) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (4) aprovado: Gabarito confirmado (vértice calculado (-5, 3)).
  - propriedade=aprovado
  - propriedade=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos em tabelas, unidades explícitas e comandos claros em cada item. Não há ambiguidade sobre o que é pedido em (a)-(d).
  - adequacao_nivel: 4/5 — Os itens (a) e (b) são de 'aplicar' (resolver sistema, usar fórmula do vértice), coerentes com resposta multiestrutural. O item (c) já exige comparação e justificativa (mais próximo de 'analisar'/relacional) e o (d) exige transferência de representação (aplicar transformação). A progressão é coerente e adequada ao Ensino Médio, ainda que ultrapasse levemente o nível 'aplicar' declarado.
  - alinhamento_bncc: 5/5 — A questão articula genuinamente álgebra e geometria: o vértice e a simetria (representação geométrica) são usados para justificar a distinção de proporcionalidade direta ao quadrado (exigência central da habilidade), e o item (d) reforça o trânsito entre as duas representações via translação. Não se limita a pedir vértice/raízes isoladamente.
  - distratores: 5/5 — Não se aplica — questão discursiva.
  - originalidade: 4/5 — O contexto de frenagem é um clássico de física/matemática, mas a comparação entre duas pistas, a exigência de justificativa via vértice/simetria e a translação entre gráficos evitam o efeito Topaze e dão originalidade suficiente à tarefa.
