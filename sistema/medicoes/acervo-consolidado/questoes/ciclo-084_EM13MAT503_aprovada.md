# Ciclo 084 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Dois estudantes lançam, ao mesmo tempo, foguetes de brinquedo verticalmente para cima a partir do solo. As alturas atingidas pelos foguetes A e B, em metros, em função do tempo $t$ (em segundos) após o lançamento, são dadas por:

$h_A(t) = -5t^2 + 20t + 2$

$h_B(t) = -4t^2 + 18t + 3$

Qual das alternativas a seguir indica corretamente qual foguete atinge a maior altura máxima, o valor dessa altura, o instante em que ela ocorre, e justifica por que esse valor corresponde de fato a um ponto de máximo (e não de mínimo)?

## Alternativas

- (a) O foguete B atinge a maior altura máxima, 23,25 m, no instante t = 2,25 s; como o coeficiente de $t^2$ é negativo em ambas as funções, seus gráficos têm concavidade voltada para baixo e o vértice é ponto de máximo.  ← correta
- (b) O foguete A atinge a maior altura máxima, pois seu coeficiente de $t^2$ (-5) é mais negativo que o do foguete B (-4), o que indicaria uma parábola 'mais alta'.
  - *erro representado:* Confundir o valor absoluto do coeficiente 'a' (que mede a abertura da parábola) com a altura do vértice, sem de fato calcular os máximos.
- (c) O foguete B atinge a maior altura máxima, 20,25 m, no instante t = 2,25 s.
  - *erro representado:* Calcular a altura máxima apenas por $-b^2/(4a)$, esquecendo de somar o termo independente $c$ da função.
- (d) O foguete B atinge a maior altura máxima, pois sua altura inicial (3 m) é maior que a do foguete A (2 m).
  - *erro representado:* Comparar apenas as alturas iniciais (o termo c, valor de h(0)) em vez de calcular e comparar as alturas máximas reais das funções.

## Gabarito

O foguete B atinge a maior altura máxima, 23,25 m, no instante t = 2,25 s; como o coeficiente de t² é negativo em ambas as funções, seus gráficos têm concavidade voltada para baixo e o vértice é ponto de máximo.

## Resolução

**Passo 1 — Reconhecer que os vértices são pontos de máximo.**

Em ambas as funções o coeficiente de $t^2$ é negativo ($a_A=-5$ e $a_B=-4$), logo os gráficos são parábolas com concavidade voltada para baixo. Isso garante que o vértice de cada parábola corresponde a um **ponto de máximo**, não de mínimo.

**Passo 2 — Calcular o instante do máximo de cada foguete.**

Para o foguete A: $t_A = -\dfrac{b}{2a} = -\dfrac{20}{2\cdot(-5)} = 2$ s

Para o foguete B: $t_B = -\dfrac{b}{2a} = -\dfrac{18}{2\cdot(-4)} = 2{,}25$ s

**Passo 3 — Calcular a altura máxima de cada foguete substituindo $t_v$ na função.**

$h_A(2) = -5(2)^2 + 20(2) + 2 = -20 + 40 + 2 = 22$ m

$h_B(2{,}25) = -4(2{,}25)^2 + 18(2{,}25) + 3 = -20{,}25 + 40{,}5 + 3 = 23{,}25$ m

**Passo 4 — Comparar os dois resultados.**

Como $23{,}25 > 22$, o foguete **B** atinge a maior altura máxima, igual a **23,25 m**, no instante **t = 2,25 s**, e esse valor é de fato um ponto de máximo porque $a_B<0$.

## Formalização verificável

- `funcao` — expressão `-5*t**2 + 20*t + 2`, esperado `[2, 22]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-4*t**2 + 18*t + 3`, esperado `[Rational(9,4), Rational(93,4)]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Gabarito confirmado (maximo de -5*t**2 + 20*t em Interval(0, oo): 20).
  - funcao/maximo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado objetivo, define claramente a função, o domínio (t≥0) e a pergunta. Não há ambiguidade lexical ou estrutural; todos os dados necessários estão presentes.
  - adequacao_nivel: 2/5 — O processo cognitivo real é 'aplicar' (usar a fórmula t_v=-b/2a e substituir), correspondente a nível de Bloom 'aplicar', não 'analisar'. Na taxonomia SOLO a resposta é uniestrutural (um único procedimento mecânico), sem exigir relacionar variáveis, comparar situações ou justificar escolhas — características esperadas de uma tarefa de análise. O conteúdo é compatível com o Ensino Médio, mas o nível cognitivo declarado não é atingido.
  - alinhamento_bncc: 3/5 — A questão atende literalmente aos dois requisitos explícitos (pede ponto de máximo de função quadrática em contexto de Cinemática), mas a habilidade EM13MAT503 fala em 'investigar' — o que pressupõe algum grau de exploração, interpretação ou justificativa sobre o comportamento da função, não apenas aplicar a fórmula do vértice. A tarefa fica mais próxima de exercício-padrão de manipulação algébrica do que de uma investigação em situação real.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos plausíveis e distintos: esquecimento do fator 2 no vértice, confusão entre coordenada t e h, e erro de substituição (omitir o quadrado). Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 2/5 — O contexto (lançamento vertical com h(t)=-5t²+20t) é um exemplo canônico e repetido em praticamente todo livro didático sobre função quadrática/cinemática. A resolução fornecida segue passo a passo o algoritmo padrão, funcionando quase como 'efeito Topaze' ao entregar o caminho de solução explicitamente. Falta um elemento de contexto significativo ou uma pergunta que exija reflexão além da aplicação direta da fórmula.
  - *sugestões:* 1) Reformule a pergunta para exigir efetivamente 'analisar', não apenas aplicar a fórmula do vértice. Por exemplo: apresente duas situações de lançamento (ou duas funções h(t) com parâmetros diferentes) e peça para comparar as alturas máximas, justificar qual bola atinge maior altura e em que instante, ou determinar em que intervalo de tempo a bola permanece acima de determinada altura – isso força relacionar múltiplas informações (SOLO relacional). 2) Evite fornecer implicitamente o caminho de resolução na formulação do problema; retire pistas que 'pavimentam' a aplicação direta de t_v=-b/2a, incentivando o estudante a decidir por si mesmo qual estratégia usar (por exemplo, pedir para justificar por que o ponto encontrado é de máximo e não de mínimo). 3) Torne o contexto menos genérico: troque o lançamento vertical clássico por uma situação com dados mais específicos (ex.: altura de um foguete de brinquedo, arremesso em um esporte com números não redondos), aumentando o valor de investigação e reduzindo a familiaridade com exercícios de livro didático. 4) Mantenha os distratores atuais, pois já representam bem erros sistemáticos, mas ajuste-os caso a nova versão do enunciado envolva comparação entre duas funções.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reformule a pergunta para exigir efetivamente 'analisar', não apenas aplicar a fórmula do vértice. Por exemplo: apresente duas situações de lançamento (ou duas funções h(t) com parâmetros diferentes) e peça para comparar as alturas máximas, justificar qual bola atinge maior altura e em que instante, ou determinar em que intervalo de tempo a bola permanece acima de determinada altura – isso força relacionar múltiplas informações (SOLO relacional). 2) Evite fornecer implicitamente o caminho de resolução na formulação do problema; retire pistas que 'pavimentam' a aplicação direta de t_v=-b/2a, incentivando o estudante a decidir por si mesmo qual estratégia usar (por exemplo, pedir para justificar por que o ponto encontrado é de máximo e não de mínimo). 3) Torne o contexto menos genérico: troque o lançamento vertical clássico por uma situação com dados mais específicos (ex.: altura de um foguete de brinquedo, arremesso em um esporte com números não redondos), aumentando o valor de investigação e reduzindo a familiaridade com exercícios de livro didático. 4) Mantenha os distratores atuais, pois já representam bem erros sistemáticos, mas ajuste-os caso a nova versão do enunciado envolva comparação entre duas funções.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (2, 22)). | (2) aprovado: Gabarito confirmado (vértice calculado (9/4, 93/4)).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente as duas funções, especifica o que é pedido (foguete de maior altura máxima, valor, instante e justificativa de máximo) e não há ambiguidade nos dados nem no comando.
  - adequacao_nivel: 4/5 — A tarefa exige comparar duas funções quadráticas, calcular vértices e justificar por que se trata de máximo (não mínimo), o que envolve decomposição e relação entre elementos — compatível com 'analisar'. O formato de múltipla escolha, no entanto, reduz um pouco a exigência de produção autônoma, aproximando a resposta de um reconhecimento relacional (SOLO relacional, mas não estendido-abstrato).
  - alinhamento_bncc: 5/5 — Cumpre exatamente a habilidade EM13MAT503: investiga pontos de máximo de funções quadráticas em contexto de cinemática, exigindo cálculo do vértice, comparação entre duas situações e justificativa da natureza do ponto crítico — não é mera manipulação algébrica isolada.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: confundir |a| com altura do vértice, esquecer o termo c no cálculo do máximo, e confundir h(0) com o máximo real. Nenhum é absurdo ou trivialmente descartável sem cálculo.
  - originalidade: 3/5 — O contexto de lançamento vertical de projéteis é um clássico recorrente em livros didáticos de função quadrática; embora bem construído e com boa articulação entre cálculo e justificativa conceitual, não há elemento diferenciado de contextualização que evite o padrão tradicional do tema.
