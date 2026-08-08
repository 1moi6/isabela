# Ciclo 043 — EM13MAT303

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Um capital inicial de R$ 1000,00 é aplicado a juros compostos, com uma taxa fixa de 5% ao mês incidindo sobre o montante do mês anterior (juros sobre juros, sem depósitos ou retiradas adicionais).

a) Escreva a expressão algébrica que fornece o montante $C(n)$, em reais, após $n$ meses de aplicação, em função de $n$.

b) Usando a expressão obtida em (a), calcule o valor exato do montante após 4 meses, $C(4)$.

c) Analise a razão $\dfrac{C(n+1)}{C(n)}$ e explique por que esse tipo de crescimento é exponencial, e não linear.

## Gabarito

a) $C(n) = 1000\left(\dfrac{21}{20}\right)^n$; b) $C(4) = \dfrac{194481}{160} = R\$\,1215{,}50625$; c) $\dfrac{C(n+1)}{C(n)} = \dfrac{21}{20} = 1{,}05$ é constante para todo $n$, o que caracteriza uma progressão geométrica e, portanto, um crescimento exponencial (diferente do crescimento linear, em que a diferença entre termos consecutivos é que seria constante).

## Resolução

**a) Construção da expressão**

A cada mês, o montante do mês anterior é multiplicado pelo fator $(1 + 0{,}05) = 1{,}05 = \dfrac{21}{20}$, pois os juros de 5% incidem sobre o valor já acumulado (juros compostos). Assim, a sequência de montantes é uma progressão geométrica de primeiro termo $C(0) = 1000$ e razão $q = \dfrac{21}{20}$:

$$C(n) = 1000\left(\frac{21}{20}\right)^n$$

em que $n$ é o número de meses decorridos.

**b) Cálculo de $C(4)$**

$$C(4) = 1000\left(\frac{21}{20}\right)^4 = 1000\cdot\frac{21^4}{20^4} = 1000\cdot\frac{194481}{160000} = \frac{194481}{160} = 1215{,}50625$$

Logo, $C(4) = R\$\,1215{,}50625$.

**c) Razão entre termos consecutivos**

$$\frac{C(n+1)}{C(n)} = \frac{1000\left(\frac{21}{20}\right)^{n+1}}{1000\left(\frac{21}{20}\right)^{n}} = \frac{21}{20} = 1{,}05$$

Essa razão é **constante e igual a 1,05 para qualquer $n$**, ou seja, o montante é sempre multiplicado pelo mesmo fator a cada mês — essa é justamente a definição de progressão geométrica, e é isso que caracteriza uma função exponencial.

Em um crescimento **linear** (progressão aritmética), o que seria constante é a **diferença** $C(n+1) - C(n)$ (um acréscimo fixo em reais a cada mês). Aqui, ao contrário, essa diferença cresce mês a mês (pois os juros incidem sobre um montante cada vez maior), enquanto o **quociente** entre termos consecutivos permanece fixo em 21/20. É exatamente essa razão constante multiplicativa — e não uma diferença constante — que evidencia o crescimento exponencial dos juros compostos.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `1000*(21/20)**n`, parâmetros `{'sequencia': 'pg', 'a1': '1000', 'razao': 'Rational(21,20)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 1000*(11/10)**n: coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(3) = 1331). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é claro e completo: capital inicial, taxa e período estão bem definidos, e os itens (a) e (b) delimitam exatamente o que se pede (lei de formação, justificativa, cálculo numérico e percentual). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O nível declarado é 'criar' (Bloom), mas as tarefas exigidas — escrever uma fórmula que decorre diretamente da definição de juros compostos, justificar uma distinção conceitual (exponencial vs. PA) e efetuar um cálculo — correspondem, no máximo, a 'aplicar/analisar'. Em termos de SOLO, a resposta esperada é relacional (integra fórmula, justificativa e cálculo), não multiestrutural, mas está bem distante de uma estrutura estendida abstrata típica de 'criar' (não há elaboração de problema novo, modelo original ou generalização). Há descompasso entre o nível cognitivo declarado e o efetivamente demandado.
  - alinhamento_bncc: 4/5 — A questão cumpre as duas exigências específicas listadas: envolve juros compostos e evidencia claramente o crescimento exponencial (item a exige justificar a natureza exponencial vs. PA; item b compara 33,1% com 3×10%=30%, tornando o efeito multiplicativo explícito). O único ponto que reduz a nota é que a habilidade BNCC menciona também 'elaborar problemas', e a questão restringe-se a resolver, sem exigir do aluno a formulação de um problema análogo.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — O enunciado reproduz o modelo clássico e recorrente de livros didáticos ('capital inicial em unidades monetárias abstratas, taxa fixa, calcule C(n)'), sem contexto significativo ou aplicado. Além disso, o próprio enunciado antecipa a resposta ao pedir explicitamente a comparação com PA e ao estruturar passo a passo (fórmula → justificativa → cálculo → percentual), configurando efeito Topaze: o caminho da resolução já está todo pavimentado, restando pouco espaço para investigação autêntica do aluno.
  - *sugestões:* 1) Ajustar o nível cognitivo: se o objetivo é realmente 'criar', peça ao aluno para elaborar um problema original envolvendo juros compostos (por exemplo, propor um cenário com dois capitais/taxas diferentes e pedir que ele formule e resolva uma questão de comparação, ou generalize a fórmula para taxa variável). Caso contrário, reclassifique o nível Bloom para 'aplicar' ou 'analisar', que é o que a tarefa atual efetivamente demanda. 2) Inserir um contexto significativo e não abstrato (ex.: financiamento real, investimento em conta específica, comparação entre bancos) para aumentar a relevância e reduzir o efeito de exercício descontextualizado. 3) Remover ou reformular a pista explícita 'justifique por que é exponencial e não uma progressão aritmética', que entrega a resposta; em vez disso, peça que o aluno investigue e classifique o tipo de crescimento por conta própria, comparando diferenças e razões sucessivas sem sugerir a resposta esperada. 4) Se a intenção é atender integralmente à habilidade EM13MAT303, considere acrescentar uma etapa em que o aluno precise elaborar (não apenas resolver) uma situação-problema envolvendo juros compostos, articulando-a com porcentagem em outro contexto (ex.: desconto, inflação) para reforçar a natureza de 'elaborar problemas' prevista na BNCC.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar o nível cognitivo: se o objetivo é realmente 'criar', peça ao aluno para elaborar um problema original envolvendo juros compostos (por exemplo, propor um cenário com dois capitais/taxas diferentes e pedir que ele formule e resolva uma questão de comparação, ou generalize a fórmula para taxa variável). Caso contrário, reclassifique o nível Bloom para 'aplicar' ou 'analisar', que é o que a tarefa atual efetivamente demanda. 2) Inserir um contexto significativo e não abstrato (ex.: financiamento real, investimento em conta específica, comparação entre bancos) para aumentar a relevância e reduzir o efeito de exercício descontextualizado. 3) Remover ou reformular a pista explícita 'justifique por que é exponencial e não uma progressão aritmética', que entrega a resposta; em vez disso, peça que o aluno investigue e classifique o tipo de crescimento por conta própria, comparando diferenças e razões sucessivas sem sugerir a resposta esperada. 4) Se a intenção é atender integralmente à habilidade EM13MAT303, considere acrescentar uma etapa em que o aluno precise elaborar (não apenas resolver) uma situação-problema envolvendo juros compostos, articulando-a com porcentagem em outro contexto (ex.: desconto, inflação) para reforçar a natureza de 'elaborar problemas' prevista na BNCC.

### Iteração 2

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (f(4) = 194481/160). | (2) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-31/20 - 11*sqrt(3)*I/20, -31/20 + 11*sqrt(3)*I/20]. | (3) aprovado: Propriedades confirmadas para 1000*(21/20)**n: coincide com a PG declarada.
  - funcao/valor=aprovado
  - equacao=rejeitado
  - propriedade=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (f(4) = 194481/160). | (2) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-31/20 - 11*sqrt(3)*I/20, -31/20 + 11*sqrt(3)*I/20]. | (3) aprovado: Propriedades confirmadas para 1000*(21/20)**n: coincide com a PG declarada. Resultado calculado independentemente: f(4) = 194481/160 | [1/10, -31/20 - 11*sqrt(3)*I/20, -31/20 + 11*sqrt(3)*I/20] | 1000*(21/20)**n. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Propriedades confirmadas para 1000*(21/20)**n: coincide com a PG declarada.
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado sem ambiguidades: capital, taxa, regime (juros compostos) e o que é pedido em cada item estão explícitos e completos. Não há duplo sentido lexical ou lacunas de dados.
  - adequacao_nivel: 2/5 — A especificação declara Bloom 'criar', mas a tarefa real exige apenas: (a) aplicar/entender uma fórmula de PG, (b) aplicar/calcular um valor numérico, (c) analisar/explicar uma razão constante — no máximo nível 'analisar', com estrutura SOLO relacional. Não há produção de algo novo pelo aluno (elaborar um problema, propor um modelo, sintetizar cenários inéditos), que é o que 'criar' exigiria. Há descompasso claro entre o nível declarado e o processo cognitivo efetivamente demandado.
  - alinhamento_bncc: 4/5 — As duas exigências explícitas da especificação são cumpridas: a questão envolve juros compostos e o item (c) evidencia de forma explícita o caráter exponencial (razão constante vs. diferença constante). Falta, porém, a dimensão de 'elaborar problemas' presente no texto da habilidade EM13MAT303 — a questão é puramente de resolução, sem exigir do aluno a criação/formulação de um problema análogo ou variante, o que reduz o alinhamento pleno com a habilidade tal como formulada.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto (capital, taxa mensal, montante em n meses) é o modelo mais clássico e recorrente de livros didáticos sobre juros compostos, sem elemento de contextualização significativa (situação realista, dado externo, tomada de decisão). O item (c), que pede a comparação conceitual razão constante vs. diferença constante, adiciona algum valor reflexivo e evita o efeito Topaze parcialmente, mas não é suficiente para tornar a questão distintiva ou aplicada a um cenário significativo.
  - *sugestões:* 1) Ajustar o nível cognitivo: ou (i) alterar a especificação de Bloom para 'analisar' (mais compatível com o que a questão de fato pede), ou (ii) reformular a questão para efetivamente demandar 'criar' — por exemplo, pedir que o aluno elabore/proponha um novo problema de juros compostos com dados diferentes (outra taxa, outro capital, outro contexto: financiamento, poupança, dívida) e que ele mesmo construa a expressão geral, calcule e justifique o crescimento exponencial nesse cenário autoral, em vez de apenas aplicar a fórmula dada. 2) Para reforçar o alinhamento com a habilidade completa (resolver E elaborar), incluir um item (d) do tipo: 'Elabore uma situação-problema distinta (outro contexto de aplicação financeira) que também resulte em crescimento exponencial e explique por quê.' 3) Para aumentar a originalidade, substituir o contexto genérico de 'capital aplicado' por uma situação mais concreta e significativa (ex.: comparação entre duas opções de investimento, ou decisão de quando resgatar um valor), evitando o padrão-livro-didático puro.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar o nível cognitivo: ou (i) alterar a especificação de Bloom para 'analisar' (mais compatível com o que a questão de fato pede), ou (ii) reformular a questão para efetivamente demandar 'criar' — por exemplo, pedir que o aluno elabore/proponha um novo problema de juros compostos com dados diferentes (outra taxa, outro capital, outro contexto: financiamento, poupança, dívida) e que ele mesmo construa a expressão geral, calcule e justifique o crescimento exponencial nesse cenário autoral, em vez de apenas aplicar a fórmula dada. 2) Para reforçar o alinhamento com a habilidade completa (resolver E elaborar), incluir um item (d) do tipo: 'Elabore uma situação-problema distinta (outro contexto de aplicação financeira) que também resulte em crescimento exponencial e explique por quê.' 3) Para aumentar a originalidade, substituir o contexto genérico de 'capital aplicado' por uma situação mais concreta e significativa (ex.: comparação entre duas opções de investimento, ou decisão de quando resgatar um valor), evitando o padrão-livro-didático puro.
