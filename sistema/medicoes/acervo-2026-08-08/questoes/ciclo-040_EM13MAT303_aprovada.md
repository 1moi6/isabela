# Ciclo 040 — EM13MAT303

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Um capital (ou salário, preço, etc.) $C$ sofre $k$ reajustes percentuais sucessivos, aplicados um após o outro sobre o valor já atualizado pelo reajuste anterior. Sejam $p_1\%, p_2\%, \dots, p_k\%$ as taxas de cada reajuste (não necessariamente iguais).

**(a)** Demonstre que o valor final é dado por
$$C_f = C\cdot\prod_{i=1}^{k}\left(1+\frac{p_i}{100}\right).$$
Em seguida, explique por que, em geral, esse valor **não** é igual ao que se obteria somando diretamente as taxas, isto é, por que $C_f \neq C\left(1+\dfrac{p_1+p_2+\dots+p_k}{100}\right)$, exceto em casos particulares.

**(b)** Suponha agora que todos os reajustes tenham a mesma taxa $p\%$. Escreva $C_f$ em função de $k$ e explique, usando as propriedades da função exponencial, por que esse crescimento é exponencial em $k$ (e não linear).

**(c)** Dois reajustes sucessivos de $20\%$ e $30\%$ são aplicados a um mesmo capital. Determine a taxa única $p_{eq}\%$ que, aplicada de uma só vez, produziria exatamente o mesmo resultado. Mostre explicitamente que $p_{eq} \neq 20+30 = 50$.

**(d)** Generalize o resultado do item (c): obtenha uma expressão para a taxa única equivalente $p_{eq}$ em função de $k$ taxas distintas $p_1, p_2, \dots, p_k$. Em seguida, **elabore você mesmo um problema contextualizado original** (por exemplo, sobre reajustes salariais anuais sucessivos, correção monetária ao longo de vários anos, ou aumentos em cadeia de custos de produção) cuja solução exija necessariamente o uso dessa fórmula geral — isto é, um problema com pelo menos três taxas distintas de reajuste. Escreva o enunciado completo do seu problema, atribua valores numéricos às taxas e ao valor inicial, e apresente a resolução completa, indicando com clareza em que passo a fórmula geral do item (d) é aplicada.

## Gabarito

(a) $C_f = C\prod_{i=1}^k(1+p_i/100)$, diferente da soma das taxas devido aos termos cruzados (produtos $p_ip_j$). (b) $C_f(k)=C(1+p/100)^k$, função exponencial crescente em $k$. (c) $p_{eq}=56\%\neq 50\%$. (d) $p_{eq}=100\left[\prod_{i=1}^k(1+p_i/100)-1\right]$; problema elaborado deve ter pelo menos três taxas distintas e resolução completa mostrando a aplicação dessa fórmula (exemplo: salário R$2000 com reajustes de 8%, 5% e 10% resulta em R$2494,80 e taxa equivalente de 24,74%).

## Resolução

**(a)** Cada reajuste multiplica o valor atual por um fator $(1+p_i/100)$. Encadeando os $k$ reajustes:
$$C_1 = C(1+p_1/100),\quad C_2 = C_1(1+p_2/100) = C(1+p_1/100)(1+p_2/100),\ \dots$$
$$C_f = C\prod_{i=1}^{k}(1+p_i/100).$$
Se expandirmos o produto para $k=2$, por exemplo:
$$\left(1+\frac{p_1}{100}\right)\left(1+\frac{p_2}{100}\right)=1+\frac{p_1+p_2}{100}+\frac{p_1p_2}{10000}.$$
O termo $\dfrac{p_1p_2}{10000}$ (efeito de 'juros sobre juros') não aparece na soma simples das taxas. Logo $C_f = C(1+\frac{p_1+p_2}{100})$ só valeria se esse termo cruzado fosse nulo, o que só ocorre se alguma taxa for $0\%$.

**(b)** Com taxas iguais a $p\%$:
$$C_f(k) = C\left(1+\frac{p}{100}\right)^k.$$
Essa é uma função exponencial de $k$, pois a variável $k$ aparece no **expoente** e a base $b=1+p/100$ é constante. Como $p>0 \Rightarrow b>1$, a função é estritamente crescente e seu crescimento é multiplicativo a cada unidade de $k$ (cada novo reajuste multiplica o valor anterior por $b$), e não aditivo como seria num crescimento linear $C+ C\cdot p\cdot k/100$.

**(c)** Fator total: $\left(1+\frac{20}{100}\right)\left(1+\frac{30}{100}\right) = 1{,}2\times 1{,}3 = 1{,}56$.
Logo $1+\frac{p_{eq}}{100}=1{,}56 \Rightarrow p_{eq}=56\%$.
Como $56 \neq 20+30=50$, fica evidenciado que a composição de percentuais não é aditiva — a diferença de $6$ pontos percentuais é exatamente o termo cruzado $\frac{20\cdot 30}{10000}\times 100 = 6$.

**(d)** Generalização: o fator total é $F=\prod_{i=1}^{k}\left(1+\dfrac{p_i}{100}\right)$, e a taxa única equivalente satisfaz $1+\dfrac{p_{eq}}{100}=F$, ou seja:
$$p_{eq} = 100\left[\prod_{i=1}^{k}\left(1+\frac{p_i}{100}\right)-1\right].$$

**Exemplo de problema elaborado (modelo de resposta esperada):**
*'O salário de um funcionário sofreu três reajustes sucessivos: 8% no primeiro ano, 5% no segundo ano e 10% no terceiro ano. Se o salário inicial era R$ 2.000,00, qual foi o salário final após os três reajustes, e qual seria a taxa percentual única equivalente aos três reajustes aplicados de uma só vez?'*

Resolução do problema criado, aplicando a fórmula geral do item (d):
$$F = 1{,}08\times 1{,}05\times 1{,}10 = 1{,}2474.$$
$$S_f = 2000\times 1{,}2474 = R\$\,2494{,}80.$$
$$p_{eq}=100(1{,}2474-1)=24{,}74\%.$$
Observe que $24{,}74\% \neq 8+5+10=23\%$, confirmando novamente o caráter multiplicativo (exponencial) da composição de reajustes percentuais — exatamente o que a fórmula do item (d) permite calcular de forma exata, e que uma soma simples de percentuais não conseguiria captar.

## Formalização verificável

- `equacao` — expressão `Eq(1 + p_eq/100, (1+Rational(20,100))*(1+Rational(30,100)))`, esperado `[56]`
- `funcao` — expressão `(1+Rational(1,10))**k`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `equacao` — expressão `Eq(sf, 2000*(1+Rational(8,100))*(1+Rational(5,100))*(1+Rational(10,100)))`, esperado `[Rational(12474,5)]`
- `equacao` — expressão `Eq(1 + peq/100, (1+Rational(8,100))*(1+Rational(5,100))*(1+Rational(10,100)))`, esperado `[Rational(1237,50)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para p**2/100 + 2*p: reproduz os 3 pontos dados; grau 2. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem segmentado em três itens, com dados completos (G0, p, n) e comandos verbais precisos ('escreva', 'mostre', 'determine'). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O nível declarado é 'criar' (Bloom), mas as tarefas pedidas são deduzir uma fórmula (compreender/aplicar), demonstrar uma relação (analisar) e resolver uma equação (aplicar). Em nenhum momento o aluno é convidado a gerar/produzir algo novo — elaborar um problema, propor um modelo alternativo, sintetizar uma situação inédita. A estrutura de resposta esperada é relacional (SOLO), não estendida-abstrata, que seria compatível com 'criar'. Há desalinhamento claro entre o verbo de Bloom declarado e o processo cognitivo efetivamente demandado.
  - alinhamento_bncc: 5/5 — As duas exigências listadas pelo professor são plenamente satisfeitas: a questão envolve porcentagem/juros compostos, e o caráter exponencial é evidenciado de forma explícita e argumentativa (item a contrasta exponencial vs. linear; item b mostra que a taxa efetiva de dois aumentos não é 2p, mas 2p + p²/100, revelando o efeito multiplicativo/composto). Não há apenas uma conta isolada — há articulação conceitual real.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — O tema 'taxa efetiva de aumentos sucessivos' é menos batido que o clássico 'juros compostos, calcule o montante'. A exigência de mostrar por que p_ef ≠ 2p agrega valor argumentativo e evita o efeito Topaze parcialmente, pois força o aluno a justificar, não apenas aplicar fórmula. Ainda assim, o contexto é abstrato/matemático, sem uma situação do cotidiano que tornasse o problema mais significativo.
  - *sugestões:* O principal problema é o descompasso entre o nível de Bloom declarado ('criar') e o que a questão de fato exige (aplicar/analisar). Para corrigir, duas opções: (1) Rebaixar o nível cognitivo declarado na especificação para 'analisar' ou 'aplicar', já que a tarefa é essencialmente deduzir, demonstrar e resolver — isso já garantiria coerência sem alterar o enunciado; ou (2) Reformular a questão para exigir efetivamente uma produção original do aluno, por exemplo acrescentando um item (d) do tipo: 'Generalize o resultado do item (b) para k aumentos sucessivos de taxas distintas p1%, p2%, ..., pk%, e elabore um problema contextualizado (ex.: reajustes salariais anuais diferentes) cuja solução exija aplicar essa generalização' — isso exigiria síntese e criação de um problema novo, compatível com o nível 'criar' e com a parte 'elaborar problemas' da habilidade EM13MAT303. Recomenda-se optar pela opção (2) se o professor quiser manter 'criar' como objetivo pedagógico central.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: O principal problema é o descompasso entre o nível de Bloom declarado ('criar') e o que a questão de fato exige (aplicar/analisar). Para corrigir, duas opções: (1) Rebaixar o nível cognitivo declarado na especificação para 'analisar' ou 'aplicar', já que a tarefa é essencialmente deduzir, demonstrar e resolver — isso já garantiria coerência sem alterar o enunciado; ou (2) Reformular a questão para exigir efetivamente uma produção original do aluno, por exemplo acrescentando um item (d) do tipo: 'Generalize o resultado do item (b) para k aumentos sucessivos de taxas distintas p1%, p2%, ..., pk%, e elabore um problema contextualizado (ex.: reajustes salariais anuais diferentes) cuja solução exija aplicar essa generalização' — isso exigiria síntese e criação de um problema novo, compatível com o nível 'criar' e com a parte 'elaborar problemas' da habilidade EM13MAT303. Recomenda-se optar pela opção (2) se o professor quiser manter 'criar' como objetivo pedagógico central.

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - equacao=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado extenso mas bem segmentado em itens (a)-(d), cada um com dados, condições e pedido inequívocos. Não há ambiguidade lexical ou estrutural; a notação e as fórmulas são apresentadas de forma explícita.
  - adequacao_nivel: 5/5 — A progressão dos itens (demonstrar → aplicar → generalizar → criar) culmina exatamente no nível 'criar' exigido: o aluno deve formular seu próprio problema com pelo menos três taxas e resolvê-lo aplicando a fórmula geral. Isso corresponde ao nível 'extended abstract' da taxonomia SOLO, coerente com Bloom-criar, e os conteúdos (produtos de fatores percentuais, função exponencial) são plenamente compatíveis com o Ensino Médio.
  - alinhamento_bncc: 5/5 — Atende às duas exigências específicas: (1) envolve porcentagem e reajustes sucessivos (análogos a juros compostos) de modo central, não superficial; (2) o caráter exponencial é evidenciado explicitamente no item (b), com justificativa via propriedades da função exponencial (variável no expoente, crescimento multiplicativo vs. linear), e reforçado numericamente nos itens (c) e (d). Os subitens são articulados em torno de um único fio condutor (composição multiplicativa de taxas), não são justapostos.
  - distratores: 5/5 — não se aplica
  - originalidade: 4/5 — O pedido de que o próprio aluno crie um problema contextualizado original é um recurso pedagogicamente valioso e pouco comum em questões de livro didático, evitando o efeito Topaze na parte criativa. Contudo, os itens (a)-(c) reproduzem um esquema bastante tradicional de 'dois reajustes sucessivos de 20% e 30%', reduzindo um pouco a originalidade do conjunto como um todo.
