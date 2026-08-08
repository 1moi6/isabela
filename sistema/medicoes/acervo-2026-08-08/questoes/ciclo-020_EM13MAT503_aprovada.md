# Ciclo 020 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Em um teste de calibração, dois drones decolam ao mesmo tempo e sobem verticalmente antes de iniciar a descida. As alturas atingidas pelos drones A e B, em metros, em função do tempo $t$ (em segundos) após a decolagem, são modeladas por:

$h_A(t) = -4t^2 + 20t + 2$

$h_B(t) = -2t^2 + 12t + 6$

O regulamento da área de testes estabelece que nenhum drone pode ultrapassar 26,5 m de altura sem autorização especial.

Qual das alternativas descreve corretamente qual drone atinge a maior altura durante o voo, o valor dessa altura máxima, e se esse valor ultrapassa o limite regulamentar?

## Alternativas

- (a) O Drone A atinge a maior altura, com máximo de 27 m, valor que ultrapassa o limite de 26,5 m.  ← correta
- (b) O Drone B atinge a maior altura, com máximo de 24 m, valor que não ultrapassa o limite de 26,5 m.
  - *erro representado:* Comparar apenas a altura inicial (termo independente c) de cada função — como o Drone B parte de 6 m contra 2 m do Drone A — e concluir erroneamente que ele também atinge a maior altura máxima, sem calcular o vértice de cada parábola.
- (c) O Drone A atinge a maior altura, mas seu máximo é de 26 m (verificado apenas nos instantes inteiros t = 1, 2 e 3 s), valor que não ultrapassa o limite de 26,5 m.
  - *erro representado:* Assumir que o instante de altura máxima deve ser um número inteiro de segundos, testando apenas t = 1, 2, 3, ... em vez de calcular o vértice da parábola pela fórmula t* = -b/(2a), que neste caso é t = 2,5 s.
- (d) O Drone B atinge a maior altura, com máximo de 6 m, valor que não ultrapassa o limite de 26,5 m.
  - *erro representado:* Aplicar a fórmula do vértice sem dividir por 2, usando t = -b/a em vez de t = -b/(2a): isso leva a calcular t = 5 s para o Drone A (h = 2 m) e t = 6 s para o Drone B (h = 6 m), fazendo o estudante concluir, de forma incorreta, que o Drone B teria a maior altura.

## Gabarito

Drone A; altura máxima de 27 m; ultrapassa o limite de 26,5 m.

## Resolução

**Passo 1 — Reconhecer que cada função é quadrática com concavidade para baixo**

Em $h_A(t) = -4t^2+20t+2$, o coeficiente de $t^2$ é $a=-4<0$, e em $h_B(t)=-2t^2+12t+6$, temos $a=-2<0$. Logo, ambas as trajetórias possuem um ponto de **máximo** (a altura sobe e depois desce).

**Passo 2 — Calcular o instante de altura máxima de cada drone**

O instante de máximo de uma parábola $at^2+bt+c$ ocorre em $t^* = -\dfrac{b}{2a}$.

Para o Drone A: $t^*_A = -\dfrac{20}{2(-4)} = -\dfrac{20}{-8} = 2{,}5\text{ s}$

Para o Drone B: $t^*_B = -\dfrac{12}{2(-2)} = -\dfrac{12}{-4} = 3\text{ s}$

**Passo 3 — Calcular a altura máxima de cada drone**

$h_A(2{,}5) = -4(2{,}5)^2 + 20(2{,}5) + 2 = -25 + 50 + 2 = 27\text{ m}$

$h_B(3) = -2(3)^2 + 12(3) + 6 = -18 + 36 + 6 = 24\text{ m}$

**Passo 4 — Comparar as alturas máximas**

Como $27\text{ m} > 24\text{ m}$, o **Drone A** atinge a maior altura durante o voo.

**Passo 5 — Verificar se essa altura ultrapassa o limite regulamentar**

Comparando com o limite de $26{,}5$ m: $27 > 26{,}5$, portanto a altura máxima do Drone A **ultrapassa** o limite regulamentar.

**Conclusão:** o Drone A atinge a maior altura, com máximo de $27$ m, valor que ultrapassa o limite de $26{,}5$ m.

## Formalização verificável

- `funcao` — expressão `-4*t**2 + 20*t + 2`, esperado `27`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `-2*t**2 + 12*t + 6`, esperado `24`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `-4*t**2 + 20*t + 2`, esperado `[5/2, 27]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (extremo calculado 23). | (2) aprovado: Gabarito confirmado (vértice calculado (2, 23)).
  - funcao/maximo=aprovado
  - funcao/vertice=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado objetivo, dados completos (a, b, c implícitos na função), pergunta única e sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — A tarefa exigida é puramente procedimental: aplicar a fórmula do vértice e substituir na função. Isso corresponde ao nível 'aplicar' de Bloom e a uma estrutura SOLO uniestrutural/multiestrutural (executar dois passos isolados), não ao nível 'analisar' declarado, que pressupõe decompor a situação, relacionar variáveis, justificar escolhas ou comparar alternativas. Não há elemento de investigação ou análise crítica no enunciado.
  - alinhamento_bncc: 3/5 — O contexto de Cinemática está presente e o cálculo do ponto de máximo é feito, atendendo parcialmente à habilidade. Porém a habilidade fala em 'investigar' pontos de máximo/mínimo, o que sugere explorar o significado físico do resultado, comparar cenários ou justificar o porquê do máximo — a questão apenas pede o cálculo direto, sem nenhuma camada investigativa além da aplicação de fórmula.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos plausíveis e distintos (confundir t com h(t), esquecer a constante c, usar fórmula incorreta do vértice), nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 3/5 — O contexto de 'projétil lançado verticalmente com h(t) = -5t²+20t+3' é um clássico recorrente em livros didáticos de função quadrática/cinemática, sem elemento diferenciador de contexto ou dado real que traga significância adicional.
  - *sugestões:* Elevar o nível cognitivo para corresponder a 'analisar': em vez de pedir apenas a altura máxima, peça, por exemplo, que o aluno determine o intervalo de tempo em que o projétil permanece acima de certa altura, compare duas trajetórias com parâmetros diferentes para decidir qual atinge maior altura, ou justifique por que o ponto obtido é máximo (e não mínimo) analisando o coeficiente 'a' e o domínio físico de t (t≥0). Isso força a decompor a situação e relacionar múltiplas informações, tornando a resposta genuinamente analítica (SOLO relacional). Também é recomendável variar o contexto ou os valores numéricos para reduzir a semelhança com o problema-tipo de livro didático, aumentando a originalidade.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Elevar o nível cognitivo para corresponder a 'analisar': em vez de pedir apenas a altura máxima, peça, por exemplo, que o aluno determine o intervalo de tempo em que o projétil permanece acima de certa altura, compare duas trajetórias com parâmetros diferentes para decidir qual atinge maior altura, ou justifique por que o ponto obtido é máximo (e não mínimo) analisando o coeficiente 'a' e o domínio físico de t (t≥0). Isso força a decompor a situação e relacionar múltiplas informações, tornando a resposta genuinamente analítica (SOLO relacional). Também é recomendável variar o contexto ou os valores numéricos para reduzir a semelhança com o problema-tipo de livro didático, aumentando a originalidade.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (extremo calculado 35). | (2) aprovado: Gabarito confirmado (vértice calculado (2, 35)). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/maximo=aprovado
  - funcao/vertice=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente os dados (função horária), o domínio (t≥0) e as três exigências (altura máxima/instante, justificativa com base no coeficiente, intervalo de tempo com h≥30). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — Embora rotulada como 'analisar', a tarefa efetiva é aplicar diretamente a fórmula do vértice (t=-b/2a), substituir valores e resolver uma inequação quadrática padrão — processos de aplicação/compreensão, não de análise (que exigiria comparar, decompor relações ou justificar sem depender de fórmula memorizada). Na taxonomia SOLO a resposta é multiestrutural: três subtarefas calculadas em paralelo e depois justapostas na alternativa, sem integração relacional que caracterizaria o nível 'analisar'.
  - alinhamento_bncc: 4/5 — A habilidade pede investigar ponto de máximo/mínimo em contexto de Cinemática, o que é atendido pelo contexto do projétil e pela justificativa baseada no sinal de 'a'. Contudo, a 'investigação' se reduz a aplicar uma fórmula memorizada, e o item adicional (intervalo com h≥30) é manipulação algébrica extra que não é o foco da habilidade, ampliando o escopo sem articulá-lo organicamente à investigação do vértice.
  - distratores: 5/5 — Cada distrator representa um erro sistemático plausível: (2) confundir vértice de parábola com mínimo universal e esquecer de inverter a desigualdade ao dividir por número negativo; (3) supor que atingir um valor acima do limiar garante que a condição vale em todo o domínio; (4) erro aritmético no discriminante. Nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 3/5 — O contexto de projétil lançado verticalmente com h(t)=-5t²+20t+15 é um clássico recorrente em livros didáticos de cinemática/função quadrática, sem elemento contextual significativo ou inesperado. O enunciado também guia bastante o caminho de resolução (menciona explicitamente 'com base no coeficiente de t²'), o que reduz a autonomia investigativa e aproxima do efeito Topaze.
  - *sugestões:* Para elevar o nível cognitivo a 'analisar' de fato: (1) Não peça diretamente 'determine a altura máxima e o instante' via fórmula pronta; em vez disso, apresente uma situação que exija comparar duas trajetórias (ex.: dois projéteis com equações diferentes) e pedir qual atinge maior altura e por quê, forçando o aluno a relacionar coeficientes sem se limitar a substituir em t=-b/2a. (2) Remova a pista explícita 'com base no coeficiente de t²' do enunciado — deixe o aluno decidir por si mesmo qual critério usar para justificar máximo/mínimo, avaliando se ele reconhece a relação a<0 ⇒ máximo sem ser guiado. (3) Integre a parte da inequação (intervalo h≥30) de forma que dependa da conclusão sobre o vértice (por exemplo, pedir para o aluno primeiro decidir se existe algum instante em que a altura ultrapassa 30 m, usando o valor máximo já encontrado, antes de resolver a desigualdade), tornando as subtarefas relacionadas e não apenas justapostas. (4) Escolha um contexto menos repetido dos livros didáticos (ex.: altura de um drone, lançamento de bola em um jogo específico, dado de um experimento com números não redondos) para aumentar a originalidade e reduzir o efeito Topaze.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para elevar o nível cognitivo a 'analisar' de fato: (1) Não peça diretamente 'determine a altura máxima e o instante' via fórmula pronta; em vez disso, apresente uma situação que exija comparar duas trajetórias (ex.: dois projéteis com equações diferentes) e pedir qual atinge maior altura e por quê, forçando o aluno a relacionar coeficientes sem se limitar a substituir em t=-b/2a. (2) Remova a pista explícita 'com base no coeficiente de t²' do enunciado — deixe o aluno decidir por si mesmo qual critério usar para justificar máximo/mínimo, avaliando se ele reconhece a relação a<0 ⇒ máximo sem ser guiado. (3) Integre a parte da inequação (intervalo h≥30) de forma que dependa da conclusão sobre o vértice (por exemplo, pedir para o aluno primeiro decidir se existe algum instante em que a altura ultrapassa 30 m, usando o valor máximo já encontrado, antes de resolver a desigualdade), tornando as subtarefas relacionadas e não apenas justapostas. (4) Escolha um contexto menos repetido dos livros didáticos (ex.: altura de um drone, lançamento de bola em um jogo específico, dado de um experimento com números não redondos) para aumentar a originalidade e reduzir o efeito Topaze.

### Iteração 3

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (extremo calculado 27). | (2) aprovado: Gabarito confirmado (extremo calculado 24). | (3) aprovado: Gabarito confirmado (vértice calculado (5/2, 27)).
  - funcao/maximo=aprovado
  - funcao/maximo=aprovado
  - funcao/vertice=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente as duas funções, o contexto (drones, calibração) e a pergunta (qual drone atinge maior altura, qual o valor e se excede o limite). Não há ambiguidade lexical ou estrutural, e os dados (funções, limite regulamentar) são completos e suficientes para resolver o problema sem informações implícitas.
  - adequacao_nivel: 4/5 — A tarefa exige mais que aplicar a fórmula do vértice: o aluno precisa calcular o máximo de duas funções distintas, compará-las entre si e depois compará-las com um critério externo (o limite regulamentar), integrando três resultados numa única conclusão. Isso corresponde a um processo relacional (SOLO) compatível com 'analisar'. Poderia ser ainda mais analítico se exigisse justificar por que a concavidade garante um máximo, mas o nível está adequado ao Ensino Médio e à dificuldade declarada como fácil.
  - alinhamento_bncc: 4/5 — A questão pede efetivamente o ponto de máximo de funções quadráticas (não apenas manipulação algébrica isolada), inserido em uma situação-problema com contexto de movimento (altura em função do tempo), compatível com cinemática. A investigação em situação é respeitada, pois o aluno precisa decidir qual função modela o comportamento relevante e comparar com um critério regulamentar real. Não é um contexto puramente físico-cinemático clássico (sem gravidade explícita), mas está dentro do espectro aceito pela habilidade ('entre outros').
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: (B) confundir altura inicial com altura máxima; (C) supor que o instante de máximo deve ser inteiro; (D) aplicar a fórmula do vértice sem dividir por 2. Nenhum é absurdo ou trivialmente eliminável, e cada um corresponde a uma falha conceitual real e comum entre estudantes.
  - originalidade: 4/5 — O uso de drones como contexto foge do clichê da bola lançada verticalmente, trazendo um cenário mais atual e significativo. O enunciado não entrega pistas que resolvam o problema por eliminação (efeito Topaze), exigindo de fato o cálculo do vértice. Poderia ganhar um pouco mais em autenticidade explicando por que a altura seguiria um modelo quadrático (ex.: fase de subida controlada), mas isso não compromete a qualidade da questão.
