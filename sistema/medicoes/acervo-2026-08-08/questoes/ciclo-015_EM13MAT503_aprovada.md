# Ciclo 015 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma fábrica de bicicletas vende atualmente cada unidade por R$ 1.200,00, comercializando 300 bicicletas por mês. Uma pesquisa de mercado mostra que, a cada redução de R$ 50,00 no preço de venda, a quantidade vendida aumenta em 40 unidades. O custo de produção é de R$ 325,00 por bicicleta, além de um custo fixo mensal de R$ 12.500,00 (aluguel, energia, salários administrativos etc.), independentemente da quantidade produzida. Determine o preço de venda que a fábrica deve praticar para maximizar seu lucro mensal e calcule o valor desse lucro máximo.

## Gabarito

Preço ótimo: R$ 950,00 por bicicleta; Lucro máximo mensal: R$ 300.000,00 (obtido em x = 5 reduções de R$ 50,00, vendendo 500 unidades).

## Resolução

**Passo 1 — Definir a variável.**

Seja $x$ o número de reduções de R$ 50,00 aplicadas ao preço (com $x \ge 0$). Então:

- Preço unitário: $p(x) = 1200 - 50x$
- Quantidade vendida: $q(x) = 300 + 40x$

**Passo 2 — Montar a função lucro.**

O lucro mensal é a receita menos o custo total (custo variável + custo fixo):

$$L(x) = \big[p(x)-325\big]\cdot q(x) - 12500$$

$$L(x) = (1200-50x-325)(300+40x) - 12500 = (875-50x)(300+40x) - 12500$$

**Passo 3 — Expandir o produto.**

$$(875-50x)(300+40x) = 875\cdot300 + 875\cdot40x - 50x\cdot300 - 50x\cdot40x$$
$$= 262500 + 35000x - 15000x - 2000x^2 = 262500 + 20000x - 2000x^2$$

Subtraindo o custo fixo:

$$L(x) = -2000x^2 + 20000x + 250000$$

**Passo 4 — Identificar o ponto de máximo.**

Como o coeficiente $a = -2000 < 0$, a parábola tem concavidade voltada para baixo, logo possui um **ponto de máximo** no vértice:

$$x_v = -\dfrac{b}{2a} = -\dfrac{20000}{2(-2000)} = 5$$

**Passo 5 — Verificar que o valor é admissível.**

Com $x=5$: preço $= 1200-50(5)=950 > 325$ (ainda cobre o custo variável) e quantidade $=300+40(5)=500>0$. Logo $x=5$ está dentro do domínio realista do problema (para $x$ entre 0 e 17,5 o preço permanece acima do custo).

**Passo 6 — Calcular o lucro máximo.**

$$L(5) = -2000(5)^2 + 20000(5) + 250000 = -50000 + 100000 + 250000 = 300000$$

**Passo 7 — Traduzir para o contexto.**

O preço que maximiza o lucro é

$$p(5) = 1200 - 50(5) = 950$$

Portanto, a fábrica deve vender cada bicicleta por **R$ 950,00**, o que corresponde à venda de 500 unidades mensais, gerando um **lucro máximo de R$ 300.000,00** por mês.

## Formalização verificável

- `funcao` — expressão `-2000*x**2 + 20000*x + 250000`, esperado `300000`, parâmetros `{'consulta': 'maximo'}`
- `funcao` — expressão `1200 - 50*x`, esperado `950`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 2 afirmações reprovadas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) rejeitado: Divergência: extremo calculado 47200; gabarito 47000.
  - equacao=aprovado
  - funcao/maximo=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 2 afirmações reprovadas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) rejeitado: Divergência: extremo calculado 47200; gabarito 47000. Resultado calculado independentemente: [400] | extremo calculado 47200. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (extremo calculado 300000). | (2) aprovado: Gabarito confirmado (f(5) = 950).
  - funcao/maximo=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado completo, com dados numéricos precisos, condições explícitas (custo variável, custo fixo, relação preço-quantidade) e pedido claro (preço ótimo e lucro máximo). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido é de fato 'aplicar': o aluno deve modelar a situação com uma variável, construir a função lucro e usar a fórmula do vértice, o que é compatível com o nível declarado. Na taxonomia SOLO a resposta esperada é relacional, pois exige integrar preço, quantidade e custos numa única função antes de otimizar. Poderia render um nível 5 se houvesse alguma etapa de justificativa sobre por que o vértice representa máximo, mas isso já é feito na resolução, então adequa-se bem ao Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão pede exatamente o ponto de máximo de uma função quadrática em contexto de matemática financeira, articulando receita, custo variável e custo fixo em um único modelo (não são itens justapostos). Cumpre integralmente a habilidade EM13MAT503: há investigação (definir variável, montar a função, validar domínio) e não mera manipulação algébrica pronta.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — O contexto de 'preço x quantidade vendida com desconto' é um clássico recorrente em livros didáticos (variação do problema do hotel/aluguel de apartamentos). Embora a inclusão de custo variável e custo fixo agregue complexidade e leve a articular lucro (não apenas receita), a estrutura geral do problema é bastante convencional e previsível, com poucas pistas de contexto genuinamente novo. Não há efeito Topaze explícito, mas o enunciado segue o roteiro-padrão que facilita a antecipação da estratégia de resolução.
