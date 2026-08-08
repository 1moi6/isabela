# Ciclo 054 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo monitora o crescimento de uma cultura de bactérias em laboratório. No início da observação (t = 0), há 400 bactérias, e a cultura cresce de modo que a população dobra a cada 6 horas. A população N(t), em número de bactérias, t horas após o início da observação, é dada por N(t) = 400 · 2^(t/6). Considerando essa lei de crescimento, qual das afirmações a seguir compara corretamente o crescimento da população entre t = 0h e t = 6h com o crescimento entre t = 12h e t = 18h?

## Alternativas

- (a) Em ambos os intervalos a população dobra (fator multiplicativo 2), mas o aumento absoluto de bactérias é maior no segundo intervalo: 400 entre 0h e 6h, contra 1600 entre 12h e 18h, pois a mesma taxa de crescimento multiplica quantidades cada vez maiores.  ← correta
- (b) Em ambos os intervalos a população aumenta exatamente 400 bactérias, já que a taxa de crescimento de 2 vezes a cada 6 horas corresponde a um acréscimo fixo de indivíduos por hora.
  - *erro representado:* Confundir crescimento exponencial com crescimento linear, supondo que a taxa constante implica incremento absoluto constante em vez de fator multiplicativo constante.
- (c) No segundo intervalo (12h a 18h) a população cresce mais do que o dobro, pois quanto mais tempo passa, maior fica o fator de multiplicação aplicado a cada período de 6 horas.
  - *erro representado:* Achar que a razão (taxa percentual) de crescimento aumenta com o tempo, quando na verdade ela é constante em qualquer intervalo de mesma duração numa função exponencial.
- (d) A população dobra apenas uma vez em todo o período analisado, atingindo 1600 bactérias em 18 horas, pois o enunciado indica que o dobro ocorre a cada 12 horas, não a cada 6.
  - *erro representado:* Erro de leitura do período de duplicação, interpretando 'dobra a cada 6 horas' como 'dobra a cada 12 horas'.

## Gabarito

Em ambos os intervalos a população dobra (fator 2), mas o aumento absoluto é de 400 bactérias no primeiro intervalo e de 1600 bactérias no segundo, pois a mesma razão de crescimento multiplica quantidades cada vez maiores.

## Resolução

**Passo 1 — Calcular a população nos quatro instantes pedidos.**

$N(0) = 400 \cdot 2^{0/6} = 400 \cdot 1 = 400$

$N(6) = 400 \cdot 2^{6/6} = 400 \cdot 2 = 800$

$N(12) = 400 \cdot 2^{12/6} = 400 \cdot 4 = 1600$

$N(18) = 400 \cdot 2^{18/6} = 400 \cdot 8 = 3200$

**Passo 2 — Analisar o fator multiplicativo em cada intervalo de 6 horas.**

Entre 0h e 6h: $\dfrac{N(6)}{N(0)} = \dfrac{800}{400} = 2$.

Entre 12h e 18h: $\dfrac{N(18)}{N(12)} = \dfrac{3200}{1600} = 2$.

Como a função é exponencial com base fixa, todo intervalo de 6 horas multiplica a população pelo mesmo fator (2), **independentemente do instante em que ele começa** — essa é a característica que define o crescimento exponencial (taxa percentual constante).

**Passo 3 — Analisar o aumento absoluto em cada intervalo.**

Entre 0h e 6h: $N(6) - N(0) = 800 - 400 = 400$ bactérias.

Entre 12h e 18h: $N(18) - N(12) = 3200 - 1600 = 1600$ bactérias.

Embora o fator multiplicativo seja o mesmo (2), o aumento absoluto é diferente: como o segundo intervalo parte de uma população maior, a mesma multiplicação por 2 produz um acréscimo absoluto quatro vezes maior (1600 contra 400).

**Conclusão:** em ambos os intervalos a população dobra (razão constante = 2), mas o número de bactérias adicionadas é bem maior no segundo intervalo, pois o crescimento exponencial aplica a mesma taxa percentual sobre quantidades cada vez maiores.

## Formalização verificável

- `funcao` — expressão `400*2**(t/6)`, esperado `400`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `400*2**(t/6)`, esperado `800`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `funcao` — expressão `400*2**(t/6)`, esperado `1600`, parâmetros `{'consulta': 'valor', 'ponto': '12'}`
- `funcao` — expressão `400*2**(t/6)`, esperado `3200`, parâmetros `{'consulta': 'valor', 'ponto': '18'}`
- `funcao` — expressão `400*2**(t/6)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(0) = 400). | (2) aprovado: Gabarito confirmado (f(6) = 800). | (3) aprovado: Gabarito confirmado (f(12) = 1600). | (4) aprovado: Gabarito confirmado (f(18) = 3200). | (5) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente os dados (N0=400, duplicação a cada 6h, função explícita) e a pergunta (comparar o crescimento entre 0-6h e 12-18h). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A resolução exige calcular quatro valores e depois comparar fator multiplicativo com incremento absoluto — isso já se aproxima de 'analisar' na taxonomia de Bloom e de estrutura relacional no SOLO, um pouco além do 'aplicar' declarado. Ainda assim, é uma extensão natural da aplicação direta da fórmula, compatível com Ensino Médio e com dificuldade média.
  - alinhamento_bncc: 5/5 — Atende plenamente à EM13MAT304: não basta calcular valores, a questão obriga o aluno a interpretar a variação (razão constante vs. acréscimo absoluto crescente), central ao entendimento de crescimento exponencial. O contexto de crescimento bacteriano é adequado e realista.
  - distratores: 5/5 — Os três distratores representam erros conceituais plausíveis e distintos: confundir exponencial com linear, achar que a taxa percentual aumenta com o tempo, e erro de leitura do período de duplicação. Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 3/5 — O contexto de bactérias que dobram de população é um clássico recorrente em livros didáticos sobre função exponencial, reduzindo a originalidade contextual. Por outro lado, a pergunta comparativa (fator multiplicativo constante vs. incremento absoluto variável) foge do formato mecânico de 'calcule N(t)', mitigando parcialmente esse ponto.
