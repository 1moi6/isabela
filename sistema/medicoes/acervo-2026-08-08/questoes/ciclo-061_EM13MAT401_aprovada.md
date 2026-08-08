# Ciclo 061 — EM13MAT401

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Considere as funções reais f(x) = 2x, g(x) = 2x + 3 e h(x) = -2x, definidas para todo x real.

a) Determine as coordenadas de dois pontos do gráfico de cada função e utilize-os para esboçar, num mesmo plano cartesiano, as retas correspondentes a f, g e h.

b) Observando os três gráficos esboçados, indique quais retas passam pela origem do plano cartesiano e quais não passam.

c) A partir do que você observou, enuncie uma regra geral: dada uma lei y = ax + b (com a ≠ 0), como decidir, apenas olhando os coeficientes a e b (sem construir o gráfico), se a reta correspondente passará ou não pela origem? Qual é o nome usual dado ao tipo de função cujo gráfico passa pela origem, e qual o nome dado ao caso em que isso não ocorre?

d) Compare os coeficientes angulares de f, g e h. Existe alguma relação geométrica de paralelismo entre duas dessas retas? Justifique sua resposta e descreva, em palavras, como o gráfico de g pode ser obtido a partir do gráfico de f.

## Gabarito

b) f e h passam pela origem; g não passa. c) A reta y=ax+b passa pela origem se, e somente se, b=0; nesse caso a função é linear/proporcional, e quando b≠0 é afim não proporcional. d) f e g são paralelas (mesmo a=2); h não é paralela a nenhuma delas; o gráfico de g é o gráfico de f transladado 3 unidades para cima.

## Resolução

**a) Pontos e esboço**

Para $f(x)=2x$: $f(0)=0$ e $f(1)=2$, logo a reta passa pelos pontos $(0,0)$ e $(1,2)$.

Para $g(x)=2x+3$: $g(0)=3$ e $g(1)=5$, logo a reta passa pelos pontos $(0,3)$ e $(1,5)$.

Para $h(x)=-2x$: $h(0)=0$ e $h(1)=-2$, logo a reta passa pelos pontos $(0,0)$ e $(1,-2)$.

Ao marcar esses pontos no plano cartesiano e traçar as retas, obtém-se: $f$ crescente passando pela origem, $g$ crescente deslocada para cima, e $h$ decrescente passando pela origem.

**b) Quais passam pela origem**

$f(0)=0$ e $h(0)=0$, então as retas de $f$ e de $h$ passam pela origem $(0,0)$.

$g(0)=3\neq 0$, então a reta de $g$ **não** passa pela origem.

**c) Regra geral**

Uma reta $y=ax+b$ passa pela origem se, e somente se, o ponto $(0,0)$ satisfaz a equação, isto é, $a\cdot 0+b=0$, ou seja, $b=0$.

- Se $b=0$, a lei é $y=ax$: a função é chamada de **função linear** (caso particular, também dito **proporcional**), e seu gráfico sempre passa pela origem.
- Se $b\neq 0$, a função é chamada de **função afim** (não proporcional), e seu gráfico é uma reta paralela à de $y=ax$, mas deslocada verticalmente, não passando pela origem.

No exemplo: $f$ e $h$ são funções lineares (proporcionais), enquanto $g$ é afim não proporcional.

**d) Paralelismo e translação**

O coeficiente angular de $f$ é $a=2$, o de $g$ também é $a=2$, e o de $h$ é $a=-2$.

Como $f$ e $g$ têm o **mesmo coeficiente angular** ($a=2$), suas retas são **paralelas**. Já $h$ tem coeficiente angular diferente ($-2$), logo não é paralela nem a $f$ nem a $g$.

Geometricamente, como $g(x)=f(x)+3$, o gráfico de $g$ é obtido **transladando verticalmente** o gráfico de $f$ em $3$ unidades para cima — por isso as retas permanecem paralelas, mas apenas a de $f$ passa pela origem.

## Formalização verificável

- `funcao` — expressão `2*x`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `2*x + 3`, esperado `[Rational(-3,2)]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `-2*x`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `2*x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `-2*x`, esperado `decrescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `2*x + 3`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (zeros da função: [0]). | (2) aprovado: Gabarito confirmado (f(0) = 0). | (3) aprovado: Gabarito confirmado (zeros da função: [2]). | (4) aprovado: Gabarito confirmado (f(0) = -6).
  - funcao/zeros=aprovado
  - funcao/valor=aprovado
  - funcao/zeros=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: define as duas funções, especifica exatamente o que deve ser calculado (interceptos nos dois eixos) e o que deve ser concluído (classificação com justificativa). Não há ambiguidade lexical ou estrutural, e os dados (leis das funções) são suficientes para resolver ambos os itens.
  - adequacao_nivel: 4/5 — O item (a) é essencialmente aplicar (calcular f(0), g(0) e resolver f(x)=0, g(x)=0), compatível com Bloom 'entender' apenas se seguido de reflexão conceitual, o que ocorre no item (b). A estrutura de resposta é multiestrutural em (a) e relacional em (b), o que é coerente com 'entender', mas o percurso é bastante guiado, reduzindo a exigência cognitiva real esperada para o nível declarado.
  - alinhamento_bncc: 4/5 — A questão exige transitar da lei algébrica para pontos do plano cartesiano (interceptos) e usa esse resultado para distinguir proporcional de afim não proporcional, atendendo ao núcleo da habilidade. Entretanto, não há exigência explícita de desenhar/analisar o gráfico como reta (apenas pontos isolados), o que enfraquece um pouco o 'trânsito para representação geométrica' pleno que a habilidade prevê; ainda assim, o objetivo central (distinguir proporcional de afim) é cumprido.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — O enunciado reproduz um formato clássico de livro didático (duas funções lineares, calcular interceptos, classificar). Mais grave: o próprio comando do item (b) já entrega o critério de classificação ('se ela passa ou não pela origem'), configurando efeito Topaze evidente — o aluno não precisa descobrir o critério, apenas aplicá-lo mecanicamente ao que já calculou. Falta um contexto significativo ou uma pergunta que exija descoberta do critério pelo próprio estudante.
  - *sugestões:* Reformule o item (b) para não revelar o critério de classificação: em vez de dizer 'se ela passa ou não pela origem', peça algo como 'que característica algébrica e geométrica diferencia as duas retas? Generalize para y = ax + b'. Isso obriga o aluno a inferir a condição b=0 versus b≠0 em vez de apenas confirmá-la. Considere também acrescentar um terceiro caso (ex.: h(x) = -2x) ou pedir que o aluno esboce as retas no plano cartesiano, fortalecendo a exigência de trânsito entre representação algébrica e geométrica prevista na habilidade EM13MAT401. Para elevar o nível cognitivo a 'entender' de forma mais robusta, peça uma generalização (ex.: 'enuncie uma regra geral para decidir, apenas observando a lei y=ax+b, se o gráfico passa pela origem') em vez de aplicar a regra a um caso já dado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule o item (b) para não revelar o critério de classificação: em vez de dizer 'se ela passa ou não pela origem', peça algo como 'que característica algébrica e geométrica diferencia as duas retas? Generalize para y = ax + b'. Isso obriga o aluno a inferir a condição b=0 versus b≠0 em vez de apenas confirmá-la. Considere também acrescentar um terceiro caso (ex.: h(x) = -2x) ou pedir que o aluno esboce as retas no plano cartesiano, fortalecendo a exigência de trânsito entre representação algébrica e geométrica prevista na habilidade EM13MAT401. Para elevar o nível cognitivo a 'entender' de forma mais robusta, peça uma generalização (ex.: 'enuncie uma regra geral para decidir, apenas observando a lei y=ax+b, se o gráfico passa pela origem') em vez de aplicar a regra a um caso já dado.

### Iteração 2

- **Verificador:** aprovado — Todas as 6 afirmações conferidas. (1) aprovado: Gabarito confirmado (zeros da função: [0]). | (2) aprovado: Gabarito confirmado (zeros da função: [-3/2]). | (3) aprovado: Gabarito confirmado (zeros da função: [0]). | (4) aprovado: Gabarito confirmado (crescente em Reals). | (5) aprovado: Gabarito confirmado (decrescente em Reals). | (6) aprovado: Gabarito confirmado (f(0) = 3).
  - funcao/zeros=aprovado
  - funcao/zeros=aprovado
  - funcao/zeros=aprovado
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é bem segmentado em quatro itens que deixam claro o que é dado (as três leis de função) e o que é pedido em cada etapa (pontos, gráfico, comparação, generalização). Não há ambiguidade lexical ou estrutural, e os dados (as três funções) são suficientes para resolver todos os itens.
  - adequacao_nivel: 3/5 — O nível de Bloom declarado é 'entender', mas os itens c) e d) exigem processos cognitivos mais elevados: em c) o aluno deve induzir e enunciar uma regra geral a partir da observação (generalização/síntese, próxima de 'criar'), e em d) deve comparar, justificar e descrever uma transformação geométrica (característico de 'analisar'). A estrutura de resposta em d) é relacional (SOLO), compatível com 'analisar', não com mera compreensão. Há descompasso entre o nível declarado e o efetivamente demandado pela questão, mesmo que os conteúdos sejam adequados ao Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão atende integralmente às exigências: exige trânsito genuíno entre forma algébrica (leis de f, g, h) e representação geométrica (esboço e leitura de gráficos), e conduz explicitamente à distinção entre o caso proporcional (f e h, com b=0) e o caso apenas afim (g, com b≠0), articulando isso com o conceito de paralelismo e translação de gráficos em um único problema coerente, não em itens desconexos.
  - distratores: 5/5 — Não se aplica: questão discursiva, sem alternativas de múltipla escolha.
  - originalidade: 4/5 — Embora o tema (retas y=ax+b, proporcionalidade, paralelismo) seja um clássico recorrente em livros didáticos, a condução por indução (observar, comparar coeficientes, só depois enunciar a regra) evita fornecer a resposta de antemão, reduzindo o efeito Topaze. Falta, porém, um contexto aplicado ou situação significativa que fugisse do exercício puramente teórico-abstrato.
