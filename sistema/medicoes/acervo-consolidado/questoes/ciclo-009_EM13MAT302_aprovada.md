# Ciclo 009 — EM13MAT302

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Uma locadora de bicicletas cobra pelo aluguel um valor que combina uma taxa fixa de retirada com um valor proporcional ao número de horas de uso. Um cliente que utilizou a bicicleta por 2 horas pagou R$ 18,00, enquanto outro cliente, que a utilizou por 5 horas, pagou R$ 33,00.

Buscando atrair clientes que alugam por períodos mais longos, a locadora lançou um novo plano de cobrança, mantendo a mesma taxa fixa de retirada, mas alterando o valor cobrado por hora de uso. Nesse novo plano, um cliente que utiliza a bicicleta por 8 horas paga R$ 10,00 a menos do que pagaria, nesse mesmo período de uso, pelo plano antigo.

Determine a lei que descreve o custo do novo plano em função do tempo de uso $t$ (em horas) e avalie para quais valores de $t$ esse novo plano é financeiramente mais vantajoso do que o plano antigo.

## Alternativas

- (a) D(t) = 3,75t + 8; o novo plano é mais vantajoso, com custo estritamente menor que o antigo, para todo tempo de uso t > 0 (os dois planos coincidem apenas em t = 0).  ← correta
- (b) D(t) = 5t - 2; o novo plano é mais vantajoso para todo t > 0.
  - *erro representado:* O estudante inverte qual parcela permanece constante: mantém o coeficiente da parte proporcional igual ao do plano antigo (a=5) e trata erroneamente a taxa fixa como a grandeza que muda, resolvendo 8(5)+b'=38 para obter b'=-2.
- (c) D(t) = 4,75t + 8; o novo plano é mais vantajoso para todo t > 0.
  - *erro representado:* Erro algébrico ao isolar o coeficiente: o estudante resolve 8a'+8=38 esquecendo de subtrair 8 dos dois lados, calculando 8a'=38 diretamente e obtendo a'=4,75.
- (d) D(t) = 3,75t + 8; porém o novo plano só se torna mais vantajoso para t > 8 horas.
  - *erro representado:* O estudante calcula corretamente D(t), mas inverte o sentido da comparação, supondo que a vantagem do novo plano só passa a valer a partir do tempo de 8 horas mencionado no enunciado, em vez de perceber que ela vale para todo t>0.

## Gabarito

D(t) = 3,75t + 8; o novo plano é mais vantajoso (custo estritamente menor) para todo t > 0, sendo os planos equivalentes apenas em t = 0.

## Resolução

**Passo 1 — Modelar o plano antigo.**
Como o custo combina uma parte fixa com uma parte proporcional ao tempo, o modelo é afim: $C(t) = a\,t + b$.

Dos dados: $C(2)=18$ e $C(5)=33$:
$2a+b=18$
$5a+b=33$

Subtraindo: $3a=15 \Rightarrow a=5$. Substituindo: $b = 18-2(5)=8$.

Logo, $C(t) = 5t+8$.

**Passo 2 — Modelar o plano novo.**
O novo plano mantém a mesma taxa fixa, então $D(t) = a't + 8$, com $a'$ a determinar.

O custo do plano antigo em $t=8$ é:
$C(8) = 5(8)+8 = 48$

O novo plano cobra R$ 10,00 a menos nesse tempo:
$D(8) = 48-10 = 38$

Como $D(8) = 8a'+8$:
$8a'+8 = 38 \Rightarrow 8a' = 30 \Rightarrow a' = 3{,}75$

Portanto, $D(t) = 3{,}75t + 8$.

**Passo 3 — Comparar os dois planos.**
Calcule a diferença:
$C(t)-D(t) = (5t+8)-(3{,}75t+8) = 1{,}25t$

Como $t \geq 0$ (tempo de uso não pode ser negativo), temos $1{,}25t \geq 0$, com igualdade apenas em $t=0$.

Logo, $C(t) \geq D(t)$ para todo $t\geq 0$, sendo $D(t) < C(t)$ estritamente para $t>0$.

**Conclusão:** $D(t) = 3{,}75t+8$, e o novo plano é sempre financeiramente mais vantajoso (ou igual) ao antigo, tornando-se estritamente mais vantajoso para qualquer tempo de uso $t>0$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*t + 8`, parâmetros `{'pontos': '[(2,18),(5,33)]', 'grau': '1'}`
- `propriedade` — expressão `-`, esperado `Rational(15,4)*t + 8`, parâmetros `{'pontos': '[(0,8),(8,38)]', 'grau': '1'}`
- `funcao` — expressão `Rational(5,4)*t`, esperado `[0]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `Rational(5,4)*t`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*x + 6: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(8) = 38).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: define claramente o contexto, os dados (dois pares tempo/valor) e a pergunta final. Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver o problema.
  - adequacao_nivel: 2/5 — A tarefa exigida é montar um sistema linear com dois pontos e resolver para os coeficientes, depois aplicar a fórmula — isso corresponde ao nível 'aplicar' (SOLO relacional), não a 'criar'. Não há elaboração de um problema novo, geração de múltiplas soluções, síntese ou avaliação crítica de modelos alternativos, que caracterizariam o nível 'criar'. A estrutura de resposta esperada (resolver sistema + substituir) é a mesma de um exercício padrão de 'aplicar função afim', incompatível com o nível cognitivo declarado.
  - alinhamento_bncc: 3/5 — A questão emprega corretamente um modelo de função afim a partir de dados contextuais, sem entregá-lo pronto, o que atende parcialmente à habilidade EM13MAT302. Contudo, essa habilidade também prevê 'elaborar problemas' — algo ausente aqui — e o processo cognitivo real (aplicar) não corresponde ao nível 'criar' declarado na especificação, o que compromete o alinhamento entre o que é pedido e o que a especificação exige.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e bem diferenciados: ignorar o valor fixo, esquecer de somá-lo após achar 'a', e trocar os coeficientes do sistema. Nenhum é trivialmente eliminável ou absurdo.
  - originalidade: 3/5 — O contexto de locadora de bicicletas é minimamente diferente do clássico 'conta de telefone/táxi', mas a estrutura do problema (dois pontos, sistema 2x2, função afim) é altamente convencional e replica o modelo padrão de livros didáticos, sem elementos que exijam reflexão sobre a escolha do modelo ou generalização.
  - *sugestões:* Ajustar a questão para que o processo cognitivo exigido corresponda de fato ao nível 'criar', ou então rebaixar o nível Bloom declarado para 'aplicar', que é o que a tarefa atual realmente demanda. Para elevar ao nível 'criar', pode-se: (1) pedir que o aluno elabore seu próprio problema contextualizado que gere o mesmo modelo C(t)=4t+6, explicitando as condições que escolheria; (2) pedir que compare e justifique por que um modelo afim é mais adequado que um modelo quadrático ou proporcional direto para esse contexto, produzindo uma justificativa original; ou (3) solicitar que o aluno proponha uma nova tarifa (outro par de valores) que resulte em um custo por hora diferente, mas mantendo o mesmo valor fixo, e explique o raciocíno de construção do sistema. Além disso, para reforçar a articulação com a habilidade, incluir explicitamente uma etapa de 'elaboração' (não apenas resolução) do problema, conforme pede a EM13MAT302.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a questão para que o processo cognitivo exigido corresponda de fato ao nível 'criar', ou então rebaixar o nível Bloom declarado para 'aplicar', que é o que a tarefa atual realmente demanda. Para elevar ao nível 'criar', pode-se: (1) pedir que o aluno elabore seu próprio problema contextualizado que gere o mesmo modelo C(t)=4t+6, explicitando as condições que escolheria; (2) pedir que compare e justifique por que um modelo afim é mais adequado que um modelo quadrático ou proporcional direto para esse contexto, produzindo uma justificativa original; ou (3) solicitar que o aluno proponha uma nova tarifa (outro par de valores) que resulte em um custo por hora diferente, mas mantendo o mesmo valor fixo, e explique o raciocíno de construção do sistema. Além disso, para reforçar a articulação com a habilidade, incluir explicitamente uma etapa de 'elaboração' (não apenas resolução) do problema, conforme pede a EM13MAT302.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*x + 6: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Propriedades confirmadas para 11*x/4 + 6: reproduz os 2 pontos dados; grau 1.
  - propriedade=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta dados numéricos completos (dois pares tempo-custo do plano atual, a condição de manutenção da taxa fixa e a diferença de R$10,00 em 8h) e a pergunta é única e inequívoca. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 2/5 — Embora a tarefa final seja 'elaborar a lei de D(t)', o processo efetivamente exigido é apenas resolver um sistema linear (Passo 1) e depois substituir valores em uma equação já com a forma dada (Passos 3-5). Isso corresponde a Bloom 'aplicar', não a 'criar': não há geração de múltiplas hipóteses, escolha de estratégia entre alternativas, nem produção de um modelo original a partir de dados brutos sem forma prescrita. Em termos SOLO, a resposta é relacional (combina duas informações dadas), não estendida/abstrata como se esperaria de um nível 'criar'.
  - alinhamento_bncc: 2/5 — A especificação exige explicitamente que o modelo não seja entregue pronto quando o nível cognitivo for 'aplicar' ou superior. O enunciado, porém, fornece C(t) = a·t + b diretamente, o que remove do aluno a tarefa de identificar/construir a forma do modelo a partir do contexto (taxa fixa + proporcional ao tempo). A questão também não pede genuína 'elaboração' de um problema novo, mas resolução guiada passo a passo de um problema já estruturado — o que não cumpre integralmente a habilidade EM13MAT302 no nível declarado.
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis: esquecer de manter a taxa fixa (divisão direta), erro de sinal na interpretação da condição (soma em vez de subtração) e troca dos coeficientes a e b ao resolver o sistema inicial. Nenhum é absurdo ou trivialmente eliminável, embora o terceiro (troca de a e b) seja um erro um pouco menos comum que os outros dois, reduzindo levemente a qualidade do conjunto.
  - originalidade: 3/5 — O contexto de locadora de bicicletas com dois planos é razoavelmente aplicado e evita o clichê da 'conta de telefone', mas a estrutura de resolução (dar a forma C(t)=at+b e depois pedir para substituir números) é o padrão clássico de exercício de sistema linear travestido de função afim, configurando um efeito Topaze: a forma pronta do modelo pavimenta fortemente o caminho da solução, reduzindo a genuína elaboração esperada em nível 'criar'.
  - *sugestões:* 1) Remova a expressão explícita 'C(t) = a·t + b' do enunciado; descreva apenas verbalmente que o custo tem uma parte fixa e uma parte proporcional ao tempo, exigindo que o aluno identifique e escreva a forma da função afim por conta própria antes de usar os dados numéricos. 2) Para atingir de fato o nível 'criar', peça que o aluno não apenas calcule D(t), mas também justifique/compare o novo modelo com o antigo (por exemplo, discuta em que faixa de tempo o novo plano é mais vantajoso), produzindo uma elaboração original e não apenas a resolução de um sistema com substituição direta. 3) Revise a condição dada (10 reais a menos em 8h) para que exija do aluno decidir como traduzi-la em equação, sem que o enunciado já sugira passo a passo a sequência de substituições — evite frases que antecipem a estratégia de solução. 4) Mantenha os distratores atuais, mas considere substituir o de 'troca de coeficientes' por outro erro mais frequente, como confundir a variável do novo coeficiente com a taxa fixa antiga (ex.: usar b como coeficiente angular).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Remova a expressão explícita 'C(t) = a·t + b' do enunciado; descreva apenas verbalmente que o custo tem uma parte fixa e uma parte proporcional ao tempo, exigindo que o aluno identifique e escreva a forma da função afim por conta própria antes de usar os dados numéricos. 2) Para atingir de fato o nível 'criar', peça que o aluno não apenas calcule D(t), mas também justifique/compare o novo modelo com o antigo (por exemplo, discuta em que faixa de tempo o novo plano é mais vantajoso), produzindo uma elaboração original e não apenas a resolução de um sistema com substituição direta. 3) Revise a condição dada (10 reais a menos em 8h) para que exija do aluno decidir como traduzi-la em equação, sem que o enunciado já sugira passo a passo a sequência de substituições — evite frases que antecipem a estratégia de solução. 4) Mantenha os distratores atuais, mas considere substituir o de 'troca de coeficientes' por outro erro mais frequente, como confundir a variável do novo coeficiente com a taxa fixa antiga (ex.: usar b como coeficiente angular).

### Iteração 3

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*t + 8: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Propriedades confirmadas para 15*t/4 + 8: reproduz os 2 pontos dados; grau 1. | (3) aprovado: Gabarito confirmado (zeros da função: [0]). | (4) aprovado: Gabarito confirmado (crescente em Reals).
  - propriedade=aprovado
  - propriedade=aprovado
  - funcao/zeros=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta de forma explícita os dados (dois pares tempo/valor para o plano antigo, a condição de manutenção da taxa fixa e a diferença de R$10 no novo plano) e a pergunta final é única e bem delimitada. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — A tarefa exige resolver um sistema linear para obter C(t), depois montar uma segunda equação para D(t) a partir de uma condição dada, e por fim comparar as duas funções. Esse processo é mais próximo de 'aplicar' (uso de procedimentos conhecidos de sistemas lineares) e 'analisar' (comparação de funções) do que de 'criar' no sentido pleno de Bloom, que pressupõe produção de um artefato original ou reorganização não guiada de elementos. A estrutura de resposta é relacional (SOLO), mas não atinge o nível de 'extended abstract' esperado de uma tarefa de criação genuína.
  - alinhamento_bncc: 4/5 — A questão cumpre a exigência de não entregar o modelo pronto — o aluno deve construir tanto C(t) quanto D(t) a partir do texto, articulando os dois planos em um único problema (não são itens independentes, já que D(t) depende de C(8)). Isso atende bem à parte 'resolver' de EM13MAT302; a dimensão 'elaborar problemas' da habilidade é menos explorada, pois o aluno resolve um problema já elaborado pelo professor, não formula um problema próprio.
  - distratores: 4/5 — Os quatro distratores representam erros sistemáticos plausíveis: troca de qual parâmetro é mantido fixo (opção 2), erro algébrico ao isolar a incógnita (opção 3) e inversão do sentido da comparação usando o valor de t=8 do enunciado como ponto de corte (opção 4). Nenhum é absurdo ou trivialmente eliminável, embora a opção 2 (com termo constante negativo) possa ser descartada por alunos atentos ao significado físico da taxa fixa, reduzindo levemente sua eficácia.
  - originalidade: 3/5 — O contexto de locação de bicicletas com taxa fixa e valor por hora é uma variação comum de problemas clássicos de tarifação (táxi, estacionamento, etc.), sem grande inovação contextual. Não há pistas do tipo 'efeito Topaze' que entreguem o caminho de resolução, o que é positivo, mas o cenário em si é bastante convencional.
