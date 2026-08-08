# Ciclo 022 — EM13MAT305

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

A escala de pH mede a acidez de uma solução aquosa a partir da concentração de íons hidrogênio $[H^+]$ (em mol/L), segundo a relação $pH = -\log_{10}[H^+]$.

Considere duas soluções aquosas, A e B, cujos valores de pH diferem em $n$ unidades, sendo B mais ácida que A, isto é, $pH_A - pH_B = n$, com $n > 0$.

Assinale a alternativa que apresenta corretamente a expressão geral que relaciona a razão entre as concentrações de $H^+$ das duas soluções e a diferença $n$ de pH, juntamente com a conclusão numérica correta para o caso em que $n = 3$.

## Alternativas

- (a) $\dfrac{[H^+]_{\text{mais ácida}}}{[H^+]_{\text{menos ácida}}} = 10^n$; para $n=3$, a solução mais ácida tem concentração de $H^+$ 1000 vezes maior.  ← correta
- (b) $\dfrac{[H^+]_{\text{mais ácida}}}{[H^+]_{\text{menos ácida}}} = 10n$; para $n=3$, a solução mais ácida tem concentração de $H^+$ 30 vezes maior.
  - *erro representado:* Tratar a diferença de logaritmos como se gerasse uma relação linear (multiplicação simples por 10 e por n), em vez de reconhecer que a diferença de logaritmos corresponde a uma razão exponencial (10 elevado a n).
- (c) $\dfrac{[H^+]_{\text{mais ácida}}}{[H^+]_{\text{menos ácida}}} = e^n$; para $n=3$, a solução mais ácida tem concentração de $H^+$ aproximadamente 20,1 vezes maior.
  - *erro representado:* Usar a base do logaritmo natural (e) em vez da base 10, ignorando que a definição de pH usa logaritmo decimal.
- (d) $\dfrac{[H^+]_{\text{mais ácida}}}{[H^+]_{\text{menos ácida}}} = 10^{-n}$; para $n=3$, a solução mais ácida tem concentração de $H^+$ 1000 vezes menor.
  - *erro representado:* Inverter o sentido da relação entre pH e concentração de H+, concluindo erroneamente que a solução mais ácida (menor pH) tem menor concentração de íons H+.

## Gabarito

A

## Resolução

**Passo 1 — Escrever a definição de pH para cada solução.**

$pH_A = -\log_{10}[H^+]_A$ e $pH_B = -\log_{10}[H^+]_B$

**Passo 2 — Usar a condição dada, $pH_A - pH_B = n$.**

$\left(-\log_{10}[H^+]_A\right) - \left(-\log_{10}[H^+]_B\right) = n$

$\log_{10}[H^+]_B - \log_{10}[H^+]_A = n$

**Passo 3 — Aplicar a propriedade do logaritmo do quociente.**

$\log_{10}\left(\dfrac{[H^+]_B}{[H^+]_A}\right) = n$

**Passo 4 — Converter para a forma exponencial.**

$\dfrac{[H^+]_B}{[H^+]_A} = 10^n$

Como B é a solução mais ácida (menor pH, maior concentração de $H^+$), essa razão é a concentração da mais ácida dividida pela da menos ácida, e o resultado $10^n > 1$ é coerente com o fato de B ser mais ácida.

**Passo 5 — Interpretar a variação: aplicar para $n = 3$.**

$\dfrac{[H^+]_{\text{mais ácida}}}{[H^+]_{\text{menos ácida}}} = 10^3 = 1000$

Ou seja, uma diferença de 3 unidades de pH corresponde a uma concentração de íons $H^+$ **1000 vezes maior** na solução mais ácida — a variação é exponencial (multiplicativa por potência de 10), não linear.

**Conclusão:** a expressão geral correta é $10^n$, e para $n=3$ a solução mais ácida tem concentração de $H^+$ 1000 vezes maior, o que corresponde à alternativa A.

## Formalização verificável

- `propriedade` — expressão `10**n`, esperado `10**n`, parâmetros `{'sequencia': 'pg', 'a1': '10', 'razao': '10'}`
- `funcao` — expressão `10**n`, esperado `1000`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: define a fórmula, os dados (M_A e M_B) e a pergunta são inequívocos. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O processo cognitivo real exigido é aplicar a definição de logaritmo e resolver uma equação (Aplicar/Analisar em Bloom, resposta relacional em SOLO), não 'Criar'. Não há elaboração de problema, generalização, síntese ou produção de algo novo por parte do aluno — apenas substituição de valores e resolução de log. A rubrica exige coerência entre o nível declarado e a estrutura de resposta esperada, o que não ocorre aqui.
  - alinhamento_bncc: 3/5 — A questão cumpre a parte de 'compreender e interpretar a variação das grandezas' (a resolução explicita que a escala é logarítmica e que a diferença de magnitude vira fator multiplicativo, não aditivo), o que é o núcleo da habilidade. Porém a habilidade também prevê 'elaborar problemas', o que não é contemplado — a questão é puramente de resolução fechada, e o verbo de Bloom declarado ('criar') não é exercido em nenhum momento do enunciado.
  - distratores: 5/5 — Os quatro distratores mapeiam erros conceituais plausíveis e distintos: confundir diferença de magnitude com razão direta, multiplicar em vez de exponenciar, e dividir magnitudes ao invés de usar a diferença como expoente. Nenhum é trivialmente eliminável.
  - originalidade: 3/5 — O contexto da escala Richter é um exemplo canônico e recorrente em livros didáticos para logaritmos; embora bem construído, não há elemento diferenciador (dado inédito, situação combinada, comparação múltipla) que fuja do padrão consagrado do 'efeito Topaze' de exemplos-modelo.
  - *sugestões:* 1) Corrigir a incompatibilidade entre o nível de Bloom declarado ('criar') e o que a questão realmente demanda: ou (a) reclassificar a especificação para 'aplicar' ou 'analisar', que é o que a tarefa atual exige, ou (b) reformular a questão para efetivamente exigir criação — por exemplo, pedir que o aluno elabore uma fórmula geral que relacione a razão I_B/I_A a qualquer diferença de magnitude (M_B - M_A), ou que formule e resolva um problema análogo (por exemplo, comparando três terremotos, ou relacionando magnitude com pH/radioatividade), evidenciando a produção de um novo problema, não apenas o cálculo de um caso particular. 2) Para reforçar o alinhamento pleno com EM13MAT305 (que menciona 'resolver E elaborar'), incluir uma segunda parte na questão em que o aluno deva generalizar a relação (ex.: 'Mostre que, em geral, se M_B - M_A = n, então I_B = I_A · 10^n') ou justificar por que a variação da intensidade cresce exponencialmente enquanto a magnitude cresce linearmente, tornando a interpretação da variação o núcleo explícito da tarefa, e não apenas um comentário na resolução. 3) Para aumentar a originalidade, variar o contexto clássico da escala Richter, combinando-o com outro fenômeno logarítmico (pH ou decaimento radioativo) num mesmo problema, ou introduzindo um dado extra que exija do aluno decidir qual variável usar, evitando o formato-modelo de livro didático.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Corrigir a incompatibilidade entre o nível de Bloom declarado ('criar') e o que a questão realmente demanda: ou (a) reclassificar a especificação para 'aplicar' ou 'analisar', que é o que a tarefa atual exige, ou (b) reformular a questão para efetivamente exigir criação — por exemplo, pedir que o aluno elabore uma fórmula geral que relacione a razão I_B/I_A a qualquer diferença de magnitude (M_B - M_A), ou que formule e resolva um problema análogo (por exemplo, comparando três terremotos, ou relacionando magnitude com pH/radioatividade), evidenciando a produção de um novo problema, não apenas o cálculo de um caso particular. 2) Para reforçar o alinhamento pleno com EM13MAT305 (que menciona 'resolver E elaborar'), incluir uma segunda parte na questão em que o aluno deva generalizar a relação (ex.: 'Mostre que, em geral, se M_B - M_A = n, então I_B = I_A · 10^n') ou justificar por que a variação da intensidade cresce exponencialmente enquanto a magnitude cresce linearmente, tornando a interpretação da variação o núcleo explícito da tarefa, e não apenas um comentário na resolução. 3) Para aumentar a originalidade, variar o contexto clássico da escala Richter, combinando-o com outro fenômeno logarítmico (pH ou decaimento radioativo) num mesmo problema, ou introduzindo um dado extra que exija do aluno decidir qual variável usar, evitando o formato-modelo de livro didático.

### Iteração 2

- **Verificador:** aprovado_parcial — 1 de 2 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (crescente em Reals). | (2) nao_verificavel: Falha ao processar a expressão (NotImplementedError: No algorithms are implemented to solve equation 10**pH_A/10**pH_B - 10**(pH_A - pH_B)). Revisar a formalização produzida pelo Gerador.
  - funcao/crescimento=aprovado
  - equacao=nao_verificavel
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é longo, mas não ambíguo: os dados (definições de M e pH, a relação já demonstrada para Richter, e a condição pH_A - pH_B = n) e o pedido (encontrar a expressão para [H+]_B/[H+]_A) estão explícitos e completos.
  - adequacao_nivel: 2/5 — O enunciado fornece, passo a passo, toda a derivação da fórmula análoga (I_B/I_A=10^n) e a resolução repete quase literalmente os mesmos passos trocando o sinal de pH. O que resta ao aluno é apenas uma aplicação direta de definição com ajuste de sinal — nível 'aplicar' ou no máximo 'analisar' na taxonomia de Bloom, e estrutura de resposta multiestrutural na SOLO. Isso não corresponde ao nível 'criar' declarado, que exigiria produzir algo novo (uma generalização própria, uma justificativa original, ou a elaboração de um problema), não apenas transpor um algoritmo já demonstrado. Além disso, o formato de múltipla escolha é pouco compatível com avaliar 'criar', pois reduz a tarefa a reconhecer a alternativa certa entre opções prontas.
  - alinhamento_bncc: 3/5 — A questão aborda dois contextos citados na habilidade (Richter e pH) e a resolução comenta a relação entre variação aditiva na escala log e variação multiplicativa na grandeza — o que atende parcialmente à exigência de 'interpretar a variação'. Porém, a tarefa efetivamente cobrada do aluno (escolher a alternativa) se resume a aplicar a definição de pH com troca de sinal, sem exigir que ele próprio articule ou explicite a interpretação da variação; os dois contextos são justapostos (um serve de 'modelo' para copiar, o outro é o alvo) mais do que verdadeiramente integrados em um raciocínio criado pelo aluno.
  - distratores: 4/5 — Os três distratores representam erros plausíveis: (b) esquecer de ajustar o sinal negativo do pH; (c) confundir a propriedade de potência com multiplicação linear; (d) inverter a operação log/exponencial. Nenhum é trivialmente absurdo, embora (d) seja um pouco menos tentador que os demais, pois exige um erro conceitual mais grosseiro.
  - originalidade: 2/5 — Embora a ideia de pedir a transferência de um raciocínio de um contexto (Richter) para outro (pH) seja interessante, o enunciado comete um forte 'efeito Topaze': fornece a derivação completa e o padrão exato de resolução a ser copiado, esvaziando o desafio. O aluno não precisa descobrir o caminho, apenas substituir sinais em uma fórmula já demonstrada passo a passo.
  - *sugestões:* 1) Remova ou resuma drasticamente a derivação passo a passo da fórmula de Richter no enunciado — apresente apenas o resultado final (I_B/I_A = 10^n) sem mostrar todo o raciocínio intermediário, para que o aluno precise reconstruir a lógica sozinho ao aplicá-la ao pH. 2) Se o objetivo é avaliar o nível 'criar' da Bloom, troque o formato de múltipla escolha por uma questão discursiva ou de elaboração, pedindo, por exemplo, que o aluno formule e justifique a expressão geral, ou que crie um problema numérico análogo (com valores de pH) explorando a variação. 3) Reforce a exigência de 'interpretar a variação': peça explicitamente que o aluno explique o que significa, em termos de acidez, uma diferença de n unidades de pH (ex.: 'quantas vezes mais concentrada em H+ é a solução B'), e não apenas que escolha a fórmula correta. 4) Ajuste o nível de Bloom declarado para 'aplicar' ou 'analisar' caso mantenha o formato atual de múltipla escolha com todo o raciocínio-modelo fornecido no enunciado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Remova ou resuma drasticamente a derivação passo a passo da fórmula de Richter no enunciado — apresente apenas o resultado final (I_B/I_A = 10^n) sem mostrar todo o raciocínio intermediário, para que o aluno precise reconstruir a lógica sozinho ao aplicá-la ao pH. 2) Se o objetivo é avaliar o nível 'criar' da Bloom, troque o formato de múltipla escolha por uma questão discursiva ou de elaboração, pedindo, por exemplo, que o aluno formule e justifique a expressão geral, ou que crie um problema numérico análogo (com valores de pH) explorando a variação. 3) Reforce a exigência de 'interpretar a variação': peça explicitamente que o aluno explique o que significa, em termos de acidez, uma diferença de n unidades de pH (ex.: 'quantas vezes mais concentrada em H+ é a solução B'), e não apenas que escolha a fórmula correta. 4) Ajuste o nível de Bloom declarado para 'aplicar' ou 'analisar' caso mantenha o formato atual de múltipla escolha com todo o raciocínio-modelo fornecido no enunciado.

### Iteração 3

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 10**n: coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(3) = 1000).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado define pH, estabelece a condição pH_A - pH_B = n e explicita quem é mais ácida, evitando ambiguidade central. Pequena imprecisão: as alternativas usam 'mais ácida/menos ácida' em vez de referenciar diretamente A e B, exigindo do aluno uma tradução implícita, mas isso não compromete a compreensão geral.
  - adequacao_nivel: 2/5 — O processo cognitivo real exigido é apenas manipular a definição de pH com propriedades de logaritmo (subtração de logs → quociente → forma exponencial) e substituir n=3 — isso é 'aplicar' (nível 3 de Bloom), no máximo 'analisar' pela comparação A/B. Não há produção de algo novo, generalização inédita, elaboração de problema ou julgamento crítico que caracterize 'criar' (nível 6). O formato de múltipla escolha, aliás, é estruturalmente incompatível com o nível 'criar', que demanda resposta aberta e construtiva (estrutura SOLO 'estendido abstrato' com produção original), não seleção entre opções prontas.
  - alinhamento_bncc: 3/5 — A questão trata de log de pH e pede interpretação numérica da variação (10^n vezes), o que toca a habilidade EM13MAT305. Porém a habilidade fala em 'resolver e elaborar problemas... compreender e interpretar a variação das grandezas' — aqui não há elaboração de problema, e a 'interpretação da variação' se reduz a um cálculo padrão (10^3=1000), sem explorar comparações múltiplas, taxas de variação, gráficos ou generalizações que evidenciem compreensão mais profunda da variação logarítmica exigida pela habilidade.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: linearização indevida (10n), troca de base (e^n) e inversão do sentido da razão (10^-n). Nenhum é trivialmente eliminável, e cobrem os erros conceituais mais comuns nesse tipo de exercício.
  - originalidade: 2/5 — O contexto de pH e a derivação da razão de concentrações via diferença de logaritmos é um exercício extremamente recorrente em livros didáticos e listas de exercícios sobre logaritmo. Não há elemento de contextualização real (dados de substâncias, situação prática, comparação com valores tabelados) nem quebra do padrão 'aplique a fórmula e calcule para n=3', o que caracteriza reprodução mecânica de enunciado clássico.
  - *sugestões:* 1) Ajustar o nível de Bloom: ou declarar 'aplicar'/'analisar' (compatível com o que a questão de fato exige), ou reformular a tarefa para exigir produção genuína — por exemplo, pedir que o aluno elabore/generalize uma fórmula para comparar N soluções, proponha um novo cenário com dados incompletos que precisem ser inferidos, ou julgue/critique uma afirmação incorreta sobre variação de pH, evitando o formato de múltipla escolha que é incompatível com 'criar'. 2) Fortalecer o alinhamento à habilidade EM13MAT305: inclua exploração mais rica da variação (ex.: comparar como a razão de concentrações cresce à medida que n aumenta, ou pedir a construção de um problema envolvendo pH de substâncias reais com dados verificáveis), não apenas o cálculo pontual de 10^3. 3) Tornar o contexto mais original e significativo: usar dados reais (ex.: pH de chuva ácida, suco gástrico, água potável) com valores concretos de duas soluções nomeadas, em vez de A e B abstratas, e evitar a estrutura-modelo de 'derive a fórmula e aplique para n=3' tão presente em livros didáticos.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar o nível de Bloom: ou declarar 'aplicar'/'analisar' (compatível com o que a questão de fato exige), ou reformular a tarefa para exigir produção genuína — por exemplo, pedir que o aluno elabore/generalize uma fórmula para comparar N soluções, proponha um novo cenário com dados incompletos que precisem ser inferidos, ou julgue/critique uma afirmação incorreta sobre variação de pH, evitando o formato de múltipla escolha que é incompatível com 'criar'. 2) Fortalecer o alinhamento à habilidade EM13MAT305: inclua exploração mais rica da variação (ex.: comparar como a razão de concentrações cresce à medida que n aumenta, ou pedir a construção de um problema envolvendo pH de substâncias reais com dados verificáveis), não apenas o cálculo pontual de 10^3. 3) Tornar o contexto mais original e significativo: usar dados reais (ex.: pH de chuva ácida, suco gástrico, água potável) com valores concretos de duas soluções nomeadas, em vez de A e B abstratas, e evitar a estrutura-modelo de 'derive a fórmula e aplique para n=3' tão presente em livros didáticos.
