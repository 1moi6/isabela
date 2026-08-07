# Ciclo 009 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento cobra a conta de água de um domicílio residencial conforme a função por partes abaixo, em que $x$ é o consumo mensal em metros cúbicos ($m^3$) e $C(x)$ é o valor da conta, em reais, válida para consumos entre $0$ e $30\,m^3$:

$$C(x) = \begin{cases} 20, & 0 \le x \le 10 \\ 20 + 2{,}5\,(x-10), & 10 < x \le 30 \end{cases}$$

Assinale a alternativa que descreve corretamente o gráfico de $C$ no intervalo $[0,30]$, indicando de forma coerente os trechos constante e crescente, o domínio, a imagem e o comportamento de crescimento da função.

## Alternativas

- (a) Para $0\le x\le10$ o gráfico é um segmento horizontal em $C=20$; para $10< x\le30$ é um segmento de reta crescente que vai de $(10,20)$ até $(30,70)$. O domínio é $[0,30]$, a imagem é $[20,70]$ e a função é crescente.  ← correta
- (b) O gráfico é um segmento horizontal em $C=20$ para todo $x\in[0,30]$; a imagem é $\{20\}$ e a função é constante (nem crescente nem decrescente).
  - *erro representado:* Ignorar a segunda sentença da função, tratando toda a conta como um valor fixo em qualquer consumo.
- (c) O gráfico é uma única reta crescente, de $(0,20)$ até $(30,95)$, sem nenhum trecho constante; o domínio é $[0,30]$ e a imagem é $[20,95]$.
  - *erro representado:* Aplicar a expressão da segunda sentença a todo o domínio, calculando erradamente $C(x) = 20 + 2{,}5x$ em vez de $20 + 2{,}5(x-10)$, obtendo $C(30)=95$.
- (d) O gráfico tem um trecho constante em $C=20$ até $x=10$ e depois cresce linearmente até $(30,70)$; porém a imagem correta é $[0,70]$, pois o consumo poderia ser nulo.
  - *erro representado:* Confundir o domínio de $x$ (que inclui o valor $0$) com o menor valor da função, supondo erroneamente que a imagem começa em $0$.

## Gabarito

Segmento constante em $C=20$ para $0\le x\le10$, seguido de reta crescente até $(30,70)$; domínio $[0,30]$, imagem $[20,70]$, função crescente.

## Resolução

**Passo 1 — Analisar a primeira sentença.** Para $0 \le x \le 10$, temos $C(x) = 20$, um valor fixo. Logo, o gráfico nesse trecho é um **segmento horizontal** em $C=20$, dos pontos $(0,20)$ até $(10,20)$.

**Passo 2 — Analisar a segunda sentença.** Para $10 < x \le 30$, temos $C(x) = 20 + 2{,}5(x-10) = 2{,}5x - 5$. Essa é uma função afim crescente (coeficiente angular $2{,}5>0$). Verificando a continuidade em $x=10$: $C(10^+) = 2{,}5(10)-5 = 20$, que coincide com o valor do primeiro trecho — o gráfico não tem 'salto'.

Calculando o valor no extremo direito: $C(30) = 2{,}5(30) - 5 = 75 - 5 = 70$.

Assim, o segundo trecho é um **segmento de reta crescente** de $(10,20)$ até $(30,70)$.

**Passo 3 — Determinar o domínio.** Pelo próprio enunciado, a função é válida para $x \in [0,30]$, logo $D = [0,30]$.

**Passo 4 — Determinar a imagem.** Como a função é constante em $20$ até $x=10$ e depois cresce continuamente até atingir $70$ em $x=30$, o menor valor assumido é $20$ e o maior é $70$. Logo, a imagem é $Im = [20,70]$.

**Passo 5 — Classificar o crescimento.** Em nenhum ponto do domínio a função diminui: ela é constante em $[0,10]$ e estritamente crescente em $(10,30]$. Por isso, globalmente ela é classificada como **crescente** (não decrescente em nenhum trecho).

**Conclusão.** O gráfico correto é: segmento horizontal em $C=20$ até $x=10$, seguido de segmento de reta crescente até $(30,70)$, com domínio $[0,30]$, imagem $[20,70]$ e função crescente.

## Formalização verificável

- `funcao` — expressão `Piecewise((20, And(x>=0, x<=10)), (Rational(5,2)*x - 5, And(x>10, x<=30)))`, esperado `Interval(0,30)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((20, And(x>=0, x<=10)), (Rational(5,2)*x - 5, And(x>10, x<=30)))`, esperado `Interval(20,70)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `Piecewise((20, And(x>=0, x<=10)), (Rational(5,2)*x - 5, And(x>10, x<=30)))`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `Piecewise((20, And(x>=0, x<=10)), (Rational(5,2)*x - 5, And(x>10, x<=30)))`, esperado `70`, parâmetros `{'consulta': 'valor', 'ponto': '30'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 1 de 4 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((20, (x >= 0) & (x <= 10)), (5*x/2 - 5, (x <= 30) & (x > 10))). Conferir manualmente. | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((20, (x >= 0) & (x <= 10)), (5*x/2 - 5, (x <= 30) & (x > 10))). Conferir manualmente. | (3) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((20, (x >= 0) & (x <= 10)), (5*x/2 - 5, (x <= 30) & (x > 10))). Conferir manualmente. | (4) aprovado: Gabarito confirmado (f(30) = 70).
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=nao_verificavel
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta a função por partes de forma explícita, define claramente o domínio de validade (0 a 30 m³) e pede a identificação de trechos, domínio, imagem e crescimento sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A tarefa de converter a expressão algébrica em descrição gráfica, calculando os valores nos extremos e classificando o crescimento, é compatível com o nível 'entender' (compreensão/interpretação de representações). A resposta exige integrar múltiplos aspectos (domínio, imagem, trechos, crescimento) de forma relacional, coerente com SOLO relacional. Não chega a exigir análise crítica mais profunda, mas está alinhada ao nível declarado.
  - alinhamento_bncc: 5/5 — A questão usa exatamente o contexto sugerido pela habilidade (conta de água), define a função por mais de uma sentença, exige mobilizar a mudança de sentença (cálculo em x=10 e x=30) e articula domínio, imagem e crescimento numa única tarefa integrada — não apenas avalia um ponto isolado.
  - distratores: 5/5 — Cada alternativa incorreta reflete um erro sistemático plausível: ignorar a segunda sentença, aplicar a fórmula errada em todo o domínio, ou confundir domínio com imagem. Nenhum distrator é absurdo ou trivialmente eliminável.
  - originalidade: 4/5 — O contexto de conta de água por faixas de consumo é significativo e realista, embora seja um tipo de contexto relativamente comum em livros didáticos. Não há pistas excessivas que antecipem a resposta (efeito Topaze), pois o aluno ainda precisa calcular os valores nos extremos.
