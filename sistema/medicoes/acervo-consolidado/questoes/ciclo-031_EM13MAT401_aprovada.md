# Ciclo 031 — EM13MAT401

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

No plano cartesiano, as retas $r$ e $s$ representam, respectivamente, as funções polinomiais do 1º grau $f$ e $g$. A reta $r$ passa pela origem do sistema e pelo ponto $(3,6)$. A reta $s$ é paralela a $r$ e intercepta os eixos coordenados formando, com eles, um triângulo de área igual a 4 unidades de área, situado inteiramente no quarto quadrante (ou seja, com um vértice sobre o semieixo positivo das abscissas e outro sobre o semieixo negativo das ordenadas, além da origem).

a) Determine a lei de $f$ e classifique-a quanto à proporcionalidade, justificando pela posição geométrica da reta $r$.

b) Determine a lei de $g$. Nos seus cálculos aparecerão duas possibilidades para o coeficiente que desloca a reta; explique, usando a condição sobre o quadrante em que o triângulo deve estar, por que apenas uma delas é válida.

c) Classifique $g$ quanto à proporcionalidade e explique, em termos geométricos, por que a reta $s$ não passa pela origem.

## Gabarito

f(x) = 2x (proporcional); g(x) = 2x - 4 (afim não proporcional, pois b = -4 ≠ 0)

## Resolução

**a) Determinação de $f$**

Como $r$ passa pela origem $(0,0)$ e por $(3,6)$, o coeficiente angular é
$$a = \frac{6-0}{3-0} = 2.$$
Como a reta passa pela origem, o coeficiente linear é $b=0$, logo
$$f(x) = 2x.$$
Geometricamente, toda reta que passa pela origem representa uma função **proporcional** (caso particular da função afim com $b=0$).

**b) Determinação de $g$**

Como $s$ é paralela a $r$, tem o mesmo coeficiente angular $a=2$:
$$g(x) = 2x + b.$$

Os pontos onde $s$ corta os eixos são:
- eixo $y$: $x=0 \Rightarrow y=b$, ponto $(0,b)$;
- eixo $x$: $y=0 \Rightarrow x=-\dfrac{b}{2}$, ponto $\left(-\dfrac{b}{2},0\right)$.

Esses dois pontos, junto com a origem, formam um triângulo retângulo de área
$$A = \frac{1}{2}\cdot|b|\cdot\left|\frac{b}{2}\right| = \frac{b^2}{4}.$$

Impondo $A=4$:
$$\frac{b^2}{4}=4 \Rightarrow b^2=16 \Rightarrow b=4 \text{ ou } b=-4.$$

**Análise geométrica dos dois casos:**

- Se $b=4$: os interceptos são $(0,4)$ e $(-2,0)$ — o triângulo fica no **primeiro** quadrante (vértices com $x\le 0$ e $y\ge 0$, ou seja, no segundo quadrante na verdade). Isso não corresponde ao quarto quadrante exigido.
- Se $b=-4$: os interceptos são $(0,-4)$ e $(2,0)$ — o triângulo tem vértices $(0,0)$, $(2,0)$ e $(0,-4)$, com $x\ge 0$ e $y\le 0$, exatamente no **quarto quadrante**, como pedido.

Logo, a única solução compatível com a condição geométrica é $b=-4$, e
$$g(x) = 2x - 4.$$

Verificação da área: $A=\dfrac{1}{2}\cdot 2\cdot 4 = 4$ ✓.

**c) Classificação de $g$**

Como $b=-4\neq 0$, $g$ é uma função afim **não proporcional**. Geometricamente, a reta $s$ corta o eixo $y$ no ponto $(0,-4)$, diferente da origem — por isso ela não passa pelo ponto $(0,0)$, ao contrário de $r$, que representa a função proporcional $f$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `2*x`, parâmetros `{'pontos': '[(0,0),(3,6)]', 'grau': '1', 'forma': 'a*x'}`
- `funcao` — expressão `2*x`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `propriedade` — expressão `-`, esperado `2*x - 4`, parâmetros `{'pontos': '[(0,-4),(2,0)]', 'grau': '1', 'forma': 'a*x + b'}`
- `funcao` — expressão `2*x - 4`, esperado `[2]`, parâmetros `{'consulta': 'zeros'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 2*x: reproduz os 2 pontos dados; grau 1; forma a*x. | (2) aprovado: Gabarito confirmado (zeros da função: [0]). | (3) aprovado: Propriedades confirmadas para 2*x - 4: reproduz os 2 pontos dados; grau 1; forma a*x + b. | (4) aprovado: Gabarito confirmado (zeros da função: [2]).
  - propriedade=aprovado
  - funcao/zeros=aprovado
  - propriedade=aprovado
  - funcao/zeros=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente os dados (ponto da reta r, paralelismo, área do triângulo, quadrante) e o que é pedido em cada item. Não há ambiguidade lexical ou estrutural; a explicação parenatética sobre o quarto quadrante reforça a compreensão sem introduzir ruído.
  - adequacao_nivel: 4/5 — O processo central (obter coeficientes, escrever a lei, calcular área) é de aplicação direta de fórmulas, coerente com Bloom 'aplicar'. Contudo, os itens (b) e (c) exigem justificativa geométrica sobre por que uma das duas soluções é descartada e por que a reta não passa pela origem, o que se aproxima de um nível relacional (SOLO) mais próximo de 'analisar'. Isso não invalida a questão, mas indica que a exigência cognitiva real é um pouco superior ao nível declarado.
  - alinhamento_bncc: 5/5 — A questão exige transitar entre a forma algébrica (f(x)=2x, g(x)=2x+b) e a representação geométrica (posição da reta, interceptos, área do triângulo), cumprindo exatamente o que a habilidade EM13MAT401 pede. Além disso, força explicitamente a distinção entre o caso proporcional (r) e o caso afim não proporcional (s), articulando os dois conceitos em um único problema coerente, não apenas justapondo itens isolados.
  - distratores: 5/5 — não se aplica
  - originalidade: 4/5 — Embora o tema (retas paralelas e área do triângulo formado com os eixos) seja um clássico de livro didático, a condição adicional sobre o quadrante em que o triângulo deve estar introduz uma camada de decisão não trivial, evitando o efeito Topaze ao exigir que o aluno descarte uma solução algebricamente válida por argumento geométrico. Falta, porém, um contexto aplicado ou motivação além do puramente matemático, o que limita a originalidade.
