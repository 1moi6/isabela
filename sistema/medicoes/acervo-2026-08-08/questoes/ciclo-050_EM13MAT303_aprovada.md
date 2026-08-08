# Ciclo 050 — EM13MAT303

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um capital C é investido a juros compostos, com taxa fixa de 10% ao mês incidindo sobre o montante acumulado no mês anterior. Sabendo que $\log 2 \approx 0{,}301$ e $\log 1{,}1 \approx 0{,}0414$, determine o menor número inteiro de meses $n$ necessário para que o montante acumulado seja pelo menos o dobro do capital inicial.

## Alternativas

- (a) 8 meses  ← correta
- (b) 7 meses
  - *erro representado:* Arredondar o valor 7,27 para baixo (para o inteiro mais próximo por truncamento), em vez de tomar o menor inteiro que efetivamente satisfaz a desigualdade (n=7 ainda não atinge o dobro do capital).
- (c) 10 meses
  - *erro representado:* Aplicar o raciocínio de juros simples, resolvendo C(1+ni)=2C, obtendo n = 1/i = 1/0,10 = 10, em vez de reconhecer o regime de juros compostos (crescimento exponencial).
- (d) 4 meses
  - *erro representado:* Confundir a taxa i com log(1+i) na equação, calculando erroneamente n = log2 / i = 0,301/0,10 ≈ 3,01, arredondando para 4.

## Gabarito

n = 8 meses

## Resolução

**Passo 1 — Modelar o montante:**

Como os juros são compostos com taxa mensal de $10\% = 0{,}10$, o montante após $n$ meses é
$$M(n) = C\,(1+0{,}10)^n = C\,(1{,}1)^n.$$

Essa expressão é uma **função exponencial** em $n$ (a variável está no expoente), o que caracteriza o crescimento composto.

**Passo 2 — Traduzir a condição do problema:**

Queremos o menor $n$ inteiro tal que $M(n) \geq 2C$, ou seja,
$$C\,(1{,}1)^n \geq 2C \quad\Longrightarrow\quad (1{,}1)^n \geq 2.$$

**Passo 3 — Resolver com logaritmos:**

Aplicando log (base 10) em ambos os lados, e usando que $\log$ é crescente:
$$n\cdot \log(1{,}1) \geq \log 2.$$

**Passo 4 — Isolar n:**

$$n \geq \dfrac{\log 2}{\log 1{,}1} \approx \dfrac{0{,}301}{0{,}0414} \approx 7{,}27.$$

**Passo 5 — Determinar o menor inteiro:**

Como $n$ deve ser inteiro e satisfazer $n \geq 7{,}27$, o menor valor possível é $n = 8$.

**Verificação:**
$$(1{,}1)^7 \approx 1{,}949 < 2 \qquad (1{,}1)^8 \approx 2{,}144 \geq 2.$$

Confirma-se que $n=8$ é o menor número de meses em que o montante atinge ao menos o dobro do capital inicial — evidenciando o crescimento exponencial típico dos juros compostos, no qual o tempo necessário para duplicar o capital cresce em progressão logarítmica, e não linear com a taxa.

## Formalização verificável

- `equacao` — expressão `Eq(n, ceiling(log(2)/log(Rational(11,10))))`, esperado `[8]`
- `funcao` — expressão `(Rational(11,10))**n`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado sem ambiguidades: taxa, período, condição de parada (dobro do capital) e dados logarítmicos necessários estão todos explícitos. O pedido ('menor número inteiro de meses') é preciso e sem múltiplas interpretações possíveis.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar a fórmula de juros compostos, montar uma inequação exponencial e resolvê-la com logaritmos — processo consistente com o nível 'aplicar' de Bloom e com estrutura relacional na SOLO (o aluno integra modelo exponencial + propriedade de log + arredondamento contextual). Não é mera memorização, mas também não exige análise ou julgamento crítico além do aplicado.
  - alinhamento_bncc: 5/5 — Atende plenamente à EM13MAT303: trata de juros compostos, usa porcentagem como taxa, e o crescimento exponencial é evidenciado tanto na modelagem (M(n)=C(1,1)^n) quanto na resolução, que comenta explicitamente a distinção entre crescimento exponencial e linear. Não é uma conta de porcentagem isolada.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: truncamento incorreto do valor não-inteiro, confusão com juros simples, e erro conceitual ao substituir a taxa pelo logaritmo da taxa. Nenhum é trivialmente descartável sem compreensão do conteúdo.
  - originalidade: 3/5 — O problema de 'tempo para dobrar capital a juros compostos usando log' é um clássico recorrente em livros didáticos e listas de vestibular. Embora tecnicamente correto e bem construído, falta um contexto ou variação que o diferencie do enunciado-padrão amplamente replicado, e não há elemento de significância real (ex.: comparação de investimentos, tomada de decisão) que enriqueça o contexto.
