# Ciclo 028 — EM13MAT402

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_quadratica
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Considere a família de funções quadráticas $f(x) = (k-4)x^2 + (k-2)x$, definida para todo $k$ real com $k \neq 4$ (garantindo que $f$ seja de fato uma função quadrática). Cada valor de $k$ determina uma parábola diferente no plano cartesiano. Sabe-se que $y$ é diretamente proporcional a $x^2$ quando a lei da função tem a forma $y = c\cdot x^2$, sem termos de grau menor que 2. Determine o único valor de $k$ para o qual o gráfico de $f$ é uma parábola cujo vértice coincide com a origem do sistema de coordenadas, isto é, o valor de $k$ para o qual $y$ é diretamente proporcional a $x^2$.

## Alternativas

- (a) $k = 2$, pois nesse caso a lei se reduz a $f(x) = -2x^2$, cujo gráfico é uma parábola com vértice na origem, caracterizando $y$ como diretamente proporcional a $x^2$.  ← correta
- (b) Qualquer valor de $k \neq 4$, pois $f(0) = 0$ para todo $k$ e, portanto, o gráfico sempre passa pela origem.
  - *erro representado:* Confundir o fato de o gráfico passar pela origem (uma raiz da função) com o vértice da parábola estar localizado na origem.
- (c) $k = 4$, pois esse é o valor que anularia o coeficiente do termo quadrático, fazendo a parábola coincidir com a origem.
  - *erro representado:* Igualar o coeficiente líder a zero (condição que, na verdade, descaracterizaria a função como quadrática), confundindo-a com a condição de vértice na origem.
- (d) Não existe valor de $k$ para o qual isso ocorra, já que a restrição $k \neq 4$ impede que o termo linear $(k-2)x$ se anule.
  - *erro representado:* Concluir erroneamente que as restrições $k \neq 4$ e $k-2=0$ são incompatíveis, sem perceber que $k=2$ satisfaz simultaneamente ambas as condições.

## Gabarito

k = 2

## Resolução

**Passo 1 — Observar o que é comum a toda a família.**

Como não há termo constante, $f(0) = (k-4)\cdot 0 + (k-2)\cdot 0 = 0$ para **todo** $k$. Ou seja, todas as parábolas dessa família passam pela origem — mas isso não significa que a origem seja o **vértice** de cada uma delas.

**Passo 2 — Calcular a coordenada $x$ do vértice em função de $k$.**

Com $a = k-4$, $b = k-2$ e $c=0$:
$$x_v = -\frac{b}{2a} = -\frac{k-2}{2(k-4)}.$$

**Passo 3 — Impor que o vértice esteja na origem.**

Como $f(0)=0$ sempre, basta impor $x_v = 0$ (o valor de $y_v$ já será $0$ automaticamente). Isso ocorre se, e somente se, o numerador se anula (o denominador é não nulo, pois $k\neq4$):
$$k - 2 = 0 \;\Rightarrow\; k = 2.$$

**Passo 4 — Verificar a lei da função nesse valor.**

Para $k=2$: $a = 2-4=-2 \neq 0$ (função quadrática válida) e $b = 2-2=0$. Logo:
$$f(x) = -2x^2,$$
que é exatamente da forma $y=c\cdot x^2$: uma parábola com vértice em $(0,0)$, representando $y$ diretamente proporcional a $x^2$.

**Passo 5 — Contraexemplo para reforçar a distinção.**

Para $k=0$, por exemplo, $f(x) = -4x^2 - 2x$. Aqui $x_v = -\frac{-2}{2(-4)} = -\frac{1}{4} \neq 0$: o gráfico passa pela origem (pois $f(0)=0$), mas o vértice está em $x=-\tfrac14$, fora da origem. Logo essa parábola **não** representa proporcionalidade direta entre $y$ e $x^2$, mesmo cruzando a origem.

**Conclusão:** o único valor que faz o vértice coincidir com a origem — e portanto caracteriza $y$ como diretamente proporcional a $x^2$ — é $k=2$.

## Formalização verificável

- `equacao` — expressão `Eq(k - 2, 0)`, esperado `[2]`
- `funcao` — expressão `-2*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (0, -10/3)). | (3) aprovado: Gabarito confirmado (vértice calculado (1, 0)). | (4) aprovado: Gabarito confirmado (vértice calculado (2, -8)). | (5) aprovado: Propriedades confirmadas para 3*x**2: reproduz os 1 pontos dados; forma a*x**2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta com precisão os dados geométricos de cada parábola (eixo de simetria, vértice, pontos de passagem) e a pergunta é unívoca: identificar qual delas é da forma y=kx². Não há ambiguidade lexical nem lacunas de dados.
  - adequacao_nivel: 3/5 — O processo cognitivo real exigido — calcular o coeficiente 'a' em cada caso a partir de dados geométricos, verificar simultaneamente duas condições algébricas (b=0 e c=0) e comparar quatro situações — corresponde a 'aplicar' e até 'analisar' na taxonomia de Bloom, e a uma estrutura relacional/estendida abstrata na SOLO. Isso extrapola o nível 'entender' declarado, que sugeriria apenas reconhecer ou explicar a condição de proporcionalidade, não deduzi-la e testá-la algebricamente em quatro casos com literal resolução de sistemas.
  - alinhamento_bncc: 5/5 — A questão cumpre plenamente as exigências: exige trânsito genuíno entre representação geométrica (vértice, eixo de simetria, pontos) e representação algébrica (obtenção de f(x)=ax²+bx+c e verificação de b=0, c=0), e força a distinção entre casos de proporcionalidade direta (y=kx²) e casos que apenas parecem satisfazê-la (simetria em relação a Oy sem vértice na origem, ou passagem pela origem sem vértice ali). Os quatro casos são articulados em um único julgamento comparativo, não justapostos como itens independentes.
  - distratores: 5/5 — Cada alternativa incorreta corresponde a um erro conceitual plausível e documentado (confundir simetria em Oy com proporcionalidade, confundir vértice em Ox com vértice na origem, confundir passar pela origem com ter vértice na origem). Nenhum distrator é trivialmente eliminável por inspeção superficial.
  - originalidade: 4/5 — A estrutura de comparar quatro parábolas definidas puramente por dados geométricos foge do exercício padrão de livro didático (que tipicamente pede para identificar a lei de formação a partir do gráfico único). O enunciado não entrega pistas que pavimentem a resposta, exigindo verificação ativa das duas condições em cada caso; falta apenas um contexto aplicado/significativo, mas isso é aceitável dado o caráter teórico declarado.
  - *sugestões:* Ajustar a declaração de nível cognitivo de Bloom para 'aplicar' ou 'analisar' (mais coerente com o esforço de dedução de duas condições algébricas simultâneas e comparação entre quatro estruturas), OU, alternativamente, se o professor deseja manter 'entender', simplificar a tarefa para que o aluno apenas reconheça verbalmente/graficamente qual parábola satisfaz vértice na origem e eixo Oy como simetria, sem exigir o cálculo algébrico completo de 'a' em cada uma das quatro parábolas. Recomenda-se optar pela primeira alternativa, pois a riqueza da questão (cálculo + comparação + distinção conceitual) já está bem construída e alinhada à habilidade BNCC; apenas a rotulagem do nível Bloom precisa refletir essa exigência real.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a declaração de nível cognitivo de Bloom para 'aplicar' ou 'analisar' (mais coerente com o esforço de dedução de duas condições algébricas simultâneas e comparação entre quatro estruturas), OU, alternativamente, se o professor deseja manter 'entender', simplificar a tarefa para que o aluno apenas reconheça verbalmente/graficamente qual parábola satisfaz vértice na origem e eixo Oy como simetria, sem exigir o cálculo algébrico completo de 'a' em cada uma das quatro parábolas. Recomenda-se optar pela primeira alternativa, pois a riqueza da questão (cálculo + comparação + distinção conceitual) já está bem construída e alinhada à habilidade BNCC; apenas a rotulagem do nível Bloom precisa refletir essa exigência real.

### Iteração 2

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (4) rejeitado: Propriedade não confirmada: a expressão -5*x**2 tem grau 0, e não 2.
  - equacao=aprovado
  - equacao=aprovado
  - funcao/vertice=aprovado
  - propriedade=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (4) rejeitado: Propriedade não confirmada: a expressão -5*x**2 tem grau 0, e não 2. Resultado calculado independentemente: [1] | [1] | vértice calculado (0, 0) | a expressão -5*x**2 tem grau 0, e não 2. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (vértice calculado (0, 0)).
  - equacao=aprovado
  - funcao/vertice=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é bem redigido, com dados completos (restrição k≠4, definição explícita de proporcionalidade direta). Há uma leve redundância entre 'vértice coincide com a origem' e 'y diretamente proporcional a x²', mas não gera ambiguidade – apenas repete a mesma condição de duas formas.
  - adequacao_nivel: 3/5 — O nível declarado é 'entender', mas a tarefa efetivamente exigida é 'aplicar' (derivar a fórmula do vértice, resolver uma equação em k, verificar consistência com a restrição k≠4). A estrutura de resposta é relacional/multiestrutural, compatível com um nível cognitivo mais elevado que a simples compreensão conceitual. O conteúdo é adequado ao Ensino Médio, mas o verbo de comando ('determine') e o processo cognitivo não se alinham perfeitamente ao rótulo 'entender'.
  - alinhamento_bncc: 2/5 — A especificação é explícita: 'pedir apenas raízes ou o vértice em forma numérica NÃO realiza esta habilidade'. Na prática, a questão se resume a calcular x_v = -(k-2)/[2(k-4)] e igualá-lo a zero — ou seja, exatamente calcular o vértice em forma numérica (parametrizado por k), sem exigir qualquer trânsito efetivo para a representação geométrica (não há esboço, leitura de gráfico, comparação de curvas ou uso de representação visual). A menção à proporcionalidade direta é apenas conceitual/textual, embutida no enunciado e na resolução, mas não é o aluno que precisa 'converter' entre representações — a conversão já está dada pelo enunciado ('y diretamente proporcional a x² quando y=cx²'). Portanto a habilidade EM13MAT402, que pede a construção dessa distinção pelo próprio estudante a partir de trânsito algébrico-geométrico, não é plenamente exercitada.
  - distratores: 3/5 — Os distratores 2 e 4 representam erros conceituais plausíveis (confundir raiz com vértice; julgar incompatíveis as restrições k≠4 e k=2). Porém o distrator 3 (k=4) é fragilizado por ser explicitamente proibido pelo próprio enunciado ('k≠4'), tornando-o quase trivialmente eliminável por qualquer aluno que releia a condição inicial, reduzindo seu poder diagnóstico.
  - originalidade: 4/5 — A ideia de trabalhar com uma família de parábolas parametrizada por k e usar um contraexemplo (k=0) na resolução para reforçar a distinção entre 'passar pela origem' e 'ter vértice na origem' é interessante e vai além do exercício padrão de livro didático. Não há contexto aplicado, mas para uma questão teórica isso é aceitável; não há pistas que entreguem a solução (não há efeito Topaze evidente).
  - *sugestões:* 1) Para atender de fato à habilidade EM13MAT402, inclua uma etapa que exija transitar entre representações: por exemplo, apresente (ou peça para o aluno esboçar/comparar) os gráficos de duas ou três parábolas da família para valores distintos de k, pedindo que ele identifique visualmente qual delas tem vértice na origem e justifique algebricamente. Alternativamente, peça que o aluno reconheça, a partir do gráfico dado (sem fórmula), se a relação y-x² é de proporcionalidade direta, e só depois obtenha k algebricamente. 2) Ajuste o verbo de comando e a tarefa para o nível 'entender': em vez de 'determine o único valor de k' (que é 'aplicar/calcular'), peça para o aluno 'explique/justifique por que apenas um valor de k' produz essa condição, ou peça que classifique cada membro da família (proporcional/não proporcional) dado um pequeno conjunto de valores de k, exigindo comparação e não apenas resolução de equação. 3) Substitua o distrator k=4 por um erro mais sutil, coerente com o cálculo do vértice — por exemplo, um valor de k que resulte de inverter a fórmula do vértice (trocar b/2a por a/2b) ou de igualar o coeficiente linear ao termo constante, mantendo-o dentro do domínio válido (k≠4), para que não seja eliminável apenas pela leitura da restrição inicial.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Para atender de fato à habilidade EM13MAT402, inclua uma etapa que exija transitar entre representações: por exemplo, apresente (ou peça para o aluno esboçar/comparar) os gráficos de duas ou três parábolas da família para valores distintos de k, pedindo que ele identifique visualmente qual delas tem vértice na origem e justifique algebricamente. Alternativamente, peça que o aluno reconheça, a partir do gráfico dado (sem fórmula), se a relação y-x² é de proporcionalidade direta, e só depois obtenha k algebricamente. 2) Ajuste o verbo de comando e a tarefa para o nível 'entender': em vez de 'determine o único valor de k' (que é 'aplicar/calcular'), peça para o aluno 'explique/justifique por que apenas um valor de k' produz essa condição, ou peça que classifique cada membro da família (proporcional/não proporcional) dado um pequeno conjunto de valores de k, exigindo comparação e não apenas resolução de equação. 3) Substitua o distrator k=4 por um erro mais sutil, coerente com o cálculo do vértice — por exemplo, um valor de k que resulte de inverter a fórmula do vértice (trocar b/2a por a/2b) ou de igualar o coeficiente linear ao termo constante, mantendo-o dentro do domínio válido (k≠4), para que não seja eliminável apenas pela leitura da restrição inicial.
