# Ciclo 048 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

A tabela a seguir apresenta pares de valores (x, y) gerados por uma mesma regra de formação:

| x  | -2 | -1 | 0 | 1 | 2 |
|----|----|----|---|---|---|
| y  | 1  | 3  | 5 | 7 | 9 |

a) Investigue os pares (x, y) da tabela, identifique um padrão entre os valores de x e y e escreva, com suas próprias palavras, a expressão algébrica y = f(x) que gera esses valores. Justifique por escrito como você chegou a essa expressão.

b) Com base no padrão observado, classifique o tipo de função obtida (por exemplo: constante, polinomial do 1º grau, polinomial do 2º grau etc.) e justifique sua classificação.

c) Assinale a alternativa que apresenta corretamente a lei de formação encontrada.

(Os itens a e b devem ser respondidos de forma discursiva e serão corrigidos separadamente, avaliando o processo de investigação e a justificativa apresentada; o item c será corrigido de forma objetiva.)

## Alternativas

- (a) y = 2x + 5  ← correta
- (b) y = 2x + 1
  - *erro representado:* Tomou o valor de y do primeiro par da tabela (x=-2, y=1) como se fosse o termo independente b, sem recalcular o valor de y quando x=0.
- (c) y = 2x
  - *erro representado:* Identificou corretamente a taxa de variação constante (a=2), mas concluiu erroneamente que a função é uma proporcionalidade direta, ignorando o termo independente b.
- (d) y = x² + 5
  - *erro representado:* Confundiu a função afim com uma função quadrática, associando incorretamente a variação constante de y a um padrão de segundo grau.

## Gabarito

y = 2x + 5 (alternativa A)

## Resolução

**Item a) e b) — investigação do padrão**

Organizando as diferenças sucessivas dos valores de $y$ para cada aumento de 1 unidade em $x$:

$3-1=2,\quad 5-3=2,\quad 7-5=2,\quad 9-7=2$

A diferença é **constante e igual a 2** sempre que $x$ aumenta 1 unidade. Isso indica que a taxa de variação $\dfrac{\Delta y}{\Delta x}$ é constante, o que é a característica que define uma **função polinomial do 1º grau (função afim)**, do tipo $y = ax+b$, com $a\neq 0$.

Como a taxa de variação é $a=2$, e pelo par $(0,5)$ temos $y=5$ quando $x=0$, segue que $b=5$.

Logo, a lei de formação é:

$$y = 2x+5$$

Verificação com os demais pontos: $x=-2 \Rightarrow y=2(-2)+5=1$ ✓; $x=1 \Rightarrow y=2(1)+5=7$ ✓; $x=2 \Rightarrow y=2(2)+5=9$ ✓.

Como $a=2\neq 0$ e o expoente de $x$ é 1, confirma-se que se trata de uma **função polinomial do 1º grau**.

**Item c)**

A alternativa que apresenta corretamente essa lei é $y=2x+5$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `2*x + 5`, parâmetros `{'pontos': '[(-2,1),(-1,3),(0,5),(1,7),(2,9)]', 'grau': '1'}`
- `funcao` — expressão `2*x + 5`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*x + 2: reproduz os 4 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta a tabela de forma limpa, os dados são completos e a solicitação (lei de formação + classificação) é inequívoca. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O Bloom declarado é 'criar', mas o processo cognitivo exigido é apenas calcular diferenças constantes e substituir em y=ax+b — um procedimento fechado e rotineiro (mais próximo de 'aplicar'). Além disso, o formato de múltipla escolha contradiz o nível 'criar': o estudante não produz a generalização, apenas reconhece qual das opções prontas bate com o padrão. A estrutura SOLO fica multiestrutural (duas etapas de cálculo), não relacional/extended abstract como se esperaria de 'criar'.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT501 exige investigar padrões, REPRESENTAR NO PLANO CARTESIANO, criar conjecturas e generalizar algebricamente. A questão cumpre apenas parcialmente: fornece a tabela (ok) e pede a lei algébrica e a classificação (ok), mas não solicita em nenhum momento a representação gráfica nem exige que o aluno formule e teste uma conjectura própria — o caminho é mecânico (diferenças constantes → a = 3 → substituir um ponto). Falta o componente de plano cartesiano e o caráter de 'criar conjecturas', reduzindo a questão a mera aplicação de fórmula.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis (troca de a e b, uso indevido de y(1) como b, confusão com PG/função exponencial). Nenhum é absurdo ou trivialmente eliminável, embora o distrator exponencial seja um pouco mais fácil de descartar por um aluno atento à tabela ser aritmética, o que reduz ligeiramente sua força.
  - originalidade: 2/5 — É o exercício-padrão de livro didático sobre função afim a partir de tabela, sem contexto significativo (não há situação real, apenas x e y abstratos). O enunciado também sofre efeito Topaze: ao pedir explicitamente 'lei de formação... e classifique o tipo de função', já sinaliza que se trata de uma função com nome a ser identificado, reduzindo o desafio de descoberta.
  - *sugestões:* 1) Ajustar o nível cognitivo: se o Bloom declarado é 'criar', abandonar o formato múltipla escolha (que já entrega as respostas prontas) e pedir resposta aberta em que o aluno construa a lei e justifique o processo de generalização, ou reformular o Bloom declarado para 'aplicar/analisar', que é o que a questão realmente exige. 2) Incluir explicitamente a etapa de representação no plano cartesiano (pedir para plotar os pontos e observar o alinhamento) antes de generalizar algebricamente, para atender integralmente à habilidade EM13MAT501. 3) Pedir que o aluno formule uma conjectura sobre o comportamento da função (ex.: 'o que ocorre com y quando x aumenta uma unidade? Generalize essa observação') em vez de apenas 'determine a lei', tornando o processo de criação mais explícito. 4) Contextualizar a tabela em uma situação real (custo, distância, tempo etc.) para aumentar a significância e reduzir o caráter mecânico/repetitivo do exercício. 5) Se mantiver múltipla escolha, reduzir as pistas do enunciado (evitar palavras como 'lei de formação' e 'classifique o tipo' que já indicam a resposta esperada), preservando o desafio de descoberta do padrão.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar o nível cognitivo: se o Bloom declarado é 'criar', abandonar o formato múltipla escolha (que já entrega as respostas prontas) e pedir resposta aberta em que o aluno construa a lei e justifique o processo de generalização, ou reformular o Bloom declarado para 'aplicar/analisar', que é o que a questão realmente exige. 2) Incluir explicitamente a etapa de representação no plano cartesiano (pedir para plotar os pontos e observar o alinhamento) antes de generalizar algebricamente, para atender integralmente à habilidade EM13MAT501. 3) Pedir que o aluno formule uma conjectura sobre o comportamento da função (ex.: 'o que ocorre com y quando x aumenta uma unidade? Generalize essa observação') em vez de apenas 'determine a lei', tornando o processo de criação mais explícito. 4) Contextualizar a tabela em uma situação real (custo, distância, tempo etc.) para aumentar a significância e reduzir o caráter mecânico/repetitivo do exercício. 5) Se mantiver múltipla escolha, reduzir as pistas do enunciado (evitar palavras como 'lei de formação' e 'classifique o tipo' que já indicam a resposta esperada), preservando o desafio de descoberta do padrão.

### Iteração 2

- **Verificador:** aprovado — Propriedades confirmadas para 3*x + 5: reproduz os 4 pontos dados; grau 1.
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é bem estruturado, com tabela completa e itens a, b, c claramente delimitados. Pequena falha: os itens a) e b) pedem ações (marcar pontos, comparar variações) que não têm como ser verificadas em uma resposta de múltipla escolha, gerando uma leve incoerência entre o que se pede e o que se avalia.
  - adequacao_nivel: 2/5 — O nível declarado é 'criar' (produção de uma generalização algébrica original a partir de padrão observado), mas o formato múltipla escolha reduz a tarefa final a reconhecer entre quatro fórmulas prontas — o que corresponde, no máximo, a 'aplicar' ou 'analisar'. A estrutura SOLO esperada para 'criar' seria uma resposta construída (relacional/extended abstract), não uma seleção. Os subitens a) e b), que efetivamente exigiriam processos de análise e criação, não são avaliáveis no formato adotado, esvaziando o processo cognitivo real exigido do aluno.
  - alinhamento_bncc: 3/5 — Os dados chegam via tabela (ok), a expressão não vem pronta (ok) e a resolução evidencia o reconhecimento da função afim (ok). Porém a habilidade pede que o próprio estudante 'investigue', 'crie conjecturas' e 'generalize' — no formato de múltipla escolha essas etapas (itens a e b) tornam-se apenas ilustrativas na resolução do professor, sem que o desempenho do aluno nelas seja de fato avaliado ou exigido para acertar a questão. Há justaposição de subtarefas (a, b, c) sem articulação avaliativa real com o formato de resposta.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e comuns: usar y inicial sem ajuste (3x+8), trocar coeficiente angular e linear (5x+3), e assumir proporcionalidade direta ignorando o termo constante (8x). Nenhum é absurdo ou trivialmente eliminável por inspeção.
  - originalidade: 3/5 — O contexto (oficina mecânica cobrando por hora) é razoavelmente significativo, ainda que próximo de contextos clássicos (táxi, estacionamento). O problema maior é o forte scaffolding do próprio enunciado: os itens a) e b) praticamente narram o caminho de resolução (observar alinhamento, calcular diferenças constantes) antes de pedir a expressão em c), configurando efeito Topaze que reduz a autonomia esperada de uma tarefa de 'criar'.
  - *sugestões:* 1) Reconsiderar o formato: para uma habilidade de nível 'criar', prefira uma questão de resposta construída (o aluno escreve a lei de formação e justifica), ou, se for mantida a múltipla escolha, adicione uma exigência de justificativa escrita para os itens a) e b) que seja de fato corrigida/pontuada, garantindo que o processo de investigação e conjectura seja avaliado, não apenas a resposta final de c). 2) Reduzir o scaffolding do enunciado: não detalhe tanto o caminho ('observe como os pontos se comportam', 'compare o quanto y aumenta') de forma que praticamente entregue o método; deixe o aluno decidir sozinho como investigar o padrão, talvez pedindo apenas 'identifique um padrão nos dados e generalize-o algebricamente'. 3) Deixe explícito no enunciado (ou em item separado) a exigência de reconhecer o tipo de função (afim), pois atualmente esse reconhecimento só aparece na resolução do professor, não é solicitado ao aluno. 4) Se o formato múltipla escolha for mantido, considere transformar em questão de dois estágios: uma parte discursiva (a, b) avaliada separadamente e uma parte objetiva (c) como verificação, deixando claro na especificação do item que ambas serão pontuadas.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reconsiderar o formato: para uma habilidade de nível 'criar', prefira uma questão de resposta construída (o aluno escreve a lei de formação e justifica), ou, se for mantida a múltipla escolha, adicione uma exigência de justificativa escrita para os itens a) e b) que seja de fato corrigida/pontuada, garantindo que o processo de investigação e conjectura seja avaliado, não apenas a resposta final de c). 2) Reduzir o scaffolding do enunciado: não detalhe tanto o caminho ('observe como os pontos se comportam', 'compare o quanto y aumenta') de forma que praticamente entregue o método; deixe o aluno decidir sozinho como investigar o padrão, talvez pedindo apenas 'identifique um padrão nos dados e generalize-o algebricamente'. 3) Deixe explícito no enunciado (ou em item separado) a exigência de reconhecer o tipo de função (afim), pois atualmente esse reconhecimento só aparece na resolução do professor, não é solicitado ao aluno. 4) Se o formato múltipla escolha for mantido, considere transformar em questão de dois estágios: uma parte discursiva (a, b) avaliada separadamente e uma parte objetiva (c) como verificação, deixando claro na especificação do item que ambas serão pontuadas.

### Iteração 3

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 2*x + 5: reproduz os 5 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado deixa claro o que é dado (tabela de pares x,y) e o que é pedido em cada item. A única leve ambiguidade é a coexistência de itens discursivos (a, b) com um item objetivo (c) dentro de uma questão classificada como 'multipla_escolha', o que pode confundir o aplicador sobre como pontuar o conjunto, mas o texto do enunciado explicita essa divisão.
  - adequacao_nivel: 4/5 — Os itens a e b exigem efetivamente processos de investigação, formulação de conjectura e justificativa escrita, compatíveis com o nível 'criar' e com estrutura SOLO relacional/estendida. O item c, por ser objetivo, testa apenas reconhecimento (nível mais baixo), mas isso é aceitável como verificação complementar, já que a criação ocorreu nos itens discursivos anteriores.
  - alinhamento_bncc: 4/5 — Atende às três exigências centrais: os dados chegam via tabela, pede-se a generalização algébrica (não valor isolado) e o item b conduz explicitamente ao reconhecimento do tipo de função (1º grau). Não explora a representação no plano cartesiano mencionada na habilidade, mas essa etapa não constava como exigência obrigatória na especificação.
  - distratores: 4/5 — As alternativas correspondem a erros sistemáticos plausíveis (confundir termo inicial da tabela com b, esquecer o termo independente, confundir com função quadrática). Nenhuma é absurda ou trivialmente eliminável, embora a alternativa y=x²+5 seja um pouco mais fácil de descartar por um aluno que já tenha calculado as diferenças constantes.
  - originalidade: 3/5 — O contexto é puramente numérico-tabular, sem aplicação significativa ou contextualização real; é um formato clássico de 'complete o padrão e encontre a lei de formação', recorrente em livros didáticos. Não há efeito Topaze evidente, mas também não há inovação de contexto.
