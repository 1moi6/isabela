# Ciclo 067 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma colônia de bactérias cresce segundo a lei $N(t) = 100 \cdot 3^{t/4}$, em que $N(t)$ é o número de bactérias e $t$ é o tempo em horas, contado a partir do instante em que a colônia tinha 100 indivíduos. Um estudante quer saber quanto tempo leva para a população **triplicar** de tamanho, e resolve investigar isso em dois momentos diferentes: partindo de $t=0$ e partindo de $t=4$ horas (quando a população já triplicou uma vez). Ele calcula: (i) o tempo $\Delta t_1$ necessário para que $N(t)$ passe de $N(0)$ para $3\cdot N(0)$; (ii) o tempo $\Delta t_2$ necessário para que $N(t)$ passe de $N(4)$ para $3\cdot N(4)$. Assinale a alternativa que descreve corretamente a relação entre $\Delta t_1$ e $\Delta t_2$, e o motivo dessa relação.

## Alternativas

- (a) $\Delta t_1 = \Delta t_2 = 4$ horas, pois na função exponencial a razão entre valores separados por um mesmo intervalo de tempo é sempre a mesma, independentemente do instante inicial ou do tamanho já atingido pela população.  ← correta
- (b) $\Delta t_2 > \Delta t_1$, pois, como a população em $t=4$ já é maior, seria necessário um tempo maior para ela triplicar novamente.
  - *erro representado:* Confunde a magnitude absoluta da grandeza (número de bactérias) com o tempo necessário para uma variação relativa, supondo que 'populações maiores demoram mais para triplicar'.
- (c) $\Delta t_2 < \Delta t_1$, pois quanto maior a população, mais rápido ela cresce, então o tempo para triplicar diminui a cada rodada.
  - *erro representado:* Confunde crescimento exponencial (variação relativa constante) com crescimento acelerado em termos absolutos, achando que a taxa relativa de crescimento aumenta com o tamanho da população.
- (d) Não é possível comparar $\Delta t_1$ e $\Delta t_2$ sem conhecer o valor de $N(0)$, já que o tempo de triplicação depende do tamanho inicial da colônia.
  - *erro representado:* Acredita erroneamente que o tempo de triplicação de uma função exponencial depende do valor inicial $N_0$, quando na verdade depende apenas da base da exponencial (taxa de crescimento).

## Gabarito

Δt1 = Δt2 = 4 horas — o tempo de triplicação é constante e independente do instante inicial, pois a variação relativa de uma função exponencial depende apenas do intervalo de tempo decorrido, não do valor absoluto da grandeza.

## Resolução

**Passo 1 — Calcular $\Delta t_1$ (triplicação a partir de $t=0$):**

Queremos $t$ tal que $N(t) = 3\cdot N(0)$, ou seja:
$$100\cdot 3^{t/4} = 3\cdot 100$$
$$3^{t/4} = 3^1 \implies \frac{t}{4}=1 \implies t = 4$$
Logo $\Delta t_1 = 4$ horas.

**Passo 2 — Calcular $\Delta t_2$ (triplicação a partir de $t=4$):**

Primeiro, $N(4) = 100\cdot 3^{4/4} = 300$. Queremos $t'$ tal que $N(4+t') = 3\cdot N(4) = 900$:
$$100\cdot 3^{(4+t')/4} = 900$$
$$3^{(4+t')/4} = 9 = 3^2 \implies \frac{4+t'}{4} = 2 \implies 4+t' = 8 \implies t' = 4$$
Logo $\Delta t_2 = 4$ horas.

**Passo 3 — Interpretar o resultado:**

Como $N(t) = N(t_0)\cdot 3^{(t-t_0)/4}$ para qualquer instante inicial $t_0$, a razão $\dfrac{N(t_0+\Delta t)}{N(t_0)} = 3^{\Delta t/4}$ depende apenas de $\Delta t$ (a variação do tempo), e não do valor de $t_0$ nem do valor absoluto de $N(t_0)$. Por isso, o tempo necessário para a população **triplicar** é sempre o mesmo (4 horas), não importa em que instante o processo começa. Esse é um traço característico do crescimento exponencial: variações **relativas** (multiplicativas) de uma grandeza ocorrem em intervalos de tempo constantes, mesmo que as variações **absolutas** (em número de bactérias) sejam cada vez maiores.

Portanto, $\Delta t_1 = \Delta t_2 = 4$ horas, pois o tempo de triplicação depende só da razão de crescimento (base 3 na exponencial), não do instante inicial nem do tamanho já atingido pela população.

## Formalização verificável

- `equacao` — expressão `Eq(3**(t/4), 3)`, esperado `[4]`
- `equacao` — expressão `Eq(3**((4+tp)/4), 9)`, esperado `[4]`
- `funcao` — expressão `100*3**(t/4)`, esperado `300`, parâmetros `{'consulta': 'valor', 'ponto': '4'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (3) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem redigido, define claramente a função, a variável, o domínio (t≥0) e o que é pedido (Δt tal que N triplica). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver o problema.
  - adequacao_nivel: 2/5 — A tarefa efetivamente pedida ao aluno é resolver a equação 3^(Δt/2)=3, um procedimento algorítmico de aplicação de propriedades de potência — nível 'aplicar' na taxonomia de Bloom, com estrutura SOLO uniestrutural/multiestrutural (identificar a equação e executá-la). A resolução do professor traz uma reflexão relacional interessante (invariância do fator multiplicativo independente do instante inicial), mas essa reflexão NÃO é exigida do aluno no enunciado nem é testável pelo formato de múltipla escolha: o aluno pode acertar apenas isolando t sem nunca perceber ou justificar a invariância. Portanto o processo cognitivo real fica aquém do nível 'analisar' declarado.
  - alinhamento_bncc: 3/5 — O contexto (crescimento de bactérias) e o tema (função exponencial) são adequados à habilidade EM13MAT304. Porém a habilidade exige explicitamente 'compreender e interpretar a variação das grandezas', e a questão, tal como formulada, avalia apenas a capacidade de resolver uma equação exponencial pontual. A ideia central da variação exponencial (que o fator de multiplicação é constante e independe do ponto de partida) aparece somente na resolução do professor, não é solicitada nem verificável pela resposta do aluno na alternativa múltipla escolhida.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis (confundir o coeficiente do expoente, trocar a base pelo tempo, inverter a equação do expoente), sem opções absurdas ou trivialmente elimináveis. Poderiam ser ligeiramente mais diversificados (ex.: um erro relacionado à leitura do 500 como parte do cálculo), mas cumprem bem a função pedagógica.
  - originalidade: 4/5 — O contexto de crescimento bacteriano é comum em livros didáticos, mas a pergunta sobre 'tempo de triplicação' (em vez do clássico 'tempo de duplicação') foge um pouco do padrão. O enunciado em si não contém pistas que pavimentem a solução (o efeito Topaze aparece apenas na resolução, não no enunciado), o que é positivo.
  - *sugestões:* Para elevar o nível cognitivo a 'analisar' e atender de fato à habilidade EM13MAT304 (compreender e interpretar a variação), reformule a questão para exigir que o aluno compare ou justifique a invariância do intervalo, em vez de apenas calculá-lo uma única vez. Por exemplo: (1) apresente duas afirmações sobre o tempo de triplicação partindo de instantes diferentes (t=0 e t=4) e peça que o aluno julgue se são iguais e explique por quê, transformando as alternativas em juízos sobre a relação entre as grandezas, não apenas em valores numéricos; ou (2) peça para comparar o comportamento de N(t) exponencial com uma função linear de crescimento equivalente em t=0, perguntando em qual delas o 'tempo para triplicar' depende do instante inicial, forçando o aluno a analisar a estrutura da variação e não só resolver uma equação isolada. Mantenha os mesmos distratores adaptando-os ao novo formato de julgamento/comparação.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para elevar o nível cognitivo a 'analisar' e atender de fato à habilidade EM13MAT304 (compreender e interpretar a variação), reformule a questão para exigir que o aluno compare ou justifique a invariância do intervalo, em vez de apenas calculá-lo uma única vez. Por exemplo: (1) apresente duas afirmações sobre o tempo de triplicação partindo de instantes diferentes (t=0 e t=4) e peça que o aluno julgue se são iguais e explique por quê, transformando as alternativas em juízos sobre a relação entre as grandezas, não apenas em valores numéricos; ou (2) peça para comparar o comportamento de N(t) exponencial com uma função linear de crescimento equivalente em t=0, perguntando em qual delas o 'tempo para triplicar' depende do instante inicial, forçando o aluno a analisar a estrutura da variação e não só resolver uma equação isolada. Mantenha os mesmos distratores adaptando-os ao novo formato de julgamento/comparação.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Gabarito confirmado (f(4) = 300).
  - equacao=aprovado
  - equacao=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (lei de crescimento, instantes iniciais definidos) e pedido claro: comparar Δt1 e Δt2 e justificar a relação. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A questão exige mais que cálculo mecânico: pede comparação entre dois processos e identificação do princípio geral (invariância do tempo de duplicação/triplicação), o que é compatível com 'analisar' (decompor a situação em duas instâncias e relacionar causa-efeito). A estrutura de resposta é relacional (SOLO), pois a alternativa correta articula o resultado numérico com a justificativa estrutural (razão constante independe do ponto inicial). Poderia exigir ainda mais análise se pedisse generalização para outro fator de multiplicação, mas atende bem ao nível declarado.
  - alinhamento_bncc: 5/5 — Cumpre exatamente a habilidade: o aluno não apenas calcula os tempos, mas deve interpretar por que a variação relativa é constante independentemente do valor absoluto da grandeza — isso é o cerne de EM13MAT304. O contexto de crescimento bacteriano é realista e articula cálculo com interpretação em um único problema coeso, não em itens soltos.
  - distratores: 5/5 — Os três distratores representam erros conceituais plausíveis e frequentes: (a) confundir crescimento absoluto com relativo assumindo que 'mais bactérias demoram mais para triplicar'; (b) inverter essa lógica assumindo aceleração relativa; (c) acreditar que o tempo de triplicação depende do valor inicial N0. Nenhum é absurdo ou trivialmente eliminável sem compreensão do conceito.
  - originalidade: 4/5 — Embora o contexto de crescimento bacteriano seja comum em livros didáticos, a proposta de comparar dois momentos distintos (t=0 e t=4) para evidenciar a invariância da razão de crescimento é uma abordagem menos mecânica que o cálculo direto de tempo de duplicação, evitando parcialmente o efeito Topaze. Poderia ser mais original com um contexto financeiro ou de decaimento radioativo pouco explorado, mas cumpre bem o objetivo pedagógico sem entregar a resposta no enunciado.
