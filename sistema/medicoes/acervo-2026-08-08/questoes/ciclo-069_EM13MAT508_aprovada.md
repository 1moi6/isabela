# Ciclo 069 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere a progressão geométrica (PG) $(a_n)$ com primeiro termo $a_1 = 5$ e razão $q = 3$.

a) Obtenha a expressão do termo geral $a_n$ em função de $n$.

b) Essa PG pode ser interpretada como a restrição, aos números naturais não nulos, de uma função exponencial $f:\mathbb{R} \to \mathbb{R}$ dada por $f(x) = 5 \cdot 3^{x-1}$. Explique por que o gráfico de $(a_n)$ é um conjunto de pontos isolados (discreto) sobre o gráfico contínuo de $f$, e indique qual é o domínio de $(a_n)$ quando ela é vista como uma função.

c) Calcule $f(5)$ e $f(6)$ e, usando esses valores, determine o menor número natural $n$ para o qual o termo $a_n$ da PG ultrapassa 1000.

## Gabarito

a) $a_n = 5\cdot 3^{n-1}$. b) $(a_n)$ é a restrição de $f(x)=5\cdot3^{x-1}$ aos naturais não nulos ($n\in\mathbb{N}^*$), por isso seu gráfico é discreto. c) $f(5)=405$, $f(6)=1215$, e o menor $n$ tal que $a_n>1000$ é $n=6$.

## Resolução

**a) Termo geral da PG**

Numa PG, $a_n = a_1 \cdot q^{n-1}$. Como $a_1 = 5$ e $q = 3$:
$$a_n = 5 \cdot 3^{n-1}$$

**b) Associação com a função exponencial e domínio**

A função $f(x) = 5 \cdot 3^{x-1}$ tem a mesma lei de formação do termo geral da PG, mas está definida para todo $x \in \mathbb{R}$ — seu gráfico é uma curva contínua. A sequência $(a_n)$, porém, só faz sentido para índices $n = 1, 2, 3, \dots$ (números naturais não nulos), pois representa termos ordenados de uma progressão. Assim:
$$a_n = f(n), \quad n \in \mathbb{N}^*$$
ou seja, os termos da PG são exatamente os valores que a função exponencial $f$ assume quando calculada nos números naturais não nulos. Por isso, o gráfico de $(a_n)$ é o conjunto de pontos $(n, f(n))$ com $n$ natural — pontos isolados sobre a curva contínua de $f$, e não a curva inteira. O domínio de $(a_n)$ como função é $\mathbb{N}^*$ (em notação SymPy, $S.Naturals$).

**c) Cálculo de $f(5)$, $f(6)$ e determinação do menor $n$**

$$f(5) = 5\cdot 3^{5-1} = 5 \cdot 3^4 = 5 \cdot 81 = 405$$
$$f(6) = 5\cdot 3^{6-1} = 5 \cdot 3^5 = 5 \cdot 243 = 1215$$

Como $a_n = f(n)$ para $n$ natural, temos $a_5 = 405 < 1000$ e $a_6 = 1215 > 1000$. Logo, o menor natural $n$ para o qual $a_n$ ultrapassa 1000 é:
$$n = 6$$

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*3**(n-1)`, parâmetros `{'sequencia': 'pg', 'a1': '5', 'razao': '3'}`
- `funcao` — expressão `5*3**(x-1)`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `5*3**(x-1)`, esperado `405`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`
- `funcao` — expressão `5*3**(x-1)`, esperado `1215`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `progressao` — expressão `-`, esperado `1215`, parâmetros `{'tipo_progressao': 'pg', 'a1': '5', 'razao': '3', 'n': '6', 'consulta': 'termo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*3**(n - 1): coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (3) aprovado: Gabarito confirmado (f(5) = 405). | (4) aprovado: Gabarito confirmado (f(6) = 1215). | (5) aprovado: Gabarito confirmado (termo da PG = 1215).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - progressao/termo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem segmentado em a), b) e c), com dados completos (a1, q, definição de f). Não há ambiguidade lexical ou estrutural; o que é dado e o que é pedido em cada item está explícito.
  - adequacao_nivel: 3/5 — Apenas o item b) exige de fato processo de análise (diferenciar domínio discreto de contínuo e relacionar as duas representações). Os itens a) e c) são majoritariamente 'aplicar' (fórmula do termo geral; cálculo direto de f(5), f(6) e comparação com 1000), reduzindo a estrutura de resposta a algo próximo do multiestrutural em vez de relacional/analítico em toda a questão, como pediria o Bloom 'analisar' declarado.
  - alinhamento_bncc: 4/5 — O item b) atende diretamente à exigência da EM13MAT508 de articular PG e função exponencial tratando o domínio discreto de forma explícita, que é o núcleo da habilidade. Os itens a) e c), porém, funcionam quase como aplicações isoladas de fórmula, sem reforçar a articulação; ainda assim, a questão como um todo cumpre a exigência central de forma satisfatória.
  - distratores: 5/5 — não se aplica
  - originalidade: 3/5 — A questão foge parcialmente do padrão mecânico de 'calcule o termo geral' ao pedir a discussão do domínio discreto, mas o contexto é puramente teórico/abstrato, sem significância aplicada. O item c) sofre efeito Topaze: ao dizer 'usando esses valores, determine o menor n', o enunciado já indica o caminho de comparação com f(5) e f(6), eliminando a necessidade de o aluno decidir sozinho a estratégia.
