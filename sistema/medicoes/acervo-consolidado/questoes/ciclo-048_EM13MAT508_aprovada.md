# Ciclo 048 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere a progressão geométrica $(a_n)$, com $n \in \mathbb{N}^{*}$ (ou seja, $n = 1, 2, 3, \dots$), definida por $a_1 = 4$ e razão $q = 2$.

a) Determine a lei de uma função exponencial $f:\mathbb{R}\to\mathbb{R}$ tal que $f(n) = a_n$ para todo $n \in \mathbb{N}^{*}$, explicitando como o primeiro termo e a razão da PG se tornam os parâmetros dessa função.

b) Compare os domínios de $(a_n)$ e de $f$, explicando por que a progressão pode ser vista como a restrição da função $f$ a um subconjunto discreto de $\mathbb{R}$.

c) Determine o valor real de $x$ para o qual $f(x) = 24$. Em seguida, usando o domínio da PG, decida (com justificativa) se existe algum termo $a_n$ da progressão igual a 24.

## Gabarito

a) $f(x) = 4\cdot 2^{x-1}$ (equivalente a $2^{x+1}$), com $a_1=4$ e $q=2$ tornando-se, respectivamente, o valor inicial e a base da exponencial. b) $(a_n)$ tem domínio discreto $\mathbb{N}^{*}$ e é a restrição de $f$, que tem domínio contínuo $\mathbb{R}$, ao conjunto $\mathbb{N}^{*}$. c) $x=\log_2 12\approx 3{,}585$, que não é natural; logo não existe termo da PG igual a 24 (situa-se entre $a_3=16$ e $a_4=32$).

## Resolução

**a) Lei da função exponencial**

O termo geral da PG é $a_n = a_1 \cdot q^{\,n-1} = 4\cdot 2^{\,n-1}$.

Para obter uma função definida em todo $\mathbb{R}$ que coincida com $a_n$ quando $x=n$ é natural, basta trocar $n$ por uma variável real $x$, mantendo o primeiro termo como o valor em $x=1$ e a razão como a base da potência:
$$f(x) = 4\cdot 2^{\,x-1}.$$
Os parâmetros de $f$ são exatamente os da PG: $a_1=4$ é o valor de $f$ em $x=1$, e $q=2$ é a base exponencial (a razão de crescimento por unidade de $x$).

**b) Comparação dos domínios**

A sequência $(a_n)$ só está definida para $n \in \mathbb{N}^{*} = \{1,2,3,\dots\}$, um conjunto **discreto**. Já a função $f(x)=4\cdot2^{x-1}$ está definida para **todo** $x \in \mathbb{R}$, formando um conjunto contínuo. Como $f(n) = 4\cdot 2^{n-1} = a_n$ para cada $n\in\mathbb{N}^{*}$, a progressão geométrica é exatamente a restrição de $f$ ao subconjunto discreto $\mathbb{N}^{*}\subset\mathbb{R}$: os pontos do gráfico de $(a_n)$ são pontos isolados sobre a curva contínua de $f$.

**c) Resolvendo $f(x)=24$**

$$4\cdot 2^{x-1} = 24 \implies 2^{x-1} = 6 \implies x - 1 = \log_2 6 \implies x = 1 + \log_2 6.$$

Como $1+\log_2 6 = \log_2 2 + \log_2 6 = \log_2 12$, temos
$$x = \log_2 12 \approx 3{,}585.$$

Esse valor não é um número natural. Como o domínio da PG é $\mathbb{N}^{*}$ (apenas os inteiros positivos), e $x \notin \mathbb{N}^{*}$, **não existe** termo $a_n$ igual a 24. De fato, calculando os termos vizinhos: $a_3 = 4\cdot2^2=16$ e $a_4=4\cdot2^3=32$, confirmando que $24$ fica entre dois termos consecutivos, sem corresponder a nenhum índice natural.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*2**(n-1)`, parâmetros `{'sequencia': 'pg', 'a1': '4', 'razao': '2'}`
- `funcao` — expressão `4*2**(n-1)`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `4*2**(x-1)`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `equacao` — expressão `Eq(4*2**(x-1), 24)`, esperado `[log(12, 2)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*2**(n - 1): coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (3) aprovado: Gabarito confirmado (domínio de 4*2**(x - 1): Interval(-oo, oo)). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/dominio=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado em três itens, com dados completos (a1, q), condições explícitas e pedidos claros e não ambíguos. A notação e as tarefas (a, b, c) são precisas.
  - adequacao_nivel: 4/5 — Os itens (a) e (b) exigem análise (relacionar estruturas, justificar por que a PG é restrição de f), compatível com 'analisar' e resposta relacional/SOLO. O item (c), porém, é majoritariamente aplicação (resolver equação exponencial), embora feche com uma decisão justificada sobre pertinência ao domínio discreto, o que resgata o caráter analítico. O conjunto da questão sustenta o nível declarado, mas o item (c) isoladamente é mais raso.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente o exigido: articula PG e função exponencial em um único problema (não justapõe itens independentes), exige comparação explícita de domínios discreto vs. contínuo, e usa essa distinção para resolver um problema (existência de termo igual a 24). Vai além do cálculo do termo geral, atendendo ao critério de que a associação precisa ser exigida pelo enunciado.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — Foge do padrão mecânico de 'calcule o termo geral' ou 'calcule a soma', propondo uma reflexão conceitual sobre domínios e a relação PG/função exponencial. Contexto é puramente matemático/teórico (sem aplicação contextualizada real), o que é aceitável dado o objetivo declarado, mas reduz um pouco o potencial de significância. Não há pistas que entreguem a resposta antes do raciocínio.
