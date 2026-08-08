# Ciclo 060 — EM13MAT402

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_quadratica
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Uma equipe de engenharia está testando dois protótipos no mesmo dia.

**Protótipo A** — um carrinho de testes que acelera em uma pista reta. A energia cinética $E$ (em joules) desenvolvida pelo carrinho, em função da velocidade $v$ (em m/s, com $v \ge 0$), é dada por:
$$E(v) = 2v^2$$

**Protótipo B** — um sistema de lançamento vertical que arremessa uma esfera de teste. A altura $h$ (em metros) da esfera acima do solo, em função do tempo $t$ (em segundos, desde o lançamento até tocar o solo), é dada por:
$$h(t) = -5t^2 + 20t$$

**a)** Para cada protótipo, determine as coordenadas do vértice, as raízes (quando existirem), a concavidade da parábola e o eixo de simetria. Em seguida, esboce, em dois planos cartesianos separados, o gráfico de $E$ em função de $v$ e o gráfico de $h$ em função de $t$, indicando nesses esboços os elementos calculados e respeitando o domínio de cada situação (velocidades e tempos não podem ser negativos, e o lançamento termina quando a esfera toca o solo).

**b)** Comparando os dois gráficos obtidos, identifique qual das duas grandezas — $E$ em função de $v$, ou $h$ em função de $t$ — é diretamente proporcional ao quadrado da sua variável independente. Justifique sua resposta descrevendo o que você observa nos gráficos (posição das parábolas em relação aos eixos, formato, presença ou não de determinados termos na curva) que permite fazer essa distinção, sem se basear apenas em olhar a fórmula.

## Gabarito

Protótipo A — $E(v)=2v^2$: vértice $(0,0)$, raiz dupla $v=0$, concavidade para cima, eixo de simetria $v=0$, domínio $[0,+\infty)$, imagem $[0,+\infty)$. Protótipo B — $h(t)=-5t^2+20t$: vértice $(2,20)$, raízes $t=0$ e $t=4$, concavidade para baixo, eixo de simetria $t=2$, domínio $[0,4]$, imagem $[0,20]$. Apenas $E(v)=2v^2$ é diretamente proporcional ao quadrado de $v$, o que se identifica no gráfico pelo vértice estar na origem e pela parábola não cruzar o eixo horizontal em outro ponto além dele; o gráfico de $h(t)$ tem vértice fora da origem e corta o eixo horizontal em dois pontos, evidenciando o termo linear.

## Resolução

**Passo 1 — Protótipo A: $E(v) = 2v^2$**

- Coeficientes: $a=2$, $b=0$, $c=0$. Como $a>0$, a concavidade é **para cima**.
- Vértice: $v_v = -\dfrac{b}{2a} = 0$, $E(0)=0$. Vértice em $(0,0)$.
- Raízes: $2v^2=0 \Rightarrow v=0$ (raiz dupla).
- Eixo de simetria: reta $v=0$.
- Domínio físico: $v\ge 0$, ou seja $[0,+\infty)$. Nesse domínio, $E$ também varia em $[0,+\infty)$.
- O esboço é o **ramo direito** de uma parábola que nasce exatamente na origem $(0,0)$ e sobe cada vez mais rapidamente, sem nenhum deslocamento horizontal ou vertical.

**Passo 2 — Protótipo B: $h(t) = -5t^2+20t$**

- Coeficientes: $a=-5$, $b=20$, $c=0$. Como $a<0$, a concavidade é **para baixo**.
- Vértice: $t_v = -\dfrac{20}{2(-5)} = 2$; $h(2) = -5(4)+20(2) = -20+40 = 20$. Vértice em $(2,20)$.
- Raízes: $h(t)=t(-5t+20)=0 \Rightarrow t=0$ ou $t=4$.
- Eixo de simetria: reta $t=2$.
- Domínio físico: do lançamento ($t=0$) até tocar o solo ($t=4$), ou seja $[0,4]$. Nesse intervalo, $h$ varia entre o mínimo nos extremos ($h=0$) e o máximo no vértice ($h=20$), logo a imagem é $[0,20]$.
- O esboço é um **arco completo** de parábola, começando em $(0,0)$, subindo até o pico $(2,20)$ e descendo simetricamente até $(4,0)$ — a curva **não nasce colada ao eixo vertical** no sentido de crescer a partir da origem como potência pura: ela sobe, atinge um máximo e desce, cruzando o eixo horizontal em dois pontos distintos.

**Passo 3 — Comparando os gráficos (item b)**

Observando os dois esboços:

- O gráfico de $E(v)=2v^2$ é uma parábola cujo vértice coincide com a origem $(0,0)$, é simétrica em relação ao próprio eixo vertical ($v=0$) e não tangencia nem cruza o eixo horizontal em nenhum outro ponto além da origem — ela só "abre" a partir dali. Esse formato (parábola com vértice na origem, um único ramo crescendo a partir de $(0,0)$ dentro do domínio físico) é exatamente o que ocorre quando uma grandeza é diretamente proporcional ao quadrado da outra: dobrando $v$, o ponto correspondente do gráfico salta para 4 vezes a altura, sempre partindo do mesmo ponto de origem.

- Já o gráfico de $h(t)$ tem vértice deslocado para fora da origem, em $(2,20)$, e a curva cruza o eixo horizontal em **dois** pontos ($t=0$ e $t=4$), formando um arco simétrico em torno de $t=2$ (e não em torno do eixo vertical $t=0$). Esse formato — parábola com eixo de simetria deslocado e vértice fora da origem — indica a presença do termo linear ($20t$), que "desloca" a curva e impede que $h$ cresça apenas em razão do quadrado de $t$: não existe uma constante $k$ tal que $h=kt^2$ para todo $t$ do domínio.

**Conclusão:** apenas o Protótipo A, com $E(v)=2v^2$, representa uma grandeza diretamente proporcional ao quadrado da variável independente. Isso se reconhece geometricamente pelo vértice da parábola coincidir com a origem do plano cartesiano e por a curva não cruzar o eixo horizontal em nenhum outro ponto — diferentemente do arco de $h(t)$, cujo vértice está fora da origem e cujo gráfico corta o eixo horizontal em dois pontos distintos.

## Formalização verificável

- `funcao` — expressão `2*v**2`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `2*v**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `2*v**2`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2*v**2`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`
- `funcao` — expressão `-5*t**2 + 20*t`, esperado `[0, 4]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `-5*t**2 + 20*t`, esperado `[2, 20]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-5*t**2 + 20*t`, esperado `Interval(0, 4)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `-5*t**2 + 20*t`, esperado `Interval(0, 20)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, 4)'}`
- `propriedade` — expressão `-`, esperado `2*v**2`, parâmetros `{'pontos': '[(1,2),(2,8),(3,18)]', 'forma': 'a*v**2', 'grau': '2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (4, 4)). | (3) rejeitado: Divergência: zeros da função calculados: [4 - 2*I, 4 + 2*I]; gabarito: []. | (4) aprovado: Gabarito confirmado (f(0) = 20).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/zeros=rejeitado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (4, 4)). | (3) rejeitado: Divergência: zeros da função calculados: [4 - 2*I, 4 + 2*I]; gabarito: []. | (4) aprovado: Gabarito confirmado (f(0) = 20). Resultado calculado independentemente: vértice calculado (0, 0) | vértice calculado (4, 4) | zeros da função calculados: [4 - 2*I, 4 + 2*I] | f(0) = 20. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (zeros da função: [0]). | (3) aprovado: Gabarito confirmado (vértice calculado (3, -1)). | (4) aprovado: Gabarito confirmado (zeros da função: [2, 4]). | (5) aprovado: Propriedades confirmadas para 2*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - funcao/vertice=aprovado
  - funcao/zeros=aprovado
  - funcao/vertice=aprovado
  - funcao/zeros=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é bem escrito e os dados de cada função estão completos. Há, porém, uma inconsistência terminológica: os itens (a) e (b) produzem apenas números (coordenadas do vértice, raízes), mas o item (c) os chama de 'representações gráficas obtidas nos itens (a) e (b)', quando nenhuma representação gráfica de fato foi construída ou fornecida.
  - adequacao_nivel: 2/5 — O nível declarado é 'entender', mas os itens (a) e (b) exigem apenas execução de procedimentos algorítmicos (fórmula do vértice, fatoração/Bhaskara) — nível 'aplicar' na taxonomia de Bloom, resposta multiestrutural em SOLO. O item (c) já exige comparação e justificativa, aproximando-se de 'analisar' (relacional). Há descompasso entre o nível cognitivo declarado e o que a questão realmente demanda, com desequilíbrio grande entre os itens.
  - alinhamento_bncc: 2/5 — A especificação exige explicitamente que a questão promova trânsito entre a forma algébrica e a representação geométrica no plano cartesiano, e adverte que pedir apenas raízes/vértice numéricos NÃO cumpre a habilidade. É exatamente o que ocorre aqui: os itens (a) e (b) só pedem valores numéricos, sem exigir esboço de gráfico, leitura de plano cartesiano ou uso de software/representação visual. O item (c) tenta compensar isso mencionando 'representações gráficas', mas essas nunca foram de fato construídas pelo aluno — a conversão geométrica é apenas nomeada, não realizada.
  - distratores: 5/5 — Não se aplica (questão discursiva, sem alternativas).
  - originalidade: 2/5 — O contexto (terreno ampliado, custo de produção) é um recorte comum de livros didáticos e as duas situações não se articulam de fato — são dois problemas de função quadrática justapostos, unidos apenas na conclusão. Além disso, o item (c) já entrega no próprio enunciado o critério de resposta ('vértice na origem', 'formato do gráfico'), configurando efeito Topaze: o aluno é guiado a repetir a definição sem precisar descobri-la por si.
  - *sugestões:* 1) Reformule os itens (a) e (b) para exigir efetivamente a construção/leitura de uma representação geométrica: peça que o aluno esboce cada parábola no plano cartesiano (indicando vértice, raízes, concavidade e eixo de simetria) ou forneça um gráfico e peça que o aluno identifique nele os elementos algébricos — não apenas calcule números. 2) Ajuste o nível de Bloom: se a intenção é 'entender/analisar', peça que o aluno compare os dois gráficos e infira, a partir do formato (parábola passando ou não pela origem, com ou sem termo linear), qual representa proporcionalidade direta ao quadrado, sem fornecer previamente os critérios ('posição do vértice e formato do gráfico') no enunciado — deixe o aluno descobrir esse critério. 3) Integre melhor os dois contextos (por exemplo, apresentando ambos como decisões do mesmo projeto de engenharia, com uma pergunta final que dependa da comparação real entre as duas grandezas, não apenas de dois blocos de cálculo independentes). 4) Considere trocar o contexto por algo menos padronizado, evitando o clichê 'terreno quadrado ampliado' e 'custo de produção', e usar um cenário onde a proporcionalidade direta ao quadrado tenha significado físico real (ex.: energia cinética, área de painel solar) para reforçar a aplicação da habilidade.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reformule os itens (a) e (b) para exigir efetivamente a construção/leitura de uma representação geométrica: peça que o aluno esboce cada parábola no plano cartesiano (indicando vértice, raízes, concavidade e eixo de simetria) ou forneça um gráfico e peça que o aluno identifique nele os elementos algébricos — não apenas calcule números. 2) Ajuste o nível de Bloom: se a intenção é 'entender/analisar', peça que o aluno compare os dois gráficos e infira, a partir do formato (parábola passando ou não pela origem, com ou sem termo linear), qual representa proporcionalidade direta ao quadrado, sem fornecer previamente os critérios ('posição do vértice e formato do gráfico') no enunciado — deixe o aluno descobrir esse critério. 3) Integre melhor os dois contextos (por exemplo, apresentando ambos como decisões do mesmo projeto de engenharia, com uma pergunta final que dependa da comparação real entre as duas grandezas, não apenas de dois blocos de cálculo independentes). 4) Considere trocar o contexto por algo menos padronizado, evitando o clichê 'terreno quadrado ampliado' e 'custo de produção', e usar um cenário onde a proporcionalidade direta ao quadrado tenha significado físico real (ex.: energia cinética, área de painel solar) para reforçar a aplicação da habilidade.

### Iteração 3

- **Verificador:** aprovado — Todas as 9 afirmações conferidas. (1) aprovado: Gabarito confirmado (zeros da função: [0]). | (2) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (3) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (4) aprovado: Gabarito confirmado (imagem de 2*v**2: Interval(0, oo)). | (5) aprovado: Gabarito confirmado (zeros da função: [0, 4]). | (6) aprovado: Gabarito confirmado (vértice calculado (2, 20)). | (7) aprovado: Gabarito confirmado (domínio Interval(0, 4) — restrição de contexto dentro do domínio máximo Reals). | (8) aprovado: Gabarito confirmado (imagem de -5*t**2 + 20*t: Interval(0, 20)). | (9) aprovado: Propriedades confirmadas para 2*v**2: reproduz os 3 pontos dados; grau 2; forma a*v**2.
  - funcao/zeros=aprovado
  - funcao/vertice=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/zeros=aprovado
  - funcao/vertice=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado longo mas sem ambiguidade: dados, domínios físicos e o que se pede em (a) e (b) estão explicitados com precisão (unidades, restrições de v e t, forma de apresentação exigida em dois planos separados).
  - adequacao_nivel: 2/5 — A especificação declara Bloom 'entender', mas o item (b) exige comparar dois gráficos, integrar vértice/raízes/formato para justificar uma distinção conceitual sem recorrer à fórmula — isso é claramente 'analisar' (SOLO relacional), não mera compreensão. Há incoerência entre o nível cognitivo declarado e o processo efetivamente demandado pela questão.
  - alinhamento_bncc: 5/5 — Cumpre as duas exigências específicas: exige trânsito algébrico→geométrico (vértice, raízes, eixo, concavidade traduzidos em esboço com domínio restrito) e força a distinção do caso de proporcionalidade direta ao quadrado via leitura geométrica (posição do vértice, interseções com eixo), não apenas por inspeção da fórmula. Os dois protótipos estão articulados num único problema comparativo, não justapostos.
  - distratores: 5/5 — não se aplica
  - originalidade: 4/5 — Contexto de engenharia com dois protótipos é razoavelmente inventivo e evita o enunciado clássico de 'lançamento de projétil' isolado; a restrição 'sem se basear apenas na fórmula' evita atalho imediato. Ainda assim, as funções escolhidas (v² puro e queda livre com termo linear) são bastante padrão em livros didáticos.
  - *sugestões:* O conteúdo, o enunciado e o alinhamento à habilidade estão bons; o problema é a classificação do nível cognitivo na especificação. Duas opções: (1) Reclassificar a especificação para Bloom 'analisar' (e SOLO relacional), pois é isso que o item (b) realmente exige — comparar formatos gráficos, relacionar vértice/raízes ao conceito de proporcionalidade e justificar sem apoio direto na fórmula; ou (2) Se o objetivo é manter o nível 'entender', simplificar o item (b) pedindo apenas que o aluno identifique qual protótipo tem proporcionalidade direta e aponte um único elemento gráfico (ex.: 'o vértice está na origem'), sem exigir justificativa comparativa elaborada entre as duas curvas. Recomenda-se a opção (1), pois a tarefa como está é rica e vale a pena preservá-la, apenas corrigindo o rótulo de nível cognitivo na especificação.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: O conteúdo, o enunciado e o alinhamento à habilidade estão bons; o problema é a classificação do nível cognitivo na especificação. Duas opções: (1) Reclassificar a especificação para Bloom 'analisar' (e SOLO relacional), pois é isso que o item (b) realmente exige — comparar formatos gráficos, relacionar vértice/raízes ao conceito de proporcionalidade e justificar sem apoio direto na fórmula; ou (2) Se o objetivo é manter o nível 'entender', simplificar o item (b) pedindo apenas que o aluno identifique qual protótipo tem proporcionalidade direta e aponte um único elemento gráfico (ex.: 'o vértice está na origem'), sem exigir justificativa comparativa elaborada entre as duas curvas. Recomenda-se a opção (1), pois a tarefa como está é rica e vale a pena preservá-la, apenas corrigindo o rótulo de nível cognitivo na especificação.
