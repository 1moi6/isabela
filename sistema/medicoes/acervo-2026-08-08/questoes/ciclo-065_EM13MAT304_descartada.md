# Ciclo 065 — EM13MAT304

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Um laboratório de microbiologia acompanha duas culturas de bactérias, ambas medidas em número de indivíduos e com o tempo $t$ em horas, contado a partir do início da observação ($t \geq 0$):

- Cultura A: começa com 50 bactérias e sua população **duplica a cada 4 horas**, sendo modelada por $P_A(t) = 50 \cdot 2^{t/4}$.
- Cultura B: começa com 800 bactérias e sua população **reduz-se à metade a cada 4 horas**, sendo modelada por $P_B(t) = 800 \cdot \left(\dfrac{1}{2}\right)^{t/4}$.

Resolva as questões a seguir, justificando cada resposta com base nas propriedades da função exponencial:

**a)** Classifique cada uma das funções $P_A$ e $P_B$ quanto à monotonicidade (crescente ou decrescente), justificando com base no valor da base da potência em cada caso.

**b)** Determine em que instante $t$ (em horas) as duas populações se igualam e qual é o valor dessa população comum nesse instante.

**c)** Calcule $P_A(4)$ e $P_B(4)$. Compare os dois valores e explique, usando o comportamento de crescimento/decaimento das funções, por que essa relação entre as populações era esperada antes do instante encontrado no item (b).

**d)** Sem refazer o cálculo do item (b), explique por que, para qualquer instante $t > 8$ horas, a Cultura A necessariamente terá mais bactérias do que a Cultura B.

## Gabarito

a) $P_A$ crescente (base 2>1); $P_B$ decrescente (base 1/2, entre 0 e 1). b) $t=8$ horas, população igual a 200 bactérias. c) $P_A(4)=100$, $P_B(4)=400$; antes de $t=8$ a Cultura B tem mais bactérias, coerente com o crescimento de A e o decaimento de B. d) Como $P_A$ é crescente e $P_B$ é decrescente e ambas valem 200 em $t=8$, para $t>8$ tem-se $P_A(t)>200>P_B(t)$.

## Resolução

**a) Monotonicidade das funções**

$P_A(t) = 50\cdot 2^{t/4}$ tem base $2 > 1$, logo $P_A$ é **crescente** para todo $t$ real: à medida que $t$ aumenta, a potência $2^{t/4}$ aumenta.

$P_B(t) = 800\cdot\left(\frac12\right)^{t/4}$ tem base $\frac12$, com $0 < \frac12 < 1$, logo $P_B$ é **decrescente** para todo $t$ real: à medida que $t$ aumenta, $\left(\frac12\right)^{t/4}$ diminui.

**b) Instante em que as populações se igualam**

Reescrevendo $\left(\frac12\right)^{t/4} = 2^{-t/4}$, a equação $P_A(t) = P_B(t)$ fica:
$$50\cdot 2^{t/4} = 800\cdot 2^{-t/4}$$
$$\frac{2^{t/4}}{2^{-t/4}} = \frac{800}{50}$$
$$2^{t/4+t/4} = 16$$
$$2^{t/2} = 2^4$$

Como a função exponencial de base 2 é injetora, os expoentes devem ser iguais:
$$\frac{t}{2} = 4 \implies t = 8$$

Substituindo em $P_A$: $P_A(8) = 50\cdot 2^{8/4} = 50\cdot 2^2 = 200$.

Conferindo em $P_B$: $P_B(8) = 800\cdot\left(\frac12\right)^{2} = 800\cdot\frac14 = 200$. ✓

As populações se igualam em **$t = 8$ horas**, com **200 bactérias** em cada cultura.

**c) Comparação em $t = 4$**

$P_A(4) = 50\cdot 2^{4/4} = 50\cdot 2 = 100$.

$P_B(4) = 800\cdot\left(\frac12\right)^{4/4} = 800\cdot\frac12 = 400$.

Como $P_B(4) = 400 > P_A(4) = 100$, antes do instante de igualdade a Cultura B ainda tem mais bactérias que a Cultura A. Isso é coerente com o item (a): como $P_A$ é crescente e parte de um valor bem menor (50), e $P_B$ é decrescente e parte de um valor bem maior (800), $P_B$ permanece acima de $P_A$ até que as curvas se cruzem em $t=8$.

**d) Comportamento para $t > 8$**

Como $P_A$ é estritamente crescente e $P_B$ é estritamente decrescente para todo $t$, e as duas funções assumem o mesmo valor (200) exatamente em $t = 8$, para qualquer $t > 8$ temos necessariamente $P_A(t) > 200$ (pois $P_A$ continua subindo a partir desse valor) e $P_B(t) < 200$ (pois $P_B$ continua descendo a partir desse valor). Logo, $P_A(t) > P_B(t)$ para todo $t > 8$, sem que seja preciso calcular novos valores numéricos — basta usar a monotonicidade das duas funções.

## Formalização verificável

- `funcao` — expressão `50*2**(t/4)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `800*(Rational(1,2))**(t/4)`, esperado `decrescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(50*2**(t/4), 800*(Rational(1,2))**(t/4))`, esperado `[8]`
- `funcao` — expressão `50*2**(t/4)`, esperado `200`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`
- `funcao` — expressão `50*2**(t/4)`, esperado `100`, parâmetros `{'consulta': 'valor', 'ponto': '4'}`
- `funcao` — expressão `800*(Rational(1,2))**(t/4)`, esperado `400`, parâmetros `{'consulta': 'valor', 'ponto': '4'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(0) = 200). | (2) aprovado: Gabarito confirmado (f(0) = 800). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (5) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é bem segmentado em três itens, com dados numéricos completos e condições explícitas (taxas percentuais, valores iniciais, intervalo de tempo). Não há ambiguidade lexical ou estrutural relevante; o único ponto que exige atenção do aluno é a distinção entre o instante contínuo do cruzamento e a hora inteira de observação, mas isso é claramente explicado no próprio enunciado.
  - adequacao_nivel: 2/5 — A especificação declara o nível Bloom 'criar', mas a tarefa pedida (escrever a lei a partir de dados fornecidos, explicar o significado das bases, resolver uma equação exponencial) corresponde, no máximo, a 'analisar/avaliar' — o aluno interpreta e justifica um fenômeno já delineado pelo professor, mas não elabora um problema, modelo ou situação nova, como o nível 'criar' exigiria (estrutura SOLO 'relacional', não 'estendido abstrato'). Há uma incompatibilidade entre o processo cognitivo realmente demandado e o nível declarado.
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as exigências listadas: vai além do cálculo mecânico, exigindo que o aluno compreenda e interprete o papel da base (fator de crescimento) na comparação entre as duas grandezas (item b), e usa um contexto realista de crescimento de seres vivos microscópicos, exatamente como citado na habilidade EM13MAT304. Os itens a, b e c articulam-se em um único raciocínio progressivo (modelar, interpretar, resolver), sem justaposição de subtarefas independentes.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O cenário de duas populações com taxas de crescimento diferentes que se cruzam é um clássico recorrente em livros didáticos de função exponencial. O item b, ao exigir a justificativa de que a ultrapassagem é 'matematicamente inevitável' via razão N_A/N_B, agrega uma camada analítica que foge um pouco do padrão mecânico, mas a estrutura geral (montar lei, comparar, encontrar cruzamento) não escapa do modelo tradicional de exercício de manual.
  - *sugestões:* Ajustar a coerência entre o nível cognitivo declarado ('criar') e o que a questão de fato demanda. Duas alternativas: (1) rebaixar o nível Bloom da especificação para 'analisar' ou 'avaliar', que corresponde ao que os itens b e c efetivamente exigem (interpretação e justificativa); ou (2) reformular a questão para incluir uma tarefa de elaboração genuína — por exemplo, pedir que o aluno proponha valores de taxa de crescimento para uma terceira colônia C, de modo que ela ultrapasse tanto A quanto B em um prazo determinado pelo próprio aluno, justificando a escolha matematicamente, ou que formule e resolva uma variação do problema (ex.: incluir decaimento de recursos limitando o crescimento). Isso tornaria a tarefa compatível com uma estrutura SOLO de nível estendido abstrato e com o verbo 'criar'. Também seria interessante variar o contexto para reduzir a semelhança com exercícios-padrão de livro didático, por exemplo usando dados de um estudo real (mesmo que fictício) com unidades ou restrições adicionais.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a coerência entre o nível cognitivo declarado ('criar') e o que a questão de fato demanda. Duas alternativas: (1) rebaixar o nível Bloom da especificação para 'analisar' ou 'avaliar', que corresponde ao que os itens b e c efetivamente exigem (interpretação e justificativa); ou (2) reformular a questão para incluir uma tarefa de elaboração genuína — por exemplo, pedir que o aluno proponha valores de taxa de crescimento para uma terceira colônia C, de modo que ela ultrapasse tanto A quanto B em um prazo determinado pelo próprio aluno, justificando a escolha matematicamente, ou que formule e resolva uma variação do problema (ex.: incluir decaimento de recursos limitando o crescimento). Isso tornaria a tarefa compatível com uma estrutura SOLO de nível estendido abstrato e com o verbo 'criar'. Também seria interessante variar o contexto para reduzir a semelhança com exercícios-padrão de livro didático, por exemplo usando dados de um estudo real (mesmo que fictício) com unidades ou restrições adicionais.

### Iteração 2

- **Verificador:** rejeitado — 2 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (decrescente em Interval(-oo, oo)). | (3) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [(log(8) + I*pi)/log(2)]. | (4) aprovado: Gabarito confirmado (f(3) = 40). | (5) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-5**(1/3)*(1/P0)**(1/3) - sqrt(3)*5**(1/3)*I*(1/P0)**(1/3), -5**(1/3)*(1/P0)**(1/3) + sqrt(3)*5**(1/3)*I*(1/P0)**(1/3)].
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
  - equacao=rejeitado
  - funcao/valor=aprovado
  - equacao=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 2 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (decrescente em Interval(-oo, oo)). | (3) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [(log(8) + I*pi)/log(2)]. | (4) aprovado: Gabarito confirmado (f(3) = 40). | (5) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-5**(1/3)*(1/P0)**(1/3) - sqrt(3)*5**(1/3)*I*(1/P0)**(1/3), -5**(1/3)*(1/P0)**(1/3) + sqrt(3)*5**(1/3)*I*(1/P0)**(1/3)]. Resultado calculado independentemente: crescente em Interval(-oo, oo) | decrescente em Interval(-oo, oo) | [3, (log(8) + I*pi)/log(2)] | f(3) = 40 | [2*5**(1/3)*(1/P0)**(1/3), -5**(1/3)*(1/P0)**(1/3) - sqrt(3)*5**(1/3)*I*(1/P0)**(1/3), -5**(1/3)*(1/P0)**(1/3) + sqrt(3)*5**(1/3)*I*(1/P0)**(1/3)]. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Todas as 6 afirmações conferidas. (1) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (decrescente em Interval(-oo, oo)). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) aprovado: Gabarito confirmado (f(8) = 200). | (5) aprovado: Gabarito confirmado (f(4) = 100). | (6) aprovado: Gabarito confirmado (f(4) = 400).
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente as duas funções, os dados iniciais, as taxas de crescimento/decaimento e o que é pedido em cada item (a, b, c, d). Não há ambiguidade lexical ou estrutural; todos os dados necessários estão explícitos.
  - adequacao_nivel: 2/5 — O processo cognitivo efetivamente exigido é analisar/aplicar/avaliar (classificar monotonicidade, resolver equação exponencial, calcular valores, justificar com base em propriedades já dadas), não criar. Não há produção de um modelo novo, generalização para outro contexto ou elaboração de um problema — apenas execução de procedimentos e justificativas sobre o modelo fornecido. Na taxonomia SOLO, as respostas variam de multiestrutural (a, c) a relacional (d), mas nenhuma chega ao nível estendido-abstrato que caracterizaria 'criar'. Há um descompasso claro entre o Bloom declarado e o que a questão de fato demanda.
  - alinhamento_bncc: 3/5 — A habilidade EM13MAT304 exige 'resolver E elaborar problemas' com funções exponenciais, compreendendo e interpretando a variação das grandezas. A questão cumpre bem a parte de resolver e interpretar (itens a, c, d exigem raciocínio sobre crescimento/decaimento, não só cálculo mecânico) e o contexto de crescimento microbiano é adequado e realista. Porém a dimensão de 'elaborar' problemas — que é textualmente parte da habilidade e coerente com o Bloom 'criar' declarado — está totalmente ausente: o aluno nunca precisa formular um problema, escolher parâmetros ou construir um cenário próprio.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O cenário de duas culturas bacterianas com crescimento e decaimento exponencial que se cruzam em determinado instante é um contexto bastante recorrente em livros didáticos de função exponencial. A articulação em quatro itens crescentes em complexidade evita repetição mecânica pura, mas não há elemento de contexto verdadeiramente inédito ou dado real/autêntico que diferencie a questão de exemplos clássicos de manual.
  - *sugestões:* Para alinhar a questão ao nível Bloom 'criar' e à parte da habilidade EM13MAT304 que pede 'elaborar problemas', adicione um item final que exija do aluno uma produção genuína, por exemplo: (e) 'Elabore uma nova situação-problema, alterando os valores iniciais e/ou taxas de crescimento/decaimento das culturas A e B, de modo que o instante de igualdade das populações seja t = 6 horas; apresente as novas funções, justifique a escolha dos parâmetros e resolva seu próprio problema.' Isso exigiria síntese e construção de um modelo, não apenas manipulação do modelo já fornecido. Alternativamente, se o professor preferir manter o formato atual (que está mais alinhado a 'analisar/avaliar'), o campo Bloom da especificação deveria ser corrigido para 'analisar' em vez de 'criar', evitando o descompasso entre especificação e questão. Para melhorar a originalidade, considere substituir o contexto de bactérias por outro cenário de decaimento/crescimento menos batido (ex.: concentração de um medicamento no sangue vs. crescimento de uma colônia de fungos em condições específicas, com dados de uma situação real reportada) e evitar que os números (t=8, cruzamento exato) sejam tão 'redondos' e previsíveis a ponto de sinalizar o caminho da resolução.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para alinhar a questão ao nível Bloom 'criar' e à parte da habilidade EM13MAT304 que pede 'elaborar problemas', adicione um item final que exija do aluno uma produção genuína, por exemplo: (e) 'Elabore uma nova situação-problema, alterando os valores iniciais e/ou taxas de crescimento/decaimento das culturas A e B, de modo que o instante de igualdade das populações seja t = 6 horas; apresente as novas funções, justifique a escolha dos parâmetros e resolva seu próprio problema.' Isso exigiria síntese e construção de um modelo, não apenas manipulação do modelo já fornecido. Alternativamente, se o professor preferir manter o formato atual (que está mais alinhado a 'analisar/avaliar'), o campo Bloom da especificação deveria ser corrigido para 'analisar' em vez de 'criar', evitando o descompasso entre especificação e questão. Para melhorar a originalidade, considere substituir o contexto de bactérias por outro cenário de decaimento/crescimento menos batido (ex.: concentração de um medicamento no sangue vs. crescimento de uma colônia de fungos em condições específicas, com dados de uma situação real reportada) e evitar que os números (t=8, cruzamento exato) sejam tão 'redondos' e previsíveis a ponto de sinalizar o caminho da resolução.
