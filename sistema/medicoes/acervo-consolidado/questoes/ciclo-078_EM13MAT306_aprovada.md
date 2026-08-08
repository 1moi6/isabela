# Ciclo 078 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em um porto, a altura da maré (em metros) varia de forma periódica ao longo do dia. Registros mostram que a maré atinge seu nível máximo de 5 m às 3h da manhã e seu nível mínimo de 1 m às 9h da manhã, repetindo esse padrão a cada 12 horas — sendo $t$ o tempo em horas contado a partir da meia-noite ($t=0$).

Um estagiário do porto, ao tentar modelar esse fenômeno, propôs a função
$$h(t) = 2\cos\left(\frac{\pi}{6}t\right) + 3,$$
com $t$ em horas, afirmando que ela representa corretamente a maré descrita.

a) Determine a amplitude, o período e o deslocamento vertical do fenômeno periódico descrito pelos registros.

b) Escreva a função $h(t)$, na forma $h(t) = A\cos(B(t-C)) + D$, que representa corretamente a maré observada.

c) Avalie se a proposta do estagiário está correta, comparando os valores previstos por sua função com os dados observados nos instantes $t=3$ h e $t=9$ h. Caso ela esteja incorreta, explique qual característica do gráfico (amplitude, período ou deslocamento de fase) foi tratada de forma equivocada.

## Gabarito

a) Amplitude $A=2$ m, período $T=12$ h, deslocamento vertical $D=3$ m. b) $h(t) = 2\cos\left(\frac{\pi}{6}(t-3)\right)+3$. c) A proposta do estagiário está incorreta: amplitude e período estão certos, mas falta o deslocamento de fase ($C=3$); sua função dá $h(3)=3$ e $h(9)=3$, valores que não correspondem aos dados reais (5 m e 1 m).

## Resolução

**a) Amplitude, período e deslocamento vertical**

A maré varia entre um máximo de $5$ m e um mínimo de $1$ m. Assim:

- Amplitude: $A = \dfrac{5-1}{2} = 2$
- Deslocamento vertical: $D = \dfrac{5+1}{2} = 3$

O intervalo entre o instante de máximo ($t=3$) e o instante de mínimo ($t=9$) corresponde a **meia** volta do ciclo (de crista a cale), ou seja, $T/2 = 9-3 = 6$ h. Logo:

$$T = 12 \text{ h}$$

**b) Construção da função correta**

O coeficiente $B$ (frequência angular) é dado por:
$$B = \frac{2\pi}{T} = \frac{2\pi}{12} = \frac{\pi}{6}$$

Como o cosseno atinge seu valor máximo quando o argumento é zero, e sabemos que o máximo ocorre em $t=3$, o deslocamento de fase deve ser $C = 3$. Assim, a função que representa corretamente o fenômeno é:

$$h(t) = 2\cos\left(\frac{\pi}{6}(t-3)\right) + 3$$

**Verificação:**
- $h(3) = 2\cos(0) + 3 = 2 + 3 = 5$ ✓ (máximo)
- $h(9) = 2\cos\left(\frac{\pi}{6}\cdot 6\right) + 3 = 2\cos(\pi) + 3 = -2+3 = 1$ ✓ (mínimo)

**c) Análise da proposta do estagiário**

A função proposta é $h(t) = 2\cos\left(\frac{\pi}{6}t\right)+3$, que tem a **mesma amplitude** ($A=2$) e o **mesmo período** ($T=12$, pois $B=\pi/6$ é igual) da função correta — porém **sem deslocamento de fase** (equivale a assumir $C=0$, ou seja, que o máximo ocorre à meia-noite).

Calculando os valores previstos pela proposta nos instantes observados:

- $h(3) = 2\cos\left(\frac{\pi}{6}\cdot 3\right)+3 = 2\cos\left(\frac{\pi}{2}\right)+3 = 2(0)+3 = 3$
- $h(9) = 2\cos\left(\frac{\pi}{6}\cdot 9\right)+3 = 2\cos\left(\frac{3\pi}{2}\right)+3 = 2(0)+3 = 3$

Os valores previstos ($3$ m em ambos os instantes) **não coincidem** com os valores observados ($5$ m em $t=3$ e $1$ m em $t=9$). Portanto, **a proposta do estagiário está incorreta**: embora amplitude e período estejam certos, ele **não aplicou o deslocamento horizontal (de fase)** necessário para que o pico do gráfico do cosseno coincida com o instante real do máximo da maré ($t=3$, e não $t=0$).

## Formalização verificável

- `funcao` — expressão `2*cos(pi/6*(t-3))+3`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `2*cos(pi/6*(t-3))+3`, esperado `5`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `2*cos(pi/6*(t-3))+3`, esperado `1`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `2*cos(pi/6*(t-3))+3`, esperado `Interval(1,5)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, 24)'}`
- `funcao` — expressão `2*cos(pi/6*t)+3`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `2*cos(pi/6*t)+3`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '9'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 6 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (maximo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 5). | (3) aprovado: Gabarito confirmado (minimo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 1). | (4) aprovado: Gabarito confirmado (imagem de 2*cos(pi*(t/6 - 1/2)) + 3: Interval(1, 5)). | (5) aprovado: Gabarito confirmado (f(3) = 3). | (6) aprovado: Gabarito confirmado (f(9) = 3).
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - funcao/imagem=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado: dados (máx 5m às 3h, mín 1m às 9h, periodicidade de 12h) são completos e não ambíguos. Os três itens (a, b, c) delimitam claramente o que é pedido em cada etapa, sem duplo sentido lexical ou estrutural.
  - adequacao_nivel: 4/5 — Os itens a e b são majoritariamente de aplicação/compreensão (extrair parâmetros e montar a função), mas o item c exige efetivamente analisar: decompor a função proposta em seus componentes (amplitude, período, fase), comparar com os dados reais e diagnosticar especificamente qual componente foi tratado de forma equivocada. Isso corresponde a uma estrutura relacional (SOLO) coerente com o nível 'analisar' do Bloom. Poderia ser ainda mais exigente se pedisse também justificar por que amplitude e período coincidem mas a fase não, mas o núcleo analítico está presente.
  - alinhamento_bncc: 5/5 — Cumpre todas as exigências: parte de fenômeno periódico real (maré); exige comparação explícita entre a situação real e a representação por cosseno no plano cartesiano; amplitude, período e deslocamento (vertical e de fase) são objeto central da tarefa, não dados decorativos — são calculados, usados na construção da função e depois auditados criticamente no item c. Os itens a, b e c estão articulados em um único fio argumentativo (não são independentes), fortalecendo o alinhamento com a habilidade.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de maré é um clássico de livro didático, mas a estrutura da tarefa foge do padrão 'monte a função e pronto': ao introduzir a proposta equivocada de um estagiário e pedir que o aluno audite essa função contra dados reais, a questão evita a mecanização e cria uma situação de validação/erro didático genuína. Há um leve efeito Topaze no item c, pois já indica quais instantes (t=3 e t=9) comparar, reduzindo parte do trabalho de decisão do aluno sobre como refutar a proposta; isso poderia ser suavizado deixando o aluno escolher os pontos de verificação.
