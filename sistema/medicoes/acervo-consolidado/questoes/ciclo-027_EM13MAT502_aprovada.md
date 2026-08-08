# Ciclo 027 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Observe a tabela abaixo, que relaciona valores de x com valores de y:

| x | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| y | 4 | 16 | 36 | 64 |

a) Investigue como y varia em função de x, testando se há proporcionalidade direta, proporcionalidade com o quadrado de x, ou outra relação.

b) Escreva a lei algébrica y = f(x) que generaliza o padrão observado na tabela, e classifique o tipo de função obtida.

## Gabarito

y = 4x²

## Resolução

**Passo 1 — Testar proporcionalidade direta (y = ax):**

Se fosse y proporcional a x, a razão $y/x$ deveria ser constante. Calculando:

$\frac{4}{1}=4,\quad \frac{16}{2}=8,\quad \frac{36}{3}=12,\quad \frac{64}{4}=16$

Como essas razões não são constantes, y não é diretamente proporcional a x.

**Passo 2 — Testar proporcionalidade ao quadrado de x (y = ax²):**

Calculamos a razão $y/x^2$ para cada par:

$\frac{4}{1^2}=4,\quad \frac{16}{2^2}=4,\quad \frac{36}{3^2}=4,\quad \frac{64}{4^2}=4$

A razão é constante e igual a $4$ em todos os casos, o que indica que y é proporcional ao quadrado de x.

**Passo 3 — Escrever a lei geral:**

Como $\frac{y}{x^2}=4$ para todos os pares da tabela, concluímos que:

$$y = 4x^2$$

**Passo 4 — Verificação:**

$x=1: y=4(1)^2=4$ ✓
$x=2: y=4(2)^2=16$ ✓
$x=3: y=4(3)^2=36$ ✓
$x=4: y=4(4)^2=64$ ✓

**Conclusão:** A lei $y=4x^2$ é uma função polinomial do 2º grau do tipo $y=ax^2$ (sem termos de grau 1 ou constante), pois y é diretamente proporcional ao quadrado de x, com constante de proporcionalidade $a=4$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*x**2`, parâmetros `{'pontos': '[(1,4),(2,16),(3,36),(4,64)]', 'grau': '2', 'forma': 'a*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é objetivo, os dados da tabela são completos e a tarefa (a) e (b) está bem delimitada. Falta apenas indicar que a análise deveria incluir a representação no plano cartesiano, mencionada na habilidade, mas isso não gera ambiguidade na leitura do que é pedido.
  - adequacao_nivel: 2/5 — O item (a) já entrega o caminho de resolução ('testando se a razão entre y e x, e depois entre y e x² é constante'), reduzindo a tarefa a um procedimento de verificação guiado (nível 'aplicar', estrutura SOLO multiestrutural) em vez de exigir que o aluno investigue e decida por si mesmo qual relação testar, como pede o nível 'analisar' declarado. O aluno não precisa comparar hipóteses concorrentes nem justificar a escolha do teste — apenas executa o cálculo indicado.
  - alinhamento_bncc: 3/5 — A questão trata do conteúdo certo (y=ax²) e pede a generalização algébrica a partir de uma tabela, cumprindo parte da habilidade. Porém: (1) não solicita a representação no plano cartesiano exigida pelo texto da habilidade; (2) a 'investigação' e a 'conjectura' ficam praticamente anuladas pelo comando que já indica o procedimento exato a seguir, contrariando o espírito de 'criar conjecturas' de forma autônoma.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — É o exemplo mais clássico e mecânico de introdução a y=ax² (tabela com razão y/x² constante, sem contexto), e o comando do item (a) funciona como forte pista ('efeito Topaze'), entregando a estratégia de solução em vez de deixar o aluno descobri-la. Não há contextualização significativa (física, geometria, etc.).
  - *sugestões:* 1) Reescreva o item (a) sem indicar qual razão testar; peça apenas algo como 'investigue como y varia em função de x e proponha uma expressão algébrica que descreva essa variação', deixando o aluno decidir testar y/x, y/x² ou outra relação — isso resgata o nível 'analisar' e a autonomia da conjectura exigida pela BNCC. 2) Inclua a solicitação de representar os pares (x,y) no plano cartesiano antes da generalização algébrica, para atender integralmente à habilidade EM13MAT502. 3) Contextualize a tabela com uma situação significativa (ex.: área de um terreno quadrado em função do lado, energia cinética em função da velocidade, distância de frenagem etc.) para aumentar a originalidade e o significado do problema. 4) Se desejar manter o formato guiado, ajuste o nível de Bloom declarado para 'aplicar', em vez de 'analisar', para haver coerência entre o comando e a taxonomia.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reescreva o item (a) sem indicar qual razão testar; peça apenas algo como 'investigue como y varia em função de x e proponha uma expressão algébrica que descreva essa variação', deixando o aluno decidir testar y/x, y/x² ou outra relação — isso resgata o nível 'analisar' e a autonomia da conjectura exigida pela BNCC. 2) Inclua a solicitação de representar os pares (x,y) no plano cartesiano antes da generalização algébrica, para atender integralmente à habilidade EM13MAT502. 3) Contextualize a tabela com uma situação significativa (ex.: área de um terreno quadrado em função do lado, energia cinética em função da velocidade, distância de frenagem etc.) para aumentar a originalidade e o significado do problema. 4) Se desejar manter o formato guiado, ajuste o nível de Bloom declarado para 'aplicar', em vez de 'analisar', para haver coerência entre o comando e a taxonomia.

### Iteração 2

- **Verificador:** rejeitado — Propriedade não confirmada: a expressão 4*x**2 vale 4*x**2 em a=2, mas a tabela dá 16.
  - propriedade=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: Propriedade não confirmada: a expressão 4*x**2 vale 4*x**2 em a=2, mas a tabela dá 16. Resultado calculado independentemente: a expressão 4*x**2 vale 4*x**2 em a=2, mas a tabela dá 16. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Propriedades confirmadas para 4*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (tabela x,y), a tarefa (investigar tipo de relação) e o produto esperado (lei algébrica e classificação). Não há ambiguidade lexical ou estrutural, e os dados numéricos são suficientes para a generalização.
  - adequacao_nivel: 4/5 — A tarefa exige comparar razões y/x e y/x² e integrar essa comparação numa conclusão geral, o que corresponde a um processo relacional/analítico compatível com 'analisar'. Contudo, o enunciado já nomeia explicitamente as hipóteses a testar ('proporcionalidade direta, proporcionalidade com o quadrado de x'), o que reduz parcialmente a exigência de o próprio aluno formular essas conjecturas — um traço mais de aplicação guiada do que de análise plena.
  - alinhamento_bncc: 5/5 — Cumpre as exigências elencadas pelo professor: os dados chegam como tabela (sem fórmula pronta), pede-se a generalização algébrica do padrão, e a resolução leva ao reconhecimento de y=ax² com a variável proporcional ao quadrado da outra. A habilidade completa da BNCC também menciona representação no plano cartesiano, que não é exigida aqui, mas isso não constava como exigência obrigatória na especificação do professor.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto é puramente numérico/abstrato, sem situação significativa. Além disso, o item (a) já entrega ao aluno as três hipóteses possíveis a testar ('proporcionalidade direta, com o quadrado de x, ou outra relação'), funcionando como forte pista que pavimenta o caminho da solução (efeito Topaze), reduzindo o espaço de investigação autônoma esperado pela habilidade.
