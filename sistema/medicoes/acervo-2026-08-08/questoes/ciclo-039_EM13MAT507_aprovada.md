# Ciclo 039 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma fábrica de móveis planeja aumentar sua produção mensal de cadeiras de forma constante. Em janeiro (mês $n=1$) foram produzidas 120 cadeiras. A partir de fevereiro, cada mês produz 15 cadeiras a mais do que o mês anterior, de modo que os valores mensais de produção formam uma progressão aritmética.

a) Escreva a lei de uma função afim $f(n)$, definida para $n$ natural, $n \geq 1$, que forneça o número de cadeiras produzidas no mês $n$, e explique por que essa função representa exatamente a mesma informação da progressão aritmética descrita (isto é, por que $f(n)$ coincide com o termo geral da PA).

b) Determine em que mês a produção mensal atingirá 300 cadeiras.

c) Usando a relação entre a soma dos termos de uma progressão aritmética e a função afim associada, calcule o total de cadeiras produzidas do mês 1 ao mês 12 (inclusive).

## Gabarito

a) $f(n) = 15n + 105$, para $n$ natural, $n \geq 1$, coincidindo com o termo geral da PA de $a_1=120$ e $d=15$; b) mês 13; c) 2430 cadeiras.

## Resolução

**a) Associando a PA à função afim**

A produção mensal forma uma PA de primeiro termo $a_1 = 120$ e razão $d = 15$. O termo geral da PA é:
$$a_n = a_1 + (n-1)d = 120 + 15(n-1) = 15n + 105$$

Como $a_n$ é uma expressão do tipo $an+b$ com $a=15$ e $b=105$, ela coincide exatamente com uma função afim $f(n) = 15n+105$ avaliada nos naturais. Ou seja, a PA é a *restrição da função afim $f(x)=15x+105$ ao domínio discreto* $n \in \mathbb{N}, n\ge 1$ — cada termo da progressão é o valor de $f$ em um número natural, e a razão $d=15$ é exatamente o coeficiente angular (taxa de variação constante) da função afim.

Assim, $f(n) = 15n + 105$, com domínio $\{n \in \mathbb{N} \mid n \geq 1\}$. Verificação: $f(1) = 15+105 = 120$. ✓

**b) Mês em que a produção atinge 300 cadeiras**

Resolvendo $f(n) = 300$:
$$15n + 105 = 300$$
$$15n = 195$$
$$n = 13$$

A produção atingirá 300 cadeiras no mês 13 (ou seja, no mês de janeiro do ano seguinte).

**c) Soma dos 12 primeiros termos**

Como $f$ é afim, o gráfico dos pontos $(n, f(n))$ está alinhado, e a soma dos $n$ primeiros termos de uma PA pode ser calculada por:
$$S_n = \frac{(a_1 + a_n)}{2}\cdot n$$

Calculando $f(12)$:
$$f(12) = 15(12) + 105 = 180 + 105 = 285$$

Então:
$$S_{12} = \frac{(120 + 285)}{2} \cdot 12 = \frac{405}{2}\cdot 12 = 405 \cdot 6 = 2430$$

A fábrica produzirá **2430 cadeiras** entre os meses 1 e 12.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `15*n + 105`, parâmetros `{'sequencia': 'pa', 'a1': '120', 'razao': '15'}`
- `funcao` — expressão `15*n + 105`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `equacao` — expressão `Eq(15*n + 105, 300)`, esperado `[13]`
- `progressao` — expressão `-`, esperado `2430`, parâmetros `{'tipo_progressao': 'pa', 'a1': '120', 'razao': '15', 'n': '12', 'consulta': 'soma'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 15*n + 105: coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) aprovado: Gabarito confirmado (soma da PA = 2430).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - equacao=aprovado
  - progressao/soma=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem definido: dados (a1=120, d=15), domínio explicitado (n natural, n≥1), e os três pedidos (lei da função, mês de determinada produção, soma) são claros e sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O item (a) exige explicitamente justificar por que f(n) coincide com o termo geral da PA, o que demanda análise da relação estrutural entre os dois objetos (não é mera aplicação de fórmula). Os itens (b) e (c) são majoritariamente aplicativos (uniestruturais/multiestruturais em SOLO), o que é esperado para consolidar o item (a), mas o peso relacional do 'analisar' fica concentrado só na parte (a). Ainda assim, no conjunto, a questão sustenta o nível declarado.
  - alinhamento_bncc: 5/5 — Atende exatamente a exigência da especificação: o item (a) pede explicitamente a associação e explicação da coincidência entre PA e função afim com domínio discreto tratado (n natural, n≥1), não apenas a aplicação de fórmulas. Os itens (b) e (c) usam essa articulação de forma orgânica (f(n)=300; soma via f(12)), mantendo os dois temas integrados num único problema, não justapostos.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto (produção de cadeiras em fábrica) é razoavelmente significativo, mas é um contexto genérico e recorrente em livros didáticos para PA. A pergunta (a) evita o efeito Topaze ao exigir explicação, mas o restante da estrutura (calcular termo, calcular soma) segue o roteiro clássico de exercícios de PA sem inovação de abordagem ou dado inesperado.
