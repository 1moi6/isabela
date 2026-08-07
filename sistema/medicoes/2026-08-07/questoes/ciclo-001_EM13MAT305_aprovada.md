# Ciclo 001 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A magnitude $M$ de um terremoto na escala Richter está relacionada à amplitude $A$ registrada no sismógrafo pela função logarítmica $M = \log_{10}\left(\dfrac{A}{A_0}\right)$, em que $A_0$ é uma amplitude de referência (constante, a mesma para todos os abalos). Em uma determinada semana, dois terremotos foram registrados: o terremoto A, com magnitude $M_A = 5{,}0$, e o terremoto B, com magnitude $M_B = 7{,}0$. 

a) Quantas vezes a amplitude do terremoto B é maior que a amplitude do terremoto A? 

b) Um terceiro terremoto, C, ocorreu na mesma região e apresentou amplitude 10000 vezes maior que a do terremoto A. Qual é a magnitude $M_C$ desse terremoto?

## Gabarito

a) 100 vezes; b) $M_C = 9{,}0$

## Resolução

**Passo 1 — Relacionar magnitude e amplitude.**

Da definição $M = \log_{10}\left(\dfrac{A}{A_0}\right)$, isolando a amplitude, temos:
$$\frac{A}{A_0} = 10^{M}$$

**Passo 2 — Amplitudes dos terremotos A e B.**

Para o terremoto A: $\dfrac{A_A}{A_0} = 10^{5{,}0}$

Para o terremoto B: $\dfrac{A_B}{A_0} = 10^{7{,}0}$

**Passo 3 — Razão entre as amplitudes (item a).**

$$\frac{A_B}{A_A} = \frac{A_0\cdot 10^{7}}{A_0\cdot 10^{5}} = 10^{7-5} = 10^{2} = 100$$

Ou seja, a amplitude do terremoto B é **100 vezes** maior que a do terremoto A. Isso mostra que, na escala Richter, cada unidade de magnitude a mais corresponde a uma amplitude 10 vezes maior — a variação da grandeza física (amplitude) é multiplicativa, enquanto a variação da magnitude (escala logarítmica) é aditiva.

**Passo 4 — Magnitude do terremoto C (item b).**

Sabemos que $A_C = 10000 \cdot A_A$. Logo:
$$\frac{A_C}{A_0} = 10000 \cdot \frac{A_A}{A_0} = 10^{4} \cdot 10^{5} = 10^{9}$$

Aplicando a definição de magnitude:
$$M_C = \log_{10}\left(\frac{A_C}{A_0}\right) = \log_{10}(10^{9}) = 9$$

**Conclusão:** a amplitude do terremoto B é 100 vezes a de A, e o terremoto C, com amplitude 10000 vezes maior que a de A, tem magnitude $M_C = 9{,}0$.

## Formalização verificável

- `equacao` — expressão `Eq(r, 10**(7 - 5))`, esperado `[100]`
- `equacao` — expressão `Eq(10**(m - 5), 10000)`, esperado `[9]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem redigido, dados completos (M_A, M_B, fator de amplitude de C), perguntas objetivas e sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — Compatível com 'aplicar': o aluno usa a definição de log para relacionar magnitude e amplitude em dois subproblemas conectados. A estrutura é multiestrutural/relacional (SOLO), coerente com 'aplicar', sem exigir análise crítica mais profunda, o que é adequado ao nível declarado.
  - alinhamento_bncc: 5/5 — A questão não se limita a aplicar a fórmula: o item (a) exige interpretar que uma diferença aditiva de magnitude corresponde a uma variação multiplicativa de amplitude, e o item (b) inverte esse raciocínio partindo da variação da grandeza física. Isso atende diretamente à exigência de 'compreender e interpretar a variação das grandezas' da EM13MAT305, com contexto realista de abalos sísmicos.
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 3/5 — O contexto da escala Richter é o exemplo mais canônico e repetido em livros didáticos para introduzir logaritmos; embora bem construído, não traz um contexto significativo diferenciado nem elementos que fujam do padrão usual desse tipo de problema.
