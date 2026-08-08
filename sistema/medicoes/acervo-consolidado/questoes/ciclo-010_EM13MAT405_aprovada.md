# Ciclo 010 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento cobra a tarifa de água residencial, em reais, em função do consumo mensal $x$ (em $m^3$), segundo a lei:

$$f(x) = \begin{cases} 15, & 0 \le x \le 5 \\ 15 + 4(x-5), & x > 5 \end{cases}$$

em que $x$ representa o volume consumido no mês (um número real não negativo, podendo assumir qualquer valor, inclusive não inteiro).

Assinale a alternativa que descreve corretamente o gráfico de $f$, seu domínio de validade, sua imagem e seu comportamento de crescimento/decrescimento.

## Alternativas

- (a) O gráfico é um segmento horizontal em $y=15$ para $0\le x\le 5$, seguido de uma semirreta crescente de coeficiente angular $4$ partindo do ponto $(5,15)$, sem salto; domínio $[0,+\infty)$, imagem $[15,+\infty)$, crescente para $x>5$.  ← correta
- (b) O gráfico é um segmento horizontal em $y=15$ para $0\le x\le 5$, seguido de uma reta decrescente de coeficiente angular $-4$ a partir de $(5,15)$, com domínio $[0,+\infty)$ e imagem $(-\infty,15]$.
  - *erro representado:* Interpretou erroneamente o sinal do coeficiente da segunda sentença, supondo que a tarifa cai com o aumento do consumo, quando na verdade o coeficiente é positivo (função crescente).
- (c) O gráfico é um segmento horizontal em $y=15$ até $x=5$, seguido de um salto até $y=35$ e depois uma reta crescente de coeficiente angular $4$, pois para $x>5$ deve-se usar diretamente $f(x)=15+4x$.
  - *erro representado:* Não distribuiu corretamente o termo $4(x-5)$, esquecendo de subtrair $5$ antes de multiplicar, o que introduz uma descontinuidade inexistente no gráfico.
- (d) O gráfico é apenas o segmento horizontal em $y=15$, pois a função só está definida para $0\le x\le 5$; fora desse intervalo, $f$ não possui domínio de validade.
  - *erro representado:* Ignorou a segunda sentença da função por partes, tratando o intervalo de validade da primeira sentença como se fosse o domínio de toda a função.

## Gabarito

O gráfico é um segmento horizontal em $y=15$ para $0\le x\le 5$, seguido de uma semirreta crescente de coeficiente angular $4$ partindo de $(5,15)$, sem descontinuidade; domínio $[0,+\infty)$, imagem $[15,+\infty)$, e a função é crescente para $x>5$.

## Resolução

**1. Simplificando a segunda sentença**

Para $x>5$: $f(x) = 15 + 4(x-5) = 15 + 4x - 20 = 4x - 5$.

**2. Verificando a continuidade no ponto de troca ($x=5$)**

- Pela primeira sentença: $f(5) = 15$.
- Pela segunda sentença (limite quando $x\to 5^+$): $4(5)-5 = 15$.

Como os dois valores coincidem, o gráfico **não tem salto** em $x=5$: a reta crescente parte exatamente do ponto $(5,15)$, sem descontinuidade.

**3. Forma do gráfico**

- Para $0 \le x \le 5$: segmento **horizontal** em $y=15$ (a tarifa mínima, constante).
- Para $x>5$: **semirreta crescente**, pois o coeficiente angular é $4>0$, partindo de $(5,15)$ e subindo indefinidamente.

**4. Domínio de validade**

Como $x$ é um consumo (não pode ser negativo e não há limite superior imposto), o domínio é $[0, +\infty)$.

**5. Imagem**

O menor valor de $f$ é $15$ (atingido em todo o trecho $[0,5]$), e para $x>5$ os valores crescem sem limite. Logo, a imagem é $[15, +\infty)$.

**6. Crescimento**

No intervalo $[0,5]$ a função é constante; no intervalo $[5,+\infty)$ ela é **crescente**, pois o coeficiente angular da reta é positivo (igual a 4).

**Conclusão:** o gráfico é um segmento horizontal em $y=15$ até $x=5$, seguido de uma semirreta crescente de coeficiente angular $4$ a partir de $(5,15)$, sem salto; domínio $[0,+\infty)$; imagem $[15,+\infty)$; crescente para $x>5$.

## Formalização verificável

- `funcao` — expressão `Piecewise((15, (x >= 0) & (x <= 5)), (4*x - 5, x > 5))`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((15, (x >= 0) & (x <= 5)), (4*x - 5, x > 5))`, esperado `Interval(15, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`
- `funcao` — expressão `4*x - 5`, esperado `crescente`, parâmetros `{'consulta': 'crescimento', 'dominio': 'Interval(5, oo)'}`
- `funcao` — expressão `Piecewise((15, (x >= 0) & (x <= 5)), (4*x - 5, x > 5))`, esperado `15`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 2 de 4 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((15, (x >= 0) & (x <= 5)), (4*x - 5, x > 5)). Conferir manualmente. | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((15, (x >= 0) & (x <= 5)), (4*x - 5, x > 5)). Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Reals). | (4) aprovado: Gabarito confirmado (f(5) = 15).
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a lei da função por partes, especifica o domínio de x (real não negativo) e pede explicitamente gráfico, domínio, imagem e monotonicidade. Não há ambiguidade lexical ou de dados incompletos.
  - adequacao_nivel: 4/5 — A tarefa exige combinar simplificação algébrica, verificação de continuidade, determinação de domínio, imagem e crescimento/decrescimento simultaneamente — isso é mais próximo de uma estrutura relacional (SOLO) do que de uma simples aplicação isolada de regra, o que extrapola levemente o nível 'aplicar' declarado, mas ainda é compatível com Ensino Médio e não chega a exigir análise crítica/comparativa entre múltiplos modelos.
  - alinhamento_bncc: 5/5 — Cumpre integralmente as exigências: função com mais de uma sentença em contexto real (conta de água), exige converter entre representação algébrica e gráfica e identificar domínio, imagem e monotonicidade em um único problema articulado, não apenas avaliar a função em um ponto.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis (erro de sinal no coeficiente, erro de distribuição algébrica gerando falsa descontinuidade, e desconsideração da segunda sentença). Nenhum é absurdo, embora o distrator 4 seja um pouco mais fácil de descartar por um aluno atento ao enunciado.
  - originalidade: 4/5 — O contexto de tarifa de água é comum em livros didáticos, mas o enunciado evita o clichê ao explorar a continuidade da função (evitando o salto típico), o que agrega uma sutileza pouco padronizada. Não há pistas explícitas que resolvam a questão antes do raciocínio do aluno.
