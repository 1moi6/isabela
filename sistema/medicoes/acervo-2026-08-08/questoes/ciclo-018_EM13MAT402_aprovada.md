# Ciclo 018 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Considere a função $f(x) = 3x^2$, que relaciona duas grandezas $x$ e $y = f(x)$, em que $y$ é diretamente proporcional ao quadrado de $x$.

A seguir estão descritos quatro esboços de parábolas no plano cartesiano, cada um caracterizado pela posição do vértice, pela equação do eixo de simetria, pelo sentido da concavidade e por um ponto adicional pertencente à curva:

**Gráfico I:** vértice em $(0,0)$; eixo de simetria $x=0$; concavidade para cima; passa pelo ponto $(1,3)$.

**Gráfico II:** vértice em $(1,0)$; eixo de simetria $x=1$; concavidade para cima; passa pelo ponto $(0,3)$.

**Gráfico III:** vértice em $(0,2)$; eixo de simetria $x=0$; concavidade para cima; passa pelo ponto $(1,5)$.

**Gráfico IV:** vértice em $(0,0)$; eixo de simetria $x=0$; concavidade para baixo; passa pelo ponto $(1,-3)$.

Qual dos gráficos descritos representa corretamente a função $f(x) = 3x^2$?

## Alternativas

- (a) Gráfico I  ← correta
- (b) Gráfico II
  - *erro representado:* Confunde uma parábola transladada horizontalmente (vértice fora da origem) com uma proporcionalidade direta ao quadrado, considerando apenas a concavidade e o ponto extra, sem perceber que o vértice não está em (0,0).
- (c) Gráfico III
  - *erro representado:* Ignora o termo constante (deslocamento vertical do vértice), assumindo que basta o eixo de simetria coincidir com x=0 para garantir a proporcionalidade direta, sem verificar se o vértice está exatamente na origem.
- (d) Gráfico IV
  - *erro representado:* Reconhece o vértice na origem, mas erra o sinal do coeficiente k, associando a concavidade para baixo (k negativo) à função f(x)=3x², em vez de perceber que essa concavidade representa y=-3x².

## Gabarito

Gráfico I

## Resolução

Uma função da forma $f(x) = kx^2$ (com $b=0$ e $c=0$ na forma geral $ax^2+bx+c$) tem uma característica geométrica exclusiva: **o vértice da parábola coincide com a origem $(0,0)$** e o **eixo de simetria é o eixo $y$ (reta $x=0$)**.

Isso ocorre porque, para $f(x)=ax^2+bx+c$, as coordenadas do vértice são $x_v = -\dfrac{b}{2a}$ e $y_v = f(x_v)$. Se $b=0$ e $c=0$, então $x_v = 0$ e $y_v = f(0) = 0$, ou seja, o vértice é sempre $(0,0)$ — e reciprocamente, se o vértice está na origem, então necessariamente $b=0$ e $c=0$.

Analisando cada gráfico:

- **Gráfico I:** vértice em $(0,0)$, eixo $x=0$, concavidade para cima (coerente com $a=3>0$) e passa por $(1,3)$. De fato, $f(1) = 3\cdot 1^2 = 3$. Todas as características batem com $f(x)=3x^2$. ✔️

- **Gráfico II:** o vértice está em $(1,0)$, não na origem. Essa é a representação de uma parábola transladada horizontalmente, como $g(x) = 3(x-1)^2 = 3x^2-6x+3$, que **não** é diretamente proporcional a $x^2$ (há termos em $x$ e constante).

- **Gráfico III:** o vértice está em $(0,2)$, deslocado verticalmente. Corresponde a $h(x) = 3x^2+2$, que tem um termo constante $c=2 \neq 0$, logo **não** é diretamente proporcional a $x^2$, mesmo com eixo de simetria em $x=0$.

- **Gráfico IV:** vértice na origem e eixo $x=0$, mas a concavidade é para baixo, o que corresponde a $j(x) = -3x^2$ (coeficiente negativo). Embora também seja uma proporcionalidade direta ao quadrado, é a função $y=-3x^2$, e **não** $f(x)=3x^2$.

Portanto, o único gráfico compatível com $f(x)=3x^2$ é o **Gráfico I**, pois é o único que tem vértice na origem, eixo de simetria $x=0$, concavidade para cima e passa pelo ponto $(1,3)$, confirmando $k=3$.

## Formalização verificável

- `funcao` — expressão `3*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*x**2`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '1'}`
- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'pontos': '[(1,3)]', 'forma': 'k*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (1, -2)). | (3) aprovado: Gabarito confirmado (vértice calculado (0, 3)). | (4) aprovado: Gabarito confirmado (vértice calculado (1, 0)).
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define com precisão o que significa 'diretamente proporcional ao quadrado', apresenta as quatro alternativas de forma explícita e a pergunta é inequívoca. Não há ambiguidade lexical ou estrutural, e os dados (as quatro leis) são suficientes para resolver o problema.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (aplicar o critério b=0 e c=0 / vértice na origem a quatro casos concretos) é compatível com o nível 'aplicar' de Bloom. Na taxonomia SOLO, a resposta é multiestrutural (analisar cada alternativa separadamente com o mesmo procedimento), o que é adequado para esse nível, embora não exija uma integração relacional mais complexa entre os casos.
  - alinhamento_bncc: 2/5 — A especificação exige explicitamente 'trânsito entre a forma algébrica e a representação geométrica no plano cartesiano' e adverte que 'pedir apenas raízes ou o vértice em forma numérica NÃO realiza esta habilidade'. A resolução apresentada faz exatamente isso: calcula x_v=-b/2a e y_v=f(x_v) numericamente para cada função, sem qualquer esboço, leitura ou interpretação gráfica real. O enunciado menciona 'posição do vértice no plano cartesiano', mas na prática a tarefa se reduz a um cálculo algébrico de coordenadas, não a uma conversão efetiva entre representações (por exemplo, associar cada lei a um gráfico dado, ou pedir que o aluno esboce/reconheça a curva). A segunda exigência (distinguir os casos de proporcionalidade direta) é cumprida, mas a primeira, central para a habilidade EM13MAT402, não é atendida de forma satisfatória.
  - distratores: 5/5 — Os quatro distratores correspondem a erros conceituais plausíveis e distintos: confundir 'sem termo constante' com proporcionalidade (B), confundir 'sem termo linear' com proporcionalidade (C), e confundir raiz dupla/forma fatorada com vértice na origem (D). Nenhum é trivialmente eliminável nem absurdo; todos exigem compreensão real do conceito para serem descartados.
  - originalidade: 3/5 — O formato (comparar quatro leis quadráticas e identificar qual tem vértice na origem) é um exercício clássico e recorrente em livros didáticos sobre proporcionalidade quadrática, sem contextualização significativa (situação real, dados de fenômeno, etc.). Não há efeito Topaze evidente, mas a definição dada no enunciado já entrega quase todo o critério de resolução (vértice na origem, eixo y), reduzindo o espaço de descoberta do aluno.
  - *sugestões:* Reformule a questão para exigir efetivamente a conversão entre representações algébrica e geométrica, não apenas o cálculo numérico do vértice. Por exemplo: apresente os quatro gráficos (esboços de parábolas com escalas nos eixos, sem as leis algébricas visíveis) e peça que o aluno associe cada gráfico à lei algébrica correspondente, ou identifique em qual gráfico a relação y=kx² se verifica observando a posição do vértice e o eixo de simetria diretamente na figura. Alternativamente, peça que o aluno esboce o gráfico de cada função (ou reconheça entre esboços dados) e justifique a partir do desenho, não apenas do cálculo de x_v e y_v. Isso garante o trânsito entre álgebra e geometria exigido pela habilidade EM13MAT402, e não apenas a obtenção numérica do vértice. Mantenha os quatro distratores, que já são bem construídos, adaptando-os ao novo formato visual.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule a questão para exigir efetivamente a conversão entre representações algébrica e geométrica, não apenas o cálculo numérico do vértice. Por exemplo: apresente os quatro gráficos (esboços de parábolas com escalas nos eixos, sem as leis algébricas visíveis) e peça que o aluno associe cada gráfico à lei algébrica correspondente, ou identifique em qual gráfico a relação y=kx² se verifica observando a posição do vértice e o eixo de simetria diretamente na figura. Alternativamente, peça que o aluno esboce o gráfico de cada função (ou reconheça entre esboços dados) e justifique a partir do desenho, não apenas do cálculo de x_v e y_v. Isso garante o trânsito entre álgebra e geometria exigido pela habilidade EM13MAT402, e não apenas a obtenção numérica do vértice. Mantenha os quatro distratores, que já são bem construídos, adaptando-os ao novo formato visual.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (f(1) = 3). | (3) aprovado: Propriedades confirmadas para 3*x**2: reproduz os 1 pontos dados; forma k*x**2.
  - funcao/vertice=aprovado
  - funcao/valor=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define com precisão o que é dado (função, definição de proporcionalidade direta) e o que é pedido (qual gráfico corresponde a f(x)=3x²). Cada 'gráfico' é descrito por dados numéricos completos e não ambíguos (vértice, eixo, concavidade, ponto extra), eliminando qualquer dúvida interpretativa.
  - adequacao_nivel: 4/5 — O processo exigido é de fato 'aplicar': o aluno aplica o critério algébrico (b=0, c=0 ⇒ vértice na origem) para julgar quatro configurações geométricas. A estrutura de resposta é relacional (SOLO), pois exige integrar vértice, eixo, concavidade e ponto simultaneamente, não apenas verificar um dado isolado. Compatível com o Ensino Médio.
  - alinhamento_bncc: 4/5 — A questão exige transitar entre a forma algébrica (f(x)=3x²) e propriedades geométricas do gráfico (vértice, eixo, concavidade), e distingue explicitamente o caso de proporcionalidade direta (Gráfico I) dos casos de deslocamento horizontal/vertical e de sinal invertido — que são precisamente os contraexemplos que a habilidade pede para diferenciar. A única ressalva é que os 'gráficos' são descritos textualmente por parâmetros numéricos, e não apresentados como imagens/plots reais; isso atenua um pouco o caráter 'geométrico visual' da conversão, embora a lógica conceitual exigida pela habilidade seja plenamente atendida.
  - distratores: 5/5 — Os três distratores representam erros conceituais distintos e plausíveis: confundir translação horizontal com proporcionalidade (II), ignorar deslocamento vertical/termo constante (III), e errar o sinal do coeficiente (IV). Nenhum é absurdo ou trivialmente eliminável; cada um exige raciocínio equivocado específico e realista.
  - originalidade: 3/5 — A questão é tecnicamente bem construída, mas segue o formato clássico de 'compare parábolas e identifique a correta', sem contexto aplicado ou significativo. Não há efeito Topaze explícito, mas também não há elemento que fuja do padrão de livro didático.
