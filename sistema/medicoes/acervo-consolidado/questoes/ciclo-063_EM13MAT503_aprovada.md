# Ciclo 063 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma rede de lanchonetes possui duas filiais, A e B, que vendem o mesmo produto por preços que podem ser ajustados mensalmente. Os gestores modelaram o lucro mensal de cada filial (em milhares de reais) em função do preço de venda unitário $p$ (em reais) pelas funções:

$L_A(p) = -2p^2 + 80p - 600$

$L_B(p) = -3p^2 + 132p - 1200$

A diretoria da rede definiu uma meta: para que a linha de produto continue sendo vendida em uma filial, o lucro mensal máximo dessa filial deve ser de pelo menos 240 mil reais.

a) Determine o preço de venda que maximiza o lucro de cada filial e o valor do lucro máximo correspondente.

b) Qual filial alcança o maior lucro máximo?

c) Com base na meta estabelecida pela diretoria, verifique se cada filial deve continuar vendendo o produto. Justifique sua resposta com os valores calculados.

## Gabarito

Filial A: preço de R$ 20, lucro máximo de 200 mil reais (não atinge a meta). Filial B: preço de R$ 22, lucro máximo de 252 mil reais (atinge a meta). A Filial B tem o maior lucro máximo e é a única que deve continuar vendendo o produto.

## Resolução

**Passo 1 — Lucro máximo da Filial A**

A função $L_A(p) = -2p^2 + 80p - 600$ é uma parábola com concavidade para baixo ($a = -2 < 0$), logo possui ponto de **máximo** no vértice.

Coordenada $p$ do vértice: $p_A = -\dfrac{b}{2a} = -\dfrac{80}{2(-2)} = -\dfrac{80}{-4} = 20$

Lucro máximo: $L_A(20) = -2(20)^2 + 80(20) - 600 = -800 + 1600 - 600 = 200$

Logo, a Filial A tem lucro máximo de **200 mil reais**, obtido com preço de **R\$ 20**.

**Passo 2 — Lucro máximo da Filial B**

A função $L_B(p) = -3p^2 + 132p - 1200$ também tem concavidade para baixo ($a=-3<0$).

$p_B = -\dfrac{132}{2(-3)} = -\dfrac{132}{-6} = 22$

$L_B(22) = -3(22)^2 + 132(22) - 1200 = -3(484) + 2904 - 1200 = -1452 + 2904 - 1200 = 252$

Logo, a Filial B tem lucro máximo de **252 mil reais**, obtido com preço de **R\$ 22**.

**Passo 3 — Comparação entre as filiais**

Como $252 > 200$, a **Filial B** alcança o maior lucro máximo.

**Passo 4 — Verificação da meta da diretoria**

A meta exige lucro máximo de pelo menos 240 mil reais.

- Filial A: lucro máximo de 200 mil reais $< 240$ mil reais → **não atinge a meta**, devendo descontinuar o produto.
- Filial B: lucro máximo de 252 mil reais $\geq 240$ mil reais → **atinge a meta**, podendo continuar vendendo o produto.

## Formalização verificável

- `funcao` — expressão `-2*p**2 + 80*p - 600`, esperado `[20, 200]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-3*p**2 + 132*p - 1200`, esperado `[22, 252]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-2*p**2 + 80*p - 600`, esperado `200`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `-3*p**2 + 132*p - 1200`, esperado `252`, parâmetros `{'consulta': 'maximo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (4, 83)). | (2) aprovado: Gabarito confirmado (maximo de -5*t**2 + 40*t + 3 em Reals: 83).
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: apresenta a função horária da altura, define claramente as variáveis, especifica o domínio de validade e formula um pedido único e inequívoco (instante e valor da altura máxima). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido (identificar concavidade, calcular vértice via fórmula, substituir e calcular a ordenada) é compatível com 'aplicar' na taxonomia de Bloom, e a resposta esperada é multiestrutural (várias etapas conectadas, mas sem exigir relacionar múltiplos conceitos de forma integrada, o que seria 'relacional/analisar'). A exigência explícita de justificar sem gráfico eleva um pouco o nível, mas ainda é aplicação direta de fórmula, sem exigir real investigação ou interpretação de múltiplos cenários.
  - alinhamento_bncc: 4/5 — Cumpre os dois requisitos explícitos: pede o ponto de máximo de uma função quadrática e o contexto é de Cinemática (lançamento vertical). A exigência de 'justificativa baseada nas propriedades da função quadrática, sem gráfico' aproxima-se do espírito investigativo da habilidade EM13MAT503. Contudo, a tarefa se reduz a um algoritmo padrão (fórmula do vértice) aplicado sem exploração adicional do fenômeno físico (por exemplo, discutir por que a=-5 representa a metade da aceleração da gravidade, ou interpretar o significado físico do vértice), o que limita a profundidade investigativa pedida pela habilidade.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — O cenário de 'lançamento vertical com h(t) = -at²+bt+c' é um dos exemplos mais reproduzidos em livros didáticos brasileiros para introduzir vértice de parábola; não há elemento de contexto significativo (por exemplo, uma situação real motivadora, dados de um problema aplicado, ou uma pergunta que exija interpretação física do resultado). A estrutura segue o roteiro clássico de 'identifique a,b,c; calcule tv; calcule h(tv)', o que facilita respostas mecânicas e reduz o valor investigativo pretendido pela habilidade.
  - *sugestões:* Para aumentar a originalidade e reforçar o caráter investigativo exigido pela habilidade EM13MAT503, sugere-se: (1) inserir um contexto mais autêntico e específico, como um problema real de lançamento de foguete de brinquedo, bola em uma competição esportiva, ou situação de Matemática Financeira (ex.: lucro de uma empresa em função do tempo), evitando o modelo genérico e repetido de 'objeto lançado verticalmente'; (2) acrescentar uma pergunta adicional que exija interpretação do resultado no contexto (por exemplo, 'o objeto atinge alguma restrição de altura máxima permitida? Justifique') para elevar o nível cognitivo além da aplicação mecânica da fórmula do vértice; (3) variar os coeficientes ou a formulação para que o estudante não reconheça imediatamente o padrão 'a,b,c → fórmula do vértice', estimulando raciocínio mais analítico, como pedir para comparar duas situações (dois lançamentos com equações diferentes) e decidir qual atinge maior altura, articulando de fato investigação sobre máximos/mínimos em vez de cálculo isolado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para aumentar a originalidade e reforçar o caráter investigativo exigido pela habilidade EM13MAT503, sugere-se: (1) inserir um contexto mais autêntico e específico, como um problema real de lançamento de foguete de brinquedo, bola em uma competição esportiva, ou situação de Matemática Financeira (ex.: lucro de uma empresa em função do tempo), evitando o modelo genérico e repetido de 'objeto lançado verticalmente'; (2) acrescentar uma pergunta adicional que exija interpretação do resultado no contexto (por exemplo, 'o objeto atinge alguma restrição de altura máxima permitida? Justifique') para elevar o nível cognitivo além da aplicação mecânica da fórmula do vértice; (3) variar os coeficientes ou a formulação para que o estudante não reconheça imediatamente o padrão 'a,b,c → fórmula do vértice', estimulando raciocínio mais analítico, como pedir para comparar duas situações (dois lançamentos com equações diferentes) e decidir qual atinge maior altura, articulando de fato investigação sobre máximos/mínimos em vez de cálculo isolado.

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (20, 200)). | (2) aprovado: Gabarito confirmado (vértice calculado (22, 252)). | (3) aprovado: Gabarito confirmado (maximo de -2*p**2 + 80*p - 600 em Reals: 200). | (4) aprovado: Gabarito confirmado (maximo de -3*p**2 + 132*p - 1200 em Reals: 252).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
  - funcao/maximo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é preciso: define as duas funções, o que é pedido em cada item (preço e lucro máximo, comparação, decisão) e o critério da meta (≥240 mil). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver integralmente a questão.
  - adequacao_nivel: 4/5 — O processo cognitivo predominante é aplicar (uso da fórmula do vértice para duas funções), compatível com o nível declarado. O item (c), que exige justificar a decisão com base num critério numérico, se aproxima de um nível relacional (SOLO) e de avaliação (Bloom), o que é positivo e não prejudica a coerência — apenas extrapola levemente 'aplicar' puro, mas de forma benéfica à investigação pedida pela habilidade.
  - alinhamento_bncc: 5/5 — A habilidade EM13MAT503 pede investigação de ponto de máximo/mínimo em contexto de Matemática Financeira, não mera manipulação algébrica. A questão cumpre isso plenamente: calcula os vértices, compara os lucros máximos e usa esse resultado para uma decisão de negócio (meta da diretoria), articulando cálculo e interpretação em um único problema coeso, não apenas dois exercícios de vértice justapostos.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de 'lucro máximo em função do preço' é um clássico recorrente em livros didáticos de função quadrática, com estrutura previsível (vértice, comparação, meta). A adição de duas filiais e uma meta de decisão dá algum valor investigativo extra, mas o enunciado ainda segue um roteiro bastante convencional, sem elemento surpreendente ou dado supérfluo que exija discernimento real do aluno.
