# Ciclo 062 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A magnitude $M$ de um abalo sísmico, medida na escala Richter, está relacionada à amplitude $A$ das ondas sísmicas registradas por um sismógrafo pela função $M = \log_{10}\left(\dfrac{A}{A_0}\right)$, em que $A_0$ é uma amplitude de referência constante (a mesma para todos os registros de um mesmo aparelho).

Uma cidade foi atingida por um terremoto de magnitude 4,0. Semanas depois, um segundo terremoto, de magnitude 6,0, atingiu a mesma região e foi registrado pelo mesmo sismógrafo.

a) Determine quantas vezes a amplitude das ondas sísmicas do terremoto de magnitude 6,0 foi maior do que a amplitude das ondas do terremoto de magnitude 4,0.

b) Um morador da cidade afirmou: "Como a diferença de magnitude foi de apenas 2 pontos, numa escala que costuma ir até 10, o segundo terremoto deve ter sido só um pouco mais forte, talvez uns 20% mais forte que o primeiro." Usando o valor obtido no item (a), explique por que essa interpretação está incorreta, destacando a natureza logarítmica (não linear) da escala Richter.

## Gabarito

a) A amplitude do terremoto de magnitude 6,0 foi 100 vezes maior que a do terremoto de magnitude 4,0. b) A interpretação do morador está errada porque a escala Richter é logarítmica: cada unidade a mais em $M$ multiplica a amplitude por 10 (não soma uma fração fixa). Uma diferença de 2 pontos corresponde a uma amplitude 100 vezes maior, não 20% maior.

## Resolução

**a) Cálculo da razão entre as amplitudes**

Para os dois terremotos, temos:

$M_1 = \log_{10}\left(\dfrac{A_1}{A_0}\right) = 4{,}0$

$M_2 = \log_{10}\left(\dfrac{A_2}{A_0}\right) = 6{,}0$

Subtraindo as duas equações e usando a propriedade do logaritmo do quociente:

$M_2 - M_1 = \log_{10}\left(\dfrac{A_2}{A_0}\right) - \log_{10}\left(\dfrac{A_1}{A_0}\right) = \log_{10}\left(\dfrac{A_2/A_0}{A_1/A_0}\right) = \log_{10}\left(\dfrac{A_2}{A_1}\right)$

Logo:

$\log_{10}\left(\dfrac{A_2}{A_1}\right) = 6{,}0 - 4{,}0 = 2{,}0$

Aplicando a definição de logaritmo (elevando 10 a ambos os lados):

$\dfrac{A_2}{A_1} = 10^{2{,}0} = 100$

**A amplitude do terremoto de magnitude 6,0 foi 100 vezes maior que a do terremoto de magnitude 4,0.**

**b) Interpretação da variação**

O erro do morador é tratar a escala Richter como se fosse uma escala **linear**, na qual a diferença de magnitudes (2 pontos) corresponderia a um aumento percentual pequeno e proporcional a essa diferença (como 20%).

No entanto, a função $M = \log_{10}(A/A_0)$ é **crescente**, mas de forma **logarítmica**: cada unidade a mais na magnitude corresponde a **multiplicar** a amplitude por 10, e não a somar uma parcela fixa. Por isso, uma diferença de 2 unidades na magnitude não corresponde a uma soma de 20% na amplitude, mas sim a uma multiplicação por $10^2 = 100$, como mostrado no item (a).

Ou seja, o terremoto de magnitude 6,0 não foi "um pouco mais forte": suas ondas tiveram amplitude **cem vezes maior** que as do terremoto de magnitude 4,0. Isso ilustra por que pequenas variações no valor de $M$ (grandeza medida na escala logarítmica) representam variações enormes na grandeza física real (a amplitude $A$).

## Formalização verificável

- `equacao` — expressão `Eq(log(x, 10), 2)`, esperado `[100]`
- `funcao` — expressão `log(x, 10)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (magnitudes 4,0 e 6,0), a fórmula e as duas tarefas (calcular razão de amplitudes e avaliar uma afirmação). Não há ambiguidade lexical ou estrutural; as condições estão completas para resolver ambos os itens.
  - adequacao_nivel: 4/5 — O item (a) é essencialmente uma aplicação direta da definição de logaritmo (nível 'aplicar'/multiestrutural), mas o item (b) exige avaliar criticamente uma afirmação errônea, articulando a razão calculada com a natureza não linear da escala — isso corresponde a 'analisar/avaliar' e a uma estrutura relacional (SOLO). O conjunto da questão, tomado como um todo, atinge o nível declarado, embora o item (a) isoladamente fique abaixo dele.
  - alinhamento_bncc: 5/5 — A questão não se limita a aplicar a definição de logaritmo: o item (b) exige explicitamente compreender e interpretar a variação da grandeza (amplitude) frente à variação de magnitude, contrastando percepção linear intuitiva com o comportamento logarítmico real. O contexto de abalos sísmicos é um dos exemplos citados na própria habilidade, e a articulação entre cálculo (a) e interpretação (b) é genuína, não uma justaposição de itens independentes.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — O contexto de terremotos e escala Richter é recorrente em livros didáticos, mas o recurso de introduzir a fala equivocada de um 'morador' que assume variação linear ('20% mais forte') é um dispositivo didático que evita o efeito Topaze, pois força o aluno a construir e justificar o contra-argumento em vez de seguir um roteiro guiado. Poderia ganhar ainda mais originalidade com dados numéricos menos usuais ou outro contexto (pH, radioatividade).
