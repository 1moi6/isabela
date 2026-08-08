# Ciclo 001 — EM13MAT302

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma empresa de transporte por aplicativo cobra, em cada corrida, uma taxa fixa somada a um valor proporcional à distância percorrida. Um cliente fez uma corrida de 4 km e pagou R$ 13,00. Em outro dia, o mesmo cliente percorreu 10 km e pagou R$ 25,00. Sabe-se que o preço da corrida varia linearmente com a distância percorrida.

a) Determine a expressão algébrica que fornece o preço C, em reais, de uma corrida em função da distância d, em quilômetros.

b) Usando essa expressão, calcule quanto custará uma corrida de 15 km.

## Gabarito

C(d) = 2d + 5; para d = 15 km, o custo é R$ 35,00.

## Resolução

**Modelando a situação**

Como o preço varia linearmente com a distância, o modelo é uma função afim:
$$C(d) = a \cdot d + b$$
onde $a$ é o valor cobrado por km e $b$ é a taxa fixa.

**Usando os dados para montar um sistema**

Com $d=4$, $C=13$: $\;13 = 4a + b$

Com $d=10$, $C=25$: $\;25 = 10a + b$

**Resolvendo o sistema**

Subtraindo a primeira equação da segunda:
$$25 - 13 = 10a - 4a \implies 12 = 6a \implies a = 2$$

Substituindo em $13 = 4a+b$:
$$13 = 4(2) + b \implies 13 = 8 + b \implies b = 5$$

**Modelo obtido**
$$C(d) = 2d + 5$$

**Item b)**

Para $d = 15$:
$$C(15) = 2(15) + 5 = 30 + 5 = 35$$

Logo, a corrida de 15 km custará **R$ 35,00**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `2*x + 5`, parâmetros `{'pontos': '[(4,13),(10,25)]', 'grau': '1'}`
- `funcao` — expressão `2*x + 5`, esperado `35`, parâmetros `{'consulta': 'valor', 'ponto': '15'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 2*x + 5: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(15) = 35).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem redigido, com dados completos (dois pares distância-preço), pedido claro em dois itens (expressão algébrica e cálculo numérico) e nenhuma ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A tarefa exige montar um sistema linear a partir de dois pontos para obter a e b, o que corresponde a 'aplicar' conhecimentos de função afim de forma não trivial (não é mera substituição em fórmula dada). A estrutura de resposta é relacional (integra dois dados para construir o modelo) seguida de aplicação unistrutural no item b, coerente com o nível declarado. Poderia exigir um pouco mais de análise (ex.: interpretar coeficientes) para elevar a nota.
  - alinhamento_bncc: 5/5 — Cumpre integralmente a habilidade: o modelo (função afim) não é entregue, o estudante precisa construí-lo a partir da situação contextualizada e depois empregá-lo para resolver um problema numérico, articulando construção e aplicação num único enunciado.
  - distratores: 5/5 — não se aplica
  - originalidade: 4/5 — O contexto de aplicativo de transporte atualiza o clássico problema de 'taxa fixa + tarifa por km', evitando o enunciado didático tradicional de táxi. A frase 'o preço varia linearmente' é necessária para orientar o tipo de modelo e não chega a pavimentar a solução (efeito Topaze), mas o esqueleto do problema ainda é bastante convencional.
