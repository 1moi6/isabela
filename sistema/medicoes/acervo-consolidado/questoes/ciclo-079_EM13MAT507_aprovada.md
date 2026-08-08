# Ciclo 079 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma marcenaria iniciou a fabricação de cadeiras artesanais em regime de produção mensal constante. No primeiro mês de operação ($n=1$) foram fabricadas 120 cadeiras. A partir do segundo mês, a quantidade produzida a cada mês aumenta sempre do mesmo valor fixo em relação ao mês anterior, de modo que no quarto mês ($n=4$) a produção atingiu 165 cadeiras. Sabe-se que esse ritmo de crescimento se mantém constante indefinidamente, e que $n$ representa o número do mês de produção ($n = 1, 2, 3, \dots$).

a) Determine a razão da progressão aritmética formada pela produção mensal e escreva a lei de uma função afim $f(n)$ que forneça a quantidade de cadeiras fabricadas no mês $n$, indicando explicitamente o domínio dessa função.

b) Usando a função $f(n)$ obtida, determine em que mês a produção mensal será de 300 cadeiras.

c) Calcule o total de cadeiras fabricadas do 1º ao 10º mês.

## Gabarito

a) $r = 15$; $f(n) = 15n + 105$, com $n \in \mathbb{N}^* = \{1,2,3,\dots\}$. b) 13º mês. c) 1875 cadeiras.

## Resolução

**a) Associando a PA à função afim**

A produção mensal forma uma progressão aritmética, pois cresce sempre da mesma quantidade fixa a cada mês. Temos $a_1 = 120$ e $a_4 = 165$.

Como $a_4 = a_1 + 3r$:
$$165 = 120 + 3r \implies 3r = 45 \implies r = 15$$

O termo geral da PA é:
$$a_n = a_1 + (n-1)r = 120 + 15(n-1) = 15n + 105$$

Como $a_n$ é da forma $f(n) = 15n + 105$, uma expressão linear em $n$ com coeficiente angular $15$ e coeficiente linear $105$, essa é exatamente a lei de uma **função afim**. A diferença essencial em relação a uma função afim de domínio contínuo é que aqui a variável $n$ representa o número do mês, que só assume valores naturais positivos. Logo:
$$f(n) = 15n + 105, \quad n \in \mathbb{N}^* = \{1, 2, 3, \dots\}$$

ou seja, o gráfico de $f$ é formado por pontos isolados (discretos) sobre a reta $y = 15x + 105$, e não por uma reta contínua.

**b) Determinando o mês em que a produção é 300**

Queremos $n$ tal que $f(n) = 300$:
$$15n + 105 = 300$$
$$15n = 195$$
$$n = 13$$

Como $13 \in \mathbb{N}^*$, essa solução é compatível com o domínio discreto da função: a produção de 300 cadeiras ocorre no **13º mês**.

**c) Soma da produção do 1º ao 10º mês**

Usando a fórmula da soma dos $n$ primeiros termos de uma PA:
$$S_{10} = \frac{n}{2}\left(2a_1 + (n-1)r\right) = \frac{10}{2}\left(2\cdot 120 + 9\cdot 15\right)$$
$$S_{10} = 5\left(240 + 135\right) = 5 \cdot 375 = 1875$$

Foram fabricadas **1875 cadeiras** do 1º ao 10º mês.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `15*n + 105`, parâmetros `{'pontos': '[(1,120),(4,165)]', 'grau': '1', 'sequencia': 'pa', 'a1': '120', 'razao': '15'}`
- `funcao` — expressão `15*n + 105`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `equacao` — expressão `Eq(15*n + 105, 300)`, esperado `[13]`
- `progressao` — expressão `-`, esperado `1875`, parâmetros `{'tipo_progressao': 'pa', 'a1': '120', 'razao': '15', 'n': '10', 'consulta': 'soma'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 15*n + 105: reproduz os 2 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) aprovado: Gabarito confirmado (soma da PA = 1875).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - equacao=aprovado
  - progressao/soma=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta dados completos (a1=120, a4=165), define claramente n como número do mês e separa bem os três pedidos (razão/lei da função, mês de produção, soma). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — O enunciado já entrega implicitamente que se trata de uma PA ('aumenta sempre do mesmo valor fixo') e pede sequencialmente razão, lei da função e domínio, o que reduz a exigência analítica para uma aplicação guiada de fórmulas (SOLO multiestrutural). Falta uma exigência que force o aluno a comparar/justificar propriedades (ex.: por que certos valores de produção não seriam atingíveis, ou por que o gráfico não pode ser interpolado continuamente), o que caracterizaria melhor o nível 'analisar'.
  - alinhamento_bncc: 4/5 — A questão cumpre a exigência central da especificação: pede explicitamente a associação entre a PA e a função afim, exigindo que o domínio discreto seja indicado (item a). Os itens b e c usam essa articulação de forma coerente, não como itens isolados. Perde ponto por não exigir do aluno uma reflexão autônoma sobre a natureza discreta do domínio (isso é fornecido pronto na resolução, sugerindo que o enunciado também poderia induzir essa resposta sem exigir raciocínio adicional).
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 3/5 — O contexto de produção em marcenaria é aplicado e minimamente contextualizado, mas a estrutura de resolução (determinar razão → escrever lei → resolver equação → somar termos) é o roteiro clássico de exercícios de PA/função afim de livros didáticos, sem exigir do aluno decisões próprias sobre modelagem ou interpretação crítica do contexto.
