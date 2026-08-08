# Ciclo 089 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma progressão geométrica (PG) de termos positivos e crescente satisfaz simultaneamente as condições $a_2 \cdot a_5 = 32$ e $a_3 + a_4 = 12$, em que $a_n$ denota o $n$-ésimo termo da progressão. Sabe-se que essa PG corresponde à restrição, ao conjunto $\mathbb{N}^*$, de uma função exponencial da forma $f(x) = a \cdot q^{x-1}$, com $a>0$ e $q>0$, tal que $f(n) = a_n$ para todo $n \in \mathbb{N}^*$.

Determine a lei da função exponencial $f$ que representa essa PG, especificando corretamente o seu domínio, e calcule o valor do décimo termo da progressão, $a_{10}$.

## Alternativas

- (a) $f(x) = 2^{x-1}$, com domínio $\mathbb{N}^*$, e $a_{10} = 512$.  ← correta
- (b) $f(x) = 2^{x}$, com domínio $\mathbb{N}^*$, e $a_{10} = 1024$.
  - *erro representado:* Erro de indexação do termo geral: usar expoente $x$ em vez de $x-1$, como se $a_1$ correspondesse a $f(1)=q^1$ em vez de $q^0$.
- (c) $f(x) = 2^{x-1}$, com domínio $\mathbb{R}$, e $a_{10} = 512$.
  - *erro representado:* Ignorar que a função que representa a PG deve ter domínio discreto ($\mathbb{N}^*$), tratando-a como se fosse a função exponencial usual de domínio real, sem restringir aos índices naturais.
- (d) $f(x) = 2x$, com domínio $\mathbb{N}^*$, e $a_{10} = 20$.
  - *erro representado:* Confundir progressão geométrica com progressão aritmética, representando a sequência por uma função afim (linear) em vez de exponencial.

## Gabarito

A

## Resolução

**Passo 1 — Escrever os termos em função de $a_1$ e $q$.**

Seja $a_1 = a$ e razão $q$. Então $a_2 = aq$, $a_3=aq^2$, $a_4=aq^3$, $a_5=aq^4$.

**Passo 2 — Montar as equações dadas.**

$a_2\cdot a_5 = (aq)(aq^4)=a^2q^5=32$

$a_3+a_4 = aq^2+aq^3 = aq^2(1+q)=12$

**Passo 3 — Isolar $a$ na segunda equação e substituir na primeira.**

Da segunda equação: $a = \dfrac{12}{q^2(1+q)}$.

Substituindo em $a^2q^5=32$:

$\left(\dfrac{12}{q^2(1+q)}\right)^2 q^5 = 32 \;\Rightarrow\; \dfrac{144\,q}{(1+q)^2}=32$

$144q = 32(1+q)^2 = 32+64q+32q^2$

$32q^2-80q+32=0 \;\Rightarrow\; 2q^2-5q+2=0$

**Passo 4 — Resolver a equação do segundo grau.**

$q=\dfrac{5\pm\sqrt{25-16}}{4}=\dfrac{5\pm3}{4}\;\Rightarrow\; q=2 \text{ ou } q=\tfrac12$

Como a PG é **crescente** (termos positivos e crescentes), descartamos $q=\tfrac12$ e ficamos com $q=2$.

**Passo 5 — Determinar $a_1$.**

$a = \dfrac{12}{q^2(1+q)} = \dfrac{12}{4\cdot 3} = 1$

Logo a PG é $1, 2, 4, 8, 16, \dots$, com $a_1=1$ e $q=2$.

**Passo 6 — Associar a PG à função exponencial.**

O termo geral da PG é $a_n = a_1\cdot q^{n-1} = 2^{n-1}$. Essa é exatamente a lei $f(x)=a\cdot q^{x-1}$ com $a=1$ e $q=2$, ou seja:

$$f(x) = 2^{x-1}$$

Como $a_n$ só está definido para índices naturais positivos (não faz sentido, por exemplo, o "termo $1{,}5$" da progressão), a função que efetivamente representa a PG tem **domínio $\mathbb{N}^*$**, e não $\mathbb{R}$. A função exponencial de domínio real $2^{x-1}$ é uma extensão contínua útil para estudar o comportamento da PG (crescimento), mas não é ela mesma a sequência.

**Passo 7 — Calcular $a_{10}$.**

$a_{10} = f(10) = 2^{10-1} = 2^9 = 512$

**Conclusão:** $f(x)=2^{x-1}$, com domínio $\mathbb{N}^*$, e $a_{10}=512$.

## Formalização verificável

- `equacao` — expressão `Eq(2*q**2 - 5*q + 2, 0)`, esperado `[Rational(1,2), 2]`
- `progressao` — expressão `-`, esperado `512`, parâmetros `{'tipo_progressao': 'pg', 'a1': '1', 'razao': '2', 'n': '10', 'consulta': 'termo'}`
- `funcao` — expressão `2**(x-1)`, esperado `512`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `funcao` — expressão `2**(x-1)`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (termo da PG = 512). | (3) aprovado: Gabarito confirmado (f(10) = 512). | (4) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)).
  - equacao=aprovado
  - progressao/termo=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado define claramente os dados (a2·a5=32, a3+a4=12) e a condição f(n)=a_n para n∈N*, o que resolve a ambiguidade sobre qual seria o domínio 'correto' de f. Ainda assim, a distinção entre 'domínio N*' e 'domínio R' pode gerar dúvida em alunos menos atentos à definição formal dada, pois na prática livros didáticos costumam tratar a lei a·q^(x-1) como extensível a R sem maiores ressalvas.
  - adequacao_nivel: 4/5 — O processo exigido (montar e resolver sistema não-linear, identificar razão e termo inicial, escrever a lei da função e justificar o domínio) é compatível com 'aplicar', com componente relacional (SOLO) ao integrar PG e função exponencial. Está no limite superior de 'aplicar', quase tangenciando 'analisar' pela exigência de justificar o domínio, mas isso é coerente com a dificuldade declarada 'difícil'.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente a exigência da especificação: obriga o aluno a associar a PG à função exponencial de domínio discreto, não apenas aplicar a fórmula do termo geral. A discussão explícita sobre domínio N* vs R no gabarito e nos distratores mostra que essa articulação é central ao problema, não periférica.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: erro de indexação do expoente, erro conceitual sobre domínio discreto, e confusão entre PG e PA. Nenhum é absurdo ou trivialmente eliminável por inspeção superficial.
  - originalidade: 4/5 — Embora o contexto seja puramente teórico (sem aplicação real), o enunciado evita a formulação mecânica típica de livros didáticos ao inserir a reflexão sobre domínio da função exponencial associada à PG, que é um ponto pouco explorado na maioria dos exercícios tradicionais. Não há pistas que pavimentem a solução (efeito Topaze).
