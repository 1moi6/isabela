# Ciclo 013 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um estudante organizou a seguinte tabela, relacionando dois números x e y que seguem um mesmo padrão de formação:

| x | y |
|---|----|
| 1 | 3 |
| 2 | 12 |
| 3 | 27 |
| 4 | 48 |

Analisando os pares de valores dessa tabela, qual expressão algébrica representa corretamente, para todo x, a relação entre x e y?

## Alternativas

- (a) y = 3x²  ← correta
- (b) y = 3x
  - *erro representado:* Assume proporcionalidade direta (linear) apenas por observar que o primeiro par (1,3) satisfaz y=3x, sem verificar os demais pares nem perceber que a razão y/x não é constante.
- (c) y = 15x - 12
  - *erro representado:* Assume que a relação é uma função afim (linear) e calcula a e b usando apenas os dois pontos extremos da tabela (1,3) e (4,48), ignorando que os pontos intermediários não satisfazem essa reta.
- (d) y = x² + 2
  - *erro representado:* Ajusta a expressão apenas ao primeiro par de valores (x=1, y=3), somando uma constante ao invés de multiplicar x² por um coeficiente, sem testar a fórmula nos demais pontos da tabela.

## Gabarito

y = 3x²

## Resolução

**Passo 1 — Testar proporcionalidade direta ($y = kx$).**
Se a relação fosse do tipo $y = kx$, a razão $\dfrac{y}{x}$ deveria ser constante. Calculando:
$\dfrac{3}{1}=3,\quad \dfrac{12}{2}=6,\quad \dfrac{27}{3}=9,\quad \dfrac{48}{4}=12$

A razão **não é constante** — ela cresce, então a relação não é linear simples ($y=kx$).

**Passo 2 — Testar proporcionalidade ao quadrado ($y = a x^2$).**
Se $y = a x^2$, então $\dfrac{y}{x^2}$ deve ser constante. Calculando:
$\dfrac{3}{1^2}=3,\quad \dfrac{12}{2^2}=3,\quad \dfrac{27}{3^2}=3,\quad \dfrac{48}{4^2}=3$

A razão $\dfrac{y}{x^2}=3$ é constante para todos os pares! Isso confirma que $y$ é proporcional ao quadrado de $x$, com constante de proporcionalidade $a=3$.

**Passo 3 — Escrever a lei de formação.**
$y = 3x^2$

**Passo 4 — Verificação final** substituindo cada x da tabela:
$x=1:\ 3(1)^2=3$ ✓
$x=2:\ 3(2)^2=12$ ✓
$x=3:\ 3(3)^2=27$ ✓
$x=4:\ 3(4)^2=48$ ✓

Todos os valores conferem, confirmando que a expressão $y=3x^2$ generaliza corretamente o padrão observado, sendo uma função polinomial do 2º grau do tipo $y=ax^2$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'pontos': '[(1,3),(2,12),(3,27),(4,48)]', 'grau': '2', 'forma': 'a*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta a tabela completa, define claramente x e y, e a pergunta ('qual expressão algébrica representa... para todo x') é inequívoca. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A tarefa exige comparar hipóteses (linear vs. quadrática) e testar consistência em múltiplos pontos, compatível com 'analisar'. Contudo, por ser múltipla escolha, o estudante pode simplesmente substituir x em cada alternativa e verificar qual bate com todos os y, reduzindo parcialmente a exigência de análise sistemática para verificação pontual — ainda assim, a resolução esperada (testar razões y/x e y/x²) sustenta um nível relacional, não meramente multiestrutural.
  - alinhamento_bncc: 5/5 — Cumpre todas as exigências listadas: dados chegam via tabela, a expressão não está pronta no enunciado, pede-se a generalização algébrica, e o processo conduz exatamente ao reconhecimento de y=ax² (a=3), conforme EM13MAT502.
  - distratores: 5/5 — As três alternativas incorretas representam erros sistemáticos plausíveis: assumir proporcionalidade direta a partir de um único par (y=3x), ajustar reta pelos extremos ignorando pontos intermediários (y=15x-12), e somar constante em vez de multiplicar (y=x²+2, coincide apenas no primeiro ponto). Nenhum é absurdo ou trivialmente descartável sem cálculo.
  - originalidade: 3/5 — O formato 'tabela numérica sem contexto + descubra a lei de formação' é um padrão didático bastante recorrente em livros. Não há contextualização significativa (situação real, física, geométrica) que dê sentido aos números, o que limita o potencial de engajamento e a autenticidade da situação-problema.
