# Ciclo 065 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um oceanógrafo registra a altura da maré (em metros) em um pequeno porto ao longo de um dia. Ele observa que a maré varia de forma periódica e simétrica em torno de um nível médio, atingindo seu valor máximo de 1,8 m exatamente à meia-noite ($t=0$, com $t$ em horas) e seu valor mínimo de 0,2 m exatamente às 6h da manhã. Esse padrão se repete a cada 12 horas.

a) Modele a altura da maré, em metros, por uma função do tipo $h(t) = A\cos(Bt) + D$, com $t$ em horas contado a partir da meia-noite. Determine explicitamente os valores de $A$, $B$ e $D$, justificando cada um a partir dos dados do fenômeno (amplitude, período e deslocamento vertical do gráfico em relação ao eixo $t$).

b) Determine todos os horários dentro das primeiras 12 horas do dia (isto é, para $0 \le t < 12$) em que a maré atinge exatamente 1,4 m de altura. Para cada horário encontrado, indique se a maré está subindo ou descendo naquele instante, justificando sua resposta apenas a partir do comportamento gráfico da função cosseno (sem usar derivadas).

## Gabarito

h(t) = 0,8·cos(πt/6) + 1,0 (A=0,8 m; B=π/6 rad/h; D=1,0 m). A maré atinge 1,4 m às 2h (descendo) e às 10h (subindo).

## Resolução

**a) Construção do modelo**

O valor máximo da maré é $1{,}8$ m e o mínimo é $0{,}2$ m. Como $h(t)=A\cos(Bt)+D$ oscila entre $D-A$ e $D+A$:

$$D = \frac{1{,}8+0{,}2}{2} = 1{,}0 \qquad A = \frac{1{,}8-0{,}2}{2} = 0{,}8$$

O fenômeno se repete a cada 12 horas, logo o período é $T=12$. Como $T=\dfrac{2\pi}{B}$:

$$B = \frac{2\pi}{12} = \frac{\pi}{6}$$

Como a maré atinge seu **máximo** exatamente em $t=0$, e $\cos(0)=1$ é o valor máximo do cosseno, a escolha de cosseno (sem deslocamento horizontal) é coerente com o fenômeno. Assim:

$$h(t) = 0{,}8\cos\!\left(\frac{\pi t}{6}\right) + 1{,}0$$

Verificação: $h(0)=0{,}8(1)+1=1{,}8$ (máximo, ok) e $h(6)=0{,}8\cos(\pi)+1=0{,}8(-1)+1=0{,}2$ (mínimo, ok).

**b) Horários em que $h(t)=1{,}4$**

$$0{,}8\cos\!\left(\frac{\pi t}{6}\right)+1 = 1{,}4 \;\Rightarrow\; \cos\!\left(\frac{\pi t}{6}\right) = 0{,}5$$

As soluções gerais de $\cos\theta = 0{,}5$ são $\theta = \dfrac{\pi}{3}+2k\pi$ ou $\theta = -\dfrac{\pi}{3}+2k\pi$ (equivalente a $\dfrac{5\pi}{3}+2k\pi$).

Fazendo $\theta = \dfrac{\pi t}{6}$, temos $t = \dfrac{6\theta}{\pi}$:

- Para $\theta=\dfrac{\pi}{3}$: $t = 6\cdot\dfrac{1}{3} = 2$
- Para $\theta=\dfrac{5\pi}{3}$: $t = 6\cdot\dfrac{5}{3} = 10$

Dentro de $0\le t<12$, as soluções são $t=2$ e $t=10$.

**Análise de crescimento/decrescimento**

Como $h(0)=1{,}8$ é máximo e $h(6)=0{,}2$ é mínimo, no intervalo $(0,6)$ a função cosseno está descendo de seu valor máximo ao mínimo — ou seja, $h(t)$ é **decrescente** nesse trecho. Logo, em $t=2$ (que está entre 0 e 6), a maré está **descendo**.

No intervalo $(6,12)$, a função retorna do mínimo ($h(6)=0{,}2$) ao próximo máximo ($h(12)=1{,}8$), portanto $h(t)$ é **crescente** nesse trecho. Logo, em $t=10$ (entre 6 e 12), a maré está **subindo**.

**Conclusão:** às 02h00 a maré está a 1,4 m e descendo; às 10h00 a maré está a 1,4 m e subindo.

## Formalização verificável

- `funcao` — expressão `Rational(4,5)*cos(pi*t/6) + 1`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `Rational(4,5)*cos(pi*t/6) + 1`, esperado `Rational(9,5)`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `Rational(4,5)*cos(pi*t/6) + 1`, esperado `Rational(1,5)`, parâmetros `{'consulta': 'minimo'}`
- `equacao` — expressão `Eq(Rational(4,5)*cos(pi*t/6) + 1, Rational(7,5))`, esperado `[2, 10]`, parâmetros `{'dominio': 'Interval.Ropen(0,12)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (maximo de 4*cos(pi*t/6)/5 + 1 em Reals: 9/5). | (3) aprovado: Gabarito confirmado (minimo de 4*cos(pi*t/6)/5 + 1 em Reals: 1/5). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado: dados completos (máximo, mínimo, instantes correspondentes, período), pedido claramente segmentado em duas etapas (modelagem e resolução/análise). Não há ambiguidade lexical ou estrutural relevante.
  - adequacao_nivel: 4/5 — O item (a) é aplicação direta de fórmulas de amplitude/período/deslocamento, compatível com Bloom 'aplicar'. O item (b) avança para uma análise qualitativa do comportamento gráfico (crescente/decrescente) sem uso de derivadas, exigindo articulação relacional entre a equação resolvida e a interpretação gráfica — isso eleva um pouco a exigência cognitiva além de um 'aplicar' puro, mas ainda dentro do escopo do Ensino Médio e coerente com a resposta esperada (estrutura relacional, não apenas multiestrutural).
  - alinhamento_bncc: 5/5 — Atende integralmente às exigências: parte de fenômeno periódico real (maré), exige modelagem explícita por cosseno com justificativa de cada parâmetro (amplitude, período, deslocamento vertical) e pede comparação entre o fenômeno e o comportamento gráfico da função (crescimento/decrescimento). Os parâmetros são centrais à resolução, não decorativos, e as duas etapas se articulam em um único problema coeso.
  - distratores: 5/5 — Não se aplica — questão discursiva.
  - originalidade: 4/5 — O contexto de maré é um clássico da matemática aplicada, mas a exigência de justificar subida/descida apenas pelo comportamento gráfico do cosseno (sem derivadas) foge do padrão mecânico de 'montar e resolver equação', evitando efeito Topaze ao não indicar o caminho de resolução.
