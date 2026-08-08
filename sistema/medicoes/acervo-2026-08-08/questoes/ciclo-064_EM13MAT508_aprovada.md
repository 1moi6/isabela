# Ciclo 064 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma bióloga monitora o crescimento de uma cultura de bactérias em um experimento de laboratório. No início da primeira hora de observação ($n = 1$), a cultura possui 200 bactérias. A cada hora que passa, o número de bactérias triplica em relação à hora anterior.

a) Escreva os três primeiros termos da sequência $(a_n)$ que representa o número de bactérias na $n$-ésima hora de observação, classifique essa sequência (PA ou PG) e indique sua razão.

b) Determine o termo geral $a_n$ dessa sequência e calcule quantas bactérias haverá na 7ª hora de observação.

c) Um colega da bióloga propõe representar esse crescimento pela função exponencial $f(x) = 200 \cdot 3^{x-1}$, definida para todo número real positivo $x$. Explique por que $f$ pode modelar o crescimento contínuo da cultura, qual é o domínio de $f$, e por que o domínio da sequência $(a_n)$ é apenas o conjunto dos números naturais não nulos (isto é, por que $(a_n)$ pode ser vista como uma restrição de $f$ aos naturais). Em seguida, verifique que $f(7) = a_7$.

## Gabarito

a) PG de razão 3, com $a_1=200, a_2=600, a_3=1800$. b) $a_n = 200\cdot 3^{n-1}$; $a_7 = 145800$. c) Domínio de $f$: $x>0$ (reais positivos); domínio de $(a_n)$: $n\in\mathbb{N}^*$, pois $(a_n)$ é a restrição de $f$ aos naturais ($a_n=f(n)$); $f(7)=145800=a_7$.

## Resolução

**a) Termos e classificação**

Como a cada hora o número de bactérias triplica em relação à hora anterior, temos:

$a_1 = 200$

$a_2 = 3 \cdot 200 = 600$

$a_3 = 3 \cdot 600 = 1800$

Como cada termo é obtido multiplicando o anterior por uma constante ($q = \dfrac{a_2}{a_1} = \dfrac{600}{200} = 3$, e $\dfrac{a_3}{a_2} = \dfrac{1800}{600} = 3$), a sequência $(a_n)$ é uma **progressão geométrica (PG)** de razão $q = 3$.

**b) Termo geral e valor na 7ª hora**

O termo geral de uma PG é $a_n = a_1 \cdot q^{n-1}$. Substituindo $a_1 = 200$ e $q = 3$:

$a_n = 200 \cdot 3^{n-1}$

Para $n = 7$:

$a_7 = 200 \cdot 3^{6} = 200 \cdot 729 = 145800$

Ou seja, haverá **145.800 bactérias** na 7ª hora de observação.

**c) Associação com a função exponencial**

A função $f(x) = 200 \cdot 3^{x-1}$ tem a mesma lei de formação do termo geral da PG, trocando o índice discreto $n$ pela variável contínua $x$. Como $x$ pode assumir qualquer número real positivo (por exemplo, $x = 2{,}5$, representando 1,5 hora após o início), $f$ descreve uma curva exponencial contínua que **passa exatamente pelos pontos da sequência** sempre que $x$ é um número natural não nulo.

O domínio de $f$ é $x > 0$, ou seja, $(0, +\infty)$, pois foi definida para todo real positivo.

Já a sequência $(a_n)$ só faz sentido para $n \in \mathbb{N}^*$ ($n = 1, 2, 3, \dots$), pois "horas de observação" são contadas em unidades inteiras — não há, no contexto do problema discreto, uma "1,5ª hora de observação" enumerada. Assim, $(a_n)$ é a **restrição de $f$ ao conjunto dos naturais não nulos**: $a_n = f(n)$.

Verificação: $f(7) = 200 \cdot 3^{7-1} = 200 \cdot 3^6 = 200 \cdot 729 = 145800$, que coincide com $a_7 = 145800$ calculado no item (b), confirmando a associação entre a PG e a função exponencial.

## Formalização verificável

- `progressao` — expressão `-`, esperado `145800`, parâmetros `{'tipo_progressao': 'pg', 'a1': '200', 'razao': '3', 'n': '7', 'consulta': 'termo'}`
- `propriedade` — expressão `-`, esperado `200*3**(n-1)`, parâmetros `{'sequencia': 'pg', 'a1': '200', 'razao': '3'}`
- `funcao` — expressão `200*3**(x-1)`, esperado `145800`, parâmetros `{'consulta': 'valor', 'ponto': '7'}`
- `funcao` — expressão `200*3**(x-1)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 145800). | (2) aprovado: Propriedades confirmadas para 200*3**(n - 1): coincide com a PG declarada. | (3) aprovado: Gabarito confirmado (f(7) = 145800). | (4) aprovado: Gabarito confirmado (domínio Interval.open(0, oo) — restrição de contexto dentro do domínio máximo Interval(-oo, oo)).
  - progressao/termo=aprovado
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado define claramente os dados (200 bactérias, taxa de triplicação, n=1 na primeira hora) e as três tarefas são bem delimitadas. Há uma pequena redundância no item c: o domínio de f (reais positivos) já é dado explicitamente na definição de f no corpo do enunciado, mas depois se pede 'qual é o domínio de f', o que pode causar uma leve confusão sobre se a resposta deve ser apenas repetir o dado ou justificá-lo. Não há ambiguidade grave.
  - adequacao_nivel: 4/5 — Os itens a) e b) são de fato 'aplicar' (uso direto de fórmulas de PG), compatíveis com estrutura SOLO multiestrutural. O item c), no entanto, pede explicações e justificativas ('explique por que', 'por que o domínio é apenas...') que exigem raciocínio relacional/comparativo, mais próximo de 'entender/analisar' do que de 'aplicar' no sentido estrito de Bloom. Isso não invalida a questão, mas indica que o nível cognitivo efetivamente demandado no item c é ligeiramente superior ao declarado, embora ainda compatível com o objetivo de 'identificar e associar' da habilidade.
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as exigências da EM13MAT508: articula explicitamente PG e função exponencial (item c), exige tratamento do domínio discreto vs. contínuo (diferença entre N* e R+), e pede verificação numérica da relação a_n = f(n). Não se trata de itens justapostos: o item c depende dos resultados de a) e b) para fechar a articulação, cumprindo a exigência de que os temas sejam realmente integrados num único problema.
  - distratores: 5/5 — não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de crescimento bacteriano é um clássico do gênero, mas o enunciado vai além do padrão ao exigir explicitamente a justificativa da diferença de domínios entre a sequência e a função associada, o que não é comum em exercícios de livro didático tradicionais sobre PG. Evita o efeito Topaze ao não entregar a resposta pronta sobre por que os domínios diferem, exigindo elaboração própria do aluno.
