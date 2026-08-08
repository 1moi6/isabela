# Ciclo 056 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

A maré de um porto varia periodicamente ao longo do dia. Um marégrafo registrou que a altura da água, em metros, em função do tempo $t$ (em horas, com $0 \le t < 24$), é bem descrita pela função

$$h(t) = 2\sin\left(\frac{\pi t}{6}\right) + 3.$$

Um estudante quer representar exatamente o mesmo fenômeno usando uma função cosseno da forma

$$h(t) = A\cos\big(B(t-C)\big) + D,$$

de modo que o gráfico dessa função coincida, ponto a ponto, com o gráfico da função seno dada, com $A>0$, $B>0$ e $0 < C < 6$.

Usando essa representação equivalente em cosseno, determine a altura máxima da maré e o instante $t$ (em horas, após $t=0$) em que essa altura máxima ocorre pela **segunda vez** dentro do intervalo $0 \le t < 24$.

## Alternativas

- (a) Altura máxima de 5 m, ocorrendo pela segunda vez em $t = 15$ horas.  ← correta
- (b) Altura máxima de 2 m, ocorrendo pela segunda vez em $t = 15$ horas.
  - *erro representado:* Confunde a amplitude A com a altura máxima real, esquecendo de somar o deslocamento vertical D (max = A+D, não apenas A).
- (c) Altura máxima de 5 m, ocorrendo pela segunda vez em $t = 9$ horas.
  - *erro representado:* Toma metade do período (6 h) como o intervalo entre máximos consecutivos, somando 6 ao invés do período completo de 12 h ao primeiro instante de máximo.
- (d) Altura máxima de 5 m, ocorrendo pela segunda vez em $t = 21$ horas.
  - *erro representado:* Erra o sinal do deslocamento de fase ao converter seno em cosseno, usando C = 9 em vez de C = 3, o que desloca incorretamente o primeiro máximo para t = 9 e o segundo para t = 21.

## Gabarito

Altura máxima = 5 m, ocorrendo pela segunda vez em $t = 15$ horas.

## Resolução

**Passo 1 — Identificar amplitude, período e deslocamento vertical.**

Na função $h(t) = 2\sin\left(\frac{\pi t}{6}\right) + 3$, temos amplitude $A=2$, deslocamento vertical $D=3$ e $B=\frac{\pi}{6}$, logo o período é
$$T = \frac{2\pi}{\pi/6} = 12 \text{ horas}.$$

A altura máxima é $A+D = 2+3 = 5$ m, atingida quando $\sin\left(\frac{\pi t}{6}\right)=1$.

**Passo 2 — Encontrar os instantes de máximo diretamente pela função seno.**

$$\frac{\pi t}{6} = \frac{\pi}{2} + 2k\pi \;\Rightarrow\; t = 3 + 12k,\quad k\in\mathbb{Z}.$$

Dentro de $0\le t<24$: primeiro máximo em $t=3$ ($k=0$) e segundo máximo em $t=15$ ($k=1$), pois o próximo máximo ocorre sempre um período (12 h) depois.

**Passo 3 — Reescrever como cosseno e conferir a coerência.**

Usando a identidade $\sin(\theta) = \cos\left(\theta - \frac{\pi}{2}\right)$, com $\theta = \frac{\pi t}{6}$:

$$\sin\left(\frac{\pi t}{6}\right) = \cos\left(\frac{\pi t}{6} - \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{6}(t-3)\right),$$

pois $\frac{\pi}{6}(t-3) = \frac{\pi t}{6} - \frac{\pi}{2}$. Logo

$$h(t) = 2\cos\left(\frac{\pi}{6}(t-3)\right) + 3,$$

ou seja, $A=2$, $B=\frac{\pi}{6}$, $C=3$ (que satisfaz $0<C<6$) e $D=3$.

Nessa forma de cosseno, o máximo ocorre quando o argumento é $0$ (mais múltiplos de $2\pi$), isto é, em $t = C + 12k = 3+12k$, confirmando exatamente os mesmos instantes $t=3$ e $t=15$ encontrados no Passo 2.

**Conclusão.** A altura máxima é $5$ m e ela ocorre pela segunda vez em $t = 15$ horas.

## Formalização verificável

- `funcao` — expressão `2*sin(pi*x/6) + 3`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `2*sin(pi*x/6) + 3`, esperado `5`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `2*sin(pi*x/6) + 3`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `2*sin(pi*x/6) + 3`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '15'}`
- `propriedade` — expressão `-`, esperado `2*cos(pi*(x-3)/6) + 3`, parâmetros `{'pontos': '[(0,3),(3,5),(6,3),(9,1),(12,3)]'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 5). | (3) rejeitado: Divergência: extremo calculado 5; gabarito 1. | (4) aprovado: Gabarito confirmado (f(3) = 5). | (5) aprovado: Gabarito confirmado (f(9) = 1).
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/minimo=rejeitado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 5). | (3) rejeitado: Divergência: extremo calculado 5; gabarito 1. | (4) aprovado: Gabarito confirmado (f(3) = 5). | (5) aprovado: Gabarito confirmado (f(9) = 1). Resultado calculado independentemente: período 12 | extremo calculado 5 | extremo calculado 5 | f(3) = 5 | f(9) = 1. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (extremo calculado 5). | (3) aprovado: Gabarito confirmado (f(3) = 5). | (4) aprovado: Gabarito confirmado (f(15) = 5). | (5) aprovado: Propriedades confirmadas para 2*cos(pi*(x/6 - 1/2)) + 3: reproduz os 5 pontos dados.
  - funcao/periodo=aprovado
  - funcao/maximo=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — Enunciado bem estruturado, com dados completos (função, domínio, condições sobre A,B,C) e pedido claro (altura máxima e segundo instante). Pequena fragilidade: pede-se 'usar essa representação em cosseno' para responder, mas a resposta final é idêntica independentemente da forma usada, o que pode gerar confusão sobre a real necessidade da conversão.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar identidades trigonométricas, extrair parâmetros (A,B,C,D) e localizar máximos, compatível com 'aplicar' em nível SOLO relacional. Porém, a resolução mostra que a conversão para cosseno (Passo 3) é dispensável para chegar à resposta — o problema poderia ser resolvido inteiramente com a função seno original, reduzindo a exigência real de comparação de representações a um passo decorativo em vez de necessário.
  - alinhamento_bncc: 4/5 — Parte de um fenômeno periódico real (maré) e exige explicitamente comparar a representação seno com uma representação cosseno equivalente, com amplitude, período e deslocamento sendo objeto de cálculo (não decorativos). Atende bem à habilidade EM13MAT306. O único ponto que impede nota máxima é que a comparação seno-cosseno não é estritamente necessária para resolver a pergunta final, o que fragiliza um pouco o vínculo entre a exigência da habilidade (comparar representações) e o que efetivamente é avaliado.
  - distratores: 5/5 — Todos os distratores correspondem a erros sistemático plausíveis e comuns: confundir amplitude com máximo total, usar metade do período em vez do período completo, e inverter o sinal do deslocamento de fase na conversão seno-cosseno. Nenhum é absurdo ou trivialmente eliminável, exigindo real compreensão dos conceitos envolvidos.
  - originalidade: 4/5 — O contexto de maré é significativo e menos batido que exemplos clássicos (roda-gigante, pêndulo). A exigência de reescrever seno como cosseno adiciona originalidade estrutural. Contudo, como essa conversão não é estritamente necessária para resolver o problema, funciona quase como uma 'pista decorativa' que pode ser ignorada por alunos mais atentos, reduzindo ligeiramente o valor pedagógico da tarefa como instrumento de comparação de representações.
