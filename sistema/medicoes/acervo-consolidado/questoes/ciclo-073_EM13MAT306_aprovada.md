# Ciclo 073 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

O nível da maré em certo ponto da costa varia de forma cíclica ao longo do dia e pode ser modelado pela função $h(t) = 2\cos\left(\dfrac{\pi}{6}(t-3)\right) + 3$, em que $t$ é o tempo em horas contado a partir da meia-noite ($t \ge 0$) e $h(t)$ é a altura da maré, em metros. Interpretando o gráfico dessa função como uma curva cossenoidal no plano cartesiano, determine: a altura máxima e a altura mínima da maré, o período do fenômeno e todos os instantes $t$, com $0 \le t < 12$, em que a maré atinge exatamente 4 metros de altura.

## Alternativas

- (a) Altura máxima 5 m; altura mínima 1 m; período 12 h; maré de 4 m em $t=1$ h e $t=5$ h.  ← correta
- (b) Altura máxima 2 m; altura mínima -2 m; período 12 h; maré de 4 m em $t=1$ h e $t=5$ h.
  - *erro representado:* Confunde a amplitude com o valor máximo/mínimo real da função, ignorando o deslocamento vertical D=3 que desloca a curva do eixo horizontal.
- (c) Altura máxima 5 m; altura mínima 1 m; período 6 h; maré de 4 m em $t=1$ h e $t=5$ h.
  - *erro representado:* Calcula o período de forma incorreta (usa T = π/B sem o fator 2, obtendo 6 em vez de 12).
- (d) Altura máxima 5 m; altura mínima 1 m; período 12 h; maré de 4 m apenas em $t=1$ h.
  - *erro representado:* Encontra apenas a solução principal da equação trigonométrica (arco de -π/3), esquecendo a simetria do cosseno que gera uma segunda solução dentro do mesmo período.

## Gabarito

Altura máxima 5 m; altura mínima 1 m; período 12 h; maré de 4 m em $t=1$ h e $t=5$ h.

## Resolução

**1. Identificando os parâmetros da função cossenoidal**

A função tem a forma $h(t) = A\cos(B(t-C)) + D$, com $A=2$, $B=\dfrac{\pi}{6}$, $C=3$ e $D=3$.

**2. Máximo e mínimo**

Como $-1 \le \cos(\cdot) \le 1$, o valor máximo ocorre quando o cosseno vale $1$:
$$h_{max} = 2(1) + 3 = 5 \text{ m}$$
e o valor mínimo ocorre quando o cosseno vale $-1$:
$$h_{min} = 2(-1) + 3 = 1 \text{ m}$$
Note que a amplitude ($A=2$) mede a distância entre a curva e a reta média $D=3$, e não o valor máximo em si — esse é um erro comum.

**3. Período**

O período de $\cos(Bt)$ é $T = \dfrac{2\pi}{B}$. Aqui $B = \dfrac{\pi}{6}$, logo:
$$T = \frac{2\pi}{\pi/6} = 12 \text{ horas}$$

**4. Instantes em que $h(t) = 4$**

$$2\cos\left(\frac{\pi}{6}(t-3)\right) + 3 = 4 \;\Rightarrow\; \cos\left(\frac{\pi}{6}(t-3)\right) = \frac{1}{2}$$

O cosseno vale $\tfrac{1}{2}$ quando o arco é $\pm\dfrac{\pi}{3}$ (mais múltiplos de $2\pi$, que aqui saem do intervalo pedido). Assim:
$$\frac{\pi}{6}(t-3) = \frac{\pi}{3} \;\Rightarrow\; t-3 = 2 \;\Rightarrow\; t = 5$$
$$\frac{\pi}{6}(t-3) = -\frac{\pi}{3} \;\Rightarrow\; t-3 = -2 \;\Rightarrow\; t = 1$$

Ambos os valores, $t=1$ e $t=5$, pertencem ao intervalo $0 \le t < 12$ (correspondendo à simetria da curva cossenoidal em torno do seu pico em $t=3$, onde $h=5$).

**Conclusão:** altura máxima $=5$ m; altura mínima $=1$ m; período $=12$ h; a maré atinge 4 m em $t=1$ h e $t=5$ h.

## Formalização verificável

- `funcao` — expressão `2*cos(pi*(t/6 - 1/2)) + 3`, esperado `5`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `2*cos(pi*(t/6 - 1/2)) + 3`, esperado `1`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `2*cos(pi*(t/6 - 1/2)) + 3`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `equacao` — expressão `Eq(2*cos(pi*(t/6 - 1/2)) + 3, 4)`, esperado `[1, 5]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (maximo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 5). | (2) aprovado: Gabarito confirmado (minimo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 1). | (3) aprovado: Gabarito confirmado (período 12). | (4) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [5].
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - funcao/periodo=aprovado
  - equacao=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (maximo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 5). | (2) aprovado: Gabarito confirmado (minimo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 1). | (3) aprovado: Gabarito confirmado (período 12). | (4) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [5]. Resultado calculado independentemente: maximo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 5 | minimo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 1 | período 12 | [1, 5]. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (maximo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 5). | (2) aprovado: Gabarito confirmado (minimo de 2*cos(pi*(t/6 - 1/2)) + 3 em Reals: 1). | (3) aprovado: Gabarito confirmado (período 12). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - funcao/periodo=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a função, o domínio de t, as unidades e as quatro grandezas a determinar (máximo, mínimo, período, instantes com h=4). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver o problema.
  - adequacao_nivel: 4/5 — O processo exigido (identificar parâmetros A, B, C, D e aplicá-los em fórmulas de máximo/mínimo/período, além de resolver uma equação trigonométrica simples) é compatível com o nível 'aplicar'. A resposta é multiestrutural (várias sub-respostas obtidas por aplicação direta de fórmulas), o que é coerente com Bloom-aplicar, embora não exija uma etapa de análise integradora entre as partes.
  - alinhamento_bncc: 4/5 — Parte de fenômeno periódico real (maré), e amplitude, período e deslocamento vertical são efetivamente objeto de avaliação (não decorativos), como comprovam os distratores. A menção a 'interpretar o gráfico como curva cossenoidal' atende parcialmente à exigência de comparação com a representação gráfica, mas a resolução é conduzida de forma puramente algébrica, sem exigir do estudante uma leitura ou esboço gráfico explícito — a comparação gráfica fica mais implícita que efetivamente demandada.
  - distratores: 5/5 — Os três distratores representam erros sistemático plausíveis e bem distintos: confundir amplitude com valor máximo/mínimo, errar a fórmula do período (esquecer o fator 2) e obter apenas uma solução da equação trigonométrica por esquecer a simetria do cosseno. Nenhum é absurdo ou trivialmente eliminável.
  - originalidade: 3/5 — O contexto de maré modelada por cosseno é um exemplo clássico e recorrente em livros didáticos de funções trigonométricas, reduzindo a originalidade. Não há efeito Topaze evidente no enunciado (as dicas de erro comum aparecem apenas na resolução, não no enunciado), mas o cenário poderia ser mais inovador ou contextualizado com dados reais/gráficos para maior significância.
