# Ciclo 045 — EM13MAT303

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

Uma corretora oferece uma aplicação inicial de R$ 2.000,00 sujeita a juros compostos de 4% ao mês, incidentes sempre sobre o saldo do mês anterior (e não sobre o capital inicial). Um colega de turma afirma que esse crescimento poderia ser descrito de forma equivalente por um acréscimo fixo de R$ 80,00 por mês (4% do capital inicial), gerando uma progressão aritmética. Elabore a expressão correta $M(t)$ que modela o saldo da aplicação após $t$ meses inteiros e utilize-a para determinar o primeiro mês inteiro em que esse saldo ultrapassa R$ 3.000,00. Assinale a alternativa que apresenta, ao mesmo tempo, a expressão correta de $M(t)$ e a resposta correta para esse mês.

## Alternativas

- (a) $M(t) = 2000 + 80t$; o saldo ultrapassa R$ 3.000,00 no mês $t = 13$.
  - *erro representado:* Tratou o crescimento como linear (juros simples com acréscimo fixo baseado no capital inicial), ignorando que os juros compostos incidem sobre o saldo acumulado, o que gera crescimento exponencial e não aritmético.
- (b) $M(t) = 2000\cdot(1{,}04)^t$; o saldo ultrapassa R$ 3.000,00 no mês $t = 10$.
  - *erro representado:* Usou a expressão exponencial corretamente, mas arredondou o valor não inteiro de $t$ (≈10,34) para baixo em vez de para cima, esquecendo que é preciso o primeiro mês em que a desigualdade estrita é satisfeita.
- (c) $M(t) = 2000\cdot(1{,}04)^t$; o saldo ultrapassa R$ 3.000,00 no mês $t = 11$.  ← correta
- (d) $M(t) = 2000\cdot(1{,}04)^t$; o saldo ultrapassa R$ 3.000,00 no mês $t = 18$.
  - *erro representado:* Confundiu o valor de referência do problema (R$3.000,00) com o dobro do capital inicial (R$4.000,00), resolvendo a equação para o valor errado e obtendo o mês em que o saldo dobra em vez do mês em que ultrapassa R$3.000,00.

## Gabarito

M(t) = 2000·(1,04)^t; o saldo ultrapassa R$3.000,00 no mês t = 11.

## Resolução

**1. Testando a afirmação do colega (modelo linear):**

Se o saldo crescesse em progressão aritmética, teríamos $M(t) = 2000 + 80t$. Note que essa expressão soma sempre a mesma *quantia* a cada mês — a diferença entre saldos consecutivos é constante, o que é típico de crescimento linear, não do que ocorre em juros compostos.

**2. Construindo o modelo correto (juros compostos):**

Como os juros incidem sobre o saldo anterior, cada mês o saldo é multiplicado pelo mesmo fator $1 + 0{,}04 = 1{,}04$. Assim:

$$M(0) = 2000,\quad M(1) = 2000\cdot 1{,}04,\quad M(2) = 2000\cdot 1{,}04^2,\ \dots$$

A razão entre saldos consecutivos é constante:
$$\frac{M(t+1)}{M(t)} = 1{,}04 \quad \text{para todo } t,$$

que é a marca do crescimento **exponencial** (diferente da diferença constante da progressão aritmética do colega). Logo, o modelo correto é:
$$M(t) = 2000\cdot(1{,}04)^t.$$

**3. Resolvendo a extrapolação pedida:**

Queremos o menor $t$ inteiro tal que $M(t) > 3000$:
$$2000\cdot(1{,}04)^t > 3000 \ \Longrightarrow\ (1{,}04)^t > 1{,}5.$$

Aplicando logaritmo:
$$t > \frac{\log(1{,}5)}{\log(1{,}04)} \approx \frac{0{,}4055}{0{,}0392} \approx 10{,}34.$$

Como $t$ deve ser inteiro, o menor valor que satisfaz a desigualdade é $t = 11$.

**4. Conferindo:**

- $M(10) = 2000\cdot(1{,}04)^{10} \approx 2960{,}49 < 3000$
- $M(11) = 2000\cdot(1{,}04)^{11} \approx 3078{,}91 > 3000$

Portanto, $M(t) = 2000\cdot(1{,}04)^t$ e o primeiro mês inteiro em que o saldo ultrapassa R$ 3.000,00 é $t = 11$.

## Formalização verificável

- `propriedade` — expressão `2000*(Rational(26,25))**n`, esperado `2000*(Rational(26,25))**n`, parâmetros `{'sequencia': 'pg', 'a1': '2000', 'razao': 'Rational(26,25)'}`
- `equacao` — expressão `Eq(2000*(Rational(26,25))**t, 3000)`, esperado `[log(Rational(3,2))/log(Rational(26,25))]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 2 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 150*(27/25)**x vale 162 em x=1, mas o 1º termo da PG é 150. | (2) aprovado: Gabarito confirmado (f(3) = 118098/625).
  - propriedade=rejeitado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 2 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 150*(27/25)**x vale 162 em x=1, mas o 1º termo da PG é 150. | (2) aprovado: Gabarito confirmado (f(3) = 118098/625). Resultado calculado independentemente: a expressão 150*(27/25)**x vale 162 em x=1, mas o 1º termo da PG é 150 | f(3) = 118098/625. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(3) = 118098/625). | (2) aprovado: Propriedades confirmadas para 150*(27/25)**n: coincide com a PG declarada.
  - funcao/valor=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado objetivo, com dados completos (capital, taxa, período) e pedido único e inequívoco. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 1/5 — A especificação declara Bloom 'criar', mas a tarefa exigida é apenas substituir valores numa fórmula pronta e calcular um número — isto é, no máximo 'aplicar', com estrutura SOLO unistrutural/multiestrutural (uma única operação em cadeia). Não há elaboração, formulação de problema, comparação de estratégias ou produção de algo novo, como o verbo 'criar' exigiria.
  - alinhamento_bncc: 2/5 — A questão envolve juros compostos (primeira exigência atendida), mas não cumpre a segunda: o caráter exponencial do crescimento não é evidenciado para o aluno no enunciado — ele só precisa calcular um valor final. A destacamento da exponencialidade aparece apenas na resolução do professor, não é algo que o estudante precise perceber, comparar ou justificar ao responder. Também não há qualquer traço de 'elaborar problemas', que a habilidade também prevê.
  - distratores: 5/5 — Os quatro distratores mapeiam erros típicos e plausíveis: confundir com juros simples, esquecer o capital inicial, e errar o número de períodos. Nenhum é absurdo ou eliminável de imediato.
  - originalidade: 2/5 — Contexto de 'investidor aplicando dinheiro a juros compostos' é o exemplo mais canônico e repetido de livros didáticos, sem elemento que torne o problema significativo ou inesperado. A resolução até entrega o caminho (identifica PG, expõe a fórmula) de modo que reforça o padrão mecânico de resolução.
  - *sugestões:* Reformular a tarefa para que exija efetivamente 'criar', não apenas calcular: por exemplo, peça ao aluno que compare dois cenários (juros simples vs. compostos) e justifique/demonstre por que um deles gera crescimento exponencial, ou que elabore uma expressão geral M(t) válida para qualquer t e a use para responder a uma pergunta que exija extrapolação (ex.: em que mês o montante dobra). Alternativamente, peça que o aluno construa um problema análogo com outro capital/taxa e resolva, atendendo à parte 'elaborar problemas' da habilidade. É importante que o enunciado, e não apenas a resolução do professor, obrigue o estudante a evidenciar o crescimento exponencial (por exemplo, perguntando explicitamente por que o crescimento não é linear, ou pedindo a razão constante entre montantes sucessivos). Também recomenda-se trocar o contexto por algo menos repetitivo dos livros didáticos, com dados ou situação mais autêntica (ex.: comparação de dois planos de investimento reais, dados de aplicação financeira atual).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformular a tarefa para que exija efetivamente 'criar', não apenas calcular: por exemplo, peça ao aluno que compare dois cenários (juros simples vs. compostos) e justifique/demonstre por que um deles gera crescimento exponencial, ou que elabore uma expressão geral M(t) válida para qualquer t e a use para responder a uma pergunta que exija extrapolação (ex.: em que mês o montante dobra). Alternativamente, peça que o aluno construa um problema análogo com outro capital/taxa e resolva, atendendo à parte 'elaborar problemas' da habilidade. É importante que o enunciado, e não apenas a resolução do professor, obrigue o estudante a evidenciar o crescimento exponencial (por exemplo, perguntando explicitamente por que o crescimento não é linear, ou pedindo a razão constante entre montantes sucessivos). Também recomenda-se trocar o contexto por algo menos repetitivo dos livros didáticos, com dados ou situação mais autêntica (ex.: comparação de dois planos de investimento reais, dados de aplicação financeira atual).

### Iteração 3

- **Verificador:** rejeitado — 1 de 2 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 2000*(26/25)**n vale 2080 em n=1, mas o 1º termo da PG é 2000. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=rejeitado
  - equacao=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 2 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 2000*(26/25)**n vale 2080 em n=1, mas o 1º termo da PG é 2000. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. Resultado calculado independentemente: a expressão 2000*(26/25)**n vale 2080 em n=1, mas o 1º termo da PG é 2000 | [log((2/3)**(1/log(25/26)))]. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
