# Ciclo 057 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

A magnitude $M$ de um terremoto na escala Richter relaciona-se com a energia $E$ (em joules) liberada pelo abalo por meio da expressão $M = \dfrac{2}{3}\log_{10}\left(\dfrac{E}{E_0}\right)$, em que $E_0 = 10^{4,4}$ J é uma constante de referência. Uma cidade foi atingida por um terremoto de magnitude 5,0. Meses depois, a mesma região sofreu outro abalo, de magnitude 6,5. Aproximadamente quantas vezes maior foi a energia liberada pelo segundo terremoto em comparação com o primeiro?

## Alternativas

- (a) Aproximadamente 178 vezes maior.  ← correta
- (b) Aproximadamente 1,3 vezes maior (30% a mais), pois $6{,}5 \div 5{,}0 = 1{,}3$.
  - *erro representado:* Tratar a escala Richter como linear, calculando a razão direta entre as magnitudes em vez de reconhecer que M é logaritmo da energia.
- (c) Aproximadamente 32 vezes maior, pois $10^{1,5} \approx 31{,}6$.
  - *erro representado:* Usar apenas a diferença de magnitude como expoente de 10 (10^(ΔM)), esquecendo de multiplicar a diferença pelo fator 3/2 que vem da definição da fórmula.
- (d) Aproximadamente 10 vezes maior, pois $10^{1} = 10$.
  - *erro representado:* Inverter o fator da fórmula, usando o expoente (2/3)·ΔM em vez de (3/2)·ΔM ao isolar E, confundindo a relação direta com a inversa.

## Gabarito

Aproximadamente 178 vezes (10^2,25)

## Resolução

**Passo 1 — Isolar a energia $E$ em função de $M$.**

Da expressão $M = \dfrac{2}{3}\log_{10}\left(\dfrac{E}{E_0}\right)$, multiplicamos ambos os lados por $\dfrac{3}{2}$:

$$\dfrac{3}{2}M = \log_{10}\left(\dfrac{E}{E_0}\right)$$

Aplicando a definição de logaritmo:

$$\dfrac{E}{E_0} = 10^{\frac{3}{2}M} \quad\Rightarrow\quad E = E_0\cdot 10^{\frac{3}{2}M}$$

Isso mostra que a energia **não varia linearmente** com $M$: cada acréscimo de magnitude corresponde a uma multiplicação da energia por uma potência de 10.

**Passo 2 — Calcular a energia para cada magnitude.**

Para $M_1 = 5{,}0$: $E_1 = E_0\cdot 10^{\frac{3}{2}\cdot 5} = E_0\cdot 10^{7{,}5}$

Para $M_2 = 6{,}5$: $E_2 = E_0\cdot 10^{\frac{3}{2}\cdot 6{,}5} = E_0\cdot 10^{9{,}75}$

**Passo 3 — Calcular a razão entre as energias.**

$$\dfrac{E_2}{E_1} = \dfrac{E_0\cdot 10^{9{,}75}}{E_0\cdot 10^{7{,}5}} = 10^{9{,}75-7{,}5} = 10^{2{,}25}$$

Note que o expoente $2{,}25$ é exatamente $\dfrac{3}{2}\cdot(M_2-M_1) = \dfrac{3}{2}\cdot 1{,}5 = \dfrac{9}{4}$.

**Passo 4 — Calcular o valor numérico.**

$$10^{2{,}25} = 10^2 \cdot 10^{0{,}25} \approx 100 \times 1{,}778 \approx 177{,}8$$

**Conclusão:** o segundo terremoto liberou aproximadamente **178 vezes** mais energia que o primeiro, mesmo a magnitude tendo aumentado apenas 1,5 unidade — evidenciando o crescimento exponencial da energia em relação à escala logarítmica de magnitude.

## Formalização verificável

- `funcao` — expressão `Rational(2,3)*log(x/10**Rational(44,10), 10)`, esperado `5`, parâmetros `{'consulta': 'valor', 'ponto': '10**Rational(119,10)'}`
- `funcao` — expressão `Rational(2,3)*log(x/10**Rational(44,10), 10)`, esperado `Rational(13,2)`, parâmetros `{'consulta': 'valor', 'ponto': '10**Rational(283,20)'}`
- `equacao` — expressão `Eq(k, 10**(Rational(9,4)))`, esperado `[10**(Rational(9,4))]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(100000000000*10**(9/10)) = 5). | (2) aprovado: Gabarito confirmado (f(100000000000000*10**(3/20)) = 13/2). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente a fórmula, os valores de M para os dois eventos e a pergunta (razão entre energias). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para a resolução.
  - adequacao_nivel: 4/5 — A tarefa exige mais que aplicação mecânica da definição de logaritmo: o aluno precisa isolar E, comparar dois estados e perceber que a diferença de magnitude não se traduz linearmente na energia, o que caracteriza uma estrutura relacional (SOLO) compatível com 'analisar'. Ainda assim, o processo é fortemente algébrico/procedimental, ficando um pouco aquém de uma análise mais aberta (ex.: comparar múltiplos cenários ou justificar o comportamento assintótico).
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as exigências: usa função logarítmica em contexto de abalos sísmicos (explicitamente citado na habilidade), e o cerne do problema é interpretar como uma pequena variação em M gera uma variação multiplicativa expressiva em E — a variação das grandezas é o próprio objeto da questão, não um subproduto acessório.
  - distratores: 5/5 — Os três distratores representam erros conceituais plausíveis e distintos: tratar a escala como linear, esquecer o fator 3/2, e inverter esse fator. Nenhum é absurdo ou trivialmente descartável sem cálculo, exigindo do aluno reconhecer corretamente a estrutura da fórmula.
  - originalidade: 3/5 — O contexto da escala Richter com cálculo de razão de energia é um clássico recorrente em livros didáticos e vestibulares; a estrutura de resolução (isolar E, substituir, dividir) segue o roteiro padrão sem inovação de contexto, formato ou abordagem. Não há efeito Topaze evidente, mas também não há elemento diferenciador que fuja do already conhecido.
