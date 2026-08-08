# Ciclo 031 — EM13MAT303

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

Um mesmo capital inicial de R$ 1.000,00 é aplicado, ao mesmo tempo, em duas propostas de investimento, ambas por um número inteiro $n$ de meses:

**Proposta A:** a cada mês, o investidor recebe sempre um rendimento igual a 6% do capital inicial (o rendimento de cada mês é somado ao montante do mês anterior, mas o percentual incide sempre sobre os R$ 1.000,00 iniciais).

**Proposta B:** a cada mês, o capital acumulado do mês anterior é multiplicado por 1,04 (ou seja, o capital cresce 4% em relação ao valor já acumulado até aquele momento).

Com base nessa descrição, resolva:

**a)** Sem usar nenhuma fórmula pronta de juros, escreva você mesmo(a) a expressão que fornece o montante $M_A(n)$ da Proposta A e a expressão que fornece o montante $M_B(n)$ da Proposta B, ambas em função do número de meses $n$. Explique, em poucas linhas, o raciocínio usado para construir cada expressão a partir da descrição do enunciado.

**b)** Calcule $M_A(n)$ e $M_B(n)$ para $n = 6, 12, 18$ e $24$ meses. A partir desses valores, identifique a partir de qual desses meses a Proposta B passa a render mais do que a Proposta A, e explique por que esse comportamento é esperado, dado o tipo de crescimento de cada proposta.

**c)** Elabore uma nova proposta de investimento, mantendo o mesmo tipo de crescimento da Proposta B mas mudando a taxa mensal (por exemplo, 3% ou 5%) e o capital inicial (diferente de R$ 1.000,00). Escreva a expressão do montante dessa nova proposta e formule uma pergunta sobre ela que exija comparar seu crescimento com o de uma proposta de juros simples equivalente — sem precisar resolvê-la.

## Gabarito

a) $M_A(n) = 1000 + 60n$ (função afim/PA); $M_B(n) = 1000(1,04)^n$ (função exponencial/PG). b) Entre os meses testados, $M_A$ é maior até $n=18$ ($2080 > 2025,82$), e a Proposta B ultrapassa a Proposta A em $n=24$ ($2563,31 > 2440$), pois seu crescimento é exponencial e o de A é linear. c) Resposta aberta: é válida qualquer expressão do tipo $C_0(1+i)^n$, com $C_0\neq 1000$ e $i \neq 0,04$, acompanhada de uma pergunta que compare esse crescimento com o de uma aplicação de juros simples equivalente.

## Resolução

**a) Construção das expressões**

*Proposta A:* a cada mês soma-se sempre a mesma quantia, $6\%$ de $1000$, isto é, $60$ reais. Depois de $n$ meses, foram somadas $n$ parcelas de $60$:
$$M_A(n) = 1000 + 60n.$$
Essa é uma função **afim** (crescimento linear) — o mesmo padrão de uma PA de primeiro termo $1000$ e razão $60$.

*Proposta B:* a cada mês o valor do mês anterior é multiplicado por $1,04$. Assim:
$M_B(1)=1000\cdot 1,04$, $M_B(2)=1000\cdot 1,04^2$, e em geral
$$M_B(n) = 1000\cdot (1,04)^n = 1000\left(\dfrac{26}{25}\right)^n.$$
Essa é uma função **exponencial** — o mesmo padrão de uma PG de primeiro termo $1000$ e razão $1,04$.

**b) Cálculo dos montantes**

| $n$ | $M_A(n)=1000+60n$ | $M_B(n)=1000(1,04)^n$ |
|---|---|---|
| 6 | $1360$ | $\approx 1265,32$ |
| 12 | $1720$ | $\approx 1601,03$ |
| 18 | $2080$ | $\approx 2025,82$ |
| 24 | $2440$ | $\approx 2563,31$ |

Até $n=18$, $M_A(n) > M_B(n)$: o crescimento linear ainda está à frente. Mas em $n=24$, $M_B(n) = 2563,31 > M_A(n) = 2440$: a Proposta B ultrapassou a Proposta A.

Isso é esperado porque $M_A(n)$ cresce **sempre a mesma quantidade fixa** por mês (60 reais), enquanto $M_B(n)$ cresce a uma **porcentagem do valor já acumulado**: à medida que o capital aumenta, o incremento absoluto de B também aumenta, fazendo seu crescimento se acelerar (crescimento exponencial), até superar o crescimento constante de A.

**c) Elaboração de uma nova proposta (resposta aberta, exemplo de solução aceitável)**

Exemplo: capital inicial de R$ 2.000,00, taxa de 3% ao mês, com juros compostos:
$$M_C(n) = 2000\,(1,03)^n.$$
Pergunta criada: *"Se um investidor colocasse os mesmos R$ 2.000,00 em uma aplicação de juros simples de 5% ao mês, a partir de qual mês a Proposta C (juros compostos a 3%) ultrapassaria essa aplicação de juros simples, mesmo tendo uma taxa mensal menor?"*
Qualquer proposta análoga é válida, desde que: (i) a expressão do montante tenha a forma $C_0\cdot(1+i)^n$ com $C_0 \neq 1000$ e $i$ diferente de $0,04$; (ii) a pergunta formulada exija comparar esse crescimento exponencial com um crescimento linear (juros simples) equivalente.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `60*n + 1000`, parâmetros `{'sequencia': 'pa', 'a1': '1000', 'razao': '60'}`
- `propriedade` — expressão `-`, esperado `1000*(Rational(26,25))**n`, parâmetros `{'sequencia': 'pg', 'a1': '1000', 'razao': 'Rational(26,25)'}`
- `funcao` — expressão `1000 + 60*n`, esperado `2080`, parâmetros `{'consulta': 'valor', 'ponto': '18'}`
- `funcao` — expressão `1000*(Rational(26,25))**n`, esperado `2025.82`, parâmetros `{'consulta': 'valor', 'ponto': '18'}`
- `funcao` — expressão `1000 + 60*n`, esperado `2440`, parâmetros `{'consulta': 'valor', 'ponto': '24'}`
- `funcao` — expressão `1000*(Rational(26,25))**n`, esperado `2563.31`, parâmetros `{'consulta': 'valor', 'ponto': '24'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 800*(21/20)**n vale 840 em n=1, mas o 1º termo da PG é 800. | (2) aprovado: Gabarito confirmado (f(6) = 85766121/80000). | (3) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=rejeitado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 800*(21/20)**n vale 840 em n=1, mas o 1º termo da PG é 800. | (2) aprovado: Gabarito confirmado (f(6) = 85766121/80000). | (3) aprovado: Gabarito confirmado (crescente em Reals). Resultado calculado independentemente: a expressão 800*(21/20)**n vale 840 em n=1, mas o 1º termo da PG é 800 | f(6) = 85766121/80000 | crescente em Reals. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 800*(21/20)**(n - 1): coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(6) = 4084101/4000). | (3) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado explicita dados (capital, taxa, período), pede claramente três produtos (expressão, valor numérico, classificação) e não há ambiguidade lexical ou estrutural. Falta apenas informar a unidade de C(n) de forma mais explícita, mas isso não gera dúvida real.
  - adequacao_nivel: 2/5 — O nível declarado é 'criar', mas a tarefa efetiva é 'aplicar/entender': o próprio enunciado já fornece a estrutura da PG (primeiro termo e razão 1+i), reduzindo o item (a) a uma substituição direta na fórmula do termo geral. O item (b) é cálculo numérico e o item (c) é justificação simples com base no valor da razão — nada exige que o aluno produza, planeje ou sintetize um modelo novo. Em termos SOLO, a resposta esperada é multiestrutural/relacional, não estendida abstrata como exigiria 'criar'.
  - alinhamento_bncc: 4/5 — Atende às exigências específicas listadas: envolve juros compostos (não porcentagem isolada) e evidencia o crescimento exponencial explicitamente nos itens (a) e (c). Não contempla, porém, a dimensão de 'elaborar problemas' presente no texto completo da habilidade EM13MAT303, ficando restrita a resolver um problema já elaborado.
  - distratores: 5/5 — não se aplica
  - originalidade: 2/5 — O contexto é o clássico 'capital aplicado a juros compostos' de livro didático, sem elemento significativo ou situação real diferenciada. Além disso, o enunciado comete efeito Topaze acentuado: informa antecipadamente que C(n) é uma PG com primeiro termo 800 e razão 1+i, entregando ao aluno a estrutura da solução antes mesmo de ele precisar identificá-la.
  - *sugestões:* 1) Reformular para exigir efetivamente o nível 'criar': por exemplo, pedir que o aluno elabore/compare duas situações de investimento (juros simples vs. compostos, ou duas taxas diferentes) e construa por si só o modelo matemático, sem fornecer de antemão que se trata de uma PG com razão 1+i — deixe que o aluno identifique essa estrutura a partir do contexto. 2) Remover a frase que entrega a fórmula ('cujo primeiro termo é C1=800 e cuja razão corresponde ao fator 1+i'), pois isso configura efeito Topaze; substitua por uma descrição da situação (ex.: 'a cada período o capital anterior é multiplicado por 1,05') e peça que o próprio aluno reconheça e escreva a expressão. 3) Enriquecer o contexto com um cenário mais significativo (ex.: financiamento, poupança para um objetivo específico, comparação de instituições financeiras) para aumentar a originalidade e a aplicabilidade. 4) Incluir uma etapa de síntese/produção, como pedir ao aluno que crie uma nova pergunta ou problema análogo variando taxa ou capital, para justificar o nível Bloom 'criar' declarado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reformular para exigir efetivamente o nível 'criar': por exemplo, pedir que o aluno elabore/compare duas situações de investimento (juros simples vs. compostos, ou duas taxas diferentes) e construa por si só o modelo matemático, sem fornecer de antemão que se trata de uma PG com razão 1+i — deixe que o aluno identifique essa estrutura a partir do contexto. 2) Remover a frase que entrega a fórmula ('cujo primeiro termo é C1=800 e cuja razão corresponde ao fator 1+i'), pois isso configura efeito Topaze; substitua por uma descrição da situação (ex.: 'a cada período o capital anterior é multiplicado por 1,05') e peça que o próprio aluno reconheça e escreva a expressão. 3) Enriquecer o contexto com um cenário mais significativo (ex.: financiamento, poupança para um objetivo específico, comparação de instituições financeiras) para aumentar a originalidade e a aplicabilidade. 4) Incluir uma etapa de síntese/produção, como pedir ao aluno que crie uma nova pergunta ou problema análogo variando taxa ou capital, para justificar o nível Bloom 'criar' declarado.

### Iteração 3

- **Verificador:** rejeitado — 4 de 6 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 60*n + 1000 vale 1060 em n=1, mas o 1º termo da PA é 1000. | (2) rejeitado: Propriedade não confirmada: a expressão 1000*(26/25)**n vale 1040 em n=1, mas o 1º termo da PG é 1000. | (3) aprovado: Gabarito confirmado (f(18) = 2080). | (4) rejeitado: Divergência: f(18) = 235836081600111350915268608/116415321826934814453125; gabarito 2025.82000000000. | (5) aprovado: Gabarito confirmado (f(24) = 2440). | (6) rejeitado: Divergência: f(24) = 72853486156297719654398512288759808/28421709430404007434844970703125; gabarito 2563.31000000000.
  - propriedade=rejeitado
  - propriedade=rejeitado
  - funcao/valor=aprovado
  - funcao/valor=rejeitado
  - funcao/valor=aprovado
  - funcao/valor=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 4 de 6 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 60*n + 1000 vale 1060 em n=1, mas o 1º termo da PA é 1000. | (2) rejeitado: Propriedade não confirmada: a expressão 1000*(26/25)**n vale 1040 em n=1, mas o 1º termo da PG é 1000. | (3) aprovado: Gabarito confirmado (f(18) = 2080). | (4) rejeitado: Divergência: f(18) = 235836081600111350915268608/116415321826934814453125; gabarito 2025.82000000000. | (5) aprovado: Gabarito confirmado (f(24) = 2440). | (6) rejeitado: Divergência: f(24) = 72853486156297719654398512288759808/28421709430404007434844970703125; gabarito 2563.31000000000. Resultado calculado independentemente: a expressão 60*n + 1000 vale 1060 em n=1, mas o 1º termo da PA é 1000 | a expressão 1000*(26/25)**n vale 1040 em n=1, mas o 1º termo da PG é 1000 | f(18) = 2080 | f(18) = 235836081600111350915268608/116415321826934814453125 | f(24) = 2440 | f(24) = 72853486156297719654398512288759808/28421709430404007434844970703125. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
