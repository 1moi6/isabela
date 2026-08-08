# Ciclo 062 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma roda-gigante tem raio de 10 m e seu eixo central está a 12 m de altura em relação ao solo. Ela gira em velocidade constante, completando uma volta a cada 40 segundos. No instante $t = 0$ (em segundos), um determinado carrinho está exatamente no ponto mais baixo do movimento circular. A altura $h(t)$, em metros, desse carrinho em relação ao solo, $t$ segundos após o início da contagem do tempo, é dada por:

$$h(t) = 12 - 10\cos\left(\dfrac{\pi t}{20}\right)$$

Imagine o movimento do carrinho representado simultaneamente de duas formas: como um ponto percorrendo o ciclo trigonométrico (com ângulo variando de $0$ a $2\pi$ radianos e voltando a se repetir) e como uma curva no plano cartesiano, com o tempo $t$ no eixo horizontal e a altura $h(t)$ no eixo vertical.

Com base nessa comparação entre as duas representações, responda:

a) Qual é o período da função $h$, ou seja, o tempo necessário para que o carrinho complete uma volta e a altura volte a se repetir? Explique como esse valor se relaciona com o fato de o ciclo trigonométrico ter $2\pi$ radianos.

b) Qual é o domínio da função $h$, considerando que $t$ representa o tempo decorrido desde o início do funcionamento da roda-gigante (que continua girando indefinidamente)?

c) Qual é a imagem da função $h$, ou seja, quais são as menores e maiores alturas atingidas pelo carrinho? Relacione essas alturas com os pontos do ciclo trigonométrico em que $\cos(\theta) = 1$ e $\cos(\theta) = -1$.

## Gabarito

a) Período $T = 40$ s, pois o ângulo $\frac{\pi t}{20}$ percorre $2\pi$ radianos (uma volta completa no ciclo trigonométrico) exatamente quando $t=40$. b) Domínio: $[0,+\infty)$. c) Imagem: $[2,22]$ metros, correspondendo a $\cos(\theta)=1$ (altura mínima, 2 m) e $\cos(\theta)=-1$ (altura máxima, 22 m).

## Resolução

**a) Período**

No ciclo trigonométrico, uma volta completa corresponde a um ângulo de $2\pi$ radianos. Na função dada, o ângulo (argumento do cosseno) é $\theta = \dfrac{\pi t}{20}$.

O período $T$ é o valor de $t$ para o qual esse ângulo completa exatamente $2\pi$:

$$\frac{\pi T}{20} = 2\pi \implies T = \frac{2\pi \cdot 20}{\pi} = 40$$

Ou seja, cada volta completa no ciclo trigonométrico ($2\pi$ radianos) corresponde, no plano cartesiano, a um intervalo de $40$ segundos no eixo $t$ após o qual o gráfico de $h(t)$ se repete. Assim, o **período é $T = 40$ segundos**.

**b) Domínio**

Como $t$ representa o tempo decorrido desde o início do funcionamento, e a roda-gigante continua girando indefinidamente (repetindo o ciclo trigonométrico voltas após voltas), o tempo pode assumir qualquer valor real não negativo. Logo:

$$D = \{t \in \mathbb{R} \mid t \ge 0\} = [0, +\infty)$$

**c) Imagem**

No ciclo trigonométrico, o cosseno de um ângulo varia entre $-1$ e $1$:
- $\cos(\theta) = 1$ ocorre no ponto $(1,0)$ do ciclo (ângulo $0$, $2\pi$, ...), correspondente ao ponto mais próximo do eixo de rotação na direção considerada;
- $\cos(\theta) = -1$ ocorre no ponto $(-1,0)$ do ciclo (ângulo $\pi$), o ponto diametralmente oposto.

Substituindo esses extremos em $h(t) = 12 - 10\cos(\theta)$:

- Quando $\cos(\theta) = 1$: $h = 12 - 10(1) = 2$ (altura mínima, carrinho na base);
- Quando $\cos(\theta) = -1$: $h = 12 - 10(-1) = 22$ (altura máxima, carrinho no topo).

Como o cosseno assume continuamente todos os valores entre $-1$ e $1$ ao longo de cada volta, $h(t)$ assume continuamente todos os valores entre $2$ e $22$. Logo, a **imagem é $[2, 22]$** metros.

## Formalização verificável

- `funcao` — expressão `12 - 10*cos(pi*t/20)`, esperado `40`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `12 - 10*cos(pi*t/20)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `12 - 10*cos(pi*t/20)`, esperado `Interval(2, 22)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 40). | (2) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (imagem de 12 - 10*cos(pi*t/20): Interval(2, 22)).
  - funcao/periodo=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta todos os dados necessários (raio, altura do eixo, período de rotação, condição inicial) e a função já fornecida, deixando claro o que se pede em cada item (período, domínio, imagem). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — As tarefas pedidas (identificar período, domínio e imagem, explicando a relação com o ciclo trigonométrico) são coerentes com o nível 'entender' de Bloom e com uma estrutura relacional na taxonomia SOLO, já que exigem conectar duas representações sem demandar análise crítica ou síntese mais complexa. O item (a), ao pedir explicação da relação entre o argumento do cosseno e as voltas no ciclo, eleva ligeiramente a exigência cognitiva, mas ainda dentro do nível declarado.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente a habilidade EM13MAT404: pede periodicidade, domínio e imagem, e exige explicitamente a comparação entre o ciclo trigonométrico e o plano cartesiano em cada item (relação do ângulo com 2π, extremos do cosseno com pontos do ciclo). Não se reduz a calcular um valor de seno/cosseno isolado.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto da roda-gigante para funções periódicas é um clássico recorrente em livros didáticos de trigonometria, reduzindo a originalidade. Ainda assim, a estrutura de resposta (explicar a relação entre representações) evita ser puramente mecânica, e não há pistas que resolvam diretamente os itens sem raciocínio do aluno.
