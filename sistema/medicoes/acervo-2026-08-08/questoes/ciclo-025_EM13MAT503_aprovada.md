# Ciclo 025 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A empresa Confecções ABC vende um certo modelo de camiseta por p reais a unidade. Uma pesquisa de mercado mostrou que, para preços entre R$ 0,00 e R$ 60,00, a quantidade de camisetas vendidas por mês, em unidades, é dada por q(p) = 300 - 5p. A receita mensal da empresa é o produto do preço de venda pela quantidade vendida, isto é, R(p) = p · q(p). Determine o preço de venda que maximiza a receita mensal da empresa e o valor dessa receita máxima.

## Alternativas

- (a) R$ 30,00 por unidade, gerando uma receita máxima de R$ 4.500,00  ← correta
- (b) R$ 60,00 por unidade, gerando uma receita máxima de R$ 0,00
  - *erro representado:* Confunde o ponto de máximo da receita com o preço em que a demanda (e a receita) se anula, isto é, calcula a raiz de R(p) = 0 em vez do vértice da parábola.
- (c) R$ 30,00 por unidade, gerando uma receita máxima de R$ 150,00
  - *erro representado:* Encontra corretamente o preço ótimo, mas substitui esse valor na função de demanda q(p) em vez de na função de receita R(p) = p·q(p), confundindo quantidade vendida com receita.
- (d) R$ 15,00 por unidade, gerando uma receita máxima de R$ 3.375,00
  - *erro representado:* Usa incorretamente a fórmula do vértice como p_v = -b/(4a) em vez de p_v = -b/(2a), obtendo um preço e uma receita incorretos.

## Gabarito

Preço de R$ 30,00 por unidade, com receita máxima de R$ 4.500,00 (alternativa a).

## Resolução

**Passo 1 — Escrever a função receita.**

Como $R(p) = p \cdot q(p)$ e $q(p) = 300 - 5p$, temos:
$$R(p) = p(300 - 5p) = -5p^2 + 300p$$

Essa é uma função quadrática em $p$, com $a = -5$, $b = 300$ e $c = 0$.

**Passo 2 — Identificar o tipo de ponto extremo.**

Como $a = -5 < 0$, a parábola tem concavidade voltada para baixo, logo o vértice corresponde a um **ponto de máximo**.

**Passo 3 — Calcular a abscissa do vértice (preço ótimo).**

$$p_v = -\frac{b}{2a} = -\frac{300}{2(-5)} = -\frac{300}{-10} = 30$$

Ou seja, o preço que maximiza a receita é **R$ 30,00**.

**Passo 4 — Calcular a receita máxima (ordenada do vértice).**

$$R(30) = -5(30)^2 + 300(30) = -5(900) + 9000 = -4500 + 9000 = 4500$$

**Conclusão.**

O ponto de máximo da função receita é $(30, 4500)$: a empresa deve cobrar **R$ 30,00** por unidade, obtendo uma receita mensal máxima de **R$ 4.500,00**.

## Formalização verificável

- `funcao` — expressão `-5*p**2 + 300*p`, esperado `[30, 4500]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Gabarito confirmado (vértice calculado (30, 4500)).
  - funcao/vertice=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a variável de decisão (preço p), a função de demanda q(p), a função receita R(p) e o domínio válido (0 a 60). O que é pedido (preço ótimo e receita máxima) está explícito, sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido é essencialmente aplicar a fórmula do vértice de uma parábola a uma situação nova (receita = preço × quantidade), compatível com o nível 'aplicar' de Bloom. Em termos SOLO, a resposta é relacional, pois exige conectar duas funções (demanda e receita) antes de aplicar o procedimento, não sendo puramente mecânica. O conteúdo é plenamente compatível com o Ensino Médio.
  - alinhamento_bncc: 4/5 — A questão pede exatamente a investigação do ponto de máximo de uma função quadrática em contexto de Matemática Financeira (receita), cumprindo as exigências declaradas. O único ponto que impede nota máxima é que o termo 'investigar' da habilidade sugere alguma exploração ou análise de comportamento (ex.: variação de R(p), justificativa do porquê é máximo), enquanto a questão se resolve por aplicação direta de fórmula, sem exigir interpretação adicional do fenômeno.
  - distratores: 4/5 — Os três distratores representam erros plausíveis e distintos: confundir raiz da receita com vértice (60,00/0), substituir o preço ótimo na função errada (150,00) e usar fórmula incorreta do vértice (-b/4a em vez de -b/2a, resultando em 15,00/3375,00). Nenhum é absurdo ou trivialmente eliminável, embora o terceiro dependa de um erro de memorização menos comum entre estudantes.
  - originalidade: 3/5 — O contexto de otimização de receita via função de demanda linear é um clássico recorrente em livros didáticos e listas de exercícios sobre função quadrática, sem elementos que tragam um contexto mais significativo ou inesperado. Não há efeito Topaze evidente (não há pistas que entreguem o caminho da resolução), mas a estrutura do problema é altamente previsível para quem já viu esse tipo de exercício.
