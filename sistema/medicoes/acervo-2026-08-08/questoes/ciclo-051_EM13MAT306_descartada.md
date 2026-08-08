# Ciclo 051 — EM13MAT306

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

Uma estação de monitoramento costeiro registrou a altura da maré (em metros) ao longo de um dia. Observou-se que a maré alta ocorre às 3h, com altura de 1,8 m, e a maré baixa ocorre às 9h, com altura de 0,4 m. Esse padrão se repete a cada 12 horas, caracterizando uma maré semidiurna. Considerando $t$ o tempo em horas contadas a partir da meia-noite (0h) e $h(t)$ a altura da maré em metros, qual função descreve corretamente esse fenômeno periódico?

## Alternativas

- (a) $h(t) = \dfrac{11}{10} + \dfrac{7}{10}\cos\left(\dfrac{\pi}{6}(t-3)\right)$  ← correta
- (b) $h(t) = 1{,}8\cos\left(\dfrac{\pi}{6}(t-3)\right)$
  - *erro representado:* Usar o valor máximo da maré como amplitude e esquecer o deslocamento vertical (linha média), em vez de calcular A = (máx−mín)/2 e D = (máx+mín)/2.
- (c) $h(t) = \dfrac{11}{10} + \dfrac{7}{10}\cos\left(\dfrac{\pi}{12}(t-3)\right)$
  - *erro representado:* Confundir o período do fenômeno (12h) com o período de um dia completo (24h) ao calcular o coeficiente B = 2π/T, usando T=24 em vez de T=12.
- (d) $h(t) = \dfrac{11}{10} + \dfrac{7}{10}\cos\left(\dfrac{\pi}{6}t\right)$
  - *erro representado:* Ignorar o deslocamento de fase, assumindo que o valor máximo ocorre em t=0 (meia-noite) em vez de t=3 (3h), quando de fato ocorre a maré alta.

## Gabarito

h(t) = 1,1 + 0,7·cos(π(t-3)/6)

## Resolução

**Passo 1 — Amplitude.** A amplitude é a metade da diferença entre o valor máximo e o valor mínimo: $A = \dfrac{1{,}8 - 0{,}4}{2} = \dfrac{1{,}4}{2} = 0{,}7 = \dfrac{7}{10}$.

**Passo 2 — Linha média (deslocamento vertical).** É a média entre máximo e mínimo: $D = \dfrac{1{,}8 + 0{,}4}{2} = \dfrac{2{,}2}{2} = 1{,}1 = \dfrac{11}{10}$.

**Passo 3 — Período.** O fenômeno se repete a cada 12 horas, logo o período é $T=12$. Para uma função cosseno $h(t) = D + A\cos(B(t-C))$, o coeficiente $B$ satisfaz $T = \dfrac{2\pi}{B} \Rightarrow B = \dfrac{2\pi}{12} = \dfrac{\pi}{6}$.

**Passo 4 — Deslocamento de fase.** Como o cosseno atinge seu valor máximo quando o argumento é zero, e sabemos que o máximo ocorre em $t=3$, devemos ter $C=3$, de modo que o argumento se anule exatamente nesse instante: $\cos\left(\dfrac{\pi}{6}(3-3)\right) = \cos(0) = 1$.

**Passo 5 — Montagem da função.** Substituindo os valores encontrados:
$$h(t) = \frac{11}{10} + \frac{7}{10}\cos\left(\frac{\pi}{6}(t-3)\right)$$

**Verificação:**
- $h(3) = \dfrac{11}{10} + \dfrac{7}{10}\cos(0) = \dfrac{11}{10}+\dfrac{7}{10} = \dfrac{18}{10} = \dfrac{9}{5} = 1{,}8$ (maré alta, confere).
- $h(9) = \dfrac{11}{10} + \dfrac{7}{10}\cos(\pi) = \dfrac{11}{10}-\dfrac{7}{10} = \dfrac{4}{10} = \dfrac{2}{5} = 0{,}4$ (maré baixa, confere).
- O período de $\cos\left(\dfrac{\pi}{6}(t-3)\right)$ é $\dfrac{2\pi}{\pi/6}=12$, como esperado.

Portanto, a função correta é $h(t) = \dfrac{11}{10} + \dfrac{7}{10}\cos\left(\dfrac{\pi}{6}(t-3)\right)$.

## Formalização verificável

- `funcao` — expressão `Rational(11,10) + Rational(7,10)*cos(pi*(t-3)/6)`, esperado `9/5`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `Rational(11,10) + Rational(7,10)*cos(pi*(t-3)/6)`, esperado `2/5`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `Rational(11,10) + Rational(7,10)*cos(pi*(t-3)/6)`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `Rational(11,10) + Rational(7,10)*cos(pi*(t-3)/6)`, esperado `9/5`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `Rational(11,10) + Rational(7,10)*cos(pi*(t-3)/6)`, esperado `2/5`, parâmetros `{'consulta': 'valor', 'ponto': '9'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (extremo calculado 9/5). | (2) rejeitado: Divergência: extremo calculado 9/5; gabarito 2/5. | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(3) = 9/5). | (5) aprovado: Gabarito confirmado (f(9) = 2/5).
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
  - funcao/periodo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (extremo calculado 9/5). | (2) rejeitado: Divergência: extremo calculado 9/5; gabarito 2/5. | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(3) = 9/5). | (5) aprovado: Gabarito confirmado (f(9) = 2/5). Resultado calculado independentemente: extremo calculado 9/5 | extremo calculado 9/5 | período 12 | f(3) = 9/5 | f(9) = 2/5. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (extremo calculado 9/5). | (2) rejeitado: Divergência: extremo calculado 9/5; gabarito 2/5. | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(3) = 9/5). | (5) aprovado: Gabarito confirmado (f(9) = 2/5).
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
  - funcao/periodo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (extremo calculado 9/5). | (2) rejeitado: Divergência: extremo calculado 9/5; gabarito 2/5. | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(3) = 9/5). | (5) aprovado: Gabarito confirmado (f(9) = 2/5). Resultado calculado independentemente: extremo calculado 9/5 | extremo calculado 9/5 | período 12 | f(3) = 9/5 | f(9) = 2/5. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (extremo calculado 9/5). | (2) rejeitado: Divergência: extremo calculado 9/5; gabarito 2/5. | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(3) = 9/5). | (5) aprovado: Gabarito confirmado (f(9) = 2/5).
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
  - funcao/periodo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (extremo calculado 9/5). | (2) rejeitado: Divergência: extremo calculado 9/5; gabarito 2/5. | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Gabarito confirmado (f(3) = 9/5). | (5) aprovado: Gabarito confirmado (f(9) = 2/5). Resultado calculado independentemente: extremo calculado 9/5 | extremo calculado 9/5 | período 12 | f(3) = 9/5 | f(9) = 2/5. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
