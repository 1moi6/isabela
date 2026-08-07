# Ciclo 011 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Um aplicativo de transporte registrou, em um banco de dados, a distância percorrida (em km) e o valor cobrado (em reais) de quatro corridas distintas, conforme a tabela abaixo:

| Distância (km) | Valor cobrado (R$) |
|---:|---:|
| 1 | 8 |
| 2 | 11 |
| 4 | 17 |
| 7 | 26 |

Observando os pares de valores da tabela, qual expressão algébrica generaliza corretamente a relação entre a distância percorrida $x$ (em km) e o valor cobrado $y$ (em reais)?

## Alternativas

- (a) $y = 3x + 5$  ← correta
- (b) $y = 6x + 2$
  - *erro representado:* Calculou a taxa de variação dividindo a diferença total de y (26-8=18) pelo número de intervalos entre os pares na tabela (4 pares, 3 intervalos), obtendo a=6, em vez de usar a diferença real entre os valores de x (7-1=6, que daria a=3). Tratou a tabela como se as distâncias fossem consecutivas (posições 1,2,3,4) em vez dos valores reais de x.
- (c) $y = 3x + 8$
  - *erro representado:* Calculou corretamente a taxa de variação (a=3) a partir dos dois primeiros pares consecutivos, mas ao determinar o termo independente usou diretamente o valor de y para x=1 (b=8), sem subtrair o produto a·x1, esquecendo de isolar corretamente b na equação y=ax+b.
- (d) $y = x^2 + 7$
  - *erro representado:* Verificou o padrão apenas nos dois primeiros pares da tabela (x=1, y=8 e x=2, y=11), que também satisfazem essa função quadrática, e concluiu precipitadamente que a relação seria uma função polinomial do 2º grau, sem testar a hipótese com os demais pares (x=4 e x=7), que contradizem esse modelo.

## Gabarito

y = 3x + 5

## Resolução

**Passo 1 — Investigar a variação de $y$ em relação à variação de $x$.**

Como os valores de $x$ não são consecutivos (1, 2, 4, 7), é preciso calcular a taxa de variação $\dfrac{\Delta y}{\Delta x}$ usando as diferenças reais entre os valores de $x$, e não a posição dos pares na tabela:

$$\frac{11-8}{2-1}=\frac{3}{1}=3 \qquad \frac{17-11}{4-2}=\frac{6}{2}=3 \qquad \frac{26-17}{7-4}=\frac{9}{3}=3$$

**Passo 2 — Reconhecer o tipo de relação.**

Como a taxa de variação $\dfrac{\Delta y}{\Delta x}$ é **constante** (igual a 3) mesmo com intervalos desiguais entre os valores de $x$, a relação entre $x$ e $y$ é uma **função polinomial do 1º grau (função afim)**, da forma $y=ax+b$, com $a=3$.

Se a relação fosse quadrática ou de outro tipo, essa razão não seria a mesma para diferentes pares de pontos — é justamente essa constância, verificada em **todos** os pares (e não apenas nos dois primeiros), que garante o caráter linear/afim da relação.

**Passo 3 — Determinar o termo independente $b$.**

Usando o par $(1,8)$ na expressão $y=3x+b$:

$$8=3(1)+b \implies b=8-3=5$$

**Passo 4 — Escrever e conferir a expressão geral.**

$$y=3x+5$$

Conferindo com os demais pares: $x=2\Rightarrow y=3(2)+5=11$ ✓; $x=4\Rightarrow y=3(4)+5=17$ ✓; $x=7\Rightarrow y=3(7)+5=26$ ✓.

Todos os pares confirmam a expressão, evidenciando que a relação tabelada corresponde a uma **função polinomial do 1º grau**: $y=3x+5$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x + 5`, parâmetros `{'pontos': '[(1,8),(2,11),(4,17),(7,26)]', 'grau': '1'}`
- `funcao` — expressão `3*x + 5`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 2 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 4*x + 3 tem termo de grau 0 (3), fora da forma a*x. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=rejeitado
  - funcao/crescimento=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 2 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 4*x + 3 tem termo de grau 0 (3), fora da forma a*x. | (2) aprovado: Gabarito confirmado (crescente em Reals). Resultado calculado independentemente: a expressão 4*x + 3 tem termo de grau 0 (3), fora da forma a*x | crescente em Reals. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*x + 3: reproduz os 4 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (tabela x,y), o que é pedido (lei de formação e tipo de função) e não há ambiguidade lexical ou estrutural. Os dados são suficientes para resolver o problema.
  - adequacao_nivel: 3/5 — O nível declarado é 'analisar', mas o formato múltipla escolha com apenas 4 pontos tabulados permite que o estudante resolva por verificação pontual (testar cada alternativa em x=1, x=2...) em vez de efetivamente decompor o padrão e generalizar, o que reduz a exigência cognitiva real para 'aplicar/verificar'. Além disso, o enunciado pede explicitamente identificar 'o tipo de função', mas nenhuma alternativa contrasta tipos de função diferentes (todas são do 1º grau), de modo que essa dimensão da tarefa nunca é de fato exigida do estudante — apenas aparece no gabarito e na resolução, não na estrutura de resposta.
  - alinhamento_bncc: 3/5 — Cumpre os requisitos de dados em tabela e expressão não fornecida previamente, e pede generalização algébrica. Porém a habilidade exige 'reconhecer quando essa representação é de função polinomial de 1º grau' — como todas as alternativas são funções afins (nenhum distrator é de outro tipo, ex. quadrática ou não linear), essa etapa de reconhecimento nunca é efetivamente testada nas opções de resposta, ficando apenas mencionada na resolução do professor.
  - distratores: 3/5 — Os distratores 'y=4x' e 'y=3x+4' representam erros sistemáticos plausíveis (esquecer o termo independente e trocar os papéis de a e b). Já o distrator 'y=x+6' tem justificativa matematicamente inconsistente: a explicação diz que o erro viria de dividir a diferença total (12) pelo número de pares (4), o que resultaria em a=3, não em a=1 como na alternativa. Esse descompasso entre o texto do erro e o valor apresentado enfraquece a qualidade do distrator, que também é rapidamente eliminável testando um segundo par (x=2 já invalida a alternativa).
  - originalidade: 2/5 — É uma questão numérica descontextualizada, no formato clássico de 'complete a tabela e encontre a lei de formação', amplamente reproduzido em livros didáticos, sem qualquer situação real ou significativa que justifique o uso da função afim. Não há efeito Topaze evidente no enunciado em si, mas a ausência de contexto aplicado reduz o valor pedagógico e a originalidade da proposta.
  - *sugestões:* 1) Inserir um contexto significativo e realista (ex.: custo de um serviço, distância percorrida, crescimento de uma grandeza física) para substituir a tabela puramente numérica, tornando a tarefa mais motivadora e menos repetitiva. 2) Incluir ao menos uma alternativa com um tipo de função diferente (ex.: y = 4x² + 3 ou outra não linear) para que a exigência de 'reconhecer que é uma função polinomial do 1º grau', prevista na habilidade, seja de fato testada e não apenas mencionada na resolução. 3) Reformular o distrator 'y = x + 6' com uma justificativa de erro sistemático coerente com o valor numérico apresentado (por exemplo, um erro real que produza a=1, como usar apenas a diferença entre o primeiro e o segundo valor dividida por 4, ou confundir x com a posição do par na tabela). 4) Para elevar a exigência ao nível 'analisar' de fato, considerar aumentar a tabela com mais pares não consecutivos em x (por exemplo, x=1,2,4,7) obrigando o estudante a calcular a taxa de variação a partir de intervalos desiguais, dificultando a resolução por simples substituição/tentativa em cada alternativa.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Inserir um contexto significativo e realista (ex.: custo de um serviço, distância percorrida, crescimento de uma grandeza física) para substituir a tabela puramente numérica, tornando a tarefa mais motivadora e menos repetitiva. 2) Incluir ao menos uma alternativa com um tipo de função diferente (ex.: y = 4x² + 3 ou outra não linear) para que a exigência de 'reconhecer que é uma função polinomial do 1º grau', prevista na habilidade, seja de fato testada e não apenas mencionada na resolução. 3) Reformular o distrator 'y = x + 6' com uma justificativa de erro sistemático coerente com o valor numérico apresentado (por exemplo, um erro real que produza a=1, como usar apenas a diferença entre o primeiro e o segundo valor dividida por 4, ou confundir x com a posição do par na tabela). 4) Para elevar a exigência ao nível 'analisar' de fato, considerar aumentar a tabela com mais pares não consecutivos em x (por exemplo, x=1,2,4,7) obrigando o estudante a calcular a taxa de variação a partir de intervalos desiguais, dificultando a resolução por simples substituição/tentativa em cada alternativa.

### Iteração 3

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*x + 5: reproduz os 4 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado sem ambiguidade: dados completos na tabela, variável independente e dependente claramente identificadas, pergunta objetiva (encontrar expressão algébrica geral).
  - adequacao_nivel: 4/5 — A exigência de calcular a taxa de variação usando as diferenças reais de x (não consecutivos) e verificar a constância em todos os pares, não apenas nos dois primeiros, força um processo de análise relacional (SOLO relacional), compatível com o nível 'analisar' de Bloom. Poderia exigir ainda mais integração (ex.: pedir justificativa do porquê não é quadrática) para atingir o nível máximo de análise.
  - alinhamento_bncc: 5/5 — Cumpre as três exigências: dados apresentados em tabela, pede generalização algébrica (não valor isolado) e conduz ao reconhecimento explícito de que a relação é uma função polinomial de 1º grau, alinhado a EM13MAT501.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e distintos: (1) confundir posição na tabela com valor real de x ao calcular a taxa, (2) erro de isolamento algébrico ao calcular b, (3) generalização precipitada a partir de apenas dois pontos, ignorando os demais. Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 4/5 — O contexto de aplicativo de transporte é atual e o uso de valores de x não consecutivos evita o padrão mecânico de tabelas com incrementos unitários, exigindo raciocínio mais cuidadoso. Ainda assim, a estrutura geral (tabela → encontrar y=ax+b) é um formato consagrado, sem inovação adicional no contexto ou na formulação da pergunta.
