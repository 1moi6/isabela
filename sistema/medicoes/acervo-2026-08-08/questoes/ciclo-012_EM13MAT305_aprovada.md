# Ciclo 012 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A magnitude $M$ de um abalo sísmico, na escala Richter, é definida por $M = \log_{10}(I)$, em que $I$ é a intensidade da onda sísmica medida em relação a uma intensidade de referência igual a 1. Estudos sismológicos mostram que a energia $E$ (em joules) liberada por um terremoto se relaciona com sua magnitude pela expressão $\log_{10}(E) = 1{,}5M + 4{,}8$.

Um terremoto A tem magnitude $M_A = 6{,}5$ e um terremoto B tem magnitude $M_B = 5{,}0$.

a) Determine quantas vezes a intensidade sísmica do terremoto A é maior que a do terremoto B.

b) Determine quantas vezes a energia liberada pelo terremoto A é maior que a liberada pelo terremoto B.

c) Um sismólogo afirma: "toda vez que a magnitude de um terremoto aumenta 1 unidade, a energia liberada aumenta sempre pelo mesmo fator, não importa qual seja a magnitude inicial". Verifique se essa afirmação é verdadeira, calculando esse fator (caso exista de fato), e explique, com base nesse resultado, por que a escala Richter é chamada de logarítmica em vez de linear.

## Gabarito

a) $10^{1,5}=10\sqrt{10}\approx 31,6$ vezes. b) $10^{2,25}=100\sqrt[4]{10}\approx 177,8$ vezes. c) Verdadeira: o fator é constante e igual a $10^{1,5}\approx 31,6$, independente de $M$, pois a diferença de magnitudes (sempre igual a 1) é o único responsável pelo expoente; isso evidencia que a escala Richter é logarítmica, transformando acréscimos aditivos em magnitude em acréscimos multiplicativos na grandeza física.

## Resolução

**a) Razão entre as intensidades**

Da definição $M = \log_{10}(I)$ segue que $I = 10^{M}$. Logo:
$$\frac{I_A}{I_B} = \frac{10^{M_A}}{10^{M_B}} = 10^{M_A - M_B} = 10^{6{,}5-5} = 10^{1{,}5}$$

$$10^{1{,}5} = 10\sqrt{10} \approx 31{,}6$$

A intensidade do terremoto A é aproximadamente **31,6 vezes** maior que a do terremoto B.

**b) Razão entre as energias**

De $\log_{10}(E) = 1{,}5M + 4{,}8$ vem $E = 10^{1{,}5M+4{,}8}$. Então:
$$\frac{E_A}{E_B} = \frac{10^{1{,}5M_A+4{,}8}}{10^{1{,}5M_B+4{,}8}} = 10^{1{,}5(M_A-M_B)} = 10^{1{,}5\cdot 1{,}5} = 10^{2{,}25}$$

$$10^{2{,}25} = 100\sqrt[4]{10} \approx 177{,}8$$

A energia liberada por A é aproximadamente **177,8 vezes** maior que a liberada por B.

**c) Análise da variação geral**

Para qualquer magnitude $M$, comparando $M$ e $M+1$:
$$\frac{E(M+1)}{E(M)} = \frac{10^{1{,}5(M+1)+4{,}8}}{10^{1{,}5M+4{,}8}} = 10^{1{,}5(M+1)+4{,}8-(1{,}5M+4{,}8)} = 10^{1{,}5}$$

O expoente $1{,}5$ **não depende de $M$**: ele desapareceu porque a diferença de magnitudes é sempre 1. Logo, a afirmação do sismólogo é **verdadeira**, e o fator constante é
$$10^{1{,}5} = 10\sqrt{10}\approx 31{,}6.$$

Isso ocorre porque $M$ é definido como um *logaritmo* da grandeza física (intensidade) e a energia é uma função exponencial de $M$. Como o logaritmo transforma multiplicações em somas, um acréscimo **constante e aditivo** na magnitude ($+1$) corresponde sempre a um acréscimo **constante e multiplicativo** (fator $10^{1{,}5}$) na energia e na intensidade, qualquer que seja o ponto de partida. É exatamente essa correspondência entre passos aditivos na escala e saltos multiplicativos na grandeza real que caracteriza uma escala logarítmica — diferente de uma escala linear, em que um acréscimo constante em $M$ corresponderia a um acréscimo constante (aditivo) na energia.

## Formalização verificável

- `equacao` — expressão `Eq(log(x,10), Rational(3,2))`, esperado `[10**Rational(3,2)]`
- `equacao` — expressão `Eq(log(y,10), Rational(9,4))`, esperado `[10**Rational(9,4)]`
- `equacao` — expressão `Eq(log(z,10), Rational(3,2))`, esperado `[10**Rational(3,2)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - equacao=aprovado
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com definições explícitas de M, I e E, dados completos (magnitudes de A e B) e pedidos claramente segmentados em a), b) e c). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 5/5 — Os itens a) e b) são de aplicação direta, mas o item c) exige generalizar o padrão para qualquer M, verificar uma afirmação e justificar a natureza logarítmica da escala — isso corresponde a 'analisar' na taxonomia de Bloom e a um nível relacional/abstrato estendido na SOLO, pois integra os resultados anteriores numa conclusão estrutural sobre a função.
  - alinhamento_bncc: 5/5 — A questão não se limita a aplicar a definição de log: exige comparar razões de intensidade e energia (variação multiplicativa) e, no item c, demonstrar que essa variação é constante e explicar por que isso caracteriza uma escala logarítmica — atendendo integralmente à EM13MAT305, que pede compreensão e interpretação da variação das grandezas em contexto de abalos sísmicos.
  - distratores: 5/5 — não se aplica (questão discursiva).
  - originalidade: 4/5 — O contexto de terremotos/escala Richter é recorrente em livros didáticos, mas o item c) evita o efeito Topaze ao exigir que o aluno descubra e justifique por si mesmo a invariância do fator multiplicativo, em vez de simplesmente pedir o cálculo de uma razão — isso confere originalidade estrutural, ainda que o tema em si não seja inédito.
