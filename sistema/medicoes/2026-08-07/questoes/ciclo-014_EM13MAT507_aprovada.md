# Ciclo 014 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Uma ONG de reflorestamento planeja plantar mudas de árvores ao longo de 10 anos consecutivos. No primeiro ano são plantadas 12 mudas. A cada ano seguinte, o número de mudas plantadas aumenta sempre em 5 unidades em relação ao ano anterior, formando uma progressão aritmética (PA) cujos termos correspondem à quantidade de mudas plantadas em cada ano n (n = 1, 2, 3, ..., 10).

a) Escreva a função afim $f(n)$, com domínio restrito aos números naturais de 1 a 10, que fornece o número de mudas plantadas no ano n, e explique por que essa restrição de domínio é necessária no contexto do problema.

b) Usando a função $f(n)$, determine quantas mudas serão plantadas no 10º ano.

c) Calcule o número total de mudas plantadas ao longo dos 10 anos, utilizando a fórmula da soma dos termos da PA.

## Gabarito

f(n) = 5n + 7, com domínio {1,2,...,10} ⊂ ℕ; f(10) = 57 mudas no 10º ano; soma total = 345 mudas.

## Resolução

**a) Associando a PA à função afim**

Os termos da PA são: $a_1 = 12$, $a_2 = 17$, $a_3 = 22$, ... com razão $r = 5$.

O termo geral da PA é $a_n = a_1 + (n-1)r = 12 + (n-1)\cdot 5 = 5n + 7$.

Como esse termo geral tem a forma $a_n = 5n+7$, que é uma expressão do tipo $f(x) = mx + b$ (com $m=5$ e $b=7$), a sequência corresponde à restrição de uma função afim $f(n) = 5n+7$ ao conjunto discreto $\{1,2,3,\dots,10\}\subset \mathbb{N}$.

A restrição do domínio a esses valores naturais é necessária porque **n representa o número do ano**, uma contagem, e não faz sentido considerar anos fracionários, negativos ou não inteiros (por exemplo, $n=2{,}5$ não corresponde a nenhum ano real do plantio). Assim, embora a fórmula $f(n)=5n+7$ esteja definida para todo número real, no contexto do problema ela só tem significado para $n \in \{1,2,\dots,10\}$.

**b) Valor no 10º ano**

$f(10) = 5(10) + 7 = 50 + 7 = 57$.

No 10º ano serão plantadas **57 mudas**.

**c) Soma dos 10 termos da PA**

$S_{10} = \dfrac{(a_1 + a_{10})\cdot 10}{2} = \dfrac{(12 + 57)\cdot 10}{2} = \dfrac{69 \cdot 10}{2} = 345$.

Ao longo dos 10 anos serão plantadas ao todo **345 mudas**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*n + 7`, parâmetros `{'pontos': '[(1,12),(2,17),(3,22)]', 'grau': '1', 'sequencia': 'pa', 'a1': '12', 'razao': '5'}`
- `progressao` — expressão `-`, esperado `345`, parâmetros `{'tipo_progressao': 'pa', 'a1': '12', 'razao': '5', 'n': '10', 'consulta': 'soma'}`
- `funcao` — expressão `5*n + 7`, esperado `57`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 7*n + 5: reproduz os 2 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Gabarito confirmado (soma da PA = 435).
  - propriedade=aprovado
  - equacao=aprovado
  - progressao/soma=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é bem estruturado, com dados suficientes (a1=12, a5=40) e comandos objetivos em a, b, c. Porém há um problema de redação: dentro do próprio item a) o enunciado já revela 'f(n) = 7n + 5' antes de pedir que o aluno a determine, o que gera uma inconsistência lógica na sequência de comandos (pede para 'escrever a lei' e, na frase seguinte, já a informa).
  - adequacao_nivel: 2/5 — O nível declarado é 'analisar' (Bloom), mas ao fornecer explicitamente a lei f(n)=7n+5 antes que o aluno precise deduzi-la, o processo cognitivo real exigido cai para 'aplicar/lembrar' nesse trecho central. Os itens b) e c) são aplicação direta de fórmulas (resolver equação linear, aplicar soma de PA), compatíveis com nível unistrutural/multiestrutural na taxonomia SOLO, não relacional/analítico. Apenas a justificativa sobre domínio discreto exige alguma análise, mas fica isolada e sem sustentação, já que a dedução da função foi 'entregue'.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT507 exige que a associação PA-função afim seja efetivamente deduzida pelo aluno, incluindo a construção de fórmulas. Como o enunciado antecipa a lei da função, a dedução deixa de ser exigida na prática — o aluno pode simplesmente confirmar um resultado já dado, em vez de construí-lo. A discussão sobre domínio discreto, embora pertinente à habilidade, fica comprometida por vir acoplada a uma resposta já fornecida, enfraquecendo o cumprimento pleno da exigência declarada.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — O contexto (marcenaria, PA de produção mensal) é razoavelmente comum em livros didáticos, mas o maior problema é o efeito Topaze evidente: o enunciado revela a fórmula f(n)=7n+5 antes de pedir que o aluno a obtenha, pavimentando a solução e esvaziando o desafio da parte de dedução, que é justamente o cerne da habilidade BNCC visada.
  - *sugestões:* Reescrever o item a) para não revelar a lei da função antes de o aluno determiná-la. Sugestão: 'a) Determine a razão da PA e escreva a lei da função afim f(n) que associa a cada mês n a produção de cadeiras. Em seguida, explique por que o gráfico de f, embora tenha a forma algébrica de uma reta, deve ser representado apenas por pontos isolados nesse contexto (justifique em termos de domínio discreto).' Isso preserva a exigência de dedução antes da discussão conceitual. Além disso, para elevar o nível cognitivo a 'analisar' de fato, seria interessante acrescentar uma pergunta que exija comparar/relacionar duas representações (por exemplo, pedir que o aluno identifique o erro de um colega que usou a fórmula da reta contínua para estimar uma produção em 'mês 4,5', ou que compare a soma da PA com a área sob a reta contínua entre n=1 e n=10, discutindo por que os valores diferem). Os itens b) e c), tal como estão, permanecem em nível de aplicação; isso é aceitável como parte da questão, mas o núcleo analítico deve ser reforçado e não comprometido por dar a resposta antecipadamente.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reescrever o item a) para não revelar a lei da função antes de o aluno determiná-la. Sugestão: 'a) Determine a razão da PA e escreva a lei da função afim f(n) que associa a cada mês n a produção de cadeiras. Em seguida, explique por que o gráfico de f, embora tenha a forma algébrica de uma reta, deve ser representado apenas por pontos isolados nesse contexto (justifique em termos de domínio discreto).' Isso preserva a exigência de dedução antes da discussão conceitual. Além disso, para elevar o nível cognitivo a 'analisar' de fato, seria interessante acrescentar uma pergunta que exija comparar/relacionar duas representações (por exemplo, pedir que o aluno identifique o erro de um colega que usou a fórmula da reta contínua para estimar uma produção em 'mês 4,5', ou que compare a soma da PA com a área sob a reta contínua entre n=1 e n=10, discutindo por que os valores diferem). Os itens b) e c), tal como estão, permanecem em nível de aplicação; isso é aceitável como parte da questão, mas o núcleo analítico deve ser reforçado e não comprometido por dar a resposta antecipadamente.

### Iteração 2

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 5*n + 7: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (soma da PA = 345). | (3) aprovado: Gabarito confirmado (f(10) = 57). | (4) rejeitado: Divergência: domínio calculado: Reals; gabarito: Naturals.
  - propriedade=aprovado
  - progressao/soma=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 5*n + 7: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (soma da PA = 345). | (3) aprovado: Gabarito confirmado (f(10) = 57). | (4) rejeitado: Divergência: domínio calculado: Reals; gabarito: Naturals. Resultado calculado independentemente: 5*n + 7 | 345 | f(10) = 57 | domínio calculado: Reals. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*n + 7: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (soma da PA = 345). | (3) aprovado: Gabarito confirmado (f(10) = 57).
  - propriedade=aprovado
  - progressao/soma=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente os dados (a1=12, r=5, 10 anos) e separa nitidamente o que é pedido em cada item (a, b, c). Não há ambiguidade lexical ou estrutural, e as condições do domínio discreto são explicitadas.
  - adequacao_nivel: 3/5 — O verbo 'analisar' exige comparação, decomposição e relação entre conceitos (SOLO relacional), mas a questão, exceto pela justificativa do domínio no item (a), reduz-se a aplicar fórmulas conhecidas (termo geral e soma da PA) — estrutura predominantemente multiestrutural. A explicação pedida em (a) é o único ponto que se aproxima de 'analisar', mas é curta e pouco explorada; (b) e (c) são aplicação direta.
  - alinhamento_bncc: 4/5 — O item (a) atende bem à exigência central da habilidade: exige explicitamente escrever f(n) a partir da PA e justificar a restrição do domínio discreto, articulando os dois conceitos. Porém, os itens (b) e (c) apenas aplicam fórmulas de PA (termo geral, soma) sem retomar ou aprofundar a relação função-afim/PA, funcionando quase como itens independentes justapostos ao (a), o que enfraquece a articulação exigida ao longo de toda a questão.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de reflorestamento é minimamente significativo e foge do exemplo genérico de 'sequência de números', mas ainda é um cenário recorrente em materiais didáticos (crescimento linear ano a ano). Não há pistas excessivas no enunciado que antecipem a resposta (o scaffolding aparece só na resolução, não no enunciado), preservando parte do desafio.
