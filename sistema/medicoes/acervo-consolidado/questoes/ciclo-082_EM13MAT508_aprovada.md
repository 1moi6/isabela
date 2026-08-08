# Ciclo 082 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo inicia, no instante t = 0 (medido em horas), uma cultura com 500 bactérias em condições ideais de crescimento. Ele verifica que, a cada 4 horas, a quantidade de bactérias triplica. Por questões práticas, o técnico responsável só registra a contagem exatamente nos instantes t = 0, 4, 8, 12, 16, ... horas, obtendo assim uma sequência numérica de valores registrados, que pode ser indexada por n = 0, 1, 2, 3, ...

a) Escreva o termo geral $a_n$ da progressão geométrica formada pelos valores registrados pelo técnico (em função de n).

b) Sabendo que, na realidade, a população de bactérias cresce continuamente (não apenas nos instantes de registro), escreva uma função exponencial $f(t)$, com $t \geq 0$ representando o tempo em horas desde o início do experimento, tal que os valores registrados pelo técnico sejam exatamente os valores de $f$ nos instantes t = 4n, ou seja, $a_n = f(4n)$ para todo n natural.

c) Usando a função $f$, determine em que instante t (em horas, com uma casa decimal) a população da cultura atinge 20000 bactérias. Esse instante corresponde a um dos momentos em que o técnico faz um registro (múltiplo de 4 horas)? Justifique.

## Gabarito

a) $a_n = 500\cdot 3^n$; b) $f(t) = 500\cdot 3^{t/4}$, com $f(4n)=a_n$; c) $t = 4\log_3 40 \approx 13{,}4$ horas, que não é múltiplo de 4, logo não coincide com nenhum registro do técnico.

## Resolução

**a) Termo geral da PG**

Os valores registrados formam uma progressão geométrica de primeiro termo $a_0 = 500$ e razão $q = 3$ (pois a quantidade triplica a cada registro). Logo:
$$a_n = 500 \cdot 3^n, \quad n = 0,1,2,3,\dots$$

Conferindo: $a_0=500$, $a_1=1500$, $a_2=4500$, $a_3=13500$, $a_4=40500$.

**b) Função exponencial associada**

A PG descreve apenas os instantes discretos $t=0,4,8,12,\dots$, ou seja, $t = 4n \Rightarrow n = t/4$. Para obter uma função contínua $f(t)$ que "estenda" a PG a qualquer instante real, basta substituir $n$ por $t/4$ na fórmula do termo geral:
$$f(t) = 500 \cdot 3^{t/4}, \quad t \geq 0$$

Verificação da associação PG–função exponencial: para $t = 4n$,
$$f(4n) = 500\cdot 3^{4n/4} = 500\cdot 3^n = a_n.$$
Ou seja, a sequência $(a_n)$ é exatamente a restrição de $f$ ao domínio discreto $\{0,4,8,12,\dots\}$, enquanto $f$ está definida para todo $t$ real não negativo (domínio contínuo). Isso confirma que a PG é o "retrato" de uma função exponencial amostrada em intervalos regulares.

Conferência pontual: $f(8) = 500\cdot 3^{8/4} = 500\cdot 3^2 = 4500 = a_2$. ✓

**c) Instante em que a população atinge 20000 bactérias**

Resolvendo $f(t) = 20000$:
$$500\cdot 3^{t/4} = 20000 \;\Rightarrow\; 3^{t/4} = 40$$
Aplicando logaritmo (base 3, ou natural):
$$\frac{t}{4} = \log_3 40 = \frac{\ln 40}{\ln 3} \approx \frac{3{,}689}{1{,}099} \approx 3{,}358$$
$$t \approx 4 \times 3{,}358 \approx 13{,}4 \text{ horas}$$

Como $t \approx 13{,}4$ não é múltiplo de 4, esse instante **não coincide** com nenhum registro do técnico. De fato, $t=13{,}4$ está entre os registros $t=12$ (onde $a_3 = 13500$) e $t=16$ (onde $a_4 = 40500$), confirmando que 20000 bactérias é um valor atingido *entre* duas contagens discretas — algo que só a função exponencial contínua $f(t)$ permite calcular, pois a PG só fornece informação nos instantes $t=4n$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `500*3**n`, parâmetros `{'sequencia': 'pg', 'a1': '500', 'razao': '3'}`
- `funcao` — expressão `500*3**(t/4)`, esperado `4500`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`
- `funcao` — expressão `500*3**(t/4)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `equacao` — expressão `Eq(500*3**(t/4), 20000)`, esperado `[4*log(40, 3)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 500*3**n: coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(8) = 4500). | (3) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (500 bactérias, triplicação em 4h, instantes de registro definidos), condições explícitas e três itens com pedidos claros e não ambíguos. A notação n=0,1,2,... e t=4n é definida sem ambiguidade.
  - adequacao_nivel: 4/5 — O nível 'aplicar' é respeitado nos itens a) e c) (aplicação direta de fórmulas de PG e resolução de equação exponencial com logaritmo). O item b) exige uma pequena etapa de tradução/generalização (substituir n por t/4), que se aproxima de 'entender relações' mas ainda é compatível com aplicar em SOLO relacional. Conteúdo (PG, função exponencial, logaritmo) é adequado ao Ensino Médio. Poderia haver leve tensão entre a complexidade de log_3(40) em c) e o nível declarado, mas resolução guiada mantém a exigência dentro do aplicar.
  - alinhamento_bncc: 5/5 — A questão articula explicitamente PG e função exponencial em um único problema: pede o termo geral da PG (a), exige a construção da função contínua que a estende e a verificação da igualdade f(4n)=a_n (b), e explora a diferença entre domínio discreto e contínuo ao perguntar se o instante de 20000 bactérias coincide com um registro (c). Isso atende integralmente à habilidade EM13MAT508, pois não basta aplicar fórmula: a questão força a reflexão sobre a natureza discreta da PG versus a natureza contínua da função.
  - distratores: 5/5 — Questão discursiva, não há alternativas; portanto critério não se aplica e a nota é definida por padrão.
  - originalidade: 4/5 — O contexto de crescimento bacteriano é comum em livros didáticos, mas a articulação entre registro discreto e função contínua, além da pergunta final sobre coincidência com o instante de registro, é uma abordagem menos mecânica e evita o efeito Topaze ao exigir justificativa argumentativa, não apenas cálculo. Poderia ganhar em originalidade com um contexto menos batido (não bactérias) ou com uma pergunta que explore mais a comparação entre os dois modelos.
