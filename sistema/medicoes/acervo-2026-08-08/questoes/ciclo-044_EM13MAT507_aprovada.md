# Ciclo 044 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma progressão aritmética $(a_n)$, com $n \in \mathbb{N}^*=\{1,2,3,\dots\}$, satisfaz $a_3 = 7$ e $a_8 = 27$. Seja $f:\mathbb{N}^*\to\mathbb{R}$ a função afim tal que $f(n)=a_n$ para todo $n$, e seja $g:\mathbb{R}\to\mathbb{R}$ a função afim que possui a mesma lei de $f$, porém definida para todo número real (isto é, $g$ é a extensão contínua de $f$).

a) Determine a lei de $f$ (e, portanto, de $g$), explicitando o domínio de $f$.

b) Calcule o valor real $x$ para o qual $g(x)=0$ e analise, com justificativa, se esse valor corresponde a algum termo da progressão aritmética $(a_n)$.

c) Calcule a soma dos 15 primeiros termos da progressão aritmética.

## Gabarito

a) $f(n) = 4n-5,\ n\in\mathbb{N}^*$ (e $g(x)=4x-5,\ x\in\mathbb{R}$). b) $x=\dfrac{5}{4}$; esse valor não é natural, logo não corresponde a nenhum termo da PA (a sequência nunca vale zero, pois pula de $-1$ para $3$ entre $n=1$ e $n=2$). c) $S_{15}=405$.

## Resolução

**a) Determinação da lei de $f$**

Como $(a_n)$ é uma PA, $a_n = a_1 + (n-1)r$. Usando $a_3=7$ e $a_8=27$:

$$a_8 - a_3 = 5r \implies 27-7=5r \implies r=4$$

$$a_1 = a_3 - 2r = 7 - 8 = -1$$

Logo, $a_n = -1+(n-1)\cdot 4 = 4n-5$.

Como $a_n=f(n)$, a função afim associada à PA é

$$f(n) = 4n-5,\quad n\in\mathbb{N}^*=\{1,2,3,\dots\}$$

O coeficiente angular $4$ é exatamente a razão $r$ da PA, e $f(1)=-1=a_1$, confirmando a associação.

**b) Extensão contínua $g$ e seu zero**

A extensão contínua tem a mesma lei: $g(x)=4x-5$, agora com $x\in\mathbb{R}$.

Zero de $g$:
$$4x-5=0 \implies x=\frac{5}{4}$$

Como o domínio de $f$ (a função que descreve a PA) é apenas $\mathbb{N}^*$, e $\frac{5}{4}$ **não é um número natural**, esse valor não corresponde a nenhum termo da sequência $(a_n)$. Ou seja, embora a reta que estende a PA cruze o eixo $x$ em $x=\dfrac{5}{4}$, a progressão aritmética (definida apenas para índices inteiros positivos) nunca assume o valor zero — seus termos passam de $a_1=-1$ (negativo) diretamente para $a_2=3$ (positivo), sem existir um termo intermediário em $n=1{,}25$.

**c) Soma dos 15 primeiros termos**

Usando a fórmula da soma da PA (equivalente à soma dos valores de $f$ em $n=1,\dots,15$):

$$S_{15} = \frac{15}{2}\big(2a_1 + 14r\big) = \frac{15}{2}\big(2(-1)+14(4)\big) = \frac{15}{2}(-2+56) = \frac{15}{2}\cdot 54 = 405$$

Portanto $S_{15}=405$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*n - 5`, parâmetros `{'pontos': '[(3,7),(8,27)]', 'grau': '1', 'sequencia': 'pa', 'a1': '-1', 'razao': '4'}`
- `funcao` — expressão `4*x - 5`, esperado `[Rational(5,4)]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `4*n - 5`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `progressao` — expressão `-`, esperado `405`, parâmetros `{'tipo_progressao': 'pa', 'a1': '-1', 'razao': '4', 'n': '15', 'consulta': 'soma'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*n - 5: reproduz os 2 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (zeros da função: [5/4]). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (4) aprovado: Gabarito confirmado (soma da PA = 405).
  - propriedade=aprovado
  - funcao/zeros=aprovado
  - funcao/dominio=aprovado
  - progressao/soma=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (a3, a8), definições precisas de f e g, domínios explicitados e perguntas claramente delimitadas em três itens sem ambiguidade.
  - adequacao_nivel: 4/5 — O item (b) exige análise genuína (comparar domínios, justificar por que o zero da extensão contínua não corresponde a termo da PA), compatível com 'analisar' e com estrutura relacional (SOLO). Porém os itens (a) e (c) são majoritariamente aplicação direta de fórmulas, o que reduz o nível cognitivo médio da questão como um todo.
  - alinhamento_bncc: 5/5 — A questão articula explicitamente PA e função afim: pede a lei de f com domínio discreto, depois a extensão contínua g, e exige justificar por que um valor real de g não corresponde a termo da PA — isso é exatamente a análise de domínio discreto vs. contínuo exigida pela habilidade, não apenas aplicação de fórmula.
  - distratores: 5/5 — Não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — A ideia de comparar f (discreta) com sua extensão contínua g e investigar o zero é pouco comum em livros didáticos tradicionais, trazendo reflexão conceitual real. Os itens (a) e (c), no entanto, seguem roteiro bastante convencional de PA.
