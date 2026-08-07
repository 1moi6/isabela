# Ciclo 016 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Um biólogo monitora o crescimento de uma colônia de bactérias em condições controladas de laboratório. Ele registra a quantidade de bactérias a cada hora, numerando as medições por $n = 1, 2, 3, \dots$ (sendo $n=1$ a primeira medição realizada). Na primeira medição foram contadas 500 bactérias, e a cada hora subsequente esse número dobra.

a) Escreva o termo geral $a_n$ da progressão geométrica (PG) que representa a quantidade de bactérias na $n$-ésima medição.

b) Para analisar a tendência de crescimento entre uma medição e outra, o biólogo define a função $f(n) = 500\cdot 2^{n-1}$, considerando agora $n$ como um número real. Determine o domínio dessa função $f$ e explique por que ele é mais amplo do que o domínio da PG original.

c) Calcule, usando o termo geral da PG, o número de bactérias na 7ª e na 8ª medições.

d) Compare os valores de $f(7)$ e $f(8)$, calculados pela função exponencial, com os termos $a_7$ e $a_8$ da PG, e explique por que esses resultados coincidem.

## Gabarito

a) $a_n = 500\cdot 2^{n-1}$; b) $D(f)=\mathbb{R}$, mais amplo que o domínio discreto $\mathbb{N}^*$ da PG; c) $a_7 = 32000$ e $a_8 = 64000$; d) $f(7)=a_7=32000$ e $f(8)=a_8=64000$, pois $f$ é a extensão contínua da PG, coincidindo com ela nos valores naturais de $n$.

## Resolução

**a) Termo geral da PG**

A quantidade inicial é $a_1 = 500$ e a razão é $q = 2$ (o número dobra a cada hora). Pela fórmula do termo geral de uma PG:

$$a_n = a_1 \cdot q^{n-1} = 500 \cdot 2^{n-1}, \quad n \in \mathbb{N}^*$$

**b) Domínio da função exponencial associada**

A função $f(n) = 500\cdot 2^{n-1}$ tem a mesma *lei de formação* da PG, mas, ao permitir que $n$ assuma qualquer valor real (e não apenas naturais), sua expressão $2^{n-1}$ está definida para todo $n \in \mathbb{R}$, pois a exponencial de base positiva não tem restrições de domínio. Logo:

$$D(f) = \mathbb{R}$$

Já a PG só está definida para os índices $n = 1, 2, 3, \dots$ (domínio discreto, $\mathbb{N}^*$), pois cada termo corresponde a uma medição específica realizada em um instante de tempo determinado — não faz sentido, por exemplo, falar em "medição número 2,5". Assim, $f$ é uma **extensão contínua** da PG: ela concorda com a PG em todos os pontos $n$ naturais, mas também está definida entre eles.

**c) Termos $a_7$ e $a_8$**

$$a_7 = 500\cdot 2^{7-1} = 500\cdot 2^6 = 500\cdot 64 = 32000$$

$$a_8 = 500\cdot 2^{8-1} = 500\cdot 2^7 = 500\cdot 128 = 64000$$

**d) Comparação entre $f$ e a PG**

Calculando a função nos mesmos pontos:

$$f(7) = 500\cdot 2^{6} = 32000 = a_7$$
$$f(8) = 500\cdot 2^{7} = 64000 = a_8$$

Os valores coincidem porque $f(n)$ foi construída exatamente com a mesma razão e o mesmo primeiro termo da PG; nos pontos $n$ naturais, a função exponencial reproduz fielmente os termos da progressão. A diferença entre elas está apenas no domínio: a PG é a versão discreta (restrita aos números naturais) da função exponencial $f$, que é sua versão contínua (definida em todo $\mathbb{R}$).

## Formalização verificável

- `propriedade` — expressão `-`, esperado `500*2**(n-1)`, parâmetros `{'sequencia': 'pg', 'a1': '500', 'razao': '2'}`
- `funcao` — expressão `500*2**(n-1)`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `500*2**(n-1)`, esperado `32000`, parâmetros `{'consulta': 'valor', 'ponto': '7'}`
- `funcao` — expressão `500*2**(n-1)`, esperado `64000`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 4 de 5 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 500*2**n vale 1000 em n=1, mas o 1º termo da PG é 500. | (2) rejeitado: Divergência: domínio calculado: Interval(-oo, oo); gabarito: Interval(0, oo). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) rejeitado: Divergência: termo calculado = 32000, gabarito = 64000. | (5) rejeitado: Divergência: termo calculado = 16000, gabarito = 32000.
  - propriedade=rejeitado
  - funcao/dominio=rejeitado
  - equacao=aprovado
  - progressao/termo=rejeitado
  - progressao/termo=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 4 de 5 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 500*2**n vale 1000 em n=1, mas o 1º termo da PG é 500. | (2) rejeitado: Divergência: domínio calculado: Interval(-oo, oo); gabarito: Interval(0, oo). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) rejeitado: Divergência: termo calculado = 32000, gabarito = 64000. | (5) rejeitado: Divergência: termo calculado = 16000, gabarito = 32000. Resultado calculado independentemente: a expressão 500*2**n vale 1000 em n=1, mas o 1º termo da PG é 500 | domínio calculado: Interval(-oo, oo) | [log(10**(2/log(2)))] | 32000 | 16000. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 500*2**(n - 1): coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (domínio de 500*2**(n - 1): Reals). | (3) aprovado: Gabarito confirmado (f(7) = 32000). | (4) aprovado: Gabarito confirmado (f(8) = 64000).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (a1=500, q=2), pedidos claros em cada item e contexto consistente. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — Os itens a) e c) são de aplicação direta (multiestrutural), mas b) e d) exigem justificar por que domínios diferem e por que valores coincidem, o que caracteriza análise relacional (comparar, explicar causas, integrar conceitos) coerente com o nível 'analisar'. Poderia exigir ainda mais integração (ex.: pedir para o aluno generalizar quando PG e função exponencial coincidem), mas o nível está adequado.
  - alinhamento_bncc: 5/5 — A questão articula explicitamente PG e função exponencial num único problema, exige comparação de domínios (discreto vs. contínuo) e pede explicação da coincidência dos valores — exatamente o que a habilidade EM13MAT508 demanda. Não se limita a aplicar fórmulas; exige a associação conceitual explícita.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de crescimento bacteriano é clássico em livros didáticos para PG/exponencial, e a estrutura de perguntas segue um roteiro previsível (termo geral, domínio, cálculo, comparação). Ainda assim, a articulação explícita entre domínio discreto e contínuo no item b) foge um pouco do padrão mecânico, mitigando o efeito Topaze parcialmente, mas o contexto poderia ser mais inovador ou menos repetido nesse tipo de aplicação.
