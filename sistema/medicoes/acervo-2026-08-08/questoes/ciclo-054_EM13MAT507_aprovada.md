# Ciclo 054 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Considere a progressão aritmética $(a_n)$ com $a_1 = 7$ e razão $r = 4$, em que $a_n$ representa o número de cadeiras da $n$-ésima fileira de um auditório, para $n = 1, 2, 3, \dots$

Um estudante deseja representar essa sequência por meio de uma função afim $f(x) = mx + k$, de modo que $f(n) = a_n$ para todo $n$ da sequência.

Determine a lei de $f$, o domínio da função que corresponde a essa situação, e o valor de $a_{15}$ calculado por meio de $f$.

## Alternativas

- (a) $f(x) = 4x + 3$, com domínio $\mathbb{N} = \{1, 2, 3, \dots\}$, e $a_{15} = 63$.  ← correta
- (b) $f(x) = 4x + 7$, com domínio $\mathbb{N} = \{1, 2, 3, \dots\}$, e $a_{15} = 67$.
  - *erro representado:* Usar diretamente $a_1$ como termo independente da função, sem ajustar $k = a_1 - r$, confundindo o valor de $f(1)$ com $f(0)$.
- (c) $f(x) = 4x + 3$, com domínio $\mathbb{R}$, e $a_{15} = 63$.
  - *erro representado:* Tratar a função associada à PA como definida para todos os reais, ignorando que a sequência tem domínio discreto (apenas os índices naturais correspondem a termos da PA).
- (d) $f(x) = 7x + 4$, com domínio $\mathbb{N} = \{1, 2, 3, \dots\}$, e $a_{15} = 109$.
  - *erro representado:* Trocar os papéis de $a_1$ e $r$ na construção da função, usando $a_1$ como coeficiente angular e $r$ como termo independente.

## Gabarito

f(x) = 4x + 3, domínio $\mathbb{N} = \{1,2,3,\dots\}$, e $a_{15} = 63$.

## Resolução

**Passo 1 — Relacionar a PA com uma função afim.**

O termo geral da PA é $a_n = a_1 + (n-1)r = 7 + (n-1)\cdot 4 = 4n + 3$.

Como $a_n$ tem a forma $mn + k$ com $m = r = 4$ e $k = a_1 - r = 3$, a sequência corresponde à função afim
$$f(x) = 4x + 3.$$

De fato, a razão $r$ da PA é exatamente o coeficiente angular $m$ da função afim, e o termo independente $k$ é obtido fazendo $x=0$ (um ponto que não pertence à sequência original, mas que define a reta que a contém).

**Passo 2 — Identificar o domínio correto.**

Embora $f(x) = 4x+3$ possa ser calculada para qualquer número real $x$, a situação descrita — número de cadeiras em fileiras — só faz sentido para $n = 1, 2, 3, \dots$, isto é, para $x$ natural. Portanto, o domínio da função que representa corretamente a PA é $\mathbb{N} = \{1, 2, 3, \dots\}$, e não $\mathbb{R}$: a reta $y = 4x+3$ apenas contém os pontos da sequência, mas nem todo ponto da reta corresponde a um termo da PA.

**Passo 3 — Calcular $a_{15}$.**

$$f(15) = 4(15) + 3 = 60 + 3 = 63.$$

Logo, $a_{15} = 63$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*n + 3`, parâmetros `{'sequencia': 'pa', 'a1': '7', 'razao': '4', 'grau': '1'}`
- `funcao` — expressão `4*x + 3`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `4*x + 3`, esperado `63`, parâmetros `{'consulta': 'valor', 'ponto': '15'}`
- `progressao` — expressão `-`, esperado `63`, parâmetros `{'tipo_progressao': 'pa', 'a1': '7', 'razao': '4', 'n': '15', 'consulta': 'termo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*n + 4: reproduz os 4 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta a PA, define claramente f(n)=a_n, especifica o domínio (N*) e pede exatamente duas coisas: a lei de f e o valor de n para a_n=244. Não há ambiguidade lexical ou estrutural, e os dados são completos e suficientes.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (obter o termo geral e resolver uma equação linear) é compatível com o nível 'aplicar' de Bloom, e a resposta esperada (fórmula + valor numérico) é coerente com uma estrutura multiestrutural típica desse nível. O conteúdo é adequado ao Ensino Médio.
  - alinhamento_bncc: 3/5 — A habilidade EM13MAT507 exige que o ALUNO identifique e associe a PA à função afim; aqui essa associação já vem pronta no enunciado (f(n)=a_n é dado como premissa, e o texto já explica o caráter discreto do gráfico). Assim, a tarefa remanescente é essencialmente encontrar o termo geral e resolver a_n=244 — o mesmo que se pediria numa questão tradicional de PA, sem exigir do estudante o passo de 'identificar/associar'. O enunciado menciona o domínio discreto, mas não exige que o aluno raciocine sobre isso para resolver o problema.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis (deslocamento de índice, troca dos papéis de a1 e r, erro de sinal ao isolar n). O distrator D exige um arredondamento pouco natural (49,6→50) para chegar a um valor 'limpo', o que o torna um pouco menos autêntico como erro espontâneo, mas ainda assim é aceitável.
  - originalidade: 2/5 — O problema é uma variação bastante convencional de exercício de PA/termo geral, sem contexto significativo (situação puramente formal). Além disso, o enunciado já entrega ao aluno a forma da função afim e explica o motivo do gráfico ser discreto, o que constitui efeito Topaze: a principal dificuldade conceitual (perceber que a_n pode ser vista como f(n)=an+b com domínio restrito) é resolvida pelo próprio enunciado, deixando ao estudante apenas a manipulação algébrica final.
  - *sugestões:* 1) Retire a explicação já pronta sobre f(n)=a_n e sobre o gráfico ser discreto: peça ao aluno que ele mesmo reconheça e justifique por que a PA pode ser vista como uma função afim de domínio discreto, e que compare/contraste com uma função afim de domínio real (ex.: peça para esboçar ou descrever a diferença entre os dois gráficos). 2) Insira uma situação-problema minimamente contextualizada (ex.: uma sequência de valores que crescem de forma constante ao longo de etapas discretas, como pagamentos mensais, posições em fileiras, etc.) para dar significado à discretização do domínio. 3) Adicione uma etapa que force a articulação real dos dois temas, por exemplo pedindo para o aluno decidir, a partir de duas leis de função apresentadas (uma contínua, uma discreta), qual representa corretamente a PA e justificar a escolha usando o conceito de domínio. Isso evita que a questão se reduza a 'calcular o termo geral e resolver uma equação', atendendo de fato à habilidade EM13MAT507.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Retire a explicação já pronta sobre f(n)=a_n e sobre o gráfico ser discreto: peça ao aluno que ele mesmo reconheça e justifique por que a PA pode ser vista como uma função afim de domínio discreto, e que compare/contraste com uma função afim de domínio real (ex.: peça para esboçar ou descrever a diferença entre os dois gráficos). 2) Insira uma situação-problema minimamente contextualizada (ex.: uma sequência de valores que crescem de forma constante ao longo de etapas discretas, como pagamentos mensais, posições em fileiras, etc.) para dar significado à discretização do domínio. 3) Adicione uma etapa que force a articulação real dos dois temas, por exemplo pedindo para o aluno decidir, a partir de duas leis de função apresentadas (uma contínua, uma discreta), qual representa corretamente a PA e justificar a escolha usando o conceito de domínio. Isso evita que a questão se reduza a 'calcular o termo geral e resolver uma equação', atendendo de fato à habilidade EM13MAT507.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*n + 9: coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (termo da PA = 27).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - progressao/termo=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O contexto (fileiras de poltronas) é claro e os dados são suficientes. O único ponto de atenção é que o enunciado acumula duas exigências (encontrar a lei correta E julgar a discussão entre os colegas), o que exige leitura cuidadosa, mas não gera ambiguidade real.
  - adequacao_nivel: 2/5 — O nível de Bloom declarado é 'aplicar', mas o que a questão de fato exige é comparar e avaliar duas modelizações concorrentes, justificando por que uma é inadequada — isso corresponde a 'analisar/avaliar' em Bloom e a uma estrutura relacional (SOLO), não a simples aplicação de fórmula. Há um descompasso entre o processo cognitivo declarado e o efetivamente demandado pelo enunciado.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente o que a EM13MAT507 exige: articula a PA (termo geral) com a função afim, tratando explicitamente do domínio discreto versus contínuo em um único problema integrado, não em itens justapostos.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: erro no termo geral (n em vez de n-1), confusão entre domínio discreto e contínuo (o próprio erro do Colega A) e troca de papéis entre a1 e r. Nenhum é absurdo ou trivialmente eliminável pela forma.
  - originalidade: 3/5 — O contexto do auditório e o diálogo entre colegas são razoavelmente originais e evitam o problema clássico de livro didático. Porém, o enunciado já entrega fortes pistas sobre a resposta (menciona explicitamente 'não existem fileiras fracionárias' e compara com 'grandeza que varia continuamente, tipo altura de líquido'), configurando efeito Topaze que reduz a exigência real de raciocínio do aluno.
  - *sugestões:* 1) Ajustar a especificação de nível cognitivo: se a intenção é manter a discussão crítica sobre domínio discreto vs. contínuo (que é rica e alinhada à BNCC), reclassifique o nível de Bloom para 'analisar' ou 'avaliar', pois a tarefa real excede 'aplicar'. 2) Alternativamente, se o nível 'aplicar' deve ser mantido, simplifique o enunciado: peça apenas que o aluno deduza f(n) a partir da PA e explicite o domínio, sem exigir julgamento comparativo entre as posições dos dois colegas. 3) Reduza o efeito Topaze removendo pistas explícitas como 'não existem fileiras fracionárias' e a analogia com o líquido subindo — deixe que o próprio aluno infira a natureza discreta da situação a partir do contexto (fileiras de poltronas), sem entregá-la no enunciado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar a especificação de nível cognitivo: se a intenção é manter a discussão crítica sobre domínio discreto vs. contínuo (que é rica e alinhada à BNCC), reclassifique o nível de Bloom para 'analisar' ou 'avaliar', pois a tarefa real excede 'aplicar'. 2) Alternativamente, se o nível 'aplicar' deve ser mantido, simplifique o enunciado: peça apenas que o aluno deduza f(n) a partir da PA e explicite o domínio, sem exigir julgamento comparativo entre as posições dos dois colegas. 3) Reduza o efeito Topaze removendo pistas explícitas como 'não existem fileiras fracionárias' e a analogia com o líquido subindo — deixe que o próprio aluno infira a natureza discreta da situação a partir do contexto (fileiras de poltronas), sem entregá-la no enunciado.

### Iteração 3

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*n + 3: grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (f(15) = 63). | (4) aprovado: Gabarito confirmado (termo da PA = 63).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - progressao/termo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado especifica claramente os dados (a1, r), a tarefa (determinar f, seu domínio e a15) e as condições. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar o procedimento de conversão PA→função afim e justificar a escolha do domínio discreto, coerente com o nível 'aplicar'. A estrutura de resposta é multiestrutural (lei, domínio, valor), adequada ao formato de múltipla escolha, mas não chega a exigir análise relacional profunda, o que é aceitável para o nível declarado.
  - alinhamento_bncc: 5/5 — A questão atende plenamente à EM13MAT507: exige explicitamente a associação da PA a uma função afim, com tratamento do domínio discreto como parte central da resposta, e não apenas a aplicação isolada da fórmula do termo geral.
  - distratores: 5/5 — Cada alternativa incorreta representa um erro conceitual plausível e comum: confundir f(1) com f(0) (alt. 2), ignorar a discretização do domínio (alt. 3) e trocar os papéis de a1 e r (alt. 4). Nenhuma é absurda ou trivialmente eliminável, pois todas mantêm coerência interna entre fórmula e valor calculado.
  - originalidade: 4/5 — O contexto do auditório é razoavelmente significativo e evita o padrão mecânico de 'calcule o termo geral'. A ênfase explícita na discussão do domínio (N vs R) foge do enunciado clássico de livro didático, embora o contexto em si (fileiras de cadeiras) seja um tema recorrente em PA.
