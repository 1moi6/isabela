# Ciclo 038 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Observe a tabela abaixo, que relaciona valores de uma grandeza $x$ a valores de uma grandeza $y$, obtidos a partir de um mesmo padrão:

| $x$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $y$ | 5 | 8 | 11 | 14 |

a) Analise como $y$ varia à medida que $x$ aumenta uma unidade e identifique o padrão presente na tabela.

b) Escreva a lei algébrica $y = f(x)$ que generaliza esse padrão para qualquer valor real de $x$.

c) Classifique o tipo de função obtida, justificando sua resposta a partir da lei encontrada.

## Gabarito

A relação é uma função afim dada por $f(x) = 3x + 2$, pois a variação de $y$ é constante (igual a 3) para cada acréscimo unitário de $x$.

## Resolução

**Passo 1 — Investigar o padrão de variação de $y$**

Calculando as diferenças sucessivas dos valores de $y$ correspondentes a acréscimos unitários de $x$:

$8-5=3$

$11-8=3$

$14-11=3$

A variação de $y$ é **constante e igual a 3** para cada aumento de uma unidade em $x$. Isso indica que os pontos $(x,y)$ pertencem a uma reta, ou seja, que a relação entre $x$ e $y$ pode ser descrita por uma função polinomial de 1º grau, da forma $y = ax + b$.

**Passo 2 — Determinar o coeficiente angular $a$**

Como a variação de $y$ por unidade de $x$ é constante e vale 3, temos $a = 3$ (esse valor corresponde à razão da progressão aritmética formada pelos valores de $y$).

**Passo 3 — Determinar o coeficiente linear $b$**

Usando o par $(1,5)$ na lei $y = 3x + b$:

$5 = 3(1) + b \Rightarrow b = 5 - 3 = 2$

**Passo 4 — Escrever e verificar a lei**

$f(x) = 3x + 2$

Verificando nos demais pontos:

$f(2) = 3(2)+2 = 8$ ✓

$f(3) = 3(3)+2 = 11$ ✓

$f(4) = 3(4)+2 = 14$ ✓

Todos os pares da tabela satisfazem a lei encontrada.

**Passo 5 — Classificação**

Como $f(x) = 3x + 2$ tem a forma $y = ax + b$ com $a = 3 \neq 0$, a função é uma **função polinomial de 1º grau (função afim)**, cujo gráfico é uma reta não horizontal com coeficiente angular $3$ e coeficiente linear $2$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x + 2`, parâmetros `{'pontos': '[(1,5),(2,8),(3,11),(4,14)]', 'grau': '1', 'sequencia': 'pa', 'a1': '5', 'razao': '3'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*x + 2: reproduz os 4 pontos dados; grau 1; coincide com a PA declarada.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é preciso: a tabela está bem estruturada, os três comandos (a, b, c) delimitam claramente o que é pedido em cada etapa, sem ambiguidade lexical ou estrutural. Os dados são suficientes para resolver o problema.
  - adequacao_nivel: 4/5 — Os itens a) e b) exigem decompor o padrão de variação e generalizar algebricamente, compatível com 'analisar' (SOLO relacional). O item c) exige justificar a classificação a partir da lei, reforçando a análise. Porém a segmentação em três subitens guia fortemente o raciocínio (identificar diferença constante → escrever lei → classificar), reduzindo um pouco a autonomia investigativa esperada em tarefas de 'analisar' puro — poderia ser mais aberta, exigindo que o próprio aluno decida os passos.
  - alinhamento_bncc: 5/5 — Atende integralmente às exigências da EM13MAT501: os dados chegam via tabela (não há fórmula pronta), pede-se explicitamente a generalização algébrica do padrão (item b) e a classificação como função polinomial de 1º grau com justificativa (item c), articulando investigação, representação algébrica e reconhecimento do tipo de função em um único fluxo coerente.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O padrão (tabela com progressão aritmética de razão 3, achar a lei e classificar) é um modelo muito recorrente em livros didáticos, sem contexto significativo ou aplicação real que motive o problema. O enunciado é competente, mas previsível — poderia inserir um contexto (físico, financeiro, geométrico) que dê sentido aos valores de x e y, evitando o formato genérico 'grandeza x e grandeza y'.
