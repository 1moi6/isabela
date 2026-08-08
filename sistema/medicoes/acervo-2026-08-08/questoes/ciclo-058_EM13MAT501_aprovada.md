# Ciclo 058 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** criar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A tabela abaixo relaciona valores de $x$ e os correspondentes valores de $y$, obtidos a partir de uma mesma regra de formação (os valores de $x$ não variam em intervalos iguais):

| $x$ | $-3$ | $1$ | $4$ | $8$ |
|---|---|---|---|---|
| $y$ | $14$ | $2$ | $-7$ | $-19$ |

Um estudante, analisando os pares ordenados $(x,y)$ da tabela, conjectura que essa relação pode ser representada por uma função polinomial do 1º grau. Assinale a alternativa que apresenta a lei de formação $f(x)$ que generaliza corretamente o padrão observado na tabela.

## Alternativas

- (a) $f(x) = -3x + 5$  ← correta
- (b) $f(x) = -12x + 14$
  - *erro representado:* Calculou a inclinação usando apenas a diferença bruta de y entre os dois primeiros pontos da tabela (Δy = -12), sem dividir pela correspondente diferença de x (Δx = 4), tratando os valores de x como se fossem consecutivos de 1 em 1.
- (c) $f(x) = 3x - 1$
  - *erro representado:* Calculou corretamente o valor absoluto da taxa de variação, mas inverteu o sinal do coeficiente angular (usou m = 3 em vez de m = -3), gerando um coeficiente linear incorreto ao ajustar com um dos pontos.
- (d) $f(x) = -11x + 13$
  - *erro representado:* Tomou o coeficiente angular como a média aritmética simples das diferenças de y entre pares consecutivos (-12, -9, -12), sem ponderar cada diferença pelo respectivo intervalo de x, obtendo m = -11 em vez de m = -3.

## Gabarito

f(x) = -3x + 5

## Resolução

**Passo 1 — Verificar se a razão entre as variações é constante (condição para função afim).**

Como os valores de $x$ não estão igualmente espaçados, é preciso calcular a razão $\dfrac{\Delta y}{\Delta x}$ entre pares consecutivos da tabela, e não apenas $\Delta y$.

Entre $x=-3$ e $x=1$: $\Delta x = 1-(-3)=4$, $\Delta y = 2-14=-12$, logo $\dfrac{\Delta y}{\Delta x}=\dfrac{-12}{4}=-3$.

Entre $x=1$ e $x=4$: $\Delta x = 4-1=3$, $\Delta y = -7-2=-9$, logo $\dfrac{\Delta y}{\Delta x}=\dfrac{-9}{3}=-3$.

Entre $x=4$ e $x=8$: $\Delta x = 8-4=4$, $\Delta y = -19-(-7)=-12$, logo $\dfrac{\Delta y}{\Delta x}=\dfrac{-12}{4}=-3$.

**Passo 2 — Concluir o tipo de função.**

A razão $\dfrac{\Delta y}{\Delta x}$ é constante e igual a $-3$ para todos os pares consecutivos, mesmo com intervalos diferentes de $x$. Isso caracteriza uma **função polinomial do 1º grau (afim)**, da forma $f(x)=mx+b$, com $m=-3$.

**Passo 3 — Determinar o coeficiente linear $b$.**

Usando o ponto $(1,2)$: $2 = -3(1)+b \Rightarrow b = 2+3 = 5$.

Logo, $f(x) = -3x+5$.

**Passo 4 — Verificar com os demais pontos.**

$f(-3) = -3(-3)+5 = 9+5 = 14$ ✓

$f(4) = -3(4)+5 = -12+5 = -7$ ✓

$f(8) = -3(8)+5 = -24+5 = -19$ ✓

Todos os pares confirmam a lei $f(x) = -3x+5$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `-3*x + 5`, parâmetros `{'pontos': '[(-3,14),(1,2),(4,-7),(8,-19)]', 'grau': '1'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 5 - 3*x: reproduz os 4 pontos dados; grau 1.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é preciso: apresenta tabela com x não equiespaçado, deixa claro o que é dado (pares x,y) e o que se pede (a lei de formação). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — O enunciado já informa que 'essa relação pode ser representada por uma função polinomial do 1º grau', o que retira do estudante parte do trabalho de reconhecer o tipo de função — tarefa central da habilidade. Com essa pista, o processo cognitivo real fica mais próximo de 'aplicar/analisar' (calcular m via Δy/Δx e depois b) do que de 'criar' uma generalização a partir de dados brutos, embora o cálculo com intervalos desiguais exija atenção além do trivial.
  - alinhamento_bncc: 3/5 — Cumpre os requisitos formais (dados em tabela, expressão não vem pronta, pede-se a generalização algébrica), mas falha parcialmente no ponto 'levar ao reconhecimento de que a relação é de função polinomial de 1º grau', pois esse reconhecimento é entregue no próprio enunciado como conjectura do estudante fictício, em vez de ser produzido pelo próprio respondente. Isso esvazia um componente central da habilidade EM13MAT501.
  - distratores: 5/5 — Os três distratores mapeiam erros sistemáticos plausíveis e distintos: ignorar Δx (tratar intervalos como unitários), inverter o sinal do coeficiente angular, e usar média aritmética simples das diferenças de y sem ponderar pelos intervalos de x. Nenhum é absurdo ou trivialmente eliminável, exigindo do estudante verificação cuidadosa.
  - originalidade: 3/5 — O formato (tabela com x não igualmente espaçado para função afim) é um exercício clássico de material didático, sem contexto significativo ou aplicação real. A menção à 'conjectura do estudante' é um verniz que não modifica a estrutura tradicional do problema, e funciona como pista (efeito Topaze) que já indica o tipo de função a ser confirmado.
