# Ciclo 059 — EM13MAT304

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Um biólogo está estudando uma colônia de bactérias em uma placa de Petri, em laboratório. No instante inicial da observação (n = 0 horas) ele conta 40 bactérias. A cada hora que passa, a quantidade de bactérias triplica em relação à hora anterior, devido à reprodução por divisão celular. As primeiras contagens registradas pelo biólogo foram:

| n (horas) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(n) (bactérias) | 40 | 120 | 360 | 1080 |

a) Usando os dados da tabela, escreva a lei de formação P(n) = a·b^n que modela o número de bactérias em função do tempo n (em horas), justificando por que esse crescimento corresponde a uma progressão geométrica.

b) Utilizando o modelo obtido, calcule quantas bactérias existirão na placa após 6 horas de observação.

c) Sem refazer contas numéricas, explique por que essa função é crescente para qualquer valor de n e o que isso significa em termos da variação da população: qual é, proporcionalmente, o aumento da quantidade de bactérias a cada hora que passa?

d) Resolvendo algebricamente a equação exponencial correspondente, determine depois de quantas horas a população atingirá exatamente 9720 bactérias.

## Gabarito

a) P(n) = 40·3^n (PG de primeiro termo 40 e razão 3); b) 29 160 bactérias; c) função crescente pois a base 3 > 1, com crescimento de 200% (triplicação) a cada hora; d) n = 5 horas.

## Resolução

**a) Determinando o modelo**

Os valores $40, 120, 360, 1080$ formam uma progressão geométrica, pois a razão entre termos consecutivos é constante:
$$\frac{120}{40} = \frac{360}{120} = \frac{1080}{360} = 3$$

Como $P(0) = 40$ é o termo inicial e a razão é $3$, o modelo exponencial é:
$$P(n) = 40 \cdot 3^{n}$$

Verificação: $P(0)=40$, $P(1)=120$, $P(2)=360$, $P(3)=1080$ — todos coincidem com a tabela.

**b) População após 6 horas**

$$P(6) = 40 \cdot 3^{6} = 40 \cdot 729 = 29160$$

Haverá **29 160 bactérias** após 6 horas.

**c) Crescimento e variação percentual**

Como a base $b = 3$ é maior que $1$, a função $P(n) = 40\cdot 3^n$ é crescente para todo $n$ real: à medida que $n$ aumenta, o expoente aumenta e, consequentemente, $3^n$ também aumenta, tornando $P(n)$ sempre maior.

Em termos de variação: a cada hora que passa,
$$\frac{P(n+1)}{P(n)} = \frac{40\cdot 3^{n+1}}{40\cdot 3^{n}} = 3$$

ou seja, a população **triplica** a cada hora, o que corresponde a um crescimento de **200% por hora** (multiplicar por 3 equivale a somar 200% ao valor anterior).

**d) Resolvendo a equação exponencial**

Queremos encontrar $n$ tal que $P(n) = 9720$:
$$40 \cdot 3^{n} = 9720$$
$$3^{n} = \frac{9720}{40} = 243$$

Como $243 = 3^{5}$, temos:
$$3^{n} = 3^{5} \implies n = 5$$

Alternativamente, usando logaritmos: $n = \dfrac{\log(243)}{\log(3)} = 5$.

Portanto, a população atingirá 9720 bactérias após **5 horas**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `40*3**n`, parâmetros `{'pontos': '[(0,40),(1,120),(2,360),(3,1080)]', 'sequencia': 'pg', 'a1': '40', 'razao': '3'}`
- `funcao` — expressão `40*3**n`, esperado `29160`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `funcao` — expressão `40*3**n`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(40*3**n, 9720)`, esperado `[5]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 100*3**(t/3): reproduz os 4 pontos dados. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - propriedade=aprovado
  - equacao=aprovado
  - funcao/dominio=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado claro, com dados completos (P0=100, triplica a cada 3h) e três pedidos bem delimitados (elaborar lei, calcular tempo, interpretar). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — A especificação declara Bloom 'criar', mas apenas o item (a) pede efetivamente a elaboração da função (e de forma bastante guiada, já que só há uma forma natural de escrever a lei a partir dos dados, sem exigir decisões ou combinação de elementos diversos). Os itens (b) e (c) são 'aplicar' e 'compreender/interpretar', respectivamente — processos de nível inferior a 'criar'. Na taxonomia SOLO, a resposta esperada é essencialmente multiestrutural (cada item resolvido isoladamente com procedimento padrão), não relacional, que seria exigido por uma tarefa de 'criar'. O nível cognitivo global da questão não corresponde ao declarado.
  - alinhamento_bncc: 3/5 — O contexto de crescimento de seres vivos microscópicos está presente e é realista, atendendo a essa exigência. O item (c) cumpre a exigência de 'compreender e interpretar a variação das grandezas'. Porém a elaboração da lei em (a) é praticamente mecânica (substituição direta de dois dados em uma forma-padrão já sugerida, 'P0 · k^(t/3)'), reduzindo o caráter de 'elaborar problema' da habilidade — a questão pede para resolver mais do que para elaborar. A articulação entre 'calcular' e 'interpretar' existe, mas o peso maior está no cálculo (itens a e b), não na elaboração/criação de um modelo genuinamente novo.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — O problema é uma variação quase canônica do exercício-padrão 'bactérias que triplicam a cada X horas', presente em praticamente todo livro didático de função exponencial. Na resolução, a fórmula P(t)=P0·k^(t/3) já é fornecida ao aluno como estrutura pronta (efeito Topaze), eliminando a necessidade de o estudante decidir a forma da lei — o que esvazia o suposto nível 'criar'. O contexto é significativo, mas o formato e a condução são bastante previsíveis.
  - *sugestões:* 1) Para justificar o nível 'criar', reformule o item (a) retirando a estrutura pronta 'P0 · k^(t/3)' da resolução esperada e do enunciado; peça explicitamente que o aluno decida e justifique a forma geral da função (por exemplo, comparando com um crescimento linear e explicando por que ele é inadequado), de modo que haja genuína elaboração de um modelo, não apenas substituição de valores em um molde dado. 2) Enriqueça o problema com um elemento que exija decisão além do cálculo direto — por exemplo, pedir para comparar duas estratégias de modelagem (base 3 elevada a t/3 vs. uma taxa de crescimento por hora, calculando essa taxa) e justificar qual é mais adequada, articulando de fato 'elaborar' com 'interpretar'. 3) Para aumentar a originalidade, mude o contexto padrão de bactérias para outro cenário de crescimento exponencial (ex.: propagação de um boato, valorização de um investimento, decaimento de medicamento no sangue) ou insira dados não didaticamente 'redondos' (ex.: triplicar a cada 3,5h) para evitar a resolução mecânica por reconhecimento de padrão. 4) Explicite melhor no item (c) uma pergunta que force relacionar a taxa de crescimento com uma grandeza do mundo real (ex.: 'que implicações práticas isso tem para o controle da cultura?'), fortalecendo o nível relacional (SOLO) e a interpretação de variação exigida pela habilidade.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Para justificar o nível 'criar', reformule o item (a) retirando a estrutura pronta 'P0 · k^(t/3)' da resolução esperada e do enunciado; peça explicitamente que o aluno decida e justifique a forma geral da função (por exemplo, comparando com um crescimento linear e explicando por que ele é inadequado), de modo que haja genuína elaboração de um modelo, não apenas substituição de valores em um molde dado. 2) Enriqueça o problema com um elemento que exija decisão além do cálculo direto — por exemplo, pedir para comparar duas estratégias de modelagem (base 3 elevada a t/3 vs. uma taxa de crescimento por hora, calculando essa taxa) e justificar qual é mais adequada, articulando de fato 'elaborar' com 'interpretar'. 3) Para aumentar a originalidade, mude o contexto padrão de bactérias para outro cenário de crescimento exponencial (ex.: propagação de um boato, valorização de um investimento, decaimento de medicamento no sangue) ou insira dados não didaticamente 'redondos' (ex.: triplicar a cada 3,5h) para evitar a resolução mecânica por reconhecimento de padrão. 4) Explicite melhor no item (c) uma pergunta que force relacionar a taxa de crescimento com uma grandeza do mundo real (ex.: 'que implicações práticas isso tem para o controle da cultura?'), fortalecendo o nível relacional (SOLO) e a interpretação de variação exigida pela habilidade.

### Iteração 2

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 40*3**n: reproduz os 4 pontos dados; coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(21/2) = 1080). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [7*(3*log(5) + 2*I*pi)/(2*log(3))].
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - equacao=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 40*3**n: reproduz os 4 pontos dados; coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(21/2) = 1080). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [7*(3*log(5) + 2*I*pi)/(2*log(3))]. Resultado calculado independentemente: 40*3**n | f(21/2) = 1080 | crescente em Interval(-oo, oo) | [7*(3*log(5) + 2*I*pi)/(2*log(3)), 21*log(5)/(2*log(3))]. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 40*3**n: reproduz os 4 pontos dados; coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(6) = 29160). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (tabela), variável e condições explícitas em cada item. Não há ambiguidade sobre o que é dado e o que se pede em a, b, c, d.
  - adequacao_nivel: 2/5 — O nível declarado é 'criar' (Bloom), mas nenhum item exige produção de algo genuinamente novo: (a) é reconhecimento de padrão e ajuste de parâmetros em fórmula já dada (b^n·a), tarefa típica de 'aplicar/analisar'; (b) e (d) são cálculo/resolução direta ('aplicar'); (c) é justificativa qualitativa ('compreender/analisar'). Não há elaboração de problema, modelo alternativo ou síntese de algo inédito pelo aluno. A estrutura de resposta esperada é predominantemente multiestrutural/relacional (SOLO), não extensa abstrata como demandaria 'criar'.
  - alinhamento_bncc: 4/5 — A questão cumpre bem as exigências específicas listadas: exige compreensão e interpretação da variação (item c pede justificar o crescimento e traduzir a razão em variação percentual, sem recorrer a cálculo mecânico) e usa contexto realista de crescimento de seres microscópicos, como pede a habilidade. O único ponto não atendido é a dimensão 'elaborar problemas' presente no texto da habilidade EM13MAT304 — a questão apenas resolve, não pede ao aluno formular um problema análogo. Isso limita, mas não invalida, o alinhamento.
  - distratores: 5/5 — Não se aplica: questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de crescimento bacteriano com triplicação horária é um clássico recorrente em livros didáticos; a estrutura (tabela + PG + potência + equação exponencial) segue o roteiro tradicional sem inovação de contexto ou de abordagem. Não há efeito Topaze evidente, mas também não há elemento diferenciador que evite a sensação de exercício-padrão.
  - *sugestões:* Para alinhar a questão ao nível 'criar' declarado, é preciso incluir uma etapa em que o aluno efetivamente produza algo novo, e não apenas aplique/interprete um modelo já fornecido. Sugestões concretas: (1) Substituir o item (a) por uma tarefa em que o aluno, a partir de uma descrição verbal (sem tabela pronta), tenha que propor e justificar seu próprio modelo, testando-o contra dados brutos e decidindo entre modelo linear e exponencial (isso já seria 'analisar/avaliar'); (2) Acrescentar um item (e) pedindo que o aluno elabore um problema análogo (mudando razão, população inicial ou contexto — ex.: decaimento radioativo ou juros compostos) e resolva-o, explicitando os critérios de construção, o que caracteriza genuinamente 'criar' na taxonomia de Bloom; (3) Alternativamente, se a intenção é manter a questão como está, corrigir a especificação para declarar o nível cognitivo real predominante ('aplicar' ou 'analisar'), evitando incompatibilidade entre o Bloom declarado e o exigido. Também recomenda-se diversificar o contexto (explorar variação de temperatura, concentração de medicamento no sangue, ou outro cenário de crescimento/decaimento) para reduzir a semelhança com o exercício-padrão de bactérias que triplicam.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para alinhar a questão ao nível 'criar' declarado, é preciso incluir uma etapa em que o aluno efetivamente produza algo novo, e não apenas aplique/interprete um modelo já fornecido. Sugestões concretas: (1) Substituir o item (a) por uma tarefa em que o aluno, a partir de uma descrição verbal (sem tabela pronta), tenha que propor e justificar seu próprio modelo, testando-o contra dados brutos e decidindo entre modelo linear e exponencial (isso já seria 'analisar/avaliar'); (2) Acrescentar um item (e) pedindo que o aluno elabore um problema análogo (mudando razão, população inicial ou contexto — ex.: decaimento radioativo ou juros compostos) e resolva-o, explicitando os critérios de construção, o que caracteriza genuinamente 'criar' na taxonomia de Bloom; (3) Alternativamente, se a intenção é manter a questão como está, corrigir a especificação para declarar o nível cognitivo real predominante ('aplicar' ou 'analisar'), evitando incompatibilidade entre o Bloom declarado e o exigido. Também recomenda-se diversificar o contexto (explorar variação de temperatura, concentração de medicamento no sangue, ou outro cenário de crescimento/decaimento) para reduzir a semelhança com o exercício-padrão de bactérias que triplicam.
