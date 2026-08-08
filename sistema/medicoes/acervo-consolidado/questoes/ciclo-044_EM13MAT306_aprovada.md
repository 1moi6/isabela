# Ciclo 044 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

As marés de um pequeno porto pesqueiro variam de forma periódica ao longo do dia, devido à atração gravitacional da Lua e do Sol. Um estudo local registrou que, tomando $t = 0$ como meia-noite (0h), a maré atinge seu nível máximo de $2{,}0$ m exatamente à meia-noite, cai até um nível mínimo de $1{,}0$ m às 6h da manhã, retorna ao máximo às 12h (meio-dia) e repete esse padrão a cada 12 horas ao longo de todo o dia.

a) Identifique a amplitude, o período e o deslocamento vertical (translação do eixo médio) desse fenômeno periódico.

b) Escreva uma função $h(t)$, em metros, que descreva a altura da maré em função do tempo $t$ (em horas), $t \in [0,24)$, usando a função cosseno. Compare essa função com o gráfico da função cosseno "pura" $y=\cos(t)$, indicando quais transformações (translação vertical e compressão/dilatação horizontal) foram necessárias para obter o modelo da maré.

c) Determine a altura da maré às 3h da manhã e explique, com base no gráfico da função obtida em (b), por que esse valor corresponde exatamente à média entre o nível máximo e o mínimo.

## Gabarito

a) Amplitude = 0,5 m; período = 12 h; deslocamento vertical = 1,5 m. b) $h(t) = 1{,}5 + 0{,}5\cos\left(\frac{\pi}{6}t\right)$, obtida comprimindo horizontalmente (fator $\pi/6$), reduzindo a amplitude (fator 0,5) e deslocando verticalmente (+1,5) o gráfico de $y=\cos(t)$. c) $h(3) = 1{,}5$ m, que é a média entre o máximo e o mínimo.

## Resolução

**a) Amplitude, período e deslocamento vertical**

O nível máximo é $2{,}0$ m e o mínimo é $1{,}0$ m. A amplitude é metade da diferença entre esses valores:
$$A = \frac{2{,}0 - 1{,}0}{2} = 0{,}5 \text{ m}$$

O deslocamento vertical (altura média, em torno da qual a maré oscila) é a média entre máximo e mínimo:
$$k = \frac{2{,}0 + 1{,}0}{2} = 1{,}5 \text{ m}$$

Como o padrão se repete a cada 12 horas (máximo em 0h e novamente em 12h), o período é:
$$T = 12 \text{ horas}$$

**b) Construção da função e comparação com $y=\cos(t)$**

A função cosseno padrão $y=\cos(t)$ tem amplitude 1, período $2\pi$, oscila entre $-1$ e $1$, e atinge seu máximo em $t=0$. Como aqui a maré também está no máximo em $t=0$ (meia-noite), o cosseno é a escolha natural (sem precisar de deslocamento horizontal de fase).

Para transformar $y=\cos(t)$ no modelo da maré:

- **Compressão horizontal**: o período deve passar de $2\pi$ para 12 horas. Como o período de $\cos(bt)$ é $\dfrac{2\pi}{b}$, temos:
$$\frac{2\pi}{b} = 12 \;\Rightarrow\; b = \frac{2\pi}{12} = \frac{\pi}{6}$$

- **Dilatação vertical (amplitude)**: multiplica-se por $A = 0{,}5$, reduzindo a oscilação de $[-1,1]$ para $[-0{,}5;\,0{,}5]$.

- **Translação vertical**: soma-se $k=1{,}5$, deslocando o eixo de oscilação de $y=0$ para $y=1{,}5$.

Assim, o modelo é:
$$h(t) = 1{,}5 + 0{,}5\cos\!\left(\frac{\pi}{6}t\right), \quad t \in [0,24)$$

O gráfico de $h(t)$ é o gráfico de $y=\cos(t)$ comprimido horizontalmente (período 12 em vez de $2\pi$), "achatado" verticalmente (amplitude 0,5 em vez de 1) e deslocado para cima em 1,5 unidades.

**c) Altura às 3h**

Substituindo $t=3$:
$$h(3) = 1{,}5 + 0{,}5\cos\!\left(\frac{\pi}{6}\cdot 3\right) = 1{,}5 + 0{,}5\cos\!\left(\frac{\pi}{2}\right) = 1{,}5 + 0{,}5\cdot 0 = 1{,}5 \text{ m}$$

No gráfico da função cosseno, $t=\dfrac{\pi}{2}$ (aqui, $t=3$ h) é exatamente o ponto em que a curva cruza o eixo médio, entre o pico máximo (em $t=0$) e o pico mínimo (em $t=6$). Por isso o valor obtido coincide com a média entre o nível máximo (2,0 m) e o mínimo (1,0 m), confirmando que $t=3$h corresponde à passagem pelo nível médio da maré.

## Formalização verificável

- `funcao` — expressão `Rational(3,2) + Rational(1,2)*cos(pi*t/6)`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `Rational(3,2) + Rational(1,2)*cos(pi*t/6)`, esperado `2`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `Rational(3,2) + Rational(1,2)*cos(pi*t/6)`, esperado `1`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `Rational(3,2) + Rational(1,2)*cos(pi*t/6)`, esperado `Rational(3,2)`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (maximo de cos(pi*t/6)/2 + 3/2 em Reals: 2). | (3) aprovado: Gabarito confirmado (minimo de cos(pi*t/6)/2 + 3/2 em Reals: 1). | (4) aprovado: Gabarito confirmado (f(3) = 3/2).
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta de forma explícita os valores de máximo, mínimo, horários de referência e período de repetição. Não há ambiguidade sobre o que é dado (valores e instantes) nem sobre o que é pedido em cada item (a, b, c). Os dados são suficientes e consistentes entre si.
  - adequacao_nivel: 4/5 — O processo cognitivo predominante é aplicar (extrair amplitude/período/deslocamento de dados concretos, construir a função e calcular um valor), compatível com o nível declarado. A resposta esperada é majoritariamente multiestrutural (identificar três parâmetros, montar a fórmula, calcular um valor), mas o item (c) exige uma justificativa relacional (por que h(3) é a média), o que eleva ligeiramente a exigência SOLO acima do puramente mecânico — coerente e até desejável para 'aplicar' com compreensão.
  - alinhamento_bncc: 5/5 — Atende às três exigências: parte de fenômeno periódico real (maré), exige explicitamente comparação com o gráfico de y=cos(t) (item b) e trata amplitude, período e deslocamento vertical como objeto central da resolução, não como dado decorativo. A articulação entre o fenômeno físico e a representação algébrica/gráfica é feita de forma integrada ao longo dos três itens, não apenas justaposta.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — O contexto de marés modeladas por cosseno é um dos exemplos mais recorrentes em livros didáticos brasileiros para este tópico, o que reduz o fator de novidade. Além disso, os dados (máximo em t=0, mínimo em t=6, período 12h) são fornecidos de modo que o aluno praticamente lê os parâmetros do enunciado sem precisar interpretar um gráfico ou tabela real, aproximando-se do 'efeito Topaze' em um problema que poderia exigir mais leitura/interpretação de dados brutos (ex.: tabela de horários de marés reais).
