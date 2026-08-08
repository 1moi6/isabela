# Ciclo 068 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Considere as quatro funções quadráticas a seguir, definidas para $x \in \mathbb{R}$:

$A) \; y = 3x^2$

$B) \; y = 3x^2 - 6$

$C) \; y = 3(x-2)^2$

$D) \; y = 3x^2 + 5x$

Para cada uma delas, determine algebricamente as coordenadas do vértice da parábola correspondente e, a partir dessa informação geométrica, identifique qual das quatro funções é tal que $y$ é diretamente proporcional a $x^2$ (isto é, pode ser escrita na forma $y = kx^2$). Justifique sua escolha relacionando a posição do vértice de cada parábola no plano cartesiano com a condição de proporcionalidade direta.

## Alternativas

- (a) A função $y = 3x^2$, pois seu gráfico é uma parábola cujo vértice está exatamente em $(0,0)$, coincidindo com a origem do plano cartesiano.  ← correta
- (b) A função $y = 3x^2 - 6$, pois seu vértice está sobre o eixo $y$ (em $x=0$), o que já garante a proporcionalidade direta entre $y$ e $x^2$.
  - *erro representado:* Confunde a condição de o vértice estar sobre o eixo y (b=0) com a condição completa de vértice na origem, ignorando que o termo constante c=-6 desloca o vértice para (0,-6).
- (c) A função $y = 3(x-2)^2$, pois seu gráfico toca o eixo $x$ em um único ponto, o que caracteriza a proporcionalidade direta com $x^2$.
  - *erro representado:* Confunde 'tangenciar o eixo x' (discriminante nulo) com 'ter vértice na origem'; o vértice de C está em (2,0), não em (0,0).
- (d) A função $y = 3x^2 + 5x$, pois seu gráfico passa pela origem (quando $x=0$, $y=0$), o que basta para garantir que $y$ é proporcional a $x^2$.
  - *erro representado:* Confunde 'a curva passar pela origem como um ponto' com 'ter o vértice na origem'; o termo linear 5x desloca o vértice para (-5/6, -25/12), quebrando a proporcionalidade direta mesmo com f(0)=0.

## Gabarito

A) y = 3x², pois é a única cujo vértice está exatamente na origem (0,0) do plano cartesiano.

## Resolução

**Condição geométrica-algébrica.** Uma função é da forma $y = kx^2$ (proporcionalidade direta entre $y$ e $x^2$) se, e somente se, não houver termo linear nem termo constante — o que equivale, geometricamente, a a parábola ter seu **vértice exatamente na origem** $(0,0)$ do plano cartesiano.

**Passo 1 — Vértice de A: $y=3x^2$.**
Aqui $a=3,\,b=0,\,c=0$. Logo $x_v = -\dfrac{b}{2a} = 0$ e $y_v = f(0) = 0$.
Vértice: $(0,0)$ — coincide com a origem.

**Passo 2 — Vértice de B: $y=3x^2-6$.**
$a=3,\,b=0,\,c=-6$. $x_v = 0$, $y_v = f(0) = -6$.
Vértice: $(0,-6)$ — está sobre o eixo $y$, mas **não** na origem (a parábola é a de A deslocada 6 unidades para baixo).

**Passo 3 — Vértice de C: $y=3(x-2)^2$.**
Expandindo: $y = 3x^2 - 12x + 12$, então $a=3,\,b=-12,\,c=12$.
$x_v = -\dfrac{-12}{2\cdot 3} = 2$, e $y_v = f(2) = 3(2-2)^2 = 0$.
Vértice: $(2,0)$ — a parábola toca o eixo $x$, mas em $x=2$, não na origem.

**Passo 4 — Vértice de D: $y=3x^2+5x$.**
$a=3,\,b=5,\,c=0$. $x_v = -\dfrac{5}{6}$.
$y_v = f\left(-\dfrac{5}{6}\right) = 3\cdot\dfrac{25}{36} + 5\cdot\left(-\dfrac{5}{6}\right) = \dfrac{25}{12} - \dfrac{25}{6} = -\dfrac{25}{12}$.
Vértice: $\left(-\dfrac{5}{6}, -\dfrac{25}{12}\right)$.
Observe que $f(0)=0$, ou seja, o gráfico de D *passa* pela origem como um ponto qualquer da curva, mas seu **vértice não está ali** — a presença do termo $5x$ desloca o vértice para fora da origem, o que confirma que $y$ não é proporcional a $x^2$ nesse caso.

**Conclusão.** Comparando os quatro vértices — $(0,0)$, $(0,-6)$, $(2,0)$ e $\left(-\frac56,-\frac{25}{12}\right)$ — apenas a parábola de **A** tem vértice exatamente na origem do plano cartesiano. Isso corresponde exatamente à condição algébrica $b=0$ e $c=0$, ou seja, $y=3x^2$, que é a única entre as quatro em que $y$ é diretamente proporcional a $x^2$.

## Formalização verificável

- `funcao` — expressão `3*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*x**2 - 6`, esperado `[0, -6]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*(x-2)**2`, esperado `[2, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*x**2 + 5*x`, esperado `[Rational(-5,6), Rational(-25,12)]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (0, 3)). | (3) aprovado: Gabarito confirmado (vértice calculado (1, 0)). | (4) aprovado: Gabarito confirmado (vértice calculado (1, -2)).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem estruturado, dados completos, sem ambiguidade lexical ou estrutural. O que é dado (quatro funções) e o que é pedido (identificar a proporcional e seu vértice) estão claramente delimitados.
  - adequacao_nivel: 4/5 — O processo exigido (checar termo linear/constante em cada função e associar ao vértice) é compatível com 'aplicar' um critério já fornecido a quatro casos, gerando resposta multiestrutural coerente com o nível declarado. Não chega a 'analisar', mas isso está de acordo com o Bloom declarado.
  - alinhamento_bncc: 2/5 — A habilidade exige que o ALUNO faça a conversão entre a forma algébrica e a geométrica, inferindo por si mesmo a equivalência 'proporcionalidade direta ⇔ vértice na origem'. Aqui essa equivalência já é dada explicitamente no enunciado ('Geometricamente, essa é a única cujo gráfico... vértice exatamente na origem'), eliminando a necessidade de o estudante transitar entre as representações — ele só precisa aplicar uma regra algébrica já fornecida (ausência de termos b e c). A questão versa sobre o tema certo, mas não realiza a habilidade como especificada.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos distintos e plausíveis: confundir termo constante com proporcionalidade, confundir deslocamento horizontal com potência pura, e confundir raiz com vértice. Nenhum é absurdo ou trivialmente eliminável sem raciocínio.
  - originalidade: 2/5 — O enunciado sofre de efeito Topaze: ao afirmar de antemão que a função proporcional é 'a única cujo gráfico é uma parábola com vértice exatamente na origem', a questão entrega a chave da solução, bastando ao aluno localizar visualmente qual expressão não tem termo extra. Isso reduz drasticamente o desafio cognitivo e o esvaziamento do propósito de 'converter representações'. O contexto também é puramente formal, sem situação significativa.
  - *sugestões:* 1) Remova do enunciado a frase que já revela a equivalência entre proporcionalidade direta e vértice na origem ('Geometricamente, essa é a única cujo gráfico... vértice exatamente na origem'); essa informação é justamente o que o aluno deveria descobrir, não algo fornecido. 2) Para atender de fato à habilidade EM13MAT402, peça explicitamente que o aluno esboce ou analise os gráficos das quatro funções (por exemplo, fornecendo os gráficos e pedindo que associe cada um à sua lei algébrica, ou pedindo que ele determine, a partir do gráfico, qual parábola passa pela origem com vértice ali) e então justifique por que apenas essa representa proporcionalidade direta, articulando abertamente as duas representações (algébrica e geométrica) em vez de apenas listar fórmulas. 3) Considere adicionar um contexto significativo (ex.: área de um quadrado em função do lado, energia cinética em função da velocidade) para que a proporcionalidade direta apareça como propriedade a ser identificada em um fenômeno real, e não apenas como exercício de forma algébrica isolada.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Remova do enunciado a frase que já revela a equivalência entre proporcionalidade direta e vértice na origem ('Geometricamente, essa é a única cujo gráfico... vértice exatamente na origem'); essa informação é justamente o que o aluno deveria descobrir, não algo fornecido. 2) Para atender de fato à habilidade EM13MAT402, peça explicitamente que o aluno esboce ou analise os gráficos das quatro funções (por exemplo, fornecendo os gráficos e pedindo que associe cada um à sua lei algébrica, ou pedindo que ele determine, a partir do gráfico, qual parábola passa pela origem com vértice ali) e então justifique por que apenas essa representa proporcionalidade direta, articulando abertamente as duas representações (algébrica e geométrica) em vez de apenas listar fórmulas. 3) Considere adicionar um contexto significativo (ex.: área de um quadrado em função do lado, energia cinética em função da velocidade) para que a proporcionalidade direta apareça como propriedade a ser identificada em um fenômeno real, e não apenas como exercício de forma algébrica isolada.

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (0, -6)). | (3) aprovado: Gabarito confirmado (vértice calculado (2, 0)). | (4) aprovado: Gabarito confirmado (vértice calculado (-5/6, -25/12)).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
- **Crítico:** aprovou
  - clareza: 3/5 — O enunciado pede que o aluno 'determine algebricamente', 'identifique' e 'justifique', sugerindo uma resposta dissertativa completa, mas o formato final é múltipla escolha, com alternativas que já contêm a justificativa por extenso. Essa mistura de formatos gera ambiguidade sobre o que efetivamente deve ser produzido pelo aluno (cálculo escrito completo? apenas escolha da letra?) e sobre como a resposta será avaliada.
  - adequacao_nivel: 4/5 — Calcular o vértice de quatro funções e comparar as posições para decidir qual satisfaz y=kx² é compatível com 'aplicar' (uso repetido de fórmula-padrão), embora a exigência de relacionar geometricamente vértice e proporcionalidade already empurre para um nível relacional (próximo de 'analisar' na taxonomia de Bloom/SOLO). Não há incoerência grave, mas o processo cognitivo é levemente mais exigente do que o nível declarado.
  - alinhamento_bncc: 5/5 — Cumpre integralmente as exigências: exige trânsito entre forma algébrica e vértice geométrico (não apenas raízes), e os quatro casos (translação vertical, horizontal e termo linear) realmente forçam a distinção entre proporcionalidade direta e outras configurações de parábola, articulando álgebra e geometria em um único problema coeso.
  - distratores: 5/5 — Cada alternativa incorreta corresponde a um erro conceitual específico e plausível (confundir vértice sobre o eixo y com vértice na origem; confundir tangência ao eixo x com vértice na origem; confundir passar pela origem com ter vértice na origem). Nenhum é absurdo ou eliminável por inspeção trivial.
  - originalidade: 3/5 — A escolha de quatro casos com armadilhas conceituais distintas é criativa e evita o enunciado clichê de 'ache o vértice da parábola'. Porém, ao incorporar a justificativa completa em cada alternativa, a questão pavimenta fortemente a solução (efeito Topaze): o aluno não precisa realmente elaborar o raciocínio geométrico pedido no enunciado, apenas reconhecer qual texto-justificativa é coerente, o que esvazia parte do valor da tarefa de 'justificar'.
