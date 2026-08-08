# Ciclo 072 — EM13MAT303

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Marina aplicou R$ 8.000,00 em um investimento que rende juros compostos a uma taxa fixa de 1,5% ao mês sobre o saldo do mês anterior. Ela decidiu que só fará o resgate no primeiro mês em que o montante acumulado for igual ou superior ao dobro do capital investido. Usando as aproximações $\log 2 \approx 0,301$ e $\log 1,015 \approx 0,00647$, determine o número mínimo de meses completos necessários para que Marina possa efetuar esse resgate.

## Alternativas

- (a) 47 meses  ← correta
- (b) 46 meses
  - *erro representado:* Arredondar 46,52 para baixo em vez de para cima, ignorando que só no mês seguinte a condição de dobrar o capital é de fato satisfeita.
- (c) 67 meses
  - *erro representado:* Tratar o crescimento como juros simples, resolvendo 8000(1+0,015n)=16000 em vez de usar a potência (1,015)^n, perdendo o caráter exponencial do problema.
- (d) 48 meses
  - *erro representado:* Usar a 'regra dos 72' (72/taxa = 72/1,5 = 48) como atalho aproximado, em vez de calcular o valor exato com os logaritmos fornecidos no enunciado.

## Gabarito

47 meses

## Resolução

**Passo 1 — Modelar o montante.**

Como os juros são compostos, o montante após $n$ meses é
$$M(n) = 8000\cdot(1{,}015)^n.$$
Essa é uma função exponencial (razão constante $1{,}015>1$ entre meses consecutivos), ou seja, o crescimento é exponencial, não linear.

**Passo 2 — Montar a condição do problema.**

Marina resgata no primeiro mês em que $M(n)\ge 2\cdot 8000 = 16000$:
$$8000\cdot(1{,}015)^n \ge 16000 \;\;\Rightarrow\;\; (1{,}015)^n \ge 2.$$

**Passo 3 — Aplicar logaritmo.**

$$\log\big((1{,}015)^n\big) \ge \log 2 \;\;\Rightarrow\;\; n\cdot \log 1{,}015 \ge \log 2 \;\;\Rightarrow\;\; n \ge \dfrac{\log 2}{\log 1{,}015}.$$

**Passo 4 — Substituir os valores aproximados.**

$$n \ge \dfrac{0{,}301}{0{,}00647} \approx 46{,}52.$$

**Passo 5 — Determinar o menor número inteiro de meses.**

Como $n$ representa um número de meses completos, é preciso o menor inteiro que satisfaça $n\ge 46{,}52$, ou seja, $n = 47$.

Verificação:
- Para $n=46$: $46\times 0{,}00647 = 0{,}29762 < 0{,}301$, logo $(1{,}015)^{46}<2$ — ainda não dobrou.
- Para $n=47$: $47\times 0{,}00647 = 0{,}30409 > 0{,}301$, logo $(1{,}015)^{47}>2$ — já dobrou.

Portanto, o menor número de meses é **47**.

## Formalização verificável

- `funcao` — expressão `8000*(Rational(203,200))**n`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(n, ceiling(log(2)/log(Rational(203,200))))`, esperado `[47]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/crescimento=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado apresenta claramente capital, taxa, condição de resgate (dobrar o montante) e fornece os logaritmos necessários. Não há ambiguidade sobre o que é dado nem sobre o que se pede.
  - adequacao_nivel: 4/5 — O processo exigido (montar a inequação exponencial, aplicar logaritmo, interpretar o arredondamento correto para 'meses completos') é compatível com 'aplicar', embora exija também uma etapa de julgamento (arredondar para cima e verificar), aproximando-se de um nível relacional na SOLO. Ainda assim é coerente com Bloom 'aplicar' em nível difícil.
  - alinhamento_bncc: 5/5 — A questão trabalha juros compostos de forma que o crescimento exponencial é central e explícito: a resolução da inequação (1,015)^n ≥ 2 obriga o uso do modelo exponencial, não sendo uma conta de porcentagem isolada. Atende integralmente às exigências da habilidade.
  - distratores: 5/5 — Os quatro distratores correspondem a erros conceituais plausíveis e distintos: arredondamento incorreto, confusão com juros simples, uso da 'regra dos 72' como atalho impreciso. Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 3/5 — O contexto (tempo para dobrar capital em juros compostos, resolvido com logaritmos fornecidos) é um clássico recorrente em livros didáticos e vestibulares. Fornecer os valores de log já direciona fortemente o caminho de resolução, reduzindo a necessidade de o aluno decidir a estratégia (leve efeito Topaze), embora seja justificável dado o nível de ensino.
