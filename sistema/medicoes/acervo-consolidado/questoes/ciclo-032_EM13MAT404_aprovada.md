# Ciclo 032 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma roda-gigante de um parque de diversões tem raio de 15 m, e seu eixo central está fixado a 17 m de altura em relação ao solo. A roda gira com velocidade angular constante, completando uma volta a cada 40 segundos. No instante t = 0 (em segundos, contado a partir da abertura do parque), uma cabine específica está exatamente no ponto mais baixo de sua trajetória circular. O parque mantém essa roda-gigante em funcionamento ininterrupto durante as 12 horas de seu horário de atendimento diário (das 9h às 21h).

Um estudante decide modelar a altura h(t), em metros, dessa cabine em relação ao solo, t segundos após a abertura do parque, representando simultaneamente o movimento da cabine no ciclo trigonométrico (posição angular ao longo da circunferência) e no plano cartesiano (gráfico de h em função de t).

a) Determine a lei da função h(t), explicitando como o ângulo percorrido no ciclo trigonométrico se relaciona com a altura registrada no gráfico cartesiano.

b) Indique o período dessa função e explique seu significado físico no contexto da roda-gigante.

c) Considerando que a roda-gigante funciona apenas durante o horário diário de operação do parque, determine o domínio de h(t) para um dia de funcionamento.

d) Determine a imagem de h(t), justificando o resultado a partir da comparação entre a variação do cosseno no ciclo trigonométrico (entre -1 e 1) e a amplitude observada no gráfico cartesiano.

## Gabarito

h(t) = 17 - 15·cos(πt/20) (equivalente a 17 + 15·sen(πt/20 - π/2)); período = 40 s; domínio, para um dia de operação = [0, 43200] segundos; imagem = [2, 32] metros.

## Resolução

## Passo 1: Relacionar o movimento circular ao ciclo trigonométrico

A cabine descreve uma circunferência de raio $R=15$ m ao redor do centro da roda, que está a $17$ m do solo. Associamos a cada instante $t$ um ângulo $\theta(t)$ varrido a partir de uma posição de referência no ciclo trigonométrico.

Como a roda dá uma volta completa ($2\pi$ rad) a cada $40$ s, a velocidade angular é $\omega = \dfrac{2\pi}{40} = \dfrac{\pi}{20}$ rad/s, logo $\theta(t) = \dfrac{\pi}{20}t + \theta_0$.

## Passo 2: Usar a condição inicial para determinar $\theta_0$

No ciclo trigonométrico, a ordenada de um ponto (multiplicada pelo raio) representa sua altura em relação ao centro da circunferência. Em $t=0$ a cabine está no ponto mais baixo, ou seja, na posição angular $\theta = -\dfrac{\pi}{2}$ (onde $\text{sen}\,\theta=-1$). Logo $\theta_0=-\dfrac{\pi}{2}$ e $\theta(t)=\dfrac{\pi}{20}t-\dfrac{\pi}{2}$.

## Passo 3: Escrever h(t) transportando o ciclo para o plano cartesiano

A altura em relação ao solo é a altura do centro somada à projeção vertical multiplicada pelo raio:
$$h(t)=17+15\,\text{sen}\left(\dfrac{\pi}{20}t-\dfrac{\pi}{2}\right)$$
Usando $\text{sen}(x-\pi/2)=-\cos x$, obtemos a forma equivalente, mais simples de analisar no plano cartesiano:
$$h(t)=17-15\cos\left(\dfrac{\pi}{20}t\right)$$
Assim, cada volta completa no ciclo trigonométrico (variação de $2\pi$ no ângulo) corresponde, no plano cartesiano, a um ciclo completo do gráfico de $h(t)$.

## Passo 4: Período

O período é o tempo necessário para o ângulo variar $2\pi$:
$$T=\dfrac{2\pi}{\pi/20}=40\text{ s}$$
Fisicamente, é o tempo de uma volta completa da roda-gigante, coincidindo com o dado do enunciado e confirmando o modelo.

## Passo 5: Domínio

A roda funciona continuamente por $12$ horas $=43200$ s por dia, com $t$ contado a partir da abertura ($t=0$). Portanto, para um dia de funcionamento:
$$D=[0,\,43200]\ \text{(em segundos)}$$

## Passo 6: Imagem

No ciclo trigonométrico, $\cos\theta$ varia continuamente entre $-1$ e $1$ conforme o ângulo percorre toda a circunferência. Como $43200/40=1080$ voltas completas cabem no intervalo de funcionamento, o ciclo é percorrido integralmente muitas vezes, garantindo que os valores extremos são de fato atingidos. Transportando essa variação para o plano cartesiano:
- mínimo: $h_{min}=17-15(1)=2$ m (quando $\cos\theta=1$)
- máximo: $h_{max}=17-15(-1)=32$ m (quando $\cos\theta=-1$)

Logo, a imagem é:
$$Im(h)=[2,\,32]\text{ (em metros)}$$

## Formalização verificável

- `funcao` — expressão `17 - 15*cos(pi*t/20)`, esperado `40`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `17 - 15*cos(pi*t/20)`, esperado `Interval(0, 43200)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `17 - 15*cos(pi*t/20)`, esperado `Interval(2, 32)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, 43200)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 40). | (2) aprovado: Gabarito confirmado (domínio Interval(0, 43200) — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (imagem de 17 - 15*cos(pi*t/20): Interval(2, 32)).
  - funcao/periodo=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado é bem estruturado, com dados completos (raio, altura do eixo, período, condição inicial, horário de funcionamento) e perguntas claramente segmentadas em a, b, c, d. Pequena ambiguidade: não se explicita se o estudante deve escrever h(t) em termos de seno ou cosseno, o que é resolvido na resolução mas não fica evidente a priori no enunciado; isso pode gerar dúvida sobre qual forma é 'a' esperada.
  - adequacao_nivel: 3/5 — O nível declarado é 'entender', compatível com identificar periodicidade, domínio e imagem. Porém o item (a) exige na prática deduzir a lei da função a partir de condições físicas (deslocamento de fase, amplitude, translação vertical), o que é um processo de 'aplicar/criar' modelos, um nível cognitivo mais alto que o declarado. Isso gera uma leve incoerência entre o Bloom declarado e a exigência real da tarefa, embora os itens b, c, d estejam bem alinhados ao nível 'entender'.
  - alinhamento_bncc: 4/5 — A questão cumpre solidamente os requisitos: pede periodicidade (b), domínio (c) e imagem (d), e exige explicitamente a comparação entre ciclo trigonométrico e plano cartesiano em cada um desses itens, não apenas calcular um valor de seno/cosseno. O item (a), embora peça a construção da lei da função (não uma das três características centrais), também exige explicitamente a articulação ciclo-plano cartesiano, e serve de base necessária para os itens seguintes, portanto não descaracteriza a habilidade. Poderia ser mais preciso ao redigir se o item (a) é parte da habilidade ou apenas suporte instrumental.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — O contexto da roda-gigante é significativo e frequentemente usado, mas aqui está bem contextualizado com dados numéricos específicos e articulado explicitamente com a dupla representação (ciclo trigonométrico / plano cartesiano), o que evita o mero 'efeito Topaze' de fórmula pronta. Ainda assim, é um contexto clássico em livros didáticos de funções trigonométricas, reduzindo um pouco a originalidade.
