# Ciclo 055 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em um teste de frenagem, a distância de frenagem $d$ (em metros) de um carrinho de brinquedo, em função de sua velocidade $v$ (em m/s, com $v \geq 0$), foi modelada por $d(v) = 0{,}5v^2$.

Em outro experimento, a altura $h$ (em metros) de uma bolinha lançada verticalmente para cima a partir de uma plataforma, em função do tempo $t$ (em segundos, com $t \geq 0$), foi modelada por $h(t) = -5t^2 + 20t + 1$.

Um estudante deseja esboçar, sem construir tabela de valores, o gráfico no plano cartesiano correspondente à situação em que a grandeza dependente é diretamente proporcional ao quadrado da grandeza independente.

Assinale a alternativa que descreve corretamente esse gráfico.

## Alternativas

- (a) Parábola com concavidade voltada para cima, vértice na origem $(0,0)$, simétrica em relação ao eixo vertical e situada no primeiro quadrante para $v \geq 0$, pois $d(v)=0{,}5v^2$ é diretamente proporcional ao quadrado de $v$.  ← correta
- (b) Parábola com concavidade voltada para baixo, vértice no ponto $(2,21)$, interceptando o eixo vertical em $(0,1)$.
  - *erro representado:* Confundir qual das duas situações é diretamente proporcional ao quadrado, atribuindo essa propriedade à função h(t), que na verdade possui termos linear e constante.
- (c) Reta crescente passando pela origem, com coeficiente angular $0{,}5$.
  - *erro representado:* Interpretar 'diretamente proporcional ao quadrado' como proporcionalidade direta simples (linear), ignorando o expoente 2 e tratando d como função de 1º grau de v.
- (d) Parábola com concavidade voltada para cima, vértice no ponto $(0; 0{,}5)$, deslocada verticalmente para cima em relação à origem.
  - *erro representado:* Confundir o coeficiente k=0,5 (que controla a abertura da parábola) com um termo constante que deslocaria o vértice para cima, quando na verdade o vértice permanece na origem.

## Gabarito

A

## Resolução

**Passo 1 — Identificar a proporcionalidade direta ao quadrado.**

Uma grandeza $y$ é diretamente proporcional ao quadrado de $x$ quando $y = kx^2$, ou seja, quando a expressão **não possui** termo linear ($bx$) nem termo constante ($c$).

- $d(v) = 0{,}5v^2$: aqui $b=0$ e $c=0$. Logo, $d$ **é** diretamente proporcional ao quadrado de $v$, com constante $k=0{,}5$.
- $h(t) = -5t^2+20t+1$: aqui $b=20\neq0$ e $c=1\neq0$. Logo, $h$ **não é** diretamente proporcional ao quadrado de $t$.

Portanto, o gráfico pedido é o de $d(v)=0{,}5v^2$.

**Passo 2 — Converter a lei algébrica em características geométricas.**

- Coeficiente do termo quadrático: $a=0{,}5>0$, logo a parábola tem **concavidade voltada para cima**.
- Vértice: $x_v = -\dfrac{b}{2a} = -\dfrac{0}{2(0{,}5)} = 0$ e $y_v = d(0) = 0$. Logo o vértice é o ponto $(0,0)$ — a **origem** do plano cartesiano, o que é característico de toda função da forma $y=kx^2$ (sem deslocamentos).
- Como o domínio físico exige $v\geq 0$, o gráfico corresponde apenas ao ramo direito da parábola, situado no primeiro quadrante (incluindo a origem).

**Passo 3 — Comparar com o gráfico de $h(t)$ (para contraste).**

Para $h(t)=-5t^2+20t+1$: $a=-5<0$ (concavidade para baixo), vértice em $t_v = -\dfrac{20}{2(-5)} = 2$, $h(2) = -20+40+1 = 21$, ou seja, vértice em $(2,21)$, e intersecção com o eixo vertical em $(0,1)$. Esse gráfico **não** representa uma proporcionalidade direta ao quadrado, pois o vértice não está na origem.

**Conclusão:** o gráfico correto é uma parábola com concavidade para cima, vértice na origem, restrita ao primeiro quadrante — alternativa (A).

## Formalização verificável

- `funcao` — expressão `Rational(1,2)*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-5*x**2 + 20*x + 1`, esperado `[2, 21]`, parâmetros `{'consulta': 'vertice'}`
- `propriedade` — expressão `-`, esperado `Rational(1,2)*x**2`, parâmetros `{'forma': 'a*x**2', 'pontos': '[(1, Rational(1,2)), (2, 2), (4, 8)]'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (2, 21)). | (3) aprovado: Propriedades confirmadas para x**2/2: reproduz os 3 pontos dados; forma a*x**2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente duas leis algébricas, define domínio de cada variável e especifica com precisão o critério de escolha (proporcionalidade direta ao quadrado). Não há ambiguidade lexical ou estrutural; os dados são suficientes para resolver sem tabela de valores.
  - adequacao_nivel: 4/5 — O processo exigido (reconhecer a ausência de termos linear/constante, transpor isso para concavidade, vértice e restrição de domínio) é compatível com 'aplicar', exigindo mais que reprodução mecânica. Em termos SOLO, a resposta correta articula múltiplas propriedades relacionadas (relacional), coerente com o nível declarado. Poderia exigir um pouco mais de análise comparativa explícita para se aproximar de 'analisar', mas está adequado ao aplicar.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente as duas exigências: (1) exige trânsito genuíno entre álgebra e geometria, pois a alternativa correta traduz coeficientes em concavidade, vértice e restrição de quadrante, não apenas pede valores numéricos; (2) obriga o estudante a distinguir qual das duas funções é diretamente proporcional ao quadrado, comparando-as em um único problema articulado, não justaposto.
  - distratores: 5/5 — Os três distratores mapeiam erros conceituais distintos e plausíveis: trocar qual função é a proporcional, confundir proporcionalidade quadrática com linear, e confundir o coeficiente k com deslocamento vertical do vértice. Nenhum é absurdo ou eliminável por inspeção superficial.
  - originalidade: 4/5 — Os contextos (frenagem e lançamento vertical) são aplicações físicas relativamente comuns em livros didáticos, mas a comparação simultânea entre duas situações para forçar a distinção conceitual é uma estrutura menos mecânica que o exercício padrão de 'ache o vértice desta parábola'. Não há pistas óbvias que entreguem a resposta (sem efeito Topaze evidente).
