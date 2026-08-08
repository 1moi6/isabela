# Ciclo 060 — EM13MAT304

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

Um laboratório de microbiologia monitora uma cultura de bactérias cuja população, em função do tempo $t$ (em horas), é dada por uma função exponencial. Sabe-se que a cultura começa com 500 bactérias e que essa quantidade **dobra a cada 3 horas**.

a) Escreva a lei da função $P(t)$ que descreve a população dessa cultura em função de $t$ e calcule quantas bactérias haverá após 9 horas.

b) Determine, em horas, quanto tempo é necessário para que a população atinja 32.000 bactérias.

c) O laboratório deseja iniciar uma **segunda cultura**, também com 500 bactérias no instante inicial, mas que precisa atingir 4.000 bactérias em apenas 6 horas (mais rapidamente do que a primeira cultura atingiu essa mesma quantidade). Proponha uma lei exponencial $Q(t) = 500 \cdot 2^{t/k}$ para essa segunda cultura, determinando o valor de $k$ (o tempo, em horas, necessário para a população dobrar) que faz a condição pedida ser satisfeita. Em seguida, compare o valor de $k$ encontrado com o tempo de duplicação da primeira cultura e explique, em termos do crescimento das duas populações, o que essa diferença significa.

## Gabarito

a) $P(t)=500\cdot 2^{t/3}$; $P(9)=4000$ bactérias. b) $t=18$ horas. c) $Q(t)=500\cdot 2^{t/2}$, com tempo de duplicação $k=2$ horas, menor que as 3 horas da primeira cultura, indicando crescimento mais rápido.

## Resolução

**a) Lei da função e valor em $t=9$**

Como a população inicial é $P_0 = 500$ e ela dobra a cada 3 horas, o modelo exponencial é
$$P(t) = 500 \cdot 2^{t/3}$$

Para $t=9$:
$$P(9) = 500 \cdot 2^{9/3} = 500 \cdot 2^{3} = 500 \cdot 8 = 4000$$

Logo, após 9 horas há **4000 bactérias**.

**b) Tempo para atingir 32.000 bactérias**

Queremos $t$ tal que:
$$500 \cdot 2^{t/3} = 32000$$
$$2^{t/3} = \frac{32000}{500} = 64 = 2^6$$
$$\frac{t}{3} = 6 \implies t = 18$$

Logo, são necessárias **18 horas**.

**c) Construção do modelo da segunda cultura**

Queremos $Q(t) = 500 \cdot 2^{t/k}$ tal que $Q(6) = 4000$:
$$500 \cdot 2^{6/k} = 4000$$
$$2^{6/k} = 8 = 2^3$$
$$\frac{6}{k} = 3 \implies k = 2$$

Portanto, a lei proposta é:
$$Q(t) = 500 \cdot 2^{t/2}$$

**Comparação e interpretação:** na primeira cultura, a duplicação ocorre a cada 3 horas, e ela levou 9 horas para atingir 4000 bactérias (calculado no item a). Na segunda cultura, para que a mesma quantidade (4000) seja atingida em apenas 6 horas, o tempo de duplicação precisa ser menor: $k=2$ horas, ou seja, a população dobra mais rapidamente. Isso significa que a segunda cultura tem uma **taxa de crescimento exponencial maior** que a primeira — quanto menor o tempo de duplicação, mais rápido o crescimento da população ao longo do tempo, mesmo partindo do mesmo valor inicial.

## Formalização verificável

- `funcao` — expressão `500*2**(t/3)`, esperado `4000`, parâmetros `{'consulta': 'valor', 'ponto': '9'}`
- `equacao` — expressão `Eq(500*2**(t/3), 32000)`, esperado `[18]`
- `equacao` — expressão `Eq(500*2**(6/k), 4000)`, esperado `[2]`
- `propriedade` — expressão `-`, esperado `500*2**(t/2)`, parâmetros `{'pontos': '[(0,500),(6,4000)]'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 500*(7/5)**t vale 700 em t=1, mas o 1º termo da PG é 500. | (2) aprovado: Gabarito confirmado (f(3) = 1372). | (3) aprovado: Gabarito confirmado (f(4) = 9604/5). | (4) aprovado: Gabarito confirmado (f(5) = 67228/25). | (5) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - propriedade=rejeitado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 500*(7/5)**t vale 700 em t=1, mas o 1º termo da PG é 500. | (2) aprovado: Gabarito confirmado (f(3) = 1372). | (3) aprovado: Gabarito confirmado (f(4) = 9604/5). | (4) aprovado: Gabarito confirmado (f(5) = 67228/25). | (5) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). Resultado calculado independentemente: a expressão 500*(7/5)**t vale 700 em t=1, mas o 1º termo da PG é 500 | f(3) = 1372 | f(4) = 9604/5 | f(5) = 67228/25 | crescente em Interval(-oo, oo). Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 500*(7/5)**t: coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(3) = 1372). | (3) aprovado: Gabarito confirmado (f(4) = 9604/5). | (4) aprovado: Gabarito confirmado (f(5) = 67228/25). | (5) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é bem estruturado, com dados completos e itens claramente delimitados. O único ponto de atenção é o item c), cuja resposta esperada é 'parcialmente correta' (correta matematicamente, mas sem sentido físico para t negativo) — isso pode gerar dúvida no aluno sobre o que responder como 'certo/errado', mas não chega a ser ambiguidade grave.
  - adequacao_nivel: 2/5 — A especificação declara nível Bloom 'criar', mas a questão exige apenas identificar termo geral (compreender/aplicar), calcular valores (aplicar) e avaliar uma afirmação dada (analisar/avaliar). Não há em nenhum momento produção de algo novo pelo aluno — nem elaboração de um problema, nem construção de um modelo original, nem síntese de elementos distintos em uma estrutura nova. A estrutura de resposta é, no máximo, relacional (SOLO), compatível com 'analisar', não com 'criar'. Há incoerência entre o nível declarado e o processo cognitivo realmente demandado, agravada pela dificuldade declarada como 'fácil', que raramente é compatível com o nível mais alto da taxonomia.
  - alinhamento_bncc: 4/5 — A questão atende bem às exigências específicas listadas: vai além do cálculo puro (itens a e b) ao exigir, no item c, compreensão e interpretação da variação da grandeza (crescimento exponencial, domínio de validade do modelo, diferença entre comportamento matemático e físico). O contexto de crescimento populacional de bactérias é adequado e realista, alinhado a 'seres vivos microscópicos'. A articulação entre progressão geométrica e função exponencial também é bem integrada em um único problema, não justaposta. A única ressalva é a incompatibilidade com o nível Bloom declarado, tratada no critério anterior.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de crescimento bacteriano com taxa percentual é um clássico recorrente em livros didáticos e não traz elemento diferenciador forte. O item c), ao introduzir a afirmação de um colega para ser avaliada, é um recurso didático positivo que foge do formato mecânico, mas não é suficiente para tornar a questão marcadamente original. Não há efeito Topaze evidente, pois o item c não entrega a resposta, mas apenas reorganiza um enunciado bastante padronizado.
  - *sugestões:* Ajustar a coerência entre o nível Bloom declarado e a exigência real da questão. Duas alternativas possíveis: (1) Rebaixar o nível Bloom declarado na especificação para 'analisar' ou 'avaliar', já que o item c) pede justamente que o aluno avalie a validade de uma afirmação e distinga o comportamento matemático do significado físico do modelo — isso é coerente com o que a questão de fato demanda. (2) Se o objetivo é realmente atingir o nível 'criar', reformular o item c) (ou acrescentar um item d) para que o aluno produza algo novo, por exemplo: peça que ele proponha e justifique um modelo exponencial alternativo (com outra taxa ou outro fenômeno, como decaimento radioativo ou depreciação financeira) que respeite alguma condição dada (ex.: mesma população inicial, mas que atinja um valor-alvo em determinado tempo), obrigando-o a formular a expressão da função e validar suas escolhas — isso caracterizaria genuinamente 'criar'. Também recomenda-se tornar o item c) mais direto quanto ao que se espera como resposta (ex.: pedir explicitamente 'identifique o que está correto e o que está incorreto na afirmação do colega, distinguindo o comportamento da função matemática do sentido físico do problema') para reduzir a ambiguidade sobre o formato da resposta esperada.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a coerência entre o nível Bloom declarado e a exigência real da questão. Duas alternativas possíveis: (1) Rebaixar o nível Bloom declarado na especificação para 'analisar' ou 'avaliar', já que o item c) pede justamente que o aluno avalie a validade de uma afirmação e distinga o comportamento matemático do significado físico do modelo — isso é coerente com o que a questão de fato demanda. (2) Se o objetivo é realmente atingir o nível 'criar', reformular o item c) (ou acrescentar um item d) para que o aluno produza algo novo, por exemplo: peça que ele proponha e justifique um modelo exponencial alternativo (com outra taxa ou outro fenômeno, como decaimento radioativo ou depreciação financeira) que respeite alguma condição dada (ex.: mesma população inicial, mas que atinja um valor-alvo em determinado tempo), obrigando-o a formular a expressão da função e validar suas escolhas — isso caracterizaria genuinamente 'criar'. Também recomenda-se tornar o item c) mais direto quanto ao que se espera como resposta (ex.: pedir explicitamente 'identifique o que está correto e o que está incorreto na afirmação do colega, distinguindo o comportamento da função matemática do sentido físico do problema') para reduzir a ambiguidade sobre o formato da resposta esperada.

### Iteração 3

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (f(9) = 4000). | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [(18*log(2)**2 - 24*I*pi*log(2))/(log(8)**2 + 16*pi**2), (18*log(2)**2 + 24*I*pi*log(2))/(log(8)**2 + 16*pi**2), log(2)/(log(sqrt(2)) - I*pi/3), log(2)/(log(sqrt(2)) + I*pi/3), log(2)/(log(sqrt(2)) + I*pi)]. | (4) aprovado: Propriedades confirmadas para 500*2**(t/2): reproduz os 2 pontos dados.
  - funcao/valor=aprovado
  - equacao=aprovado
  - equacao=rejeitado
  - propriedade=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (f(9) = 4000). | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [(18*log(2)**2 - 24*I*pi*log(2))/(log(8)**2 + 16*pi**2), (18*log(2)**2 + 24*I*pi*log(2))/(log(8)**2 + 16*pi**2), log(2)/(log(sqrt(2)) - I*pi/3), log(2)/(log(sqrt(2)) + I*pi/3), log(2)/(log(sqrt(2)) + I*pi)]. | (4) aprovado: Propriedades confirmadas para 500*2**(t/2): reproduz os 2 pontos dados. Resultado calculado independentemente: f(9) = 4000 | [18] | [2, (18*log(2)**2 - 24*I*pi*log(2))/(log(8)**2 + 16*pi**2), (18*log(2)**2 + 24*I*pi*log(2))/(log(8)**2 + 16*pi**2), log(2)/(log(sqrt(2)) - I*pi/3), log(2)/(log(sqrt(2)) + I*pi/3), log(2)/(log(sqrt(2)) + I*pi)] | 500*2**(t/2). Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
