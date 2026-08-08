# Ciclo 046 — EM13MAT306

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

A altura da maré (em metros) em certo porto varia de forma periódica ao longo do dia e pode ser modelada pela função $h(t) = 5 + 3\cos\left(\dfrac{\pi t}{6}\right)$, em que $t$ é o tempo em horas, com $t \geq 0$. Comparando essa situação com o gráfico da função cosseno no plano cartesiano, assinale a alternativa que indica corretamente a amplitude, o período e a altura mínima da maré prevista pelo modelo.

## Alternativas

- (a) Amplitude 3 m, período 12 h, mínimo 2 m  ← correta
- (b) Amplitude 5 m, período 12 h, mínimo 2 m
  - *erro representado:* Confunde o deslocamento vertical (d = 5) com a amplitude, ignorando que a amplitude é o coeficiente que multiplica o cosseno.
- (c) Amplitude 3 m, período 6 h, mínimo 2 m
  - *erro representado:* Calcula o período usando apenas o denominador de B (6) em vez de aplicar a fórmula T = 2π/B corretamente, esquecendo o fator 2π.
- (d) Amplitude 3 m, período 12 h, mínimo 8 m
  - *erro representado:* Troca o valor de máximo pelo de mínimo, associando incorretamente cos = 1 (em vez de cos = -1) ao ponto de menor altura.

## Gabarito

Amplitude = 3 m, período = 12 h, mínimo = 2 m

## Resolução

A função $h(t) = 5 + 3\cos\left(\dfrac{\pi t}{6}\right)$ tem a forma geral $h(t) = d + A\cos(Bt)$, comparável ao gráfico padrão de $y = \cos(x)$ deslocado verticalmente e com amplitude e período alterados.

**Amplitude:** é o coeficiente que multiplica o cosseno, ou seja, $A = 3$. Isso significa que o gráfico de $\cos$ é 'esticado' verticalmente por um fator 3, oscilando entre $-3$ e $3$ em torno do eixo médio.

**Deslocamento vertical:** $d = 5$ desloca todo o gráfico do cosseno 5 unidades para cima — é o valor médio da maré, não a amplitude.

**Período:** para $y = \cos(Bt)$, o período é $T = \dfrac{2\pi}{B}$. Aqui $B = \dfrac{\pi}{6}$, logo:
$$T = \dfrac{2\pi}{\pi/6} = 2\pi \cdot \dfrac{6}{\pi} = 12 \text{ horas}.$$

**Altura mínima:** como $\cos\left(\dfrac{\pi t}{6}\right)$ varia entre $-1$ e $1$, temos:
$$h_{min} = 5 + 3\cdot(-1) = 2 \text{ m}, \qquad h_{max} = 5 + 3\cdot 1 = 8 \text{ m}.$$

Portanto, a amplitude é 3 m, o período é 12 h e a altura mínima é 2 m.

## Formalização verificável

- `funcao` — expressão `5 + 3*cos(pi*t/6)`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `5 + 3*cos(pi*t/6)`, esperado `8`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `5 + 3*cos(pi*t/6)`, esperado `2`, parâmetros `{'consulta': 'minimo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 5). | (3) rejeitado: Divergência: extremo calculado 5; gabarito 1.
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 5). | (3) rejeitado: Divergência: extremo calculado 5; gabarito 1. Resultado calculado independentemente: período 12 | extremo calculado 5 | extremo calculado 5. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 8). | (3) rejeitado: Divergência: extremo calculado 8; gabarito 2.
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 8). | (3) rejeitado: Divergência: extremo calculado 8; gabarito 2. Resultado calculado independentemente: período 12 | extremo calculado 8 | extremo calculado 8. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 8). | (3) rejeitado: Divergência: extremo calculado 8; gabarito 2.
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 8). | (3) rejeitado: Divergência: extremo calculado 8; gabarito 2. Resultado calculado independentemente: período 12 | extremo calculado 8 | extremo calculado 8. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
