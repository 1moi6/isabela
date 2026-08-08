# Ciclo 027 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em sismologia, a energia $E$ (em joules) liberada por um terremoto se relaciona com sua magnitude $M$ na escala de momento sísmico pela expressão $\log_{10}(E) = 1{,}5\,M + 4{,}8$. Um instituto de monitoramento registrou dois eventos em uma mesma região: o Terremoto I, de magnitude $M_1 = 4{,}5$, e o Terremoto II, de magnitude $M_2 = 6{,}9$. Considerando a relação entre magnitude e energia liberada, qual das alternativas descreve corretamente quantas vezes a energia liberada pelo Terremoto II é maior que a liberada pelo Terremoto I?

## Alternativas

- (a) A energia liberada por II é aproximadamente 3981 vezes maior que a de I.  ← correta
- (b) A energia liberada por II é aproximadamente 3,6 vezes maior que a de I.
  - *erro representado:* Confundir o valor do expoente log10(E2/E1) = 1,5·(M2−M1) = 3,6 com a própria razão E2/E1, esquecendo de aplicar a exponenciação de base 10.
- (c) A energia liberada por II é aproximadamente 251 vezes maior que a de I.
  - *erro representado:* Esquecer o coeficiente 1,5 da fórmula e calcular apenas 10^(M2−M1) = 10^2,4, em vez de 10^(1,5·(M2−M1)).
- (d) A energia liberada por II é aproximadamente 1,53 vezes maior que a de I.
  - *erro representado:* Tratar a magnitude como diretamente proporcional à energia e calcular apenas a razão M2/M1 = 6,9/4,5, ignorando a natureza logarítmica da relação.

## Gabarito

A energia liberada pelo Terremoto II é aproximadamente 3981 vezes maior que a do Terremoto I.

## Resolução

**Passo 1 — Escrever a energia de cada evento a partir da fórmula.**

Como $\log_{10}(E) = 1{,}5M + 4{,}8$, temos $E = 10^{1{,}5M + 4{,}8}$. Logo:

$E_1 = 10^{1{,}5(4{,}5) + 4{,}8}$ e $E_2 = 10^{1{,}5(6{,}9) + 4{,}8}$

**Passo 2 — Perceber que a comparação pedida é uma razão, não um valor isolado.**

Em vez de calcular $E_1$ e $E_2$ separadamente (números enormes), usa-se a propriedade dos expoentes:

$\dfrac{E_2}{E_1} = \dfrac{10^{1{,}5M_2 + 4{,}8}}{10^{1{,}5M_1 + 4{,}8}} = 10^{1{,}5M_2 + 4{,}8 - (1{,}5M_1 + 4{,}8)} = 10^{1{,}5(M_2 - M_1)}$

Note que a constante $4{,}8$ se cancela: ela é a mesma para os dois eventos e **não interfere na variação relativa** — o que importa é a diferença de magnitudes.

**Passo 3 — Calcular a diferença de magnitude e o expoente.**

$M_2 - M_1 = 6{,}9 - 4{,}5 = 2{,}4$

$1{,}5 \times 2{,}4 = 3{,}6$

**Passo 4 — Elevar a base 10 ao expoente (não confundir o expoente com a razão!).**

$\dfrac{E_2}{E_1} = 10^{3{,}6} \approx 3981$

**Conclusão:** um aumento de $2{,}4$ pontos na escala de magnitude corresponde a uma energia cerca de **3981 vezes maior**, evidenciando que a relação entre magnitude e energia é exponencial (não linear): pequenas variações em $M$ produzem variações multiplicativas enormes em $E$.

## Formalização verificável

- `funcao` — expressão `10**(Rational(3,2)*M + Rational(24,5))`, esperado `10**(Rational(231,20))`, parâmetros `{'consulta': 'valor', 'ponto': 'Rational(9,2)'}`
- `funcao` — expressão `10**(Rational(3,2)*M + Rational(24,5))`, esperado `10**(Rational(303,20))`, parâmetros `{'consulta': 'valor', 'ponto': 'Rational(69,10)'}`
- `equacao` — expressão `Eq(10**(Rational(303,20))/10**(Rational(231,20)), x)`, esperado `[10**(Rational(18,5))]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(9/2) = 100000000000*10**(11/20)). | (2) aprovado: Gabarito confirmado (f(69/10) = 1000000000000000*10**(3/20)). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado apresenta claramente a fórmula, os dois valores de magnitude e a pergunta (razão E2/E1). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para a resolução.
  - adequacao_nivel: 4/5 — A tarefa exige mais do que aplicar diretamente a definição de logaritmo: o aluno precisa perceber que a comparação pedida é uma razão, que a constante 4,8 se cancela e que o expoente 1,5(M2−M1) não é a própria razão, mas seu logaritmo. Isso envolve decompor a relação e integrar múltiplos elementos (característica relacional/analítica). Ainda assim, o procedimento final é bastante guiado pelos passos da fórmula, ficando na fronteira entre 'aplicar' e 'analisar' — por isso não atinge nota máxima.
  - alinhamento_bncc: 5/5 — A questão atende exatamente ao que a habilidade pede: usa um contexto realista de abalos sísmicos e força a interpretação da variação da grandeza (energia) a partir da variação da magnitude, evidenciando a natureza exponencial/logarítmica da relação — não se limita a 'aplicar log10'. A conclusão explicitada na resolução (pequenas variações em M geram variações multiplicativas enormes em E) é justamente o tipo de interpretação de variação exigido pela EM13MAT305.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e distintos: confundir o expoente com a razão final, esquecer o coeficiente 1,5, e tratar a relação como proporcionalidade direta entre M e E. Nenhum é absurdo ou trivialmente eliminável, e cobrem os principais pontos de confusão conceitual do problema.
  - originalidade: 4/5 — O contexto sísmico com a escala de magnitude é um cenário comum em materiais didáticos sobre logaritmos, mas a questão evita o formato mais mecânico (calcular E para um único M) ao pedir a razão entre dois eventos, exigindo raciocínio sobre a estrutura da fórmula em vez de mera substituição. Não há pistas que entreguem o caminho da solução (efeito Topaze), mas o tema em si não é inédito.
