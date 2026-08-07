# Ciclo 004 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Um biólogo estuda o crescimento de uma cultura de bactérias em laboratório. O número de bactérias na cultura, em milhares, t horas após o início da observação, é modelado pela função exponencial $N(t) = 2^t$. Para planejar os experimentos, o biólogo também usa a função $T(N) = \log_2(N)$, que indica quantas horas são necessárias para que a cultura atinja uma quantidade $N$ (em milhares) de bactérias.

Ao plotar as duas funções no mesmo plano cartesiano usando um software gráfico, o biólogo observou que as curvas de $N(t)$ e $T(N)$ são simétricas em relação à reta $y = x$.

Com base nessas informações, responda:

a) Determine o domínio e a imagem de $N(t) = 2^t$ e de $T(N) = \log_2(N)$.

b) Classifique cada uma das funções quanto ao crescimento (crescente ou decrescente), justificando com base na definição de cada tipo de função.

c) Explique, matematicamente, por que os gráficos dessas duas funções são simétricos em relação à reta $y = x$, relacionando as características (domínio, imagem e crescimento) de uma função com as da outra.

## Gabarito

N(t)=2^t: domínio ℝ, imagem (0,+∞), crescente. T(N)=log₂(N): domínio (0,+∞), imagem ℝ, crescente. As funções são inversas entre si (por isso domínio e imagem se invertem), o que explica a simetria dos gráficos em relação à reta y = x.

## Resolução

**a) Domínio e imagem**

Para a função exponencial $N(t) = 2^t$:
- O expoente $t$ pode assumir qualquer número real, logo o domínio é $D(N) = \mathbb{R}$.
- Como toda potência de base positiva (aqui $2$) e diferente de $1$ é sempre positiva, a imagem é $Im(N) = (0, +\infty)$.

Para a função logarítmica $T(N) = \log_2(N)$:
- O logaritmo só está definido para argumentos positivos, logo o domínio é $D(T) = (0, +\infty)$.
- Como o logaritmo pode assumir qualquer valor real (positivo, negativo ou zero, dependendo de $N$), a imagem é $Im(T) = \mathbb{R}$.

Observe que o domínio de $N(t)$ é igual à imagem de $T(N)$, e o domínio de $T(N)$ é igual à imagem de $N(t)$.

**b) Crescimento**

A função $N(t) = 2^t$ tem base $2 > 1$, portanto é **crescente**: à medida que $t$ aumenta, $N(t)$ aumenta.

A função $T(N) = \log_2(N)$ também tem base $2 > 1$, portanto é **crescente**: à medida que $N$ aumenta, $T(N)$ aumenta.

Ambas as funções são crescentes em todo o seu domínio.

**c) Relação entre as funções e simetria em relação a $y = x$**

As funções $N(t) = 2^t$ e $T(N) = \log_2(N)$ são **funções inversas uma da outra**: aplicar $T$ ao resultado de $N$ devolve o valor original, isto é, $T(N(t)) = \log_2(2^t) = t$, e analogamente $N(T(N)) = 2^{\log_2(N)} = N$.

De modo geral, o gráfico de uma função e o gráfico de sua função inversa são sempre simétricos em relação à reta $y = x$, pois se o ponto $(a,b)$ pertence ao gráfico de $N$ (ou seja, $N(a) = b$), então o ponto $(b,a)$ pertence ao gráfico de $T$ (pois $T(b) = a$) — e esses dois pontos são simétricos em relação à reta $y=x$.

Essa relação de inversão também explica por que domínio e imagem se trocam entre as duas funções: o domínio de uma é a imagem da outra. Além disso, como a base $2$ é maior que $1$ em ambos os casos, as duas funções preservam o caráter crescente — uma função inversa de uma função crescente é sempre crescente.

## Formalização verificável

- `funcao` — expressão `2**t`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2**t`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `2**t`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(N, 2)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(N, 2)`, esperado `S.Reals`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `log(N, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 5 de 6 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**t: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**t. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(N)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(N)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente o contexto, as funções e as três tarefas (a, b, c). Os dados são suficientes e não há ambiguidade lexical ou estrutural; o aluno sabe exatamente o que é pedido em cada item.
  - adequacao_nivel: 3/5 — Os itens (a) e (b) exigem apenas identificar/aplicar definições (nível 'lembrar/entender', resposta unistrutural ou multiestrutural). Já o item (c) pede uma resposta relacional — articular domínio, imagem e crescimento para justificar a simetria dos gráficos — o que corresponde a um processo mais próximo de 'analisar' na taxonomia de Bloom e a uma estrutura SOLO relacional, superior ao nível 'entender' declarado na especificação. Há, portanto, um descompasso entre o nível cognitivo nominal e o efetivamente demandado pelo item mais elaborado.
  - alinhamento_bncc: 5/5 — A questão trata exponencial e logarítmica de forma articulada em um único problema, exige comparação explícita das três características fundamentais (domínio, imagem, crescimento) e pede que o aluno relacione as duas funções (inversas, simetria em y=x), cumprindo integralmente o que a habilidade EM13MAT403 demanda — não se limita a calcular valores isolados.
  - distratores: 5/5 — Não se aplica: questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto biológico (crescimento bacteriano) é mais significativo que o clássico 'juros compostos', mas o enunciado já informa que os gráficos são simétricos em relação a y=x antes de pedir a explicação no item (c), o que configura um leve efeito Topaze — entrega parte da conclusão que o aluno deveria descobrir ou justificar de forma mais autônoma.
