# Ciclo 037 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma colônia de bactérias em um experimento de laboratório tem seu número de indivíduos, a partir do início da observação, dado por $N(t) = 100 \cdot 2^{t}$, em que $t$ é o tempo em horas ($t \geq 0$) e $N(t)$ é o número de bactérias. Um pesquisador quer saber, ao contrário, quanto tempo é necessário para que a colônia atinja um determinado número $N$ de bactérias, e por isso utiliza a função inversa de $N(t)$, que ele chama de $t(N)$.

a) Determine o domínio e a imagem de $N(t)$, considerando o contexto do experimento.

b) Encontre a expressão de $t(N)$ (a função inversa de $N(t)$) e determine seu domínio e sua imagem.

c) Compare o crescimento das duas funções: as duas são crescentes, mas uma cresce 'cada vez mais rápido' e a outra cresce 'cada vez mais devagar' à medida que a variável aumenta. Identifique qual é qual e justifique observando como varia o incremento de cada função.

d) Explique por que o domínio de $N(t)$ coincide com a imagem de $t(N)$, e a imagem de $N(t)$ coincide com o domínio de $t(N)$, relacionando esse fato com a posição dos gráficos das duas funções no plano cartesiano.

## Gabarito

a) $D_N=[0,+\infty)$, $Im_N=[100,+\infty)$. b) $t(N)=\log_2(N/100)$, com $D_t=[100,+\infty)$, $Im_t=[0,+\infty)$. c) $N(t)$ cresce cada vez mais rápido (convexa); $t(N)$ cresce cada vez mais devagar (côncava). d) Por serem funções inversas, seus gráficos são simétricos em relação à reta $y=x$, o que troca domínio e imagem entre as duas funções.

## Resolução

**a) Domínio e imagem de $N(t) = 100\cdot 2^t$**

Como $t$ representa tempo a partir do início da observação, $t \geq 0$. Logo:
$$D_N = [0, +\infty)$$

Quando $t=0$, $N(0) = 100 \cdot 2^0 = 100$, o menor valor possível. Como $2^t$ é crescente e ilimitada quando $t \to +\infty$, $N(t)$ também cresce sem limite. Logo:
$$Im_N = [100, +\infty)$$

**b) Função inversa $t(N)$**

De $N = 100\cdot 2^t$, isolamos $t$:
$$\frac{N}{100} = 2^t \implies t = \log_2\left(\frac{N}{100}\right)$$

Como funções inversas trocam domínio e imagem entre si:
$$D_t = Im_N = [100, +\infty), \qquad Im_t = D_N = [0, +\infty)$$

(De fato, o menor $N$ possível no experimento é 100, e para $N=100$ temos $t=\log_2(1)=0$, consistente.)

**c) Comparando o crescimento**

Ambas as funções são estritamente crescentes, pois a base $2$ é maior que $1$ tanto na exponencial quanto no logaritmo.

Porém, o **modo** de crescer é diferente. Observe os incrementos de $N(t)$ a cada hora:
- de $t=0$ a $t=1$: $N$ vai de $100$ a $200$ (aumenta 100)
- de $t=1$ a $t=2$: $N$ vai de $200$ a $400$ (aumenta 200)
- de $t=2$ a $t=3$: $N$ vai de $400$ a $800$ (aumenta 400)

Ou seja, o incremento absoluto de $N(t)$ **aumenta** a cada intervalo — a função exponencial cresce cada vez mais rápido (é convexa, sua taxa de variação aumenta).

Já para $t(N)$: cada vez que $N$ **dobra**, $t$ aumenta sempre a mesma quantidade fixa, 1 hora (pois $\log_2(2N/100) - \log_2(N/100) = \log_2 2 = 1$). Mas para produzir esse mesmo aumento de 1 unidade em $t$, é preciso um incremento absoluto de $N$ cada vez maior (de $100\to200$, depois $200\to400$, depois $400\to800$...). Isso significa que, para incrementos iguais de $N$, o aumento de $t$ fica cada vez menor — a função logarítmica cresce cada vez mais devagar (é côncava, sua taxa de variação diminui).

**d) Relação entre domínio e imagem das duas funções**

Como $t(N)$ é a função inversa de $N(t)$, seus gráficos são simétricos em relação à reta $y=x$ no plano cartesiano. Essa simetria troca os eixos: o que era eixo do domínio (horizontal) de uma passa a ser o eixo da imagem (vertical) da outra. Por isso, necessariamente:
$$D_{N} = Im_{t} = [0,+\infty) \qquad \text{e} \qquad Im_{N} = D_{t} = [100,+\infty)$$

Essa é uma propriedade geral de qualquer par de funções inversas, e em particular da relação entre exponencial e logaritmo de mesma base: uma 'desfaz' a outra, e seus papéis de domínio e imagem se invertem.

## Formalização verificável

- `funcao` — expressão `100*2**t`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `100*2**t`, esperado `Interval(100, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`
- `funcao` — expressão `100*2**t`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(N/100, 2)`, esperado `Interval(100, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(N/100, 2)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(100, oo)'}`
- `funcao` — expressão `log(N/100, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 6 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (imagem de 100*2**t: Interval(100, oo)). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio Interval(100, oo) — restrição de contexto dentro do domínio máximo Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(N/100)/log(2): Interval(0, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem segmentado em itens a-d, com dados completos (base 2, N0=100, t≥0) e pedidos explícitos. Não há ambiguidade lexical ou estrutural relevante.
  - adequacao_nivel: 5/5 — Os itens c e d exigem comparação de taxas de variação e justificativa da relação geométrica entre os gráficos (simetria em y=x), o que corresponde a 'analisar' (SOLO relacional/extended abstract), não apenas cálculo pontual. Conteúdo compatível com o Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão trata exponencial e logarítmica no mesmo problema (uma é a inversa da outra), compara explicitamente domínio, imagem e padrão de crescimento (convexidade x concavidade) e articula ambas via a relação de inversão — atendendo integralmente à EM13MAT403, não se limitando a calcular valores isolados.
  - distratores: 5/5 — não se aplica (questão discursiva)
  - originalidade: 4/5 — O contexto de crescimento bacteriano é um clássico recorrente em livros didáticos, reduzindo o ineditismo do cenário. Por outro lado, a forma de conduzir a análise (via incrementos absolutos e simetria gráfica, em vez de fórmulas prontas) evita o efeito Topaze e exige raciocínio genuíno do aluno.
