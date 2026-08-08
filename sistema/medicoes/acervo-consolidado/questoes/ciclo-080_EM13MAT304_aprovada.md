# Ciclo 080 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um laboratório de microbiologia monitora duas culturas de bactérias mantidas em condições ideais de nutrientes e temperatura, iniciando a contagem no instante $t=0$ (em horas).

- A **Cultura A** parte de 500 bactérias e duplica sua população a cada 3 horas, sendo modelada por $P_A(t) = 500 \cdot 2^{t/3}$.
- A **Cultura B** parte de 8000 bactérias e duplica sua população a cada 6 horas, sendo modelada por $P_B(t) = 8000 \cdot 2^{t/6}$.

Embora a Cultura B comece com uma população 16 vezes maior que a Cultura A, o pesquisador responsável afirma que, depois de certo tempo, a Cultura A ultrapassará a Cultura B e permanecerá com mais bactérias dali em diante, para sempre.

a) Determine o instante $t$ (em horas) em que as duas culturas apresentam exatamente a mesma quantidade de bactérias.

b) Sem calcular os valores das populações em instantes específicos, explique — comparando os tempos de duplicação (ou as taxas de crescimento) das duas culturas — por que, a partir do instante encontrado no item (a), a Cultura A permanecerá **para sempre** com mais bactérias que a Cultura B.

c) Confirme numericamente a afirmação do pesquisador calculando $P_A(30)$ e $P_B(30)$, isto é, as populações das duas culturas 30 horas após o início do experimento.

## Gabarito

a) $t = 24$ horas. b) Como a taxa de crescimento relativo de A ($\ln 2/3$) é maior que a de B ($\ln 2/6$), a razão $P_A(t)/P_B(t) = \frac{1}{16}\cdot 2^{t/6}$ é uma exponencial crescente que vale 1 em $t=24$h e cresce indefinidamente para $t>24$h; logo A ultrapassa B nesse instante e permanece maior para sempre. c) $P_A(30)=512000$ e $P_B(30)=256000$, confirmando que $P_A(30) > P_B(30)$.

## Resolução

**a) Igualando as populações**

$$500 \cdot 2^{t/3} = 8000 \cdot 2^{t/6}$$

Dividindo ambos os lados por $500 \cdot 2^{t/6}$:

$$2^{t/3 - t/6} = \frac{8000}{500} = 16$$

Como $\frac{t}{3} - \frac{t}{6} = \frac{t}{6}$, temos:

$$2^{t/6} = 16 = 2^4 \;\Rightarrow\; \frac{t}{6} = 4 \;\Rightarrow\; t = 24 \text{ horas}$$

Nesse instante, ambas as culturas têm $P_A(24)=500\cdot 2^8 = 128000$ bactérias, o mesmo valor de $P_B(24) = 8000\cdot 2^4 = 128000$.

**b) Interpretando as taxas de crescimento**

O tempo de duplicação da Cultura A é 3 horas, enquanto o da Cultura B é 6 horas — ou seja, A dobra sua população **duas vezes mais rápido** que B. Isso significa que a taxa exponencial de crescimento de A, $\frac{\ln 2}{3}$, é maior que a de B, $\frac{\ln 2}{6}$.

Para entender o comportamento da razão entre as populações, escrevemos:

$$\frac{P_A(t)}{P_B(t)} = \frac{500}{8000}\cdot 2^{t/3 - t/6} = \frac{1}{16}\cdot 2^{t/6}$$

Essa razão é uma função exponencial crescente de $t$ (pois a base $2>1$ e o expoente $t/6$ cresce com $t$). Em $t=24$ h, a razão vale exatamente 1 (populações iguais). Como a razão é estritamente crescente para todo $t$, para $t>24$ ela é sempre maior que 1, e continua aumentando indefinidamente conforme $t$ cresce. Logo, não é apenas que A ultrapassa B em $t=24$: como a taxa relativa de crescimento de A é permanentemente maior que a de B, a diferença entre as populações só tende a aumentar, e A permanece maior que B **para sempre**.

**c) Confirmação numérica em $t=30$**

$$P_A(30) = 500 \cdot 2^{30/3} = 500 \cdot 2^{10} = 500 \cdot 1024 = 512000$$

$$P_B(30) = 8000 \cdot 2^{30/6} = 8000 \cdot 2^{5} = 8000 \cdot 32 = 256000$$

De fato, $P_A(30) = 512000 > 256000 = P_B(30)$, confirmando que 6 horas após o cruzamento (que ocorreu em $t=24$h), a Cultura A já tem o dobro de bactérias da Cultura B, evidenciando o comportamento descrito no item (b).

## Formalização verificável

- `equacao` — expressão `Eq(500*2**(t/3), 8000*2**(t/6))`, esperado `[24]`
- `funcao` — expressão `500*2**(t/3)`, esperado `512000`, parâmetros `{'consulta': 'valor', 'ponto': '30'}`
- `funcao` — expressão `8000*2**(t/6)`, esperado `256000`, parâmetros `{'consulta': 'valor', 'ponto': '30'}`
- `funcao` — expressão `500*2**(t/3)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `8000*2**(t/6)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (f(30) = 512000). | (3) aprovado: Gabarito confirmado (f(30) = 256000). | (4) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (5) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - equacao=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, dados completos (populações iniciais, tempos de duplicação, fórmulas explícitas), com três itens claramente delimitados e sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O item (b) exige genuína análise: comparar taxas de crescimento e justificar um comportamento assintótico sem calcular valores pontuais, o que corresponde a nível 'analisar' e estrutura relacional (SOLO). Os itens (a) e (c), porém, são majoritariamente de aplicação/cálculo direto, o que é adequado como apoio, mas faz com que apenas parte da questão atinja o nível declarado — o peso do item analítico poderia ser maior.
  - alinhamento_bncc: 5/5 — Cumpre integralmente a habilidade: exige interpretar a variação das grandezas (item b, comparação de taxas relativas de crescimento), articula cálculo e interpretação em um mesmo problema coeso (não são itens justapostos, pois b depende do resultado de a e c confirma a conclusão de b), e o contexto de crescimento de bactérias é apropriado e realista.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — Contexto de culturas bacterianas com tempos de duplicação distintos é mais elaborado que o clássico 'quando as populações se igualam'; a pergunta sobre permanência 'para sempre' evita resposta mecânica e exige raciocínio sobre taxas relativas. Ainda assim, a estrutura geral (duas exponenciais, igualar, comparar) é um formato consagrado em livros didáticos, o que limita um pouco a originalidade plena.
