# Ciclo 008 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere as funções quadráticas reais definidas por

$f(x) = 3x^2$

$g(x) = 3x^2 + 6x + 3$

$h(x) = -3x^2 + 12$

a) Determine, para cada função, as coordenadas do vértice da parábola correspondente no plano cartesiano.

b) Uma dessas três funções representa uma situação em que a variável $y$ é diretamente proporcional ao quadrado da variável $x$ (isto é, $y = kx^2$ para alguma constante real $k$). Identifique qual delas é essa função, indique o valor de $k$ e justifique sua escolha com base nos vértices obtidos no item anterior e na forma algébrica de cada expressão, explicando por que as outras duas não satisfazem essa condição.

c) Descreva, em termos de translação no plano cartesiano (direção, sentido e número de unidades deslocadas), como o gráfico de $g$ pode ser obtido a partir do gráfico de $f$.

d) Descreva, indicando o(s) tipo(s) de transformação geométrica envolvida(s) (reflexão e/ou translação), como o gráfico de $h$ se relaciona com o gráfico de $f$.

## Gabarito

a) Vértices: $f\to(0,0)$; $g\to(-1,0)$; $h\to(0,12)$.
b) Apenas $f(x)=3x^2$ é diretamente proporcional a $x^2$ (vértice na origem e sem termos linear/constante), com $k=3$; $g$ e $h$ não satisfazem a condição pois seus vértices não coincidem com a origem.
c) $g$ é o gráfico de $f$ deslocado 1 unidade para a esquerda (translação horizontal), sem deslocamento vertical.
d) $h$ é o gráfico de $f$ refletido em torno do eixo $x$ e depois deslocado 12 unidades para cima.

## Resolução

**a) Vértices das três parábolas**

Para $f(x)=3x^2$: comparando com $f(x)=ax^2+bx+c$, temos $a=3,\;b=0,\;c=0$. O vértice tem abscissa $x_v=-\dfrac{b}{2a}=0$ e ordenada $y_v=f(0)=0$. Logo, o vértice é $(0,0)$, a própria origem.

Para $g(x)=3x^2+6x+3$: aqui $a=3,\;b=6,\;c=3$. Então $x_v=-\dfrac{6}{2\cdot 3}=-1$ e $y_v=g(-1)=3(1)-6+3=0$. Vértice: $(-1,0)$.

Alternativamente, $g(x)=3(x^2+2x+1)=3(x+1)^2$, forma que já revela o vértice $(-1,0)$.

Para $h(x)=-3x^2+12$: aqui $a=-3,\;b=0,\;c=12$. Então $x_v=0$ e $y_v=h(0)=12$. Vértice: $(0,12)$.

**b) Identificando a proporcionalidade direta ao quadrado**

Uma relação do tipo $y=kx^2$ tem gráfico uma parábola cujo vértice é obrigatoriamente a origem $(0,0)$ (pois quando $x=0$, $y=0$) e cuja expressão algébrica não pode ter termo linear ($bx$) nem termo constante ($c$) diferentes de zero.

- $f(x)=3x^2$ tem vértice $(0,0)$ e não possui termos em $x$ nem constante: é exatamente da forma $y=kx^2$, com $k=3$. **Esta é a função procurada.**
- $g(x)=3x^2+6x+3$ tem vértice $(-1,0)$, fora da origem — a translação horizontal introduzida pelo termo $6x$ impede a proporcionalidade direta, mesmo o vértice tendo ordenada nula.
- $h(x)=-3x^2+12$ tem vértice $(0,12)$; embora esteja sobre o eixo $y$, não está na origem, pois o termo constante $12$ desloca toda a parábola para cima — logo $h(0)=12\neq 0$, contrariando a exigência de que $y=0$ quando $x=0$.

Portanto, apenas $f(x)=3x^2$ representa $y$ diretamente proporcional a $x^2$, com constante de proporcionalidade $k=3$.

**c) Relação geométrica entre $f$ e $g$**

Como $g(x)=3(x+1)^2=f(x+1)$, o gráfico de $g$ é obtido a partir do gráfico de $f$ por uma **translação horizontal de 1 unidade para a esquerda** (substituir $x$ por $x+1$ desloca o gráfico no sentido negativo do eixo $x$), sem nenhum deslocamento vertical — coerente com o fato de os vértices $(0,0)$ e $(-1,0)$ terem a mesma ordenada e abscissas diferindo em $1$ unidade.

**d) Relação geométrica entre $f$ e $h$**

Como $h(x)=-3x^2+12=-f(x)+12$, o gráfico de $h$ é obtido a partir do gráfico de $f$ por uma **reflexão em torno do eixo $x$** (o fator $-1$ inverte a concavidade, que passa de voltada para cima para voltada para baixo) seguida de uma **translação vertical de 12 unidades para cima**. Isso é coerente com os vértices: o de $f$ é $(0,0)$ e, após a reflexão (que mantém o vértice em $(0,0)$) e a translação vertical, o vértice de $h$ passa a ser $(0,12)$.

## Formalização verificável

- `funcao` — expressão `3*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*x**2 + 6*x + 3`, esperado `[-1, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-3*x**2 + 12`, esperado `[0, 12]`, parâmetros `{'consulta': 'vertice'}`
- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'forma': 'a*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (-1, 0)). | (3) aprovado: Gabarito confirmado (vértice calculado (0, 12)). | (4) aprovado: Propriedades confirmadas para 3*x**2: forma a*x**2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (três leis algébricas) e quatro pedidos claramente delimitados. Não há ambiguidade lexical ou estrutural; cada item define exatamente o que deve ser produzido (vértice, identificação com justificativa, descrição de translação, descrição de reflexão/translação).
  - adequacao_nivel: 4/5 — O processo cognitivo efetivamente exigido ultrapassa em parte o nível 'entender' declarado: o item (a) é de aplicação direta de fórmula, mas o item (b) exige comparar as três formas algébricas, justificar por que duas delas não satisfazem a condição de proporcionalidade e articular vértice+forma algébrica — isso é mais próximo de 'analisar' (SOLO relacional). Os itens (c) e (d) também pedem justificativa relacional, não mera identificação. O conteúdo é plenamente compatível com o Ensino Médio, mas a exigência cognitiva real é levemente superior à do Bloom declarado, o que não compromete a qualidade da questão, apenas o rótulo de nível.
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as duas exigências da EM13MAT402: (1) exige trânsito genuíno entre forma algébrica e representação geométrica — os vértices são usados para justificar a proporcionalidade (b) e para descrever translações/reflexões (c, d), não apenas calculados isoladamente; (2) distingue explicitamente o caso em que y é diretamente proporcional a x² (f) dos casos em que não é (g, h), com justificativa algébrica e geométrica coerente. Os quatro itens formam um problema articulado, não questões independentes justapostas.
  - distratores: 5/5 — Não se aplica: a questão é discursiva, sem alternativas de múltipla escolha.
  - originalidade: 4/5 — Evita o formato mecânico de 'encontre o vértice de uma parábola' isolado, articulando três funções para construir um raciocínio comparativo sobre proporcionalidade e transformações — isso é mais elaborado que o exercício padrão de livro didático. Falta, porém, um contexto significativo (aplicação real), o que é aceitável dado que a natureza declarada é 'teórica', mas reduz um pouco o potencial de engajamento e significância do enunciado.
