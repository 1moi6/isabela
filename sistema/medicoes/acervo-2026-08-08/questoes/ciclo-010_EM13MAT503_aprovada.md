# Ciclo 010 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma empresa registrou, em três meses de testes de preço, os seguintes dados sobre o preço unitário $p$ (em reais) de um produto e o lucro mensal $L$ (em milhares de reais):

| Preço $p$ (R$) | Lucro $L(p)$ (mil R$) |
|---|---|
| 10 | 60 |
| 30 | 340 |
| 50 | 300 |

Sabe-se que, nesse intervalo de preços praticáveis pela empresa, $0 \le p \le 60$, o lucro pode ser modelado por uma função quadrática $L(p) = ap^2+bp+c$.

a) Determine os coeficientes $a$, $b$ e $c$ da função $L(p)$ a partir dos dados da tabela.

b) Calcule o preço que maximiza o lucro mensal e o valor desse lucro máximo.

c) Uma concorrente pratica o preço fixo de R\$ 45,00. Calcule o lucro que a empresa teria caso adotasse esse mesmo preço e compare com o lucro máximo obtido no item (b).

d) Calcule $L(0)$ e $L(60)$, interprete esses valores no contexto do problema e explique, usando o sinal do coeficiente $a$, por que o lucro cresce e depois decresce à medida que o preço aumenta de $0$ a $60$ reais.

## Gabarito

L(p) = -0,4p² + 30p - 200; preço ótimo p = R$37,50 com lucro máximo de 362,5 mil reais; ao preço da concorrência (R$45,00) o lucro seria 340 mil reais, 22,5 mil a menos; L(0) = -200 (prejuízo) e L(60) = 160 (lucro reduzido), consistentes com a concavidade negativa da parábola.

## Resolução

**a) Determinação da lei da função**

Substituindo os três pontos em $L(p)=ap^2+bp+c$:

$100a+10b+c=60$ (1)
$900a+30b+c=340$ (2)
$2500a+50b+c=300$ (3)

(2) $-$ (1): $800a+20b=280 \Rightarrow 40a+b=14$ (i)

(3) $-$ (2): $1600a+20b=-40 \Rightarrow 80a+b=-2$ (ii)

(ii) $-$ (i): $40a=-16 \Rightarrow a=-\dfrac{2}{5}=-0,4$

De (i): $b=14-40(-0,4)=14+16=30$

De (1): $c=60-100(-0,4)-10(30)=60+40-300=-200$

Logo, $L(p) = -0,4p^2+30p-200$.

**b) Ponto de máximo**

Como $a=-0,4<0$, a parábola tem concavidade para baixo, então o vértice é um ponto de **máximo**.

$$p^* = -\frac{b}{2a} = -\frac{30}{2(-0,4)} = \frac{30}{0,8}=37,5$$

$$L(37,5) = -0,4(37,5)^2+30(37,5)-200 = -562,5+1125-200 = 362,5$$

O preço ótimo é $p=R\$\,37{,}50$, com lucro máximo de $R\$\,362.500,00$ (362,5 mil reais).

**c) Comparação com a concorrência**

$$L(45) = -0,4(45)^2+30(45)-200 = -810+1350-200 = 340$$

Adotando o preço da concorrência, a empresa teria lucro de $340$ mil reais, ou seja, $362,5-340=22,5$ mil reais **a menos** do que praticando seu próprio preço ótimo.

**d) Análise nos extremos do domínio**

$$L(0) = -200 \qquad L(60) = -0,4(60)^2+30(60)-200 = -1440+1800-200 = 160$$

Em $p=0$ o lucro é $-200$ mil reais: sem cobrar nada pelo produto não há receita, e a empresa apenas acumula seus custos fixos, resultando em prejuízo. Em $p=60$ o lucro é $160$ mil reais, positivo, mas bem menor que o máximo de $362,5$ mil, pois um preço muito alto reduz a quantidade vendida.

Como $a=-0,4<0$, a função é côncava para baixo: o lucro cresce enquanto $p<37,5$ (aumentar o preço ainda compensa a perda de vendas) e decresce quando $p>37,5$ (a queda nas vendas passa a superar o ganho por unidade), confirmando que $p=37,5$ é de fato o ponto de máximo dentro do intervalo $[0,60]$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `-Rational(2,5)*p**2 + 30*p - 200`, parâmetros `{'pontos': '[(10,60),(30,340),(50,300)]', 'grau': '2'}`
- `funcao` — expressão `-Rational(2,5)*p**2 + 30*p - 200`, esperado `[Rational(75,2), Rational(725,2)]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-Rational(2,5)*p**2 + 30*p - 200`, esperado `340`, parâmetros `{'consulta': 'valor', 'ponto': '45'}`
- `funcao` — expressão `-Rational(2,5)*p**2 + 30*p - 200`, esperado `-200`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `-Rational(2,5)*p**2 + 30*p - 200`, esperado `160`, parâmetros `{'consulta': 'valor', 'ponto': '60'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (30, 2500)). | (2) aprovado: Gabarito confirmado (extremo calculado 2500).
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente a função, o domínio de validade, a variável e a grandeza pedida (preço ótimo e lucro máximo). Não há ambiguidade lexical ou estrutural; os dados são suficientes para resolver o problema sem suposições adicionais.
  - adequacao_nivel: 4/5 — O processo exigido (aplicar a fórmula do vértice, verificar a concavidade e checar o domínio) é compatível com o nível 'aplicar' de Bloom. A exigência de justificar que o ponto é máximo eleva a resposta a um nível relacional (SOLO), pois articula sinal do coeficiente, cálculo do vértice e verificação de domínio, e não apenas reproduz um algoritmo isolado. Não chega a exigir 'analisar' de fato (não há comparação de cenários ou interpretação crítica adicional), mas está coerente com o nível declarado.
  - alinhamento_bncc: 4/5 — A questão contextualiza a função quadrática em Matemática Financeira (lucro vs. preço), pede exatamente o ponto de máximo e exige uma justificativa que comprove que se trata de máximo — atendendo às exigências específicas listadas. O termo 'investigar' da habilidade é atendido de forma moderada, pois a tarefa é guiada por passos previsíveis (vértice, domínio, valor), sem exigir do aluno formular hipóteses próprias sobre a situação (ex.: por que o lucro cai fora do intervalo, ou comparação com preços de mercado). Ainda assim, cumpre concretamente o que foi especificado.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — O contexto 'lucro em função do preço, modelado por função quadrática com coeficiente negativo' é um dos exemplos mais recorrentes e genéricos em livros didáticos de Matemática Financeira. Os valores numéricos (vértice em p=30, domínio 0 a 60) também seguem o padrão-livro típico. Não há elemento que torne a situação significativa ou realista (dados de mercado, tabela, gráfico, comparação com concorrência), e a estrutura do enunciado praticamente antecipa o caminho de resolução (fórmula do vértice), configurando efeito Topaze leve.
  - *sugestões:* Reformule o contexto para reduzir o efeito 'exemplo de livro didático': (1) insira um elemento de dados reais ou verossímeis — por exemplo, apresente uma tabela com preços e lucros observados em três meses e peça que o aluno ajuste/reconheça a lei da função antes de otimizar, ou peça a interpretação do significado do coeficiente negativo em termos de mercado (por que lucro cai para preços muito altos ou muito baixos); (2) acrescente uma pergunta de investigação adicional coerente com 'investigar' da BNCC, como comparar o lucro máximo com o lucro em um preço fixado pela concorrência, ou pedir que o aluno discuta se o preço ótimo é praticável dado algum limite de mercado, tornando a tarefa mais analítica e menos um cálculo direto de vértice; (3) altere os coeficientes ou o formato numérico para evitar o padrão 'canônico' de vértice inteiro exato, e considere pedir also a análise do que ocorre nos extremos do domínio (p=0 e p=60) para reforçar a investigação do comportamento da função, não apenas o ponto de máximo.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule o contexto para reduzir o efeito 'exemplo de livro didático': (1) insira um elemento de dados reais ou verossímeis — por exemplo, apresente uma tabela com preços e lucros observados em três meses e peça que o aluno ajuste/reconheça a lei da função antes de otimizar, ou peça a interpretação do significado do coeficiente negativo em termos de mercado (por que lucro cai para preços muito altos ou muito baixos); (2) acrescente uma pergunta de investigação adicional coerente com 'investigar' da BNCC, como comparar o lucro máximo com o lucro em um preço fixado pela concorrência, ou pedir que o aluno discuta se o preço ótimo é praticável dado algum limite de mercado, tornando a tarefa mais analítica e menos um cálculo direto de vértice; (3) altere os coeficientes ou o formato numérico para evitar o padrão 'canônico' de vértice inteiro exato, e considere pedir also a análise do que ocorre nos extremos do domínio (p=0 e p=60) para reforçar a investigação do comportamento da função, não apenas o ponto de máximo.

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Propriedades confirmadas para -2*p**2/5 + 30*p - 200: reproduz os 3 pontos dados; grau 2. | (2) aprovado: Gabarito confirmado (vértice calculado (75/2, 725/2)). | (3) aprovado: Gabarito confirmado (f(45) = 340). | (4) aprovado: Gabarito confirmado (f(0) = -200). | (5) aprovado: Gabarito confirmado (f(60) = 160).
  - propriedade=aprovado
  - funcao/vertice=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com tabela de dados, domínio explícito e itens (a-d) claramente delimitados quanto ao que é dado e ao que se pede. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — Os itens a) e b) exigem aplicar procedimentos (resolver sistema linear, usar fórmula do vértice), coerentes com Bloom 'aplicar' e estrutura SOLO multiestrutural/relacional. Porém o item d) pede 'interprete' e 'explique o porquê', que são processos de nível analisar/avaliar, superiores ao aplicar declarado — leve descompasso entre o nível cognitivo nominal e o efetivamente demandado nesse item específico.
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as exigências: pede o ponto de máximo de uma função quadrática (item b) em contexto de Matemática Financeira (preço x lucro), e amplia para investigação genuína ao articular determinação da lei, comparação com cenário alternativo (item c) e análise de extremos do domínio com justificativa via sinal de 'a' (item d) — caracterizando investigação em situação, não mera manipulação algébrica isolada.
  - distratores: 5/5 — não se aplica
  - originalidade: 4/5 — O contexto preço-lucro é recorrente em livros didáticos, mas a estratégia de fornecer três pontos tabulados (exigindo montar e resolver um sistema para obter a lei, em vez de fornecê-la diretamente) e a articulação com um cenário concorrente (item c) evitam o formato mais mecânico e trivial, agregando originalidade moderada sem grandes pistas de resolução (efeito Topaze) explícitas.
