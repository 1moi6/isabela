# Avaliação de questões — avaliador 3

## Como responder

São 22 questões de Matemática do Ensino Médio. Leia cada uma como leria uma
questão que você pensasse em usar com a sua turma, e responda às quatro
perguntas que vêm logo abaixo dela.

Onde se pergunta pelo **nível de dificuldade**, responda pensando nos seus
alunos, não num aluno ideal. É essa resposta que permite calibrar o sistema: ele
classifica cada questão como fácil, média ou difícil por conta própria, e
precisamos saber o quanto isso corresponde à sala de aula real.

**A amostra tem qualidade variável, e pode conter questões com erro matemático.**
Se encontrar algum, aponte onde.

Não há resposta certa sobre você: o que está sendo avaliado é o sistema que
produziu estas questões, não quem as lê. Um "recusada" bem justificado vale mais
para este trabalho do que um "aceita" por gentileza.

Você pode responder direto neste documento ou na planilha `respostas-avaliador-3.csv`, que já
vem com os códigos dos itens nas linhas. O que for mais cômodo.

Tempo estimado: cerca de 75 minutos.

---

### Q067

Uma colônia de bactérias cresce segundo a lei $N(t) = 100 \cdot 3^{t/4}$, em que $N(t)$ é o número de bactérias e $t$ é o tempo em horas, contado a partir do instante em que a colônia tinha 100 indivíduos. Um estudante quer saber quanto tempo leva para a população **triplicar** de tamanho, e resolve investigar isso em dois momentos diferentes: partindo de $t=0$ e partindo de $t=4$ horas (quando a população já triplicou uma vez). Ele calcula: (i) o tempo $\Delta t_1$ necessário para que $N(t)$ passe de $N(0)$ para $3\cdot N(0)$; (ii) o tempo $\Delta t_2$ necessário para que $N(t)$ passe de $N(4)$ para $3\cdot N(4)$. Assinale a alternativa que descreve corretamente a relação entre $\Delta t_1$ e $\Delta t_2$, e o motivo dessa relação.

(a) $\Delta t_1 = \Delta t_2 = 4$ horas, pois na função exponencial a razão entre valores separados por um mesmo intervalo de tempo é sempre a mesma, independentemente do instante inicial ou do tamanho já atingido pela população.
(b) $\Delta t_2 > \Delta t_1$, pois, como a população em $t=4$ já é maior, seria necessário um tempo maior para ela triplicar novamente.
(c) $\Delta t_2 < \Delta t_1$, pois quanto maior a população, mais rápido ela cresce, então o tempo para triplicar diminui a cada rodada.
(d) Não é possível comparar $\Delta t_1$ e $\Delta t_2$ sem conhecer o valor de $N(0)$, já que o tempo de triplicação depende do tamanho inicial da colônia.

**Gabarito proposto:** Δt1 = Δt2 = 4 horas — o tempo de triplicação é constante e independente do instante inicial, pois a variação relativa de uma função exponencial depende apenas do intervalo de tempo decorrido, não do valor absoluto da grandeza.

**Habilidade declarada:** EM13MAT304 — Resolver e elaborar problemas com funções exponenciais nos quais é necessário compreender e interpretar a variação das grandezas envolvidas, em contextos como o da Matemática Financeira e o do crescimento de seres vivos microscópicos, entre outros.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q069

Considere a sequência $(a_n)$, definida para $n = 0, 1, 2, 3, \ldots$, com primeiro termo $a_0 = 5$ e razão $q = 3$ (uma progressão geométrica). Um pesquisador registra o número de bactérias em uma cultura a cada hora exata, de modo que $a_n$ é a contagem observada na hora $n$. Ele percebe que esses valores coincidem com os da função exponencial $f(t) = 5 \cdot 3^t$ para $t = n$, ou seja, $f(n) = a_n$ para todo $n$ natural.

Ricardo, colega do pesquisador, argumenta: "Como $f(t)=5\cdot 3^t$ está definida para qualquer número real $t$, o valor $f(2{,}5) = 5\cdot 3^{2{,}5}$ é a contagem real de bactérias no instante intermediário entre a segunda e a terceira hora."

Avalie a afirmação de Ricardo e assinale a alternativa correta.

(a) Ricardo está errado: a progressão geométrica $(a_n)$ está definida apenas para os índices naturais $n=0,1,2,3,\ldots$, que correspondem às horas exatas em que a contagem foi feita. A função $f(t)=5\cdot3^t$ é uma extensão contínua que apenas interpola os termos da PG nos pontos inteiros; o valor $f(2{,}5)$ existe matematicamente, mas não corresponde a nenhum termo da sequência, pois o fenômeno só foi definido (e medido) nos instantes discretos.
(b) Ricardo está certo, pois a PG e a função exponencial são exatamente a mesma coisa: como $f$ está definida para todo $t$ real, qualquer valor calculado por $f$ é automaticamente um termo válido da progressão.
(c) Ricardo está errado, mas pelo motivo errado: ele deveria ter estimado o valor em $t=2{,}5$ fazendo a média aritmética simples entre $a_2=45$ e $a_3=135$ (interpolação linear), e não usando a fórmula exponencial $5\cdot3^{2,5}$.
(d) Ricardo está certo, porque, em princípio, o número de bactérias poderia ser medido continuamente ao longo do tempo; logo $f(2{,}5)$ representa a contagem real esperada nesse instante, ainda que o pesquisador só tenha registrado valores a cada hora.

**Gabarito proposto:** A

**Habilidade declarada:** EM13MAT508 — Identificar e associar sequências numéricas (PG) a funções exponenciais de domínios discretos para análise de propriedades, incluindo dedução de algumas fórmulas e resolução de problemas.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q015

Uma colônia de bactérias em um experimento de laboratório tem seu número de indivíduos, a partir do início da observação, dado por $N(t) = 100 \cdot 2^{t}$, em que $t$ é o tempo em horas ($t \geq 0$) e $N(t)$ é o número de bactérias. Um pesquisador quer saber, ao contrário, quanto tempo é necessário para que a colônia atinja um determinado número $N$ de bactérias, e por isso utiliza a função inversa de $N(t)$, que ele chama de $t(N)$.

a) Determine o domínio e a imagem de $N(t)$, considerando o contexto do experimento.

b) Encontre a expressão de $t(N)$ (a função inversa de $N(t)$) e determine seu domínio e sua imagem.

c) Compare o crescimento das duas funções: as duas são crescentes, mas uma cresce 'cada vez mais rápido' e a outra cresce 'cada vez mais devagar' à medida que a variável aumenta. Identifique qual é qual e justifique observando como varia o incremento de cada função.

d) Explique por que o domínio de $N(t)$ coincide com a imagem de $t(N)$, e a imagem de $N(t)$ coincide com o domínio de $t(N)$, relacionando esse fato com a posição dos gráficos das duas funções no plano cartesiano.

**Gabarito proposto:** a) $D_N=[0,+\infty)$, $Im_N=[100,+\infty)$. b) $t(N)=\log_2(N/100)$, com $D_t=[100,+\infty)$, $Im_t=[0,+\infty)$. c) $N(t)$ cresce cada vez mais rápido (convexa); $t(N)$ cresce cada vez mais devagar (côncava). d) Por serem funções inversas, seus gráficos são simétricos em relação à reta $y=x$, o que troca domínio e imagem entre as duas funções.

**Habilidade declarada:** EM13MAT403 — Comparar e analisar as representações, em plano cartesiano, das funções exponencial e logarítmica para identificar as características fundamentais (domínio, imagem, crescimento) de cada uma, com ou sem apoio de tecnologias digitais, estabelecendo relações entre elas.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q081

Um professor de Física e um analista financeiro registraram duas situações reais.

**Situação 1 — Queda livre**
Um objeto é solto (sem velocidade inicial) do alto de um prédio. A distância percorrida $d$ (em metros) foi medida em função do tempo $t$ (em segundos):

| $t$ (s) | 1 | 2 | 3 |
|---|---|---|---|
| $d$ (m) | 5 | 20 | 45 |

**Situação 2 — Lucro de uma loja**
Uma loja varia o preço unitário $p$ (em reais) de um produto e registra o lucro mensal $L$ (em milhares de reais):

| $p$ (R\$) | 10 | 20 | 30 |
|---|---|---|---|
| $L$ (mil R\$) | 800 | 1200 | 800 |

Sabendo que, em ambos os casos, a grandeza da segunda linha é uma função polinomial do 2º grau da grandeza da primeira linha, resolva:

a) Determine a lei algébrica $d(t)$ e a lei algébrica $L(p)$ que descrevem cada situação.

b) Para cada função, identifique no plano cartesiano: as coordenadas do vértice da parábola, o sentido da concavidade e os pontos em que o gráfico intercepta os eixos coordenados.

c) Apenas uma das duas situações representa uma grandeza **diretamente proporcional ao quadrado** da outra. Diga qual é e justifique sua resposta usando dois argumentos: um algébrico (a forma da lei obtida em (a)) e um geométrico (a posição do gráfico em relação à origem do plano cartesiano).

**Gabarito proposto:** $d(t)=5t^2$, vértice $(0,0)$, concavidade para cima, parábola passando pela origem — diretamente proporcional a $t^2$. $L(p)=-4p^2+160p-400$, vértice $(20,1200)$, concavidade para baixo, intercepta o eixo $L$ em $(0,-400)$ e o eixo $p$ em $p=20\pm10\sqrt3$ — quadrática geral, não é proporcional ao quadrado de $p$. A situação diretamente proporcional ao quadrado é a Situação 1 (queda livre).

**Habilidade declarada:** EM13MAT402 — Converter representações algébricas de funções polinomiais de 2º grau para representações geométricas no plano cartesiano, distinguindo os casos nos quais uma variável for diretamente proporcional ao quadrado da outra, recorrendo ou não a softwares ou aplicativos de álgebra e geometria dinâmica.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q046

Um biólogo monitora o crescimento de uma colônia de bactérias em um meio de cultura controlado. No início da observação ($t=0$), a colônia possui 500 bactérias. Verificou-se experimentalmente que essa população duplica a cada 3 horas, mantendo esse padrão de crescimento durante todo o experimento, que dura pelo menos 24 horas.

a) Elabore a lei da função exponencial $N(t)$ que fornece o número de bactérias em função do tempo $t$, em horas, decorrido desde o início da observação.

b) Utilizando a função obtida, determine o número de bactérias presentes após 9 horas de observação.

c) Um estudante afirmou que, como a população duplica a cada 3 horas, o crescimento percentual da colônia a cada hora deve ser de $\dfrac{100\%}{3}\approx 33{,}3\%$. Mostre que essa afirmação está incorreta, determinando a taxa de crescimento percentual horária real da colônia (isto é, encontre $i$ tal que $N(t) = 500\cdot(1+i)^t$ para todo $t$), e explique por que o raciocínio do estudante falha, considerando o comportamento multiplicativo da função exponencial.

d) Determine depois de quantas horas a população da colônia atingirá 32000 bactérias.

**Gabarito proposto:** a) $N(t) = 500\cdot 2^{t/3}$; b) 4000 bactérias; c) $i = 2^{1/3}-1 \approx 26\%$ ao hora — o raciocínio do estudante é inválido pois o crescimento exponencial é multiplicativo, não pode ser dividido linearmente pelo tempo; d) 18 horas.

**Habilidade declarada:** EM13MAT304 — Resolver e elaborar problemas com funções exponenciais nos quais é necessário compreender e interpretar a variação das grandezas envolvidas, em contextos como o da Matemática Financeira e o do crescimento de seres vivos microscópicos, entre outros.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q044

As marés de um pequeno porto pesqueiro variam de forma periódica ao longo do dia, devido à atração gravitacional da Lua e do Sol. Um estudo local registrou que, tomando $t = 0$ como meia-noite (0h), a maré atinge seu nível máximo de $2{,}0$ m exatamente à meia-noite, cai até um nível mínimo de $1{,}0$ m às 6h da manhã, retorna ao máximo às 12h (meio-dia) e repete esse padrão a cada 12 horas ao longo de todo o dia.

a) Identifique a amplitude, o período e o deslocamento vertical (translação do eixo médio) desse fenômeno periódico.

b) Escreva uma função $h(t)$, em metros, que descreva a altura da maré em função do tempo $t$ (em horas), $t \in [0,24)$, usando a função cosseno. Compare essa função com o gráfico da função cosseno "pura" $y=\cos(t)$, indicando quais transformações (translação vertical e compressão/dilatação horizontal) foram necessárias para obter o modelo da maré.

c) Determine a altura da maré às 3h da manhã e explique, com base no gráfico da função obtida em (b), por que esse valor corresponde exatamente à média entre o nível máximo e o mínimo.

**Gabarito proposto:** a) Amplitude = 0,5 m; período = 12 h; deslocamento vertical = 1,5 m. b) $h(t) = 1{,}5 + 0{,}5\cos\left(\frac{\pi}{6}t\right)$, obtida comprimindo horizontalmente (fator $\pi/6$), reduzindo a amplitude (fator 0,5) e deslocando verticalmente (+1,5) o gráfico de $y=\cos(t)$. c) $h(3) = 1{,}5$ m, que é a média entre o máximo e o mínimo.

**Habilidade declarada:** EM13MAT306 — Resolver e elaborar problemas em contextos que envolvem fenômenos periódicos reais, como ondas sonoras, ciclos menstruais, movimentos cíclicos, entre outros, e comparar suas representações com as funções seno e cosseno, no plano cartesiano, com ou sem apoio de aplicativos de álgebra e geometria.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q029

Considere a função $f(x) = 3\cos(2x) - 1$, definida para $x \in \mathbb{R}$.

No ciclo trigonométrico (circunferência de raio 1 centrada na origem), o valor de $\cos(\theta)$ corresponde à abscissa do ponto $P$ que se desloca sobre a circunferência conforme o ângulo $\theta$ varia.

Usando essa relação entre o ciclo trigonométrico e a representação de $f$ no plano cartesiano, determine, justificando cada resposta com base no comportamento do ponto $P$ sobre a circunferência:

a) o domínio de $f$;

b) o período de $f$;

c) a imagem de $f$.

**Gabarito proposto:** Domínio: $\mathbb{R}$; Período: $\pi$; Imagem: $[-4, 2]$

**Habilidade declarada:** EM13MAT404 — Identificar as características fundamentais das funções seno e cosseno (periodicidade, domínio, imagem), por meio da comparação das representações em ciclos trigonométricos e em planos cartesianos, com ou sem apoio de tecnologias digitais.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q033

Observe a tabela abaixo, que relaciona valores de $x$ e $y$:

| $x$ | $-3$ | $-1$ | $2$ | $4$ |
|---|---|---|---|---|
| $y$ | $27$ | $3$ | $12$ | $48$ |

Analisando os pares de valores, investigue como $y$ varia em função de $x$ e determine a expressão algébrica que generaliza essa relação para qualquer valor de $x$. Em seguida, classifique o tipo de função polinomial obtida, justificando sua resposta.

**Gabarito proposto:** y = 3x², uma função quadrática do tipo y = ax² (com a = 3)

**Habilidade declarada:** EM13MAT502 — Investigar relações entre números expressos em tabelas para representá-los no plano cartesiano, identificando padrões e criando conjecturas para generalizar e expressar algebricamente essa generalização, reconhecendo quando essa representação é de função polinomial de 2º grau do tipo y = ax².

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q065

Um oceanógrafo registra a altura da maré (em metros) em um pequeno porto ao longo de um dia. Ele observa que a maré varia de forma periódica e simétrica em torno de um nível médio, atingindo seu valor máximo de 1,8 m exatamente à meia-noite ($t=0$, com $t$ em horas) e seu valor mínimo de 0,2 m exatamente às 6h da manhã. Esse padrão se repete a cada 12 horas.

a) Modele a altura da maré, em metros, por uma função do tipo $h(t) = A\cos(Bt) + D$, com $t$ em horas contado a partir da meia-noite. Determine explicitamente os valores de $A$, $B$ e $D$, justificando cada um a partir dos dados do fenômeno (amplitude, período e deslocamento vertical do gráfico em relação ao eixo $t$).

b) Determine todos os horários dentro das primeiras 12 horas do dia (isto é, para $0 \le t < 12$) em que a maré atinge exatamente 1,4 m de altura. Para cada horário encontrado, indique se a maré está subindo ou descendo naquele instante, justificando sua resposta apenas a partir do comportamento gráfico da função cosseno (sem usar derivadas).

**Gabarito proposto:** h(t) = 0,8·cos(πt/6) + 1,0 (A=0,8 m; B=π/6 rad/h; D=1,0 m). A maré atinge 1,4 m às 2h (descendo) e às 10h (subindo).

**Habilidade declarada:** EM13MAT306 — Resolver e elaborar problemas em contextos que envolvem fenômenos periódicos reais, como ondas sonoras, ciclos menstruais, movimentos cíclicos, entre outros, e comparar suas representações com as funções seno e cosseno, no plano cartesiano, com ou sem apoio de aplicativos de álgebra e geometria.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q082

Um biólogo inicia, no instante t = 0 (medido em horas), uma cultura com 500 bactérias em condições ideais de crescimento. Ele verifica que, a cada 4 horas, a quantidade de bactérias triplica. Por questões práticas, o técnico responsável só registra a contagem exatamente nos instantes t = 0, 4, 8, 12, 16, ... horas, obtendo assim uma sequência numérica de valores registrados, que pode ser indexada por n = 0, 1, 2, 3, ...

a) Escreva o termo geral $a_n$ da progressão geométrica formada pelos valores registrados pelo técnico (em função de n).

b) Sabendo que, na realidade, a população de bactérias cresce continuamente (não apenas nos instantes de registro), escreva uma função exponencial $f(t)$, com $t \geq 0$ representando o tempo em horas desde o início do experimento, tal que os valores registrados pelo técnico sejam exatamente os valores de $f$ nos instantes t = 4n, ou seja, $a_n = f(4n)$ para todo n natural.

c) Usando a função $f$, determine em que instante t (em horas, com uma casa decimal) a população da cultura atinge 20000 bactérias. Esse instante corresponde a um dos momentos em que o técnico faz um registro (múltiplo de 4 horas)? Justifique.

**Gabarito proposto:** a) $a_n = 500\cdot 3^n$; b) $f(t) = 500\cdot 3^{t/4}$, com $f(4n)=a_n$; c) $t = 4\log_3 40 \approx 13{,}4$ horas, que não é múltiplo de 4, logo não coincide com nenhum registro do técnico.

**Habilidade declarada:** EM13MAT508 — Identificar e associar sequências numéricas (PG) a funções exponenciais de domínios discretos para análise de propriedades, incluindo dedução de algumas fórmulas e resolução de problemas.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q024

A tabela abaixo relaciona valores de $x$ e os correspondentes valores de $y$, obtidos a partir de uma mesma regra de formação (os valores de $x$ não variam em intervalos iguais):

| $x$ | $-3$ | $1$ | $4$ | $8$ |
|---|---|---|---|---|
| $y$ | $14$ | $2$ | $-7$ | $-19$ |

Um estudante, analisando os pares ordenados $(x,y)$ da tabela, conjectura que essa relação pode ser representada por uma função polinomial do 1º grau. Assinale a alternativa que apresenta a lei de formação $f(x)$ que generaliza corretamente o padrão observado na tabela.

(a) $f(x) = -3x + 5$
(b) $f(x) = -12x + 14$
(c) $f(x) = 3x - 1$
(d) $f(x) = -11x + 13$

**Gabarito proposto:** f(x) = -3x + 5

**Habilidade declarada:** EM13MAT501 — Investigar relações entre números expressos em tabelas para representá-los no plano cartesiano, identificando padrões e criando conjecturas para generalizar e expressar algebricamente essa generalização, reconhecendo quando essa representação é de função polinomial de 1º grau.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q087

Considere a progressão aritmética $(a_n)$ com primeiro termo $a_1 = 7$ e razão $r = 4$: $(7, 11, 15, 19, 23, \dots)$. Essa PA pode ser vista como a restrição da função afim $f(x) = 4x + 3$ ao conjunto dos números naturais não nulos, de modo que $a_n = f(n)$ para todo $n \geq 1$ (o gráfico da PA é o conjunto de pontos discretos $(n, a_n)$ sobre a reta que representa $f$).

Qual é o menor termo dessa PA que é maior do que 100?

(a) 103
(b) 99
(c) 107
(d) 100

**Gabarito proposto:** 103

**Habilidade declarada:** EM13MAT507 — Identificar e associar sequências numéricas (PA) a funções afins de domínios discretos para análise de propriedades, incluindo dedução de algumas fórmulas e resolução de problemas.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q028

Duas empresas de transporte por aplicativo, TáxiJá e MoveCar, calculam o valor da corrida em função da distância percorrida, em quilômetros.

- A TáxiJá cobra R$ 2,50 por quilômetro rodado, sem qualquer taxa adicional.
- A MoveCar cobra uma taxa fixa de R$ 4,00 pela chamada do carro, mais R$ 1,50 por quilômetro rodado.

Considere $x$ a distância percorrida, em quilômetros ($x \geq 0$), e $y$ o valor pago, em reais.

a) Escreva a lei de formação que representa o valor cobrado por cada empresa, em função de $x$.

b) Represente, num mesmo plano cartesiano, os gráficos das duas funções, indicando claramente o ponto em que cada reta corta o eixo $y$.

c) Uma dessas funções representa uma grandeza diretamente proporcional à distância percorrida, e a outra não. Identifique qual delas é a proporcional e explique, a partir do gráfico (ou da lei algébrica), como reconhecer esse comportamento.

d) Determine algebricamente a distância a partir da qual a corrida pela MoveCar passa a ser mais barata que pela TáxiJá, e indique as coordenadas do ponto em que os dois gráficos se cruzam.

**Gabarito proposto:** a) $f_T(x)=2{,}5x$ e $f_M(x)=1{,}5x+4$. b) Retas crescentes: $f_T$ passa pela origem $(0,0)$; $f_M$ corta o eixo $y$ em $(0,4)$. c) $f_T$ é diretamente proporcional (passa pela origem, $b=0$); $f_M$ não é proporcional ($b=4\neq 0$). d) A partir de $x=4$ km a MoveCar fica mais barata; o ponto de intersecção das retas é $(4,10)$.

**Habilidade declarada:** EM13MAT401 — Converter representações algébricas de funções polinomiais de 1º grau para representações geométricas no plano cartesiano, distinguindo os casos nos quais o comportamento é proporcional, recorrendo ou não a softwares ou aplicativos de álgebra e geometria dinâmica.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q063

Uma rede de lanchonetes possui duas filiais, A e B, que vendem o mesmo produto por preços que podem ser ajustados mensalmente. Os gestores modelaram o lucro mensal de cada filial (em milhares de reais) em função do preço de venda unitário $p$ (em reais) pelas funções:

$L_A(p) = -2p^2 + 80p - 600$

$L_B(p) = -3p^2 + 132p - 1200$

A diretoria da rede definiu uma meta: para que a linha de produto continue sendo vendida em uma filial, o lucro mensal máximo dessa filial deve ser de pelo menos 240 mil reais.

a) Determine o preço de venda que maximiza o lucro de cada filial e o valor do lucro máximo correspondente.

b) Qual filial alcança o maior lucro máximo?

c) Com base na meta estabelecida pela diretoria, verifique se cada filial deve continuar vendendo o produto. Justifique sua resposta com os valores calculados.

**Gabarito proposto:** Filial A: preço de R$ 20, lucro máximo de 200 mil reais (não atinge a meta). Filial B: preço de R$ 22, lucro máximo de 252 mil reais (atinge a meta). A Filial B tem o maior lucro máximo e é a única que deve continuar vendendo o produto.

**Habilidade declarada:** EM13MAT503 — Investigar pontos de máximo ou de mínimo de funções quadráticas em contextos da Matemática Financeira ou da Cinemática, entre outros.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q010

Uma companhia de saneamento cobra a tarifa de água residencial, em reais, em função do consumo mensal $x$ (em $m^3$), segundo a lei:

$$f(x) = \begin{cases} 15, & 0 \le x \le 5 \\ 15 + 4(x-5), & x > 5 \end{cases}$$

em que $x$ representa o volume consumido no mês (um número real não negativo, podendo assumir qualquer valor, inclusive não inteiro).

Assinale a alternativa que descreve corretamente o gráfico de $f$, seu domínio de validade, sua imagem e seu comportamento de crescimento/decrescimento.

(a) O gráfico é um segmento horizontal em $y=15$ para $0\le x\le 5$, seguido de uma semirreta crescente de coeficiente angular $4$ partindo do ponto $(5,15)$, sem salto; domínio $[0,+\infty)$, imagem $[15,+\infty)$, crescente para $x>5$.
(b) O gráfico é um segmento horizontal em $y=15$ para $0\le x\le 5$, seguido de uma reta decrescente de coeficiente angular $-4$ a partir de $(5,15)$, com domínio $[0,+\infty)$ e imagem $(-\infty,15]$.
(c) O gráfico é um segmento horizontal em $y=15$ até $x=5$, seguido de um salto até $y=35$ e depois uma reta crescente de coeficiente angular $4$, pois para $x>5$ deve-se usar diretamente $f(x)=15+4x$.
(d) O gráfico é apenas o segmento horizontal em $y=15$, pois a função só está definida para $0\le x\le 5$; fora desse intervalo, $f$ não possui domínio de validade.

**Gabarito proposto:** O gráfico é um segmento horizontal em $y=15$ para $0\le x\le 5$, seguido de uma semirreta crescente de coeficiente angular $4$ partindo de $(5,15)$, sem descontinuidade; domínio $[0,+\infty)$, imagem $[15,+\infty)$, e a função é crescente para $x>5$.

**Habilidade declarada:** EM13MAT405 — Reconhecer funções definidas por uma ou mais sentenças (como a tabela do Imposto de Renda, contas de luz, água, gás etc.), em suas representações algébrica e gráfica, convertendo essas representações de uma para outra e identificando domínios de validade, imagem, crescimento e decrescimento.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q038

Uma roda-gigante tem 15 m de raio e seu centro está fixado a 17 m do solo. Ela gira com velocidade angular constante, completando uma volta inteira a cada 40 segundos. Uma passageira embarca no ponto mais baixo da roda (o ponto da circunferência mais próximo do chão) no instante $t=0$, e a roda gira continuamente a partir daí. Associando o movimento circular da cabine ao ciclo trigonométrico — em que o ângulo percorrido a partir do ponto mais baixo corresponde a $\theta(t)=\dfrac{2\pi}{40}t$ — a altura $h(t)$, em metros, da cabine em relação ao solo, $t$ segundos após o embarque, é dada por
$$h(t) = 17 - 15\cos\left(\frac{2\pi}{40}t\right).$$
Considerando a correspondência entre o percurso da cabine no ciclo trigonométrico e o gráfico de $h(t)$ no plano cartesiano, identifique a alternativa que apresenta corretamente o período do movimento, o domínio de $h$ (levando em conta que $t$ representa o tempo decorrido desde o embarque, com a roda girando indefinidamente) e a imagem de $h$ (a faixa de alturas atingidas pela cabine).

(a) Período de 40 s; domínio $t \in [0, +\infty)$; imagem $[2, 32]$ metros.
(b) Período de 40 s; domínio $t \in [0, +\infty)$; imagem $[-15, 15]$ metros.
(c) Período de $\dfrac{\pi}{20}$ s; domínio $t \in [0, +\infty)$; imagem $[2, 32]$ metros.
(d) Período de 40 s; domínio $t \in [0, 40]$; imagem $[2, 32]$ metros.

**Gabarito proposto:** A

**Habilidade declarada:** EM13MAT404 — Identificar as características fundamentais das funções seno e cosseno (periodicidade, domínio, imagem), por meio da comparação das representações em ciclos trigonométricos e em planos cartesianos, com ou sem apoio de tecnologias digitais.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q011

Uma função afim $f(x) = ax + b$, com $a, b \in \mathbb{R}$ e $a \neq 0$, satisfaz simultaneamente as condições $f(2) = 7$ e $f(f(1)) = 13$. Determine a soma de todos os valores possíveis de $f(0)$.

(a) 4
(b) 3
(c) 1
(d) 6

**Gabarito proposto:** 4

**Habilidade declarada:** EM13MAT302 — Resolver e elaborar problemas cujos modelos são as funções polinomiais de 1º e 2º graus, em contextos diversos, incluindo ou não tecnologias digitais.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q062

A magnitude $M$ de um abalo sísmico, medida na escala Richter, está relacionada à amplitude $A$ das ondas sísmicas registradas por um sismógrafo pela função $M = \log_{10}\left(\dfrac{A}{A_0}\right)$, em que $A_0$ é uma amplitude de referência constante (a mesma para todos os registros de um mesmo aparelho).

Uma cidade foi atingida por um terremoto de magnitude 4,0. Semanas depois, um segundo terremoto, de magnitude 6,0, atingiu a mesma região e foi registrado pelo mesmo sismógrafo.

a) Determine quantas vezes a amplitude das ondas sísmicas do terremoto de magnitude 6,0 foi maior do que a amplitude das ondas do terremoto de magnitude 4,0.

b) Um morador da cidade afirmou: "Como a diferença de magnitude foi de apenas 2 pontos, numa escala que costuma ir até 10, o segundo terremoto deve ter sido só um pouco mais forte, talvez uns 20% mais forte que o primeiro." Usando o valor obtido no item (a), explique por que essa interpretação está incorreta, destacando a natureza logarítmica (não linear) da escala Richter.

**Gabarito proposto:** a) A amplitude do terremoto de magnitude 6,0 foi 100 vezes maior que a do terremoto de magnitude 4,0. b) A interpretação do morador está errada porque a escala Richter é logarítmica: cada unidade a mais em $M$ multiplica a amplitude por 10 (não soma uma fração fixa). Uma diferença de 2 pontos corresponde a uma amplitude 100 vezes maior, não 20% maior.

**Habilidade declarada:** EM13MAT305 — Resolver e elaborar problemas com funções logarítmicas nos quais é necessário compreender e interpretar a variação das grandezas envolvidas, em contextos como os de abalos sísmicos, pH, radioatividade, Matemática Financeira, entre outros.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q007

Uma oficina mecânica cobra por seus serviços de revisão um valor fixo de mão de obra, mais uma taxa que depende do número de horas de trabalho. Uma revisão que durou 2 horas custou R$ 150,00, e outra revisão, no mesmo padrão de cobrança, durou 5 horas e custou R$ 300,00. Sabendo que o custo total varia linearmente com o número de horas trabalhadas, qual seria o custo de uma revisão que durasse 8 horas?

(a) R$ 450,00
(b) R$ 400,00
(c) R$ 600,00
(d) R$ 480,00

**Gabarito proposto:** R$ 450,00

**Habilidade declarada:** EM13MAT302 — Resolver e elaborar problemas cujos modelos são as funções polinomiais de 1º e 2º graus, em contextos diversos, incluindo ou não tecnologias digitais.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q034

Duas empresas de aplicativo de transporte, A e B, calculam o valor da corrida em função da distância percorrida $x$ (em km). A empresa A cobra R$ 2,50 por quilômetro rodado, sem nenhuma taxa adicional. A empresa B cobra uma taxa fixa de embarque de R$ 3,00 mais R$ 2,00 por quilômetro rodado. Sejam $y_A(x)$ e $y_B(x)$, em reais, os custos totais das corridas das empresas A e B, respectivamente, em função de $x$. Se essas duas funções forem representadas por retas em um plano cartesiano (custo $y$ no eixo vertical e distância $x$ no eixo horizontal), assinale a alternativa que descreve corretamente essas retas.

(a) A reta que representa a empresa A passa pela origem (0,0) e tem coeficiente angular 2,5, sendo uma função proporcional; a reta da empresa B corta o eixo y no ponto (0,3) e tem coeficiente angular 2, não sendo proporcional.
(b) A reta que representa a empresa B passa pela origem (0,0), pois seu coeficiente angular é 2; a reta da empresa A corta o eixo y no ponto (0,3), pois seu coeficiente angular é 2,5.
(c) Ambas as retas passam pela origem (0,0), já que representam custo por quilômetro rodado; a reta de A tem coeficiente angular 2,5 e a de B tem coeficiente angular 2.
(d) A reta da empresa A corta o eixo y no ponto (0, 2,5); a reta da empresa B corta o eixo y no ponto (0,2) e tem coeficiente angular 3.

**Gabarito proposto:** A reta que representa a empresa A passa pela origem $(0,0)$ e tem coeficiente angular 2,5 (função proporcional); a reta da empresa B corta o eixo y no ponto $(0,3)$ e tem coeficiente angular 2 (função afim, não proporcional).

**Habilidade declarada:** EM13MAT401 — Converter representações algébricas de funções polinomiais de 1º grau para representações geométricas no plano cartesiano, distinguindo os casos nos quais o comportamento é proporcional, recorrendo ou não a softwares ou aplicativos de álgebra e geometria dinâmica.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q031

No plano cartesiano, as retas $r$ e $s$ representam, respectivamente, as funções polinomiais do 1º grau $f$ e $g$. A reta $r$ passa pela origem do sistema e pelo ponto $(3,6)$. A reta $s$ é paralela a $r$ e intercepta os eixos coordenados formando, com eles, um triângulo de área igual a 4 unidades de área, situado inteiramente no quarto quadrante (ou seja, com um vértice sobre o semieixo positivo das abscissas e outro sobre o semieixo negativo das ordenadas, além da origem).

a) Determine a lei de $f$ e classifique-a quanto à proporcionalidade, justificando pela posição geométrica da reta $r$.

b) Determine a lei de $g$. Nos seus cálculos aparecerão duas possibilidades para o coeficiente que desloca a reta; explique, usando a condição sobre o quadrante em que o triângulo deve estar, por que apenas uma delas é válida.

c) Classifique $g$ quanto à proporcionalidade e explique, em termos geométricos, por que a reta $s$ não passa pela origem.

**Gabarito proposto:** f(x) = 2x (proporcional); g(x) = 2x - 4 (afim não proporcional, pois b = -4 ≠ 0)

**Habilidade declarada:** EM13MAT401 — Converter representações algébricas de funções polinomiais de 1º grau para representações geométricas no plano cartesiano, distinguindo os casos nos quais o comportamento é proporcional, recorrendo ou não a softwares ou aplicativos de álgebra e geometria dinâmica.

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

### Q027

Observe a tabela abaixo, que relaciona valores de x com valores de y:

| x | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| y | 4 | 16 | 36 | 64 |

a) Investigue como y varia em função de x, testando se há proporcionalidade direta, proporcionalidade com o quadrado de x, ou outra relação.

b) Escreva a lei algébrica y = f(x) que generaliza o padrão observado na tabela, e classifique o tipo de função obtida.

**Gabarito proposto:** y = 4x²

**Habilidade declarada:** EM13MAT502 — Investigar relações entre números expressos em tabelas para representá-los no plano cartesiano, identificando padrões e criando conjecturas para generalizar e expressar algebricamente essa generalização, reconhecendo quando essa representação é de função polinomial de 2º grau do tipo y = ax².

**Tem erro matemático?**
( ) não   ( ) sim, aqui: ______________________________   ( ) não sei dizer

**Que nível de dificuldade esta questão tem para os seus alunos?**
( ) fácil   ( ) média   ( ) difícil   ( ) fora do alcance da turma

**Você usaria esta questão?**
( ) aceita   ( ) aceita com ajuste   ( ) recusada

**Por quê?** _(obrigatório quando não for "aceita")_

>

---

---

## Para terminar

**1. Você usaria um sistema assim no seu planejamento? Por quê?**

>

**2. O que faltou nas questões que você viu?**

>

**3. O que atrapalhou — na questão, no enunciado, no formato deste material?**

>

Obrigado. Se quiser saber quais itens tinham erro e qual era, é só pedir.
