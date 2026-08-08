# Ciclo 073 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** criar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Observe a tabela abaixo, que relaciona valores de $x$ e $y$:

| $x$ | $-3$ | $-1$ | $2$ | $4$ |
|---|---|---|---|---|
| $y$ | $27$ | $3$ | $12$ | $48$ |

Analisando os pares de valores, investigue como $y$ varia em função de $x$ e determine a expressão algébrica que generaliza essa relação para qualquer valor de $x$. Em seguida, classifique o tipo de função polinomial obtida, justificando sua resposta.

## Gabarito

y = 3x², uma função quadrática do tipo y = ax² (com a = 3)

## Resolução

**Passo 1 — Observar o espaçamento dos valores de $x$.**

Os valores de $x$ dados são $-3, -1, 2, 4$. As diferenças entre valores consecutivos de $x$ são $2, 3, 2$ — ou seja, **não são igualmente espaçados**. Isso significa que o método usual de calcular diferenças sucessivas de $y$ (útil quando $x$ forma uma PA) não pode ser aplicado diretamente. É preciso investigar a relação de outra forma.

**Passo 2 — Testar proporcionalidade direta ($y = bx$).**

Calculando a razão $\dfrac{y}{x}$ para cada par:

$$\frac{27}{-3}=-9,\quad \frac{3}{-1}=-3,\quad \frac{12}{2}=6,\quad \frac{48}{4}=12$$

As razões não são iguais, logo $y$ **não** é diretamente proporcional a $x$ — a relação não é do tipo $y=bx$.

**Passo 3 — Testar proporcionalidade ao quadrado de $x$ ($y = ax^2$).**

Calculando $x^2$ para cada valor: $9, 1, 4, 16$.

Calculando a razão $\dfrac{y}{x^2}$:

$$\frac{27}{9}=3,\quad \frac{3}{1}=3,\quad \frac{12}{4}=3,\quad \frac{48}{16}=3$$

Todas as razões são iguais a $3$! Isso indica que $y$ é proporcional ao quadrado de $x$, com constante de proporcionalidade $a=3$.

**Passo 4 — Escrever e verificar a generalização.**

A lei que expressa o padrão é:

$$y = 3x^2$$

Verificando com todos os pares da tabela:
- $3\cdot(-3)^2 = 3\cdot 9 = 27$ ✓
- $3\cdot(-1)^2 = 3\cdot 1 = 3$ ✓
- $3\cdot(2)^2 = 3\cdot 4 = 12$ ✓
- $3\cdot(4)^2 = 3\cdot 16 = 48$ ✓

**Passo 5 — Classificação.**

Como $y$ depende de $x$ através de $y=ax^2$ (com $a=3\neq 0$), trata-se de uma **função polinomial do 2º grau (função quadrática)** da forma particular $y=ax^2$, cujo gráfico é uma parábola com vértice na origem $(0,0)$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'pontos': '[(-3,27),(-1,3),(2,12),(4,48)]', 'forma': 'a*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado apresenta claramente os dados (tabela) e as duas tarefas pedidas (encontrar a expressão algébrica e classificar a função). Não há ambiguidade lexical grave, mas a instrução 'classifique o tipo de função polinomial obtida' poderia ser mais específica quanto ao nível de detalhe esperado na justificativa (ex.: mencionar o grau e a forma particular y=ax²), evitando que alunos deem respostas incompletas.
  - adequacao_nivel: 4/5 — A tarefa exige que o aluno teste hipóteses (proporcionalidade direta, depois quadrática) e formule uma generalização algébrica, o que corresponde ao nível 'criar' de Bloom e a uma resposta de estrutura relacional/extended abstract na taxonomia SOLO. O uso de valores de x não igualmente espaçados impede uma solução puramente mecânica (diferenças finitas), reforçando a exigência de raciocínio investigativo. Poderia exigir explicitamente a representação gráfica para elevar ainda mais a complexidade cognitiva.
  - alinhamento_bncc: 4/5 — Cobre as exigências centrais da especificação: dados em tabela, pedido de generalização algébrica e reconhecimento do padrão y=ax². Falta, porém, o componente 'representar no plano cartesiano' presente no texto original da habilidade EM13MAT502, que não é solicitado nem sugerido no enunciado. Isso não compromete o atendimento às bullets específicas da especificação, mas deixa uma lacuna frente à habilidade plena.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — Foge do padrão clássico de tabelas com x em progressão aritmética, forçando o aluno a investigar por tentativa (proporcionalidade direta vs. quadrática) em vez de aplicar uma fórmula memorizada. O enunciado não entrega pistas diretas sobre o expoente ou a constante, evitando o efeito Topaze. Poderia ganhar em contextualização (situação real) para reforçar significância, mas atende bem ao critério teórico.
