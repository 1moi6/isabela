# Ciclo 011 — EM13MAT302

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma função afim $f(x) = ax + b$, com $a, b \in \mathbb{R}$ e $a \neq 0$, satisfaz simultaneamente as condições $f(2) = 7$ e $f(f(1)) = 13$. Determine a soma de todos os valores possíveis de $f(0)$.

## Alternativas

- (a) 4  ← correta
- (b) 3
  - *erro representado:* Encontra corretamente a equação quadrática, mas considera apenas a raiz a=2, ignorando que a=3 também gera uma solução válida (falha na análise de casos).
- (c) 1
  - *erro representado:* Encontra corretamente a equação quadrática, mas considera apenas a raiz a=3, ignorando que a=2 também gera uma solução válida (falha na análise de casos).
- (d) 6
  - *erro representado:* Interpreta erroneamente f(f(1)) como 2·f(1) (confundindo composição de função com o dobro do valor) em vez de aplicar f novamente sobre f(1), obtendo um único valor de a e, portanto, um único valor de f(0), sem necessidade de análise de casos.

## Gabarito

4

## Resolução

**Passo 1 — Traduzir as condições.**

Como $f(x) = ax+b$, a condição $f(2)=7$ fornece:
$$2a+b=7 \implies b = 7-2a$$

**Passo 2 — Expressar $f(f(1))$.**

Primeiro, $f(1) = a+b$. Usando $b=7-2a$:
$$f(1) = a + (7-2a) = 7-a$$

Agora aplicamos $f$ novamente:
$$f(f(1)) = f(7-a) = a(7-a)+b = 7a - a^2 + (7-2a)$$

**Passo 3 — Impor $f(f(1))=13$.**

$$7a - a^2 + 7 - 2a = 13$$
$$-a^2 + 5a + 7 = 13$$
$$-a^2 + 5a - 6 = 0 \implies a^2 - 5a + 6 = 0$$

**Passo 4 — Resolver a equação quadrática (análise de casos).**

$$a^2-5a+6=(a-2)(a-3)=0 \implies a=2 \text{ ou } a=3$$

Ambas as raízes são não nulas, logo ambas geram funções afins válidas — é preciso considerar os dois casos.

**Caso $a=2$:** $b = 7-2(2)=3$, logo $f(x)=2x+3$ e $f(0)=3$.

**Caso $a=3$:** $b = 7-2(3)=1$, logo $f(x)=3x+1$ e $f(0)=1$.

**Passo 5 — Somar os valores possíveis de $f(0)$.**

$$f(0)_{\text{soma}} = 3+1 = 4$$

## Formalização verificável

- `equacao` — expressão `Eq(a**2 - 5*a + 6, 0)`, esperado `[2, 3]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Conjunto-solução do gabarito coincide exatamente com o calculado.
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a função afim, as duas condições numéricas e o que se pede (soma de todos os valores possíveis de f(0)). Não há ambiguidade lexical ou estrutural; os dados são suficientes para resolver o problema.
  - adequacao_nivel: 4/5 — A resolução exige montar equações a partir das condições (aplicar conceitos de função afim e composição), resolver uma equação quadrática e, adicionalmente, verificar a validade de duas soluções distintas — este último passo se aproxima de 'analisar' na taxonomia de Bloom/SOLO (estrutura relacional, pois é preciso relacionar as duas raízes e decidir sobre sua aceitabilidade). Ainda assim, o núcleo da tarefa é compatível com 'aplicar' em nível avançado, dentro do esperado para Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão articula de fato função de 1º grau (afim) com função de 2º grau (a equação resultante da composição é quadrática), cumprindo a habilidade EM13MAT302 de forma integrada, não como itens justapostos. O modelo não é entregue pronto: o aluno precisa construí-lo a partir das condições dadas, respeitando a exigência de não fornecer o modelo quando o nível é 'aplicar' ou superior.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis: escolha de apenas uma das raízes válidas (3 e 1) e uma interpretação equivocada da composição f(f(1)) como 2·f(1) (6). Nenhum é absurdo ou trivialmente eliminável; todos exigem que o aluno cometa um erro conceitual específico e coerente com o raciocínio esperado.
  - originalidade: 3/5 — O problema é puramente algébrico/teórico, sem contextualização significativa, e o formato (determinar coeficientes de função afim via composição) é um tipo de exercício relativamente comum em materiais didáticos, ainda que a exigência de somar múltiplas soluções traga um toque de originalidade. Não há efeito Topaze evidente, mas o contexto poderia ser enriquecido para maior significância.
