# Ciclo 084 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo registra, a cada hora, a quantidade de bactérias em uma cultura recém-formada. As contagens feitas nos instantes t = 0h, 1h, 2h e 3h foram, respectivamente, 500, 1500, 4500 e 13500 bactérias, valores que formam uma progressão geométrica. O biólogo quer expressar essa progressão por meio de uma função exponencial P(n), em que n representa o número de horas completas decorridas desde o início da cultura (n assume apenas valores inteiros não negativos, pois as contagens só são feitas hora a hora), de modo a prever a quantidade de bactérias após 5 horas.

Qual alternativa apresenta corretamente a função P(n) — incluindo seu domínio — que corresponde a essa progressão geométrica, junto com o valor de P(5) obtido a partir dela?

## Alternativas

- (a) $P(n) = 500 \cdot 3^n$, com $n \in \mathbb{N}$; $P(5) = 121500$ bactérias.  ← correta
- (b) $P(n) = 500 \cdot 3^{n-1}$, com $n \in \mathbb{N}$; $P(5) = 40500$ bactérias.
  - *erro representado:* Aplicar mecanicamente a fórmula do termo geral da PG (a_n = a1·q^(n-1), válida quando o índice começa em 1) ao índice n que já representa o número de horas a partir de 0, defasando o expoente em uma unidade.
- (c) $P(n) = 500 + 3n$, com $n \in \mathbb{N}$; $P(5) = 515$ bactérias.
  - *erro representado:* Confundir a progressão geométrica com uma progressão aritmética, tratando o crescimento como linear (soma da razão) em vez de multiplicativo.
- (d) $P(n) = 500 \cdot n^3$, com $n \in \mathbb{N}$; $P(5) = 62500$ bactérias.
  - *erro representado:* Inverter os papéis de base e expoente, escrevendo uma função potência (variável na base) em vez da função exponencial correta (variável no expoente).

## Gabarito

A

## Resolução

**1. Identificar a razão da PG**

A sequência das contagens é $500, 1500, 4500, 13500, \dots$

$\dfrac{1500}{500} = 3$, $\dfrac{4500}{1500} = 3$, $\dfrac{13500}{4500} = 3$

Logo, é uma PG de razão $q = 3$, cujo primeiro valor observado (em $t=0$) é $500$.

**2. Associar a PG a uma função exponencial de domínio discreto**

Como o índice $n$ já começa em $0$ (correspondendo à primeira medição), a função que reproduz exatamente os termos da progressão é

$$P(n) = 500 \cdot 3^{n}$$

pois $P(0) = 500 \cdot 3^0 = 500$, coincidindo com o valor inicial. Note que essa é a mesma família de funções exponenciais $f(x) = a\cdot q^x$, mas aqui restrita aos instantes de medição: como $n$ conta horas completas decorridas, seu domínio é discreto, $n \in \mathbb{N} = \{0,1,2,3,\dots\}$, e não o conjunto dos reais.

**3. Verificar com os dados**

$P(1) = 500\cdot 3 = 1500$ ✓

$P(2) = 500\cdot 9 = 4500$ ✓

$P(3) = 500\cdot 27 = 13500$ ✓

**4. Calcular P(5)**

$$P(5) = 500 \cdot 3^5 = 500 \cdot 243 = 121500$$

Portanto, $P(n) = 500\cdot 3^n$, com $n \in \mathbb{N}$, e $P(5) = 121500$ bactérias.

## Formalização verificável

- `progressao` — expressão `-`, esperado `121500`, parâmetros `{'tipo_progressao': 'pg', 'a1': '500', 'razao': '3', 'n': '6', 'consulta': 'termo'}`
- `funcao` — expressão `500*3**n`, esperado `121500`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`
- `funcao` — expressão `500*3**n`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 121500). | (2) aprovado: Gabarito confirmado (f(5) = 121500). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals).
  - progressao/termo=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (valores da PG, instantes de medição) e pergunta única e precisa (função P(n) com domínio + valor de P(5)). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido (identificar razão, escrever a lei de formação, calcular um termo) é compatível com o nível 'aplicar' e a estrutura multiestrutural do SOLO. Não exige análise crítica adicional, mas isso é coerente com o Bloom declarado.
  - alinhamento_bncc: 4/5 — A questão vai além de aplicar mecanicamente a fórmula do termo geral: exige explicitamente que o aluno reconheça o domínio discreto (n ∈ ℕ) e diferencie essa função da exponencial de domínio real, o que atende à exigência de articulação PG-função exponencial pedida pela habilidade. Poderia reforçar ainda mais essa articulação exigindo justificativa sobre por que o domínio é discreto, mas o requisito mínimo é cumprido.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e distintos: defasagem de índice na fórmula do termo geral, confusão PG/PA, e inversão de base/expoente. Nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 3/5 — O contexto de crescimento bacteriano é um clássico recorrente em livros didáticos de função exponencial; embora bem contextualizado e sem 'efeito Topaze' evidente, não traz uma abordagem inovadora ou inesperada.
