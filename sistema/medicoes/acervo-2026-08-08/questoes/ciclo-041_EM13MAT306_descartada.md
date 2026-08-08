# Ciclo 041 — EM13MAT306

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

Um posto de monitoramento mede, ao longo de um dia, a profundidade da água h(t), em metros, na entrada de um pequeno porto. Por causa da maré, esse valor varia de forma periódica e pode ser bem aproximado por uma função do tipo

h(t) = D + A·cos(B(t − C)),

em que t é o número de horas decorridas desde a meia-noite (0 ≤ t < 24) e A, B, C, D são constantes reais, com A > 0.

Foram feitas as seguintes observações nesse dia:

- O ciclo completo da maré (de uma maré alta até a próxima maré alta) se repete a cada 12 horas.
- Às 14h, a profundidade da água é de exatamente 19/10 m, valor que corresponde à média entre os níveis mais alto e mais baixo atingidos pela maré, e nesse instante a água está subindo.
- Às 17h, a maré atinge seu nível mais alto, de 16/5 m.

a) Determine os valores de A, B, C e D e escreva a lei de h(t).

b) Determine a profundidade mínima da água (maré baixa) nesse dia e todos os instantes, dentro do intervalo [0,24), em que ela ocorre.

c) Descreva como o gráfico de h(t) no intervalo [0,24] se relaciona com o gráfico da função y = cos(t): indique a amplitude, o período e o deslocamento vertical envolvidos nessa comparação.

## Gabarito

A = 13/10, B = π/6, C = 17, D = 19/10, logo h(t) = 19/10 + (13/10)cos(π/6 (t−17)); profundidade mínima = 3/5 m, ocorrendo em t = 11h e t = 23h.

## Resolução

**a) Determinando A, B, C e D**

O ciclo completo da maré se repete a cada 12 horas, ou seja, o período de $h$ é $T = 12$. Como $T = \dfrac{2\pi}{B}$, temos
$$B = \frac{2\pi}{12} = \frac{\pi}{6}.$$

O enunciado diz que às 17h a maré atinge seu valor **máximo**. Na forma $h(t) = D + A\cos(B(t-C))$, o cosseno vale 1 (seu máximo) quando o argumento é zero, isto é, quando $t = C$. Logo
$$C = 17.$$

O enunciado também informa que às 14h a profundidade é exatamente a **média** entre os níveis máximo e mínimo — essa média é justamente $D$ (o deslocamento vertical, em torno do qual a curva oscila). Assim,
$$D = \frac{19}{10}.$$

(Confirmação: em $t=14$, o argumento é $B(14-17) = \frac{\pi}{6}(-3) = -\frac{\pi}{2}$, e $\cos\left(-\frac{\pi}{2}\right)=0$, logo $h(14)=D+A\cdot 0 = D$, consistente com o dado.)

Como a maré alta (máximo) vale $D + A$:
$$D + A = \frac{16}{5} \quad\Rightarrow\quad A = \frac{16}{5} - \frac{19}{10} = \frac{32}{10}-\frac{19}{10} = \frac{13}{10}.$$

Portanto:
$$h(t) = \frac{19}{10} + \frac{13}{10}\cos\left(\frac{\pi}{6}(t-17)\right).$$

**b) Profundidade mínima e instantes em que ocorre**

O valor mínimo do cosseno é $-1$, logo o mínimo de $h$ é
$$h_{min} = D - A = \frac{19}{10}-\frac{13}{10} = \frac{6}{10} = \frac{3}{5}\ \text{m}.$$

Esse mínimo ocorre quando $\cos\left(\frac{\pi}{6}(t-17)\right) = -1$, ou seja, quando
$$\frac{\pi}{6}(t-17) = \pi + 2k\pi \;\Rightarrow\; t - 17 = 6 + 12k \;\Rightarrow\; t = 23 + 12k,\ k\in\mathbb{Z}.$$

Dentro do intervalo $[0,24)$, isso dá $t = 23$ (tomando $k=0$) e $t = 23-12 = 11$ (tomando $k=-1$).

Assim, a maré baixa, de $\dfrac{3}{5}$ m, ocorre **às 11h e às 23h**, como esperado em um regime semidiurno (duas marés altas e duas marés baixas por dia).

**c) Comparação com y = cos(t)**

Partindo de $y=\cos(t)$:
- A **amplitude** passa de 1 para $A = \dfrac{13}{10}$: o gráfico é "esticado" verticalmente, oscilando entre $-\frac{13}{10}$ e $\frac{13}{10}$ em torno de zero antes da translação.
- O fator $B=\dfrac{\pi}{6}$ comprime o gráfico horizontalmente, reduzindo o período de $2\pi$ para $12$ horas (dois ciclos completos a cada 24 h).
- A translação horizontal $C = 17$ desloca o máximo do cosseno (que em $y=\cos(t)$ ocorre em $t=0$) para $t=17$.
- A translação vertical $D=\dfrac{19}{10}$ eleva toda a curva, fazendo-a oscilar entre $\frac{3}{5}$ (mínimo) e $\frac{16}{5}$ (máximo) em vez de entre $-1$ e $1$.

O gráfico de $h(t)$ em $[0,24]$ é, portanto, uma curva cossenoidal com dois picos (em $t=5$ e $t=17$, pois o período é 12h) de altura $\frac{16}{5}$ e dois vales (em $t=11$ e $t=23$) de altura $\frac{3}{5}$, todos centrados na reta $h=\frac{19}{10}$.

## Formalização verificável

- `funcao` — expressão `Rational(19,10) + Rational(13,10)*cos(pi*(t-17)/6)`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `Rational(19,10) + Rational(13,10)*cos(pi*(t-17)/6)`, esperado `Rational(16,5)`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `Rational(19,10) + Rational(13,10)*cos(pi*(t-17)/6)`, esperado `Rational(3,5)`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `Rational(19,10) + Rational(13,10)*cos(pi*(t-17)/6)`, esperado `Rational(16,5)`, parâmetros `{'consulta': 'valor', 'ponto': '17'}`
- `funcao` — expressão `Rational(19,10) + Rational(13,10)*cos(pi*(t-17)/6)`, esperado `Rational(19,10)`, parâmetros `{'consulta': 'valor', 'ponto': '14'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 3/5; gabarito 16/5. | (3) aprovado: Gabarito confirmado (extremo calculado 3/5). | (4) aprovado: Gabarito confirmado (f(17) = 16/5). | (5) aprovado: Gabarito confirmado (f(14) = 19/10).
  - funcao/periodo=aprovado
  - funcao/maximo=rejeitado
  - funcao/minimo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 3/5; gabarito 16/5. | (3) aprovado: Gabarito confirmado (extremo calculado 3/5). | (4) aprovado: Gabarito confirmado (f(17) = 16/5). | (5) aprovado: Gabarito confirmado (f(14) = 19/10). Resultado calculado independentemente: período 12 | extremo calculado 3/5 | extremo calculado 3/5 | f(17) = 16/5 | f(14) = 19/10. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 3/5; gabarito 16/5. | (3) aprovado: Gabarito confirmado (extremo calculado 3/5). | (4) aprovado: Gabarito confirmado (f(17) = 16/5). | (5) aprovado: Gabarito confirmado (f(14) = 19/10).
  - funcao/periodo=aprovado
  - funcao/maximo=rejeitado
  - funcao/minimo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 3/5; gabarito 16/5. | (3) aprovado: Gabarito confirmado (extremo calculado 3/5). | (4) aprovado: Gabarito confirmado (f(17) = 16/5). | (5) aprovado: Gabarito confirmado (f(14) = 19/10). Resultado calculado independentemente: período 12 | extremo calculado 3/5 | extremo calculado 3/5 | f(17) = 16/5 | f(14) = 19/10. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 3/5; gabarito 16/5. | (3) aprovado: Gabarito confirmado (extremo calculado 3/5). | (4) aprovado: Gabarito confirmado (f(17) = 16/5). | (5) aprovado: Gabarito confirmado (f(14) = 19/10).
  - funcao/periodo=aprovado
  - funcao/maximo=rejeitado
  - funcao/minimo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) rejeitado: Divergência: extremo calculado 3/5; gabarito 16/5. | (3) aprovado: Gabarito confirmado (extremo calculado 3/5). | (4) aprovado: Gabarito confirmado (f(17) = 16/5). | (5) aprovado: Gabarito confirmado (f(14) = 19/10). Resultado calculado independentemente: período 12 | extremo calculado 3/5 | extremo calculado 3/5 | f(17) = 16/5 | f(14) = 19/10. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
