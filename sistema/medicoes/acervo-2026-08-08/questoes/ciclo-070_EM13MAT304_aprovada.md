# Ciclo 070 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo monitora o crescimento de uma colônia de bactérias em um meio de cultura controlado. Ele constata que, nas primeiras horas de observação, a população cresce segundo um modelo exponencial da forma $P(t) = P_0 \cdot a^t$, em que $P(t)$ é o número de bactérias (em milhares) $t$ horas após o início da observação, $P_0$ é a população inicial e $a$ é uma constante positiva.

Sabe-se que, no instante $t=0$, a colônia possui 5 mil bactérias e que, decorridas 4 horas, a população atinge 80 mil bactérias.

a) Determine a lei da função $P(t)$ que descreve essa população.

b) Determine, em horas, o tempo necessário para que a população atinja 320 mil bactérias.

c) Calcule o aumento absoluto (em milhares de bactérias) ocorrido entre a 1ª hora de observação (de $t=0$ a $t=1$) e o aumento absoluto ocorrido entre a 5ª e a 6ª hora (de $t=4$ a $t=5$). Em seguida, explique por que esses dois valores são diferentes, mesmo que a taxa percentual de crescimento da colônia seja a mesma em qualquer intervalo de uma hora.

## Gabarito

a) $P(t) = 5\cdot 2^t$; b) $t = 6$ horas; c) aumento na 1ª hora = 5 mil bactérias; aumento entre a 5ª e 6ª hora = 80 mil bactérias — valores diferentes porque, embora a taxa percentual de crescimento seja sempre 100% ao hora (fator constante $a=2$), o aumento absoluto é proporcional à população atual, que cresce exponencialmente.

## Resolução

**a) Determinando a lei de $P(t)$**

Como $P(0) = P_0$, e sabemos que $P(0) = 5$, temos $P_0 = 5$.

Usando o dado em $t=4$: $P(4) = 5\cdot a^4 = 80 \Rightarrow a^4 = 16 \Rightarrow a = 2$ (raiz positiva, pois $a>0$ representa uma taxa de crescimento).

Logo, $P(t) = 5\cdot 2^t$.

**b) Tempo para atingir 320 mil bactérias**

$5\cdot 2^t = 320 \Rightarrow 2^t = 64 = 2^6 \Rightarrow t = 6$ horas.

**c) Comparando os aumentos absolutos**

Calculando os valores da função:

$P(0)=5$, $P(1)=5\cdot2=10$ → aumento na 1ª hora: $10-5=5$ mil bactérias.

$P(4)=80$, $P(5)=80\cdot2=160$ → aumento entre a 5ª e a 6ª hora: $160-80=80$ mil bactérias.

Os aumentos absolutos são diferentes (5 mil contra 80 mil), embora a razão $\dfrac{P(t+1)}{P(t)} = a = 2$ seja **constante** para qualquer $t$ — ou seja, a população sempre *dobra* (cresce 100%) a cada hora, não importa em que instante estamos.

Isso ocorre porque o aumento absoluto em cada intervalo de uma hora é $P(t+1)-P(t) = P(t)\cdot(a-1) = P(t)$, ou seja, é **proporcional à população já existente naquele instante**. Como a própria população cresce exponencialmente, o aumento absoluto também cresce, mesmo que a taxa percentual de crescimento (o fator multiplicativo por hora) permaneça sempre igual a 2 (100% de aumento relativo). Essa é a característica essencial do crescimento exponencial: taxa relativa constante, mas variação absoluta crescente ao longo do tempo.

## Formalização verificável

- `funcao` — expressão `5*2**t`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `5*2**t`, esperado `10`, parâmetros `{'consulta': 'valor', 'ponto': '1'}`
- `funcao` — expressão `5*2**t`, esperado `80`, parâmetros `{'consulta': 'valor', 'ponto': '4'}`
- `funcao` — expressão `5*2**t`, esperado `160`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`
- `equacao` — expressão `Eq(5*2**t, 320)`, esperado `[6]`
- `funcao` — expressão `5*2**t`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 6 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(0) = 5). | (2) aprovado: Gabarito confirmado (f(1) = 10). | (3) aprovado: Gabarito confirmado (f(4) = 80). | (4) aprovado: Gabarito confirmado (f(5) = 160). | (5) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (6) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente os dados (P0=5, P(4)=80), o modelo matemático e as três tarefas (a, b, c). Não há ambiguidade lexical ou estrutural, e as unidades (milhares, horas) são consistentes ao longo do texto.
  - adequacao_nivel: 4/5 — Os itens (a) e (b) são de aplicação direta (resolver equações exponenciais), compatíveis com 'aplicar/compreender'. O item (c) eleva o nível para 'analisar', pois exige comparar dois intervalos, identificar que a razão constante não implica variação absoluta constante, e articular a relação entre taxa percentual e taxa absoluta — isso é coerente com resposta relacional na taxonomia SOLO. Poderia ser ainda mais desafiador se toda a questão exigisse esse tipo de raciocínio, não apenas o item final.
  - alinhamento_bncc: 5/5 — A questão atende à EM13MAT304 de forma explícita: além do cálculo do modelo (a, b), o item (c) exige compreensão e interpretação da variação das grandezas, contrastando taxa relativa constante com variação absoluta crescente — exatamente o núcleo da habilidade. O contexto de crescimento bacteriano é adequado e realista.
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 4/5 — O contexto de crescimento bacteriano é um clássico em funções exponenciais, mas a pergunta interpretativa do item (c) foge do padrão mecânico de 'calcule e substitua', exigindo justificativa conceitual sem entregar pistas óbvias que pavimentem a resposta (evita efeito Topaze).
