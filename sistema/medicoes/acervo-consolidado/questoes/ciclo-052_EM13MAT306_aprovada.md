# Ciclo 052 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma boia de monitoramento registrou a altura da água (em metros) em um cais, em intervalos regulares de 3 horas, ao longo de um dia. Observou-se que o padrão de subida e descida se repete a cada 12 horas (maré semidiurna). Os dados coletados foram:

| t (horas) | 0 | 3 | 6 | 9 | 12 |
|---|---|---|---|---|---|
| h (metros) | 8 | 5 | 2 | 5 | 8 |

Esse tipo de fenômeno periódico pode ser representado no plano cartesiano por uma função seno ou por uma função cosseno. Observando em que instante ocorrem os valores máximo e mínimo da maré, identifique qual das duas representações (seno ou cosseno) é a mais adequada para modelar h(t) e, em seguida, utilize o modelo escolhido para determinar a altura da água no instante t = 2 horas.

## Alternativas

- (a) 6,5 m  ← correta
- (b) 7,6 m (aproximadamente)
  - *erro representado:* Assumir automaticamente que todo fenômeno periódico deve ser modelado por seno, sem verificar que a maré atinge seu valor máximo em t=0 (o que exige cosseno); usa h(t)=5+3·sen(πt/6), obtendo h(2)=5+3·(√3/2)≈7,6.
- (c) 9,5 m
  - *erro representado:* Confundir o valor médio (deslocamento vertical k) com o valor máximo observado, usando k=8 em vez de k=(8+2)/2=5; calcula h(t)=8+3·cos(πt/6), obtendo h(2)=9,5.
- (d) 3,5 m
  - *erro representado:* Tomar o intervalo entre um máximo e o mínimo seguinte (6 horas) como se fosse o período completo, usando T=6 em vez de T=12 e, portanto, ω=π/3 em vez de π/6; calcula h(t)=5+3·cos(πt/3), obtendo h(2)=3,5.

## Gabarito

6,5 m

## Resolução

**Passo 1 — Amplitude e valor médio (deslocamento vertical).**
O valor máximo é $8$ m e o mínimo é $2$ m. Logo:
$$k=\frac{8+2}{2}=5,\qquad A=\frac{8-2}{2}=3$$

**Passo 2 — Período e frequência angular.**
O padrão se repete a cada $12$ h, então $T=12$ e
$$\omega=\frac{2\pi}{T}=\frac{2\pi}{12}=\frac{\pi}{6}$$

**Passo 3 — Escolha entre seno e cosseno.**
A função seno, sem deslocamento de fase, vale $0$ (o valor médio $k$) em $t=0$ e cresce a partir daí. Já a função cosseno atinge seu **valor máximo** exatamente em $t=0$. Como a tabela mostra $h(0)=8$ (o máximo), a representação adequada é a **cosseno**, sem necessidade de deslocamento de fase:
$$h(t)=5+3\cos\left(\frac{\pi}{6}t\right)$$

Conferindo com a tabela: $h(3)=5+3\cos(\pi/2)=5$ ✓; $h(6)=5+3\cos(\pi)=2$ ✓; $h(9)=5+3\cos(3\pi/2)=5$ ✓; $h(12)=5+3\cos(2\pi)=8$ ✓.

**Passo 4 — Cálculo em $t=2$.**
$$h(2)=5+3\cos\left(\frac{\pi}{6}\cdot 2\right)=5+3\cos\left(\frac{\pi}{3}\right)=5+3\cdot\frac{1}{2}=6{,}5\text{ m}$$

Portanto, a altura da água em $t=2$ h é **6,5 m**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5 + 3*cos(pi*t/6)`, parâmetros `{'pontos': '[(0,8),(3,5),(6,2),(9,5),(12,8)]'}`
- `funcao` — expressão `5 + 3*cos(pi*t/6)`, esperado `Rational(13,2)`, parâmetros `{'consulta': 'valor', 'ponto': '2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (maximo de 2*cos(pi*t/6) + 3 em Reals: 5). | (2) aprovado: Gabarito confirmado (minimo de 2*cos(pi*t/6) + 3 em Reals: 1). | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(0) = 5).
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - funcao/periodo=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — Os dados (altura máxima, mínima, instantes e período) são claros e suficientes. Porém há uma inconsistência: o enunciado já fixa a forma da função como h(t)=k+A·cos(ωt), mas uma das alternativas usa seno, o que contraria o 'tipo' pedido e pode confundir o aluno sobre se a forma funcional é ou não parte do que deve ser decidido.
  - adequacao_nivel: 2/5 — O processo cognitivo real é apenas substituir valores em fórmulas prontas (k=(max+min)/2, A=(max-min)/2, ω=2π/T) e montar a expressão — isso é 'aplicar', não 'analisar'. Como a forma cosseno já é dada no enunciado, não há decisão a ser feita sobre qual função (seno ou cosseno) melhor representa o fenômeno, que seria o núcleo de uma tarefa analítica. Em termos SOLO, a resposta é multiestrutural (calcular três parâmetros independentes e combiná-los), não relacional/analítica.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT306 exige 'comparar as representações com as funções seno e cosseno' — ou seja, o aluno deveria justificar por que o cosseno (e não o seno) modela o fenômeno, a partir da leitura do comportamento periódico. Ao fornecer a forma h(t)=k+A·cos(ωt) já pronta no enunciado, essa comparação é eliminada, reduzindo a questão a um exercício de cálculo de parâmetros (que atende apenas parcialmente ao critério 'amplitude, período e deslocamento como objeto da questão'), sem cumprir a exigência central de comparação de representações.
  - distratores: 3/5 — Os distratores que trocam k e A, ou usam T em vez de ω, representam erros sistemáticos plausíveis. Contudo, o distrator com seno é trivialmente eliminável, pois o próprio enunciado já declarou que a função é do tipo cosseno — tornando essa alternativa incoerente com a premissa dada, não um erro conceitual genuíno a ser descartado por análise do fenômeno.
  - originalidade: 2/5 — O contexto de marés com h(t)=k+A·cos(ωt) é um exemplo extremamente recorrente em livros didáticos e listas de exercícios sobre funções trigonométricas, sem elementos que tragam um ângulo novo ao problema. Além disso, ao entregar a forma da função pronta, o enunciado pavimenta fortemente a solução (efeito Topaze), retirando do aluno a etapa de modelagem/decisão que daria originalidade e desafio à tarefa.
  - *sugestões:* 1) Remova do enunciado a informação de que a função é do tipo h(t)=k+A·cos(ωt); apresente os dados do fenômeno (ex.: uma tabela de alturas em diferentes horários ou um gráfico) e peça explicitamente que o aluno decida e justifique se a modelagem deve ser feita com seno ou com cosseno, com base no comportamento observado (onde ocorre o máximo/mínimo). Isso restaura a exigência de 'comparar representações' da habilidade EM13MAT306. 2) Ajuste as alternativas para que todas sigam o mesmo formato até a fase ser de fato uma variável em disputa — por exemplo, inclua opções com cosseno e seno com deslocamentos de fase diferentes (ex.: cos(ωt), sen(ωt+π/2), sen(ωt) etc.), todas plausíveis dado o enunciado revisado, evitando que uma alternativa seja eliminável apenas por não bater com uma forma pré-anunciada. 3) Para elevar o nível cognitivo a 'analisar', peça também que o aluno interprete o significado de k, A e ω no contexto (por exemplo, pergunte qual seria a altura da água às 3h ou peça para identificar em que intervalo a maré está subindo), de modo que a resposta exija relacionar múltiplos aspectos da função com o fenômeno, não apenas montar a expressão.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Remova do enunciado a informação de que a função é do tipo h(t)=k+A·cos(ωt); apresente os dados do fenômeno (ex.: uma tabela de alturas em diferentes horários ou um gráfico) e peça explicitamente que o aluno decida e justifique se a modelagem deve ser feita com seno ou com cosseno, com base no comportamento observado (onde ocorre o máximo/mínimo). Isso restaura a exigência de 'comparar representações' da habilidade EM13MAT306. 2) Ajuste as alternativas para que todas sigam o mesmo formato até a fase ser de fato uma variável em disputa — por exemplo, inclua opções com cosseno e seno com deslocamentos de fase diferentes (ex.: cos(ωt), sen(ωt+π/2), sen(ωt) etc.), todas plausíveis dado o enunciado revisado, evitando que uma alternativa seja eliminável apenas por não bater com uma forma pré-anunciada. 3) Para elevar o nível cognitivo a 'analisar', peça também que o aluno interprete o significado de k, A e ω no contexto (por exemplo, pergunte qual seria a altura da água às 3h ou peça para identificar em que intervalo a maré está subindo), de modo que a resposta exija relacionar múltiplos aspectos da função com o fenômeno, não apenas montar a expressão.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*cos(pi*t/6) + 5: reproduz os 5 pontos dados. | (2) aprovado: Gabarito confirmado (f(2) = 13/2).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (tabela de altura x tempo), o contexto (maré semidiurna) e as duas tarefas pedidas (escolher entre seno/cosseno e calcular h(2)). Não há ambiguidade lexical ou estrutural, e os dados fornecidos são suficientes para resolver o problema sem informações implícitas.
  - adequacao_nivel: 4/5 — A etapa de comparar h(0)=máximo com as propriedades de seno (que parte do valor médio) e cosseno (que parte do máximo) exige de fato uma análise relacional (SOLO relacional), compatível com o nível 'analisar' de Bloom. No entanto, a etapa final de cálculo de h(2) é aplicação direta de fórmula, reduzindo um pouco o peso analítico do conjunto da questão. Ainda assim, a decisão do modelo é o núcleo cognitivo da tarefa e está bem alinhada ao nível declarado.
  - alinhamento_bncc: 5/5 — Cumpre todas as exigências: parte de fenômeno periódico real (maré), exige explicitamente comparar a situação com as representações seno e cosseno no plano cartesiano, e amplitude, período e deslocamento vertical são elementos centrais do raciocínio (não decorativos), pois são usados tanto para escolher o modelo quanto para validar contra a tabela.
  - distratores: 5/5 — Os quatro distratores mapeiam erros conceituais plausíveis e distintos: escolha automática de seno sem checar a fase, confusão entre valor médio e valor máximo (deslocamento vertical incorreto), e erro no cálculo do período (confundir meio período com período completo). Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 4/5 — O contexto de maré é um clássico dos livros didáticos para funções periódicas, mas o enunciado evita o efeito Topaze ao não indicar diretamente qual função usar, exigindo que o aluno raciocine sobre a fase a partir dos dados. Poderia ganhar em originalidade com um contexto menos convencional (ex.: batimento cardíaco, sinal sonoro, ciclo de iluminação).
