# Ciclo 081 — EM13MAT401

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Duas gráficas de impressão, identificadas por R e S, cobram pelo serviço de acordo com o número de folhas impressas ($x$) e o valor total cobrado, em reais ($y$). Usando um aplicativo de geometria dinâmica, uma estudante registrou os seguintes pontos no plano cartesiano:

- O gráfico de R passa pelos pontos $A(0,3)$ e $B(4,11)$.
- O gráfico de S passa pelos pontos $C(2,4)$ e $D(5,10)$.

Determine as leis $y = f(x)$ que descrevem R e S e, a partir delas, analise o comportamento geométrico das duas retas no plano cartesiano, comparando-as com a reta de equação $y = 2x$. Assinale a alternativa que classifica corretamente cada gráfico quanto ao tipo de função e apresenta a justificativa geométrica adequada.

## Alternativas

- (a) R é uma função afim não proporcional ($y=2x+3$), cujo gráfico é uma reta paralela a $y=2x$, deslocada 3 unidades para cima, não passando pela origem; S é uma função linear (proporcional), pois sua lei é $y=2x$, coincidindo com a própria reta $y=2x$ e passando pela origem do plano cartesiano.  ← correta
- (b) Como R e S têm o mesmo coeficiente angular ($a=2$) da reta $y=2x$, ambas representam relações de proporcionalidade direta, diferindo apenas na posição inicial da reta no plano.
  - *erro representado:* Confundir igualdade de inclinação (coeficiente angular) com proporcionalidade, ignorando o valor do coeficiente linear (termo constante) na classificação.
- (c) R é proporcional, pois seu gráfico foi definido a partir de um ponto com abscissa nula ($x=0$); S não é proporcional, pois nenhum dos pontos fornecidos tem abscissa igual a zero, logo sua reta não passa pela origem.
  - *erro representado:* Julgar a proporcionalidade pela presença de um ponto com x=0 nos dados fornecidos, em vez de calcular efetivamente o coeficiente linear (b) da lei da função.
- (d) Nem R nem S representam relações de proporcionalidade direta, pois ambas as leis obtidas apresentam termo constante não nulo: $y=2x+3$ para R e $y=2x+2$ para S; portanto, nenhuma das retas passa pela origem.
  - *erro representado:* Erro algébrico ao calcular o coeficiente linear de S: usar b = y - x (em vez de b = y - a·x) ao substituir o ponto (2,4), obtendo b=2 em vez de b=0.

## Gabarito

R é uma função afim não proporcional ($y=2x+3$), cujo gráfico é paralelo a $y=2x$ mas deslocado 3 unidades para cima, não passando pela origem; S é uma função linear (proporcional), pois $y=2x$ coincide com a própria reta $y=2x$, passando pela origem.

## Resolução

**Passo 1 — Lei de R.**
O coeficiente angular é $a = \dfrac{11-3}{4-0} = \dfrac{8}{4} = 2$.
Usando o ponto $A(0,3)$: $3 = 2(0) + b \Rightarrow b = 3$.
Logo, $R: y = 2x + 3$.

**Passo 2 — Lei de S.**
O coeficiente angular é $a = \dfrac{10-4}{5-2} = \dfrac{6}{3} = 2$.
Usando o ponto $C(2,4)$: $4 = 2(2) + b \Rightarrow b = 4 - 4 = 0$.
Logo, $S: y = 2x$.

**Passo 3 — Comparação geométrica com $y=2x$.**
Ambas as retas têm o mesmo coeficiente angular ($a=2$) da reta $y=2x$, ou seja, têm a mesma inclinação. No entanto:
- $R$ tem $b=3 \neq 0$: seu gráfico é uma reta **paralela** a $y=2x$, deslocada 3 unidades para cima, e **não passa pela origem** $(0,0)$.
- $S$ tem $b=0$: sua lei coincide exatamente com $y=2x$, portanto seu gráfico **passa pela origem**.

**Passo 4 — Classificação.**
Como $S$ tem termo constante nulo e seu gráfico passa pela origem, $S$ representa uma **função linear (proporcionalidade direta)** entre número de folhas e valor cobrado. Já $R$, apesar de ter a mesma inclinação, possui um termo constante não nulo (uma espécie de "taxa fixa" de R\$3), sendo uma **função afim geral, não proporcional**.

**Conclusão:** a alternativa correta é a que afirma que R é afim não proporcional (paralela a $y=2x$, deslocada, sem passar pela origem) e S é linear/proporcional (coincide com $y=2x$, passando pela origem).

## Formalização verificável

- `funcao` — expressão `2*x + 3`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `2*x`, esperado `0`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `propriedade` — expressão `-`, esperado `2*x + 3`, parâmetros `{'pontos': '[(0,3),(4,11)]', 'grau': '1'}`
- `propriedade` — expressão `-`, esperado `2*x`, parâmetros `{'pontos': '[(2,4),(5,10)]', 'grau': '1', 'forma': 'a*x'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 2*x + 3: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(0) = 3).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado deixa claro os dados (pontos A e B), o que se pede (lei da função e classificação geométrica) e as condições. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (calcular a e b, depois verificar b=0) é predominantemente procedimental/aplicativo, mas a etapa de interpretar o resultado geométrico e classificar como proporcional ou não corresponde razoavelmente ao nível 'entender'. A estrutura de resposta é multiestrutural (cálculo + verificação), compatível com o nível declarado, embora não exija análise mais profunda.
  - alinhamento_bncc: 5/5 — A questão exige explicitamente o trânsito entre a forma algébrica (y=ax+b) e a interpretação geométrica (posição da reta em relação à origem), e força a distinção entre o caso proporcional e o caso afim geral, cumprindo integralmente as exigências da habilidade EM13MAT401.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis: omitir o cálculo de b assumindo proporcionalidade, trocar os coeficientes a e b, e confundir 'crescente' com 'proporcional'. Nenhum é absurdo ou trivialmente eliminável sem raciocínio.
  - originalidade: 2/5 — O problema reproduz um formato clássico e descontextualizado de livro didático (determinar a reta por dois pontos e checar se passa pela origem), sem qualquer contexto significativo ou aplicação. Além disso, o próprio enunciado já nomeia o conceito-chave ('função seria proporcional'), funcionando como pista que reduz o esforço de descoberta do aluno (efeito Topaze).
  - *sugestões:* Para elevar a originalidade: (1) inserir um contexto significativo e real (ex.: custo de um serviço, distância percorrida, crescimento de uma grandeza) que dê sentido aos pontos A e B, em vez de apresentá-los de forma puramente abstrata; (2) evitar mencionar diretamente no enunciado o termo 'proporcional' e a condição de passar pela origem — reformule para que o aluno precise concluir isso por si mesmo a partir da lei encontrada, por exemplo perguntando apenas 'classifique o tipo de função e justifique geometricamente'; (3) considerar pedir que o aluno esboce mentalmente ou compare com o gráfico de y=2x, reforçando o trânsito algébrico-geométrico sem entregar a resposta na pergunta. Essas mudanças preservam o alinhamento à habilidade BNCC e a qualidade dos distratores, mas tornam a tarefa menos mecânica e mais alinhada a um contexto significativo.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para elevar a originalidade: (1) inserir um contexto significativo e real (ex.: custo de um serviço, distância percorrida, crescimento de uma grandeza) que dê sentido aos pontos A e B, em vez de apresentá-los de forma puramente abstrata; (2) evitar mencionar diretamente no enunciado o termo 'proporcional' e a condição de passar pela origem — reformule para que o aluno precise concluir isso por si mesmo a partir da lei encontrada, por exemplo perguntando apenas 'classifique o tipo de função e justifique geometricamente'; (3) considerar pedir que o aluno esboce mentalmente ou compare com o gráfico de y=2x, reforçando o trânsito algébrico-geométrico sem entregar a resposta na pergunta. Essas mudanças preservam o alinhamento à habilidade BNCC e a qualidade dos distratores, mas tornam a tarefa menos mecânica e mais alinhada a um contexto significativo.

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(0) = 3). | (2) aprovado: Gabarito confirmado (f(0) = 0). | (3) aprovado: Propriedades confirmadas para 2*x + 3: reproduz os 2 pontos dados; grau 1. | (4) aprovado: Propriedades confirmadas para 2*x: reproduz os 2 pontos dados; grau 1; forma a*x.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - propriedade=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta dados completos (pontos das retas R e S), pede claramente a determinação das leis e a comparação geométrica com y=2x, sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exige calcular coeficientes (aplicar), comparar retas e classificar seu comportamento geométrico (entender/comparar), o que é coerente com 'entender' na taxonomia de Bloom quando esta categoria inclui comparar e classificar. A resposta esperada é relacional (SOLO), pois articula inclinação, coeficiente linear e posição da reta — adequado ao nível declarado, embora tangencie 'analisar'.
  - alinhamento_bncc: 5/5 — A questão exige trânsito efetivo entre forma algébrica (determinar a lei a partir de pontos) e representação geométrica (posição da reta, paralelismo, passagem pela origem), e distingue explicitamente o caso proporcional (S) do caso apenas afim (R), cumprindo integralmente os dois requisitos da habilidade EM13MAT401.
  - distratores: 4/5 — Os três distratores representam erros conceituais ou algébricos plausíveis: confundir inclinação com proporcionalidade, julgar proporcionalidade pela presença de x=0 nos dados brutos, e erro de substituição no cálculo do coeficiente linear. Nenhum é absurdo ou trivialmente eliminável, embora o distrator 3 seja um pouco menos comum como erro sistemático típico de estudante.
  - originalidade: 4/5 — O contexto de gráficas de impressão com uso de aplicativo de geometria dinâmica foge do enunciado clássico de 'ache a equação da reta pelos pontos'. Há leve efeito Topaze ao já indicar a comparação com y=2x no comando, mas isso é necessário para direcionar à habilidade sem tornar a resposta trivial.
