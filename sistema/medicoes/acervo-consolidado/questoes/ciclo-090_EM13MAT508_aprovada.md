# Ciclo 090 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma progressão geométrica $(a_n)$, definida apenas para $n \in \mathbb{N}^*$ (isto é, $n = 1, 2, 3, \dots$), tem $a_1 = 4$ e $a_4 = 32$. Sabe-se que essa PG é a restrição ao conjunto $\{1,2,3,\dots\}$ de uma função exponencial $f:\mathbb{Z}\to\mathbb{R}$, dada por $f(n) = A\cdot B^n$, tal que $f(n) = a_n$ para todo $n \geq 1$. Determine o valor de $f(0)$, isto é, o valor que a função exponencial assume fora do domínio original da progressão.

## Alternativas

- (a) $f(0) = 4$
  - *erro representado:* Esquecer o deslocamento do expoente no termo geral da PG, tratando $a_n = a_1\cdot q^n$ em vez de $a_1\cdot q^{n-1}$; isso leva a supor $f(n) = a_1\cdot q^n$ e, portanto, $f(0) = a_1 = 4$.
- (b) $f(0) = 2$  ← correta
- (c) $f(0) = 8$
  - *erro representado:* Calcular corretamente $q=2$, mas obter o coeficiente $A$ multiplicando $a_1$ pela razão em vez de dividir ($A = a_1\cdot q = 8$), invertendo a relação entre $A$ e $a_1$.
- (d) $f(0) = \dfrac{1}{2}$
  - *erro representado:* Determinar a razão de forma incorreta, calculando $q = a_4/a_1 = 8$ (ignorando o expoente 3 na relação $a_4 = a_1\cdot q^3$), e então obter $A = a_1/q = 4/8 = 1/2$.

## Gabarito

f(0) = 2

## Resolução

**Passo 1 — Termo geral da PG.**

Como $(a_n)$ é uma progressão geométrica de razão $q$, seu termo geral é $a_n = a_1\cdot q^{n-1}$.

**Passo 2 — Determinar a razão $q$.**

Usando $a_4 = a_1\cdot q^3$:

$$32 = 4\cdot q^3 \Rightarrow q^3 = 8 \Rightarrow q = 2.$$

**Passo 3 — Associar a PG à função exponencial.**

Queremos escrever $a_n = A\cdot B^n$ (com domínio estendido a todo $\mathbb{Z}$), coincidindo com $a_n = a_1\cdot q^{n-1}$ para $n\geq 1$. Reescrevendo:

$$a_1\cdot q^{n-1} = \left(\dfrac{a_1}{q}\right)\cdot q^{n}.$$

Comparando com $A\cdot B^n$, temos $B = q = 2$ e $A = \dfrac{a_1}{q} = \dfrac{4}{2} = 2$.

**Passo 4 — Verificação.**

$f(1) = A\cdot B = 2\cdot 2 = 4 = a_1$ ✓

$f(4) = A\cdot B^4 = 2\cdot 16 = 32 = a_4$ ✓

A função $f(n) = 2\cdot 2^n$ realmente coincide com a PG para todo $n\geq 1$, sendo sua extensão natural a todos os inteiros (domínio discreto ampliado).

**Passo 5 — Calcular $f(0)$.**

$$f(0) = A\cdot B^0 = A = 2.$$

Portanto, $f(0) = 2$, valor que não pertence ao domínio original da PG (que começa em $n=1$), mas é obtido naturalmente pela função exponencial associada.

## Formalização verificável

- `progressao` — expressão `-`, esperado `32`, parâmetros `{'tipo_progressao': 'pg', 'a1': '4', 'razao': '2', 'n': '4', 'consulta': 'termo'}`
- `funcao` — expressão `2*2**x`, esperado `2`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 32). | (2) aprovado: Gabarito confirmado (f(0) = 2).
  - progressao/termo=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado é compreensível: dados (a1, a4, forma f(n)=A·B^n) e pedido (f(0)) estão bem delimitados. Há alguma redundância ('definida apenas para n∈N*' e depois 'restrição ao conjunto {1,2,3,...}'), mas não gera ambiguidade real. A notação f:Z→R para uma 'exponencial' pode estranhar levemente por não ser o domínio usual, mas o texto explica que é uma extensão discreta.
  - adequacao_nivel: 4/5 — O processo exigido (aplicar termo geral da PG, montar sistema para A e B, extrapolar para n=0) é compatível com o nível 'aplicar': o aluno usa fórmulas conhecidas em uma situação nova (extensão do domínio). Do ponto de vista SOLO, a resposta exige relacionar duas representações (PG e função exponencial), configurando nível relacional, coerente com 'aplicar'. Conteúdo compatível com EM.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente o que a habilidade pede: exige que o aluno associe explicitamente a PG (a_n) à função exponencial f(n)=A·B^n, tratando o domínio discreto e sua extensão a Z. Não se limita a aplicar a fórmula do termo geral isoladamente — a articulação entre os dois objetos é o núcleo do problema, não um acessório.
  - distratores: 4/5 — Três distratores representam erros sistemáticos plausíveis e bem descritos (deslocamento de índice, inversão na relação A=a1/q, erro ao extrair a raiz cúbica de q^3). O distrator 'f(0)=4' é ligeiramente frágil porque, se o aluno verificasse f(1) com seu próprio raciocínio, encontraria inconsistência com a1=4; ainda assim é um erro comum de não verificação, portanto aceitável.
  - originalidade: 3/5 — O problema foge do modelo mais batido de 'encontre o termo geral da PG', ao introduzir a ideia de extensão a Z e o cálculo de f(0) fora do domínio original — isso é um ganho de originalidade conceitual. Por outro lado, o contexto é puramente formal/abstrato (sem aplicação significativa) e o enunciado já fornece a forma f(n)=A·B^n, o que reduz a exigência de descoberta e aproxima-se de um efeito Topaze leve, pois praticamente indica o caminho da resolução.
