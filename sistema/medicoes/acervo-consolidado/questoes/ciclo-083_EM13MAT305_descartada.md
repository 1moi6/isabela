# Ciclo 083 — EM13MAT305

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

A escala Richter mede a magnitude $M$ de um terremoto por meio da expressão $M = \log_{10}\left(\dfrac{A}{A_0}\right)$, em que $A$ é a amplitude máxima das ondas sísmicas registradas por um sismógrafo e $A_0$ é uma amplitude de referência, constante e igual para todos os terremotos analisados por esse mesmo tipo de equipamento.

Um terremoto ocorrido na cidade X foi registrado com magnitude 5,0 na escala Richter. Meses depois, um terremoto na cidade Y, medido pelo mesmo tipo de sismógrafo (portanto, com a mesma referência $A_0$), foi registrado com magnitude 7,0.

Com base na relação entre magnitude e amplitude estabelecida pela fórmula, quantas vezes maior foi a amplitude máxima das ondas sísmicas do terremoto de Y em comparação com a do terremoto de X?

## Alternativas

- (a) 100 vezes  ← correta
- (b) 2 vezes
  - *erro representado:* Tratar a diferença entre as magnitudes (7,0 - 5,0 = 2) como se fosse diretamente o fator multiplicativo da amplitude, ignorando que a escala é logarítmica (base 10).
- (c) 20 vezes
  - *erro representado:* Supor crescimento linear e multiplicar a diferença de magnitudes por 10 (2 × 10 = 20), em vez de usar 10 elevado à diferença de magnitudes.
- (d) 1,4 vezes
  - *erro representado:* Calcular a razão direta entre as magnitudes (7/5 = 1,4), tratando a escala Richter como uma escala linear proporcional à amplitude.

## Gabarito

A amplitude das ondas sísmicas do terremoto de Y foi 100 vezes maior que a do terremoto de X.

## Resolução

**Passo 1 — Escrever a amplitude de cada terremoto a partir da fórmula.**

Da relação $M = \log_{10}\left(\dfrac{A}{A_0}\right)$, isolamos $A$:
$$\frac{A}{A_0} = 10^{M} \quad \Rightarrow \quad A = A_0 \cdot 10^{M}$$

Para a cidade X ($M=5{,}0$): $A_X = A_0 \cdot 10^{5}$

Para a cidade Y ($M=7{,}0$): $A_Y = A_0 \cdot 10^{7}$

**Passo 2 — Comparar as amplitudes por meio da razão $A_Y/A_X$.**

$$\frac{A_Y}{A_X} = \frac{A_0 \cdot 10^{7}}{A_0 \cdot 10^{5}} = 10^{7-5} = 10^{2} = 100$$

O valor $A_0$ se cancela, pois é o mesmo para os dois terremotos — o que importa é a **diferença entre as magnitudes**, não o valor absoluto de $A_0$.

**Passo 3 — Interpretar a variação.**

Como a escala Richter é logarítmica, cada unidade a mais na magnitude corresponde a uma multiplicação da amplitude por 10 (não a uma soma). Uma diferença de 2 unidades (de 5,0 para 7,0) corresponde, portanto, a uma multiplicação por $10^2 = 100$.

**Conclusão:** a amplitude das ondas do terremoto de Y foi **100 vezes** maior que a do terremoto de X.

## Formalização verificável

- `equacao` — expressão `Eq(log(x, 10), 2)`, esperado `[100]`
- `funcao` — expressão `10**M`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta dados completos, define claramente a fórmula, os valores de magnitude e o que é pedido (razão A2/A1). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — A especificação declara nível 'criar' (Bloom), mas a tarefa realizada é resolver um problema padrão aplicando a fórmula dada e convertendo diferença logarítmica em razão — isso corresponde a 'aplicar' ou, no máximo, 'analisar' (relacionar variáveis), não a 'criar'. Não há produção de algo novo, formulação de hipótese, elaboração de problema ou síntese original exigida pelo aluno. A estrutura de resposta é relacional (SOLO), compatível com aplicar/analisar, mas não com criar.
  - alinhamento_bncc: 4/5 — A questão atende à exigência de que a variação das grandezas seja o objeto central: o aluno precisa entender que uma diferença de 2 unidades de magnitude corresponde a uma razão de 10² entre amplitudes, não apenas aplicar a definição isolada do logaritmo. O contexto (abalos sísmicos) é adequado. Falta, porém, o componente 'elaborar problemas' da habilidade — a questão só pede para resolver, não para o aluno criar ou generalizar a relação.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: confundir escala logarítmica com linear (2x), multiplicar em vez de exponenciar (20x), e erro de contagem na diferença de magnitudes (1000x). Nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 3/5 — O cenário de terremotos e escala Richter com diferença de 2 unidades de magnitude é um exemplo clássico e recorrente em livros didáticos e vestibulares. O contexto é significativo, mas a estrutura do problema é bastante previsível e não inova em relação ao formato tradicional dessas questões.
  - *sugestões:* Ajustar a questão para que o processo cognitivo exigido corresponda de fato ao nível 'criar', ou então alterar a especificação para 'aplicar'/'analisar', que é o que a tarefa atual demanda. Para elevar ao nível 'criar', seria necessário, por exemplo: (a) pedir que o aluno formule uma expressão geral para a razão A2/A1 em função de ΔM, generalizando o raciocínio para qualquer diferença de magnitude, e depois use essa expressão para resolver um novo caso; ou (b) solicitar que o aluno elabore um problema análogo (com outro par de magnitudes ou outro contexto, como pH ou radioatividade) que exija a mesma interpretação de variação logarítmica, incluindo a resolução. Também é recomendável tornar o contexto menos padronizado (evitar o exemplo clássico de terremotos com ΔM=2) ou combiná-lo com outro fenômeno logarítmico para reforçar a articulação de conteúdos e aumentar a originalidade.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a questão para que o processo cognitivo exigido corresponda de fato ao nível 'criar', ou então alterar a especificação para 'aplicar'/'analisar', que é o que a tarefa atual demanda. Para elevar ao nível 'criar', seria necessário, por exemplo: (a) pedir que o aluno formule uma expressão geral para a razão A2/A1 em função de ΔM, generalizando o raciocínio para qualquer diferença de magnitude, e depois use essa expressão para resolver um novo caso; ou (b) solicitar que o aluno elabore um problema análogo (com outro par de magnitudes ou outro contexto, como pH ou radioatividade) que exija a mesma interpretação de variação logarítmica, incluindo a resolução. Também é recomendável tornar o contexto menos padronizado (evitar o exemplo clássico de terremotos com ΔM=2) ou combiná-lo com outro fenômeno logarítmico para reforçar a articulação de conteúdos e aumentar a originalidade.

### Iteração 2

- **Verificador:** aprovado_parcial — 1 de 2 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Falha ao processar a expressão (PolynomialError: 10**d contains an element of the set of generators.). Revisar a formalização produzida pelo Gerador. | (2) aprovado: Gabarito confirmado (f(3/2) = 10*sqrt(10)).
  - propriedade=nao_verificavel
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente as variáveis (A, A0, M1, M2, ΔM), especifica o que é dado e o que é pedido (obter a expressão geral e depois aplicá-la numericamente). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O nível de Bloom declarado é 'criar', mas o processo cognitivo real exigido é isolar A na definição, formar a razão e simplificar — uma derivação algébrica guiada passo a passo, típica de 'aplicar/analisar', não de produção original ou síntese. Em termos SOLO, a resposta esperada é relacional (aplicar uma fórmula geral e substituir valores), e não 'extended abstract', que se esperaria de uma tarefa de criação. Além disso, o formato múltipla escolha reduz ainda mais a possibilidade de avaliar um processo de 'criar', pois o aluno só escolhe entre valores numéricos finais, sem precisar demonstrar a construção da regra geral.
  - alinhamento_bncc: 4/5 — A habilidade EM13MAT305 exige compreender e interpretar a variação de grandezas em contexto logarítmico realista. A questão cumpre isso: o cerne do problema é a razão A2/A1 em função de ΔM, que expressa exatamente a variação relativa das amplitudes em função da diferença de magnitudes, indo além da mera aplicação da definição de logaritmo. O contexto sísmico é adequado. Não articula múltiplos temas, mas isso não é exigido aqui.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis: confusão com a crença popular de 'dobra por ponto' (base 2), tratamento linear em vez de exponencial, e confusão com a fórmula de energia sísmica (expoente 1,5ΔM). Nenhum é absurdo ou trivialmente eliminável; exigem compreensão real da estrutura da fórmula para descartar.
  - originalidade: 4/5 — O contexto de escala Richter é um clássico do ensino de logaritmos, mas a proposta de derivar uma regra geral para a razão de amplitudes em função de ΔM (em vez de apenas calcular uma magnitude a partir de dados) foge do formato mais mecânico usual. O enunciado não entrega pistas diretas da solução, exigindo do aluno a manipulação algébrica completa.
  - *sugestões:* Ajustar a coerência entre o nível de Bloom declarado ('criar') e o processo cognitivo real exigido. Duas rotas possíveis: (1) Rebaixar a especificação de Bloom para 'aplicar' ou 'analisar', já que a tarefa é essencialmente derivar uma fórmula por manipulação algébrica direta a partir de uma definição dada, seguida de substituição numérica — isso é coerente com o formato de múltipla escolha atual. (2) Se quiser manter o nível 'criar', reformular como questão dissertativa/aberta, pedindo que o aluno proponha e justifique por si só (sem que o enunciado sugira passo a passo) uma regra geral de comparação entre dois terremotos, e/ou peça que ele generalize o raciocínio para outro contexto (ex.: pH ou radioatividade), exigindo transferência e síntese — isso aproximaria a tarefa de um nível SOLO 'extended abstract' compatível com 'criar'. Em qualquer caso, evitar que o formato de múltipla escolha seja usado para avaliar processos de criação, pois esse formato naturalmente reduz a tarefa a reconhecimento/aplicação de fórmula.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a coerência entre o nível de Bloom declarado ('criar') e o processo cognitivo real exigido. Duas rotas possíveis: (1) Rebaixar a especificação de Bloom para 'aplicar' ou 'analisar', já que a tarefa é essencialmente derivar uma fórmula por manipulação algébrica direta a partir de uma definição dada, seguida de substituição numérica — isso é coerente com o formato de múltipla escolha atual. (2) Se quiser manter o nível 'criar', reformular como questão dissertativa/aberta, pedindo que o aluno proponha e justifique por si só (sem que o enunciado sugira passo a passo) uma regra geral de comparação entre dois terremotos, e/ou peça que ele generalize o raciocínio para outro contexto (ex.: pH ou radioatividade), exigindo transferência e síntese — isso aproximaria a tarefa de um nível SOLO 'extended abstract' compatível com 'criar'. Em qualquer caso, evitar que o formato de múltipla escolha seja usado para avaliar processos de criação, pois esse formato naturalmente reduz a tarefa a reconhecimento/aplicação de fórmula.

### Iteração 3

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente os dados (magnitudes 5,0 e 7,0, mesma referência A0) e a pergunta (razão entre amplitudes). Não há ambiguidade lexical ou estrutural, e todas as informações necessárias estão presentes.
  - adequacao_nivel: 2/5 — A especificação declara nível 'criar' (Bloom), mas a tarefa exigida é isolar A na fórmula e calcular uma razão de potências — processo de 'aplicar/compreender', com estrutura SOLO no máximo multiestrutural (identificar duas expressões e dividir). Não há elaboração de problema, modelo novo ou síntese de elementos, que caracterizariam 'criar'. O formato de múltipla escolha reforça essa limitação, pois o aluno apenas seleciona entre respostas prontas, sem produzir nada. Há incoerência clara entre o nível cognitivo declarado e o exigido pela questão.
  - alinhamento_bncc: 4/5 — A questão vai além da simples definição de logaritmo: exige perceber que uma diferença constante de magnitude corresponde a um fator multiplicativo na amplitude (variação exponencial), o que atende ao espírito da EM13MAT305 sobre interpretar a variação de grandezas em abalos sísmicos. Poderia ser mais robusta se pedisse generalização (ex.: fórmula para diferença arbitrária de magnitudes) ou comparação de múltiplos cenários, aproximando-se mais do nível 'criar' declarado.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: tratar a diferença de magnitude como fator direto (2x), multiplicar linearmente por 10 (20x) e calcular razão direta das magnitudes (1,4x). Nenhum é trivialmente eliminável, e todos remetem a concepções equivocadas comuns sobre escalas logarítmicas.
  - originalidade: 3/5 — O contexto de terremotos e escala Richter é clássico em livros didáticos para introduzir logaritmos; a estrutura do problema (comparar duas cidades com magnitudes dadas) é bastante convencional, sem elementos que tragam um efeito de surpresa ou aplicação inédita. Não há 'efeito Topaze' evidente, mas também não há inovação de contexto.
  - *sugestões:* Ajustar a coerência entre o nível de Bloom declarado ('criar') e a tarefa cognitiva real. Duas rotas possíveis: (1) Rebaixar a classificação Bloom para 'aplicar' ou 'analisar', já que a questão, como está, apenas pede a aplicação da fórmula e cálculo de uma razão — isso resolveria a incoerência sem alterar o enunciado. (2) Se o objetivo é manter o nível 'criar', reformular a questão para um formato aberto (não múltipla escolha) em que o aluno precise, por exemplo, elaborar uma expressão geral que relacione a razão de amplitudes a uma diferença arbitrária de magnitudes (A_Y/A_X = 10^(M_Y-M_X)), propor um novo cenário com dados fictícios e justificar seu raciocínio, ou criar um problema análogo em outro contexto logarítmico (pH, radioatividade) que exija a mesma interpretação da variação. Para aumentar a originalidade, considere usar dados reais de terremotos históricos ou comparar três eventos em vez de dois, exigindo síntese maior. Por fim, mantendo o formato de múltipla escolha, o nível 'criar' não é alcançável — escolha um entre ajustar o Bloom ou mudar o formato para permitir produção autônoma do aluno.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a coerência entre o nível de Bloom declarado ('criar') e a tarefa cognitiva real. Duas rotas possíveis: (1) Rebaixar a classificação Bloom para 'aplicar' ou 'analisar', já que a questão, como está, apenas pede a aplicação da fórmula e cálculo de uma razão — isso resolveria a incoerência sem alterar o enunciado. (2) Se o objetivo é manter o nível 'criar', reformular a questão para um formato aberto (não múltipla escolha) em que o aluno precise, por exemplo, elaborar uma expressão geral que relacione a razão de amplitudes a uma diferença arbitrária de magnitudes (A_Y/A_X = 10^(M_Y-M_X)), propor um novo cenário com dados fictícios e justificar seu raciocínio, ou criar um problema análogo em outro contexto logarítmico (pH, radioatividade) que exija a mesma interpretação da variação. Para aumentar a originalidade, considere usar dados reais de terremotos históricos ou comparar três eventos em vez de dois, exigindo síntese maior. Por fim, mantendo o formato de múltipla escolha, o nível 'criar' não é alcançável — escolha um entre ajustar o Bloom ou mudar o formato para permitir produção autônoma do aluno.
