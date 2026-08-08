# Ciclo 017 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 2

## Enunciado

O pH de uma solução aquosa é definido por $pH = -\log_{10}[H^+]$, em que $[H^+]$ é a concentração de íons hidrogênio, em mol/L. Essa é uma escala logarítmica: variações constantes de pH correspondem a variações multiplicativas (e não aditivas) na concentração de $H^+$.

Um laboratório analisa duas amostras, A e B, e verifica que o pH de A é maior que o pH de B, sendo $\Delta$ a diferença entre os dois valores de pH (isto é, $pH_A - pH_B = \Delta$).

A partir da definição de pH, é possível deduzir uma expressão geral, em função de $\Delta$, para a razão $\dfrac{[H^+]_B}{[H^+]_A}$, que indica quantas vezes a concentração de $H^+$ de B é maior que a de A (ou seja, quantas vezes B é mais ácida que A).

Usando essa expressão geral, determine aproximadamente quantas vezes a amostra B é mais ácida que a amostra A, sabendo que $\Delta = 2{,}5$.

## Alternativas

- (a) B é aproximadamente 316 vezes mais ácida que A, pois $10^{2,5}\approx 316,2$.  ← correta
- (b) A é aproximadamente 316 vezes mais ácida que B.
  - *erro representado:* Inverteu a relação entre pH maior/menor e concentração de H+, atribuindo a maior acidez à amostra de maior pH.
- (c) B é 25 vezes mais ácida que A, pois $2{,}5 \times 10 = 25$.
  - *erro representado:* Tratou a variação da escala logarítmica como linear (multiplicando Δ por 10), em vez de usar 10 elevado a Δ.
- (d) B é aproximadamente 12,18 vezes mais ácida que A, pois $e^{2,5}\approx 12{,}18$.
  - *erro representado:* Usou a base do logaritmo natural (e) em vez da base 10, que é a base correta da escala de pH.

## Gabarito

A amostra B é aproximadamente 316 vezes mais ácida que a amostra A, pois $[H^+]_B/[H^+]_A = 10^{2,5} \approx 316,2$.

## Resolução

**Passo 1 — Elaborar a expressão geral.**

Pela definição, $pH_A = -\log_{10}[H^+]_A$ e $pH_B = -\log_{10}[H^+]_B$.

Como $pH_A - pH_B = \Delta$, temos:

$-\log_{10}[H^+]_A - \left(-\log_{10}[H^+]_B\right) = \Delta$

$\log_{10}[H^+]_B - \log_{10}[H^+]_A = \Delta$

Pela propriedade do logaritmo do quociente:

$\log_{10}\left(\dfrac{[H^+]_B}{[H^+]_A}\right) = \Delta$

Logo, a expressão geral procurada é:

$$\dfrac{[H^+]_B}{[H^+]_A} = 10^{\Delta}$$

Essa fórmula mostra que, na escala de pH, cada unidade de diferença corresponde a uma multiplicação por 10 na concentração de $H^+$ — é isso que caracteriza a variação logarítmica da grandeza.

**Passo 2 — Aplicar a expressão a $\Delta = 2{,}5$.**

$$\dfrac{[H^+]_B}{[H^+]_A} = 10^{2{,}5} = 10^{2}\cdot 10^{1/2} = 100\sqrt{10} \approx 316{,}2$$

**Conclusão:** a amostra B é aproximadamente **316 vezes mais ácida** que a amostra A.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `10**Delta`, parâmetros `{'forma': '10**Delta'}`
- `equacao` — expressão `Eq(razao, 10**Rational(5,2))`, esperado `[100*sqrt(10)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - equacao=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem construído: define claramente a fórmula, os dados (magnitudes 4 e 6) e a pergunta (razão entre amplitudes). Não há ambiguidade lexical ou estrutural, e a informação de que A0 é fixa para a região elimina qualquer dúvida sobre variáveis desconhecidas.
  - adequacao_nivel: 2/5 — A especificação declara nível Bloom 'criar', mas a tarefa efetivamente exigida é montar duas equações log e dividir potências — processo de 'aplicar' (definição de log) com, no máximo, 'analisar' (relacionar duas equações). Não há produção de algo novo, elaboração de estratégia original ou síntese exigida por 'criar'. Na taxonomia SOLO, a resposta é relacional (combina duas relações dadas), não estendida abstrata, que seria esperada em 'criar'. Há um descompasso claro entre o nível cognitivo declarado e o que a questão de fato demanda do estudante.
  - alinhamento_bncc: 4/5 — A questão cumpre a exigência central da habilidade: usa função logarítmica em contexto realista (sismos) e exige compreender que uma diferença aditiva na escala log corresponde a uma variação multiplicativa (exponencial) na grandeza física — isso vai além de 'só aplicar a definição', pois o aluno precisa interpretar a natureza da variação, não apenas calcular um logaritmo isolado. Falta, porém, a dimensão de 'elaborar problemas' prevista na habilidade, já que a questão apenas resolve um problema fechado em formato de múltipla escolha.
  - distratores: 5/5 — Os quatro distratores mapeiam erros conceituais plausíveis e distintos: tratar a escala como linear (2x), confundir multiplicação com potenciação (20x) e tratar a razão de magnitudes como proporcional à amplitude (1,5x). Nenhum é absurdo ou trivialmente descartável sem raciocínio.
  - originalidade: 3/5 — O contexto de escala Richter para introduzir logaritmos é um dos exemplos mais recorrentes em livros didáticos e material de vestibular; a formulação 'quantas vezes maior é a amplitude' também é um padrão clássico. Não há elemento de contextualização adicional (dado real, situação inédita, comparação com outro fenômeno) que diferencie a questão do lugar-comum.
  - *sugestões:* Ajustar o nível cognitivo real da questão para condizer com 'criar', ou rebaixar a especificação de Bloom para 'aplicar/analisar', que é o que a tarefa de fato demanda. Para elevar genuinamente ao nível 'criar', seria necessário pedir, por exemplo, que o aluno elabore uma fórmula geral para a razão de amplitudes em função da diferença de magnitudes (ou proponha e justifique um cenário sísmico hipotético cuja razão de amplitudes seja um valor dado, deduzindo a diferença de magnitude necessária), exigindo formulação de um modelo, não apenas substituição em fórmula pronta. Além disso, para aumentar originalidade, seria interessante trocar o contexto padrão de terremotos por outra grandeza logarítmica menos batida (pH, decibéis, datação radioativa) ou inserir um dado numérico/contextual menos previsível (ex.: comparação com um terremoto histórico real, tabela de dados).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar o nível cognitivo real da questão para condizer com 'criar', ou rebaixar a especificação de Bloom para 'aplicar/analisar', que é o que a tarefa de fato demanda. Para elevar genuinamente ao nível 'criar', seria necessário pedir, por exemplo, que o aluno elabore uma fórmula geral para a razão de amplitudes em função da diferença de magnitudes (ou proponha e justifique um cenário sísmico hipotético cuja razão de amplitudes seja um valor dado, deduzindo a diferença de magnitude necessária), exigindo formulação de um modelo, não apenas substituição em fórmula pronta. Além disso, para aumentar originalidade, seria interessante trocar o contexto padrão de terremotos por outra grandeza logarítmica menos batida (pH, decibéis, datação radioativa) ou inserir um dado numérico/contextual menos previsível (ex.: comparação com um terremoto histórico real, tabela de dados).

### Iteração 2

- **Verificador:** aprovado_parcial — 1 de 2 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Falha ao processar a expressão (PolynomialError: 10**Delta contains an element of the set of generators.). Revisar a formalização produzida pelo Gerador. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=nao_verificavel
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a grandeza pH, os dados (Δ = pH_A - pH_B) e o que se pede (razão [H+]_B/[H+]_A e seu valor numérico). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para a resolução.
  - adequacao_nivel: 3/5 — O enunciado descreve um processo de dedução de fórmula geral (que poderia justificar 'criar' ou ao menos 'analisar'), mas o formato de múltipla escolha só avalia o resultado numérico final (10^2,5≈316), não a capacidade do aluno de formular a expressão geral por conta própria — essa etapa já é praticamente entregue no próprio enunciado ('é possível deduzir uma expressão... a partir da definição'). Assim, o que é efetivamente cobrado nas alternativas corresponde a um nível cognitivo de 'aplicar', inferior ao 'criar' declarado. Há descompasso entre o processo narrado na resolução (que exige elaboração) e o que é de fato testado pela escolha de alternativa.
  - alinhamento_bncc: 4/5 — A questão trata de função logarítmica em contexto de pH e exige compreender que uma variação aditiva de Δ unidades de pH corresponde a uma variação multiplicativa de 10^Δ na concentração de H+ — isso vai além da mera aplicação da definição de log, atendendo ao requisito de interpretar a variação das grandezas. O contexto é realista e pertinente à habilidade EM13MAT305. Ainda assim, como apontado no critério anterior, a interpretação da variação fica mais evidente na resolução do que na tarefa cognitiva real exigida pelas alternativas.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis: inversão da relação pH/acidez, tratamento linear em vez de exponencial da escala (erro clássico em escalas logarítmicas) e uso da base errada (e em vez de 10). Nenhum é absurdo ou trivialmente eliminável sem raciocínio.
  - originalidade: 4/5 — O contexto de pH é um clássico dos livros didáticos, mas a proposta de deduzir uma expressão geral em função de Δ (em vez de apenas calcular pH a partir de uma concentração dada) traz um viés menos mecânico que o problema padrão. Ainda há certo efeito 'Topaze', pois o enunciado praticamente indica o caminho da dedução ('a partir da definição de pH, é possível deduzir...'), reduzindo a autonomia do aluno na etapa de formulação.
