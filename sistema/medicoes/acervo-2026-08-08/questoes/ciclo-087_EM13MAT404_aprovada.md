# Ciclo 087 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Um ponto P parte da posição (0, 5) no instante t = 0 e passa a se mover indefinidamente, no sentido anti-horário, sobre uma circunferência de centro (0, 3) e raio 2, completando uma volta completa a cada intervalo de tempo Δt = 4π unidades de tempo. A ordenada de P, em função do tempo t, é dada por y(t) = 3 + 2cos(t/2).

Comparando a trajetória de P na circunferência (o ciclo trigonométrico deslocado e ampliado) com a representação gráfica de y(t) no plano cartesiano t × y, assinale a alternativa que apresenta corretamente o domínio, a imagem e o período dessa função.

## Alternativas

- (a) Domínio = ℝ; Imagem = [1, 5]; Período = 4π
  - *erro representado:* Acreditar que, por o ângulo no ciclo trigonométrico poder crescer ou decrescer indefinidamente (periodicidade), a função estaria definida para todo t real, ignorando que o tempo t, no gráfico cartesiano, tem um instante inicial (t = 0) a partir do qual o movimento existe.
- (b) Domínio = [0, +∞); Imagem = [-2, 2]; Período = 4π
  - *erro representado:* Calcular a imagem apenas a partir da amplitude do cosseno (2·cos varia em [-2,2]), esquecendo de somar o deslocamento vertical dado pela ordenada do centro da circunferência (3).
- (c) Domínio = [0, +∞); Imagem = [1, 5]; Período = 2π
  - *erro representado:* Usar o período padrão de cos(t), que é 2π, sem considerar que o argumento t/2 faz o ponto percorrer o ciclo mais lentamente, dobrando o tempo necessário para uma volta completa.
- (d) Domínio = [0, +∞); Imagem = [1, 5]; Período = 4π  ← correta

## Gabarito

D) Domínio = [0, +∞); Imagem = [1, 5]; Período = 4π

## Resolução

**1) Relacionando o ciclo com a função**

Se P parte de $(0,5)$ e gira com ângulo $\theta(t) = \dfrac{\pi}{2} + \dfrac{t}{2}$, sua ordenada é $y(t) = 3 + 2\sin\theta(t) = 3 + 2\cos\left(\dfrac{t}{2}\right)$, coerente com o enunciado.

**2) Imagem — usando a circunferência**

Na circunferência, o centro tem ordenada $3$ e o raio é $2$; logo a ordenada de qualquer ponto da trajetória varia entre $3-2=1$ e $3+2=5$. Essa é exatamente a faixa vertical ocupada pela curva no plano cartesiano, pois o cosseno varia continuamente entre $-1$ e $1$:
$$y(t) = 3 + 2\cos(t/2) \in [3-2,\ 3+2] = [1,5].$$
Assim, $\text{Im}(y) = [1,5]$ (não $[-1,1]$ nem $[-2,2]$, que ignoram o deslocamento vertical do centro).

**3) Período — usando a volta completa no ciclo**

Uma volta completa no ciclo corresponde a um acréscimo de $2\pi$ no ângulo $\theta$. Como $\theta(t) = \pi/2 + t/2$, um acréscimo $\Delta t$ em $t$ gera um acréscimo $\Delta t/2$ em $\theta$. Igualando a uma volta completa:
$$\frac{\Delta t}{2} = 2\pi \quad\Rightarrow\quad \Delta t = 4\pi,$$
que é exatamente o valor dado no enunciado. Logo o período fundamental é $T = 4\pi$ (não $2\pi$, que seria o período de $\cos(t)$ sem levar em conta a 'lentidão' do giro, causada pelo fator $1/2$ no argumento).

**4) Domínio — comparando o ciclo (que se repete para sempre) com o gráfico cartesiano (que começa em t = 0)**

No ciclo trigonométrico puro, o ângulo $\theta$ poderia crescer ou decrescer indefinidamente, sugerindo (erradamente) que a função estaria definida para todo $t \in \mathbb{R}$. Mas o movimento de P **começa** em $t=0$: antes desse instante o ponto simplesmente não existia em movimento, e depois dele continua girando para sempre. Ou seja, o eixo do tempo no gráfico cartesiano não é bidirecional como o ângulo abstrato do ciclo — ele tem uma origem física. Portanto o domínio da função que descreve esse movimento real é:
$$D(y) = [0, +\infty).$$

**5) Conclusão**

$$D(y) = [0,+\infty), \quad \text{Im}(y) = [1,5], \quad T = 4\pi.$$

## Formalização verificável

- `funcao` — expressão `3 + 2*cos(t/2)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `3 + 2*cos(t/2)`, esperado `Interval(1, 5)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`
- `funcao` — expressão `3 + 2*cos(t/2)`, esperado `4*pi`, parâmetros `{'consulta': 'periodo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 4). | (2) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (imagem de 3*sin(pi*x/2 + pi/4): Interval(-3, 3)).
  - funcao/periodo=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado define com precisão R, θ0, ω, sentido e instante inicial, sem ambiguidade lexical. Porém, o próprio enunciado já declara 't ≥ 0' antes de pedir o domínio como resposta, o que gera uma pequena inconsistência entre o que é 'dado' e o que é 'pedido'.
  - adequacao_nivel: 3/5 — O nível 'entender' é compatível com identificar período, domínio e imagem, mas os três subitens exigem esforços cognitivos desiguais: período e imagem demandam raciocínio (relacionar ω a T; relacionar R à amplitude), enquanto o domínio já foi fornecido literalmente no enunciado ('t≥0'), tornando essa parte apenas uma tarefa de cópia/reconhecimento, não de compreensão.
  - alinhamento_bncc: 3/5 — A questão articula bem ciclo trigonométrico e plano cartesiano para período e imagem, atendendo à EM13MAT404 nesses dois aspectos. Mas o domínio, que deveria emergir da comparação entre as duas representações (por que t não pode ser negativo, dado o contexto do movimento), já vem resolvido no enunciado, esvaziando parcialmente essa parte da habilidade.
  - distratores: 3/5 — Os erros de confundir ω com T e esquecer a amplitude R são sistemáticos e plausíveis. Contudo, a opção com domínio ℝ torna-se trivialmente eliminável, pois o próprio enunciado já afirmou explicitamente 't ≥ 0', enfraquecendo esse distrator.
  - originalidade: 2/5 — O contexto de MCU aplicado à trigonometria é razoavelmente pertinente, mas há um claro efeito Topaze: ao escrever 'em função do tempo t (em segundos, com t≥0)' antes de perguntar o domínio, o enunciado entrega a resposta de um dos três subitens, comprometendo o desafio da questão.
  - *sugestões:* 1) Remova a menção explícita 't ≥ 0' da frase que introduz y(t); mantenha apenas a informação de que o movimento se inicia em t=0 e continua indefinidamente, deixando o aluno deduzir o domínio a partir do contexto físico, não de uma declaração literal. 2) Equilibre o grau de exigência entre os três subitens, garantindo que também o domínio exija comparação entre o ciclo (que se repete indefinidamente) e a representação cartesiana (que começa em t=0), e não apenas releitura do enunciado. 3) Revise o distrator de domínio ℝ para que dependa de um raciocínio equivocado sobre periodicidade, e não apenas da desatenção a uma frase já dada. 4) Considere variar o contexto (evitar o clássico 'ponto girando no ciclo trigonométrico' sem elemento novo) para aumentar a originalidade, por exemplo relacionando a um fenômeno físico ou biológico com interpretação de gráfico real.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Remova a menção explícita 't ≥ 0' da frase que introduz y(t); mantenha apenas a informação de que o movimento se inicia em t=0 e continua indefinidamente, deixando o aluno deduzir o domínio a partir do contexto físico, não de uma declaração literal. 2) Equilibre o grau de exigência entre os três subitens, garantindo que também o domínio exija comparação entre o ciclo (que se repete indefinidamente) e a representação cartesiana (que começa em t=0), e não apenas releitura do enunciado. 3) Revise o distrator de domínio ℝ para que dependa de um raciocínio equivocado sobre periodicidade, e não apenas da desatenção a uma frase já dada. 4) Considere variar o contexto (evitar o clássico 'ponto girando no ciclo trigonométrico' sem elemento novo) para aumentar a originalidade, por exemplo relacionando a um fenômeno físico ou biológico com interpretação de gráfico real.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (2) aprovado: Gabarito confirmado (imagem de 2*cos(t/2) + 3: Interval(1, 5)). | (3) aprovado: Gabarito confirmado (período 4*pi).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/periodo=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado descreve com precisão a trajetória circular, o instante inicial, o sentido de rotação e fornece a lei y(t). A única fonte de possível dúvida é a restrição do domínio a [0,+∞): isso depende de o aluno interpretar t como 'tempo decorrido desde o início do movimento' (convenção física comum em problemas de movimento), e não como variável puramente matemática que admitiria extensão a t<0. Essa é uma sutileza real, mas o contexto ('parte da posição... no instante t=0') deixa isso razoavelmente explícito, evitando ambiguidade grave.
  - adequacao_nivel: 4/5 — O processo cognitivo pedido — traduzir entre a representação no ciclo trigonométrico e a representação cartesiana para extrair domínio, imagem e período — corresponde bem ao nível 'entender' declarado, especialmente pela ênfase em comparação de representações (não em cálculo isolado de valores). A exigência simultânea de três atributos aproxima a resposta de uma estrutura relacional (SOLO), o que é coerente e até desejável para o nível declarado, sem exceder para 'analisar' de forma incompatível.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente as exigências da EM13MAT404: pede domínio, imagem e período (as três características fundamentais listadas), e a resolução mobiliza explicitamente a comparação entre o ciclo trigonométrico (raio, centro, volta completa) e o gráfico cartesiano (eixo do tempo com origem física) para justificar cada atributo. Não se trata de mero cálculo de seno/cosseno de um ângulo, mas de articulação genuína entre as duas representações, como a habilidade exige.
  - distratores: 5/5 — Os três distratores correspondem a erros sistemáticos plausíveis e didaticamente relevantes: (a) supor domínio ℝ por confundir periodicidade angular com domínio temporal do modelo; (b) esquecer o deslocamento vertical do centro ao calcular a imagem; (c) usar o período padrão 2π ignorando o fator 1/2 no argumento. Nenhum é absurdo ou trivialmente eliminável por inspeção superficial.
  - originalidade: 4/5 — O contexto de um ponto se movendo sobre uma circunferência deslocada e ampliada, articulado com a leitura do gráfico cartesiano, é mais elaborado do que o exercício-padrão de 'dado y=a+b cos(ct), encontre domínio/imagem/período'. Evita o efeito Topaze ao exigir que o aluno construa a relação entre θ(t) e t antes de responder, embora o tema (movimento circular gerando função trigonométrica) seja um contexto já conhecido em livros didáticos.
