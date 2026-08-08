# Ciclo 021 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 2

## Enunciado

No mesmo plano cartesiano estão representadas duas curvas, $C_1$ e $C_2$, associadas a duas funções reais $f$ e $g$, cada uma definida por uma única sentença (sem sentenças por partes). Sabe-se que:

- $C_1$ passa pelos pontos $\left(-1,\ \dfrac{1}{2}\right)$, $(0,1)$, $(1,2)$ e $(2,4)$;
- $C_2$ passa pelos pontos $\left(\dfrac{1}{2},\ -1\right)$, $(1,0)$, $(2,1)$ e $(4,2)$;
- $C_1$ e $C_2$ são simétricas uma em relação à outra em torno da reta $y=x$.

Com base na leitura desses pontos e na relação de simetria entre as curvas, assinale a alternativa que descreve corretamente o domínio, a imagem e o comportamento de crescimento de $f$ e de $g$.

## Alternativas

- (a) $f$ tem domínio $\mathbb{R}$ e imagem $(0,+\infty)$; $g$ tem domínio $(0,+\infty)$ e imagem $\mathbb{R}$; ambas são crescentes em todo o seu domínio.  ← correta
- (b) $f$ tem domínio $(0,+\infty)$ e imagem $\mathbb{R}$; $g$ tem domínio $\mathbb{R}$ e imagem $(0,+\infty)$; ambas são crescentes.
  - *erro representado:* Inverteu qual curva é a exponencial e qual é a logarítmica: atribuiu a $f$ o domínio/imagem que pertence a $g$ e vice-versa, provavelmente por confundir o efeito da simetria em torno de $y=x$.
- (c) $f$ tem domínio $\mathbb{R}$ e imagem $(0,+\infty)$; $g$ tem domínio $\mathbb{R}$ e imagem $\mathbb{R}$; ambas são crescentes.
  - *erro representado:* Esqueceu a restrição de existência da função logarítmica (só definida para argumentos positivos), atribuindo erroneamente domínio real a $g$.
- (d) $f$ é crescente, mas $g$ é decrescente, pois $C_2$ passa por pontos com ordenada negativa.
  - *erro representado:* Confundiu o sinal dos valores da função (ordenadas negativas) com o sentido de variação (crescente/decrescente), concluindo incorretamente que valores negativos implicam decrescimento.

## Gabarito

Alternativa A: $f$ tem domínio $\mathbb{R}$ e imagem $(0,+\infty)$; $g$ tem domínio $(0,+\infty)$ e imagem $\mathbb{R}$; ambas são crescentes em todo o seu domínio.

## Resolução

**Passo 1 — Reconhecer o padrão de $C_1$.**

Os pontos de $C_1$ são $(-1,\tfrac12), (0,1), (1,2), (2,4)$. A cada aumento de $1$ unidade em $x$, o valor de $y$ dobra: $\tfrac12 \to 1 \to 2 \to 4$. Esse é o comportamento característico de uma função exponencial de base $2$: $f(x) = 2^x$. Verificando: $f(-1)=2^{-1}=\tfrac12$, $f(0)=1$, $f(1)=2$, $f(2)=4$. ✓

**Passo 2 — Reconhecer o padrão de $C_2$.**

Os pontos de $C_2$ são exatamente os pontos de $C_1$ com as coordenadas trocadas: $(-1,\tfrac12)\to(\tfrac12,-1)$, $(0,1)\to(1,0)$, $(1,2)\to(2,1)$, $(2,4)\to(4,2)$. Trocar as coordenadas de todos os pontos de uma curva é exatamente a operação que gera a **função inversa**. Logo $g = f^{-1}$, isto é, $g(x) = \log_2(x)$. Verificando: $g(\tfrac12)=\log_2(\tfrac12)=-1$, $g(1)=0$, $g(2)=1$, $g(4)=2$. ✓

**Passo 3 — Usar a simetria em relação a $y=x$.**

Como $g$ é a inversa de $f$, o gráfico de $g$ é o reflexo do gráfico de $f$ em torno da reta $y=x$ — o que é coerente com a informação dada no enunciado. Uma consequência direta dessa relação é que **domínio e imagem se trocam** entre a função e sua inversa:
$$\text{Dom}(f) = \text{Im}(g) \quad \text{e} \quad \text{Im}(f) = \text{Dom}(g).$$

**Passo 4 — Determinar domínio e imagem de cada uma.**

- $f(x)=2^x$: está definida para todo $x$ real, e como $2^x>0$ sempre, $\text{Dom}(f)=\mathbb{R}$ e $\text{Im}(f)=(0,+\infty)$.
- $g(x)=\log_2(x)$: só está definida para $x>0$, e assume qualquer valor real, logo $\text{Dom}(g)=(0,+\infty)$ e $\text{Im}(g)=\mathbb{R}$.

Isso confirma a relação do Passo 3: $\text{Dom}(f)=\mathbb{R}=\text{Im}(g)$ e $\text{Im}(f)=(0,+\infty)=\text{Dom}(g)$.

**Passo 5 — Analisar o crescimento.**

Como a base $2>1$ em ambas as expressões, a exponencial $f(x)=2^x$ é **crescente** em $\mathbb{R}$, e sua inversa $g(x)=\log_2(x)$ também é **crescente** em $(0,+\infty)$ (funções inversas de funções crescentes são crescentes). Note que $C_2$ conter pontos com ordenada negativa não indica decrescimento: apenas significa que, para $x$ entre $0$ e $1$, $g(x)$ é negativo — o valor da função, não seu sentido de variação.

**Conclusão:** $f$ tem domínio $\mathbb{R}$ e imagem $(0,+\infty)$; $g$ tem domínio $(0,+\infty)$ e imagem $\mathbb{R}$; ambas são crescentes.

## Formalização verificável

- `funcao` — expressão `2**x`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2**x`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'S.Reals'}`
- `funcao` — expressão `2**x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(x, 2)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(x, 2)`, esperado `S.Reals`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval.open(0, oo)'}`
- `funcao` — expressão `log(x, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `propriedade` — expressão `-`, esperado `2**x`, parâmetros `{'pontos': '[(-1, Rational(1,2)), (0, 1), (1, 2), (2, 4)]'}`
- `propriedade` — expressão `-`, esperado `log(x, 2)`, parâmetros `{'pontos': '[(Rational(1,2), -1), (1, 0), (2, 1), (4, 2)]'}`

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
  - clareza: 5/5 — O enunciado é direto: define claramente as duas funções, pede domínio, imagem, crescimento e relação entre os gráficos, sem ambiguidade lexical ou estrutural. Todos os dados necessários estão presentes.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (reconhecer e relacionar propriedades já estudadas de exponencial/log) corresponde ao nível 'entender' declarado. A resposta é multiestrutural (várias propriedades) com um componente relacional (simetria/inversibilidade), compatível com o nível pedido, sem exigir análise crítica mais profunda — o que é coerente com 'entender', não com 'analisar' ou 'avaliar'.
  - alinhamento_bncc: 5/5 — A questão trata exponencial e logarítmica simultaneamente, compara domínio, imagem e crescimento das duas, e articula-as explicitamente por meio da relação de inversibilidade e simetria em torno de y=x, cumprindo integralmente a EM13MAT403 tal como especificada, sem se limitar a cálculo de valores isolados.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis: troca de domínio/imagem entre as funções, crença equivocada de que log é sempre decrescente e confusão do eixo de simetria, e atribuição errada de sinal às imagens negando a relação de inversas. Nenhum é trivialmente eliminável à primeira vista, embora o distrator 4 acumule dois erros ao mesmo tempo, tornando-o um pouco mais fácil de descartar por atenção ao sinal de 2^x.
  - originalidade: 2/5 — O enunciado é uma reprodução quase canônica de exercícios de livro didático sobre exponencial/log: sem contexto aplicado, sem uso de gráfico real ou dado a ser interpretado, apenas pede a enumeração padrão de domínio/imagem/crescimento/simetria — exatamente a sequência mnemônica que aparece em praticamente todo material didático sobre o tema.
  - *sugestões:* Reformule o enunciado para sair do modelo 'liste as propriedades de f e g' e criar um cenário significativo que exija comparação real entre as duas representações gráficas — por exemplo, apresentar os gráficos de f(x)=2^x e g(x)=log2(x) (sem as fórmulas, apenas as curvas) em um mesmo plano cartesiano e pedir para o aluno identificar, a partir da leitura gráfica, qual curva é qual, justificando pela simetria em relação a y=x, ou inserir um contexto aplicado (ex.: crescimento de uma população em função do tempo e o tempo necessário para atingir certo tamanho, usando a inversa) que force o aluno a usar a relação entre as duas funções para resolver algo, não apenas descrevê-las. Isso preserva o alinhamento à BNCC e ao nível 'entender', mas evita o formato mecânico de lista de propriedades.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule o enunciado para sair do modelo 'liste as propriedades de f e g' e criar um cenário significativo que exija comparação real entre as duas representações gráficas — por exemplo, apresentar os gráficos de f(x)=2^x e g(x)=log2(x) (sem as fórmulas, apenas as curvas) em um mesmo plano cartesiano e pedir para o aluno identificar, a partir da leitura gráfica, qual curva é qual, justificando pela simetria em relação a y=x, ou inserir um contexto aplicado (ex.: crescimento de uma população em função do tempo e o tempo necessário para atingir certo tamanho, usando a inversa) que force o aluno a usar a relação entre as duas funções para resolver algo, não apenas descrevê-las. Isso preserva o alinhamento à BNCC e ao nível 'entender', mas evita o formato mecânico de lista de propriedades.

### Iteração 2

- **Verificador:** aprovado_parcial — 7 de 8 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)). | (7) aprovado: Propriedades confirmadas para 2**x: reproduz os 4 pontos dados. | (8) aprovado: Propriedades confirmadas para log(x)/log(2): reproduz os 4 pontos dados.
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - propriedade=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta dados completos (pontos das duas curvas) e uma pergunta única e bem delimitada (domínio, imagem, crescimento). Não há ambiguidade lexical ou estrutural; a condição de simetria em y=x está explicitada, reforçando a leitura correta.
  - adequacao_nivel: 3/5 — A tarefa exige inferir a lei de duas funções a partir de padrões numéricos, aplicar a propriedade de inversas (troca de domínio/imagem) e articular isso com crescimento — um processo relacional (SOLO) que se aproxima mais de 'analisar/aplicar' do que de 'entender'. O nível cognitivo efetivamente demandado é mais exigente que o declarado, havendo descompasso entre a complexidade real da questão e o rótulo de Bloom escolhido.
  - alinhamento_bncc: 5/5 — A questão articula exponencial e logarítmica em um único problema (via simetria/inversa), comparando explicitamente domínio, imagem e crescimento das duas funções, exatamente como pede EM13MAT403. Não se limita a calcular valores isolados; exige estabelecer a relação entre as representações gráficas.
  - distratores: 5/5 — As três alternativas incorretas correspondem a erros conceituais plausíveis e distintos: troca de domínio/imagem entre f e g, esquecimento da restrição de existência do logaritmo, e confusão entre sinal da imagem e sentido de crescimento. Nenhuma é absurda ou trivialmente descartável.
  - originalidade: 4/5 — O uso de pontos simétricos para induzir o reconhecimento de exponencial/logarítmica e da relação de inversibilidade foge do padrão 'dado f(x)=2^x, calcule...'. Ainda assim, o padrão numérico (dobrar a cada unidade) é um recurso didático já bastante comum, o que reduz um pouco o ineditismo do contexto.
