# Ciclo 005 — EM13MAT302

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** criar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 2

## Enunciado

Uma pessoa comparou dois aplicativos de mototáxi usando cada um deles em meses diferentes, sempre para o mesmo tipo de deslocamento no trabalho. Em cada aplicativo, a fatura mensal é composta por uma tarifa fixa mais um valor constante por quilômetro total rodado no mês (isto é, o custo mensal é uma função afim da quilometragem mensal $x$, em km, com $0 \le x \le 150$). Os registros de fatura foram:

- MotoVá: em um mês, rodou 40 km e pagou R$ 62,00; em outro mês, rodou 100 km e pagou R$ 122,00.
- UrbanMoto: em um mês, rodou 40 km e pagou R$ 70,00; em outro mês, rodou 90 km e pagou R$ 100,00.

a) Determine a lei $c_A(x)$ que dá o custo mensal do MotoVá e a lei $c_B(x)$ que dá o custo mensal do UrbanMoto, em função da quilometragem mensal $x$.

b) Determine a quilometragem mensal para a qual os dois aplicativos cobram exatamente o mesmo valor, e qual é esse valor. Indique qual aplicativo é mais barato para quilometragens menores que esse valor e qual é mais barato para quilometragens maiores.

c) Um terceiro aplicativo, o RotaFácil, acaba de entrar no mercado, cobrando uma tarifa fixa de R$ 50,00 mais R$ 0,50 por quilômetro rodado no mês. Elabore uma única função $C(x)$, definida por partes para $0 \le x \le 150$, que forneça sempre o menor custo mensal possível entre os três aplicativos, para qualquer quilometragem mensal $x$ nesse intervalo (explicite os intervalos de $x$ de cada sentença). Em seguida, justifique com os cálculos por que o UrbanMoto não aparece em nenhuma sentença da função que você construiu, ou seja, mostre que ele nunca é a opção mais barata para nenhum valor de $x$ em $[0,150]$.

## Gabarito

c_A(x) = x + 22; c_B(x) = 0,6x + 46; equilíbrio A–B em x = 60 km (custo R$ 82,00), com MotoVá mais barato para x<60 e UrbanMoto mais barato para x>60. Com o RotaFácil, c_C(x) = 0,5x + 50, e a função de menor custo é C(x) = x+22 para 0≤x≤56 e C(x) = 0,5x+50 para 56<x≤150; o UrbanMoto nunca é a opção mais barata em [0,150].

## Resolução

**a) Construindo os modelos afins**

MotoVá: dois pontos $(40,62)$ e $(100,122)$.
$$a=\frac{122-62}{100-40}=\frac{60}{60}=1,\qquad b=62-1\cdot 40=22$$
$$c_A(x)=x+22$$

UrbanMoto: dois pontos $(40,70)$ e $(90,100)$.
$$a=\frac{100-70}{90-40}=\frac{30}{50}=\frac{3}{5}=0{,}6,\qquad b=70-0{,}6\cdot 40=46$$
$$c_B(x)=0{,}6x+46$$

**b) Ponto de equilíbrio entre MotoVá e UrbanMoto**

$$x+22=0{,}6x+46 \Rightarrow 0{,}4x=24 \Rightarrow x=60$$

Custo nesse ponto: $c_A(60)=60+22=82$ reais.

Como $c_A(0)=22<c_B(0)=46$, o MotoVá é mais barato para $x<60$; como as retas se cruzam apenas em $x=60$ e $c_B$ cresce mais devagar, para $x>60$ o UrbanMoto passa a ser mais barato (por exemplo, em $x=150$: $c_A=172$ e $c_B=136$).

**c) Incluindo o RotaFácil e construindo a função de menor custo**

Lei do RotaFácil: $c_C(x)=0{,}5x+50$.

Precisamos comparar as três retas duas a duas para descobrir, em cada faixa de $x$, qual delas é a menor.

*MotoVá × RotaFácil:*
$$x+22=0{,}5x+50 \Rightarrow 0{,}5x=28 \Rightarrow x=56,\ \text{custo }78$$

*UrbanMoto × RotaFácil:*
$$0{,}6x+46=0{,}5x+50 \Rightarrow 0{,}1x=4 \Rightarrow x=40,\ \text{custo }70$$

*MotoVá × UrbanMoto:* já obtido, $x=60$.

Agora testamos o custo das três funções em pontos representativos de cada intervalo delimitado pelos cruzamentos ($x=0,\,40,\,56,\,60,\,150$):

- $x=20$: $c_A=42,\ c_B=58,\ c_C=60$ → menor é $c_A$.
- $x=40$: $c_A=62,\ c_B=70,\ c_C=70$ → menor é $c_A$ (B e C empatam, mas A é menor que ambos).
- $x=50$: $c_A=72,\ c_B=76,\ c_C=75$ → menor é $c_A$.
- $x=56$: $c_A=78,\ c_B=79{,}6,\ c_C=78$ → menor é $c_A=c_C$.
- $x=58$: $c_A=80,\ c_B=80{,}8,\ c_C=79$ → menor é $c_C$.
- $x=100$: $c_A=122,\ c_B=106,\ c_C=100$ → menor é $c_C$.
- $x=150$: $c_A=172,\ c_B=136,\ c_C=125$ → menor é $c_C$.

Os testes mostram que o mínimo é sempre dado por $c_A$ ou por $c_C$, nunca por $c_B$. A troca entre eles ocorre exatamente no cruzamento de $c_A$ com $c_C$, em $x=56$ (o cruzamento de $c_B$ com $c_C$, em $x=40$, não chega a valer, pois nesse ponto $c_A$ já é menor que os dois). Logo:

$$C(x)=\begin{cases}x+22, & 0\le x\le 56\\[2mm] 0{,}5x+50, & 56< x\le 150\end{cases}$$

**Por que o UrbanMoto nunca é o mais barato:**

- Para $0\le x<60$, $c_A(x)<c_B(x)$ (pois só se cruzam em $x=60$ e em $x=0$ já vale $c_A<c_B$); logo, nessa faixa, $c_B$ nunca é menor que $c_A$.
- Para $x\ge 40$, $c_B(x)>c_C(x)$, pois a inclinação de $c_B$ (0,6) é maior que a de $c_C$ (0,5) e elas partem empatadas em $x=40$; logo, para todo $x\ge 40$, $c_B$ é sempre maior que $c_C$.
- Juntando as duas conclusões: para $x<60$ há sempre alguém mais barato que $c_B$ (o próprio $c_A$, já que $x<60<... $ cobre inclusive $0\le x<40$), e para $x\ge 40$ há sempre $c_C$ mais barato que $c_B$. Como esses dois intervalos cobrem todo $[0,150]$, em nenhum ponto o UrbanMoto é a opção de menor custo — no máximo empata com outra opção (em $x=40$, empata com $c_C$, mas $c_A$ ainda é menor que ambos).

Portanto, o UrbanMoto é sempre dominado por MotoVá ou por RotaFácil e não aparece na função $C(x)$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `x + 22`, parâmetros `{'pontos': '[(40,62),(100,122)]', 'grau': '1'}`
- `propriedade` — expressão `-`, esperado `3*x/5 + 46`, parâmetros `{'pontos': '[(40,70),(90,100)]', 'grau': '1'}`
- `equacao` — expressão `Eq(x + 22, 3*x/5 + 46)`, esperado `[60]`
- `funcao` — expressão `x + 22`, esperado `82`, parâmetros `{'consulta': 'valor', 'ponto': '60'}`
- `equacao` — expressão `Eq(x + 22, x/2 + 50)`, esperado `[56]`
- `funcao` — expressão `Piecewise((x + 22, x <= 56), (x/2 + 50, True))`, esperado `100`, parâmetros `{'consulta': 'valor', 'ponto': '100'}`
- `funcao` — expressão `Piecewise((x + 22, x <= 56), (x/2 + 50, True))`, esperado `Interval(0, 150)`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 2*x + 10: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem estruturado, dados suficientes (dois pares de valores para a MoveJá, taxa única para a RodaFácil) e pergunta claramente delimitada em dois itens. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O processo cognitivo real exigido é montar um sistema linear 2x2 (item a) e resolver uma inequação linear com arredondamento para inteiro (item b) — isso corresponde a 'aplicar' (talvez 'analisar' no SOLO relacional, ao comparar dois modelos), mas não a 'criar'. Não há produção de algo novo (elaboração de problema, síntese de critério original, generalização); o aluno apenas executa procedimentos-padrão de função afim. Há incompatibilidade entre o nível Bloom declarado e o que a tarefa de fato demanda.
  - alinhamento_bncc: 3/5 — A questão exige construir o modelo (não o entrega pronto) e articula dois modelos afins em um único problema de comparação, o que atende parcialmente à habilidade EM13MAT302. Contudo, a habilidade também prevê 'elaborar problemas', e a tarefa é puramente de resolução; além disso, o nível cognitivo declarado ('criar') não é operacionalizado no enunciado, o que é uma falha de alinhamento entre especificação e execução.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de aplicativos de transporte é atual e evita o clichê de 'planos de telefonia', mas a estrutura (duas tarifas, ponto de equilíbrio) ainda é um modelo clássico de função afim recontextualizado. Não há pistas que entreguem a solução (sem efeito Topaze), e o aluno precisa de fato montar o sistema.
  - *sugestões:* Ajustar a discrepância entre o nível Bloom declarado ('criar') e o que a questão de fato exige. Duas alternativas: (1) Rebaixar a especificação para 'aplicar' ou 'analisar', já que a tarefa atual (montar sistema linear e resolver inequação) é coerente com esses níveis; ou (2) Elevar a tarefa para exigir criação genuína, por exemplo: pedir que o aluno elabore ele mesmo um novo problema análogo (com outra empresa fictícia e outros dois pontos dados), proponha um critério de decisão para um usuário com padrão de uso variável (ex.: parte do mês roda pouco, parte roda muito) e construa uma função por partes ou uma regra de recomendação, justificando com base nos dois modelos. Isso exigiria síntese e produção de um artefato novo, alinhando-se a 'criar'. Também recomenda-se acrescentar explicitamente ao enunciado um pedido de elaboração (não apenas resolução), para atender de forma mais completa ao verbo 'elaborar' presente na habilidade EM13MAT302.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a discrepância entre o nível Bloom declarado ('criar') e o que a questão de fato exige. Duas alternativas: (1) Rebaixar a especificação para 'aplicar' ou 'analisar', já que a tarefa atual (montar sistema linear e resolver inequação) é coerente com esses níveis; ou (2) Elevar a tarefa para exigir criação genuína, por exemplo: pedir que o aluno elabore ele mesmo um novo problema análogo (com outra empresa fictícia e outros dois pontos dados), proponha um critério de decisão para um usuário com padrão de uso variável (ex.: parte do mês roda pouco, parte roda muito) e construa uma função por partes ou uma regra de recomendação, justificando com base nos dois modelos. Isso exigiria síntese e produção de um artefato novo, alinhando-se a 'criar'. Também recomenda-se acrescentar explicitamente ao enunciado um pedido de elaboração (não apenas resolução), para atender de forma mais completa ao verbo 'elaborar' presente na habilidade EM13MAT302.

### Iteração 2

- **Verificador:** aprovado_parcial — 6 de 7 afirmações conferidas; o restante não é formalizável. (1) aprovado: Propriedades confirmadas para x + 22: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Propriedades confirmadas para 3*x/5 + 46: reproduz os 2 pontos dados; grau 1. | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) aprovado: Gabarito confirmado (f(60) = 82). | (5) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (6) aprovado: Gabarito confirmado (f(100) = 100). | (7) nao_verificavel: Verificação inconclusiva: não foi possível determinar o domínio de Piecewise((x + 22, x <= 56), (x/2 + 50, True)). Conferir manualmente.
  - propriedade=aprovado
  - propriedade=aprovado
  - equacao=aprovado
  - funcao/valor=aprovado
  - equacao=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=nao_verificavel
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado especifica claramente o tipo de função (afim), o domínio de x, os dados (pares ponto-custo) e as três tarefas (a, b, c) com condições precisas. Não há ambiguidade lexical ou estrutural relevante; os dados são suficientes para resolver cada item sem suposições extras.
  - adequacao_nivel: 5/5 — Os itens a e b exigem aplicar/analisar (construir modelo a partir de pontos, comparar duas retas), preparando o terreno para o item c, que exige criar: construir uma nova função definida por partes a partir da comparação de três modelos e justificar por que uma opção nunca domina — resposta do tipo relacional/estendida na SOLO, coerente com o nível 'criar' declarado. Conteúdo compatível com Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão não entrega o modelo pronto: os coeficientes das funções afins precisam ser deduzidos a partir de pares (x, custo). O item c pede explicitamente 'elaborar' uma função por partes que combina os três modelos em um único problema articulado (não é apenas justapor itens independentes), atendendo integralmente a EM13MAT302.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de comparação de aplicativos de mototáxi renova o clássico 'problema das operadoras', e o uso de pares de pontos (em vez de fornecer tarifa fixa/variável diretamente) evita o efeito Topaze na etapa de modelagem. Ainda assim, a estrutura geral (duas retas + terceira opção + ponto de equilíbrio) é um padrão bastante recorrente em livros didáticos, o que limita um pouco a originalidade plena.
