# Ciclo 033 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 2

## Enunciado

Um professor propõe que os alunos investiguem, usando um software gráfico (ou construindo os gráficos manualmente em papel milimetrado), as funções $f(x) = 2^x$ e $g(x) = \log_2 x$.

a) Determine o domínio e o conjunto-imagem de $f$ e de $g$. Compare esses dois conjuntos (domínio de $f$ com imagem de $g$, e domínio de $g$ com imagem de $f$) e explique, matematicamente, por que essa relação ocorre.

b) Calcule $f(3)$ e $g(8)$; calcule também $f(0)$ e $g(1)$. Observando os pares de valores obtidos, descreva que tipo de simetria os gráficos de $f$ e $g$ apresentam no plano cartesiano.

c) Classifique $f$ e $g$ quanto ao crescimento (crescente ou decrescente) em todo o domínio de cada uma. Em seguida, utilizando os valores calculados no item (b), explique por que o fato de $f$ e $g$ serem ambas crescentes é compatível com a simetria identificada — ou seja, justifique por que essa simetria não transforma o crescimento de uma função em decrescimento na outra.

## Gabarito

a) $D(f)=\mathbb{R}=Im(g)$ e $D(g)=(0,+\infty)=Im(f)$, pois $g$ é a inversa de $f$. b) $f(3)=8, g(8)=3, f(0)=1, g(1)=0$: os gráficos de $f$ e $g$ são simétricos em relação à reta $y=x$. c) $f$ e $g$ são ambas crescentes; a simetria por $y=x$ preserva a ordem dos valores, por isso não inverte o crescimento.

## Resolução

**a) Domínio e imagem**

Para $f(x) = 2^x$: como a base $2>0$ e $2 \neq 1$, a expressão $2^x$ está definida para todo $x$ real e sempre resulta em um número positivo. Logo:
$$D(f) = \mathbb{R}, \qquad Im(f) = (0, +\infty)$$

Para $g(x) = \log_2 x$: o logaritmo só é definido para argumentos positivos, e pode resultar em qualquer número real. Logo:
$$D(g) = (0, +\infty), \qquad Im(g) = \mathbb{R}$$

Comparando: $D(f) = Im(g) = \mathbb{R}$ e $D(g) = Im(f) = (0,+\infty)$. Essa troca ocorre porque $g$ é a **função inversa** de $f$ (pois $g(x)=\log_2 x$ desfaz a operação $f(x)=2^x$, já que $\log_2(2^x)=x$). Para duas funções inversas entre si, o domínio de uma é sempre igual à imagem da outra, pois inverter uma função significa trocar o papel de $x$ e $y$.

**b) Valores e simetria**

$f(3) = 2^3 = 8$ e $g(8) = \log_2 8 = 3$. O ponto $(3,8)$ pertence ao gráfico de $f$, e o ponto $(8,3)$ pertence ao gráfico de $g$ — as coordenadas estão trocadas.

$f(0) = 2^0 = 1$ e $g(1) = \log_2 1 = 0$. O ponto $(0,1)$ pertence a $f$, e o ponto $(1,0)$ pertence a $g$ — novamente coordenadas trocadas.

Como, para todo ponto $(a,b)$ do gráfico de $f$, o ponto $(b,a)$ pertence ao gráfico de $g$, os dois gráficos são **simétricos em relação à reta $y = x$** (reflexão que troca as coordenadas de cada ponto).

**c) Crescimento e compatibilidade com a simetria**

$f(x)=2^x$ é crescente em $\mathbb{R}$ (base $2>1$: quanto maior $x$, maior $2^x$).

$g(x)=\log_2 x$ é crescente em $(0,+\infty)$ (base $2>1$: quanto maior $x$, maior $\log_2 x$).

Com os valores do item (b): $f(0)=1 < f(3)=8$ mostra que $f$ cresce de $x=0$ para $x=3$. Ao refletir esses pontos trocando as coordenadas, obtemos $g(1)=0 < g(8)=3$, ou seja, $g$ também cresce de $x=1$ para $x=8$. A ordem entre os valores foi preservada na troca de coordenadas — isso acontece porque a reflexão em torno da reta $y=x$ preserva a relação de ordem quando a função original é crescente (se $x_1<x_2 \Rightarrow f(x_1)<f(x_2)$, então trocando as coordenadas, $f(x_1) < f(x_2)$ vira exatamente a condição de que $g$ também cresce nesse intervalo). Por isso, a simetria em relação a $y=x$ **não inverte o sentido de crescimento**: uma função crescente tem inversa também crescente (o mesmo não ocorreria se $f$ fosse decrescente, caso em que $g$ também seria decrescente).

## Formalização verificável

- `funcao` — expressão `2**x`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2**x`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'imagem', 'dominio': 'S.Reals'}`
- `funcao` — expressão `2**x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(x, 2)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(x, 2)`, esperado `S.Reals`, parâmetros `{'consulta': 'imagem', 'dominio': 'Interval.open(0, oo)'}`
- `funcao` — expressão `log(x, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `2**x`, esperado `8`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `log(x, 2)`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`
- `funcao` — expressão `2**x`, esperado `1`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`
- `funcao` — expressão `log(x, 2)`, esperado `0`, parâmetros `{'consulta': 'valor', 'ponto': '1'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 5 de 6 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado claro, dados completos (funções explicitadas, domínios pedidos como maiores subconjuntos possíveis), pedido dividido em três itens bem delimitados, sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — Os itens (a) e (b) são de nível 'compreender/aplicar' (determinar domínio/imagem, classificar crescimento) e admitem resposta multiestrutural (fatos isolados sobre cada função). Só o item (c) exige de fato relacionar as duas funções e justificar com base nos itens anteriores, o que se aproxima de 'analisar' (estrutura relacional, SOLO). Como a maior parte da questão fica em nível inferior e apenas o item final atinge o nível declarado, a exigência cognitiva efetiva é heterogênea, abaixo do que 'analisar' pressupõe de ponta a ponta.
  - alinhamento_bncc: 3/5 — A questão trata domínio, imagem e crescimento de ambas as funções e pede a relação geométrica entre elas no item (c), o que atende ao núcleo da habilidade. Contudo, os itens (a) e (b) são resolvidos separadamente para f e para g, funcionando como subquestões justapostas e independentes (a habilidade adverte explicitamente contra isso: 'não uma de cada vez'). A articulação numa análise integrada só ocorre no item final, e mesmo aí a resolução entrega quase toda a conclusão (é a inversa, simétrica a y=x), reduzindo o esforço analítico do aluno a uma verificação de padrão já apontado pela estrutura do enunciado.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — É o exemplo canônico e recorrente de livro didático (exponencial de base 2 e seu log de base 2, simetria em y=x). Não há contexto significativo ou situação aplicada. Além disso, a resolução e o gabarito revelam de forma direta a relação-chave (função inversa, simetria) logo nos itens anteriores, funcionando como efeito Topaze: o aluno é conduzido item a item até a conclusão, sem precisar descobrir a relação por si.
  - *sugestões:* 1) Reestruture os itens para que a comparação seja o eixo central desde o início, evitando resolver f e g separadamente: por exemplo, peça diretamente 'compare o domínio e a imagem de f e g e explique por que ocorre essa relação' em vez de pedir domínio/imagem de cada uma isoladamente e só depois relacioná-las. 2) Remova ou reduza pistas na formulação que já sugerem a resposta (não mencione que os gráficos 'estão traçados no mesmo plano' de forma que induza à simetria); peça ao aluno que ele mesmo trace ou analise os gráficos e infira a relação, sem indicar de antemão que há uma relação a ser descoberta. 3) Insira um contexto ou situação aplicada (uso de tecnologia, gráfico dado para leitura, dados de um fenômeno real modelado por exponencial/log) para fugir do exemplo-padrão de livro didático. 4) Ajuste o item (c) para exigir justificativa analítica mais elaborada, como comparar taxas de crescimento ou usar valores específicos para evidenciar a simetria, elevando de fato o processo cognitivo ao nível 'analisar' em toda a questão, não apenas no fechamento.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reestruture os itens para que a comparação seja o eixo central desde o início, evitando resolver f e g separadamente: por exemplo, peça diretamente 'compare o domínio e a imagem de f e g e explique por que ocorre essa relação' em vez de pedir domínio/imagem de cada uma isoladamente e só depois relacioná-las. 2) Remova ou reduza pistas na formulação que já sugerem a resposta (não mencione que os gráficos 'estão traçados no mesmo plano' de forma que induza à simetria); peça ao aluno que ele mesmo trace ou analise os gráficos e infira a relação, sem indicar de antemão que há uma relação a ser descoberta. 3) Insira um contexto ou situação aplicada (uso de tecnologia, gráfico dado para leitura, dados de um fenômeno real modelado por exponencial/log) para fugir do exemplo-padrão de livro didático. 4) Ajuste o item (c) para exigir justificativa analítica mais elaborada, como comparar taxas de crescimento ou usar valores específicos para evidenciar a simetria, elevando de fato o processo cognitivo ao nível 'analisar' em toda a questão, não apenas no fechamento.

### Iteração 2

- **Verificador:** aprovado_parcial — 9 de 10 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)). | (7) aprovado: Gabarito confirmado (f(3) = 8). | (8) aprovado: Gabarito confirmado (f(8) = 3). | (9) aprovado: Gabarito confirmado (f(0) = 1). | (10) aprovado: Gabarito confirmado (f(1) = 0).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado dividido em três itens bem delimitados, cada um especificando claramente o que é dado (as duas funções) e o que se pede (domínio/imagem, valores/simetria, crescimento/justificativa). Não há ambiguidade lexical ou estrutural; os dados são suficientes para resolver cada etapa.
  - adequacao_nivel: 4/5 — O item (a) exige comparação e explicação matemática (analisar), o item (c) exige justificar por que a simetria não inverte o crescimento — isso é relacional/analítico, coerente com SOLO relacional e Bloom 'analisar'. O item (b), isoladamente, é mais aplicação (calcular valores), mas funciona como etapa preparatória para a análise pedida em (c), não como fim em si. Conteúdo plenamente compatível com o Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão articula exponencial e logarítmica num único problema, exigindo comparação de domínio, imagem e crescimento, e estabelece a relação entre elas (inversibilidade, simetria em y=x). O cálculo de valores em (b) não é o objetivo final, mas evidência usada para justificar a simetria exigida em (c) — portanto cumpre a habilidade, não apenas 'toca no assunto'.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — A abordagem (domínio/imagem trocados, simetria em y=x, crescimento preservado) é um percurso clássico no ensino de funções inversas exponencial/logarítmica, ainda que bem estruturado. O enunciado guia bastante o raciocínio ao pedir explicitamente os pares de valores a calcular em (b), reduzindo o espaço de investigação autônoma sugerido pela introdução (uso de software). Poderia ganhar em originalidade com um contexto aplicado (ex.: escalas, crescimento populacional) em vez de tratamento puramente formal.
