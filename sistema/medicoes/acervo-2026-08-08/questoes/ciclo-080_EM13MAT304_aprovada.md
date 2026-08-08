# Ciclo 080 — EM13MAT304

- **Situação:** aprovada
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Em um laboratório de microbiologia, uma cultura de bactérias é colocada para crescer em condições ideais. No instante em que a contagem se inicia (t = 0 horas), há 300 bactérias. Após 6 horas de observação, a contagem indica 2400 bactérias. Sabe-se que, nessas condições, a população cresce exponencialmente com uma taxa constante por hora (ou seja, o número de bactérias é multiplicado pelo mesmo fator a cada hora que passa). Determine quantas horas, contadas a partir do início da observação, serão necessárias para que a população atinja 19200 bactérias.

## Alternativas

- (a) 12 horas  ← correta
- (b) 36 horas
  - *erro representado:* Interpreta erroneamente o intervalo de 6 horas do enunciado como o próprio 'tempo de duplicação', calculando 19200/300 = 64 = 2^6 e multiplicando 6 duplicações por 6 horas cada, em vez de extrair corretamente o fator de crescimento por hora (dobra a cada 2 horas).
- (c) 54 horas
  - *erro representado:* Trata o crescimento como linear (aritmético) em vez de exponencial: calcula a taxa de aumento por hora como (2400-300)/6 = 350 e usa regra de três para achar quando a população chegaria a 19200.
- (d) 2 horas
  - *erro representado:* Encontra corretamente que b^6 = 8, mas conclui erroneamente que b = 8 (sem extrair a raiz sexta), resolvendo 300·8^t = 19200 e obtendo t = 2.

## Gabarito

12 horas

## Resolução

**Passo 1 — Montar o modelo exponencial.**

Como o crescimento é exponencial com taxa constante por hora, a população pode ser escrita como
$$P(t) = P_0 \cdot b^{t}$$
onde $P_0 = 300$ (população inicial) e $b$ é o fator de crescimento por hora.

**Passo 2 — Usar o dado em $t=6$ para interpretar a taxa de variação.**

Como $P(6) = 2400$:
$$300 \cdot b^{6} = 2400 \;\Rightarrow\; b^{6} = 8$$

Como $8 = 2^3$, temos $b^6 = 2^3$, ou seja, $b = 2^{1/2} = \sqrt{2}$.

Isso significa que, embora a população multiplique por 8 em 6 horas, o fator de crescimento a cada hora é $\sqrt{2}$ — equivalente a dizer que a população **dobra a cada 2 horas** (pois $b^2 = (\sqrt2)^2 = 2$). É esse ritmo de variação, e não o intervalo de 6 horas em si, que deve ser usado para projetar o crescimento.

**Passo 3 — Escrever o modelo já com esse fator.**

$$P(t) = 300 \cdot 2^{t/2}$$

(Verificação: $P(6) = 300\cdot 2^{3} = 300 \cdot 8 = 2400$ ✓)

**Passo 4 — Resolver a equação para $P(t) = 19200$.**

$$300 \cdot 2^{t/2} = 19200 \;\Rightarrow\; 2^{t/2} = 64$$

Como $64 = 2^6$:
$$\frac{t}{2} = 6 \;\Rightarrow\; t = 12$$

**Conclusão:** serão necessárias **12 horas** desde o início da contagem para que a população atinja 19200 bactérias.

## Formalização verificável

- `equacao` — expressão `Eq(300*2**(t/2), 19200)`, esperado `[12]`
- `funcao` — expressão `300*2**(t/2)`, esperado `2400`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `funcao` — expressão `300*2**(t/2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento', 'dominio': 'Interval(0, oo)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-1 + 2**(1/5)*(-1/4 + sqrt(5)/4 - I*sqrt(sqrt(5)/8 + 5/8)), -1 + 2**(1/5)*(-1/4 + sqrt(5)/4 + I*sqrt(sqrt(5)/8 + 5/8)), -1 + 2**(1/5)*(-sqrt(5)/4 - 1/4 - I*sqrt(5/8 - sqrt(5)/8)), -1 + 2**(1/5)*(-sqrt(5)/4 - 1/4 + I*sqrt(5/8 - sqrt(5)/8))]. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - equacao=aprovado
  - equacao=rejeitado
  - funcao/crescimento=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-1 + 2**(1/5)*(-1/4 + sqrt(5)/4 - I*sqrt(sqrt(5)/8 + 5/8)), -1 + 2**(1/5)*(-1/4 + sqrt(5)/4 + I*sqrt(sqrt(5)/8 + 5/8)), -1 + 2**(1/5)*(-sqrt(5)/4 - 1/4 - I*sqrt(5/8 - sqrt(5)/8)), -1 + 2**(1/5)*(-sqrt(5)/4 - 1/4 + I*sqrt(5/8 - sqrt(5)/8))]. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). Resultado calculado independentemente: [35] | [-1 + 2**(1/5), -1 + 2**(1/5)*(-1/4 + sqrt(5)/4 - I*sqrt(sqrt(5)/8 + 5/8)), -1 + 2**(1/5)*(-1/4 + sqrt(5)/4 + I*sqrt(sqrt(5)/8 + 5/8)), -1 + 2**(1/5)*(-sqrt(5)/4 - 1/4 - I*sqrt(5/8 - sqrt(5)/8)), -1 + 2**(1/5)*(-sqrt(5)/4 - 1/4 + I*sqrt(5/8 - sqrt(5)/8))] | crescente em Interval(-oo, oo). Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (f(6) = 2400). | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - equacao=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem definido: dados iniciais, taxa constante, valor-alvo e pergunta explícitos, sem ambiguidade lexical ou estrutural. Todas as informações necessárias estão presentes.
  - adequacao_nivel: 5/5 — A resolução exige mais que aplicação mecânica de fórmula: o aluno deve extrair o fator de crescimento por hora a partir de um intervalo de 6h e depois aplicar esse fator em uma nova equação exponencial — compatível com 'aplicar' em nível relacional (SOLO), adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — Cumpre a habilidade EM13MAT304: exige interpretar a variação (perceber que o dobro ocorre a cada 2h, não a cada 6h) além de calcular, em contexto realista de crescimento microbiano. Articula compreensão e cálculo em um único problema coeso.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e distintos: má interpretação do intervalo temporal (36h), confusão entre crescimento linear e exponencial (54h), e erro algébrico ao não extrair a raiz corretamente (2h). Nenhum é trivialmente eliminável.
  - originalidade: 4/5 — O contexto de cultura bacteriana é um clássico do gênero, mas o enunciado evita o 'efeito Topaze' ao não revelar diretamente o período de duplicação, forçando o aluno a deduzi-lo. Poderia ganhar mais originalidade com variação de contexto ou formato de dados (ex.: gráfico, tabela).
