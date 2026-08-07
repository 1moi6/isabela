# Ciclo 010 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma locadora de bicicletas cobra uma taxa fixa de manutenção mais um valor por hora de uso. A tabela abaixo mostra o valor total pago (em reais) por clientes que alugaram uma bicicleta durante diferentes quantidades de horas em um mesmo dia:

| Horas de uso (x) | Valor total pago em R$ (y) |
|---|---|
| 1 | 8 |
| 2 | 11 |
| 3 | 14 |
| 4 | 17 |

a) Observando os pares de valores da tabela, identifique o padrão de variação entre x e y e represente esses pontos no plano cartesiano (x, y).

b) Escreva uma expressão algébrica y = f(x) que generalize esse padrão, permitindo calcular o valor pago para qualquer quantidade x de horas de uso.

c) Justifique por que a relação encontrada é uma função polinomial do 1º grau, indicando o que representam, no contexto do problema, o coeficiente que multiplica x e o termo constante da expressão.

## Gabarito

f(x) = 3x + 5, função polinomial do 1º grau, com a=3 (valor por hora) e b=5 (taxa fixa)

## Resolução

**a) Identificando o padrão**

Organizando os pares $(x,y)$: $(1,8), (2,11), (3,14), (4,17)$.

Calculando a variação de $y$ a cada aumento de 1 unidade em $x$:

$11-8=3$

$14-11=3$

$17-14=3$

A cada hora a mais de uso, o valor pago aumenta sempre **3 reais**. Isso indica que a variação de $y$ é constante em relação à variação de $x$ (taxa de variação constante $= 3$), o que caracteriza uma progressão aritmética de razão 3 nos valores de $y$. Ao marcar os pontos $(1,8), (2,11), (3,14), (4,17)$ no plano cartesiano, eles ficam alinhados, sugerindo que pertencem a uma **reta**.

**b) Generalizando algebricamente**

Como a taxa de variação é constante e igual a 3, a expressão deve ter a forma $y = 3x + b$.

Usando o ponto $(1,8)$ para encontrar $b$:

$8 = 3(1) + b \Rightarrow b = 8 - 3 = 5$

Verificando com os demais pontos:

$x=2: y = 3(2)+5 = 11$ ✓

$x=3: y = 3(3)+5 = 14$ ✓

$x=4: y = 3(4)+5 = 17$ ✓

Logo, a expressão que generaliza o padrão é:

$$f(x) = 3x + 5$$

**c) Reconhecendo o tipo de função**

A expressão $f(x) = 3x + 5$ tem a forma $f(x) = ax+b$, com $a=3 \neq 0$ e $b=5$, que é a lei geral de uma **função polinomial do 1º grau (função afim)**.

No contexto do problema:

- O coeficiente $a=3$ representa o **valor cobrado por hora de uso** (a taxa de variação do custo).
- O termo constante $b=5$ representa a **taxa fixa de manutenção**, cobrada mesmo que o tempo de uso $x$ tendesse a zero (o valor inicial, quando $x=0$).

Como o acréscimo em $y$ é sempre proporcional e constante ao acréscimo em $x$ (variação linear), confirma-se que a relação tabelada é, de fato, uma função afim.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x + 5`, parâmetros `{'pontos': '[(1,8),(2,11),(3,14),(4,17)]', 'grau': '1'}`
- `funcao` — expressão `3*x + 5`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*x + 5: reproduz os 4 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta dados completos em tabela, distingue claramente as três tarefas (identificar padrão/plotar, generalizar algebricamente, justificar o tipo de função) e não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O item c exige justificar por que a relação é afim e interpretar os coeficientes, o que corresponde a 'analisar' (SOLO relacional/estendido abstrato). Porém os itens a e b são majoritariamente 'aplicar/entender' (calcular diferenças constantes, substituir em fórmula), reduzindo um pouco a exigência analítica média da questão como um todo.
  - alinhamento_bncc: 5/5 — Cumpre integralmente as exigências: dados chegam via tabela sem fórmula pronta, pede-se generalização algébrica (não valor isolado) e o item c conduz explicitamente ao reconhecimento da função como polinomial de 1º grau, com interpretação contextual dos coeficientes.
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 3/5 — O contexto de 'taxa fixa + valor por hora' é uma estrutura muito recorrente em livros didáticos (análogo a táxi, aluguel de carro), reduzindo a originalidade. Não há efeito Topaze evidente, mas o cenário poderia ser mais inovador ou trazer dado supérfluo/desafio extra para diferenciar de exercícios padrão.
