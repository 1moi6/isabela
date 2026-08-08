# Ciclo 061 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo inicia uma cultura de bactérias com 200 indivíduos. A cada hora que passa, a quantidade de bactérias na cultura dobra em relação à hora anterior. Seja $a_n$ o número de bactérias existentes ao final da $n$-ésima hora de observação, com $n = 1, 2, 3, \dots$ (isto é, $a_1$ é a quantidade ao final da 1ª hora, $a_2$ ao final da 2ª hora, e assim por diante).

a) Mostre que a sequência $(a_n)$ é uma progressão geométrica, indicando o primeiro termo e a razão.

b) Escreva a lei $f(n)$ de uma função exponencial que descreva exatamente essa progressão geométrica, especificando qual é o domínio dessa função e por que ele deve ser desse tipo (e não todos os números reais).

c) Usando a fórmula do termo geral da PG (ou, equivalentemente, a função $f(n)$ obtida no item b), determine quantas bactérias haverá ao final da 6ª hora de observação.

## Gabarito

a) PG de razão $q=2$ e $a_1=200$; b) $f(n)=200\cdot 2^{n-1}$, com domínio $D=\{1,2,3,\dots\}$ (naturais, pois $n$ conta horas); c) $a_6 = f(6) = 6400$ bactérias.

## Resolução

**a) Identificando a PG**

Como a quantidade dobra a cada hora, temos $a_{n+1} = 2\cdot a_n$ para todo $n \geq 1$. Isso significa que a razão entre termos consecutivos é constante e igual a $q = 2$. Logo, $(a_n)$ é uma progressão geométrica de razão $q=2$, com primeiro termo $a_1 = 200$ (quantidade ao final da 1ª hora).

**b) Associando a PG a uma função exponencial**

O termo geral da PG é dado por
$$a_n = a_1 \cdot q^{\,n-1} = 200 \cdot 2^{\,n-1}.$$

Essa expressão é exatamente a lei de uma função exponencial
$$f(n) = 200 \cdot 2^{\,n-1},$$
em que a base da exponencial ($2$) coincide com a razão da PG e o coeficiente ($200$) coincide com o primeiro termo.

Como $n$ representa o número da hora de observação (1ª hora, 2ª hora, etc.), $n$ só pode assumir valores inteiros positivos: $n \in \{1, 2, 3, \dots\}$. Assim, o domínio de $f$ é o conjunto dos números naturais (a partir de 1), $D = \mathbb{N}^* = \{1,2,3,\dots\}$, e **não** todo o conjunto dos reais — não faz sentido, por exemplo, falar em "1,5 hora de observação" nesse contexto discreto de contagem de termos da sequência. Por isso $f$ é uma função exponencial de domínio discreto que apenas "amostra" a curva exponencial contínua $y = 200\cdot 2^{x-1}$ nos pontos inteiros.

**c) Cálculo para a 6ª hora**

Usando $n=6$:
$$f(6) = a_6 = 200 \cdot 2^{6-1} = 200 \cdot 2^5 = 200 \cdot 32 = 6400.$$

Logo, ao final da 6ª hora haverá **6400 bactérias**.

## Formalização verificável

- `progressao` — expressão `-`, esperado `6400`, parâmetros `{'tipo_progressao': 'pg', 'a1': '200', 'razao': '2', 'n': '6', 'consulta': 'termo'}`
- `funcao` — expressão `200*2**(n-1)`, esperado `6400`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `funcao` — expressão `200*2**(n-1)`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `propriedade` — expressão `-`, esperado `200*2**(n-1)`, parâmetros `{'sequencia': 'pg', 'a1': '200', 'razao': '2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 6400). | (2) aprovado: Gabarito confirmado (f(6) = 6400). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (4) aprovado: Propriedades confirmadas para 200*2**(n - 1): coincide com a PG declarada.
  - progressao/termo=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, define claramente a variável a_n, o contexto e o que é pedido em cada item, sem ambiguidades.
  - adequacao_nivel: 4/5 — O nível 'aplicar' é coerente com os itens a) e c), que exigem reconhecer a PG e usar a fórmula do termo geral. O item b) exige mais que aplicação simples (articular PG e função exponencial, justificar domínio discreto), aproximando-se de 'analisar/compreender relações estruturais', mas isso enriquece a questão sem contradizer o nível declarado, já que a resposta esperada é relacional (SOLO), compatível com aplicar+.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente as exigências: articula explicitamente PG e função exponencial (item b pede a lei f(n) que reproduz a PG), trata o domínio discreto com justificativa contextual (por que não são todos os reais), e usa a fórmula do termo geral de modo integrado à interpretação funcional. Não é mera aplicação de fórmula isolada.
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 3/5 — O contexto de bactérias que dobram é um clássico recorrente em livros didáticos para progressão geométrica/exponencial. A estrutura da questão, embora bem construída pedagogicamente, não escapa do exemplo mais batido do tema, reduzindo o efeito de novidade.
