# Ciclo 047 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere as três funções quadráticas, definidas para todo $x \in \mathbb{R}$:

$f(x) = 3x^2$

$g(x) = 3x^2 - 12$

$h(x) = 3(x+2)^2$

a) Entre as três funções, identifique qual delas representa uma situação em que a variável $y$ é diretamente proporcional ao quadrado de $x$, isto é, pode ser escrita na forma $y = kx^2$ com $k$ constante. Justifique algebricamente por que as outras duas NÃO se enquadram nessa relação de proporcionalidade direta.

b) Determine as coordenadas do vértice da parábola associada a cada uma das três funções.

c) Descreva, em termos de translações no plano cartesiano (direção e número de unidades deslocadas), como os gráficos de $g$ e de $h$ podem ser obtidos a partir do gráfico de $f$.

## Gabarito

Apenas $f(x)=3x^2$ é diretamente proporcional a $x^2$ (vértice em $(0,0)$). Vértices: $f\to(0,0)$, $g\to(0,-12)$, $h\to(-2,0)$. O gráfico de $g$ é o de $f$ deslocado 12 unidades para baixo; o de $h$ é o de $f$ deslocado 2 unidades para a esquerda.

## Resolução

**a) Identificando a proporcionalidade direta**

Dizer que $y$ é diretamente proporcional ao quadrado de $x$ significa que existe uma constante $k$ tal que $y = kx^2$, **sem nenhum termo aditivo** (nem constante, nem linear).

- $f(x) = 3x^2$: já está na forma $y = kx^2$, com $k=3$. **É** diretamente proporcional a $x^2$.
- $g(x) = 3x^2 - 12$: ao dividir por $x^2$ obtemos $\dfrac{g(x)}{x^2} = 3 - \dfrac{12}{x^2}$, que **não é constante**. Logo, $g$ **não** representa proporcionalidade direta — a constante $-12$ quebra a razão constante entre $y$ e $x^2$.
- $h(x) = 3(x+2)^2 = 3x^2 + 12x + 12$: expandindo, aparece o termo linear $12x$ e o termo constante $12$. Como há termos de grau menor que 2, $h$ **também não** é da forma $y=kx^2$.

Portanto, apenas $f$ representa uma relação de proporcionalidade direta entre $y$ e $x^2$.

**b) Vértices**

- $f(x) = 3x^2 = 3(x-0)^2 + 0 \Rightarrow$ vértice $(0,0)$.
- $g(x) = 3x^2 - 12 = 3(x-0)^2 + (-12) \Rightarrow$ vértice $(0,-12)$.
- $h(x) = 3(x+2)^2 = 3(x-(-2))^2 + 0 \Rightarrow$ vértice $(-2,0)$.

**c) Translações no plano**

Comparando cada função com $f(x)=3x^2$ (que já está na forma canônica $a(x-x_v)^2+y_v$ com vértice na origem):

- $g(x) = 3x^2 - 12$: mesmo coeficiente $a=3$, mesma abertura, mas o vértice passou de $(0,0)$ para $(0,-12)$. Logo, o gráfico de $g$ é o gráfico de $f$ **transladado 12 unidades para baixo**.
- $h(x) = 3(x+2)^2$: mesmo coeficiente $a=3$, mesma abertura, vértice em $(-2,0)$. Logo, o gráfico de $h$ é o gráfico de $f$ **transladado 2 unidades para a esquerda**.

Geometricamente, apenas o gráfico de $f$ tem vértice na origem — condição necessária (mas equivalente, junto com a ausência de termos de grau menor na forma algébrica) para que a parábola represente $y$ diretamente proporcional a $x^2$; os deslocamentos de $g$ e $h$ tiram justamente essa propriedade.

## Formalização verificável

- `funcao` — expressão `3*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*x**2 - 12`, esperado `[0, -12]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `3*(x+2)**2`, esperado `[-2, 0]`, parâmetros `{'consulta': 'vertice'}`
- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'forma': 'a*x**2', 'grau': '2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (0, -12)). | (3) aprovado: Gabarito confirmado (vértice calculado (-2, 0)). | (4) aprovado: Propriedades confirmadas para 3*x**2: grau 2; forma a*x**2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente as três funções, os dados são completos e cada subitem (a, b, c) delimita precisamente o que é pedido, sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O nível 'entender' é majoritariamente respeitado (interpretar a forma algébrica e relacioná-la à geometria), mas o item (a) exige justificativa algébrica que se aproxima de 'analisar' (SOLO relacional: conectar ausência de termo aditivo/linear com quebra de proporcionalidade). Isso não é grave, mas indica leve descompasso entre o Bloom declarado e a exigência real da tarefa.
  - alinhamento_bncc: 4/5 — A questão cumpre as duas exigências centrais: (i) exige trânsito entre forma algébrica e representação geométrica, pois o item (c) pede a tradução dos parâmetros algébricos em translações no plano, complementando o item (b) que por si só seria apenas numérico; (ii) distingue explicitamente o caso de proporcionalidade direta (item a). Os itens estão articulados em torno das mesmas três funções e se complementam (b alimenta c, a se conecta ao vértice na origem), evitando justaposição de itens soltos.
  - distratores: 5/5 — não se aplica
  - originalidade: 3/5 — A estrutura (comparar três funções quadráticas por translação e proporcionalidade) é bastante convencional e lembra exercícios clássicos de livro didático. Não há contexto significativo ou aplicação; ainda assim, a exigência de justificativa algébrica evita ser puramente mecânica, o que impede nota mais baixa.
