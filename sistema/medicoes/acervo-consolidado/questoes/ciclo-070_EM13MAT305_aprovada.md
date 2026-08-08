# Ciclo 070 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

A magnitude de um abalo sísmico na escala Richter é definida por $M = \log_{10}\left(\dfrac{I}{I_0}\right)$, em que $I$ é a intensidade da onda sísmica registrada pelo sismógrafo e $I_0$ é uma intensidade de referência fixa, igual para todos os abalos.

Um sismólogo estuda uma situação hipotética em que dois abalos, de magnitudes $M_1$ e $M_2$, ocorrem na mesma falha geológica e suas ondas se sobrepõem exatamente no mesmo instante, de modo que a intensidade total registrada pelo sismógrafo passa a ser a soma das intensidades individuais dos dois abalos, isto é, $I = I_1 + I_2$.

Elabore a expressão geral que forneça a magnitude resultante $M$ em função de $M_1$ e $M_2$ nessa situação e utilize-a para calcular o valor de $M$ quando $M_1 = 5$ e $M_2 = 6$.

Assinale a alternativa que apresenta corretamente o valor de $M$ (aproximado a duas casas decimais).

## Alternativas

- (a) $M \approx 6{,}04$  ← correta
- (b) $M = 11$
  - *erro representado:* Somar diretamente as magnitudes ($M_1+M_2$), tratando a escala Richter como linear em vez de logarítmica.
- (c) $M = 5{,}5$
  - *erro representado:* Calcular a média aritmética das magnitudes, supondo (erroneamente) que a sobreposição de ondas equivale a uma média das magnitudes.
- (d) $M = 6$
  - *erro representado:* Considerar apenas a maior magnitude, assumindo que a contribuição do abalo menor é desprezível e não altera o resultado.

## Gabarito

M ≈ 6,04

## Resolução

**Passo 1 — Expressar as intensidades individuais.**

Da definição $M = \log_{10}(I/I_0)$, isolando $I$: $I = I_0 \cdot 10^{M}$.

Logo:
$$I_1 = I_0 \cdot 10^{M_1}, \qquad I_2 = I_0 \cdot 10^{M_2}$$

**Passo 2 — Somar as intensidades (não as magnitudes).**

Como a onda resultante tem intensidade $I = I_1 + I_2$:
$$I = I_0\left(10^{M_1} + 10^{M_2}\right)$$

**Passo 3 — Elaborar a expressão geral para a magnitude resultante.**

Substituindo em $M = \log_{10}(I/I_0)$:
$$M = \log_{10}\left(10^{M_1} + 10^{M_2}\right)$$

Essa é a expressão geral pedida: ela mostra que magnitudes **não se somam diretamente** quando as intensidades se somam — é necessário somar as intensidades (potências de 10) e só depois aplicar o logaritmo.

**Passo 4 — Aplicar aos valores dados.**

Com $M_1 = 5$ e $M_2 = 6$:
$$M = \log_{10}\left(10^{5} + 10^{6}\right) = \log_{10}(1{,}1 \times 10^{6}) = 6 + \log_{10}(1{,}1)$$

Como $\log_{10}(1{,}1) \approx 0{,}0414$:
$$M \approx 6{,}04$$

**Interpretação da variação:** embora a intensidade total ($1{,}1\times10^6\,I_0$) seja $10\%$ maior do que a intensidade do abalo mais forte sozinho ($10^6\,I_0$), a magnitude aumenta apenas de $6$ para $6{,}04$. Isso evidencia a natureza logarítmica da escala: grandes variações de intensidade correspondem a pequenas variações de magnitude, e vice-versa.

## Formalização verificável

- `equacao` — expressão `Eq(M, log(10**M1 + 10**M2, 10))`, esperado `[log(10**M1 + 10**M2, 10)]`
- `funcao` — expressão `log(x, 10)`, esperado `log(1100000, 10)`, parâmetros `{'consulta': 'valor', 'ponto': '10**5 + 10**6'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem redigido, com dados completos (M_A, M_B, definição da fórmula) e pergunta inequívoca sobre a razão de intensidades. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — A tarefa cognitiva real é isolar I na fórmula, substituir valores e calcular uma razão de potências — isto é 'aplicar' (e no máximo 'analisar' a diferença de comportamento linear vs. exponencial), mas não configura 'criar' na taxonomia de Bloom, que exigiria gerar/produzir algo novo (formular um problema, propor um modelo, sintetizar critérios). Em termos SOLO, a resposta é relacional (integra dois dados numa razão), não estendida abstrata, como o nível 'criar' pressuporia. Há um descompasso claro entre o Bloom declarado e o processo cognitivo exigido.
  - alinhamento_bncc: 4/5 — A questão cumpre as três exigências específicas listadas: usa função logarítmica, contextualiza com abalos sísmicos, e coloca a variação (diferença aditiva de magnitude vs. fator multiplicativo de intensidade) como núcleo do problema, não como aplicação mecânica da definição. Falta, porém, o componente de 'elaborar' problemas presente no texto da habilidade EM13MAT305, já que a questão apenas resolve — isso não é penalizado pelas exigências específicas, mas limita a nota máxima.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos plausíveis e distintos: (i) tratar a escala como linear (Δ=2,5), (ii) confundir potenciação com multiplicação (10×2,5), (iii) inverter a razão das intensidades. Nenhum é absurdo ou trivialmente eliminável; todos exigem que o estudante realmente compreenda a relação log/exponencial para descartá-los.
  - originalidade: 3/5 — O contexto da escala Richter para exemplificar logaritmos é um dos exemplos mais recorrentes em livros didáticos e already conhecido pelos estudantes como 'o exemplo clássico de log'. A pergunta específica ('quantas vezes maior') também é um formato padrão. Não há efeito Topaze evidente no enunciado, mas a originalidade do contexto é baixa.
  - *sugestões:* 1) Ajustar o nível de Bloom declarado para 'aplicar' ou 'analisar', que é o que a questão de fato demanda; OU 2) reformular a questão para efetivamente exigir 'criar': por exemplo, pedir ao aluno que elabore uma expressão geral que relacione a razão de intensidades a uma diferença arbitrária de magnitude ΔM, ou que proponha e justifique um novo cenário (ex.: um terremoto C tal que sua intensidade seja k vezes a de A) e calcule a magnitude resultante, envolvendo síntese/generalização e não apenas substituição numérica. 3) Para aumentar a originalidade, considerar variar o contexto (pH, radioatividade, decibéis) ou apresentar o problema de forma menos padronizada, evitando o formato 'clássico de livro didático' da escala Richter com pergunta direta de razão de intensidades.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar o nível de Bloom declarado para 'aplicar' ou 'analisar', que é o que a questão de fato demanda; OU 2) reformular a questão para efetivamente exigir 'criar': por exemplo, pedir ao aluno que elabore uma expressão geral que relacione a razão de intensidades a uma diferença arbitrária de magnitude ΔM, ou que proponha e justifique um novo cenário (ex.: um terremoto C tal que sua intensidade seja k vezes a de A) e calcule a magnitude resultante, envolvendo síntese/generalização e não apenas substituição numérica. 3) Para aumentar a originalidade, considerar variar o contexto (pH, radioatividade, decibéis) ou apresentar o problema de forma menos padronizada, evitando o formato 'clássico de livro didático' da escala Richter com pergunta direta de razão de intensidades.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (f(1100000) = log(11)/log(10) + 5).
  - equacao=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado define a escala Richter, a condição de sobreposição de ondas e pede duas coisas (elaborar a expressão geral e calcular M). Os dados são completos e não há ambiguidade lexical. Uma pequena tensão fica entre o comando 'elabore a expressão geral' e o formato final de resposta (múltipla escolha apenas com valores numéricos), o que pode confundir o aluno sobre o que efetivamente deve produzir por escrito.
  - adequacao_nivel: 3/5 — O processo descrito (deduzir I=I0·10^M, somar intensidades, reaplicar o log) é de fato um processo de síntese/criação de um modelo, compatível com 'criar'. Contudo, como o formato é múltipla escolha e as alternativas trazem apenas valores numéricos de M, o aluno pode chegar à resposta calculando diretamente log10(10^5+10^6) sem nunca formalizar a expressão geral M=log10(10^M1+10^M2). Isso rebaixa o nível cognitivo efetivamente cobrado para algo mais próximo de 'aplicar/analisar', gerando incoerência entre o Bloom declarado (criar) e o SOLO da resposta esperada (relacional, não abstrato-estendido).
  - alinhamento_bncc: 4/5 — A questão envolve função logarítmica em contexto realista (abalos sísmicos) e exige mais do que aplicar a definição — é preciso converter magnitude em intensidade, somar intensidades e reconverter, entendendo por que magnitudes não se somam linearmente. Isso atende bem à habilidade EM13MAT305. O único ponto fraco é que a 'interpretação da variação das grandezas' (o fato de M crescer pouco mesmo com 10x mais intensidade) fica relegada à resolução/gabarito, sem ser explicitamente cobrada como parte da resposta a ser assinalada — o aluno pode acertar sem verbalizar essa interpretação.
  - distratores: 5/5 — Os quatro distratores representam erros conceituais plausíveis e distintos: soma direta das magnitudes (11), média aritmética (5,5) e desconsideração do abalo menor (6). Nenhum é absurdo ou trivialmente eliminável, e cobrem bem os equívocos típicos de confundir escala logarítmica com escala linear.
  - originalidade: 4/5 — Embora o tema 'escala Richter' seja recorrente em livros didáticos, o cenário de sobreposição simultânea de dois abalos e a exigência de deduzir a fórmula de combinação de magnitudes (em vez de apenas calcular M a partir de I/I0) é uma variação criativa e não uma cópia mecânica de problema clássico. Não há pistas que entreguem a solução (efeito Topaze), pois o aluno precisa descobrir por si que deve operar com as intensidades, não com as magnitudes.
