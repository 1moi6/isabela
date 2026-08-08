# Ciclo 002 — EM13MAT405

- **Situação:** aprovada
- **Temas:** funcao_por_partes
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma companhia de saneamento cobra a conta de água residencial mensal com base no consumo $x$, medido em metros cúbicos ($m^3$), segundo a lei abaixo, em que $C(x)$ é o valor da conta, em reais. Considere que $x$ pode assumir qualquer valor real não negativo (não necessariamente inteiro).

$$C(x) = \begin{cases} 15 + 2x, & \text{se } 0 \le x \le 10 \\ 35 + 4(x-10), & \text{se } x > 10 \end{cases}$$

a) Determine o domínio de validade dessa função, considerando o significado de $x$ no contexto.

b) Calcule o valor da conta para um consumo de exatamente $10\,m^3$ e para um consumo de $12\,m^3$, indicando em cada caso qual das duas sentenças da lei foi utilizada.

c) Determine a imagem da função $C$.

d) A função $C$ é crescente, decrescente ou nenhuma das duas coisas em todo o seu domínio? Justifique observando o comportamento de cada sentença.

e) Descreva (sem desenhar) o formato do gráfico de $C$: de que tipo são os dois trechos, se há salto (descontinuidade) no ponto de junção $x=10$, e como se compara a inclinação de um trecho com a do outro.

## Gabarito

a) Domínio: $[0,+\infty)$. b) $C(10)=35$ (1ª sentença); $C(12)=43$ (2ª sentença). c) Imagem: $[15,+\infty)$. d) $C$ é crescente em todo o domínio. e) Duas semirretas que se encontram sem salto em $(10,35)$, sendo a segunda mais inclinada (coeficiente angular 4) que a primeira (coeficiente angular 2).

## Resolução

**a) Domínio de validade**

Como $x$ representa um consumo de água, não pode ser negativo, e não há um limite superior estabelecido no problema (o consumo pode crescer indefinidamente). Logo, o domínio é

$$D = [0, +\infty) = \text{Interval}(0,\infty).$$

**b) Valores em $x=10$ e $x=12$ (mobilizando a mudança de sentença)**

Como $10$ satisfaz $0 \le x \le 10$, usamos a **primeira** sentença:
$$C(10) = 15 + 2\cdot 10 = 15 + 20 = 35.$$

Como $12 > 10$, usamos a **segunda** sentença:
$$C(12) = 35 + 4(12-10) = 35 + 4\cdot 2 = 35 + 8 = 43.$$

Observe que a mudança de regra em $x=10$ não gera salto: as duas sentenças coincidem exatamente nesse ponto ($C(10)=35$ pelas duas expressões), garantindo continuidade.

**c) Imagem**

No trecho $0 \le x \le 10$: $C(x) = 15+2x$ é linear crescente, variando de $C(0)=15$ até $C(10)=35$. Logo, nesse trecho, $C$ assume todos os valores em $[15,35]$.

No trecho $x>10$: $C(x) = 35+4(x-10)$ também é linear crescente, partindo de valores próximos (mas maiores) que $35$ e crescendo sem limite quando $x \to \infty$. Logo, nesse trecho, $C$ assume todos os valores em $(35, +\infty)$.

Unindo os dois conjuntos de valores:
$$\text{Im}(C) = [15,35] \cup (35,\infty) = [15,+\infty) = \text{Interval}(15,\infty).$$

**d) Crescimento**

No primeiro trecho, o coeficiente angular é $2>0$: função crescente.
No segundo trecho, o coeficiente angular é $4>0$: função crescente.
Como os dois trechos são crescentes e se encaixam continuamente em $x=10$ (sem salto para baixo), $C$ é **crescente em todo o domínio** $[0,+\infty)$.

**e) Formato do gráfico**

O gráfico é formado por dois segmentos de reta:
- de $(0,15)$ até $(10,35)$, com inclinação $2$;
- a partir de $(10,35)$, seguindo indefinidamente, com inclinação $4$.

Como os dois valores coincidem em $x=10$, não há salto (descontinuidade) no gráfico: as duas retas se encontram exatamente nesse ponto, formando um "bico" onde a reta muda de inclinação, ficando **mais inclinada** (mais íngreme) para $x>10$ do que para $0 \le x \le 10$.

## Formalização verificável

- `funcao` — expressão `Piecewise((15 + 2*x, (x >= 0) & (x <= 10)), (35 + 4*(x - 10), x > 10))`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `Piecewise((15 + 2*x, (x >= 0) & (x <= 10)), (35 + 4*(x - 10), x > 10))`, esperado `Interval(15, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`
- `funcao` — expressão `Piecewise((15 + 2*x, (x >= 0) & (x <= 10)), (35 + 4*(x - 10), x > 10))`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `Piecewise((15 + 2*x, (x >= 0) & (x <= 10)), (35 + 4*(x - 10), x > 10))`, esperado `35`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `funcao` — expressão `Piecewise((15 + 2*x, (x >= 0) & (x <= 10)), (35 + 4*(x - 10), x > 10))`, esperado `43`, parâmetros `{'consulta': 'valor', 'ponto': '12'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 2 de 5 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((2*x + 15, (x >= 0) & (x <= 10)), (4*x - 5, x > 10)). Conferir manualmente. | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((2*x + 15, (x >= 0) & (x <= 10)), (4*x - 5, x > 10)). Conferir manualmente. | (3) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((2*x + 15, (x >= 0) & (x <= 10)), (4*x - 5, x > 10)). Conferir manualmente. | (4) aprovado: Gabarito confirmado (f(10) = 35). | (5) aprovado: Gabarito confirmado (f(12) = 43).
  - funcao/dominio=nao_verificavel
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=nao_verificavel
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem construído, com definição precisa da lei de formação, domínio contextual explicitado e subitens claramente delimitados (o que é dado e o que se pede em cada um). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A maior parte das tarefas (calcular valores mobilizando a troca de sentença, determinar domínio/imagem, comparar coeficientes angulares) é compatível com 'entender' (interpretar, comparar, explicar), nível SOLO multiestrutural/relacional. Os itens d) e e), que exigem justificar continuidade e comparar inclinações, tangenciam 'analisar', mas isso está alinhado ao que a própria habilidade BNCC pede (crescimento/decrescimento, domínio, imagem), então a exigência cognitiva não destoa gravemente do nível declarado.
  - alinhamento_bncc: 4/5 — A questão usa função definida por duas sentenças em contexto real (conta de água), exige domínio de validade, imagem e análise de crescimento, e o item b) mobiliza explicitamente a mudança de sentença (x=10 e x=12), cumprindo o requisito central da habilidade. O ponto fraco é o item e): pede 'descrever sem desenhar' o gráfico, o que atende apenas parcialmente à exigência de 'converter entre representação algébrica e gráfica' — não há conversão efetiva (nem leitura de gráfico dado, nem produção de gráfico), apenas descrição verbal. Ainda assim, os demais objetivos da habilidade são plenamente atendidos.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — O contexto de conta de água é um dos exemplos citados na própria habilidade BNCC, portanto não é totalmente original, mas a condução por múltiplos subitens (domínio, avaliação pontual, imagem, monotonicidade, descrição gráfica) evita a repetição mecânica de um exercício-padrão de livro didático e não entrega pistas que reduzam o raciocínio do aluno a uma aplicação trivial.
