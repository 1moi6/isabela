# Ciclo 053 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma academia cobra R$ 70,00 pela mensalidade do primeiro mês de plano. A partir do segundo mês, o valor da mensalidade aumenta R$ 8,00 em relação ao mês imediatamente anterior, e esse padrão se mantém indefinidamente. Chame de $n$ o número do mês (com $n = 1, 2, 3, \dots$) e de $f(n)$ o valor da mensalidade cobrada nesse mês. Construa a lei que expressa $f(n)$ em função de $n$, levando em conta o conjunto de valores que $n$ pode assumir, e use essa lei para determinar o valor da mensalidade no 15º mês.

## Alternativas

- (a) R$ 182,00  ← correta
- (b) R$ 190,00
  - *erro representado:* Erro de deslocamento de índice: usar $f(n) = 70 + 8n$ em vez de $f(n) = 70 + 8(n-1)$, como se a primeira mensalidade correspondesse a $n=0$, somando um aumento a mais do que deveria.
- (c) R$ 1.050,00
  - *erro representado:* Confundir função afim com função linear (proporcional): tratar a mensalidade como diretamente proporcional ao mês, calculando $f(n) = 70n$, sem considerar que a taxa de variação é $8$ e não $70$.
- (d) R$ 120,00
  - *erro representado:* Calcular apenas o total acumulado de aumentos ($8 \times 15$), esquecendo de somar o valor inicial da mensalidade ($a_1 = 70$).

## Gabarito

R$ 182,00

## Resolução

**Passo 1 — Reconhecer o padrão da sequência.**

Os valores das mensalidades são $70, 78, 86, 94, \dots$. A diferença entre um termo e o anterior é sempre a mesma, $8$, o que caracteriza uma **progressão aritmética (PA)** de primeiro termo $a_1 = 70$ e razão $r = 8$.

**Passo 2 — Obter o termo geral da PA.**

$$a_n = a_1 + (n-1)\cdot r = 70 + 8(n-1) = 8n + 62$$

**Passo 3 — Associar a PA a uma função afim.**

A expressão $a_n = 8n + 62$ tem a forma $f(n) = an + b$, com $a=8$ e $b=62$, que é exatamente a lei de uma **função afim**. Assim, a mensalidade no mês $n$ pode ser escrita como

$$f(n) = 8n + 62.$$

**Passo 4 — Identificar o domínio.**

Diferente de uma função afim genérica $f(x) = ax+b$ definida para todo $x$ real, aqui $n$ representa a *ordem do mês* — só faz sentido para valores inteiros positivos ($n=1,2,3,\dots$). Logo, o domínio de $f$ é o conjunto dos números naturais positivos, $\mathbb{N}^\ast$ (domínio **discreto**), e não o conjunto dos reais.

**Passo 5 — Calcular o valor pedido.**

$$f(15) = 8\cdot 15 + 62 = 120 + 62 = 182.$$

Portanto, a mensalidade no 15º mês é **R$ 182,00**.

## Formalização verificável

- `progressao` — expressão `-`, esperado `182`, parâmetros `{'tipo_progressao': 'pa', 'a1': '70', 'razao': '8', 'n': '15', 'consulta': 'termo'}`
- `propriedade` — expressão `-`, esperado `8*n + 62`, parâmetros `{'sequencia': 'pa', 'a1': '70', 'razao': '8', 'grau': '1', 'forma': 'a*n + b'}`
- `funcao` — expressão `8*n + 62`, esperado `182`, parâmetros `{'consulta': 'valor', 'ponto': '15'}`
- `funcao` — expressão `8*n + 62`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(15) = 182). | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (termo da PA = 182). | (4) aprovado: Propriedades confirmadas para 8*n + 62: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada.
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
  - progressao/termo=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é lexical e estruturalmente inequívoco: dados completos (valor inicial, razão, mês pedido) e pergunta objetiva. Não há ambiguidade, mas a clareza vem acompanhada de excesso de informação pré-mastigada (ver críticas em outros critérios).
  - adequacao_nivel: 2/5 — O enunciado já afirma explicitamente que a sequência é uma PA de razão 8, que ela pode ser representada por uma função afim de domínio discreto, e até nomeia a forma f(n)=a_n. Ao aluno resta apenas substituir n=15 numa fórmula essencialmente fornecida. Isso corresponde ao nível 'aplicar' (SOLO uniestrutural), não a 'analisar' (que exigiria o aluno próprio identificar a estrutura de PA, decidir a forma da função afim e justificar a discretização do domínio).
  - alinhamento_bncc: 2/5 — A especificação exige que a associação PA↔função afim seja *exigida pelo enunciado*, não meramente informada. Aqui o texto faz essa associação pelo próprio professor/autor da questão ('a sequência (a_n) é uma PA de razão 8... pode ser representada por uma função afim... domínio discreto'), eliminando exatamente o trabalho cognitivo que a habilidade EM13MAT507 pretende avaliar. O aluno só aplica uma fórmula já entregue — não identifica, não associa, não analisa propriedades do domínio discreto por conta própria.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos plausíveis e distintos (deslocamento de índice, troca de papéis entre a1 e r, confusão entre termo geral e soma dos termos), sem opções absurdas ou trivialmente descartáveis.
  - originalidade: 2/5 — O contexto (mensalidade progressiva) é razoavelmente aplicado, mas o enunciado sofre forte efeito Topaze: fornece a classificação da sequência como PA, a razão, a forma funcional afim e a justificativa do domínio discreto antes de perguntar qualquer coisa — pavimentando quase toda a solução e deixando apenas a substituição numérica para o aluno.
  - *sugestões:* Reescreva o enunciado retirando as afirmações prontas de que a sequência é uma PA de razão 8, de que ela é representável por uma função afim e de que o domínio é discreto — essas conclusões devem ser produzidas pelo aluno, não fornecidas. Sugestão de estrutura: apresente apenas os fatos brutos (mensalidade inicial R$70, aumento de R$8 por mês) e peça explicitamente que o aluno (a) reconheça a natureza da sequência, (b) construa a lei da função afim correspondente especificando seu domínio (por que é discreto e não real) e (c) use essa lei para calcular o valor no 15º mês — exigindo a articulação real entre PA e função afim, coerente com o nível 'analisar' da habilidade EM13MAT507, e sem entregar a fórmula ou a classificação previamente.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reescreva o enunciado retirando as afirmações prontas de que a sequência é uma PA de razão 8, de que ela é representável por uma função afim e de que o domínio é discreto — essas conclusões devem ser produzidas pelo aluno, não fornecidas. Sugestão de estrutura: apresente apenas os fatos brutos (mensalidade inicial R$70, aumento de R$8 por mês) e peça explicitamente que o aluno (a) reconheça a natureza da sequência, (b) construa a lei da função afim correspondente especificando seu domínio (por que é discreto e não real) e (c) use essa lei para calcular o valor no 15º mês — exigindo a articulação real entre PA e função afim, coerente com o nível 'analisar' da habilidade EM13MAT507, e sem entregar a fórmula ou a classificação previamente.

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PA = 182). | (2) aprovado: Propriedades confirmadas para 8*n + 62: grau 1; forma a*n + b; coincide com a PA declarada. | (3) aprovado: Gabarito confirmado (f(15) = 182). | (4) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals).
  - progressao/termo=aprovado
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente os dados (valor inicial, aumento constante), a variável n e o que é pedido (lei geral e valor no mês 15). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — A tarefa exige reconhecer o padrão, converter termo geral de PA em função afim e considerar o domínio discreto — isso vai além de mera aplicação mecânica de fórmula, mas ainda é predominantemente um processo de tradução/aplicação (Bloom: aplicar/entender) e não uma análise no sentido de comparar, diferenciar ou avaliar estruturas concorrentes. A estrutura de resposta é relacional (SOLO), mas não chega a 'analisar' no sentido pleno de decompor e justificar escolhas entre representações.
  - alinhamento_bncc: 4/5 — O enunciado força a articulação entre PA e função afim ao pedir explicitamente a construção da lei 'levando em conta o conjunto de valores que n pode assumir', e a resolução trata o domínio discreto de forma explícita, como exige a especificação. Falta apenas nomear ou instigar o aluno a comparar explicitamente com a função afim contínua para reforçar a distinção discreto/contínuo de forma mais direta no enunciado (não só na resolução).
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis (deslocamento de índice, confusão afim/linear, esquecimento do termo inicial). Nenhum é absurdo ou trivialmente eliminável, embora o distrator de R$1.050,00 seja numericamente bem distante dos demais, o que pode facilitar sua eliminação por estimativa grosseira.
  - originalidade: 4/5 — O contexto de mensalidade de academia é aplicado e razoavelmente significativo, fugindo do exemplo clássico de 'sequência numérica pura'. Contudo, a instrução 'Construa a lei... Chame de n... f(n)' funciona como forte andaime que já indica o caminho de resolução (leve efeito Topaze), reduzindo um pouco a exigência de descoberta autônoma do aluno.
