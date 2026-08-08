# Ciclo 076 — EM13MAT401

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Duas empresas de aplicativo de transporte, A e B, calculam o valor da corrida em função da distância percorrida $x$ (em km). A empresa A cobra R$ 2,50 por quilômetro rodado, sem nenhuma taxa adicional. A empresa B cobra uma taxa fixa de embarque de R$ 3,00 mais R$ 2,00 por quilômetro rodado. Sejam $y_A(x)$ e $y_B(x)$, em reais, os custos totais das corridas das empresas A e B, respectivamente, em função de $x$. Se essas duas funções forem representadas por retas em um plano cartesiano (custo $y$ no eixo vertical e distância $x$ no eixo horizontal), assinale a alternativa que descreve corretamente essas retas.

## Alternativas

- (a) A reta que representa a empresa A passa pela origem (0,0) e tem coeficiente angular 2,5, sendo uma função proporcional; a reta da empresa B corta o eixo y no ponto (0,3) e tem coeficiente angular 2, não sendo proporcional.  ← correta
- (b) A reta que representa a empresa B passa pela origem (0,0), pois seu coeficiente angular é 2; a reta da empresa A corta o eixo y no ponto (0,3), pois seu coeficiente angular é 2,5.
  - *erro representado:* Trocar as funções: atribuir o comportamento proporcional (passar pela origem) à empresa que possui taxa fixa, e vice-versa.
- (c) Ambas as retas passam pela origem (0,0), já que representam custo por quilômetro rodado; a reta de A tem coeficiente angular 2,5 e a de B tem coeficiente angular 2.
  - *erro representado:* Ignorar o termo constante (taxa fixa) da função afim, supondo que qualquer função 'por km rodado' é proporcional e passa pela origem.
- (d) A reta da empresa A corta o eixo y no ponto (0, 2,5); a reta da empresa B corta o eixo y no ponto (0,2) e tem coeficiente angular 3.
  - *erro representado:* Confundir o papel do coeficiente angular com o do termo independente, trocando os valores de a e b na leitura do gráfico.

## Gabarito

A reta que representa a empresa A passa pela origem $(0,0)$ e tem coeficiente angular 2,5 (função proporcional); a reta da empresa B corta o eixo y no ponto $(0,3)$ e tem coeficiente angular 2 (função afim, não proporcional).

## Resolução

**Passo 1 — Escrever as leis das funções.**

Empresa A: cobra só por km rodado, sem taxa fixa: $y_A(x) = 2{,}5x$.

Empresa B: cobra taxa fixa de R\$3,00 mais R\$2,00 por km: $y_B(x) = 2x + 3$.

**Passo 2 — Analisar a natureza de cada função.**

$y_A(x) = 2{,}5x$ é da forma $y = ax$ (sem termo constante), logo é uma função **linear/proporcional**. Seu gráfico é uma reta que passa pela origem $(0,0)$, já que $y_A(0) = 2{,}5 \cdot 0 = 0$. O coeficiente angular é $a = 2{,}5$.

$y_B(x) = 2x+3$ é da forma $y = ax+b$ com $b = 3 \neq 0$, logo é uma função **afim não proporcional**. Seu gráfico é uma reta que **não** passa pela origem, pois $y_B(0) = 3 \neq 0$. Ela corta o eixo $y$ no ponto $(0,3)$ e tem coeficiente angular $a = 2$.

**Passo 3 — Conclusão geométrica.**

A reta de A passa pela origem (comportamento proporcional, coeficiente angular 2,5); a reta de B corta o eixo $y$ em $(0,3)$ (comportamento afim, não proporcional, coeficiente angular 2). As duas retas são crescentes, pois ambos os coeficientes angulares são positivos, mas apenas a de A representa proporcionalidade direta entre custo e distância.

## Formalização verificável

- `funcao` — expressão `Rational(5,2)*x`, esperado `0`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `2*x + 3`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `Rational(5,2)*x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `2*x + 3`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(0) = 0). | (2) aprovado: Gabarito confirmado (f(0) = 3). | (3) aprovado: Gabarito confirmado (crescente em Reals). | (4) aprovado: Gabarito confirmado (crescente em Reals).
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem definido, com dados numéricos completos, contexto plausível e pergunta objetiva sobre a natureza geométrica das retas. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido (traduzir leis algébricas em características geométricas e classificar proporcional vs. afim) é compatível com 'aplicar': o aluno usa procedimentos conhecidos (identificar a e b) em situação nova. A resposta é multiestrutural (dois aspectos por reta: intercepto e inclinação), o que é coerente com o nível 'aplicar' declarado, embora não exija análise comparativa mais profunda entre os dois modelos.
  - alinhamento_bncc: 5/5 — A questão exige efetivamente o trânsito entre representação algébrica (y=2,5x e y=2x+3) e representação geométrica (posição da reta, intercepto, inclinação), e obriga a distinguir o caso proporcional do caso afim, articulando os dois conceitos num único problema comparativo. Atende integralmente às exigências da habilidade.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: troca de atribuição entre empresas, generalização incorreta de que toda cobrança 'por km' é proporcional, e confusão entre o papel do coeficiente angular e do termo independente. Nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 4/5 — O contexto de aplicativos de transporte atualiza o clássico problema de tarifa (táxi), tornando-o mais significativo, e o enunciado não entrega pistas diretas sobre proporcionalidade/afinidade, evitando o efeito Topaze. Ainda assim, a estrutura do problema é próxima de exercícios tradicionais de comparação de planos tarifários.
