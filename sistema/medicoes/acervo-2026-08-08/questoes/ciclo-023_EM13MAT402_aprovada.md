# Ciclo 023 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Em um laboratório de física, dois experimentos com movimento vertical/inclinado foram registrados.

**Situação A:** uma esfera é solta do repouso no topo de uma rampa e rola livremente. A distância percorrida $d$ (em metros) em função do tempo $t$ (em segundos) é dada por $d(t) = 3t^2$.

**Situação B:** um pequeno foguete de brinquedo é lançado de uma plataforma elevada, com velocidade inicial diferente de zero. Enquanto está no ar, sua altura $h$ (em metros) em função do tempo $t$ (em segundos) é dada por $h(t) = -5t^2 + 10t + 2$.

Um software de geometria dinâmica gerou quatro esboços de parábolas no plano cartesiano (tempo no eixo horizontal, grandeza no eixo vertical), sem indicar valores numéricos:

- **Gráfico I:** concavidade voltada para cima; o vértice coincide com a origem $(0,0)$; a curva passa pela origem e cresce continuamente para $t>0$, sem nunca assumir valores negativos.
- **Gráfico II:** concavidade voltada para cima; o vértice está deslocado para a direita da origem e abaixo do eixo horizontal; a curva não passa pela origem.
- **Gráfico III:** concavidade voltada para baixo; o vértice está deslocado para a direita da origem e acima do eixo horizontal; a curva corta o eixo vertical em um ponto acima da origem e, depois de atingir o ponto mais alto, desce e cruza o eixo horizontal em um instante positivo.
- **Gráfico IV:** concavidade voltada para baixo; o vértice coincide com a origem $(0,0)$; a curva é decrescente para todo $t>0$.

Com base nas equações e nos esboços descritos, identifique corretamente a qual situação corresponde cada gráfico e qual das duas situações representa uma grandeza diretamente proporcional ao quadrado da outra.

## Alternativas

- (a) Gráfico I corresponde à situação A e Gráfico III à situação B. Apenas a situação A representa uma grandeza diretamente proporcional ao quadrado do tempo, pois sua parábola tem vértice na origem, passa por $(0,0)$ e a razão $d(t)/t^2$ é constante ($k=3$).  ← correta
- (b) Gráfico IV corresponde à situação A e Gráfico II à situação B, e ambas as situações representam grandezas diretamente proporcionais ao quadrado do tempo, já que as duas são funções quadráticas em $t$.
  - *erro representado:* Confunde 'ser função quadrática' com 'ser diretamente proporcional ao quadrado da variável', ignorando o papel do vértice e dos termos adicionais; também erra a associação gráfica ao inverter a concavidade indicada pelo sinal do coeficiente principal.
- (c) Gráfico I corresponde à situação A e Gráfico III à situação B, mas ambas as situações são diretamente proporcionais, pois em ambos os casos a grandeza depende do quadrado do tempo.
  - *erro representado:* Generaliza que qualquer expressão contendo $t^2$ é proporcionalidade direta, sem verificar se a curva passa pela origem nem se a razão pela variável ao quadrado é constante, ignorando os termos lineares e constantes de $h(t)$.
- (d) Gráfico II corresponde à situação A e Gráfico III à situação B; nenhuma das duas situações representa proporcionalidade direta, pois em ambas o coeficiente do termo quadrático é diferente de 1.
  - *erro representado:* Confunde proporcionalidade direta com coeficiente de proporcionalidade igual a 1, e escolhe o gráfico errado para a situação A ao supor, indevidamente, que o coeficiente 3 desloca o vértice para fora da origem.

## Gabarito

Gráfico I corresponde à situação A e Gráfico III à situação B; apenas a situação A ($d(t)=3t^2$) representa proporcionalidade direta entre a distância e o quadrado do tempo, pois sua parábola tem vértice na origem e razão $d(t)/t^2$ constante.

## Resolução

**Passo 1 – Analisar a situação A: $d(t) = 3t^2$**

Essa função não possui termo linear nem termo constante. Logo:
- o coeficiente do termo quadrático é $a = 3 > 0$, portanto a concavidade é voltada para cima;
- o vértice é calculado por $t_v = -\dfrac{b}{2a} = -\dfrac{0}{6} = 0$ e $d(0) = 0$, ou seja, o vértice é o ponto $(0,0)$;
- como $d(0)=0$ e não há deslocamento horizontal ou vertical em relação a $y = 3t^2$, a curva passa pela origem.

Esse comportamento (concavidade para cima, vértice na origem, passando por $(0,0)$) corresponde exatamente ao **Gráfico I**.

Além disso, para essa função, $\dfrac{d(t)}{t^2} = 3$ é constante para todo $t \neq 0$. Isso caracteriza $d$ como **diretamente proporcional ao quadrado de $t$**, com constante de proporcionalidade $k=3$: dobrando o tempo, a distância fica multiplicada por $2^2=4$.

**Passo 2 – Analisar a situação B: $h(t) = -5t^2 + 10t + 2$**

Aqui $a = -5 < 0$, então a concavidade é voltada para baixo. O vértice é:
$$t_v = -\frac{b}{2a} = -\frac{10}{2\cdot(-5)} = 1, \qquad h(1) = -5(1)^2+10(1)+2 = 7.$$
Logo o vértice é $(1,7)$, deslocado para a direita e para cima em relação à origem — não coincide com $(0,0)$.

O valor inicial é $h(0) = 2 \neq 0$, isto é, a curva corta o eixo vertical acima da origem (não passa pela origem). Como o foguete continua subindo até $t=1$ e depois desce, cruzando o eixo horizontal (o chão) em um instante $t>0$, esse comportamento corresponde ao **Gráfico III**.

**Passo 3 – Verificar a proporcionalidade**

Para $h(t)$, a razão $\dfrac{h(t)}{t^2}$ não é constante (por exemplo, $h(1)/1^2 = 7$ e $h(2)/2^2 = (-20+20+2)/4 = 0{,}5$). Além disso, o vértice não está na origem e a curva não passa por $(0,0)$. Portanto, **a situação B não representa uma proporcionalidade direta entre $h$ e $t^2$** — a presença dos termos $10t$ e $2$ desloca a parábola em relação a $y=-5t^2$.

**Conclusão:** Gráfico I → Situação A; Gráfico III → Situação B; apenas a Situação A é um caso de grandeza diretamente proporcional ao quadrado da outra.

## Formalização verificável

- `funcao` — expressão `3*t**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*t**2`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `-5*t**2 + 10*t + 2`, esperado `[1, 7]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-5*t**2 + 10*t + 2`, esperado `2`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (10, 50)).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta claramente duas funções quadráticas em contextos distintos, define as variáveis e unidades, e a pergunta final é precisa quanto ao que se pede (vértice, concavidade e proporcionalidade direta ao quadrado). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido é essencialmente aplicar fórmulas conhecidas (vértice = -b/2a, substituição, verificação de termos lineares/constantes) e comparar dois casos, compatível com o nível 'aplicar'. A resposta exige relacionar informações de duas funções (SOLO relacional), o que é adequado, mas o raciocínio permanece dentro de procedimentos padronizados sem exigir generalização ou análise mais profunda.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT402 exige trânsito efetivo entre representação algébrica e representação geométrica no plano cartesiano (ex.: esboçar, reconhecer gráfico, identificar transformações visuais), não apenas calcular numericamente vértice e concavidade a partir da fórmula. A questão e sua resolução são inteiramente algébricas: não há gráfico apresentado, nem se pede a construção ou leitura de um gráfico, apenas cálculo simbólico de coordenadas e sinal de 'a'. A especificação do próprio professor alerta que 'pedir apenas... o vértice em forma numérica NÃO realiza esta habilidade' — e é exatamente isso que ocorre aqui, mesmo mencionando 'plano cartesiano' no enunciado. A distinção de proporcionalidade direta é bem trabalhada, mas a conversão geométrica exigida pela habilidade não se concretiza.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e comuns: inversão de sinal na fórmula do vértice, confusão conceitual entre função quadrática genérica e proporcionalidade direta, e erro de substituição (usar x=0 em vez de x_v). Nenhum é trivialmente eliminável por absurdo aparente.
  - originalidade: 3/5 — O uso de dois contextos (energia elástica e lucro) para contrastar proporcionalidade direta é uma escolha razoavelmente significativa, mas a estrutura da pergunta e o procedimento de resolução seguem o padrão clássico de 'calcule o vértice e diga a concavidade', sem explorar visualização gráfica ou uso de tecnologia sugerido pela habilidade, reduzindo o potencial de originalidade pedagógica.
  - *sugestões:* Reformule a questão para exigir efetivamente a conversão entre representação algébrica e geométrica, conforme pede EM13MAT402: (1) apresente gráficos (esboços ou imagens) das duas parábolas, sem rotular numericamente o vértice, e peça ao aluno para associar cada gráfico à função correspondente, justificando pela posição do vértice e concavidade; ou (2) peça para o aluno esboçar/descrever qualitativamente o formato e a posição da parábola (deslocamento horizontal/vertical em relação a y=ax²) a partir da equação, e não apenas calcular numericamente as coordenadas do vértice via fórmula. Mantenha a comparação entre as duas situações para preservar a distinção de proporcionalidade direta, mas garanta que ao menos uma etapa da resposta dependa da leitura ou construção do gráfico no plano cartesiano, não apenas de substituição em fórmulas algébricas.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule a questão para exigir efetivamente a conversão entre representação algébrica e geométrica, conforme pede EM13MAT402: (1) apresente gráficos (esboços ou imagens) das duas parábolas, sem rotular numericamente o vértice, e peça ao aluno para associar cada gráfico à função correspondente, justificando pela posição do vértice e concavidade; ou (2) peça para o aluno esboçar/descrever qualitativamente o formato e a posição da parábola (deslocamento horizontal/vertical em relação a y=ax²) a partir da equação, e não apenas calcular numericamente as coordenadas do vértice via fórmula. Mantenha a comparação entre as duas situações para preservar a distinção de proporcionalidade direta, mas garanta que ao menos uma etapa da resposta dependa da leitura ou construção do gráfico no plano cartesiano, não apenas de substituição em fórmulas algébricas.

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (zeros da função: [0]). | (3) aprovado: Gabarito confirmado (vértice calculado (1, 7)). | (4) aprovado: Gabarito confirmado (f(0) = 2).
  - funcao/vertice=aprovado
  - funcao/zeros=aprovado
  - funcao/vertice=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado é extenso mas bem estruturado: define claramente as duas funções, descreve cada gráfico com atributos geométricos precisos (concavidade, vértice, interseção com eixos) e formula a pergunta de forma inequívoca. A única leve perda de clareza é a densidade de informação nos quatro esboços, que exige leitura cuidadosa, mas não gera ambiguidade real.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (transportar coeficientes algébricos para propriedades geométricas do gráfico e verificar proporcionalidade) é compatível com 'aplicar', embora já roce 'analisar' pela necessidade de comparar duas situações e integrar múltiplos critérios (vértice, concavidade, razão d/t²). A estrutura de resposta é relacional (SOLO), coerente com o nível declarado. Conteúdo plenamente adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — Cumpre integralmente a habilidade: exige transitar da forma algébrica (equações de d(t) e h(t)) para a representação geométrica (associação com esboços descritos qualitativamente, sem valores numéricos, o que reforça o trânsito conceitual) e articula isso com a distinção entre proporcionalidade direta ao quadrado (situação A) e não proporcionalidade (situação B), unindo os dois aspectos da habilidade num único problema, não em itens isolados.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis: confundir concavidade/vértice ao trocar gráficos, generalizar 'ter t²' como proporcionalidade direta sem checar vértice na origem, e confundir a constante de proporcionalidade k com a exigência de k=1. Nenhum é absurdo ou trivialmente eliminável sem compreensão do conceito.
  - originalidade: 5/5 — O contexto de laboratório com esfera e foguete, aliado a gráficos descritos apenas qualitativamente (sem eixos numerados), evita o padrão mecânico de 'ache o vértice desta parábola' e não oferece pistas diretas que resolvam o problema sem raciocínio (sem efeito Topaze). É uma abordagem pouco convencional para o tema.
