# Ciclo 085 — EM13MAT303

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Um capital $C_0$ é aplicado a juros compostos, com taxa fixa $i$ por período, de modo que o montante após $n$ períodos é dado por $M(n) = C_0\cdot(1+i)^n$. Sabe-se que, ao final de 3 períodos, o montante corresponde a 8 vezes o capital inicial, isto é, $M(3) = 8\,C_0$. Mantendo-se a mesma taxa $i$ por todo o tempo, qual é o montante $M(6)$, em função de $C_0$?

## Alternativas

- (a) $16\,C_0$
  - *erro representado:* Supor crescimento linear: como o número de períodos dobrou (de 3 para 6), o aluno dobra diretamente o montante (2 × 8C0), ignorando que, em juros compostos, dobrar os períodos eleva o fator de crescimento ao quadrado, não ao dobro.
- (b) $32\,C_0$
  - *erro representado:* Erro na propriedade de potência de potência: calcular $\left[(1+i)^3\right]^2$ somando os expoentes (3+2=5) em vez de multiplicá-los (3×2=6), obtendo $(1+i)^5 = 2^5 = 32$.
- (c) $64\,C_0$  ← correta
- (d) $512\,C_0$
  - *erro representado:* Erro de contagem de blocos de 3 períodos: o aluno calcula 6÷3 incorretamente como 3 (em vez de 2) e eleva o fator ao cubo, obtendo $8^3 = 512$, aplicando compostas de mais do que o necessário.

## Gabarito

64 C0

## Resolução

**Passo 1 — Traduzir o dado em uma equação.**

Como $M(n) = C_0\cdot(1+i)^n$, a condição $M(3) = 8\,C_0$ fornece
$$C_0\cdot(1+i)^3 = 8\,C_0 \;\Rightarrow\; (1+i)^3 = 8.$$

**Passo 2 — Usar a propriedade de potência para obter $(1+i)^6$ sem precisar isolar $i$.**

Como $6 = 3\cdot 2$, escrevemos
$$(1+i)^6 = \left[(1+i)^3\right]^2 = 8^2 = 64.$$

Esse passo é o núcleo do raciocínio: dobrar o número de períodos **eleva ao quadrado** o fator de crescimento acumulado (comportamento exponencial), e não o dobra (comportamento que seria linear).

**Passo 3 — Calcular o montante pedido.**

$$M(6) = C_0\cdot(1+i)^6 = C_0\cdot 64 = 64\,C_0.$$

Portanto, após 6 períodos o montante é $64\,C_0$, ou seja, 64 vezes o capital inicial — muito mais que o dobro dos 8 vezes obtidos em 3 períodos, evidenciando o crescimento exponencial (e não linear) do capital sob juros compostos.

## Formalização verificável

- `funcao` — expressão `2**n`, esperado `64`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `funcao` — expressão `2**n`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 2 afirmações reprovadas. (1) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-3**(1/3)/2 - 3**(5/6)*I/2, -3**(1/3)/2 + 3**(5/6)*I/2]. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - equacao=rejeitado
  - equacao=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 2 afirmações reprovadas. (1) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-3**(1/3)/2 - 3**(5/6)*I/2, -3**(1/3)/2 + 3**(5/6)*I/2]. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. Resultado calculado independentemente: [3**(1/3), -3**(1/3)/2 - 3**(5/6)*I/2, -3**(1/3)/2 + 3**(5/6)*I/2] | [81]. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(6) = 64). | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a fórmula do montante, o dado (M(3)=8C0) e a pergunta (M(6) em função de C0). Não há ambiguidade lexical nem lacunas de informação.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar a propriedade de potência de potência a uma situação de juros compostos, compatível com o nível 'aplicar' de Bloom. A resposta esperada é relacional (conecta a condição dada com a propriedade exponencial), coerente com SOLO relacional, ainda que a manipulação seja relativamente mecânica uma vez identificada a estratégia.
  - alinhamento_bncc: 4/5 — A questão envolve juros compostos e evidencia explicitamente o crescimento exponencial (tanto no comando quanto na resolução, que contrasta com o raciocínio linear incorreto). Contudo, é uma abordagem bastante formal/algébrica, sem uso de porcentagem explícita nem contextualização financeira concreta (valores, taxa real), o que a aproxima mais de um exercício sobre propriedades de potência do que de um problema aplicado de juros compostos.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos plausíveis: raciocínio linear (16C0), erro na propriedade de potência somando expoentes (32C0) e erro na contagem de blocos de período (512C0). Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 3/5 — O contexto de juros compostos é o clássico de livros didáticos, mas a forma de indagar (dado M(3)=8C0, pedir M(6) sem calcular i) foge do modelo padrão de 'ache a taxa/o montante direto'. Ainda assim, falta um contexto significativo (situação real, valores concretos, tomada de decisão) que tornaria o problema mais motivador e menos uma manipulação algébrica pura.
