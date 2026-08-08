# Ciclo 076 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma loja de roupas vende um certo modelo de jaqueta. O custo de aquisição de cada peça, pago ao fornecedor, é de R$ 80,00. Uma pesquisa de mercado mostrou que, se a loja fixar o preço de venda em $p$ reais (com $80 < p < 150$), a quantidade de jaquetas vendidas por mês, em unidades, é dada por $q(p) = 300 - 2p$.

a) Escreva a expressão do lucro mensal $L(p)$ obtido com a venda das jaquetas, em função do preço $p$, sabendo que o lucro é o produto entre o lucro unitário (preço de venda menos custo de aquisição) e a quantidade vendida.

b) Determine o preço $p$ que maximiza o lucro mensal e calcule esse lucro máximo.

c) Confirme que esse preço realmente fornece o maior lucro possível, calculando o lucro para dois preços vizinhos — R\$ 114,00 e R\$ 116,00 — e comparando os resultados com o lucro obtido no preço ótimo encontrado no item (b).

d) A diretoria da loja quer saber para quais preços o lucro mensal ultrapassa R\$ 2.400,00. Determine esse intervalo de preços.

e) Suponha agora que o custo de aquisição da jaqueta suba de R\$ 80,00 para um valor genérico $c$ reais, mantendo-se a mesma relação de demanda $q(p) = 300-2p$. Escreva o lucro $L(p,c)$ em função de $p$ e $c$, obtenha o preço ótimo em função de $c$ e use essa expressão para determinar de quanto aumenta o preço ótimo se o custo subir de R\$ 80,00 para R\$ 90,00.

## Gabarito

a) $L(p) = -2p^2+460p-24000$; b) $p=115$ reais, lucro máximo $= 2450$ reais; c) $L(114)=L(116)=2448 < 2450$, confirmando o máximo; d) $110 < p < 120$; e) $p^*(c) = 75 + c/2$; aumento de R$5,00 no preço ótimo quando o custo sobe R$10,00.

## Resolução

**a) Construção da função lucro**

O lucro unitário é (preço − custo) $= p - 80$. A quantidade vendida é $q(p) = 300-2p$. Logo:
$$L(p) = (p-80)(300-2p) = 300p - 2p^2 - 24000 + 160p = -2p^2 + 460p - 24000$$

com $80 < p < 150$.

**b) Preço ótimo e lucro máximo**

Como $a = -2 < 0$, a parábola tem concavidade para baixo, logo possui ponto de **máximo** no vértice:
$$p^* = -\frac{b}{2a} = -\frac{460}{2(-2)} = 115$$
$$L(115) = -2(115)^2 + 460(115) - 24000 = -26450 + 52900 - 24000 = 2450$$

O preço ótimo é **R\$ 115,00**, com lucro mensal máximo de **R\$ 2.450,00**.

**c) Confirmação pela comparação com preços vizinhos**

$$L(114) = -2(114)^2+460(114)-24000 = -25992+52440-24000 = 2448$$
$$L(116) = -2(116)^2+460(116)-24000 = -26912+53360-24000 = 2448$$

Como $L(114) = L(116) = 2448 < 2450 = L(115)$, o lucro cresce até $p=115$ e depois decresce — confirmando que $p=115$ é de fato o ponto de máximo (comportamento simétrico em torno do vértice).

**d) Intervalo em que o lucro supera R\$ 2.400,00**

$$-2p^2+460p-24000 > 2400 \Rightarrow -2p^2+460p-26400>0$$

Dividindo por $-2$ (invertendo a desigualdade):
$$p^2 - 230p + 13200 < 0$$

Raízes: $\Delta = 230^2 - 4(13200) = 52900-52800=100$, $\sqrt{\Delta}=10$
$$p = \frac{230\pm10}{2} \Rightarrow p=110 \text{ ou } p=120$$

Como a parábola $p^2-230p+13200$ tem concavidade para cima, ela é negativa entre as raízes:
$$110 < p < 120$$

Ou seja, o lucro supera R\$ 2.400,00 para preços entre R\$ 110,00 e R\$ 120,00.

**e) Lucro em função de $p$ e de um custo genérico $c$**

$$L(p,c) = (p-c)(300-2p) = -2p^2 + (300+2c)p - 300c$$

O vértice (preço ótimo) é:
$$p^*(c) = \frac{300+2c}{4} = 75 + \frac{c}{2}$$

Verificação: para $c=80$, $p^*=75+40=115$ (confere com o item b).

Para $c=90$: $p^*(90) = 75+45=120$.

A variação do preço ótimo é:
$$\Delta p^* = p^*(90)-p^*(80) = 120-115 = 5$$

Ou seja, se o custo de aquisição subir R\$ 10,00, o preço ótimo deve subir apenas **R\$ 5,00** — metade do aumento do custo, pois $p^*(c)=75+c/2$ tem coeficiente angular $1/2$ em relação a $c$.

## Formalização verificável

- `funcao` — expressão `-2*p**2 + 460*p - 24000`, esperado `[115, 2450]`, parâmetros `{'consulta': 'vertice'}`
- `equacao` — expressão `Eq(-2*p**2 + 460*p - 24000, 2400)`, esperado `[110, 120]`
- `propriedade` — expressão `-`, esperado `75 + c/2`, parâmetros `{'pontos': '[(80,115),(90,120)]', 'grau': '1'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (50, 9000)). | (2) aprovado: Gabarito confirmado (maximo de -10*p**2 + 1000*p - 16000 em Reals: 9000).
  - funcao/vertice=aprovado
  - funcao/maximo=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado bem definido: dá custo, função de demanda, fórmula do lucro, domínio explícito e pergunta única e objetiva. Não há ambiguidade lexical ou de dados.
  - adequacao_nivel: 2/5 — O processo exigido é puramente aplicar a fórmula do vértice de uma parábola (procedimento algorítmico), o que corresponde a 'aplicar' (Bloom) e a uma estrutura uniestrutural/multiestrutural (SOLO). Não há investigação, comparação de cenários, justificativa qualitativa do porquê é máximo além do sinal de 'a', nem exploração das restrições de domínio. Isso não atinge o nível 'analisar' declarado.
  - alinhamento_bncc: 4/5 — O contexto de Matemática Financeira (lucro, preço, custo) está presente e articulado numa única situação, e a pergunta pede exatamente o ponto de máximo de uma função quadrática, cumprindo os requisitos explícitos da especificação. Falta, porém, o caráter 'investigativo' pedido pela habilidade EM13MAT503 — a tarefa se reduz a aplicar o vértice, sem exigir interpretação do fenômeno (ex.: por que reduzir/aumentar o preço afeta o lucro, ou análise nos extremos do domínio).
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 2/5 — O problema segue o modelo clássico e repetitivo de livros didáticos (produto genérico, demanda linear, lucro quadrático, pede vértice). Não há elemento de contexto significativo diferenciado nem desafio investigativo; o enunciado praticamente pavimenta a solução ao fornecer L(p) já pronto, restando apenas substituir na fórmula do vértice — efeito Topaze evidente.
  - *sugestões:* 1) Elevar o nível cognitivo para 'analisar': em vez de fornecer L(p) já montado, peça que o aluno construa a função lucro a partir de dados de custo, preço e demanda, e que justifique por que o ponto encontrado é de máximo (não apenas citando o sinal de 'a', mas comparando valores de L em pontos vizinhos ou analisando a variação marginal). 2) Adicionar uma camada investigativa, por exemplo: pedir a faixa de preços para a qual o lucro é maior que um valor de referência, ou pedir como a resposta mudaria se o custo de aquisição aumentasse, exigindo reanálise do vértice em função de um parâmetro. 3) Tornar o contexto menos genérico e mais significativo — usar dados reais ou uma situação de decisão empresarial mais rica (ex.: promoção sazonal, comparação entre dois produtos) para evitar o padrão mecânico de livro didático. 4) Evitar fornecer L(p) pronto; deixar que o aluno derive a expressão a partir da relação preço-quantidade, reforçando o raciocínio investigativo em vez da mera substituição na fórmula do vértice.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Elevar o nível cognitivo para 'analisar': em vez de fornecer L(p) já montado, peça que o aluno construa a função lucro a partir de dados de custo, preço e demanda, e que justifique por que o ponto encontrado é de máximo (não apenas citando o sinal de 'a', mas comparando valores de L em pontos vizinhos ou analisando a variação marginal). 2) Adicionar uma camada investigativa, por exemplo: pedir a faixa de preços para a qual o lucro é maior que um valor de referência, ou pedir como a resposta mudaria se o custo de aquisição aumentasse, exigindo reanálise do vértice em função de um parâmetro. 3) Tornar o contexto menos genérico e mais significativo — usar dados reais ou uma situação de decisão empresarial mais rica (ex.: promoção sazonal, comparação entre dois produtos) para evitar o padrão mecânico de livro didático. 4) Evitar fornecer L(p) pronto; deixar que o aluno derive a expressão a partir da relação preço-quantidade, reforçando o raciocínio investigativo em vez da mera substituição na fórmula do vértice.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (115, 2450)). | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Propriedades confirmadas para c/2 + 75: reproduz os 2 pontos dados; grau 1.
  - funcao/vertice=aprovado
  - equacao=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem segmentado em itens, com dados numéricos explícitos, domínio de p definido (80<p<150) e cada subitem delimita claramente o que é pedido. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — Os subitens progridem de uniestrutural (a), multiestrutural (b), relacional (c e d, exigindo comparação e interpretação de comportamento da parábola) até quase extended abstract (e, generalização com parâmetro c), o que é compatível ou até superior ao nível 'analisar' declarado. Ressalva: a complexidade do item (e) - função de duas variáveis e derivação de fórmula paramétrica - contrasta com a dificuldade declarada como 'fácil', gerando alguma inconsistência entre o nível anunciado e a exigência cognitiva real do item final.
  - alinhamento_bncc: 4/5 — Os itens (a), (b), (c) e (e) atendem diretamente à habilidade EM13MAT503, investigando o ponto de máximo em contexto de matemática financeira e generalizando-o. O item (d), embora relevante ao tema de função quadrática, desloca o foco para resolução de inequação quadrática, que não é estritamente 'investigar ponto de máximo/mínimo'; não compromete o núcleo da questão, mas é uma extensão que extrapola ligeiramente a habilidade declarada.
  - distratores: 5/5 — não se aplica (questão discursiva).
  - originalidade: 3/5 — O contexto de 'preço ótimo de venda com demanda linear decrescente' é um clássico recorrente em livros didáticos de função quadrática, pouco inovador. Além disso, o enunciado já fornece explicitamente a regra de construção do lucro ('lucro é o produto entre o lucro unitário e a quantidade vendida'), o que caracteriza efeito Topaze: a etapa de modelagem, que seria o cerne de uma investigação, é entregue ao aluno, restando apenas manipulação algébrica e leitura de vértice/inequação.
