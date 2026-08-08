# Ciclo 058 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma agência de viagens vende pacotes turísticos a um preço unitário de $x$ reais. Um estudo de mercado mostrou que a quantidade de pacotes vendidos por mês, em função do preço, é dada por $q(x) = 1000 - 4x$ (em unidades). Por cláusula do contrato firmado com a operadora parceira, o preço do pacote deve obrigatoriamente estar entre R$\,200,00$ e R$\,300,00$, incluindo os extremos. Considerando a receita mensal $R(x) = x \cdot q(x)$, determine o preço que maximiza a receita da agência dentro dessa faixa contratual e o valor dessa receita máxima.

## Alternativas

- (a) R$125,00, com receita máxima de R$62.500,00
  - *erro representado:* Calcular apenas o vértice da parábola pela fórmula $x_v = -b/(2a)$ e ignorar a restrição de domínio imposta pelo contrato (o vértice não pertence ao intervalo permitido).
- (b) R$200,00, com receita máxima de R$40.000,00  ← correta
- (c) R$300,00, com receita máxima de R$-60.000,00
  - *erro representado:* Escolher arbitrariamente o extremo superior do intervalo como candidato ao máximo, sem analisar se a função é crescente ou decrescente nesse trecho (nem comparar com o outro extremo).
- (d) R$250,00, com receita máxima de R$0,00
  - *erro representado:* Supor que o máximo de uma função restrita a um intervalo ocorre automaticamente no ponto médio desse intervalo, sem usar as propriedades da parábola (posição do vértice e monotonicidade).

## Gabarito

Preço de R$200,00, com receita máxima de R$40.000,00 (alternativa B)

## Resolução

**Passo 1 — Modelar a receita.**

A receita mensal é $R(x) = x \cdot q(x) = x(1000 - 4x) = 1000x - 4x^2$.

Essa é uma função quadrática com $a = -4$, $b = 1000$, portanto a parábola tem concavidade voltada para baixo.

**Passo 2 — Encontrar o vértice da parábola (sem restrição).**

$$x_v = -\dfrac{b}{2a} = -\dfrac{1000}{2(-4)} = 125$$

$$R(125) = 1000(125) - 4(125)^2 = 125000 - 62500 = 62500$$

Sem restrições, a receita máxima ocorreria em $x = 125$, com $R = 62500$.

**Passo 3 — Verificar a restrição contratual.**

O preço deve pertencer ao intervalo $[200, 300]$. Como $x_v = 125 < 200$, o vértice **não pertence** a esse intervalo — logo o máximo da função **no domínio permitido** não é o vértice.

**Passo 4 — Analisar o comportamento da função no intervalo.**

Como $a = -4 < 0$, a função $R(x)$ é crescente para $x < 125$ e decrescente para $x > 125$. Todo o intervalo $[200, 300]$ está à direita do vértice, portanto $R(x)$ é **decrescente** em todo esse intervalo.

**Passo 5 — Concluir onde ocorre o máximo restrito.**

Se a função é decrescente em $[200, 300]$, o maior valor de $R(x)$ nesse intervalo ocorre no **extremo esquerdo**, isto é, em $x = 200$.

**Passo 6 — Calcular a receita máxima.**

$$R(200) = 1000(200) - 4(200)^2 = 200000 - 160000 = 40000$$

Para confirmar que realmente é o maior valor, comparamos com o outro extremo:

$$R(300) = 1000(300) - 4(300)^2 = 300000 - 360000 = -60000$$

Como $R(200) = 40000 > R(300) = -60000$, confirma-se que o máximo no intervalo ocorre em $x = 200$.

**Resposta:** o preço que maximiza a receita, respeitando a cláusula contratual, é **R$\,200,00$**, gerando uma receita máxima de **R$\,40.000,00$**.

## Formalização verificável

- `funcao` — expressão `1000*x - 4*x**2`, esperado `[125, 62500]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `1000*x - 4*x**2`, esperado `40000`, parâmetros `{'consulta': 'maximo', 'dominio': 'Interval(200, 300)'}`
- `funcao` — expressão `1000*x - 4*x**2`, esperado `decrescente`, parâmetros `{'consulta': 'crescimento', 'dominio': 'Interval(200, 300)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 2 de 3 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (vértice calculado (125, 62500)). | (2) aprovado: Gabarito confirmado (maximo de -4*x**2 + 1000*x em Interval(200, 300): 40000). | (3) nao_verificavel: Verificação inconclusiva: não foi possível decidir a monotonicidade de -4*x**2 + 1000*x em Reals. Conferir manualmente.
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
  - funcao/crescimento=nao_verificavel
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado define claramente a função de demanda, a fórmula da receita, a restrição contratual de preço e o que deve ser determinado (preço ótimo e receita máxima). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver o problema sem suposições adicionais.
  - adequacao_nivel: 4/5 — O processo cognitivo real exigido (calcular o vértice, verificar se pertence ao intervalo, analisar a monotonicidade da parábola no domínio restrito e comparar extremos) é mais próximo de 'analisar' do que de simples 'aplicar' uma fórmula. Isso não é um defeito grave — está de acordo com o espírito investigativo da habilidade — mas extrapola levemente o nível de Bloom declarado ('aplicar'), sendo estruturalmente relacional (SOLO) e não apenas procedimental.
  - alinhamento_bncc: 5/5 — A questão atende integralmente à EM13MAT503: exige investigação genuína do ponto de máximo em contexto de Matemática Financeira, não apenas aplicação mecânica da fórmula do vértice. A restrição de domínio obriga o aluno a raciocinar sobre a posição do vértice em relação ao intervalo permitido e sobre o comportamento da função nas bordas — exatamente o tipo de investigação que a habilidade pretende avaliar.
  - distratores: 3/5 — As alternativas 'a' e 'd' representam erros sistemáticos plausíveis (ignorar a restrição; supor que o máximo ocorre no ponto médio do intervalo). Contudo, a alternativa 'c' (R$300,00 com receita de -R$60.000,00) é fragilizada pelo valor de receita negativo, que soa contextualmente absurdo para um problema de vendas reais e pode ser eliminado por bom senso, sem necessidade de cálculo — reduzindo seu poder diagnóstico como distrator.
  - originalidade: 4/5 — O contexto de maximização de receita via preço x demanda é um clássico recorrente em livros didáticos, mas a inclusão da cláusula contratual que desloca o intervalo de análise para fora do vértice é um elemento não trivial que evita o efeito Topaze e obriga a uma investigação real, distinguindo a questão do problema-padrão de 'ache o vértice da parábola'.
