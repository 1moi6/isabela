# Ciclo 069 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Considere a sequência $(a_n)$, definida para $n = 0, 1, 2, 3, \ldots$, com primeiro termo $a_0 = 5$ e razão $q = 3$ (uma progressão geométrica). Um pesquisador registra o número de bactérias em uma cultura a cada hora exata, de modo que $a_n$ é a contagem observada na hora $n$. Ele percebe que esses valores coincidem com os da função exponencial $f(t) = 5 \cdot 3^t$ para $t = n$, ou seja, $f(n) = a_n$ para todo $n$ natural.

Ricardo, colega do pesquisador, argumenta: "Como $f(t)=5\cdot 3^t$ está definida para qualquer número real $t$, o valor $f(2{,}5) = 5\cdot 3^{2{,}5}$ é a contagem real de bactérias no instante intermediário entre a segunda e a terceira hora."

Avalie a afirmação de Ricardo e assinale a alternativa correta.

## Alternativas

- (a) Ricardo está errado: a progressão geométrica $(a_n)$ está definida apenas para os índices naturais $n=0,1,2,3,\ldots$, que correspondem às horas exatas em que a contagem foi feita. A função $f(t)=5\cdot3^t$ é uma extensão contínua que apenas interpola os termos da PG nos pontos inteiros; o valor $f(2{,}5)$ existe matematicamente, mas não corresponde a nenhum termo da sequência, pois o fenômeno só foi definido (e medido) nos instantes discretos.  ← correta
- (b) Ricardo está certo, pois a PG e a função exponencial são exatamente a mesma coisa: como $f$ está definida para todo $t$ real, qualquer valor calculado por $f$ é automaticamente um termo válido da progressão.
  - *erro representado:* Confundir a função contínua com a sequência discreta, achando que o domínio da PG se estende automaticamente para os reais.
- (c) Ricardo está errado, mas pelo motivo errado: ele deveria ter estimado o valor em $t=2{,}5$ fazendo a média aritmética simples entre $a_2=45$ e $a_3=135$ (interpolação linear), e não usando a fórmula exponencial $5\cdot3^{2,5}$.
  - *erro representado:* Confundir a natureza discreta do domínio — que torna $f(2,5)$ sem significado para a sequência — com a escolha do método de interpolação, como se o problema fosse apenas decidir entre interpolação linear ou exponencial.
- (d) Ricardo está certo, porque, em princípio, o número de bactérias poderia ser medido continuamente ao longo do tempo; logo $f(2{,}5)$ representa a contagem real esperada nesse instante, ainda que o pesquisador só tenha registrado valores a cada hora.
  - *erro representado:* Não perceber que o modelo (a PG) foi definido para representar o fenômeno apenas nos instantes discretos de medição, confundindo o domínio do modelo matemático com o domínio (hipoteticamente contínuo) do fenômeno físico.

## Gabarito

A

## Resolução

**1. Identificando o que é a PG e o que é a função exponencial.**

A sequência $(a_n)$ é uma progressão geométrica: $a_0=5$, $q=3$, então $a_n = 5\cdot 3^n$, mas **apenas para $n = 0,1,2,3,\ldots$** (índices naturais), pois cada termo corresponde a uma contagem feita em uma hora exata.

A função $f(t) = 5\cdot 3^t$ tem domínio real ($t$ pode ser qualquer número real), e ela foi construída de modo que $f(n) = a_n$ para todo $n$ natural — ou seja, $f$ é uma **extensão contínua** dos termos discretos da PG.

**2. Calculando alguns termos para comparação.**

$a_0 = 5$, $a_1 = 15$, $a_2 = 45$, $a_3 = 135$.

De fato, $f(0)=5$, $f(1)=15$, $f(2)=45$, $f(3)=135$: os valores coincidem exatamente nos pontos inteiros.

**3. Analisando $f(2{,}5)$.**

Como $f$ tem domínio real, o número $f(2{,}5)=5\cdot 3^{2,5}\approx 77{,}9$ existe matematicamente. Porém, a progressão $(a_n)$ — que é o modelo que de fato representa o fenômeno medido (contagens feitas hora a hora) — **só está definida para índices naturais**. Não existe "$a_{2,5}$": o pesquisador não mediu bactérias em $t=2{,}5$, e o modelo discreto não faz essa previsão.

**4. Conclusão.**

$f(t)=5\cdot3^t$ é apenas a curva contínua que passa pelos pontos $(n, a_n)$ para interpolar visualmente a PG; o valor $f(2{,}5)$ é um artifício matemático de extensão da fórmula, sem correspondência com um termo real da sequência, que só existe para $n$ natural. Logo, Ricardo está errado.

**Gabarito: alternativa A.**

## Formalização verificável

- `progressao` — expressão `-`, esperado `45`, parâmetros `{'tipo_progressao': 'pg', 'a1': '5', 'razao': '3', 'n': '3', 'consulta': 'termo'}`
- `funcao` — expressão `5*3**t`, esperado `45`, parâmetros `{'consulta': 'valor', 'ponto': '2'}`
- `funcao` — expressão `5*3**t`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `propriedade` — expressão `-`, esperado `5*3**n`, parâmetros `{'pontos': '[(0,5),(1,15),(2,45),(3,135)]', 'sequencia': 'pg', 'a1': '5', 'razao': '3'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (f(5) = 162). | (3) aprovado: Propriedades confirmadas para 2*3**(n - 1): coincide com a PG declarada.
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: apresenta a PG, define claramente o que se pede (função exponencial associada, com domínio adequado) e não há ambiguidade lexical ou estrutural. Os dados são suficientes para resolver.
  - adequacao_nivel: 3/5 — O processo cognitivo real exigido é essencialmente 'aplicar' a fórmula do termo geral e reconhecer o domínio correto — uma tarefa multiestrutural (calcular razão, termo inicial, montar expressão, escolher domínio), mas não chega a exigir 'analisar' no sentido de decompor relações, comparar sistematicamente estruturas ou justificar causalmente a escolha. O rótulo Bloom 'analisar' está superestimado em relação à demanda cognitiva efetiva.
  - alinhamento_bncc: 4/5 — A questão atende bem à exigência de tratar explicitamente o domínio discreto, pois força o estudante a distinguir entre domínio natural e real (alternativa c) e não apenas aplicar a fórmula do termo geral. A articulação entre PG e função exponencial é central ao problema, não incidental. Poderia ser mais forte se exigisse justificar a escolha do domínio, não apenas selecioná-lo.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: deslocamento de índice (b), confusão discreto/contínuo (c) e troca de papéis entre a1 e q (d). Nenhum é absurdo ou trivialmente eliminável sem cálculo ou raciocínio.
  - originalidade: 2/5 — A PG (2,6,18,54,162) e a tarefa de montar f(n)=a1·q^(n-1) são extremamente recorrentes em livros didáticos, sem contexto aplicado ou situação significativa. Além disso, o próprio enunciado já entrega a chave da resposta ao explicar que 'n indica a posição do termo' e que 'não faz sentido n=2,5' — isso constitui efeito Topaze, pavimentando a distinção discreto/contínuo que deveria ser conclusão do próprio raciocínio do estudante, não uma pista do enunciado.
  - *sugestões:* 1) Reduzir o efeito Topaze: remova do enunciado a explicação de que 'n indica a posição' e a observação sobre 'não fazer sentido n=2,5' — deixe que o próprio estudante infira a necessidade do domínio discreto ao analisar as alternativas. 2) Elevar o nível cognitivo para verdadeiramente 'analisar': por exemplo, apresente o raciocínio de um estudante fictício que propõe uma função f(x)=2·3^x com domínio real e pergunte por que essa proposta está incorreta, ou peça para comparar duas funções propostas justificando qual representa fielmente a PG e por quê — isso exige decompor e avaliar relações, não só aplicar fórmula. 3) Contextualizar com uma situação significativa (crescimento populacional discreto, juros compostos com aportes anuais, etc.) em vez da PG genérica e descontextualizada, evitando repetição de exemplo clássico de livro didático. 4) Se mantiver o formato atual, acrescente uma exigência de justificativa (não apenas escolha de alternativa) para caracterizar melhor o nível 'analisar' da taxonomia SOLO/Bloom.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reduzir o efeito Topaze: remova do enunciado a explicação de que 'n indica a posição' e a observação sobre 'não fazer sentido n=2,5' — deixe que o próprio estudante infira a necessidade do domínio discreto ao analisar as alternativas. 2) Elevar o nível cognitivo para verdadeiramente 'analisar': por exemplo, apresente o raciocínio de um estudante fictício que propõe uma função f(x)=2·3^x com domínio real e pergunte por que essa proposta está incorreta, ou peça para comparar duas funções propostas justificando qual representa fielmente a PG e por quê — isso exige decompor e avaliar relações, não só aplicar fórmula. 3) Contextualizar com uma situação significativa (crescimento populacional discreto, juros compostos com aportes anuais, etc.) em vez da PG genérica e descontextualizada, evitando repetição de exemplo clássico de livro didático. 4) Se mantiver o formato atual, acrescente uma exigência de justificativa (não apenas escolha de alternativa) para caracterizar melhor o nível 'analisar' da taxonomia SOLO/Bloom.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 135). | (2) aprovado: Gabarito confirmado (domínio Naturals0 — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (3) aprovado: Gabarito confirmado (f(5/2) = 45*sqrt(3)).
  - progressao/termo=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta dados completos, a tabela de contagens, a proposta de Ricardo e o cálculo específico que deve ser avaliado. A pergunta final ('avalie a afirmação') é inequívoca quanto ao que se pede.
  - adequacao_nivel: 4/5 — Exigir que o aluno avalie a validade de um argumento (distinguir domínio discreto da PG do domínio contínuo da extensão exponencial) é coerente com 'analisar' (diferenciar/julgar critérios) e com resposta de estrutura relacional (SOLO), não apenas multiestrutural. Conteúdo compatível com o Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão articula diretamente PG e função exponencial num único problema, exigindo justamente a discussão do domínio discreto vs. contínuo pedida pela EM13MAT508, e não apenas a aplicação mecânica de fórmulas de termo geral.
  - distratores: 2/5 — As alternativas C e D exploram erros (PA em vez de PG, razão calculada por diferença) que já estão contraditos explicitamente pelo próprio enunciado, que informa 'progressão geométrica de razão 3'. Isso torna esses distratores trivialmente elimináveis por simples releitura do enunciado, sem exigir o raciocínio central da questão (domínio discreto x contínuo). Além disso, a alternativa C contém contradição interna: afirma que a colônia 'cresce sempre pelo mesmo valor absoluto' mas lista incrementos diferentes (10, 30, 90), o que a torna absurda e facilmente descartável à primeira leitura, mesmo sem entender o conceito avaliado. Apenas a alternativa B representa de fato um erro sistemático plausível relacionado ao foco da questão (confundir extensão contínua com validade total no domínio real).
  - originalidade: 4/5 — O contexto de bactérias é um clássico recorrente em livros didáticos, mas a abordagem – analisar criticamente o raciocínio de um estudante fictício sobre domínio discreto vs. extensão contínua – foge do formato mecânico usual e evita pistas diretas para a resposta (não há efeito Topaze evidente).
  - *sugestões:* Reformule as alternativas C e D para que explorem erros relacionados ao núcleo conceitual da questão (a relação entre domínio discreto da PG e domínio contínuo da função exponencial), e não erros já descartados pelo próprio enunciado (que já afirma explicitamente 'razão 3' e 'progressão geométrica'). Por exemplo, um distrator mais produtivo seria: 'Ricardo está errado porque deveria ter usado apenas os termos da PG (t=0,1,2,3) para interpolar linearmente o valor em t=2,5, e não a fórmula exponencial' (erro de confundir interpolação linear com extensão exponencial), ou 'Ricardo está certo, mas apenas porque o experimento poderia, em princípio, ser medido continuamente, então f(2,5) representa uma contagem real esperada' (erro de não perceber a diferença entre modelo matemático contínuo e fenômeno discreto por natureza, mesmo que hipoteticamente mensurável). Além disso, corrija a contradição interna da alternativa C (ela afirma crescimento constante mas lista valores diferentes) antes de descartá-la ou reaproveitá-la de outra forma. Isso tornará os quatro distratores igualmente plausíveis e centrados no mesmo raciocínio exigido pela questão.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule as alternativas C e D para que explorem erros relacionados ao núcleo conceitual da questão (a relação entre domínio discreto da PG e domínio contínuo da função exponencial), e não erros já descartados pelo próprio enunciado (que já afirma explicitamente 'razão 3' e 'progressão geométrica'). Por exemplo, um distrator mais produtivo seria: 'Ricardo está errado porque deveria ter usado apenas os termos da PG (t=0,1,2,3) para interpolar linearmente o valor em t=2,5, e não a fórmula exponencial' (erro de confundir interpolação linear com extensão exponencial), ou 'Ricardo está certo, mas apenas porque o experimento poderia, em princípio, ser medido continuamente, então f(2,5) representa uma contagem real esperada' (erro de não perceber a diferença entre modelo matemático contínuo e fenômeno discreto por natureza, mesmo que hipoteticamente mensurável). Além disso, corrija a contradição interna da alternativa C (ela afirma crescimento constante mas lista valores diferentes) antes de descartá-la ou reaproveitá-la de outra forma. Isso tornará os quatro distratores igualmente plausíveis e centrados no mesmo raciocínio exigido pela questão.

### Iteração 3

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PG = 45). | (2) aprovado: Gabarito confirmado (f(2) = 45). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (4) aprovado: Propriedades confirmadas para 5*3**n: reproduz os 4 pontos dados; coincide com a PG declarada.
  - progressao/termo=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a PG, a função exponencial associada e o argumento de Ricardo a ser avaliado. Não há ambiguidade lexical ou estrutural; os dados (a0=5, q=3, f(t)=5·3^t) são suficientes para a análise pedida.
  - adequacao_nivel: 5/5 — A tarefa exige avaliar criticamente um argumento (analisar), distinguindo o domínio discreto da PG do domínio contínuo da função — não basta aplicar fórmula do termo geral. A resposta correta exige articulação relacional entre os dois conceitos (SOLO relacional), coerente com o nível 'analisar' declarado.
  - alinhamento_bncc: 5/5 — Cumpre exatamente a exigência da EM13MAT508: a associação entre PG e função exponencial é o núcleo do problema (não um mero pretexto), e o domínio discreto é tratado explicitamente como o ponto central da análise, articulando os dois temas em um único raciocínio.
  - distratores: 4/5 — B representa a confusão clássica entre sequência e função (domínio discreto vs. real); D confunde modelo matemático com fenômeno físico hipoteticamente contínuo — ambos plausíveis. C é criativo (desloca o erro para o método de interpolação), mas é um erro menos comum entre estudantes reais, sendo levemente mais sofisticado que um erro 'espontâneo' típico; ainda assim não é absurdo nem trivialmente eliminável.
  - originalidade: 4/5 — O contexto de bactérias é recorrente em livros didáticos, mas a questão não segue o script padrão de 'calcule o termo n' — em vez disso, explora criticamente a diferença entre modelo discreto e extensão contínua, evitando pistas diretas (efeito Topaze) e exigindo julgamento conceitual do estudante.
