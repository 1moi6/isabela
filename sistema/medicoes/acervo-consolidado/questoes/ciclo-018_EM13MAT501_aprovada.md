# Ciclo 018 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma empresa de saneamento básico cobra mensalmente pelo consumo de água uma tarifa composta por um valor fixo somado a um valor proporcional ao consumo, medido em metros cúbicos (m³). A tabela a seguir mostra o valor total pago por três clientes que tiveram consumos diferentes num mesmo mês:

| Consumo (m³) | Valor cobrado (R$) |
|---|---|
| 3 | 21,50 |
| 7 | 37,50 |
| 12 | 57,50 |

a) Analise os dados da tabela e explique por que o valor cobrado V pode ser descrito por uma função polinomial do 1º grau do consumo x.

b) Determine a lei algébrica que expressa V em função de x.

c) Qual é o valor da tarifa fixa mensal, isto é, a parcela que o cliente paga mesmo que não haja variação proporcional ao consumo?

## Gabarito

A relação é uma função afim porque a razão $\Delta V/\Delta x$ é constante e igual a 4, mesmo com intervalos de consumo diferentes. A lei é $V(x) = 4x + 9{,}5$, e a tarifa fixa é R$ 9,50.

## Resolução

**1. Organizando os pares (consumo, valor):**

$(3;\,21{,}5)$, $(7;\,37{,}5)$, $(12;\,57{,}5)$

Como os consumos não estão igualmente espaçados (as diferenças são $4$ e $5$, não uma constante como em uma tabela usual), não basta olhar as diferenças brutas: é preciso calcular a **taxa de variação** $\dfrac{\Delta V}{\Delta x}$ entre pares consecutivos.

**2. Calculando as taxas de variação:**

Entre o 1º e o 2º cliente:
$$\Delta x_1 = 7-3=4, \qquad \Delta V_1 = 37{,}5-21{,}5=16$$
$$\frac{\Delta V_1}{\Delta x_1}=\frac{16}{4}=4$$

Entre o 2º e o 3º cliente:
$$\Delta x_2 = 12-7=5, \qquad \Delta V_2 = 57{,}5-37{,}5=20$$
$$\frac{\Delta V_2}{\Delta x_2}=\frac{20}{5}=4$$

**3. Reconhecendo a função afim:**

Como a razão $\dfrac{\Delta V}{\Delta x}$ é a mesma ($=4$) mesmo para intervalos de tamanhos diferentes, a variação de $V$ é diretamente proporcional à variação de $x$. Isso caracteriza uma **função polinomial do 1º grau (afim)**, do tipo $V(x)=ax+b$, com $a=4$ (a taxa constante encontrada).

**4. Determinando o coeficiente linear $b$:**

Usando o ponto $(3;\,21{,}5)$:
$$21{,}5 = 4\cdot 3 + b \;\Rightarrow\; 21{,}5 = 12 + b \;\Rightarrow\; b = 9{,}5$$

Logo:
$$V(x) = 4x + 9{,}5$$

**5. Verificação com o terceiro par:**

$$V(12) = 4\cdot 12 + 9{,}5 = 48+9{,}5 = 57{,}5 \;\checkmark$$

Confirma-se que a lei encontrada é consistente com todos os dados da tabela.

**6. Interpretando a tarifa fixa:**

A parte que não depende do consumo é o coeficiente linear $b$, ou seja, o valor de $V$ quando $x=0$:
$$V(0) = 9{,}5$$

Portanto, a tarifa fixa mensal é **R$ 9,50**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*x + Rational(19,2)`, parâmetros `{'pontos': '[(3, Rational(43,2)), (7, Rational(75,2)), (12, Rational(115,2))]', 'grau': '1'}`
- `funcao` — expressão `4*x + Rational(19,2)`, esperado `Rational(19,2)`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `4*x + Rational(19,2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*x + 19/2: reproduz os 3 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(0) = 19/2). | (3) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é preciso: apresenta a tabela com consumo e valor cobrado, define o que é dado (valor fixo + proporcional) e separa claramente os três pedidos (justificar, determinar lei, interpretar coeficiente). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O item (a) exige comparar razões de variação em intervalos desiguais para justificar a linearidade — isso é coerente com 'analisar' (nível relacional na SOLO). O item (b) pede a generalização algébrica, também compatível. Porém o item (c) apenas reinterpreta o valor de b já obtido em (b), sendo de nível mais baixo (compreensão/aplicação), o que dilui um pouco a exigência analítica global da questão.
  - alinhamento_bncc: 4/5 — Atende às exigências centrais listadas: dados fornecidos em tabela sem a lei pronta, pedido explícito de generalização algébrica (item b) e reconhecimento da função como polinomial de 1º grau (item a). A escolha de consumos não equiespaçados fortalece a investigação de padrão exigida pela habilidade. Não há exploração da representação no plano cartesiano, mas isso não constava como exigência explícita do professor, apenas da habilidade original; por isso a perda é pequena, não crítica.
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 4/5 — O contexto de tarifa de água é comum em materiais didáticos, mas o uso de consumos não igualmente espaçados evita o efeito Topaze de identificar a razão constante por diferenças simples, exigindo do estudante o cálculo de taxas de variação — um traço de design didático positivo e menos mecânico que o padrão usual.
