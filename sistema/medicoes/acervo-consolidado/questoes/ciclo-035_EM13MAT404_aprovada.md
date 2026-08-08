# Ciclo 035 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Ao girar um ponto sobre o ciclo trigonométrico (circunferência de raio 1 centrada na origem), sua ordenada varia continuamente entre $-1$ e $1$, repetindo os mesmos valores a cada volta completa de $2\pi$ radianos. Essa ordenada é justamente o valor de $\sin(x)$ representado no plano cartesiano. Considere agora a função $f(x) = 3\sin(x) - 1$, definida para todo número real $x$. Com base na relação entre o que ocorre no ciclo trigonométrico e o comportamento do gráfico de $f$ no plano cartesiano, assinale a alternativa que indica corretamente o domínio, o período e a imagem de $f$.

## Alternativas

- (a) Domínio $\mathbb{R}$, período $2\pi$, imagem $[-4, 2]$  ← correta
- (b) Domínio $\mathbb{R}$, período $2\pi$, imagem $[-1, 1]$
  - *erro representado:* Usa apenas a imagem do seno básico observada no ciclo trigonométrico, esquecendo de aplicar a multiplicação por 3 e o deslocamento de -1 sobre o intervalo.
- (c) Domínio $\mathbb{R}$, período $6\pi$, imagem $[-4, 2]$
  - *erro representado:* Confunde o coeficiente que multiplica o valor do seno (amplitude) com um coeficiente que multiplicaria o ângulo x, aplicando erroneamente o fator 3 ao período em vez de apenas à amplitude.
- (d) Domínio $\mathbb{R}$, período $2\pi$, imagem $[-2, 4]$
  - *erro representado:* Inverte o sinal do deslocamento vertical, somando 1 em vez de subtrair 1 ao transportar o intervalo [-3,3] para a imagem final.

## Gabarito

Domínio $\mathbb{R}$, período $2\pi$, imagem $[-4, 2]$

## Resolução

**Passo 1 — Domínio.** No ciclo trigonométrico, o ponto pode girar indefinidamente, para qualquer ângulo $x$ (positivo, negativo ou nulo), sem restrição. Logo, $\sin(x)$ está definido para todo $x$ real, e como $f(x)=3\sin(x)-1$ é obtida por operações que não restringem esse domínio, $D(f) = \mathbb{R}$.

**Passo 2 — Período.** No ciclo trigonométrico, a ordenada do ponto repete seus valores a cada volta completa, ou seja, a cada $2\pi$ radianos, pois o argumento de $\sin$ em $f(x)=3\sin(x)-1$ é simplesmente $x$ (não há fator multiplicando $x$ dentro do seno). Multiplicar o resultado do seno por $3$ e subtrair $1$ apenas estica e desloca verticalmente o gráfico no plano cartesiano — não altera a rapidez com que o ponto completa uma volta no ciclo. Portanto, o período continua sendo $T = 2\pi$.

**Passo 3 — Imagem.** No ciclo trigonométrico, a ordenada satisfaz $-1 \le \sin(x) \le 1$. Multiplicando por $3$: $-3 \le 3\sin(x) \le 3$. Subtraindo $1$ de cada parte da desigualdade (deslocamento vertical do gráfico no plano cartesiano): $-3-1 \le 3\sin(x)-1 \le 3-1$, ou seja, $-4 \le f(x) \le 2$. Logo, a imagem é $[-4, 2]$.

**Conclusão:** $D(f)=\mathbb{R}$, $T=2\pi$, $Im(f)=[-4,2]$.

## Formalização verificável

- `funcao` — expressão `3*sin(x) - 1`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `3*sin(x) - 1`, esperado `2*pi`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `3*sin(x) - 1`, esperado `Interval(-4, 2)`, parâmetros `{'consulta': 'imagem', 'dominio': 'S.Reals'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de 3*sin(x) - 1: Reals). | (2) aprovado: Gabarito confirmado (período 2*pi). | (3) aprovado: Gabarito confirmado (imagem de 3*sin(x) - 1: Interval(-4, 2)).
  - funcao/dominio=aprovado
  - funcao/periodo=aprovado
  - funcao/imagem=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente a função, o contexto do ciclo trigonométrico e pede explicitamente domínio, período e imagem. Não há ambiguidade nos dados ou na pergunta.
  - adequacao_nivel: 4/5 — A tarefa exige compreender como as transformações (amplitude e deslocamento vertical) afetam domínio, período e imagem, o que é coerente com o nível 'entender' de Bloom. A estrutura de resposta é multiestrutural (três características determinadas separadamente), compatível com esse nível, embora não exija integração mais profunda (relacional) entre elas.
  - alinhamento_bncc: 4/5 — A questão de fato usa a comparação entre o ciclo trigonométrico (ordenada do ponto) e o plano cartesiano (gráfico de f) para justificar domínio, período e imagem, atendendo à habilidade EM13MAT404. Não se restringe a calcular um valor de seno, mas mobiliza a relação pedida. Poderia explorar mais explicitamente o papel do ciclo na determinação do período (ex.: variação do argumento), mas o vínculo está presente e não é mera decoração.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e distintos: (1) ignorar a transformação da imagem, (2) confundir amplitude com fator de frequência no período, (3) inverter o sinal do deslocamento vertical. Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 3/5 — Apesar da explicação contextual sobre o ciclo trigonométrico, a tarefa final (determinar domínio, período e imagem de a·sen(x)+b) é um exercício clássico e recorrente em livros didáticos, sem elemento de contexto significativo ou aplicação não convencional.
