# Ciclo 056 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um biólogo monitora o crescimento de uma colônia de bactérias em um experimento de laboratório, registrando a quantidade de indivíduos ao final de cada hora, a partir da 1ª hora de observação. Os dados coletados nas quatro primeiras horas foram:

| Hora (n) | Quantidade de bactérias |
|---|---|
| 1 | 100 |
| 2 | 300 |
| 3 | 900 |
| 4 | 2700 |

Essa quantidade cresce segundo o mesmo padrão observado nessas quatro medições, formando uma progressão geométrica. O biólogo deseja expressar o número de bactérias por meio de uma função exponencial $f(n)$, definida para $n$ natural, $n \geq 1$, que reproduza exatamente os valores registrados na tabela.

Assinale a alternativa que apresenta corretamente essa função $f(n)$ e o número de bactérias previsto para a 7ª hora de observação.

## Alternativas

- (a) $f(n) = 100 \cdot 3^{n-1}$; na 7ª hora haverá $72900$ bactérias.  ← correta
- (b) $f(n) = 100 + 200(n-1)$; na 7ª hora haverá $1300$ bactérias.
  - *erro representado:* Tratar a sequência como progressão aritmética, usando a diferença entre os dois primeiros termos como se fosse uma razão aditiva, em vez de identificar a razão geométrica constante.
- (c) $f(n) = 100 \cdot 3^{n}$; na 7ª hora haverá $218700$ bactérias.
  - *erro representado:* Erro de indexação: usar o expoente n em vez de n-1, não ajustando a fórmula do termo geral ao fato de a contagem começar em n=1 (deveria valer 100 para n=1, mas essa fórmula dá 300).
- (d) $f(n) = 100 \cdot 3^{n-1}$; na 7ª hora haverá $109300$ bactérias, calculadas pela soma de todos os termos da progressão até a 7ª hora.
  - *erro representado:* Confundir o termo geral da PG (quantidade presente naquela hora) com a soma dos termos da progressão (soma acumulada das quantidades de todas as horas anteriores), aplicando a fórmula da soma S_n em vez da fórmula do termo a_n.

## Gabarito

f(n) = 100·3^(n-1); f(7) = 72900 bactérias

## Resolução

**Passo 1 — Reconhecer a progressão geométrica.**

Os valores $100, 300, 900, 2700$ satisfazem $\dfrac{300}{100} = \dfrac{900}{300} = \dfrac{2700}{900} = 3$, logo constituem uma PG de primeiro termo $a_1 = 100$ e razão $q = 3$.

**Passo 2 — Termo geral da PG.**

$a_n = a_1 \cdot q^{\,n-1} = 100 \cdot 3^{\,n-1}$

**Passo 3 — Associar a PG à função exponencial de domínio discreto.**

A sequência $(a_n)$ é a restrição, aos números naturais $n \geq 1$, da função exponencial $f(n) = 100 \cdot 3^{\,n-1}$. Ou seja, $f(1)=100$, $f(2)=300$, $f(3)=900$, $f(4)=2700$, coincidindo com os dados da tabela — a PG é exatamente a "amostragem" dessa função exponencial nos pontos inteiros.

**Passo 4 — Calcular a previsão para a 7ª hora.**

$f(7) = 100 \cdot 3^{7-1} = 100 \cdot 3^{6} = 100 \cdot 729 = 72900$

**Conclusão:** $f(n) = 100 \cdot 3^{n-1}$ e, na 7ª hora, há $72900$ bactérias.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `100*3**(n-1)`, parâmetros `{'pontos': '[(1,100),(2,300),(3,900),(4,2700)]', 'sequencia': 'pg', 'a1': '100', 'razao': '3'}`
- `funcao` — expressão `100*3**(n-1)`, esperado `72900`, parâmetros `{'consulta': 'valor', 'ponto': '7'}`
- `funcao` — expressão `100*3**(n-1)`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 100*3**(n - 1): reproduz os 4 pontos dados; coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(7) = 72900). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)).
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta dados completos e organizados em tabela, define claramente o domínio (n natural, n≥1) e especifica exatamente o que se pede: a expressão de f(n) e o valor em n=7. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (identificar o padrão geométrico, formular a expressão algébrica e calcular um valor futuro) é compatível com o nível 'aplicar' de Bloom. A resposta esperada é relacional (SOLO), pois exige conectar a razão constante ao expoente e ao índice do domínio discreto, não apenas repetir um procedimento memorizado.
  - alinhamento_bncc: 3/5 — O enunciado menciona a função exponencial de domínio discreto e a PG, mas a exigência efetiva de resposta reduz-se a aplicar a fórmula do termo geral a_n = a1·q^(n-1) e renomeá-la como f(n). A articulação conceitual entre sequência e função (por que a PG é uma restrição da exponencial aos naturais) aparece apenas na resolução do professor, não é testada nem exigida pelas alternativas — o aluno pode acertar sem refletir sobre essa relação, apenas calculando a razão e o termo geral. Isso contraria a exigência explícita da especificação de que a aplicação de fórmula não basta.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e pedagogicamente relevantes: confundir PG com PA, erro de indexação do expoente (relevante à noção de domínio discreto), e confusão entre termo geral e soma de termos. Nenhum é absurdo ou trivialmente descartável, e cobrem bem o espectro de equívocos esperados.
  - originalidade: 3/5 — O contexto de crescimento bacteriano é um clássico recorrente em livros didáticos para introduzir PG/exponencial, pouco inovador. Além disso, a tabela já revela imediatamente a razão constante (300/100=3, etc.), o que configura um leve 'efeito Topaze': o padrão fica evidente antes mesmo de qualquer raciocínio sobre a natureza da função, reduzindo o desafio interpretativo.
