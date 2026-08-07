# Ciclo 003 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em um estudo sobre a maré de um porto, registrou-se que, em determinado dia, a altura da água atinge seu valor máximo de 5 metros exatamente à meia-noite (t = 0 h) e seu valor mínimo de 1 metro às 6 h da manhã. Esse padrão se repete integralmente a cada 12 horas, de modo que a maré volta a atingir seu valor máximo às 12 h, às 24 h, e assim sucessivamente. Deseja-se representar, no plano cartesiano, a altura h(t) da maré (em metros) em função do tempo t (em horas) por meio de uma função do tipo h(t) = A·cos(B·t) + D, com A, B e D constantes reais positivas, que reproduza fielmente a amplitude, o período e o deslocamento vertical observados.

Qual das expressões abaixo representa corretamente h(t)?

## Alternativas

- (a) h(t) = 2cos(πt/6) + 3  ← correta
- (b) h(t) = 4cos(πt/6) + 3
  - *erro representado:* Uso da diferença entre máximo e mínimo (5-1=4) diretamente como amplitude, sem dividir por 2.
- (c) h(t) = 2cos(πt/6) + 5
  - *erro representado:* Uso do valor máximo (5) como deslocamento vertical D, em vez da média entre máximo e mínimo.
- (d) h(t) = 2cos(πt/3) + 3
  - *erro representado:* Confusão entre o intervalo de tempo do máximo ao mínimo (6h, meio período) e o período completo do fenômeno (12h), levando a B = 2π/6 em vez de 2π/12.

## Gabarito

h(t) = 2cos(πt/6) + 3

## Resolução

**Passo 1 — Amplitude (A):** a amplitude é a metade da diferença entre o valor máximo e o valor mínimo:
$$A = \frac{5-1}{2} = 2$$

**Passo 2 — Deslocamento vertical (D):** é a média entre o valor máximo e o valor mínimo, que representa o "nível médio" em torno do qual a maré oscila:
$$D = \frac{5+1}{2} = 3$$

**Passo 3 — Período (T) e coeficiente B:** como a maré alta se repete a cada 12 horas, o período completo do fenômeno é $T = 12$. Como $T = \dfrac{2\pi}{B}$, temos:
$$B = \frac{2\pi}{12} = \frac{\pi}{6}$$

**Passo 4 — Ajuste de fase:** a função cosseno atinge seu valor máximo em $x=0$, ou seja, $\cos(0)=1$. Como o enunciado informa que a maré atinge seu máximo exatamente em $t=0$, o cosseno já está alinhado com o fenômeno, sem necessidade de deslocamento horizontal (defasagem).

**Passo 5 — Montagem da função:**
$$h(t) = 2\cos\left(\frac{\pi}{6}t\right) + 3$$

**Verificação:**
- Em $t=0$: $h(0) = 2\cos(0)+3 = 2+3 = 5$ (máximo, confere).
- Em $t=6$: $h(6) = 2\cos(\pi)+3 = -2+3 = 1$ (mínimo, confere).
- Período: $T = \dfrac{2\pi}{\pi/6} = 12$ horas (confere).

Portanto, a função correta é $h(t) = 2\cos\left(\dfrac{\pi}{6}t\right)+3$.

## Formalização verificável

- `funcao` — expressão `2*cos(pi*x/6) + 3`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `2*cos(pi*x/6) + 3`, esperado `Interval(1, 5)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `2*cos(pi*x/6) + 3`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `2*cos(pi*x/6) + 3`, esperado `1`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (imagem de 2*cos(pi*x/6) + 3: Interval(1, 5)). | (3) aprovado: Gabarito confirmado (f(0) = 5). | (4) aprovado: Gabarito confirmado (f(6) = 1).
  - funcao/periodo=aprovado
  - funcao/imagem=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado explicita claramente os dados (máximo, mínimo, instantes, periodicidade) e o que se pede (identificar h(t)). Não há ambiguidade lexical ou estrutural; os dados são suficientes para resolver univocamente o problema.
  - adequacao_nivel: 5/5 — O processo exigido é de fato 'aplicar': o aluno usa fórmulas conhecidas (A = (max-min)/2, D = (max+min)/2, B = 2π/T) em uma situação concreta, sem precisar justificar ou comparar múltiplas estratégias. A estrutura de resposta é multiestrutural/relacional (combinar três parâmetros calculados separadamente), compatível com o nível 'aplicar' declarado. Conteúdo (função cosseno, período, amplitude) é adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — Parte de um fenômeno periódico real (maré), exige representar a situação por uma função cosseno no plano cartesiano e articula amplitude, período e deslocamento vertical como elementos centrais do raciocínio, não decorativos — todos são efetivamente calculados e usados na resposta. Cumpre integralmente as exigências da EM13MAT306 listadas.
  - distratores: 5/5 — Os três distratores correspondem a erros sistemáticos plausíveis e comuns: (1) não dividir a diferença por 2 para obter a amplitude, (2) usar o valor máximo em vez da média como D, (3) confundir o intervalo até o mínimo (meio período) com o período completo. Nenhum é absurdo ou trivialmente descartável sem cálculo.
  - originalidade: 4/5 — O contexto de maré é um clássico recorrente em materiais didáticos sobre funções trigonométricas, o que reduz um pouco a originalidade, mas o enunciado não copia literalmente um problema-padrão e apresenta dados específicos e plausíveis. Há leve efeito Topaze ao afirmar explicitamente que o máximo ocorre em t=0, o que elimina de antemão a necessidade de raciocinar sobre defasagem de fase, facilitando a tarefa além do estritamente necessário para o nível 'aplicar'.
