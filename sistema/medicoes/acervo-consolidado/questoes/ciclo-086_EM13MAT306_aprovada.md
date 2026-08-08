# Ciclo 086 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma roda-gigante tem 40 m de diâmetro e seu centro está a 22 m de altura em relação ao solo. Ela gira com velocidade constante, completando uma volta a cada 12 minutos. Um passageiro embarca no ponto mais baixo da roda (rente ao chão de segurança, a 2 m de altura) no instante $t = 0$ minuto. A altura $h(t)$, em metros, desse passageiro em relação ao solo, $t$ minutos após o embarque, pode ser descrita por uma função do tipo cosseno. Considerando o gráfico de $h(t)$ ao longo de todo o primeiro giro completo ($0 \le t \le 12$ min), assinale a alternativa que apresenta corretamente a lei de $h(t)$ e o intervalo de tempo, nesse primeiro giro, em que a altura do passageiro é maior que 32 m.

## Alternativas

- (a) $h(t) = 22 - 20\cos\left(\dfrac{\pi t}{6}\right)$, e a altura é maior que 32 m para $t \in (4, 8)$ minutos.  ← correta
- (b) $h(t) = 22 - 40\cos\left(\dfrac{\pi t}{6}\right)$, e a altura é maior que 32 m para $t \in (4, 8)$ minutos.
  - *erro representado:* Confundiu o diâmetro com o raio, usando a amplitude igual ao diâmetro (40) em vez do raio (20).
- (c) $h(t) = 22 - 20\cos\left(\dfrac{\pi t}{3}\right)$, e a altura é maior que 32 m para $t \in (2, 4)$ minutos.
  - *erro representado:* Calculou o período de forma incorreta, assumindo que a roda completa uma volta em 6 minutos em vez de 12, o que dobra o coeficiente angular do argumento.
- (d) $h(t) = 22 + 20\cos\left(\dfrac{\pi t}{6}\right)$, e a altura é maior que 32 m para $t \in (0, 2) \cup (10, 12)$ minutos.
  - *erro representado:* Assumiu incorretamente que o passageiro embarca no ponto mais alto da roda, usando cosseno positivo em vez de negativo na fase inicial.

## Gabarito

h(t) = 22 - 20cos(πt/6); altura > 32 m para t entre 4 e 8 minutos (alternativa A)

## Resolução

**1. Amplitude:** o raio da roda é metade do diâmetro: $R = 40/2 = 20$ m. Essa é a amplitude do movimento (a amplitude é o raio, não o diâmetro).

**2. Deslocamento vertical:** o centro da roda está a 22 m do solo, então a função oscila em torno de $D = 22$.

**3. Período:** a roda completa uma volta a cada 12 minutos, logo $T = 12$ e o coeficiente angular do argumento é $b = \dfrac{2\pi}{T} = \dfrac{2\pi}{12} = \dfrac{\pi}{6}$.

**4. Fase inicial:** em $t=0$ o passageiro está no ponto **mais baixo**, ou seja, $h(0) = D - R = 22 - 20 = 2$. Como a função cosseno começa em seu valor máximo, usamos o **cosseno negativo** para que o ponto de partida seja o mínimo:
$$h(t) = 22 - 20\cos\left(\frac{\pi t}{6}\right)$$
Confira: $h(0) = 22 - 20(1) = 2$ ✓; $h(6) = 22 - 20(-1) = 42$ (ponto mais alto, na metade da volta) ✓.

**5. Leitura gráfica — altura maior que 32 m:** no gráfico de $h(t)$, essa é uma curva cosseno invertida oscilando entre 2 m (mínimo) e 42 m (máximo), com centro em 22 m. Queremos o intervalo em que a curva fica **acima da reta horizontal $y=32$**.

Resolvendo algebricamente para confirmar a leitura do gráfico:
$$22 - 20\cos\left(\frac{\pi t}{6}\right) > 32 \;\Rightarrow\; \cos\left(\frac{\pi t}{6}\right) < -\frac{1}{2}$$
No intervalo $0 \le t \le 12$ (ou seja, $0 \le \frac{\pi t}{6} \le 2\pi$), o cosseno é menor que $-\tfrac12$ quando o ângulo está entre $120°$ e $240°$:
$$\frac{\pi t}{6} = \frac{2\pi}{3} \Rightarrow t = 4 \qquad \frac{\pi t}{6} = \frac{4\pi}{3} \Rightarrow t = 8$$
Isso corresponde exatamente ao trecho do gráfico em que a curva está no seu 'pico' central, entre os instantes $t=4$ min e $t=8$ min — coerente com a simetria em torno de $t=6$ (o instante do máximo).

**Conclusão:** $h(t) = 22 - 20\cos\left(\dfrac{\pi t}{6}\right)$ e a altura é maior que 32 m para $t \in (4, 8)$ minutos.

## Formalização verificável

- `funcao` — expressão `22 - 20*cos(pi*t/6)`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `22 - 20*cos(pi*t/6)`, esperado `42`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `22 - 20*cos(pi*t/6)`, esperado `2`, parâmetros `{'consulta': 'minimo'}`
- `funcao` — expressão `22 - 20*cos(pi*t/6)`, esperado `32`, parâmetros `{'consulta': 'valor', 'ponto': '4'}`
- `funcao` — expressão `22 - 20*cos(pi*t/6)`, esperado `32`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(4) = 5/2). | (2) aprovado: Gabarito confirmado (período 12). | (3) aprovado: Gabarito confirmado (maximo de 3*cos(pi*x/6) + 4 em Reals: 7). | (4) aprovado: Gabarito confirmado (minimo de 3*cos(pi*x/6) + 4 em Reals: 1).
  - funcao/valor=aprovado
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente os dados (máximo, mínimo, instantes, período), a forma da função e a pergunta final. Não há ambiguidade lexical ou estrutural, e todos os dados necessários para resolver o problema estão presentes.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar um procedimento conhecido (determinar A, ω, k a partir de dados e avaliar a função em um ponto), o que é coerente com o nível 'aplicar' de Bloom. Estruturalmente é multiestrutural (várias etapas integradas), compatível com essa exigência cognitiva e com o Ensino Médio, embora não avance para níveis de análise ou avaliação.
  - alinhamento_bncc: 2/5 — A questão cumpre parcialmente a habilidade: trata de um fenômeno periódico real (maré) e faz da amplitude, período e deslocamento vertical objetos explícitos de cálculo. Porém, a habilidade EM13MAT306 exige explicitamente 'comparar suas representações com as funções seno e cosseno, no plano cartesiano', e a questão não pede nenhuma leitura, esboço ou comparação gráfica — é puramente algébrica/numérica. Essa exigência central da habilidade não é atendida, o que compromete o alinhamento pleno com a BNCC.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: esquecer o deslocamento k, usar amplitude sem dividir por 2, e confundir o período com 24h em vez de 12h. Nenhum é absurdo ou trivialmente eliminável, e cada um mapeia um erro conceitual específico do processo de modelagem.
  - originalidade: 3/5 — O contexto de marés para funções trigonométricas é um dos exemplos mais recorrentes em livros didáticos e situações de vestibular, o que reduz a originalidade. Não há efeito Topaze evidente (os dados não entregam a resposta), mas a estrutura do problema é bastante convencional e previsível para quem já viu esse tipo de exercício.
  - *sugestões:* Incluir na questão uma etapa que exija explicitamente comparar a função obtida com sua representação no plano cartesiano — por exemplo, pedir para identificar em um gráfico fornecido (ou a ser esboçado) qual curva corresponde a h(t), ou perguntar em que intervalo de tempo a altura da água é maior que determinado valor, exigindo leitura gráfica. Isso tornaria a exigência de 'comparar representações no plano cartesiano', prevista na habilidade EM13MAT306, efetivamente atendida, e não apenas o cálculo numérico de h(4). Também seria interessante variar o contexto (evitar o clássico exemplo de marés) para aumentar a originalidade, mantendo a mesma estrutura de cálculo de amplitude, período e deslocamento.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Incluir na questão uma etapa que exija explicitamente comparar a função obtida com sua representação no plano cartesiano — por exemplo, pedir para identificar em um gráfico fornecido (ou a ser esboçado) qual curva corresponde a h(t), ou perguntar em que intervalo de tempo a altura da água é maior que determinado valor, exigindo leitura gráfica. Isso tornaria a exigência de 'comparar representações no plano cartesiano', prevista na habilidade EM13MAT306, efetivamente atendida, e não apenas o cálculo numérico de h(4). Também seria interessante variar o contexto (evitar o clássico exemplo de marés) para aumentar a originalidade, mantendo a mesma estrutura de cálculo de amplitude, período e deslocamento.

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (maximo de 22 - 20*cos(pi*t/6) em Reals: 42). | (3) aprovado: Gabarito confirmado (minimo de 22 - 20*cos(pi*t/6) em Reals: 2). | (4) aprovado: Gabarito confirmado (f(4) = 32). | (5) aprovado: Gabarito confirmado (f(8) = 32).
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado especifica claramente diâmetro, altura do centro, período, ponto de embarque e o que se pede (lei de h(t) e intervalo). Não há ambiguidade nos dados nem na pergunta.
  - adequacao_nivel: 5/5 — A tarefa exige aplicar corretamente os parâmetros (amplitude, deslocamento, período, fase) na construção do modelo e depois resolver uma inequação trigonométrica — processo compatível com 'aplicar' e com estrutura relacional (SOLO), coerente com o nível declarado.
  - alinhamento_bncc: 4/5 — Parte de um fenômeno periódico real (roda-gigante) e usa amplitude, período e deslocamento como elementos centrais, não decorativos. A menção ao 'gráfico de h(t)' sugere articulação com a representação cartesiana, mas a resolução é conduzida quase inteiramente por via algébrica, sem exigir efetivamente que o aluno compare a função com o traçado gráfico (ex.: leitura visual do gráfico fornecido). Poderia reforçar mais explicitamente essa comparação gráfica exigida pela habilidade.
  - distratores: 5/5 — Cada distrator reproduz um erro conceitual plausível e distinto: confundir raio com diâmetro, calcular período errado, e inverter a fase (assumir início no máximo). Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 3/5 — O contexto de roda-gigante para funções trigonométricas é um clássico recorrente em livros didáticos e provas; embora bem construído, não traz elemento inovador de contextualização nem rompe com o padrão usual desse tipo de problema.
