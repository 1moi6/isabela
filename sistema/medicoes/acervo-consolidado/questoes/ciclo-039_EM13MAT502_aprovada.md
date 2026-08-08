# Ciclo 039 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

A tabela abaixo relaciona o comprimento $L$ do lado de um certo tipo de figura com a grandeza $A$ associada a ela, para quatro valores de $L$:

| $L$ | $A$ |
|---|---|
| 1 | 3 |
| 2 | 12 |
| 3 | 27 |
| 4 | 48 |

Investigando os pares de valores dessa tabela, qual expressão algébrica, escrita em função de $L$, generaliza corretamente a relação entre $A$ e $L$ para todos os pares apresentados (e não apenas para alguns deles)?

## Alternativas

- (a) $A = 3L^2$  ← correta
- (b) $A = 3L$
  - *erro representado:* Aluno percebe que a razão A/L cresce, mas erra ao supor proporcionalidade direta simples usando apenas o primeiro par (3/1=3), sem perceber que essa razão não se mantém constante para os demais pontos.
- (c) $A = L^2 + 2$
  - *erro representado:* Aluno ajusta uma expressão quadrática apenas para o primeiro par de valores (1²+2=3), somando uma constante em vez de multiplicar, e não testa se a fórmula vale para os demais pares da tabela.
- (d) $A = 9L - 6$
  - *erro representado:* Aluno assume erroneamente que a relação é linear e ajusta uma reta usando apenas os dois primeiros pontos (1,3) e (2,12), obtendo o coeficiente angular 9 e extrapolando essa reta para toda a tabela, sem perceber que ela falha nos pontos seguintes.

## Gabarito

A = 3L²

## Resolução

**Passo 1 — Testar um modelo linear simples.**
Se a relação fosse do tipo $A = kL$, o valor de $k = A/L$ deveria ser constante. Calculando: $3/1=3$, $12/2=6$, $27/3=9$, $48/4=12$. Como $k$ não é constante, a relação **não é linear** (não é do tipo $A=kL$).

**Passo 2 — Observar como $A$ cresce em relação a $L$.**
As diferenças sucessivas de $A$ são: $12-3=9$, $27-12=15$, $48-27=21$. Essas diferenças não são constantes (o que confirmaria uma reta), mas crescem de forma regular: $15-9=6$ e $21-15=6$. Uma segunda diferença constante é a marca característica de uma função **quadrática**.

**Passo 3 — Testar um modelo do tipo $A = aL^2$.**
Como a razão $A/L$ não é constante, mas $A$ parece crescer com o quadrado de $L$, testamos a razão $A/L^2$: $3/1^2=3$, $12/2^2=3$, $27/3^2=3$, $48/4^2=3$. Essa razão é constante e igual a $3$ para todos os pares.

**Passo 4 — Escrever a generalização.**
Como $A/L^2 = 3$ para todos os pontos da tabela, concluímos que $A = 3L^2$.

**Verificação final:** $L=1\Rightarrow 3(1)^2=3$; $L=2\Rightarrow 3(4)=12$; $L=3\Rightarrow 3(9)=27$; $L=4\Rightarrow 3(16)=48$. Todos os pares conferem, confirmando que a relação é do tipo $y=ax^2$, com $a=3$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'pontos': '[(1,3),(2,12),(3,27),(4,48)]', 'grau': '2', 'forma': 'a*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado apresenta dados completos em tabela, pergunta única e sem ambiguidade: pede-se a expressão algébrica que relaciona y a x a partir dos pares dados.
  - adequacao_nivel: 2/5 — O Bloom declarado é 'criar', que exige produzir/gerar uma generalização original (SOLO: nível relacional/estendido abstrato, resposta aberta). No entanto, o formato de múltipla escolha reduz a tarefa a testar/comparar quatro expressões prontas contra a tabela — processo de 'analisar' ou no máximo 'aplicar', não de 'criar'. O estudante não constrói a lei de formação por si mesmo; apenas verifica qual alternativa se ajusta. Há incompatibilidade estrutural entre o processo cognitivo declarado e o exigido pela questão.
  - alinhamento_bncc: 3/5 — Cumpre os requisitos específicos: dados em tabela (não em expressão pronta), pedido de generalização algébrica, e reconhecimento da relação y=ax². Porém a habilidade EM13MAT502 enfatiza 'criar conjecturas para generalizar e expressar algebricamente' — um processo ativo de construção — que fica esvaziado pelo formato de múltipla escolha, que transforma a criação em reconhecimento/seleção. A dimensão de representação no plano cartesiano, mencionada na habilidade, também não é explorada, embora isso seja um aspecto secundário.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e bem fundamentados: extrapolação precipitada de proporcionalidade direta a partir de um único par, confusão entre a segunda diferença (2a) e o coeficiente a, e ajuste apressado de uma função quadrática pura testando apenas o primeiro par. Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 3/5 — O contexto ('experimento' genérico, tabela numérica abstrata) é o clássico exercício de proporcionalidade quadrática presente em praticamente todo livro didático. Não há contextualização significativa (situação real, dado de fenômeno físico com significado) nem elementos que tornem o problema memorável ou motivador; a estrutura segue o roteiro-padrão de 'teste de razões' sem inovação de abordagem.
  - *sugestões:* 1) Reformular o formato: transformar a questão em resposta aberta (dissertativa) ou em uma sequência de sub-tarefas (ex.: pedir que o aluno primeiro represente os pontos no plano cartesiano, depois teste as razões y/x e y/x², e por fim escreva a lei de formação), de modo que o aluno efetivamente construa a generalização em vez de apenas escolher entre opções prontas — isso alinha o processo cognitivo real ao nível 'criar' declarado. 2) Se for necessário manter múltipla escolha por razões de formato de prova, rebaixar o Bloom declarado para 'analisar' ou 'aplicar', que é o que a tarefa de fato demanda. 3) Incluir explicitamente a etapa de representação no plano cartesiano, conforme previsto na habilidade EM13MAT502 (por exemplo, apresentando o gráfico dos pontos como parte do enunciado ou pedindo que o aluno o esboce). 4) Contextualizar a tabela com uma situação real e significativa (ex.: distância percorrida em queda livre, área de uma figura em função do lado, etc.) para aumentar a originalidade e o significado da tarefa, evitando o padrão genérico de 'tabela de experimento'.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reformular o formato: transformar a questão em resposta aberta (dissertativa) ou em uma sequência de sub-tarefas (ex.: pedir que o aluno primeiro represente os pontos no plano cartesiano, depois teste as razões y/x e y/x², e por fim escreva a lei de formação), de modo que o aluno efetivamente construa a generalização em vez de apenas escolher entre opções prontas — isso alinha o processo cognitivo real ao nível 'criar' declarado. 2) Se for necessário manter múltipla escolha por razões de formato de prova, rebaixar o Bloom declarado para 'analisar' ou 'aplicar', que é o que a tarefa de fato demanda. 3) Incluir explicitamente a etapa de representação no plano cartesiano, conforme previsto na habilidade EM13MAT502 (por exemplo, apresentando o gráfico dos pontos como parte do enunciado ou pedindo que o aluno o esboce). 4) Contextualizar a tabela com uma situação real e significativa (ex.: distância percorrida em queda livre, área de uma figura em função do lado, etc.) para aumentar a originalidade e o significado da tarefa, evitando o padrão genérico de 'tabela de experimento'.

### Iteração 2

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é limpo, a tabela é bem apresentada, e a pergunta final é inequívoca quanto ao que se pede (expressão algébrica válida para todos os pares).
  - adequacao_nivel: 2/5 — O nível declarado é 'criar', mas o próprio enunciado já executa quase todo o processo cognitivo esperado do aluno: calcula as diferenças sucessivas, calcula as segundas diferenças, afirma que são constantes, e ainda sugere explicitamente testar a razão A/L². Ao aluno resta apenas verificar uma conta já indicada, o que corresponde no máximo a 'aplicar' (SOLO: uniestrutural/multiestrutural), não a 'criar' uma generalização a partir de investigação própria.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT502 exige que o estudante investigue, identifique padrões e crie a generalização algébrica. Aqui a investigação (diferenças, segundas diferenças, razão A/L²) é entregue pronta no enunciado; o estudante não a realiza, apenas confirma uma conclusão já apresentada. A questão viola o espírito da habilidade mesmo cumprindo formalmente o requisito de 'a expressão não vem pronta' — o *processo* de generalização, que é o núcleo da habilidade, foi feito pelo enunciado e não pelo aluno.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e bem fundamentados: proporcionalidade direta ingênua (A=3L), ajuste pontual sem coeficiente (L²+2) e extrapolação linear a partir de apenas dois pontos (9L-6). Nenhum é trivialmente eliminável sem cálculo, e cada um reflete um raciocínio incompleto real de estudantes.
  - originalidade: 2/5 — Apesar do contexto de esquadros ser um verniz interessante, o enunciado sofre forte 'efeito Topaze': descreve a curva como 'arco de parábola', fornece as diferenças já calculadas e ainda indica a razão A/L² a ser testada — pistas que pavimentam quase integralmente a solução, esvaziando o desafio de generalização que a questão deveria propor.
  - *sugestões:* Reescrever o enunciado retirando as etapas de investigação já resolvidas: (1) não apresentar as diferenças sucessivas nem as segundas diferenças calculadas; (2) não descrever a curva como 'arco de parábola' nem mencionar que 'se curva cada vez mais acentuadamente'; (3) não sugerir a razão A/L² a ser testada. Deixar apenas a tabela de pares (L, A) e a pergunta 'qual expressão algébrica generaliza a relação para todos os pares?', de modo que o próprio estudante precise conduzir a investigação (testar diferenças, tentar razões, propor hipóteses) e chegar sozinho à conjectura A = 3L². Isso restaura o nível cognitivo 'criar' e alinha a questão de fato ao processo exigido pela habilidade EM13MAT502, mantendo os mesmos distratores, que já são de boa qualidade.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reescrever o enunciado retirando as etapas de investigação já resolvidas: (1) não apresentar as diferenças sucessivas nem as segundas diferenças calculadas; (2) não descrever a curva como 'arco de parábola' nem mencionar que 'se curva cada vez mais acentuadamente'; (3) não sugerir a razão A/L² a ser testada. Deixar apenas a tabela de pares (L, A) e a pergunta 'qual expressão algébrica generaliza a relação para todos os pares?', de modo que o próprio estudante precise conduzir a investigação (testar diferenças, tentar razões, propor hipóteses) e chegar sozinho à conjectura A = 3L². Isso restaura o nível cognitivo 'criar' e alinha a questão de fato ao processo exigido pela habilidade EM13MAT502, mantendo os mesmos distratores, que já são de boa qualidade.

### Iteração 3

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — Enunciado bem estruturado: tabela completa com quatro pares, pergunta explícita sobre generalização algébrica válida para todos os pares (frisando explicitamente 'não apenas para alguns'). Não há ambiguidade lexical ou estrutural. Pequeno ponto de melhoria: o termo 'grandeza A' fica vago sem contexto geométrico concreto (não se diz que figura é essa), o que reduz um pouco a precisão contextual, mas não compromete a compreensão da tarefa.
  - adequacao_nivel: 3/5 — O processo de investigar razões, testar hipóteses de linearidade e quadraticidade e formular a expressão A=3L² corresponde de fato a uma atividade de 'criar/generalizar' na fase de resolução mental do aluno. No entanto, o formato de múltipla escolha reduz a exigência estrutural: o estudante não precisa produzir a expressão do zero, apenas testá-la contra quatro alternativas já prontas, o que aproxima a tarefa de um nível 'analisar/aplicar' (testar candidatas) mais do que de 'criar' genuíno, tensionando a coerência entre o Bloom declarado e a estrutura SOLO esperada (que seria mais relacional/abstrata se a resposta fosse aberta).
  - alinhamento_bncc: 4/5 — Cumpre os requisitos centrais: dados apresentados em tabela, expressão algébrica ausente do enunciado, tarefa de generalização que conduz ao reconhecimento do padrão y=ax² (aqui A=3L²), com verificação sistemática via razões e diferenças finitas — processo compatível com 'investigar e generalizar'. Falta, porém, articulação explícita com a representação no plano cartesiano mencionada na habilidade (ainda que seja um componente acessório da habilidade, sua ausência deixa uma dimensão da EM13MAT502 não contemplada).
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e pedagogicamente informativos: (i) assumir proporcionalidade direta usando só o primeiro par; (ii) ajustar quadrática aditiva em vez de multiplicativa validando só um ponto; (iii) ajustar reta usando apenas dois pontos iniciais e extrapolar. Nenhum é absurdo ou trivialmente descartável sem cálculo, e todos exigem que o aluno teste contra os demais pares para descartá-los — o que reforça o objetivo da questão.
  - originalidade: 3/5 — O formato é o clássico exercício de 'complete a tabela e ache a lei de formação', comum em livros didáticos, sem contextualização significativa (a 'figura' e a grandeza A não são especificadas ou situadas em um problema real). Não há efeito Topaze evidente — a tabela não entrega pistas óbvias demais — mas a ausência de contexto aplicado limita o potencial de engajamento e a autenticidade da tarefa investigativa.
  - *sugestões:* Para elevar a qualidade: (1) Contextualizar a tabela em uma situação concreta (ex.: L = lado de um quadrado e A = área de uma peça decorativa feita com esse quadrado multiplicado por um fator, ou L = raio e A = alguma grandeza física proporcional ao quadrado), tornando o problema mais significativo e menos 'genérico'; (2) Considerar complementar a tarefa pedindo também a representação gráfica dos pontos no plano cartesiano (mesmo que como etapa description, não obrigatoriamente separada em subitem), para atender integralmente à habilidade EM13MAT502, que menciona explicitamente essa representação; (3) Se o objetivo é manter o nível 'criar' da Bloom de forma mais fiel, considerar formato de resposta aberta (não múltipla escolha) ou ao menos pedir que o aluno explicite o raciocínio de generalização como parte da resposta, já que o MC tende a reduzir a tarefa para 'testar candidatas' em vez de 'produzir' a expressão.
