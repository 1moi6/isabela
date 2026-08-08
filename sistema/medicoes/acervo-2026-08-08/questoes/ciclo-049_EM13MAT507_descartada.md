# Ciclo 049 — EM13MAT507

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Uma empresa de irrigação registra, ao final de cada dia, o volume de água armazenado em um reservatório que está sendo enchido a uma taxa constante. Os registros dos três primeiros dias foram: 22 L (dia 1), 27 L (dia 2) e 32 L (dia 3). O padrão de crescimento diário se mantém enquanto dura o enchimento, e o dia 1 corresponde ao início das medições (n = 1, n natural). Associando essa sequência de medições a uma função afim f(n), que fornece o volume armazenado ao final do dia n, determine em qual dia o reservatório terá 152 litros armazenados.

## Alternativas

- (a) 27º dia  ← correta
- (b) 26º dia
  - *erro representado:* Trata o primeiro registro como correspondente a n = 0 em vez de n = 1, usando incorretamente f(n) = 5n + 22 e resolvendo 5n + 22 = 152, o que dá n = 26.
- (c) 30º dia
  - *erro representado:* Esquece de isolar o termo independente antes de dividir, resolvendo diretamente 5n = 152 (sem subtrair 17), obtendo n = 30,4 e arredondando para 30.
- (d) 33º dia
  - *erro representado:* Inverte o sinal do termo independente ao montar a equação, resolvendo 5n − 17 = 152, o que dá n = 33,8, arredondado (por truncamento) para 33.

## Gabarito

27º dia

## Resolução

**Passo 1 — Reconhecer a PA.** Os volumes registrados formam uma progressão aritmética: $22, 27, 32, \dots$, com primeiro termo $a_1 = 22$ e razão $r = 5$ (cada dia acrescenta 5 litros).

**Passo 2 — Associar a PA a uma função afim de domínio discreto.** O termo geral da PA é $a_n = a_1 + (n-1)r = 22 + (n-1)\cdot 5 = 5n + 17$. Como o índice $n$ representa o número do dia (variável discreta, $n \in \mathbb{N}$, $n \geq 1$), essa sequência corresponde à função afim $f(n) = 5n + 17$, restrita aos naturais, que descreve o volume ao final do dia $n$.

**Passo 3 — Verificar a coerência com os dados.** $f(1) = 5(1)+17 = 22$; $f(2) = 27$; $f(3) = 32$. Os valores conferem com os registros fornecidos.

**Passo 4 — Resolver a equação.** Queremos $n$ tal que $f(n) = 152$:
$$5n + 17 = 152 \implies 5n = 135 \implies n = 27.$$

**Passo 5 — Conclusão.** Como $n = 27$ é um número natural, o reservatório atingirá 152 litros ao final do **27º dia**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*n + 17`, parâmetros `{'pontos': '[(1,22),(2,27),(3,32)]', 'grau': '1', 'sequencia': 'pa', 'a1': '22', 'razao': '5'}`
- `equacao` — expressão `Eq(5*n + 17, 152)`, esperado `[27]`
- `funcao` — expressão `5*n + 17`, esperado `147`, parâmetros `{'consulta': 'valor', 'ponto': '26'}`
- `funcao` — expressão `5*n + 17`, esperado `152`, parâmetros `{'consulta': 'valor', 'ponto': '27'}`
- `funcao` — expressão `5*n + 17`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*n + 14: grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (f(25) = 114). | (4) aprovado: Gabarito confirmado (termo da PA = 114).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - progressao/termo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta dados completos (primeiro termo, razão, domínio) e pede claramente a lei de f(n) e o valor em n=25. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — O processo cognitivo real exigido é 'aplicar' (montar a fórmula do termo geral e substituir n=25), não 'analisar'. Não há exigência de decompor relações, comparar a função afim contínua com sua restrição discreta, justificar por que a PA é uma amostragem de f, ou avaliar propriedades. Na taxonomia SOLO, a resposta esperada é multiestrutural (aplicar duas etapas de cálculo), incompatível com o nível 'analisar' declarado, que exigiria resposta relacional ou estendida abstrata.
  - alinhamento_bncc: 3/5 — A questão menciona a associação PA-função afim ao pedir a 'lei de formação' de f(n), mas o enunciado não exige explicitamente que o estudante trate do domínio discreto ou justifique a relação estrutural entre PA e função afim — isso aparece só na resolução, não é demandado pelo enunciado. Falta uma exigência que force o raciocínio sobre por que a sequência é uma restrição de uma função afim (ex.: comparar com valores não naturais, ou identificar o que mudaria se o domínio fosse real).
  - distratores: 4/5 — Os três distratores representam erros conceituais plausíveis e comuns (deslocamento de índice, inversão dos coeficientes, confusão entre termo geral e soma dos termos). Nenhum é absurdo ou trivialmente eliminável por inspeção rápida, embora o terceiro (soma dos termos) produza um valor claramente distante dos demais, o que pode facilitar sua eliminação por estimativa.
  - originalidade: 4/5 — O contexto de auditório com fileiras crescentes é razoavelmente aplicado e evita a repetição literal do clássico problema de 'postes e fios', mas ainda segue o padrão-modelo de PA em contexto de fileiras/assentos, comum em livros didáticos. O enunciado já indica diretamente que se deve usar uma função, reduzindo parte do desafio de identificação (leve efeito Topaze).
  - *sugestões:* Reformule o enunciado para exigir efetivamente um processo de análise, não apenas aplicação de fórmula. Sugestões concretas: (1) Peça explicitamente que o estudante explique por que a sequência de assentos pode ser vista como uma função afim de domínio discreto, e o que mudaria (ou não faria sentido) se n assumisse valores não naturais (ex.: n=2,5); (2) Acrescente uma segunda exigência que force comparação/relacionamento, como perguntar em que fileira haveria exatamente 150 assentos e verificar se esse valor é compatível com o domínio (n natural), evidenciando a diferença entre a função afim contínua e sua restrição discreta; (3) Evite que o enunciado já diga 'representar por meio de uma função' de forma tão direta — peça primeiro que o estudante reconheça o padrão (PA) e só depois questione a relação com a função afim, deixando a associação como parte do raciocínio a ser construído, não apenas executado. Essas mudanças elevam o nível cognitivo para 'analisar' de fato e fortalecem o alinhamento com a habilidade EM13MAT507, que exige articulação e não apenas aplicação da fórmula do termo geral.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reformule o enunciado para exigir efetivamente um processo de análise, não apenas aplicação de fórmula. Sugestões concretas: (1) Peça explicitamente que o estudante explique por que a sequência de assentos pode ser vista como uma função afim de domínio discreto, e o que mudaria (ou não faria sentido) se n assumisse valores não naturais (ex.: n=2,5); (2) Acrescente uma segunda exigência que force comparação/relacionamento, como perguntar em que fileira haveria exatamente 150 assentos e verificar se esse valor é compatível com o domínio (n natural), evidenciando a diferença entre a função afim contínua e sua restrição discreta; (3) Evite que o enunciado já diga 'representar por meio de uma função' de forma tão direta — peça primeiro que o estudante reconheça o padrão (PA) e só depois questione a relação com a função afim, deixando a associação como parte do raciocínio a ser construído, não apenas executado. Essas mudanças elevam o nível cognitivo para 'analisar' de fato e fortalecem o alinhamento com a habilidade EM13MAT507, que exige articulação e não apenas aplicação da fórmula do termo geral.

### Iteração 2

- **Verificador:** rejeitado — 1 de 5 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 5*n + 17: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) rejeitado: Divergência no conjunto-solução — soluções do gabarito não confirmadas: [133/5]. | (3) aprovado: Gabarito confirmado (f(26) = 147). | (4) aprovado: Gabarito confirmado (f(27) = 152). | (5) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals).
  - propriedade=aprovado
  - equacao=rejeitado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 5 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 5*n + 17: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) rejeitado: Divergência no conjunto-solução — soluções do gabarito não confirmadas: [133/5]. | (3) aprovado: Gabarito confirmado (f(26) = 147). | (4) aprovado: Gabarito confirmado (f(27) = 152). | (5) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). Resultado calculado independentemente: 5*n + 17 | [] | f(26) = 147 | f(27) = 152 | domínio Naturals — restrição de contexto dentro do domínio máximo Reals. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*n + 17: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Gabarito confirmado (f(26) = 147). | (4) aprovado: Gabarito confirmado (f(27) = 152). | (5) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals).
  - propriedade=aprovado
  - equacao=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente o contexto, os dados (três registros diários), a condição (crescimento constante) e o que é pedido (dia em que o volume atinge 152 L). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — A especificação declara Bloom 'analisar', mas a resolução mostrada é puramente procedural: reconhecer a PA, escrever o termo geral, associá-lo à função afim e resolver uma equação linear — isso corresponde a 'aplicar' (SOLO multiestrutural), não a 'analisar'. Não há exigência de comparar, decompor, justificar escolhas entre representações ou identificar relações não explícitas. O nível cognitivo efetivamente demandado é inferior ao declarado.
  - alinhamento_bncc: 3/5 — O enunciado exige explicitamente associar a sequência de medições a uma função afim de domínio discreto, o que atende ao requisito de articulação entre PA e função afim (não apenas aplicar a fórmula do termo geral isoladamente). Porém, a habilidade EM13MAT507 também prevê 'análise de propriedades', o que a questão não contempla — ela se limita a montar e resolver uma equação, sem investigar propriedades da relação PA/função afim (ex.: taxa de variação como razão, comparação de representações, generalização).
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e bem descritos (erro de indexação n=0 vs n=1, esquecimento do termo constante, inversão de sinal com arredondamento incorreto). Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 4/5 — O contexto de reservatório de irrigação é razoavelmente aplicado e evita o clichê mais batido de livros didáticos (idades, salários), embora a estrutura de resolução (PA com termos dados, achar n para valor final) seja um padrão bastante recorrente em questões de PA/função afim.
  - *sugestões:* Ajustar a questão para que o processo cognitivo exigido corresponda de fato ao nível 'analisar': por exemplo, apresentar duas sequências de enchimento com taxas diferentes (ou um reservatório com vazamento simultâneo) e pedir que o estudante compare as funções afins associadas, identifique em que dia os volumes se igualam, ou justifique por que a relação é ou não uma função afim válida para domínio discreto justificando a escolha da representação (tabela, fórmula, gráfico). Alternativamente, se o formato atual for mantido, reclassificar o nível de Bloom da especificação para 'aplicar', e reforçar o alinhamento à habilidade exigindo explicitamente a comparação/dedução de propriedades da associação PA→função afim, não apenas a resolução de uma equação linear.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a questão para que o processo cognitivo exigido corresponda de fato ao nível 'analisar': por exemplo, apresentar duas sequências de enchimento com taxas diferentes (ou um reservatório com vazamento simultâneo) e pedir que o estudante compare as funções afins associadas, identifique em que dia os volumes se igualam, ou justifique por que a relação é ou não uma função afim válida para domínio discreto justificando a escolha da representação (tabela, fórmula, gráfico). Alternativamente, se o formato atual for mantido, reclassificar o nível de Bloom da especificação para 'aplicar', e reforçar o alinhamento à habilidade exigindo explicitamente a comparação/dedução de propriedades da associação PA→função afim, não apenas a resolução de uma equação linear.
