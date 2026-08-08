# Ciclo 085 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma cultura de bactérias em laboratório cresce de forma exponencial, e a população, em função do tempo $t$ (em horas), é dada por $P(t) = P_0 \cdot 2^{t/4}$, em que $P_0$ é a população inicial. Sabe-se, portanto, que essa população dobra a cada 4 horas. Determine, aproximadamente, quantas horas são necessárias para que a população se torne o triplo da população inicial.

## Alternativas

- (a) $t = 4\log_2 3 \approx 6{,}34$ horas  ← correta
- (b) $t = 6$ horas
  - *erro representado:* Raciocínio linear/proporcional: o estudante assume que, como o fator de crescimento (3) é 1,5 vezes o fator de dobra (2), o tempo também deveria ser 1,5 vezes o tempo de dobra, calculando $\frac{3}{2}\times 4 = 6$, tratando o crescimento exponencial como linear.
- (c) $t = 12$ horas
  - *erro representado:* Erro de proporcionalidade direta entre o fator multiplicativo e o tempo: o estudante pensa que, para triplicar (fator 3), basta multiplicar o tempo de dobra por 3, calculando $3 \times 4 = 12$, ignorando a natureza logarítmica da relação entre fator de crescimento e tempo.
- (d) $t = 4\log_3 2 \approx 2{,}52$ horas
  - *erro representado:* Inversão da base e do argumento do logaritmo ao resolver $2^{t/4}=3$: o estudante escreve $t = 4\log_3 2$ em vez de $t = 4\log_2 3$, trocando os papéis das bases na equação exponencial.

## Gabarito

t = 4 log₂3 ≈ 6,34 horas (alternativa a)

## Resolução

Queremos o instante $t$ em que $P(t) = 3P_0$.

Como $P(t) = P_0 \cdot 2^{t/4}$, substituímos:

$$P_0 \cdot 2^{t/4} = 3P_0 \quad \Rightarrow \quad 2^{t/4} = 3$$

Aplicando logaritmo natural (ou de qualquer base) aos dois lados:

$$\frac{t}{4}\ln 2 = \ln 3 \quad \Rightarrow \quad t = 4\cdot \frac{\ln 3}{\ln 2} = 4\log_2 3$$

Calculando numericamente: $\log_2 3 \approx 1{,}585$, logo

$$t \approx 4 \times 1{,}585 \approx 6{,}34 \text{ horas}$$

**Por que não vale o raciocínio linear?** Um erro comum é pensar que, como o fator de crescimento é multiplicativo, o tempo para triplicar seria proporcional ao tempo para dobrar, calculado como $\frac{3}{2}\times 4 = 6$ horas, ou até que triplicar a população levaria o triplo do tempo de dobrar, ou seja, $3\times 4 = 12$ horas. Ambos os raciocínios tratam o crescimento como se fosse linear (aditivo), mas o crescimento é exponencial: o tempo necessário para multiplicar a população por um fator $k$ é dado por $t = 4\log_2 k$, uma relação logarítmica, não linear. Por isso, o valor correto é ligeiramente maior que o tempo de dobrar (4h), mas bem menor que o dobro desse tempo (8h) — de fato, $6{,}34$ h está nesse intervalo, o que confirma a coerência da resposta.

## Formalização verificável

- `equacao` — expressão `Eq(2**(t/4), 3)`, esperado `[4*log(3)/log(2)]`
- `funcao` — expressão `2**(t/4)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `2**(t/4)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (3) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem definido: fórmula explícita, condição inicial e pergunta claras, sem ambiguidade. Dados suficientes para resolução direta.
  - adequacao_nivel: 4/5 — O enunciado em si pede apenas 'aplicar' a equação exponencial (resposta uniestrutural/multiestrutural), coerente com Bloom 'aplicar'. A resolução acrescenta uma discussão sobre por que o raciocínio linear falha, o que é rico, mas essa reflexão não é exigida pelo enunciado nem avaliada pelas alternativas — o aluno só precisa resolver a equação, sem precisar 'interpretar a variação' explicitamente no que é pedido.
  - alinhamento_bncc: 3/5 — O contexto (crescimento bacteriano) é adequado e a equação exponencial é central, mas a habilidade EM13MAT304 exige explicitamente 'compreender e interpretar a variação das grandezas', não apenas calcular um valor de t. O enunciado poderia perguntar, por exemplo, comparar taxas, taxa de crescimento instantânea, ou justificar por que triplicar não é proporcional a dobrar dentro do próprio enunciado (não apenas na resolução). Como está, é essencialmente um exercício de resolução de equação exponencial com contexto de crescimento — atende parcialmente, mas não articula plenamente a interpretação exigida pela habilidade.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: raciocínio proporcional simples (6h), proporcional direto ingênuo (12h) e inversão de base/argumento no logaritmo (2,52h). Nenhum é absurdo ou trivialmente eliminável, todos exigem certo raciocínio para descartar.
  - originalidade: 3/5 — O contexto de crescimento bacteriano com dobra é um clássico recorrente em livros didáticos, pouco inovador. A pergunta sobre 'tempo para triplicar' é uma variação padrão do problema de meia-vida/duplicação, sem elemento significativo novo ou aplicação prática diferenciada. Não há efeito Topaze evidente, mas a originalidade é baixa.
