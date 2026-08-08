# Ciclo 036 — EM13MAT306

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

A altura da maré (em metros) em certo ponto da costa é modelada, para $t$ em horas contadas a partir da meia-noite ($0 \le t \le 24$, um dia completo), pela função $h(t) = 3\cos\left(\dfrac{\pi t}{6}\right) + \dfrac{7}{2}$.

a) Reescreva $h(t)$ em uma forma equivalente usando a função seno, no formato $h(t) = A\,\mathrm{sen}\big(B(t-C)\big) + D$, indicando os valores de $A$, $B$, $C$ e $D$. Compare, em palavras, como o gráfico dessa senoide se relaciona com o gráfico de $y=3\,\mathrm{sen}\left(\dfrac{\pi t}{6}\right)+\dfrac{7}{2}$ (qual é o deslocamento horizontal entre eles).

b) Determine o período do fenômeno e interprete o que esse valor significa em relação ao intervalo entre duas marés altas consecutivas.

c) Determine as alturas máxima e mínima da maré ao longo do dia.

d) Calcule a altura da maré exatamente às 10h ($t=10$).

e) Indique o conjunto de todas as alturas possíveis (imagem) da maré durante as 24 horas do dia.

## Gabarito

a) $h(t)=3\,\mathrm{sen}\left(\frac{\pi}{6}(t+3)\right)+\frac{7}{2}$, deslocamento de 3h à esquerda em relação a $3\,\mathrm{sen}(\pi t/6)+7/2$; b) Período = 12 horas (maré semidiurna); c) Máximo = 13/2 m, Mínimo = 1/2 m; d) $h(10)=5$ m; e) Imagem = $[1/2, 13/2]$.

## Resolução

**a) Forma equivalente em seno**

Usando a identidade $\cos\theta = \mathrm{sen}\left(\theta + \dfrac{\pi}{2}\right)$:

$$h(t) = 3\,\mathrm{sen}\left(\frac{\pi t}{6} + \frac{\pi}{2}\right) + \frac{7}{2}$$

Como $\dfrac{\pi}{6}\cdot 3 = \dfrac{\pi}{2}$, podemos fatorar:

$$h(t) = 3\,\mathrm{sen}\left(\frac{\pi}{6}(t+3)\right) + \frac{7}{2}$$

Logo, na forma $A\,\mathrm{sen}(B(t-C))+D$: $A=3$, $B=\dfrac{\pi}{6}$, $C=-3$, $D=\dfrac{7}{2}$.

Isso mostra que o gráfico de $h(t)$ (que é uma cossenoide) coincide com o gráfico de $y=3\,\mathrm{sen}\left(\dfrac{\pi t}{6}\right)+\dfrac{7}{2}$ deslocado **3 horas para a esquerda** no eixo do tempo — a cossenoide é uma senoide defasada em $\dfrac{\pi}{2}$ rad, o que corresponde a um quarto do período (12/4 = 3h).

**b) Período**

O período de $\cos(Bt)$ é $T = \dfrac{2\pi}{B}$. Aqui $B=\dfrac{\pi}{6}$, logo:

$$T = \frac{2\pi}{\pi/6} = 12 \text{ horas}$$

Isso significa que o padrão de maré se repete a cada 12 horas — ou seja, há duas marés altas e duas marés baixas por dia (maré semidiurna).

**c) Máximo e mínimo**

Como $-1 \le \cos(\cdot) \le 1$:

$$h_{max} = 3(1) + \frac{7}{2} = \frac{13}{2}\text{ m}, \qquad h_{min} = 3(-1) + \frac{7}{2} = \frac{1}{2}\text{ m}$$

**d) Valor em $t=10$**

$$h(10) = 3\cos\left(\frac{10\pi}{6}\right) + \frac{7}{2} = 3\cos\left(\frac{5\pi}{3}\right) + \frac{7}{2} = 3\left(\frac{1}{2}\right) + \frac{7}{2} = \frac{3}{2}+\frac{7}{2} = 5\text{ m}$$

**e) Imagem em $[0,24]$**

Como $24$ é múltiplo do período $12$, dentro de $[0,24]$ o cosseno atinge tanto o valor $1$ (em $t=0,12,24$) quanto o valor $-1$ (em $t=6,18$). Assim, todos os valores entre o mínimo e o máximo são efetivamente alcançados:

$$\text{Im}(h) = \left[\frac{1}{2}, \frac{13}{2}\right]$$

## Formalização verificável

- `funcao` — expressão `3*cos(pi*t/6) + Rational(7,2)`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `3*cos(pi*t/6) + Rational(7,2)`, esperado `Rational(13,2)`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `3*cos(pi*t/6) + Rational(7,2)`, esperado `Rational(1,2)`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `3*cos(pi*t/6) + Rational(7,2)`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `funcao` — expressão `3*cos(pi*t/6) + Rational(7,2)`, esperado `Interval(Rational(1,2), Rational(13,2))`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0,24)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 1/2; gabarito 7/2. | (3) aprovado: Gabarito confirmado (extremo calculado 1/2). | (4) aprovado: Gabarito confirmado (f(10) = 1/2).
  - funcao/periodo=aprovado
  - funcao/maximo=rejeitado
  - funcao/minimo=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 1/2; gabarito 7/2. | (3) aprovado: Gabarito confirmado (extremo calculado 1/2). | (4) aprovado: Gabarito confirmado (f(10) = 1/2). Resultado calculado independentemente: período 12 | extremo calculado 1/2 | extremo calculado 1/2 | f(10) = 1/2. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** rejeitado — 2 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 13/2). | (3) rejeitado: Divergência: extremo calculado 13/2; gabarito 1/2. | (4) aprovado: Gabarito confirmado (f(10) = 5). | (5) rejeitado: Divergência: imagem calculado: Interval.Ropen(1/2, 13/2); gabarito: Interval(1/2, 13/2).
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
  - funcao/valor=aprovado
  - funcao/imagem=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 2 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 13/2). | (3) rejeitado: Divergência: extremo calculado 13/2; gabarito 1/2. | (4) aprovado: Gabarito confirmado (f(10) = 5). | (5) rejeitado: Divergência: imagem calculado: Interval.Ropen(1/2, 13/2); gabarito: Interval(1/2, 13/2). Resultado calculado independentemente: período 12 | extremo calculado 13/2 | extremo calculado 13/2 | f(10) = 5 | imagem calculado: Interval.Ropen(1/2, 13/2). Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 13/2). | (3) rejeitado: Divergência: extremo calculado 13/2; gabarito 1/2. | (4) aprovado: Gabarito confirmado (f(10) = 5). | (5) aprovado: Gabarito confirmado (imagem de 3*cos(pi*t/6) + 7/2: Interval(1/2, 13/2)).
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
  - funcao/valor=aprovado
  - funcao/imagem=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 13/2). | (3) rejeitado: Divergência: extremo calculado 13/2; gabarito 1/2. | (4) aprovado: Gabarito confirmado (f(10) = 5). | (5) aprovado: Gabarito confirmado (imagem de 3*cos(pi*t/6) + 7/2: Interval(1/2, 13/2)). Resultado calculado independentemente: período 12 | extremo calculado 13/2 | extremo calculado 13/2 | f(10) = 5 | imagem de 3*cos(pi*t/6) + 7/2: Interval(1/2, 13/2). Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
