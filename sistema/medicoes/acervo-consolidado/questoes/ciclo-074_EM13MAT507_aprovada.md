# Ciclo 074 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma empresa de transporte urbano inaugurou uma nova linha de ônibus. No primeiro mês de operação (mês 1), a linha transportou 340 passageiros. Devido à divulgação e à adesão gradual dos moradores, o número de passageiros transportados em cada mês superou o do mês anterior em exatamente 45 passageiros, formando uma progressão aritmética que se manteve mês após mês.

A diretoria da empresa sabe que essa evolução mensal pode ser descrita por uma função afim $f$, definida apenas para os números naturais $n \geq 1$ (o mês de operação), de modo que $f(n)$ forneça o número de passageiros transportados no mês $n$, coincidindo com os termos da progressão aritmética.

Com base nessa função afim, determine a partir de qual mês o número de passageiros transportados ultrapassará, pela primeira vez, 10.000 passageiros mensais.

## Alternativas

- (a) Mês 216  ← correta
- (b) Mês 215
  - *erro representado:* Usar o termo geral com índice deslocado, $a_n = a_1 + n\cdot r = 340+45n$ (sem o $-1$), o que leva a resolver $45n+340>10000$ e obter $n>214{,}67$, arredondando para $n=215$.
- (c) Mês 217
  - *erro representado:* Resolver corretamente $n>215{,}67$ e arredondar para $216$, mas em seguida somar 1 mês a mais por engano, supondo que o mês 1 corresponde a $n=0$ na contagem final (erro de contagem/off-by-one na conversão para o domínio discreto).
- (d) Mês 16
  - *erro representado:* Confundir o número de passageiros transportados NO mês (o termo $a_n$) com o total acumulado de passageiros até aquele mês (a soma $S_n$ da PA), resolvendo $S_n>10000$ em vez de $a_n>10000$.

## Gabarito

Mês 216 (alternativa A)

## Resolução

**1. Identificando a progressão aritmética**

O número de passageiros no mês $n$ forma uma PA com primeiro termo $a_1 = 340$ e razão $r = 45$.

**2. Associando a PA à função afim**

O termo geral da PA é:
$$a_n = a_1 + (n-1)r = 340 + 45(n-1) = 45n + 295$$

Como a evolução mensal é descrita por uma função afim $f$ que coincide com a PA nos naturais, temos:
$$f(n) = 45n + 295, \quad n \in \mathbb{N}, \; n \geq 1$$

Note que $f$ é a restrição aos naturais da função afim $g(x) = 45x + 295$ definida em $\mathbb{R}$: a reta que passa pelos pontos $(1,340)$, $(2,385)$, $(3,430)$, etc. É essa correspondência entre a PA e a reta que permite tratar o problema algebricamente como uma inequação, mesmo sabendo que só fazem sentido valores naturais de $n$.

**3. Resolvendo a inequação (em $\mathbb{R}$, para localizar a região)**

Queremos o menor $n$ tal que $f(n) > 10000$:
$$45n + 295 > 10000$$
$$45n > 9705$$
$$n > \frac{9705}{45} = 215{,}67\ldots$$

**4. Voltando ao domínio discreto**

Como $n$ representa um número de mês, deve ser um número natural. O menor natural maior que $215{,}67$ é $n = 216$ (e não $215$, pois $215 < 215{,}67$).

**5. Verificação**

$$a_{215} = 45(215) + 295 = 9675 + 295 = 9970 < 10000$$
$$a_{216} = 45(216) + 295 = 9720 + 295 = 10015 > 10000$$

De fato, o mês 215 ainda não ultrapassa 10.000, e o mês 216 é o primeiro a ultrapassar.

**Resposta: mês 216.**

## Formalização verificável

- `propriedade` — expressão `45*n + 295`, esperado `45*n + 295`, parâmetros `{'pontos': '[(1,340),(2,385),(3,430)]', 'grau': '1', 'sequencia': 'pa', 'a1': '340', 'razao': '45'}`
- `progressao` — expressão `-`, esperado `9970`, parâmetros `{'tipo_progressao': 'pa', 'a1': '340', 'razao': '45', 'n': '215', 'consulta': 'termo'}`
- `progressao` — expressão `-`, esperado `10015`, parâmetros `{'tipo_progressao': 'pa', 'a1': '340', 'razao': '45', 'n': '216', 'consulta': 'termo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 45*n + 295: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (termo da PA = 9970). | (3) aprovado: Gabarito confirmado (termo da PA = 10015).
  - propriedade=aprovado
  - progressao/termo=aprovado
  - progressao/termo=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado define claramente os dados (a1=340, r=45) e a pergunta (primeiro mês em que f(n)>10000). A menção à 'função afim definida apenas para os números naturais' é conceitualmente correta, mas pode gerar leve estranhamento no aluno por não ser a forma usual de apresentar função afim; ainda assim não compromete a compreensão do problema.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar a fórmula do termo geral, montar e resolver uma inequação e, crucialmente, interpretar o resultado no domínio discreto (arredondar corretamente para o natural seguinte). Isso é compatível com 'aplicar' na taxonomia de Bloom, com estrutura de resposta multiestrutural a relacional (SOLO), pois exige conectar dois conceitos e cuidar da transição contínuo-discreto. Conteúdo adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente o que a especificação exige: articula a PA com a função afim (f(n)=45n+295), trata explicitamente o domínio discreto (distinguindo a resolução em R da resposta válida em N) e exige essa associação para resolver o problema, não apenas aplicar mecanicamente uma fórmula.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis: deslocamento de índice na PA (mês 215), erro de off-by-one na conversão para o discreto (mês 217) e confusão entre termo e soma da PA (mês 16). Nenhum é absurdo ou trivialmente eliminável, embora a justificativa do distrator 'mês 217' seja um pouco artificial/forçada em comparação aos outros.
  - originalidade: 4/5 — O contexto de transporte urbano é razoavelmente contextualizado e evita o clichê de 'salário' ou 'conta de água'. O enunciado não entrega pistas diretas sobre como montar a inequação nem sobre o cuidado com o arredondamento, evitando efeito Topaze de forma satisfatória, embora a estrutura ainda seja próxima de problemas clássicos de PA/função afim.
