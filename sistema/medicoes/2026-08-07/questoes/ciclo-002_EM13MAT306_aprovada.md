# Ciclo 002 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em um porto, a altura da coluna de água varia de forma periódica ao longo do dia por causa das marés. Registros mostram que, num certo dia, a maré alta (altura máxima) atinge 8 metros e a maré baixa (altura mínima) atinge 2 metros, repetindo esse ciclo completo a cada 12 horas. Considere que, no instante $t = 0$ (meia-noite), a água está exatamente no nível médio entre a maré alta e a maré baixa, e está subindo a partir desse instante.

a) Determine a amplitude, o período e o valor do deslocamento vertical (nível médio) desse fenômeno, explicando por que uma função seno (ou cosseno), e não uma função linear, é adequada para representar essa variação no plano cartesiano.

b) Escreva a lei $h(t)$, em metros, que descreve a altura da água em função do tempo $t$ (em horas), coerente com as condições do enunciado.

c) Usando a função obtida em (b), calcule a altura da água às 3 horas da manhã (isto é, em $t = 3$).

## Gabarito

Amplitude $A=3$, nível médio $k=5$, período $T=12$ horas; $h(t) = 3\sin\left(\frac{\pi}{6}t\right)+5$; $h(3) = 8$ metros.

## Resolução

**a) Amplitude, período e nível médio**

A altura oscila entre um máximo de $8\,m$ e um mínimo de $2\,m$, repetindo o padrão indefinidamente a cada $12$ horas. Esse comportamento — valores que sobem, descem e retornam ao mesmo padrão em intervalos iguais de tempo — é característico de um fenômeno **periódico**, e não pode ser bem descrito por uma função linear (que cresce ou decresce sem repetir valores). Por isso, usamos seno ou cosseno, que são periódicas e limitadas.

- Amplitude: $A = \dfrac{h_{max} - h_{min}}{2} = \dfrac{8 - 2}{2} = 3$
- Nível médio (deslocamento vertical): $k = \dfrac{h_{max} + h_{min}}{2} = \dfrac{8+2}{2} = 5$
- Período: $T = 12$ horas, e como $T = \dfrac{2\pi}{B}$, temos $B = \dfrac{2\pi}{12} = \dfrac{\pi}{6}$

**b) Construção da lei $h(t)$**

Como em $t=0$ a água está no nível médio e **subindo**, a função seno (que vale $0$ e cresce em $t=0$) é a mais adequada, em vez do cosseno (que começaria no máximo). Assim:

$$h(t) = A\sin(Bt) + k = 3\sin\left(\frac{\pi}{6}t\right) + 5$$

Verificação: $h(0) = 3\sin(0) + 5 = 5$ (nível médio) e a derivada/crescimento inicial é positivo, consistente com "subindo".

**c) Altura às 3 horas ($t = 3$)**

$$h(3) = 3\sin\left(\frac{\pi}{6}\cdot 3\right) + 5 = 3\sin\left(\frac{\pi}{2}\right) + 5 = 3(1) + 5 = 8$$

Às 3h da manhã a água atinge $8$ metros — exatamente a maré alta, o que faz sentido, pois um quarto do período ($12/4 = 3$ horas) após o nível médio crescente, a função seno atinge seu valor máximo.

## Formalização verificável

- `funcao` — expressão `3*sin(pi*x/6) + 5`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `3*sin(pi*x/6) + 5`, esperado `Interval(2, 8)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `3*sin(pi*x/6) + 5`, esperado `8`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (imagem de 3*sin(pi*x/6) + 5: Interval(2, 8)). | (3) aprovado: Gabarito confirmado (f(3) = 8).
  - funcao/periodo=aprovado
  - funcao/imagem=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem construído: define claramente máximo, mínimo, período, condição inicial (t=0, nível médio, subindo) e o que se pede em cada item. Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver univocamente todas as etapas.
  - adequacao_nivel: 4/5 — A maior parte da questão (construir h(t), calcular amplitude/período/deslocamento, avaliar h(3)) corresponde bem ao nível 'aplicar' (SOLO multiestrutural/relacional, pois integra vários parâmetros num único modelo). Porém o pedido em (a) de 'explicar por que uma função seno... é adequada' exige justificativa conceitual, que se aproxima mais de 'entender/analisar' do que de 'aplicar' puro — não invalida a questão, mas gera leve dissonância com o nível de Bloom declarado.
  - alinhamento_bncc: 5/5 — Cumpre as três exigências: parte de fenômeno periódico real (marés), exige explicitamente comparar a situação com a representação seno/cosseno (justificativa em a) e escolha seno vs. cosseno em b), e trata amplitude, período e deslocamento vertical como objeto central da resolução, não como dados decorativos.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de marés para funções periódicas é um exemplo clássico e recorrente em livros didáticos e videoaulas sobre o tema. A explicação pedida em (a) adiciona algum valor pedagógico, mas a estrutura geral (dado max/min, período, calcular h em um instante) segue o roteiro padrão, sem elemento de contexto ou abordagem que a diferencie de questões já amplamente conhecidas.
