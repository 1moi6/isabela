# Ciclo 053 — EM13MAT501

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Uma empresa de entregas rápidas registrou o valor cobrado (em reais) para diferentes distâncias percorridas por seus motoboys, conforme a tabela abaixo:

| Distância d (km) | Valor cobrado V (R$) |
|---|---|
| 2 | 12 |
| 5 | 21 |
| 8 | 30 |
| 11 | 39 |

Analisando os dados da tabela, qual expressão algébrica V(d) generaliza corretamente o padrão observado, e que tipo de função ela representa?

## Alternativas

- (a) V(d) = 3d + 6 — função polinomial do 1º grau  ← correta
- (b) V(d) = 6d — função polinomial do 1º grau
  - *erro representado:* Assumiu proporcionalidade direta (ignorou o termo constante), calculando a razão V/d apenas do primeiro par de valores (12/2 = 6) sem considerar o coeficiente linear.
- (c) V(d) = 3d² + 6 — função polinomial do 2º grau
  - *erro representado:* Concluiu que o crescimento é quadrático apenas por observar que os valores aumentam, sem verificar que a diferença entre valores consecutivos de V é constante (o que indica 1º grau, não 2º).
- (d) V(d) = 9d - 6 — função polinomial do 1º grau
  - *erro representado:* Usou diretamente a diferença entre valores consecutivos de V (ΔV = 9) como coeficiente angular, sem dividir pela variação correspondente de d (Δd = 3).

## Gabarito

V(d) = 3d + 6 — função polinomial do 1º grau (afim)

## Resolução

**Passo 1 — Organizar os dados e observar as variações**

Calculando a variação de $d$ e de $V$ entre linhas consecutivas da tabela:

$\Delta d = 5-2 = 3,\quad \Delta V = 21-12 = 9$

$\Delta d = 8-5 = 3,\quad \Delta V = 30-21 = 9$

$\Delta d = 11-8 = 3,\quad \Delta V = 39-30 = 9$

**Passo 2 — Calcular a taxa de variação**

Como $\Delta d$ é sempre igual e $\Delta V$ também é sempre igual, a razão $\dfrac{\Delta V}{\Delta d}$ é constante:

$\dfrac{\Delta V}{\Delta d} = \dfrac{9}{3} = 3$

Uma taxa de variação constante entre grandezas indica que a relação entre $d$ e $V$ é do tipo $V(d) = a\cdot d + b$, ou seja, uma **função polinomial do 1º grau (função afim)**, com $a = 3$.

**Passo 3 — Determinar o coeficiente linear $b$**

Usando o ponto $(2,12)$:

$12 = 3\cdot 2 + b \Rightarrow 12 = 6 + b \Rightarrow b = 6$

**Passo 4 — Escrever a lei de formação e verificar**

$V(d) = 3d + 6$

Verificando com os demais pontos:

- $d=5$: $3(5)+6=21$ ✓
- $d=8$: $3(8)+6=30$ ✓
- $d=11$: $3(11)+6=39$ ✓

Todos os pontos satisfazem a expressão, confirmando que a relação é de **função polinomial do 1º grau**, com lei $V(d) = 3d + 6$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*d + 6`, parâmetros `{'pontos': '[(2,12),(5,21),(8,30),(11,39)]', 'grau': '1'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*h + 5: reproduz os 4 pontos dados; grau 1.
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (tabela h x V), a condição (h inteiro positivo) e o que se pede (expressão V(h)). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — A especificação declara nível 'criar', que na taxonomia de Bloom exige produção original (gerar a lei algébrica e testá-la, sem opções pré-definidas), correspondendo a uma resposta ao menos relacional/estendida-abstrata no SOLO. Ao transformar a tarefa em múltipla escolha, o estudante apenas reconhece/verifica qual alternativa satisfaz os pares dados — processo de 'aplicar' ou no máximo 'analisar', não de 'criar'. A resolução mostra o raciocínio de generalização esperado, mas o formato de resposta oferecido ao aluno não exige esse raciocínio de forma plena, pois a checagem por substituição nas alternativas é suficiente para acertar.
  - alinhamento_bncc: 4/5 — A questão cumpre a maior parte das exigências: dados em tabela (não em expressão pronta), pedido de generalização algébrica (não cálculo de valor isolado) e conteúdo que leva ao reconhecimento de função afim. Falta, porém, o aspecto de 'representá-los no plano cartesiano' presente na habilidade — a questão não articula a leitura tabular com uma representação gráfica, tratando apenas o registro numérico-algébrico.
  - distratores: 4/5 — Três distratores representam erros sistemáticos plausíveis (inversão de coeficientes, proporcionalidade direta ignorando o termo constante, suposição de grau quadrático a partir de diferenças constantes). O último é um pouco menos natural, pois a diferença constante na primeira ordem é justamente o indício de função afim, não quadrática — um aluno mais atento dificilmente cometeria esse erro, tornando esse distrator moderadamente menos plausível que os demais.
  - originalidade: 4/5 — O contexto de locadora de bicicletas foge do clichê da conta telefônica/taxa de táxi, trazendo aplicação razoavelmente significativa. Não há pistas explícitas que entreguem a solução (efeito Topaze), embora a estrutura seja previsível dentro do gênero 'tabela com variação constante'.
  - *sugestões:* Ajustar a coerência entre o nível de Bloom declarado ('criar') e o formato da questão. Duas alternativas: (1) Manter múltipla escolha, mas rebaixar o nível cognitivo declarado na especificação para 'aplicar' ou 'analisar', já que reconhecer a alternativa correta por substituição não configura criação; ou (2) Preservar o nível 'criar' transformando a questão em formato aberto/dissertativo, pedindo explicitamente que o estudante: (a) organize os dados da tabela no plano cartesiano, (b) identifique o padrão de variação, (c) construa por si mesmo a lei V(h) = ah + b determinando a e b, e (d) justifique por que a relação é uma função polinomial de 1º grau. Isso também fortalece o alinhamento com a habilidade EM13MAT501, que menciona explicitamente a representação no plano cartesiano — aspecto ausente na versão atual. Se optar por manter múltipla escolha, considere substituir o distrator 'V(h)=3h²+5' por um erro mais plausível relacionado à leitura incorreta da tabela (ex.: usar dois pontos não consecutivos e calcular inclinação errada).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a coerência entre o nível de Bloom declarado ('criar') e o formato da questão. Duas alternativas: (1) Manter múltipla escolha, mas rebaixar o nível cognitivo declarado na especificação para 'aplicar' ou 'analisar', já que reconhecer a alternativa correta por substituição não configura criação; ou (2) Preservar o nível 'criar' transformando a questão em formato aberto/dissertativo, pedindo explicitamente que o estudante: (a) organize os dados da tabela no plano cartesiano, (b) identifique o padrão de variação, (c) construa por si mesmo a lei V(h) = ah + b determinando a e b, e (d) justifique por que a relação é uma função polinomial de 1º grau. Isso também fortalece o alinhamento com a habilidade EM13MAT501, que menciona explicitamente a representação no plano cartesiano — aspecto ausente na versão atual. Se optar por manter múltipla escolha, considere substituir o distrator 'V(h)=3h²+5' por um erro mais plausível relacionado à leitura incorreta da tabela (ex.: usar dois pontos não consecutivos e calcular inclinação errada).

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 2*x + 5: reproduz os 4 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é claro: dados em tabela, pergunta explícita sobre V(d). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O enunciado já afirma que 'os pontos estão alinhados, indicando uma relação com taxa de variação constante', entregando ao aluno a conjectura (que é justamente o que o nível 'criar' deveria exigir que ele formulasse). Resta apenas calcular a e b, processo de nível 'aplicar' (SOLO multiestrutural), não 'criar' (SOLO relacional/estendido abstrato). O formato múltipla escolha também restringe estruturalmente a geração livre da expressão, pois o aluno pode testar as alternativas contra a tabela sem de fato construir o modelo.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT501 exige que o próprio estudante identifique o padrão e formule a conjectura de linearidade a partir da tabela. Aqui essa etapa central é feita pelo enunciado, que já declara 'taxa de variação constante' e 'pontos alinhados'. Isso descumpre a exigência de que a questão 'leve ao reconhecimento' — o reconhecimento já foi entregue, restando só a determinação algébrica dos coeficientes.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis e distintos (assumir proporcionalidade direta, calcular Δd incorretamente como 1, inverter a razão da inclinação). Nenhum é absurdo ou trivialmente eliminável, embora o distrator V(d)=2d seja ligeiramente mais fácil de descartar por não passar por nenhum ponto da tabela.
  - originalidade: 2/5 — Contexto de transportadora é razoavelmente aplicado, mas o enunciado sofre forte efeito Topaze: ao afirmar antecipadamente que há 'taxa de variação constante' e que os pontos 'estão alinhados', ele pavimenta a solução e elimina o desafio de descoberta que caracterizaria uma tarefa de nível 'criar'. É essencialmente um exercício clássico de tabela-para-lei-afim, sem elemento que o diferencie de exemplos padronizados de livro didático.
  - *sugestões:* Remova do enunciado as frases que já revelam a conclusão ('os pontos estão alinhados', 'relação com taxa de variação constante'). Apresente apenas a tabela e peça diretamente: 'Qual expressão algébrica V(d) generaliza o padrão observado na tabela, e que tipo de função ela representa?'. Assim o aluno precisa, por si mesmo, plotar/analisar os pontos, perceber a taxa de variação constante e só então formular a lei — cumprindo de fato o processo de 'criar' e a exigência da habilidade BNCC de identificar o padrão antes de generalizá-lo. Se o formato múltipla escolha for mantido, considere transformar a questão em resposta construída (ex.: pedir a expressão E a classificação do tipo de função), ou usar alternativas que testem também a classificação (ex.: incluir opções com funções quadráticas ou exponenciais aproximadamente ajustadas aos pontos) para forçar o aluno a validar a linearidade em vez de apenas ajustar coeficientes.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Remova do enunciado as frases que já revelam a conclusão ('os pontos estão alinhados', 'relação com taxa de variação constante'). Apresente apenas a tabela e peça diretamente: 'Qual expressão algébrica V(d) generaliza o padrão observado na tabela, e que tipo de função ela representa?'. Assim o aluno precisa, por si mesmo, plotar/analisar os pontos, perceber a taxa de variação constante e só então formular a lei — cumprindo de fato o processo de 'criar' e a exigência da habilidade BNCC de identificar o padrão antes de generalizá-lo. Se o formato múltipla escolha for mantido, considere transformar a questão em resposta construída (ex.: pedir a expressão E a classificação do tipo de função), ou usar alternativas que testem também a classificação (ex.: incluir opções com funções quadráticas ou exponenciais aproximadamente ajustadas aos pontos) para forçar o aluno a validar a linearidade em vez de apenas ajustar coeficientes.

### Iteração 3

- **Verificador:** aprovado — Propriedades confirmadas para 3*d + 6: reproduz os 4 pontos dados; grau 1.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta a tabela de forma organizada, deixa claro o que é dado (pares distância/valor) e o que é pedido (a lei de formação e a classificação do tipo de função). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido — investigar variações, formular conjectura e generalizar algebricamente — é compatível com 'criar'. Contudo, o formato de múltipla escolha reduz parcialmente a demanda de produção livre (típica do nível 'criar'/extended abstract da SOLO) para uma tarefa de reconhecimento entre opções prontas. Isso é atenuado pelo fato de os distratores exigirem que o estudante realmente execute o raciocínio antes de escolher, mas a estrutura de resposta não é plenamente 'criar'.
  - alinhamento_bncc: 5/5 — Cumpre as três exigências: os dados chegam como tabela, a expressão não é fornecida, pede-se a generalização algébrica (não um valor isolado) e a questão conduz ao reconhecimento de que a relação é afim (1º grau). Atende plenamente à EM13MAT501.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: proporcionalidade direta (ignorar b), suposição de grau 2 por crescimento aparente, e uso incorreto de ΔV sem dividir por Δd. Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 4/5 — O contexto de entregas rápidas é aplicado e minimamente significativo, evitando o clássico 'tabela de números soltos'. Não há pistas explícitas que antecipem a resposta (efeito Topaze), embora o contexto em si seja relativamente comum em materiais didáticos sobre função afim.
