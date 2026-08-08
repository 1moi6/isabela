# Ciclo 034 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma locadora de bicicletas cobra uma taxa fixa de utilização mais um valor proporcional ao tempo de uso. A tabela a seguir mostra o valor total pago por diferentes clientes, de acordo com o tempo de uso da bicicleta:

| Tempo de uso (horas) | Valor total pago (R$) |
|---|---|
| 1 | 8 |
| 2 | 12 |
| 3 | 16 |
| 4 | 20 |

a) Observando o padrão de variação entre o tempo de uso e o valor pago, escreva uma expressão algébrica que permita calcular o valor total V, em reais, pago por um cliente que usa a bicicleta durante t horas, para qualquer valor inteiro positivo de t.

b) Classifique o tipo de função obtida em (a), justificando sua resposta a partir da expressão algébrica encontrada.

## Gabarito

V(t) = 4t + 4; a relação é uma função polinomial do 1º grau (afim), pois apresenta taxa de variação constante (4) e t aparece com expoente 1.

## Resolução

**Passo 1 — Observar a variação do valor pago em relação ao tempo.**

Calculando a diferença entre valores consecutivos da tabela:

$12-8=4$

$16-12=4$

$20-16=4$

A cada hora adicional, o valor pago aumenta sempre a mesma quantia: $4$ reais. Isso indica uma variação **constante**, ou seja, uma taxa de variação fixa igual a $4$.

**Passo 2 — Escrever a lei geral.**

Como a variação é constante, o valor total deve ter a forma

$$V(t) = 4t + b$$

em que $b$ é o valor pago quando $t=0$ (a taxa fixa da locadora).

**Passo 3 — Determinar $b$ usando um ponto da tabela.**

Usando o par $(1, 8)$:

$$8 = 4(1) + b \implies b = 4$$

Verificando com outro ponto, por exemplo $(3,16)$:

$$4(3)+4 = 12+4 = 16 \ \checkmark$$

Logo, a lei que representa a situação é:

$$V(t) = 4t + 4$$

**Passo 4 — Classificar a função.**

A expressão $V(t) = 4t + 4$ tem a forma $V(t) = a\,t + b$, com $a = 4 \neq 0$ e $b = 4$, isto é, a variável $t$ aparece elevada apenas ao expoente 1. Portanto, trata-se de uma **função polinomial do 1º grau (função afim)**, com coeficiente angular (taxa de variação) $4$ e coeficiente linear $4$. Como $a=4>0$, a função é crescente, o que é coerente com o fato de o valor pago aumentar conforme o tempo de uso aumenta.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*t + 4`, parâmetros `{'pontos': '[(1,8),(2,12),(3,16),(4,20)]', 'grau': '1'}`
- `funcao` — expressão `4*x + 4`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*t + 4: reproduz os 4 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado sem ambiguidade: tabela completa, pedido explícito de expressão algébrica em (a) e classificação justificada em (b). Não há dados faltantes nem duplo sentido lexical.
  - adequacao_nivel: 3/5 — O nível 'criar' é defensável (generalizar um padrão em lei algébrica), mas a resolução mostra que o processo é essencialmente mecânico: calcular diferenças constantes e ajustar y=ax+b, algo mais próximo de 'aplicar/analisar'. A estrutura SOLO da resposta esperada é multiestrutural/relacional, não plenamente 'extended abstract', o que fragiliza a correspondência plena com 'criar'. O conteúdo (função afim) é compatível com o Ensino Médio.
  - alinhamento_bncc: 4/5 — Atende às três exigências centrais listadas: dados apresentados em tabela sem fórmula pronta, pedido de generalização algébrica (não cálculo pontual) e condução ao reconhecimento da função como polinomial de 1º grau, com justificativa baseada na expressão. Falta, porém, o componente de representação no plano cartesiano mencionado na habilidade original, o que impede nota máxima.
  - distratores: 5/5 — não se aplica
  - originalidade: 4/5 — O contexto de locadora de bicicletas é um pouco menos batido que os clássicos 'plano de celular' ou 'corrida de táxi', ainda que a estrutura (taxa fixa + variável) seja recorrente em livros didáticos. O enunciado não entrega pistas que pavimentem a solução, evitando efeito Topaze.
