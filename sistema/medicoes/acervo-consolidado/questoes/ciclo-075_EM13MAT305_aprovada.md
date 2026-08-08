# Ciclo 075 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

O potencial hidrogeniônico (pH) de uma solução aquosa é definido por $pH = -\log_{10}[H^+]$, em que $[H^+]$ é a concentração de íons hidrogênio (em mol/L). Quando uma solução sofre diluição ou concentração, sua concentração de $H^+$ é multiplicada por um fator $k>0$ (por exemplo, $k = \tfrac{1}{10}$ significa que a concentração caiu para um décimo do valor original; $k=5$ significa que ela quintuplicou).

**(a)** Mostre, usando as propriedades dos logaritmos, que a variação do pH causada por esse fator, $\Delta pH = pH_{final} - pH_{inicial}$, pode ser escrita como uma fórmula que depende apenas de $k$ (isto é, não depende do valor inicial de $[H^+]$).

**(b)** Uma solução tem $pH_{inicial} = 4{,}0$. Ela é diluída de modo que a concentração de $H^+$ passa a ser $\tfrac{1}{10}$ da concentração original ($k = \tfrac{1}{10}$). Calcule o novo pH e a variação $\Delta pH$, e diga se a solução ficou mais ácida ou mais básica.

**(c)** Agora é sua vez de elaborar um problema: invente uma situação com um pH inicial diferente de $4{,}0$ e um fator $k$ diferente de $\tfrac{1}{10}$ (pode representar uma diluição, com $0<k<1$, ou uma concentração, com $k>1$). Escreva o enunciado completo do seu problema (informando claramente o pH inicial e o fator $k$ escolhidos) e, em seguida, resolva-o usando a fórmula geral obtida no item (a), calculando o novo pH, a variação $\Delta pH$ e interpretando se a solução se tornou mais ácida ou mais básica.

## Gabarito

(a) $\Delta pH = -\log_{10}(k)$, independente do pH inicial. (b) $pH_{final}=5{,}0$; $\Delta pH = +1$; a solução ficou menos ácida. (c) Resposta aberta: será considerada correta qualquer situação-problema coerente (com pH inicial e fator $k$ escolhidos pelo estudante, diferentes dos do item b) cuja resolução aplique corretamente $\Delta pH=-\log_{10}(k)$ e $pH_{final}=pH_{inicial}-\log_{10}(k)$, com interpretação correta do sinal da variação (ácida/básica).

## Resolução

**Item (a):**

Seja $[H^+]_i$ a concentração inicial e $[H^+]_f = k\cdot [H^+]_i$ a concentração final, com $k>0$.

$pH_{final} = -\log_{10}\big(k\cdot [H^+]_i\big)$

Usando a propriedade $\log(ab) = \log a + \log b$:

$pH_{final} = -\log_{10}(k) - \log_{10}([H^+]_i) = -\log_{10}(k) + pH_{inicial}$

Logo:

$$\Delta pH = pH_{final} - pH_{inicial} = -\log_{10}(k)$$

Essa expressão mostra que a **variação** do pH depende apenas do fator multiplicativo $k$ aplicado à concentração, e não do valor absoluto de $[H^+]_i$ — característica típica de grandezas relacionadas por escala logarítmica: variações **multiplicativas** na grandeza original (concentração) correspondem a variações **aditivas** na grandeza transformada (pH).

**Item (b):**

Com $pH_{inicial} = 4{,}0$ e $k = \tfrac{1}{10}$:

$$\Delta pH = -\log_{10}\left(\tfrac{1}{10}\right) = -(-1) = 1$$

$$pH_{final} = 4{,}0 + 1 = 5{,}0$$

Como o pH aumentou (de 4,0 para 5,0), a solução ficou **menos ácida** (mais próxima da neutralidade), confirmando que diluir a concentração de $H^+$ aumenta o pH.

**Item (c):**

Resposta pessoal (aberta). O estudante deve:

1. Escolher um $pH_{inicial}$ diferente de 4,0 e um fator $k$ diferente de $\tfrac{1}{10}$, escrevendo um enunciado coerente (por exemplo: "Uma solução tem pH inicial 6,0 e sua concentração de $H^+$ é multiplicada por 100 (k=100). Qual o novo pH?").
2. Aplicar corretamente a fórmula $\Delta pH = -\log_{10}(k)$.
3. Calcular $pH_{final} = pH_{inicial} - \log_{10}(k)$.
4. Interpretar corretamente o sinal da variação: se $k>1$ (concentração aumenta), $\Delta pH<0$ e a solução fica mais ácida; se $0<k<1$ (diluição), $\Delta pH>0$ e a solução fica menos ácida (mais básica).

Exemplo de resolução válida (com os dados sugeridos acima): $\Delta pH = -\log_{10}(100) = -2$, então $pH_{final} = 6{,}0 - 2 = 4{,}0$; a solução ficou mais ácida.

## Formalização verificável

- `funcao` — expressão `4 - log(k, 10)`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': 'Rational(1,10)'}`
- `funcao` — expressão `-log(k, 10)`, esperado `1`, parâmetros `{'consulta': 'valor', 'ponto': 'Rational(1,10)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de -log(x)/log(10): Interval.open(0, oo)). | (2) aprovado: Gabarito confirmado (decrescente em Interval.open(0, oo)). | (3) aprovado: Propriedades confirmadas para -k: reproduz os 4 pontos dados; grau 1. | (4) aprovado: Gabarito confirmado (f(4) = -4).
  - funcao/dominio=aprovado
  - funcao/crescimento=aprovado
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente a função pH, especifica o que é dado ([H+] multiplicado por 10^k) e o que é pedido (expressão da variação, prova de independência do valor inicial, e cálculo numérico no item b). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver ambos os itens.
  - adequacao_nivel: 2/5 — O nível de Bloom declarado é 'criar', mas o processo cognitivo efetivamente exigido é deduzir/demonstrar uma relação algébrica (item a) e aplicá-la a um caso numérico (item b) — isso corresponde a 'analisar' ou, no máximo, 'avaliar' (justificar a independência do valor inicial), não a 'criar' um produto, modelo ou problema novo. Na taxonomia SOLO, a resposta esperada é relacional (integrar a propriedade do logaritmo do produto para generalizar a variação), o que é coerente com Bloom 'analisar', mas não caracteriza extended abstract exigida por 'criar'. Há, portanto, incompatibilidade entre o nível cognitivo declarado e o que a questão de fato demanda.
  - alinhamento_bncc: 4/5 — A questão atende bem à exigência central da EM13MAT305 de 'compreender e interpretar a variação das grandezas envolvidas' em contexto de pH: o item (a) exige demonstrar que a variação do pH é aditiva e independente do valor inicial (indo além da mera aplicação da definição de log), e o item (b) usa esse resultado interpretativamente. O contexto é realista (pH). O único ponto que não é plenamente atendido é a dimensão 'elaborar problemas' da habilidade, que não é exercitada (a questão é só de resolução, não de elaboração/criação de problema), o que reforça a incoerência apontada no critério anterior.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — Embora o contexto de pH seja um clássico dos livros didáticos, a abordagem de generalizar algebricamente a variação do pH em função de k (em vez de apenas calcular pH de uma solução específica) foge do exercício mecânico padrão e evita fortemente o efeito Topaze, pois o aluno precisa construir a dedução por conta própria.
  - *sugestões:* Ajustar o nível de Bloom declarado para 'analisar' (ou reformular a tarefa para de fato exigir 'criar'). Se a intenção é manter Bloom='criar', reformule o item (b) ou adicione um item (c) em que o aluno deva elaborar seu próprio problema/contexto (por exemplo, propor uma situação hipotética de duas soluções ou um cenário de diluição/concentração e formular a pergunta sobre variação de pH, construindo seu próprio modelo), atendendo à parte 'elaborar problemas' da habilidade EM13MAT305. Alternativamente, se o objetivo é manter a estrutura atual (dedução + aplicação), reclassifique a especificação para Bloom='analisar' e SOLO='relacional', o que tornaria a questão plenamente coerente com o que já está bem construído nos itens (a) e (b).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar o nível de Bloom declarado para 'analisar' (ou reformular a tarefa para de fato exigir 'criar'). Se a intenção é manter Bloom='criar', reformule o item (b) ou adicione um item (c) em que o aluno deva elaborar seu próprio problema/contexto (por exemplo, propor uma situação hipotética de duas soluções ou um cenário de diluição/concentração e formular a pergunta sobre variação de pH, construindo seu próprio modelo), atendendo à parte 'elaborar problemas' da habilidade EM13MAT305. Alternativamente, se o objetivo é manter a estrutura atual (dedução + aplicação), reclassifique a especificação para Bloom='analisar' e SOLO='relacional', o que tornaria a questão plenamente coerente com o que já está bem construído nos itens (a) e (b).

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(1/10) = 5). | (2) aprovado: Gabarito confirmado (f(1/10) = 1).
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (definição de pH, significado de k, valores numéricos) e comandos claros para cada item. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A questão progride de compreender (a) e aplicar (b) até criar (c), sendo esta progressão pedagogicamente adequada para culminar no nível 'criar' declarado. O item (c) exige efetivamente elaboração de um problema novo com resolução completa, compatível com SOLO 'extended abstract'. O único ponto de atenção é que apenas o item (c) atinge plenamente o nível 'criar', mas isso é esperado em questões escalonadas que preparam o aluno para a criação final.
  - alinhamento_bncc: 5/5 — Cumpre integralmente a habilidade EM13MAT305: usa função logarítmica em contexto de pH, coloca a variação (ΔpH) como objeto central da questão (não a mera definição de log) e exige explicitamente 'elaborar' um problema (item c), tal como a habilidade prescreve com o verbo 'elaborar'. Os itens articulam-se em torno de uma única fórmula geral, não são independentes.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de pH é recorrente em livros didáticos, mas o enfoque na demonstração de que ΔpH depende só de k, aliado à tarefa de criação de um problema análogo, evita o efeito Topaze e demanda raciocínio genuíno em vez de mera substituição em fórmula. Poderia ganhar mais originalidade explorando uma aplicação real (ex.: chuva ácida, efluente industrial) em vez de um enunciado genérico.
