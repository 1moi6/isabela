# Ciclo 075 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em um laboratório, a população de uma colônia de bactérias é modelada por $N(t) = N_0 \cdot 2^{t/2}$, em que $N_0$ é a população inicial (em número de indivíduos) e $t$ é o tempo decorrido, em horas. Um pesquisador quer entender como a população se transforma quando o tempo avança 6 horas a partir de um instante qualquer $t$. Qual é o fator pelo qual a população fica multiplicada ao passar de $N(t)$ para $N(t+6)$, e essa razão depende do valor de $t$ escolhido?

## Alternativas

- (a) O fator é 8, e essa razão é a mesma para qualquer valor de $t$.  ← correta
- (b) O fator é 6, pois em 6 horas a população aumenta 6 vezes o valor inicial em cada intervalo de 2 horas.
  - *erro representado:* Confunde crescimento multiplicativo (exponencial) com crescimento aditivo, somando os fatores de crescimento (2+2+2=6) em vez de multiplicá-los (2×2×2=8).
- (c) O fator é 3, pois basta calcular o expoente $6/2$ e esse já é o resultado da razão entre as populações.
  - *erro representado:* Calcula corretamente o valor do expoente (3) mas esquece de elevar a base 2 a essa potência, confundindo o expoente com o próprio fator multiplicativo.
- (d) O fator é 64, e ele varia conforme o valor de $t$ considerado.
  - *erro representado:* Erra a simplificação do expoente ao dividir, calculando $2^{6}$ em vez de $2^{6/2}$, e ainda supõe erroneamente que a razão dependeria de $t$.

## Gabarito

O fator é 8, e essa razão é a mesma para qualquer valor de $t$ (alternativa correta: 8, independe de $t$).

## Resolução

Escrevemos a razão entre as populações nos instantes $t+6$ e $t$:

$$\frac{N(t+6)}{N(t)} = \frac{N_0 \cdot 2^{(t+6)/2}}{N_0 \cdot 2^{t/2}}$$

O fator $N_0$ se cancela. Usando a propriedade de potências $a^{m}/a^{n} = a^{m-n}$:

$$\frac{N(t+6)}{N(t)} = 2^{\frac{t+6}{2} - \frac{t}{2}} = 2^{\frac{6}{2}} = 2^3 = 8$$

Como o termo $t$ desapareceu no cálculo do expoente, o resultado **não depende do instante $t$ escolhido**: em qualquer intervalo de 6 horas, a população fica sempre multiplicada por 8. Essa é a característica essencial do crescimento exponencial: a taxa (fator) de variação relativa é constante para intervalos de tempo iguais, independentemente do ponto de partida.

Portanto, o fator é $8$, e ele é o mesmo para qualquer $t$.

## Formalização verificável

- `funcao` — expressão `2**((t+6)/2)/2**(t/2)`, esperado `8`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `2**((t+6)/2)/2**(t/2)`, esperado `8`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(0) = 8). | (2) aprovado: Gabarito confirmado (f(5) = 8).
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a função, o que é dado (N0, t) e o que se pede (fator multiplicativo e sua dependência de t). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — A questão exige mais do que cálculo mecânico: pede que o aluno interprete por que a razão independe de t, o que se aproxima de 'analisar'. Porém, a resolução é puramente algébrica e direta (uma única simplificação de potências), sem exigir comparação entre múltiplas relações ou generalização a partir de dados variados, o que é mais típico de SOLO multiestrutural/relacional inicial do que de uma análise plena. A classificação como 'fácil' reforça essa tensão com o nível Bloom declarado.
  - alinhamento_bncc: 4/5 — O contexto (crescimento de bactérias) é adequado à habilidade EM13MAT304. A questão vai além do cálculo puro ao perguntar explicitamente se a razão depende de t, atendendo à exigência de 'compreender e interpretar a variação das grandezas'. Poderia articular ainda mais a interpretação (ex.: pedir uma justificativa qualitativa sobre taxa de crescimento constante) para atingir nota máxima.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e comuns: confusão aditiva vs. multiplicativa (6 em vez de 8), esquecimento de elevar a base ao expoente (3 em vez de 8), e erro na simplificação da potência com suposição incorreta de dependência de t (64). Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 3/5 — O contexto de crescimento bacteriano com modelo exponencial é um clássico recorrente em livros didáticos, e a estrutura de pedir a razão N(t+6)/N(t) é uma abordagem previsível. A pergunta sobre a dependência de t adiciona algum valor interpretativo, mas o enunciado ainda segue um roteiro bastante convencional, sem elementos de contexto verdadeiramente significativos ou inesperados.
