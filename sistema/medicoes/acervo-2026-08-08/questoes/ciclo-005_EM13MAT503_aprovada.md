# Ciclo 005 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma empresa de aplicativo de transporte por assinatura mensal cobra atualmente R$ 40,00 por mês e possui 800 assinantes ativos. Uma pesquisa de mercado mostra que, para cada R$ 2,00 de aumento no valor da mensalidade, a empresa perde 20 assinantes; e, para cada R$ 2,00 de redução, ganha 20 assinantes a mais, respeitando o limite de capacidade da plataforma, que é de 1000 assinantes simultâneos. Além da receita das assinaturas, a empresa tem um custo fixo mensal de R$ 5.000,00 para manter os servidores, independentemente do valor cobrado ou do número de assinantes.

a) Determine o valor da mensalidade que maximiza o lucro mensal da empresa e calcule esse lucro máximo.

b) Sem refazer os cálculos, explique — a partir do sinal do coeficiente da função quadrática que descreve o lucro em função do preço — por que o ponto encontrado é necessariamente de máximo, e não de mínimo.

c) Os investidores exigem que o lucro mensal seja de, no mínimo, R$ 30.000,00. Determine para quais valores da mensalidade essa exigência é atendida.

## Gabarito

a) Mensalidade de R$ 60,00, com lucro máximo de R$ 31.000,00. b) Como o coeficiente $a=-10$ da função quadrática do lucro é negativo, a parábola tem concavidade para baixo, e por isso o vértice corresponde a um ponto de máximo (o maior valor que a função assume), e não de mínimo. c) O lucro é de pelo menos R$ 30.000,00 para mensalidades entre R$ 50,00 e R$ 70,00 (inclusive).

## Resolução

**Modelando a quantidade de assinantes em função do preço**

Seja $p$ o valor da mensalidade (em reais). Cada aumento de $2$ reais reduz em $20$ o número de assinantes, ou seja, a variação é de $-10$ assinantes por real de aumento. Partindo de $800$ assinantes quando $p = 40$:

$$N(p) = 800 - 10(p-40) = 1200 - 10p$$

Verificação: $N(40) = 800$ (correto) e $N(60) = 600$, que é menor que a capacidade máxima de $1000$ assinantes — logo essa restrição não impede o resultado obtido adiante.

**Receita e lucro**

A receita mensal é $R(p) = p \cdot N(p) = p(1200-10p) = -10p^2 + 1200p$.

Descontando o custo fixo de $R\$ 5.000{,}00$, o lucro mensal é:

$$L(p) = -10p^2 + 1200p - 5000$$

**a) Máximo do lucro**

Como $a = -10 < 0$, o gráfico de $L(p)$ é uma parábola com concavidade para baixo, e seu vértice é um ponto de máximo. A abscissa do vértice é:

$$p_v = -\dfrac{b}{2a} = -\dfrac{1200}{2(-10)} = 60$$

O lucro máximo é:

$$L(60) = -10(60)^2 + 1200(60) - 5000 = -36000 + 72000 - 5000 = 31000$$

Portanto, a mensalidade que maximiza o lucro é **R$ 60,00**, gerando um lucro mensal máximo de **R$ 31.000,00**.

**b) Justificativa do máximo**

Em uma função quadrática $L(p) = ap^2+bp+c$, o vértice é ponto de mínimo quando $a>0$ (parábola com concavidade para cima) e ponto de máximo quando $a<0$ (parábola com concavidade para baixo). Aqui $a=-10<0$, então os valores de $L(p)$ crescem à esquerda do vértice e decrescem à direita dele — ou seja, o vértice $(60, 31000)$ é o ponto mais alto do gráfico, confirmando que se trata de um máximo, não de um mínimo.

**c) Intervalo de preços com lucro de pelo menos R$ 30.000,00**

Queremos resolver $L(p) \geq 30000$:

$$-10p^2+1200p-5000 \geq 30000$$
$$-10p^2+1200p-35000 \geq 0$$

Dividindo por $-10$ (invertendo a desigualdade):

$$p^2 - 120p + 3500 \leq 0$$

Resolvendo a equação $p^2-120p+3500=0$ pela fórmula de Bhaskara:

$$\Delta = (-120)^2 - 4(1)(3500) = 14400 - 14000 = 400$$
$$p = \dfrac{120 \pm \sqrt{400}}{2} = \dfrac{120 \pm 20}{2}$$
$$p = 50 \quad \text{ou} \quad p = 70$$

Como o coeficiente de $p^2$ nessa desigualdade é positivo, a expressão é negativa (ou nula) **entre** as raízes. Logo:

$$50 \leq p \leq 70$$

A exigência dos investidores é atendida para mensalidades entre **R$ 50,00 e R$ 70,00**, incluindo os extremos.

## Formalização verificável

- `funcao` — expressão `-10*p**2 + 1200*p - 5000`, esperado `[60, 31000]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-10*p**2 + 1200*p - 5000`, esperado `31000`, parâmetros `{'consulta': 'maximo'}`
- `equacao` — expressão `Eq(-10*p**2 + 1200*p - 5000, 30000)`, esperado `[50, 70]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (45, 20250)). | (2) aprovado: Gabarito confirmado (extremo calculado 20250).
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (preço inicial, quantidade vendida, taxa de variação) e os três subitens pedidos (a, b, c) são inequívocos quanto ao que deve ser produzido como resposta.
  - adequacao_nivel: 2/5 — O nível de Bloom declarado é 'analisar', mas a tarefa exige apenas construir a função (substituição direta) e aplicar a fórmula do vértice — isso é 'aplicar', não 'analisar'. Não há decomposição de relações concorrentes, comparação de cenários, justificativa do porquê o vértice é máximo, nem interpretação crítica dos resultados (ex.: restrições de domínio, sensibilidade do modelo). A estrutura SOLO da resposta esperada é multiestrutural (montar fórmula → aplicar fórmula → calcular valor), não relacional/estendida abstrata como exigiria uma questão de análise genuína.
  - alinhamento_bncc: 3/5 — O contexto (matemática financeira, maximização de receita) e o conteúdo (função quadrática, ponto de máximo) estão corretos e a questão de fato pede o ponto de máximo, cumprindo o núcleo temático da habilidade. Porém, o verbo-chave da habilidade é 'investigar', que pressupõe alguma exploração ou justificativa do comportamento da função (por que existe máximo, o que ocorre fora do vértice, limites do modelo), e a questão se limita a um procedimento mecânico de montagem e aplicação de fórmula, sem exigir investigação.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — É um dos problemas mais clássicos e recorrentes de livros didáticos sobre função quadrática ('aumento de preço reduz vendas'), sem qualquer elemento de contexto significativo, dado inesperado ou obstáculo que exija reflexão adicional. O enunciado já entrega o caminho de resolução passo a passo (efeito Topaze), citando explicitamente 'preço vezes quantidade vendida' e a relação linear de queda, deixando pouco espaço para o aluno formular sozinho o modelo.
  - *sugestões:* 1) Para elevar o nível cognitivo a 'analisar': acrescente uma pergunta que exija comparação ou justificativa, por exemplo pedir para o aluno explicar por que o vértice representa máximo (e não mínimo) analisando o sinal do coeficiente 'a', ou pedir que compare a receita em dois preços diferentes e justifique qual estratégia é mais vantajosa, ou investigar o intervalo de preços em que a receita permanece acima de um valor mínimo estabelecido (isso exigiria resolver uma inequação quadrática, elevando a estrutura da resposta a relacional). 2) Para reduzir o 'efeito Topaze': não explicite a fórmula 'preço vezes quantidade' nem sugira diretamente a variável x de acréscimo; deixe o aluno decidir como modelar a relação entre preço e quantidade. 3) Para aumentar originalidade: mude o contexto para algo menos manual (ex.: precificação dinâmica de aplicativo de transporte, aluguel de equipamentos, plano de assinatura) e insira um dado extra não essencial ou uma restrição realista (ex.: capacidade máxima do local, custo fixo a subtrair da receita para pedir o lucro em vez da receita bruta), tornando o problema menos reconhecível como exercício-padrão de livro didático.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Para elevar o nível cognitivo a 'analisar': acrescente uma pergunta que exija comparação ou justificativa, por exemplo pedir para o aluno explicar por que o vértice representa máximo (e não mínimo) analisando o sinal do coeficiente 'a', ou pedir que compare a receita em dois preços diferentes e justifique qual estratégia é mais vantajosa, ou investigar o intervalo de preços em que a receita permanece acima de um valor mínimo estabelecido (isso exigiria resolver uma inequação quadrática, elevando a estrutura da resposta a relacional). 2) Para reduzir o 'efeito Topaze': não explicite a fórmula 'preço vezes quantidade' nem sugira diretamente a variável x de acréscimo; deixe o aluno decidir como modelar a relação entre preço e quantidade. 3) Para aumentar originalidade: mude o contexto para algo menos manual (ex.: precificação dinâmica de aplicativo de transporte, aluguel de equipamentos, plano de assinatura) e insira um dado extra não essencial ou uma restrição realista (ex.: capacidade máxima do local, custo fixo a subtrair da receita para pedir o lucro em vez da receita bruta), tornando o problema menos reconhecível como exercício-padrão de livro didático.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (60, 31000)). | (2) aprovado: Gabarito confirmado (extremo calculado 31000). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado é bem estruturado, com dados suficientes e pedidos claros nos três itens. O único ponto que exige atenção é a informação sobre o limite de 1000 assinantes: ela não é usada no cálculo final, e o enunciado não deixa explícito que o aluno deve verificar se essa restrição é ou não ativa no ponto de máximo, podendo gerar hesitação sobre seu papel — embora isso seja aceitável em uma questão de investigação, uma pequena reformulação ('verifique se essa restrição interfere no resultado') tornaria a exigência mais explícita.
  - adequacao_nivel: 4/5 — O item (b) exige efetivamente um processo de análise conceitual (justificar o tipo de ponto crítico a partir do sinal do coeficiente, sem recalcular), compatível com o nível 'analisar' e com resposta de estrutura relacional (SOLO). Já os itens (a) e (c) são majoritariamente de aplicação (montar função, achar vértice, resolver inequação), o que é esperado em questões 'fácil' de matemática financeira, mas reduz um pouco a predominância do nível cognitivo declarado no conjunto da questão.
  - alinhamento_bncc: 5/5 — A questão atende integralmente à habilidade EM13MAT503: investiga um ponto de máximo de função quadrática (lucro) em contexto de matemática financeira, exige a determinação desse ponto (item a), a justificativa conceitual do tipo de extremo via sinal do coeficiente (item b) e uma extensão investigativa via inequação quadrática associada ao mesmo modelo (item c). Os itens articulam-se em torno de uma única função, sem justaposição artificial de subtemas.
  - distratores: 5/5 — não se aplica (questão discursiva)
  - originalidade: 3/5 — O contexto de aplicativo de assinatura é atual e o dado do limite de capacidade evita uma resolução puramente mecânica, funcionando como um contraponto ao efeito Topaze. Entretanto, a estrutura matemática subjacente (preço x quantidade vendida com variação linear, otimização de receita menos custo fixo) é um modelo clássico e recorrente em livros didáticos, apenas revestido de nova ambientação.
