# Ciclo 042 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 2

## Enunciado

Um biólogo estuda o crescimento de uma colônia de bactérias em laboratório. Ele constata que, em um modelo matemático simplificado, a quantidade de indivíduos na colônia, em milhares, pode ser descrita pela função $f(x) = 2^{x}$, em que $x$ representa o número de horas decorridas desde um instante de referência (podendo $x$ assumir valores negativos, representando horas anteriores a esse instante, dentro do intervalo em que o modelo é válido).

Para resolver o problema inverso — estimar quantas horas se passaram até que a colônia atingisse uma determinada quantidade $y$ de milhares de indivíduos — o biólogo utiliza a função $g(x) = \log_{2}(x)$.

Com base nessas duas funções, resolva:

**a)** Determine o domínio e a imagem de $f$ e de $g$. Compare os dois pares de conjuntos e explique, em termos matemáticos, por que essa relação entre eles não é uma coincidência.

**b)** Analise o crescimento de $f$ e de $g$ (cada uma é crescente ou decrescente?). Embora ambas cresçam no mesmo sentido, explique, sem usar tabelas numéricas, por que o crescimento de $f$ é qualitativamente muito mais rápido que o de $g$ à medida que $x$ aumenta.

**c)** Calcule as composições $f(g(x))$ e $g(f(x))$, indicando para quais valores de $x$ cada composição está definida. O que esses resultados revelam sobre a relação entre as funções $f$ e $g$?

**d)** Sabendo que $f(1) = 2$ e $f(3) = 8$, calcule $g(2)$ e $g(8)$. Em seguida, esboce em um mesmo plano cartesiano os gráficos de $f$, de $g$ e da reta $y = x$, situando nele os pontos $(1,2)$, $(2,1)$, $(3,8)$ e $(8,3)$. Explique, a partir desse esboço, que relação geométrica existe entre o gráfico de $f$ e o gráfico de $g$, e como as respostas dos itens (a), (b) e (c) justificam essa relação.

## Gabarito

a) $D_f=\mathbb{R}$, $Im_f=(0,+\infty)$; $D_g=(0,+\infty)$, $Im_g=\mathbb{R}$ — domínio e imagem se invertem entre f e g. b) f e g são ambas crescentes, mas f cresce de forma multiplicativa (cada vez mais rápido) e g cresce de forma cada vez mais lenta. c) $f(g(x))=x$ para $x>0$ e $g(f(x))=x$ para todo x real, mostrando que g é a função inversa de f. d) $g(2)=1$, $g(8)=3$; os gráficos de f e g são simétricos em relação à reta $y=x$.

## Resolução

**a) Domínio e imagem**

Para $f(x) = 2^{x}$: como toda potência de base positiva está definida para qualquer expoente real, o domínio de $f$ é $D_f = \mathbb{R}$. Como $2^x > 0$ para todo $x$, e $f$ assume todos os valores positivos, a imagem é $Im_f = (0, +\infty)$.

Para $g(x) = \log_2(x)$: o logaritmo só está definido para argumentos positivos, logo $D_g = (0, +\infty)$. Como o logaritmo assume qualquer valor real quando o argumento varia em $(0,+\infty)$, temos $Im_g = \mathbb{R}$.

Comparando: $D_f = Im_g = \mathbb{R}$ e $Im_f = D_g = (0,+\infty)$. Essa troca exata entre domínio e imagem não é coincidência: ela é a marca registrada de duas funções que são **inversas uma da outra** — o domínio de uma função sempre coincide com a imagem de sua inversa, e vice-versa.

**b) Crescimento**

Como a base $2 > 1$, $f(x) = 2^x$ é **crescente** em todo o seu domínio, e $g(x) = \log_2(x)$ também é **crescente** em todo o seu domínio (base do logaritmo maior que 1).

Apesar de ambas serem crescentes, o crescimento é qualitativamente diferente: em $f$, cada aumento de uma unidade em $x$ **multiplica** o valor da função por 2 (crescimento multiplicativo/exponencial), fazendo $f$ crescer cada vez mais depressa. Em $g$, para que o valor da função aumente uma unidade é preciso que o argumento $x$ seja **multiplicado** por 2 (pois $\log_2(2x) = \log_2(x)+1$); ou seja, é preciso um acréscimo cada vez maior em $x$ para obter o mesmo ganho em $g$. Por isso $g$ cresce cada vez mais devagar, enquanto $f$ cresce cada vez mais rápido.

**c) Composições**

$f(g(x)) = 2^{\log_2(x)} = x$, definida para $x \in (0,+\infty)$ (domínio de $g$).

$g(f(x)) = \log_2(2^{x}) = x$, definida para todo $x \in \mathbb{R}$ (domínio de $f$).

Como aplicar $g$ depois de $f$ (e $f$ depois de $g$) devolve sempre o valor original de $x$, isso mostra que $f$ e $g$ **desfazem uma a ação da outra**: são funções inversas, $g = f^{-1}$ (e $f = g^{-1}$).

**d) Pontos e gráfico**

Como $f(1)=2$, temos $g(2) = 1$ (pois $g$ desfaz o que $f$ fez). Como $f(3)=8$, temos $g(8) = 3$.

Observe que o ponto $(1,2)$ de $f$ corresponde ao ponto $(2,1)$ de $g$ — as coordenadas trocaram de posição. O mesmo ocorre com $(3,8)$ e $(8,3)$. Trocar as coordenadas $(a,b) \to (b,a)$ é exatamente a operação de **refletir um ponto em torno da reta $y=x$**.

No esboço, a curva $y = 2^x$ parte de valores próximos de $0$ (para $x$ muito negativo), passa por $(0,1)$, $(1,2)$ e $(3,8)$, subindo cada vez mais rápido. A curva $y=\log_2(x)$ passa por $(1,0)$, $(2,1)$ e $(8,3)$, subindo cada vez mais devagar, com uma assíntota vertical em $x=0$. As duas curvas são simétricas uma da outra em relação à reta $y=x$, que corta o plano na diagonal.

Essa simetria gráfica é a representação geométrica exata do que foi mostrado algebricamente: como $D_f = Im_g$, $Im_f = D_g$ (item a) e $f(g(x))=g(f(x))=x$ (item c), $f$ e $g$ são funções inversas, e por isso seus gráficos são reflexos um do outro através da reta $y=x$. O item (b) explica por que, apesar dessa simetria, uma curva ($f$) dispara para cima muito mais rapidamente que a outra ($g$) se afasta lentamente do eixo — reflexo do fato de que uma é exponencial e a outra, logarítmica.

## Formalização verificável

- `funcao` — expressão `2**x`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2**x`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `2**x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(x, 2)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(x, 2)`, esperado `S.Reals`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `log(x, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `2**x`, esperado `2`, parâmetros `{'consulta': 'valor', 'ponto': '1'}`
- `funcao` — expressão `log(x, 2)`, esperado `1`, parâmetros `{'consulta': 'valor', 'ponto': '2'}`
- `funcao` — expressão `2**x`, esperado `8`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `log(x, 2)`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 8 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de 2**x - 1: Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (imagem de 2**x - 1: Interval.open(-1, oo)). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x + 1)/log(2): Interval.open(-1, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x + 1)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(-1, oo)). | (7) aprovado: Gabarito confirmado (f(3) = 3). | (8) aprovado: Gabarito confirmado (f(3) = 3).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem segmentado em a), b), c), com dados completos (leis das funções, base explícita) e pedidos inequívocos. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — Os itens a) e b) são majoritariamente de compreensão/aplicação (determinar domínio/imagem, classificar crescimento), mas o item c) exige articular composição de funções, relação domínio-imagem e interpretação geométrica (simetria em y=x), configurando análise relacional (SOLO relacional/estendido abstrato). O conjunto atinge o nível 'analisar', embora as partes iniciais isoladamente fiquem em nível inferior.
  - alinhamento_bncc: 4/5 — A questão trata exponencial e logarítmica conjuntamente e as compara em domínio, imagem e crescimento, além de estabelecer a relação de inversão entre ambas — atendendo ao núcleo da habilidade. Falta, porém, exploração mais explícita da 'representação em plano cartesiano' (não há gráfico fornecido nem pedido de esboço), ficando a comparação gráfica reduzida a uma afirmação verbal sobre simetria.
  - distratores: 5/5 — não se aplica
  - originalidade: 2/5 — O par f(x)=2^x-1 e g(x)=log2(x+1) como inversas é um exemplo canônico de livro didático, sem contexto significativo. Além disso, o enunciado do item c) já afirma que se deve 'mostrar que g é a função inversa de f', entregando a conclusão a ser provada (efeito Topaze), o que esvazia o desafio analítico de descobrir essa relação por conta própria.
  - *sugestões:* 1) Reduzir o efeito Topaze no item c): em vez de dizer 'mostre que g é a inversa de f', peça algo como 'investigue a relação entre f e g calculando as composições f(g(x)) e g(f(x)); o que essas composições revelam sobre a relação entre as duas funções?' — deixando o aluno concluir a inversão. 2) Incluir um pedido explícito de representação gráfica (esboçar ou analisar um gráfico fornecido com as duas curvas e a reta y=x) para atender de forma mais direta à exigência de 'representações em plano cartesiano' da habilidade EM13MAT403. 3) Inserir um contexto ou situação aplicada (por exemplo, crescimento populacional e seu processo inverso de estimativa de tempo) para tornar o problema menos repetitivo em relação a exercícios clássicos de livros didáticos, mantendo a articulação entre domínio, imagem, crescimento e simetria gráfica das duas funções.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reduzir o efeito Topaze no item c): em vez de dizer 'mostre que g é a inversa de f', peça algo como 'investigue a relação entre f e g calculando as composições f(g(x)) e g(f(x)); o que essas composições revelam sobre a relação entre as duas funções?' — deixando o aluno concluir a inversão. 2) Incluir um pedido explícito de representação gráfica (esboçar ou analisar um gráfico fornecido com as duas curvas e a reta y=x) para atender de forma mais direta à exigência de 'representações em plano cartesiano' da habilidade EM13MAT403. 3) Inserir um contexto ou situação aplicada (por exemplo, crescimento populacional e seu processo inverso de estimativa de tempo) para tornar o problema menos repetitivo em relação a exercícios clássicos de livros didáticos, mantendo a articulação entre domínio, imagem, crescimento e simetria gráfica das duas funções.

### Iteração 2

- **Verificador:** aprovado_parcial — 9 de 10 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)). | (7) aprovado: Gabarito confirmado (f(1) = 2). | (8) aprovado: Gabarito confirmado (f(2) = 1). | (9) aprovado: Gabarito confirmado (f(3) = 8). | (10) aprovado: Gabarito confirmado (f(8) = 3).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é longo, porém organizado em itens claramente delimitados, cada um explicitando o que é dado e o que se pede. Não há ambiguidade lexical ou estrutural; os dados (definições de f, g, valores de f(1) e f(3)) são suficientes para resolver todos os subitens.
  - adequacao_nivel: 5/5 — O processo cognitivo exigido vai além de aplicar fórmulas: o aluno precisa comparar domínio/imagem, justificar por que a troca não é coincidência, contrastar taxas de crescimento sem tabelas, interpretar composições e sintetizar tudo numa explicação geométrica única. Isso corresponde a 'analisar' (e até tangencia 'avaliar'/'criar' na síntese do item d), com estrutura de resposta relacional/extended abstract na taxonomia SOLO — compatível com Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as exigências: trata exponencial e logarítmica em conjunto (não isoladamente), compara explicitamente domínio, imagem e crescimento (itens a e b), e ainda articula essas comparações com a representação gráfica no plano cartesiano e a relação de inversão (itens c e d), exigindo que o aluno costure os resultados anteriores numa única explicação. Não se limita a calcular valores; a comparação é o núcleo da tarefa.
  - distratores: 5/5 — Não se aplica: a questão é discursiva, sem alternativas de múltipla escolha.
  - originalidade: 4/5 — O contexto do biólogo e da colônia de bactérias evita o enunciado puramente abstrato de livro didático, mas funciona mais como moldura do que como elemento realmente explorado na resolução (não há uso quantitativo do contexto biológico nas respostas). A sequência de perguntas, embora bem construída, segue um roteiro previsível (domínio/imagem, crescimento, composição, gráfico) sem inovar na forma de instigar a descoberta, mas não há pistas que entreguem a resposta (sem efeito Topaze evidente).
