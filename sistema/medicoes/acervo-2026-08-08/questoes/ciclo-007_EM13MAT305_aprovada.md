# Ciclo 007 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A magnitude $M$ de um terremoto, na escala Richter, é modelada pela função logarítmica $$M(A) = \log_{10}\left(\dfrac{A}{A_0}\right),$$ em que $A$ é a amplitude máxima das ondas sísmicas registradas por um sismógrafo (em milímetros) e $A_0 = 1\text{ mm}$ é uma amplitude de referência padrão.

Em uma região sísmica, um primeiro terremoto foi registrado com magnitude $M_1 = 5{,}0$. Algumas semanas depois, um segundo terremoto na mesma região foi registrado com magnitude $M_2 = 7{,}5$.

a) Calcule a razão $\dfrac{A_2}{A_1}$ entre a amplitude do segundo terremoto e a amplitude do primeiro.

b) Um colega afirmou: "a diferença de magnitude entre os dois terremotos é de apenas 2,5 pontos, então o segundo terremoto deve ter uma amplitude só um pouco maior que o dobro da do primeiro". Usando o resultado do item (a), explique por que essa afirmação está incorreta, relacionando a variação aditiva na escala Richter com a variação multiplicativa na amplitude real das ondas.

c) Um terceiro terremoto na mesma região apresentou amplitude igual ao dobro da amplitude do segundo terremoto ($A_3 = 2A_2$). Determine a magnitude $M_3$ desse terceiro terremoto, com uma casa decimal.

## Gabarito

a) $A_2/A_1 = 10^{2{,}5} \approx 316{,}2$; b) o aumento de 2,5 pontos corresponde a multiplicar a amplitude por $10^{2{,}5}\approx 316$, não a dobrar — a escala é logarítmica, não linear, então pequenas variações na magnitude representam variações multiplicativas enormes na amplitude; c) $M_3 = \log_{10}(2) + 7{,}5 \approx 7{,}8$.

## Resolução

**Item (a): razão entre amplitudes**

Da definição da função, isolamos $A$ em função de $M$:
$$M = \log_{10}\left(\frac{A}{A_0}\right) \iff \frac{A}{A_0} = 10^{M}$$

Com $A_0 = 1$:
$$A_1 = 10^{5{,}0}, \qquad A_2 = 10^{7{,}5}$$

Logo,
$$\frac{A_2}{A_1} = \frac{10^{7{,}5}}{10^{5{,}0}} = 10^{7{,}5-5{,}0} = 10^{2{,}5} \approx 316{,}2$$

**Item (b): interpretação da variação**

O erro do colega é tratar a escala Richter como uma escala linear (proporcional), quando na verdade ela é logarítmica. Uma variação **aditiva** de $\Delta M = 2{,}5$ na magnitude corresponde a uma variação **multiplicativa** de $10^{\Delta M} = 10^{2{,}5} \approx 316$ vezes na amplitude real das ondas, como calculado no item (a). Ou seja, cada acréscimo de 1 unidade na magnitude multiplica a amplitude por 10; um acréscimo de apenas 2,5 unidades já multiplica a amplitude por mais de 300 vezes — muito mais do que o "dobro" sugerido pelo colega. Isso mostra que pequenas diferenças na escala Richter escondem variações físicas enormes na energia liberada e na amplitude das ondas sísmicas.

**Item (c): magnitude do terceiro terremoto**

Como $A_3 = 2A_2$:
$$M_3 = \log_{10}\left(\frac{2A_2}{A_0}\right) = \log_{10}(2) + \log_{10}\left(\frac{A_2}{A_0}\right) = \log_{10}(2) + M_2$$

Substituindo $M_2 = 7{,}5$ e $\log_{10}(2) \approx 0{,}301$:
$$M_3 \approx 0{,}301 + 7{,}5 = 7{,}801 \approx 7{,}8$$

## Formalização verificável

- `funcao` — expressão `log(x, 10)`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '10**5'}`
- `funcao` — expressão `log(x, 10)`, esperado `Rational(15,2)`, parâmetros `{'consulta': 'valor', 'ponto': '10**(Rational(15,2))'}`
- `funcao` — expressão `log(x, 10)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(x, 10**(Rational(5,2)))`, esperado `[10**(Rational(5,2))]`
- `equacao` — expressão `Eq(x, log(2,10) + Rational(15,2))`, esperado `[log(2,10) + Rational(15,2)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(100000) = 5). | (2) aprovado: Gabarito confirmado (f(10000000*sqrt(10)) = 15/2). | (3) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (5) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a função, as variáveis e a constante de referência, e cada item tem um pedido bem delimitado. Não há ambiguidade lexical ou estrutural; todos os dados necessários (M1, M2, A0) estão explícitos.
  - adequacao_nivel: 4/5 — O item (b) exige comparar a variação aditiva na escala com a variação multiplicativa na amplitude e explicar por que a intuição linear falha — isso é coerente com o nível 'analisar' e com uma resposta relacional (SOLO). Já os itens (a) e (c) são majoritariamente aplicativos (isolar A ou M na fórmula), o que reduz um pouco o peso analítico do conjunto, mas a articulação entre eles sustenta o nível declarado.
  - alinhamento_bncc: 5/5 — A questão não se limita a aplicar a definição de logaritmo: o item (b) coloca a interpretação da variação (aditiva vs. multiplicativa) como objeto central da tarefa, exigindo justificativa conceitual, não apenas cálculo. O contexto de abalos sísmicos é um dos exemplos citados na própria habilidade, e os três itens formam uma progressão coesa (calcular, interpretar, aplicar de volta), articulando o tema em vez de justapor subtarefas soltas.
  - distratores: 5/5 — não se aplica (questão discursiva).
  - originalidade: 4/5 — O contexto da escala Richter é um clássico dos livros didáticos sobre logaritmos, mas o elaborador evita o 'efeito Topaze' ao inserir a afirmação equivocada de um colega no item (b), forçando o estudante a construir a refutação com base em raciocínio próprio, em vez de seguir passos guiados. Ainda assim, o cenário em si é pouco inovador frente a outras aplicações possíveis (pH, radioatividade, finanças).
