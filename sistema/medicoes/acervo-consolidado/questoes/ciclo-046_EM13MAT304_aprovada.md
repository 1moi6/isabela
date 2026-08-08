# Ciclo 046 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo monitora o crescimento de uma colônia de bactérias em um meio de cultura controlado. No início da observação ($t=0$), a colônia possui 500 bactérias. Verificou-se experimentalmente que essa população duplica a cada 3 horas, mantendo esse padrão de crescimento durante todo o experimento, que dura pelo menos 24 horas.

a) Elabore a lei da função exponencial $N(t)$ que fornece o número de bactérias em função do tempo $t$, em horas, decorrido desde o início da observação.

b) Utilizando a função obtida, determine o número de bactérias presentes após 9 horas de observação.

c) Um estudante afirmou que, como a população duplica a cada 3 horas, o crescimento percentual da colônia a cada hora deve ser de $\dfrac{100\%}{3}\approx 33{,}3\%$. Mostre que essa afirmação está incorreta, determinando a taxa de crescimento percentual horária real da colônia (isto é, encontre $i$ tal que $N(t) = 500\cdot(1+i)^t$ para todo $t$), e explique por que o raciocínio do estudante falha, considerando o comportamento multiplicativo da função exponencial.

d) Determine depois de quantas horas a população da colônia atingirá 32000 bactérias.

## Gabarito

a) $N(t) = 500\cdot 2^{t/3}$; b) 4000 bactérias; c) $i = 2^{1/3}-1 \approx 26\%$ ao hora — o raciocínio do estudante é inválido pois o crescimento exponencial é multiplicativo, não pode ser dividido linearmente pelo tempo; d) 18 horas.

## Resolução

**a) Construção da lei da função**

Como a população duplica a cada 3 horas, o número de bactérias é multiplicado por 2 sempre que $t$ aumenta em 3 unidades. Isso caracteriza uma função exponencial da forma
$$N(t) = N_0 \cdot 2^{t/3}$$
com $N_0 = 500$ (população inicial). Logo,
$$N(t) = 500\cdot 2^{t/3}.$$

Verificação: $N(0)=500$, $N(3)=500\cdot2=1000$, $N(6)=500\cdot4=2000$ — de fato duplica a cada 3 h.

**b) Valor após 9 horas**

$$N(9) = 500\cdot 2^{9/3} = 500\cdot 2^{3} = 500\cdot 8 = 4000.$$

Após 9 horas, há **4000 bactérias**.

**c) Taxa de crescimento horária real**

Queremos escrever a mesma função na forma $N(t) = 500\cdot(1+i)^t$. Para que essa forma coincida com $500\cdot 2^{t/3}$ para todo $t$, as bases devem ser iguais:
$$(1+i)^t = \left(2^{1/3}\right)^t \;\Rightarrow\; 1+i = 2^{1/3}.$$
Logo,
$$i = 2^{1/3} - 1 \approx 1{,}2599 - 1 = 0{,}2599,$$
ou seja, a colônia cresce aproximadamente **26% a cada hora**, e não 33,3%.

O erro do estudante está em tratar o crescimento como se fosse **distribuído de forma aditiva/linear** ao longo das 3 horas (dividindo os 100% de aumento por 3). Mas o crescimento exponencial é **multiplicativo**: em cada hora a população é multiplicada pelo mesmo fator $2^{1/3}$, e não recebe uma fração fixa do aumento total. Prova disso: se a taxa fosse realmente $33{,}3\%$ ao h, após 3 horas o fator acumulado seria $(1{,}333)^3 \approx 2{,}37$, e não exatamente $2$, como exige o enunciado.

**d) Tempo para atingir 32000 bactérias**

$$500\cdot 2^{t/3} = 32000 \;\Rightarrow\; 2^{t/3} = 64 = 2^{6} \;\Rightarrow\; \frac{t}{3} = 6 \;\Rightarrow\; t = 18.$$

A população atingirá 32000 bactérias após **18 horas**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `500*2**(t/3)`, parâmetros `{'pontos': '[(0,500),(3,1000),(6,2000),(9,4000)]'}`
- `funcao` — expressão `500*2**(t/3)`, esperado `4000`, parâmetros `{'consulta': 'valor', 'ponto': '9'}`
- `funcao` — expressão `500*2**(t/3)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(1+i, 2**(Rational(1,3)))`, esperado `[2**(Rational(1,3)) - 1]`
- `equacao` — expressão `Eq(500*2**(t/3), 32000)`, esperado `[18]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 500*2**(t/3): reproduz os 4 pontos dados. | (2) aprovado: Gabarito confirmado (f(9) = 4000). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (5) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem segmentado em itens, dados completos (N0=500, período de duplicação=3h, duração mínima=24h), pedidos inequívocos em cada alínea. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — O nível declarado é 'criar', mas a exigência cognitiva real é predominantemente 'aplicar' (itens b e d) e 'analisar/avaliar' (item c, que exige justificar por que um raciocínio está errado). O item a), que deveria corresponder à 'elaboração' da lei, é na prática uma tradução quase direta do dado 'duplica a cada 3h' para a forma 2^(t/3) — um padrão-tipo já bastante conhecido em livros didáticos, sem exigir síntese ou produção verdadeiramente original de um modelo. Em termos de SOLO, a resposta esperada é relacional (conecta variação e forma funcional) mas não chega a ser uma estrutura ampliada/abstrata que caracterizaria 'criar' de fato.
  - alinhamento_bncc: 5/5 — Cumpre bem as exigências da EM13MAT304: o item c) obriga o aluno a compreender e interpretar a natureza multiplicativa (não aditiva) da variação exponencial, indo além do cálculo mecânico. O contexto (crescimento de bactérias) é um exemplo explícito de 'seres vivos microscópicos' citado na habilidade. Os itens articulam-se em torno de uma única situação, sem justaposição artificial de subtemas.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de duplicação bacteriana é um clássico recorrente em livros didáticos, reduzindo um pouco a originalidade dos itens a), b) e d). Porém o item c), que expõe e refuta um erro conceitual comum (confundir taxa distribuída linearmente com taxa multiplicativa), é um diferencial pedagógico interessante e evita o efeito Topaze ao exigir que o próprio aluno construa o contra-argumento, em vez de apenas seguir passos guiados.
