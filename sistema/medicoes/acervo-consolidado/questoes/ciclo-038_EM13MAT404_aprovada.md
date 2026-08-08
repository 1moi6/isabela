# Ciclo 038 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma roda-gigante tem 15 m de raio e seu centro está fixado a 17 m do solo. Ela gira com velocidade angular constante, completando uma volta inteira a cada 40 segundos. Uma passageira embarca no ponto mais baixo da roda (o ponto da circunferência mais próximo do chão) no instante $t=0$, e a roda gira continuamente a partir daí. Associando o movimento circular da cabine ao ciclo trigonométrico — em que o ângulo percorrido a partir do ponto mais baixo corresponde a $\theta(t)=\dfrac{2\pi}{40}t$ — a altura $h(t)$, em metros, da cabine em relação ao solo, $t$ segundos após o embarque, é dada por
$$h(t) = 17 - 15\cos\left(\frac{2\pi}{40}t\right).$$
Considerando a correspondência entre o percurso da cabine no ciclo trigonométrico e o gráfico de $h(t)$ no plano cartesiano, identifique a alternativa que apresenta corretamente o período do movimento, o domínio de $h$ (levando em conta que $t$ representa o tempo decorrido desde o embarque, com a roda girando indefinidamente) e a imagem de $h$ (a faixa de alturas atingidas pela cabine).

## Alternativas

- (a) Período de 40 s; domínio $t \in [0, +\infty)$; imagem $[2, 32]$ metros.  ← correta
- (b) Período de 40 s; domínio $t \in [0, +\infty)$; imagem $[-15, 15]$ metros.
  - *erro representado:* Confunde a amplitude do movimento (raio do ciclo) com a imagem da função, esquecendo de somar o deslocamento vertical do centro do ciclo (17 m) à faixa de variação do cosseno.
- (c) Período de $\dfrac{\pi}{20}$ s; domínio $t \in [0, +\infty)$; imagem $[2, 32]$ metros.
  - *erro representado:* Erra o cálculo do período ao inverter a relação entre o coeficiente do argumento e o período, calculando $B$ no lugar de $\dfrac{2\pi}{B}$ (usa $2\pi/40$ como se já fosse o período, sem resolver a equação $2\pi t/40=2\pi$).
- (d) Período de 40 s; domínio $t \in [0, 40]$; imagem $[2, 32]$ metros.
  - *erro representado:* Confunde o domínio da função com o intervalo correspondente a uma única volta (um período), não percebendo que a roda continua girando indefinidamente e que $t$ pode assumir qualquer valor não negativo.

## Gabarito

A

## Resolução

**1. Relacionando o ciclo trigonométrico ao movimento**

No ciclo trigonométrico, o cosseno de um ângulo $\theta$ varia entre $-1$ e $1$ conforme o ponto percorre a circunferência de raio $1$. Aqui, a cabine percorre uma circunferência de raio $15$ m centrada a $17$ m do solo, e o ângulo percorrido no instante $t$ é $\theta(t) = \dfrac{2\pi}{40}t$. Como a passageira embarca no ponto mais baixo (onde $\cos\theta = 1$ dá a altura mínima), a altura é modelada por $h(t) = 17 - 15\cos\theta(t)$: o sinal negativo garante que, em $\theta=0$, tenhamos $h(0)=17-15=2$ m (ponto mais baixo).

**2. Período**

No ciclo trigonométrico, uma volta completa corresponde a $\theta$ variar de $0$ a $2\pi$. Isso ocorre quando
$$\frac{2\pi}{40}t = 2\pi \;\Rightarrow\; t = 40.$$
Ou seja, transportando o período fundamental $2\pi$ do cosseno (no ciclo) para o eixo $t$ (no plano cartesiano) através do fator de escala $\frac{2\pi}{40}$, obtém-se o período $T = 40$ segundos — o tempo de uma volta completa da roda.

**3. Domínio**

Como $t$ representa o tempo decorrido a partir do embarque e a roda continua girando indefinidamente (não para após uma volta), os valores possíveis de $t$ são todos os números reais não negativos:
$$\text{Dom}(h) = [0, +\infty).$$

**4. Imagem**

No ciclo trigonométrico, $\cos\theta \in [-1,1]$. Logo:
$$-1 \le \cos\theta(t) \le 1 \;\Rightarrow\; -15 \le -15\cos\theta(t) \le 15 \;\Rightarrow\; 2 \le 17-15\cos\theta(t) \le 32.$$
Portanto a imagem de $h$ é o intervalo $[2, 32]$ metros — a altura mínima ($2$ m, ponto mais baixo) e a máxima ($32$ m, ponto mais alto), obtidas somando/subtraindo o raio (amplitude) à altura do centro do ciclo.

**Conclusão:** Período $=40$ s; Domínio $=[0,+\infty)$; Imagem $=[2,32]$ m — alternativa A.

## Formalização verificável

- `funcao` — expressão `17 - 15*cos(2*pi*x/40)`, esperado `40`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `17 - 15*cos(2*pi*x/40)`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `17 - 15*cos(2*pi*x/40)`, esperado `Interval(2, 32)`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval(0, oo)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 40). | (2) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (imagem de 17 - 15*cos(pi*x/20): Interval(2, 32)).
  - funcao/periodo=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado especifica claramente raio, altura do centro, período de giro, ponto de embarque e fornece explicitamente a função h(t). Não há ambiguidade quanto ao que é pedido (período, domínio, imagem) nem quanto às condições do problema.
  - adequacao_nivel: 3/5 — A questão fornece a função pronta e pede que se extraiam três características por aplicação direta de fórmulas conhecidas (T=2π/B, imagem = centro±amplitude, domínio conforme contexto). Isso corresponde mais a 'aplicar' um procedimento memorizado do que a 'analisar' — não há decomposição, comparação de relações ou justificativa que exija diferenciar elementos inter-relacionados além do cálculo mecânico de cada característica isoladamente. Em termos SOLO, a resposta esperada é multiestrutural (três cálculos paralelos), não relacional, o que fica aquém do nível 'analisar' declarado.
  - alinhamento_bncc: 4/5 — A questão cumpre as exigências pontuais: pede periodicidade, domínio e imagem (não pede calcular seno/cosseno de um ângulo isolado) e menciona explicitamente a associação entre ciclo trigonométrico e plano cartesiano tanto no enunciado quanto na resolução, articulando os dois registros dentro de um único problema aplicado (roda-gigante). O único ponto que impede nota 5 é que a comparação ciclo-plano aparece mais como justificativa retórica na resolução do que como algo que o aluno precisa efetivamente mobilizar para responder — ele pode resolver usando apenas as fórmulas algébricas sem de fato 'comparar representações'.
  - distratores: 5/5 — Os três distratores correspondem a erros sistemáticos plausíveis e comuns: confundir amplitude com imagem, inverter a relação entre coeficiente angular e período, e confundir domínio da função com o intervalo de uma única volta. Nenhum é absurdo ou trivialmente eliminável, e todos exigem que o aluno tenha compreensão real dos conceitos para descartá-los.
  - originalidade: 3/5 — O contexto de roda-gigante para funções trigonométricas é um clássico recorrente em livros didáticos e ENEM, reduzindo a novidade do problema. A articulação explícita com o ciclo trigonométrico dá algum diferencial pedagógico, mas a estrutura geral (dar a função pronta e pedir T, domínio, imagem) é bastante previsível e não evita certo 'efeito Topaze', já que a resolução praticamente entrega o caminho passo a passo já na formulação do problema.
