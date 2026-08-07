# Ciclo 017 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Considere a progressão geométrica $(a_n)$ com $a_1 = 3$ e razão $q = 2$, isto é, $(a_n) = (3, 6, 12, 24, 48, \dots)$.

Toda PG pode ser vista como a restrição aos naturais não nulos de uma função exponencial $f(x) = A\cdot b^{x}$, com $A$ e $b$ constantes reais, tal que $f(n) = a_n$ para todo $n \in \mathbb{N}^*$.

Um colega afirmou que a função exponencial associada a essa PG é $g(x) = 3\cdot 2^{x}$, pois bastou usar o primeiro termo da PG como coeficiente e a razão como base.

Verifique se a proposta do colega é de fato consistente com pelo menos dois termos da progressão. Em seguida, determine a função exponencial $f(x) = A\cdot b^{x}$ que corretamente satisfaz $f(n) = a_n$ para todo $n \in \mathbb{N}^*$ e calcule o valor de $f\left(\dfrac{3}{2}\right)$.

## Alternativas

- (a) $f(3/2) = 3\sqrt{2}$  ← correta
- (b) $f(3/2) = 6\sqrt{2}$
  - *erro representado:* Manteve a proposta incorreta do colega (A = a1 = 3 em vez de A = a1/q), calculando com g(x)=3·2^x em vez da função corrigida.
- (c) $f(3/2) = 6$
  - *erro representado:* Tratou o domínio como apenas os naturais, arredondando x=3/2 para n=2 e usando diretamente o termo a2 da PG, ignorando a extensão contínua da exponencial.
- (d) $f(3/2) = 6\sqrt{3}$
  - *erro representado:* Confundiu a base b da exponencial com o primeiro termo da PG (usou b=3 em vez de b=q=2), montando f(x)=2·3^x.

## Gabarito

$f(3/2) = 3\sqrt{2}$

## Resolução

**Passo 1 — Testar a proposta do colega**

A proposta é $g(x) = 3\cdot 2^{x}$. Verificando nos dois primeiros índices da PG:

$g(1) = 3\cdot 2^1 = 6$, mas $a_1 = 3$.

$g(2) = 3\cdot 2^2 = 12$, mas $a_2 = 6$.

Em ambos os casos, $g(n) = 2\cdot a_n = a_{n+1}$: o colega usou $A = a_1$ em vez de ajustar o coeficiente, o que desloca toda a função em uma unidade de índice. Logo, $g$ **não** é a função correta.

**Passo 2 — Determinar $A$ e $b$ corretamente**

Como $f(n) = A\cdot b^n$ deve valer $a_1=3$ e $a_2=6$:

$A\cdot b = 3 \quad (i)$

$A\cdot b^2 = 6 \quad (ii)$

Dividindo (ii) por (i): $b = \dfrac{6}{3} = 2$, que coincide com a razão $q$ da PG — isso não é coincidência: a razão entre termos consecutivos de uma PG é exatamente a base da exponencial que a representa.

Substituindo em (i): $A\cdot 2 = 3 \Rightarrow A = \dfrac{3}{2}$.

Assim, $f(x) = \dfrac{3}{2}\cdot 2^{x} = 3\cdot 2^{x-1}$.

Conferindo: $f(1) = 3\cdot 2^0 = 3 = a_1$; $f(2) = 3\cdot 2^1 = 6 = a_2$; $f(3) = 3\cdot 2^2 = 12 = a_3$. A função é consistente com toda a PG.

**Passo 3 — Calcular $f(3/2)$**

$f\left(\dfrac{3}{2}\right) = 3\cdot 2^{\frac{3}{2}-1} = 3\cdot 2^{1/2} = 3\sqrt{2}$.

Observe que $x = 3/2$ não corresponde a nenhum termo da PG (que só existe para índices naturais), mas a extensão exponencial permite calcular esse valor intermediário de forma consistente com os termos discretos conhecidos.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*2**(x-1)`, parâmetros `{'pontos': '[(1,3),(2,6),(3,12)]', 'sequencia': 'pg', 'a1': '3', 'razao': '2'}`
- `funcao` — expressão `3*2**(x-1)`, esperado `3*sqrt(2)`, parâmetros `{'consulta': 'valor', 'ponto': 'Rational(3,2)'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*2**(n - 1): coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(7/2) = 12*sqrt(2)).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define precisamente a PG, a forma da função exponencial, a condição de coincidência nos naturais e o valor pedido. Não há ambiguidade lexical ou estrutural; os dados são suficientes e a notação é padrão.
  - adequacao_nivel: 2/5 — Embora o Bloom declarado seja 'analisar', o processo cognitivo real exigido é resolver um sistema linear simples (duas equações para A e b) e substituir na fórmula — isto é 'aplicar' (C3), não 'analisar' (C4). Na taxonomia SOLO a resposta esperada é multiestrutural (executar passos independentes em sequência: achar b, achar A, substituir), sem exigir comparação, justificativa estrutural ou inferência sobre relações não explicitadas. A resolução fornecida confirma isso: é um algoritmo direto de 5 passos mecânicos, sem exigência de análise crítica (ex.: discutir por que a extensão é única, comparar hipóteses alternativas, ou justificar condições de existência).
  - alinhamento_bncc: 4/5 — A questão cumpre a exigência de articular PG e função exponencial num único problema, indo além da mera aplicação do termo geral (exige montar e resolver o sistema A·b e A·b² para obter os parâmetros). Isso atende ao requisito 'a associação... precisa ser exigida pelo enunciado'. Um ponto de atenção: a habilidade fala em 'domínios discretos', mas o problema pede justamente uma extensão a um valor não natural (7/2), o que é pedagogicamente rico mas desloca parcialmente o foco do domínio discreto para o contínuo — isso não invalida o alinhamento, mas merece nota abaixo do máximo por não explorar tanto as propriedades discretas da PG em si (ex.: soma, recorrência).
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: confundir A com a1 (24√2), aplicar média aritmética em vez de geométrica (18), e arredondar o domínio para o natural mais próximo (24). Nenhum é absurdo ou trivialmente eliminável por inspeção superficial.
  - originalidade: 4/5 — O problema evita o padrão mecânico de 'ache o décimo termo da PG' e explora a interpolação exponencial de forma pouco comum em livros didáticos, com verificação via média geométrica. Não há contexto do mundo real (é puramente formal), o que limita um pouco a significância, mas não há pistas explícitas que pavimentem a solução (efeito Topaze) — o aluno precisa de fato montar o sistema.
  - *sugestões:* Elevar o nível cognitivo de 'aplicar' para 'analisar' de forma coerente com SOLO relacional/estendido abstrato. Sugestões concretas: (1) Apresentar DUAS propostas de função exponencial que passam pelos mesmos dois primeiros termos da PG (ex.: com bases ou constantes diferentes) e pedir ao aluno que analise/justifique qual delas é a extensão válida para todos os naturais, obrigando comparação e argumentação, não só cálculo. (2) Ou pedir que o aluno demonstre/justifique por que a base b da exponencial deve necessariamente coincidir com a razão q da PG, antes de calcular f(7/2) — transformando o passo 2 da resolução (hoje apenas verificado) em parte explícita da tarefa de análise. (3) Ou incluir um item que peça para identificar o erro em uma resolução incorreta apresentada (ex.: alguém que usou A=3), exigindo que o estudante analise a inconsistência entre a proposta e a condição dada. Qualquer uma dessas mudanças manteria a articulação PG-exponencial já presente, mas exigiria decompor, comparar ou justificar relações, alinhando o processo cognitivo ao Bloom 'analisar' declarado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Elevar o nível cognitivo de 'aplicar' para 'analisar' de forma coerente com SOLO relacional/estendido abstrato. Sugestões concretas: (1) Apresentar DUAS propostas de função exponencial que passam pelos mesmos dois primeiros termos da PG (ex.: com bases ou constantes diferentes) e pedir ao aluno que analise/justifique qual delas é a extensão válida para todos os naturais, obrigando comparação e argumentação, não só cálculo. (2) Ou pedir que o aluno demonstre/justifique por que a base b da exponencial deve necessariamente coincidir com a razão q da PG, antes de calcular f(7/2) — transformando o passo 2 da resolução (hoje apenas verificado) em parte explícita da tarefa de análise. (3) Ou incluir um item que peça para identificar o erro em uma resolução incorreta apresentada (ex.: alguém que usou A=3), exigindo que o estudante analise a inconsistência entre a proposta e a condição dada. Qualquer uma dessas mudanças manteria a articulação PG-exponencial já presente, mas exigiria decompor, comparar ou justificar relações, alinhando o processo cognitivo ao Bloom 'analisar' declarado.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*2**(x - 1): reproduz os 3 pontos dados; coincide com a PG declarada. | (2) aprovado: Gabarito confirmado (f(3/2) = 3*sqrt(2)).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado define claramente a PG, a proposta do colega a ser verificada, e as duas tarefas pedidas (correção da função e cálculo de f(3/2)). Não há ambiguidade lexical ou estrutural; a resolução explicita a distinção entre domínio discreto da PG e a extensão contínua da função, evitando confusão.
  - adequacao_nivel: 4/5 — A tarefa exige identificar por que a proposta do colega falha (diagnóstico de erro sistemático) e reconstruir a relação correta entre A, b e os termos da PG — isso é compatível com 'analisar' e com resposta relacional (SOLO), pois integra múltiplos elementos (razão, termo inicial, extensão da função) em vez de aplicar mecanicamente uma fórmula. Não chega a nível 5 porque, após a etapa de análise, a resolução final recai em substituição direta em fórmula já deduzida.
  - alinhamento_bncc: 5/5 — A questão articula PG e função exponencial em um único problema, exigindo que o aluno relacione termos discretos (a1, a2) com os parâmetros contínuos (A, b) e verifique a consistência da correspondência — exatamente o que a habilidade EM13MAT508 pede. O tratamento do domínio discreto é explícito (verificação em a1 e a2) e a extensão a x=3/2 reforça a distinção discreto/contínuo, sem descaracterizar a habilidade.
  - distratores: 5/5 — Os três distratores mapeiam erros conceituais plausíveis e distintos: manter a proposta errada do colega, confundir domínio discreto com índice arredondado, e trocar os papéis de A e b. Nenhum é absurdo ou eliminável por inspeção trivial.
  - originalidade: 4/5 — O uso de uma 'proposta equivocada de colega' para provocar análise crítica foge do formato mecânico de livro didático e evita o efeito Topaze parcial, pois o aluno precisa descobrir por si o motivo do erro em vez de seguir um roteiro guiado passo a passo. Poderia ganhar nota máxima com um contexto mais aplicado (não puramente formal-algébrico).
