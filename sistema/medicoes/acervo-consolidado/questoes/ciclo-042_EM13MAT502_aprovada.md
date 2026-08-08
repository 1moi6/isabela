# Ciclo 042 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma equipe de engenharia rodoviária testa, em pista seca, a distância de frenagem d (em metros) de um automóvel a partir do instante em que o motorista aciona os freios, para diferentes velocidades v (em km/h). Os resultados de quatro testes estão na tabela abaixo:

| v (km/h) | 10 | 20 | 30 | 40 |
|---|---|---|---|---|
| d (m) | 2 | 8 | 18 | 32 |

Sabendo que a distância de frenagem depende apenas da velocidade e que o padrão observado nos testes se mantém para qualquer velocidade, qual expressão algébrica representa corretamente d em função de v?

## Alternativas

- (a) $d(v) = \dfrac{v^2}{50}$  ← correta
- (b) $d(v) = 0{,}6v - 4$
  - *erro representado:* Assumir, sem verificar as demais diferenças, que a relação é linear: calcula a inclinação usando apenas os dois primeiros pontos $\left(\frac{8-2}{20-10}=0{,}6\right)$ e ajusta um termo independente, ignorando que as diferenças sucessivas não são constantes.
- (c) $d(v) = 0{,}2v$
  - *erro representado:* Calcular a razão $d/v$ (proporcionalidade direta simples) em vez de $d/v^2$, usando apenas o primeiro par ($2/10=0{,}2$) e generalizar essa razão como se $d$ fosse diretamente proporcional a $v$, sem elevar ao quadrado.
- (d) $d(v) = \dfrac{v^2}{25}$
  - *erro representado:* Erro de cálculo ao obter a constante de proporcionalidade: usar apenas um par de valores (por exemplo, $d=8$ e $v=20$) mas dividir $v$ por $2$ antes de elevar ao quadrado ($10^2=100$, $8/100$ arredondado incorretamente), chegando a $a=1/25$ em vez de $1/50$, sem checar a consistência com os demais pontos da tabela.

## Gabarito

d(v) = v²/50

## Resolução

**Passo 1 — Testar se a relação é linear.**

As diferenças sucessivas de $d$ são: $8-2=6$, $18-8=10$, $32-18=14$. Como essas diferenças não são constantes, a relação **não é linear** (não é do tipo $d = mv + n$).

**Passo 2 — Testar as segundas diferenças.**

As diferenças das diferenças são: $10-6=4$ e $14-10=4$. Como as segundas diferenças são constantes (iguais a 4) para um passo constante de $v$ ($\Delta v = 10$), isso indica uma relação **quadrática**, ou seja, $d = av^2 + bv + c$.

**Passo 3 — Testar se a relação é do tipo $d = av^2$ (sem termos de grau menor).**

Calculamos a razão $\dfrac{d}{v^2}$ para cada par:

$\dfrac{2}{10^2} = \dfrac{2}{100} = \dfrac{1}{50}$

$\dfrac{8}{20^2} = \dfrac{8}{400} = \dfrac{1}{50}$

$\dfrac{18}{30^2} = \dfrac{18}{900} = \dfrac{1}{50}$

$\dfrac{32}{40^2} = \dfrac{32}{1600} = \dfrac{1}{50}$

Como a razão $\dfrac{d}{v^2}$ é constante e igual a $\dfrac{1}{50}$ em **todos** os pontos (e não passa por $v=0$ com $d\neq 0$ nem apresenta termo linear), concluímos que não há termos de grau 1 nem constante: a relação é exatamente do tipo $y = ax^2$.

**Passo 4 — Escrever a expressão geral.**

$$d(v) = \dfrac{v^2}{50}$$

Verificação final: $d(10)=\frac{100}{50}=2$, $d(20)=\frac{400}{50}=8$, $d(30)=\frac{900}{50}=18$, $d(40)=\frac{1600}{50}=32$ — todos coincidem com a tabela.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `v**2/50`, parâmetros `{'pontos': '[(10,2),(20,8),(30,18),(40,32)]', 'grau': '2', 'forma': 'a*v**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para v**2/50: reproduz os 4 pontos dados; grau 2; forma a*v**2.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado deixa claro o que é dado (tabela v-d), o que é pedido (expressão algébrica de d em função de v) e a condição de generalização ('o padrão... se mantém para qualquer velocidade'). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 5/5 — O processo exigido (testar diferenças sucessivas, depois segundas diferenças, depois razão d/v², descartando termos lineares e constantes) é compatível com 'analisar': o estudante decompõe o padrão em componentes e relaciona evidências para justificar a forma y=ax². A estrutura de resposta é relacional (SOLO), não meramente multiestrutural, pois exige integrar diferentes testes (linearidade descartada, quadraticidade confirmada, ausência de termos extras) numa conclusão única.
  - alinhamento_bncc: 5/5 — Atende às exigências específicas listadas: dados chegam como tabela sem expressão pronta; pede-se a generalização algébrica do padrão; a questão conduz ao reconhecimento de que a relação é do tipo y=ax² (proporcionalidade ao quadrado), com verificação explícita de que não há termos de grau 1 ou constante. A ausência de representação gráfica no plano cartesiano não fere as exigências listadas, que não a tornam obrigatória para este item.
  - distratores: 4/5 — Os três distratores incorretos correspondem a erros sistemáticos plausíveis: assumir linearidade sem checar todas as diferenças, confundir proporcionalidade direta com quadrática, e erro de cálculo ao obter a constante. Nenhum é trivialmente eliminável à primeira vista. O quarto distrator (v²/25) tem uma justificativa de erro um pouco artificial ('dividir v por 2 antes de elevar ao quadrado'), menos natural que os demais, o que reduz ligeiramente sua qualidade pedagógica.
  - originalidade: 4/5 — O contexto de frenagem é um tema aplicado recorrente em materiais de física/matemática, mas o enunciado evita entregar pistas diretas (não menciona 'quadrática' ou 'proporcional ao quadrado'), preservando o desafio investigativo e evitando o efeito Topaze. Não é o exemplo mais inovador possível, mas é significativo e evita repetição mecânica de enunciados de livro.
