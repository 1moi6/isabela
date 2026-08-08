# Ciclo 077 — EM13MAT303

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma fintech oferece uma aplicação financeira em que o capital investido é corrigido mensalmente por juros compostos, a uma taxa fixa, sem aportes ou resgates. Marina investiu R$ 6.000,00 nessa aplicação, com taxa de 4% ao mês.

a) Elabore a expressão algébrica da função $M(t)$, que fornece o montante (em reais) acumulado por Marina após $t$ meses de aplicação.

b) Utilizando a função elaborada, calcule o montante ao final do 10º mês, arredondando o resultado para duas casas decimais.

c) Determine o menor número inteiro de meses necessário para que o montante ultrapasse o dobro do capital investido. Em seguida, explique por que esse tempo é bem menor do que o que seria necessário caso o capital rendesse mensalmente um valor fixo de R$ 240,00 (4% do capital inicial, sem incidência de juros sobre juros) — evidenciando, com essa comparação, o caráter exponencial (e não linear) do crescimento sob juros compostos.

## Gabarito

a) $M(t) = 6000\cdot(1,04)^t$; b) $M(10) \approx R\$\,8.881{,}47$; c) menor número inteiro de meses: $t = 18$ (contra 25 meses no regime linear equivalente, evidenciando o crescimento exponencial).

## Resolução

**a) Modelagem da função**

Como o capital é corrigido mensalmente por uma taxa percentual constante $i = 4\% = 0,04$ aplicada sobre o montante do mês anterior (e não sobre um valor fixo), cada mês o montante é multiplicado pelo mesmo fator $(1+i)$. Isso caracteriza um crescimento exponencial:

$$M(t) = 6000\cdot(1+0,04)^t = 6000\cdot(1,04)^t = 6000\cdot\left(\dfrac{26}{25}\right)^t$$

em que $t$ é o número de meses.

**b) Montante após 10 meses**

$$M(10) = 6000\cdot(1,04)^{10} = 6000\cdot 1{,}480244\ldots \approx R\$\,8.881{,}47$$

**c) Tempo para dobrar o capital**

Queremos o menor $t$ inteiro tal que $M(t) > 12000$ (o dobro de 6000):

$$6000\cdot(1,04)^t > 12000 \;\Rightarrow\; (1,04)^t > 2$$

Aplicando logaritmo em ambos os lados:

$$t > \dfrac{\log 2}{\log 1,04} \approx \dfrac{0,6931}{0,03922} \approx 17,67$$

Como $t$ deve ser um número inteiro de meses, o menor valor que satisfaz a desigualdade é $t = 18$. Conferindo:

- $M(17) = 6000\cdot(1,04)^{17} \approx R\$\,11.687{,}40 < 12.000$
- $M(18) = 6000\cdot(1,04)^{18} \approx R\$\,12.154{,}90 > 12.000$

Logo, **18 meses** é o menor número inteiro de meses necessário.

**Comparação com crescimento linear**

Se, em vez de juros compostos, o capital rendesse sempre um valor fixo de $0,04\cdot 6000 = R\$\,240,00$ por mês (juros simples, crescimento linear), o montante seria $M_{lin}(t) = 6000 + 240t$, e o tempo para dobrar o capital seria:

$$6000 + 240t = 12000 \;\Rightarrow\; t = \dfrac{6000}{240} = 25 \text{ meses}$$

Assim, no regime linear seriam necessários 25 meses, contra apenas 18 meses nos juros compostos. Essa diferença ocorre porque, nos juros compostos, os 4% incidem sobre um montante que cresce mês a mês (juros sobre juros), fazendo os incrementos mensais aumentarem progressivamente — comportamento típico de uma função exponencial, e não de uma função linear, em que o incremento mensal é sempre o mesmo valor fixo.

## Formalização verificável

- `funcao` — expressão `6000*Rational(26,25)**t`, esperado `6000*Rational(26,25)**10`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `funcao` — expressão `6000*Rational(26,25)**t`, esperado `6000*Rational(26,25)**17`, parâmetros `{'consulta': 'valor', 'ponto': '17'}`
- `funcao` — expressão `6000*Rational(26,25)**t`, esperado `6000*Rational(26,25)**18`, parâmetros `{'consulta': 'valor', 'ponto': '18'}`
- `equacao` — expressão `Eq(6000*Rational(26,25)**n, 12000)`, esperado `[log(2)/log(Rational(26,25))]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(10) = 6776020591362048/762939453125). | (2) aprovado: Gabarito confirmado (f(17) = 54423711138487234826600448/4656612873077392578125). | (3) aprovado: Gabarito confirmado (f(18) = 1415016489600668105491611648/116415321826934814453125). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem segmentado em três itens, com dados completos (capital, taxa, condições de ausência de aportes/resgates) e comandos verbais precisos (elaborar, calcular, determinar, explicar). Não há ambiguidade lexical ou estrutural relevante.
  - adequacao_nivel: 4/5 — O item (a) exige efetivamente 'criar' a expressão algébrica a partir da descrição textual do fenômeno, compatível com Bloom 'criar' e SOLO relacional/estendido abstrato. Os itens (b) e (c) recaem em 'aplicar' e 'analisar/avaliar' (comparação com crescimento linear), o que é coerente com um problema aplicado, mas faz com que o nível cognitivo mais alto (criar) fique restrito a apenas uma parte da questão, não sustentado ao longo de toda ela.
  - alinhamento_bncc: 5/5 — Atende plenamente à EM13MAT303: envolve juros compostos e porcentagem, exige elaboração de modelo exponencial (não apenas cálculo isolado) e articula explicitamente a comparação com crescimento linear (juros simples) para evidenciar o caráter exponencial, que é exatamente a exigência central da habilidade.
  - distratores: 5/5 — Não se aplica (questão discursiva, sem alternativas).
  - originalidade: 4/5 — O contexto de fintech é atual, mas o núcleo do problema (capital investido a juros compostos) é um cenário recorrente em livros didáticos. O diferencial está na comparação estrutural com o regime linear equivalente no item (c), que exige raciocínio próprio em vez de aplicação mecânica de fórmula, reduzindo o efeito Topaze. Ainda assim, poderia explorar um contexto menos convencional (ex.: dados de mercado real, gráfico, tabela) para elevar a originalidade.
