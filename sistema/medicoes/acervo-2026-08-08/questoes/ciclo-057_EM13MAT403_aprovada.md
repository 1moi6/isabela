# Ciclo 057 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo estuda o crescimento de uma cultura de bactérias em laboratório. A quantidade de bactérias na cultura, em milhares, $t$ horas após o início da observação, é dada por $N(t) = 100 \cdot 2^{t/3}$, para $t \geq 0$. Para planejar a coleta de amostras, o biólogo também utiliza uma função que fornece o tempo necessário, em horas, para que a cultura atinja uma quantidade $N$ de bactérias (em milhares): $T(N) = 3 \cdot \log_2\left(\dfrac{N}{100}\right)$, para $N \geq 100$. Analisando o domínio, a imagem e o comportamento de crescimento das duas funções, bem como a relação entre seus gráficos, assinale a alternativa correta.

## Alternativas

- (a) O domínio de $N(t)$ é $[0,+\infty)$ e sua imagem é $[100,+\infty)$; o domínio de $T(N)$ é $[100,+\infty)$ e sua imagem é $[0,+\infty)$. Ambas as funções são crescentes, e seus gráficos são simétricos em relação à reta $y=x$, pois $T$ é a função inversa de $N$.  ← correta
- (b) O domínio de $N(t)$ é $[100,+\infty)$ e sua imagem é $[0,+\infty)$; o domínio de $T(N)$ é $[0,+\infty)$ e sua imagem é $[100,+\infty)$. Ambas as funções são crescentes, e seus gráficos são simétricos em relação à reta $y=x$.
  - *erro representado:* Inverteu domínio e imagem de cada função, confundindo a variável independente com a dependente em cada modelo (achou que o domínio de $N$ deveria ser o conjunto de valores de população, e não de tempo).
- (c) O domínio de $N(t)$ é $[0,+\infty)$ e sua imagem é $[100,+\infty)$; o domínio de $T(N)$ é $[100,+\infty)$ e sua imagem é $[0,+\infty)$. A função $N(t)$ é crescente, mas $T(N)$ é decrescente, pois o logaritmo cresce mais lentamente que a exponencial.
  - *erro representado:* Confundiu 'crescer mais lentamente' (menor taxa de variação) com 'ser decrescente'; na verdade $T(N)$ também é estritamente crescente, apenas com taxa de crescimento menor que a de $N(t)$.
- (d) O domínio de $N(t)$ é $[0,+\infty)$ e sua imagem é $[100,+\infty)$; como toda função logarítmica está definida para qualquer número real, o domínio de $T(N)$ é $\mathbb{R}$, e sua imagem é $[0,+\infty)$. Ambas as funções são crescentes.
  - *erro representado:* Ignorou a condição de existência do logaritmo (o argumento deve ser estritamente positivo, e o contexto exige $N \geq 100$), atribuindo indevidamente domínio real irrestrito a $T(N)$.

## Gabarito

Domínio de $N(t)$: $[0,+\infty)$; Imagem de $N(t)$: $[100,+\infty)$; Domínio de $T(N)$: $[100,+\infty)$; Imagem de $T(N)$: $[0,+\infty)$; ambas crescentes; gráficos simétricos em relação a $y=x$ (funções inversas).

## Resolução

**Passo 1 — Domínio de $N(t)$:** o contexto exige $t \geq 0$ (tempo não pode ser negativo), logo $D(N) = [0,+\infty)$.

**Passo 2 — Imagem de $N(t)$:** em $t=0$, $N(0) = 100 \cdot 2^0 = 100$; como a base $2>1$, $N(t)$ cresce sem limite quando $t \to +\infty$. Logo $Im(N) = [100,+\infty)$.

**Passo 3 — Crescimento de $N(t)$:** como a base da exponencial é $2>1$, $N(t)$ é estritamente crescente em todo o seu domínio.

**Passo 4 — Domínio de $T(N)$:** o problema restringe $N \geq 100$ (tempo para atingir pelo menos a população inicial), o que também garante que o argumento do logaritmo, $N/100$, seja $\geq 1 > 0$. Logo $D(T) = [100,+\infty)$.

**Passo 5 — Imagem de $T(N)$:** em $N=100$, $T(100) = 3\log_2(1) = 0$; quando $N \to +\infty$, $T(N) \to +\infty$. Logo $Im(T) = [0,+\infty)$.

**Passo 6 — Crescimento de $T(N)$:** como $\log_2$ é crescente (base $2>1$) e o fator $3$ é positivo, $T(N)$ é estritamente crescente.

**Passo 7 — Relação entre as funções:** substituindo, $T(N(t)) = 3\log_2\!\big(2^{t/3}\big) = 3\cdot\dfrac{t}{3} = t$, e analogamente $N(T(N))=N$. Logo $T$ é a função inversa de $N$. Por isso, $D(N)=Im(T)=[0,+\infty)$ e $Im(N)=D(T)=[100,+\infty)$, e os gráficos de $N$ e $T$ são simétricos em relação à reta $y=x$.

**Conclusão:** a alternativa correta é a que descreve exatamente essas correspondências de domínio, imagem, crescimento e simetria.

## Formalização verificável

- `funcao` — expressão `100*2**(t/3)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `100*2**(t/3)`, esperado `Interval(100, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`
- `funcao` — expressão `100*2**(t/3)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `3*log(N/100, 2)`, esperado `Interval(100, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `3*log(N/100, 2)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(100, oo)'}`
- `funcao` — expressão `3*log(N/100, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 6 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (imagem de 100*2**(t/3): Interval(100, oo)). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio Interval(100, oo) — restrição de contexto dentro do domínio máximo Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de 3*log(N/100)/log(2): Interval(0, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado define claramente as duas funções, seus contextos (tempo e população), as condições de domínio explicitadas pelo problema (t≥0, N≥100) e o que se pede (comparar domínio, imagem, crescimento e relação gráfica). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver sem informações implícitas.
  - adequacao_nivel: 4/5 — A tarefa exige decompor cada função em suas características (domínio, imagem, crescimento) e depois relacioná-las (inversas, simetria em y=x), o que corresponde a 'analisar' na taxonomia de Bloom e a uma resposta de nível relacional na SOLO. Os distratores exigem que o aluno verifique múltiplas afirmações simultaneamente, não permitindo acerto por checagem isolada de um único dado. Poderia ser ainda mais forte se pedisse justificativa explícita da simetria via composição, mas já está presente na resolução.
  - alinhamento_bncc: 5/5 — Cumpre as três exigências: (1) trata exponencial e logarítmica na mesma questão, articuladas por serem inversas uma da outra dentro do mesmo contexto (crescimento bacteriano); (2) compara explicitamente domínio, imagem e crescimento de ambas; (3) não se limita a calcular valores — a resposta correta exige comparar as quatro características e a relação entre os gráficos, exatamente o que a habilidade EM13MAT403 pede.
  - distratores: 5/5 — Os três distratores representam erros conceituais plausíveis e comuns: troca de domínio/imagem entre as funções, confusão entre 'crescer mais lentamente' e 'ser decrescente', e desconsideração da restrição de existência do logaritmo. Nenhum é absurdo ou trivialmente eliminável sem raciocínio matemático genuíno.
  - originalidade: 4/5 — O contexto de crescimento bacteriano é aplicado e coerente, evitando o exemplo puramente abstrato de livro didático. Não há pistas diretas que entreguem a resposta (efeito Topaze), embora o contexto de crescimento bacteriano com função tempo-para-população seja um cenário relativamente comum em materiais didáticos sobre exponencial/logaritmo, reduzindo um pouco a novidade.
