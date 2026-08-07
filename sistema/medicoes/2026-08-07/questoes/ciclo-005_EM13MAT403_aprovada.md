# Ciclo 005 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 2

## Enunciado

Um biólogo estuda o crescimento de uma colônia de bactérias que dobra de tamanho a cada hora, descrito pela função $f(x) = 2^x$, em que $x$ representa o tempo em horas e $f(x)$ o número de bactérias. Ele também quer saber, em função da quantidade $x$ de bactérias, quanto tempo levou para a colônia atingir esse valor, o que é descrito pela função $g(x) = \log_2(x)$. Comparando as leis de $f$ e $g$, qual das alternativas descreve corretamente o domínio, a imagem e o crescimento dessas duas funções, bem como a relação entre seus gráficos no plano cartesiano?

## Alternativas

- (a) O domínio de $f$ é $\mathbb{R}$ e sua imagem é $\mathbb{R}_{+}^{*}$; o domínio de $g$ é $\mathbb{R}_{+}^{*}$ e sua imagem é $\mathbb{R}$. Ambas são crescentes, e o gráfico de $g$ é a reflexão do gráfico de $f$ em relação à reta $y=x$, pois $g$ é a inversa de $f$.  ← correta
- (b) O domínio de $f$ é $\mathbb{R}_{+}^{*}$ e sua imagem é $\mathbb{R}$; o domínio de $g$ é $\mathbb{R}$ e sua imagem é $\mathbb{R}_{+}^{*}$. Ambas são crescentes, e seus gráficos são simétricos em relação ao eixo $y$.
  - *erro representado:* Troca o domínio e a imagem entre as duas funções, invertendo qual delas exige argumento positivo, e erra a relação geométrica entre os gráficos.
- (c) O domínio de $f$ é $\mathbb{R}$ e sua imagem é $\mathbb{R}_{+}^{*}$; o domínio de $g$ é $\mathbb{R}_{+}^{*}$ e sua imagem é $\mathbb{R}$. A função $f$ é crescente, mas $g$ é decrescente, pois toda função logarítmica decresce.
  - *erro representado:* Generaliza incorretamente que funções logarítmicas são sempre decrescentes, ignorando que isso só ocorre quando a base está entre 0 e 1.
- (d) O domínio de $f$ é $\mathbb{R}$ e sua imagem é $\mathbb{R}_{+}^{*}$; o domínio de $g$ é $\mathbb{R}_{+}^{*}$ e sua imagem é $\mathbb{R}$. Ambas são crescentes, e o gráfico de $g$ é a reflexão do gráfico de $f$ em relação ao eixo $x$, pois $g(x) = -f(x)$ para valores correspondentes.
  - *erro representado:* Confunde a simetria de funções inversas (em relação à reta $y=x$) com a simetria de funções opostas (em relação ao eixo $x$).

## Gabarito

O domínio de $f$ é $\mathbb{R}$ e sua imagem é $\mathbb{R}_{+}^{*}$; o domínio de $g$ é $\mathbb{R}_{+}^{*}$ e sua imagem é $\mathbb{R}$. Ambas são crescentes, e o gráfico de $g$ é a reflexão do gráfico de $f$ em relação à reta $y=x$, pois $g$ é a inversa de $f$.

## Resolução

**Passo 1 — Domínio e imagem de $f(x) = 2^x$.**

A função exponencial está definida para todo $x$ real, logo $D(f) = \mathbb{R}$. Como $2^x > 0$ para qualquer $x$, a imagem é $Im(f) = \mathbb{R}_{+}^{*} = (0, +\infty)$.

**Passo 2 — Domínio e imagem de $g(x) = \log_2(x)$.**

O logaritmo só está definido para argumentos positivos, então $D(g) = \mathbb{R}_{+}^{*} = (0, +\infty)$. Como o logaritmo pode assumir qualquer valor real (positivo, negativo ou zero), $Im(g) = \mathbb{R}$.

Note que $D(f) = Im(g)$ e $Im(f) = D(g)$: os conjuntos se invertem entre as duas funções.

**Passo 3 — Crescimento.**

Como a base $2 > 1$ em ambos os casos, $f$ é estritamente crescente (quanto maior $x$, maior $2^x$) e $g$ é estritamente crescente (quanto maior $x$, maior $\log_2(x)$).

**Passo 4 — Relação entre os gráficos.**

Como os pares $(x, f(x))$ satisfazem $f(x) = y \iff \log_2(y) = x$, temos que $g(x) = \log_2(x)$ é a função inversa de $f(x) = 2^x$. Sabe-se que o gráfico de qualquer função e o de sua inversa são simétricos em relação à reta $y = x$ (basta trocar as coordenadas $(x,y)$ por $(y,x)$). Logo, o gráfico de $g$ é obtido refletindo o gráfico de $f$ em torno da reta $y = x$.

**Conclusão:** $D(f)=\mathbb{R}$, $Im(f)=\mathbb{R}_{+}^{*}$; $D(g)=\mathbb{R}_{+}^{*}$, $Im(g)=\mathbb{R}$; ambas crescentes; gráficos simétricos em relação a $y=x$.

## Formalização verificável

- `funcao` — expressão `2**x`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2**x`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `2**x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(x, 2)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(x, 2)`, esperado `S.Reals`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `log(x, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 5 de 6 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado deixa claro o que é dado (as duas funções, já explicitamente definidas como inversas) e o que é pedido (comparar domínio, imagem e crescimento). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido é essencialmente reconhecer e relacionar propriedades já conhecidas (domínio/imagem trocados, crescimento mantido), compatível com o nível 'entender' de Bloom. A estrutura de resposta é multiestrutural (lista três características comparadas lado a lado), coerente com esse nível, embora o verbo 'analise' no enunciado sugira um processo cognitivo um pouco mais elevado do que o efetivamente demandado.
  - alinhamento_bncc: 5/5 — A questão articula exponencial e logarítmica num único problema, exigindo a comparação simultânea de domínio, imagem e crescimento e estabelecendo a relação de inversão entre elas — exatamente o que a EM13MAT403 demanda. Não se limita a calcular valores isolados.
  - distratores: 5/5 — Cada alternativa incorreta corresponde a um erro conceitual plausível e documentado na prática (troca de domínio/imagem entre f e g; ignorar a restrição x>0 do log; supor que inversão implica crescimento oposto). Nenhuma é trivialmente eliminável ou absurda.
  - originalidade: 2/5 — O enunciado já informa explicitamente que as funções são inversas e que o gráfico de g é obtido refletindo o de f em y=x. Essa informação antecipa boa parte da resposta (a relação domínio↔imagem trocados e a preservação do crescimento), configurando efeito Topaze. Além disso, é um enunciado muito próximo do modelo clássico de livro didático, sem contexto significativo ou elemento motivador além da definição matemática pura.
  - *sugestões:* Retire do enunciado a afirmação explícita de que f e g são inversas e a menção à reflexão em torno de y=x — deixe que o aluno precise perceber essa relação a partir da análise dos gráficos ou das leis das funções, em vez de recebê-la pronta. Uma alternativa é apresentar apenas as leis f(x)=2^x e g(x)=log2(x) (ou seus gráficos) e pedir que o estudante identifique, a partir da comparação, que características se relacionam e como. Também é recomendável inserir algum contexto ou situação (por exemplo, crescimento de uma grandeza e seu processo inverso) para tornar a questão menos genérica e mais próxima de uma situação significativa, evitando a reprodução do modelo padrão de livro didático.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Retire do enunciado a afirmação explícita de que f e g são inversas e a menção à reflexão em torno de y=x — deixe que o aluno precise perceber essa relação a partir da análise dos gráficos ou das leis das funções, em vez de recebê-la pronta. Uma alternativa é apresentar apenas as leis f(x)=2^x e g(x)=log2(x) (ou seus gráficos) e pedir que o estudante identifique, a partir da comparação, que características se relacionam e como. Também é recomendável inserir algum contexto ou situação (por exemplo, crescimento de uma grandeza e seu processo inverso) para tornar a questão menos genérica e mais próxima de uma situação significativa, evitando a reprodução do modelo padrão de livro didático.

### Iteração 2

- **Verificador:** aprovado_parcial — 5 de 6 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente f e g, especifica o que se pede (domínio, imagem, crescimento e relação gráfica) e não apresenta ambiguidade lexical ou estrutural. Os dados são suficientes para resolver a questão.
  - adequacao_nivel: 4/5 — A tarefa exige relacionar múltiplas características (domínio, imagem, crescimento, simetria gráfica) entre duas funções, o que corresponde a uma estrutura relacional na taxonomia SOLO, compatível com o nível 'entender' declarado. O conteúdo é apropriado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão articula exponencial e logarítmica num único problema, exige comparação simultânea de domínio, imagem e crescimento, e estabelece explicitamente a relação de inversão/simetria entre os gráficos, atendendo integralmente à EM13MAT403.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis: troca de domínio/imagem entre as funções, generalização indevida sobre monotonicidade do logaritmo, e confusão entre simetria de função inversa (reta y=x) e função oposta (eixo x). Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 4/5 — O contexto de crescimento bacteriano é um clássico da matemática aplicada, mas está bem integrado à pergunta conceitual, que não guia mecanicamente o raciocínio nem entrega pistas que pavimentem a resposta (efeito Topaze é evitado).
