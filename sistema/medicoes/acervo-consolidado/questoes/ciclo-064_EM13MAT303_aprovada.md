# Ciclo 064 — EM13MAT303

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma grandeza positiva $C$ sofre, em cada uma de $n$ etapas sucessivas, um acréscimo percentual constante de taxa $i$ (com $0<i<1$): ao final de cada etapa, o valor da grandeza fica multiplicado por $(1+i)$ em relação ao valor obtido na etapa anterior. Esse é exatamente o modelo de capitalização por juros compostos.

**a)** Deduza, a partir da regra acima, a expressão geral $C_n$ do valor da grandeza após $n$ etapas, em função de $C$, $i$ e $n$. Em seguida, explique por que essa dependência de $C_n$ em relação a $n$ caracteriza um crescimento **exponencial**, e não um crescimento linear (do tipo somar, a cada etapa, um valor fixo igual a $iC$).

**b)** Um colega afirma que, se em duas etapas sucessivas a grandeza recebe acréscimos percentuais de taxas $i_1$ e $i_2$ (não necessariamente iguais), então a taxa percentual única $I$ equivalente às duas etapas combinadas é simplesmente $I = i_1+i_2$. Usando a expressão obtida no item (a), construa a fórmula correta de $I$ em função de $i_1$ e $i_2$, e mostre algebricamente que, sempre que $i_1>0$ e $i_2>0$, tem-se $I > i_1+i_2$.

**c)** Aplicando o modelo do item (a) com uma taxa constante de $i=20\%$ por etapa, determine o menor número inteiro de etapas $n$ necessário para que a grandeza mais que dobre de valor em relação ao valor inicial $C$.

## Gabarito

(a) $C_n = C(1+i)^n$, exponencial pois $n$ está no expoente e a razão entre termos consecutivos é constante e igual a $(1+i)$; (b) $I = i_1+i_2+i_1i_2$, que excede $i_1+i_2$ em $i_1i_2>0$; (c) $n=4$.

## Resolução

**Item (a) — construção da fórmula geral**

Após a etapa 1: $C_1 = C(1+i)$.

Após a etapa 2, o acréscimo incide sobre $C_1$ (e não sobre $C$): $C_2 = C_1(1+i) = C(1+i)^2$.

Repetindo o raciocínio (indução): a cada nova etapa o valor anterior é **multiplicado** pelo mesmo fator $(1+i)$. Logo,
$$C_n = C(1+i)^n.$$

Esse crescimento é exponencial porque a variável $n$ aparece no **expoente**, não como fator multiplicativo de um incremento fixo. Os valores $C, C(1+i), C(1+i)^2, \dots$ formam uma progressão **geométrica** de razão $(1+i)>1$: cada termo é obtido multiplicando o anterior pela mesma constante. Se o crescimento fosse linear, teríamos $C_n = C + n\cdot(iC)$, em que os incrementos absolutos $iC, iC, iC,\dots$ seriam sempre iguais — o que **não** ocorre aqui, pois o incremento absoluto da etapa $n$ é $iC(1+i)^{n-1}$, que cresce a cada etapa. É essa multiplicação repetida pelo mesmo fator (e não a soma repetida da mesma parcela) que define o caráter exponencial do processo.

**Item (b) — taxa equivalente a duas etapas**

Aplicando duas etapas sucessivas de taxas $i_1$ e $i_2$ à fórmula de (a):
$$C_2 = C(1+i_1)(1+i_2).$$

A taxa única equivalente $I$ deve satisfazer $C(1+I) = C(1+i_1)(1+i_2)$, ou seja,
$$1+I = (1+i_1)(1+i_2) = 1 + i_1 + i_2 + i_1 i_2 \;\Rightarrow\; I = i_1+i_2+i_1 i_2.$$

Comparando com a afirmação do colega:
$$I - (i_1+i_2) = i_1 i_2.$$

Se $i_1>0$ e $i_2>0$, então $i_1 i_2>0$, logo $I > i_1+i_2$ estritamente. O erro de simplesmente somar as taxas percentuais ignora o termo $i_1 i_2$, que representa o efeito de o segundo acréscimo incidir também sobre o acréscimo já obtido na primeira etapa — a essência da composição exponencial.

**Item (c) — menor $n$ para mais que dobrar**

Com $i=20\% = \dfrac{1}{5}$, temos $1+i = \dfrac{6}{5}$, e queremos o menor inteiro $n$ tal que
$$C\left(\frac{6}{5}\right)^n > 2C \;\Longleftrightarrow\; \left(\frac{6}{5}\right)^n > 2.$$

Testando valores inteiros:
- $n=3$: $\left(\frac{6}{5}\right)^3 = \dfrac{216}{125} = 1{,}728 < 2$ (ainda não dobrou).
- $n=4$: $\left(\frac{6}{5}\right)^4 = \dfrac{1296}{625} = 2{,}0736 > 2$ (já mais que dobrou).

De fato, resolvendo a igualdade $\left(\frac{6}{5}\right)^n = 2$ obtemos $n = \dfrac{\log 2}{\log(6/5)} \approx 3{,}80$, um valor não inteiro entre 3 e 4; como o crescimento é exponencial (estritamente crescente em $n$), o menor inteiro que satisfaz a desigualdade é o primeiro inteiro maior que $3{,}80$.

Portanto, $n = 4$ etapas.

## Formalização verificável

- `progressao` — expressão `-`, esperado `Rational(216,125)`, parâmetros `{'tipo_progressao': 'pg', 'a1': '1', 'razao': 'Rational(6,5)', 'n': '4', 'consulta': 'termo'}`
- `progressao` — expressão `-`, esperado `Rational(1296,625)`, parâmetros `{'tipo_progressao': 'pg', 'a1': '1', 'razao': 'Rational(6,5)', 'n': '5', 'consulta': 'termo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 216/125). | (2) aprovado: Gabarito confirmado (termo da PG = 1296/625).
  - progressao/termo=aprovado
  - progressao/termo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem delimitado: define a variável C, a taxa i, a sequência de etapas e o que cada item pede (deduzir C_n, comparar com o colega, calcular n). Não há ambiguidade lexical ou lacunas de dados; as condições (0<i<1, i1>0, i2>0) estão explicitadas.
  - adequacao_nivel: 3/5 — A questão mistura níveis cognitivos distintos: o item (a) é essencialmente 'entender/analisar' (deduzir e justificar por que é exponencial), o item (b) é o único que de fato exige 'criar' (construir uma fórmula nova a partir de princípios e demonstrar uma desigualdade), e o item (c) é 'aplicar' (busca por tentativa de valores inteiros). O roteiro é fortemente guiado passo a passo, o que reduz a autonomia esperada de uma tarefa de 'criar' — a estrutura de resposta fica mais próxima de multiestrutural (itens paralelos, cada um resolvido isoladamente) do que relacional/abstrata estendida, que seria o esperado no topo de Bloom.
  - alinhamento_bncc: 4/5 — A questão trabalha explicitamente juros compostos e porcentagem, e o caráter exponencial é tematizado de forma central (item a exige justificar por que não é linear; item b evidencia o termo i1*i2 como assinatura da composição multiplicativa). Não há apenas uma 'conta de porcentagem isolada'. Falta, porém, a dimensão de 'elaborar problemas' prevista na habilidade — a questão é só de resolução, não pede que o aluno formule um problema análogo.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — Evita o enunciado clássico de 'calcule o montante após X anos com taxa Y'; introduz uma generalização (taxas diferentes por etapa) e uma demonstração algébrica, fugindo do automatismo de fórmula. Por outro lado, o contexto é abstrato ('grandeza positiva'), sem ancoragem em situação real (dinheiro, população, etc.), o que reduz a significância contextual esperada pela BNCC para esse tipo de habilidade.
