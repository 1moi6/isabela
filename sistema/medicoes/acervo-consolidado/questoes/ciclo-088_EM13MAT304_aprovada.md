# Ciclo 088 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo monitora duas culturas de microrganismos mantidas em condições ideais de crescimento.

- A cultura A começa com uma quantidade $A_0$ de microrganismos, e essa quantidade dobra a cada 2 horas.
- A cultura B começa com o quádruplo da quantidade inicial da cultura A, ou seja, com $4A_0$ microrganismos, e essa quantidade dobra a cada 6 horas.

Sabendo que as duas populações crescem de forma exponencial desde o início da observação, determine depois de quantas horas as duas culturas terão exatamente a mesma quantidade de microrganismos.

## Alternativas

- (a) 6 horas  ← correta
- (b) 3 horas
  - *erro representado:* Interpretou 'o quádruplo' como 'o dobro', usando $B_0 = 2A_0$ em vez de $4A_0$, o que altera o termo constante da equação de expoentes.
- (c) 8 horas
  - *erro representado:* Erro no cálculo da diferença de frações dos períodos: calculou $\frac{1}{2} - \frac{1}{6} = \frac{1}{4}$ em vez de $\frac{1}{3}$.
- (d) 4 horas
  - *erro representado:* Assumiu, sem montar a equação exponencial, que o instante de igualdade é simplesmente a diferença entre os períodos de duplicação (6 − 2 = 4 horas).

## Gabarito

6 horas

## Resolução

**Modelando as populações**

Como a cultura A dobra a cada 2 horas, sua população no instante $t$ (em horas) é
$$P_A(t) = A_0 \cdot 2^{t/2}.$$

Como a cultura B começa com $4A_0$ e dobra a cada 6 horas,
$$P_B(t) = 4A_0 \cdot 2^{t/6}.$$

**Interpretando a situação**

No instante $t=0$, $P_B(0)=4A_0 > A_0 = P_A(0)$: a cultura B começa muito maior. Porém A cresce mais rapidamente (seu tempo de duplicação é menor), então a diferença entre as populações vai diminuindo até que, em algum instante, elas se igualam — e depois disso A ultrapassa B. É esse instante que queremos encontrar.

**Montando a equação**

$$A_0 \cdot 2^{t/2} = 4A_0 \cdot 2^{t/6}.$$

Como $A_0 > 0$, podemos cancelá-lo:
$$2^{t/2} = 4 \cdot 2^{t/6}.$$

Escrevendo $4 = 2^2$ e usando a propriedade de produto de potências de mesma base:
$$2^{t/2} = 2^{2 + t/6}.$$

**Igualando os expoentes**

Como as bases são iguais (e a função exponencial é injetora), os expoentes devem ser iguais:
$$\frac{t}{2} = 2 + \frac{t}{6}.$$

Multiplicando tudo por 6:
$$3t = 12 + t \implies 2t = 12 \implies t = 6.$$

**Verificação**

$P_A(6) = A_0 \cdot 2^{3} = 8A_0$.

$P_B(6) = 4A_0 \cdot 2^{1} = 8A_0$.

As populações coincidem em $8A_0$, confirmando que $t = 6$ horas é o instante correto.

## Formalização verificável

- `equacao` — expressão `Eq(A0*2**(t/2), 4*A0*2**(t/6))`, esperado `[6]`, parâmetros `{'A0': 'symbol positivo, cancelado na resolução'}`
- `funcao` — expressão `2**(t/2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `4*2**(t/6)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado define claramente as duas populações, seus valores iniciais e taxas de crescimento, e a pergunta ('depois de quantas horas') é inequívoca. Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver o problema.
  - adequacao_nivel: 4/5 — O processo exigido (modelar duas funções exponenciais, igualá-las e resolver a equação) é compatível com 'aplicar': o aluno usa procedimentos conhecidos (potências, propriedades de exponenciais) em uma situação nova. A estrutura de resposta é relacional (SOLO), pois exige combinar duas relações (A0 vs 4A0, períodos 2h vs 6h) em uma única equação — coerente com o nível declarado, embora um pouco próximo de 'analisar' pela necessidade de comparar taxas de crescimento.
  - alinhamento_bncc: 4/5 — O contexto de crescimento de microrganismos é realista e atende à habilidade EM13MAT304. A questão exige compreensão da variação das grandezas (perceber que A cresce mais rápido apesar de começar menor, e quantificar quando as curvas se cruzam), não apenas cálculo mecânico. Poderia reforçar ainda mais a interpretação explícita da variação relativa (ex.: pedir que o aluno justifique por que as populações se cruzam), mas o requisito é satisfeito.
  - distratores: 5/5 — Cada distrator representa um erro sistemático plausível: confundir 'quádruplo' com 'dobro' (3h), erro aritmético na subtração de frações dos períodos (8h), e a suposição ingênua de subtrair diretamente os períodos de duplicação (4h). Nenhum é absurdo ou trivialmente eliminável, exigindo verificação cuidadosa do aluno.
  - originalidade: 3/5 — O tema (duas populações com taxas de crescimento diferentes que se cruzam) é uma variação comum de problemas de exponencial em livros didáticos, ainda que bem construída com valores não triviais (4A0, períodos 2h e 6h). Falta um elemento mais distintivo de contexto ou uma pergunta que vá além do cálculo direto (ex.: pedir justificativa qualitativa antes do cálculo) para evitar o padrão clássico de 'iguale as exponenciais'.
