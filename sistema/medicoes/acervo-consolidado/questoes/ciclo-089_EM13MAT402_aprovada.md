# Ciclo 089 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma função quadrática $y = ax^2 + bx + c$ (com $a \neq 0$) representa uma relação em que $y$ é diretamente proporcional ao quadrado de $x$ quando existe uma constante $k \neq 0$ tal que $y = kx^2$ para todo $x$ real — ou seja, quando $b = 0$ e $c = 0$ simultaneamente.

Considere quatro parábolas, todas com concavidade voltada para cima, esboçadas no plano cartesiano e descritas apenas por características geométricas de seus gráficos:

- **Parábola A**: intercepta o eixo $x$ nos pontos $(0,0)$ e $(4,0)$, e passa pelo ponto $(1,-3)$.
- **Parábola B**: tangencia o eixo $x$ exatamente no ponto $(0,0)$ — esse ponto é o vértice da parábola — e passa pelo ponto $(3,18)$.
- **Parábola C**: intercepta o eixo $x$ nos pontos $(-3,0)$ e $(3,0)$, e passa pelo ponto $(1,-8)$.
- **Parábola D**: tangencia o eixo $x$ exatamente no ponto $(2,0)$ — esse ponto é o vértice da parábola — e passa pelo ponto $(0,8)$.

Assinale a alternativa que identifica corretamente qual das parábolas descritas representa uma função em que $y$ é diretamente proporcional ao quadrado de $x$.

## Alternativas

- (a) Parábola A, pois seu gráfico passa pela origem do plano cartesiano.
  - *erro representado:* Confundir 'o gráfico passar pela origem' com 'ser diretamente proporcional ao quadrado', ignorando que existe uma segunda raiz distinta de zero (x=4), o que mostra que o vértice não está na origem.
- (b) Parábola B, pois seu vértice está na origem e ela não possui termo linear nem constante.  ← correta
- (c) Parábola C, pois seu gráfico é simétrico em relação ao eixo y.
  - *erro representado:* Confundir a simetria em relação ao eixo y (que garante apenas b=0) com a proporcionalidade direta ao quadrado, ignorando que o gráfico está deslocado verticalmente (c=-9≠0), com vértice em (0,-9) e não na origem.
- (d) Parábola D, pois seu gráfico tangencia o eixo x em um único ponto.
  - *erro representado:* Acreditar que a tangência ao eixo x (raiz dupla) já garante a proporcionalidade direta, sem verificar que o ponto de tangência precisa ser exatamente a origem — aqui a tangência ocorre em (2,0).

## Gabarito

Alternativa (b): Parábola B, pois $y=2x^2$, com vértice na origem, $b=0$ e $c=0$.

## Resolução

**Ideia-chave:** $y$ é diretamente proporcional a $x^2$ somente quando a equação da parábola é $y=kx^2$, isto é, quando $b=0$ **e** $c=0$ ao mesmo tempo — geometricamente, isso significa que o **vértice está exatamente na origem**. Passar pela origem, ou ser simétrica em relação ao eixo $y$, ou tangenciar o eixo $x$ em um único ponto **não bastam isoladamente**.

**Parábola A** — raízes em $x=0$ e $x=4$: $y=a\,x(x-4)$. Usando $(1,-3)$: $a(1)(1-4)=-3a=-3 \Rightarrow a=1$. Logo $y=x^2-4x$, com $b=-4\neq 0$. Embora passe pela origem, **não** é proporcional (a outra raiz, $x=4$, mostra que o vértice não está em $(0,0)$).

**Parábola B** — vértice (tangência) em $(0,0)$, logo raiz dupla em $x=0$: $y=a x^2$. Usando $(3,18)$: $9a=18 \Rightarrow a=2$. Logo $y=2x^2$, com $b=0$ e $c=0$. **É** diretamente proporcional, com $k=2$.

**Parábola C** — raízes em $x=-3$ e $x=3$: $y=a(x-3)(x+3)=ax^2-9a$. Usando $(1,-8)$: $a-9a=-8a=-8 \Rightarrow a=1$. Logo $y=x^2-9$: aqui $b=0$ (é simétrica em relação ao eixo $y$), mas $c=-9\neq 0$, então o vértice é $(0,-9)$, **não** a origem. Não é proporcional.

**Parábola D** — vértice (tangência) em $(2,0)$: $y=a(x-2)^2$. Usando $(0,8)$: $4a=8 \Rightarrow a=2$. Logo $y=2x^2-8x+8$, com $b=-8\neq0$ e $c=8\neq0$. Apesar de tangenciar o eixo $x$ em um único ponto (raiz dupla), essa tangência ocorre em $(2,0)$ e não na origem, então **não** é proporcional.

**Conclusão:** apenas a Parábola B tem simultaneamente $b=0$ e $c=0$ (vértice na origem), logo é a única cuja lei é $y=kx^2$, isto é, $y$ diretamente proporcional a $x^2$.

## Formalização verificável

- `funcao` — expressão `x**2 - 4*x`, esperado `[0, 4]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `x**2 - 4*x`, esperado `-3`, parâmetros `{'consulta': 'valor', 'ponto': '1'}`
- `funcao` — expressão `2*x**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `2*x**2`, esperado `18`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `x**2 - 9`, esperado `[-3, 3]`, parâmetros `{'consulta': 'zeros'}`
- `funcao` — expressão `x**2 - 9`, esperado `-8`, parâmetros `{'consulta': 'valor', 'ponto': '1'}`
- `funcao` — expressão `2*x**2 - 8*x + 8`, esperado `[2, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `2*x**2 - 8*x + 8`, esperado `8`, parâmetros `{'consulta': 'valor', 'ponto': '0'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 8 afirmações conferidas. (1) aprovado: Gabarito confirmado (zeros da função: [0, 4]). | (2) aprovado: Gabarito confirmado (f(1) = -3). | (3) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (4) aprovado: Gabarito confirmado (f(3) = 18). | (5) aprovado: Gabarito confirmado (zeros da função: [-3, 3]). | (6) aprovado: Gabarito confirmado (f(1) = -8). | (7) aprovado: Gabarito confirmado (vértice calculado (2, 0)). | (8) aprovado: Gabarito confirmado (f(0) = 8).
  - funcao/zeros=aprovado
  - funcao/valor=aprovado
  - funcao/vertice=aprovado
  - funcao/valor=aprovado
  - funcao/zeros=aprovado
  - funcao/valor=aprovado
  - funcao/vertice=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é preciso: define claramente o conceito de proporcionalidade direta ao quadrado, especifica os dados de cada parábola (interceptos, ponto de tangência, ponto adicional) e a pergunta é inequívoca. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — O processo cognitivo real exigido ultrapassa 'entender': o aluno precisa montar a equação da parábola a partir de dados geométricos, resolver para o coeficiente 'a' usando o ponto extra, e só então comparar com o critério b=0 e c=0 em quatro casos — isso é 'aplicar' e 'analisar' na taxonomia de Bloom, e a estrutura de resposta é relacional (compara quatro casos simultaneamente), não meramente compreensiva. Há descompasso entre o nível declarado (entender) e o nível efetivamente demandado.
  - alinhamento_bncc: 4/5 — A questão exige converter descrições geométricas (raízes, ponto de tangência, ponto adicional) em representações algébricas (y=ax²+bx+c) e usa isso para distinguir qual caso é diretamente proporcional ao quadrado, cumprindo as duas exigências centrais da habilidade. O único ponto fraco é que a definição do critério (b=0 e c=0) já é fornecida pronta no enunciado, reduzindo parcialmente a exigência de o próprio aluno construir essa distinção a partir da geometria (ele só verifica uma regra já dada).
  - distratores: 5/5 — Cada distrator corresponde a um erro conceitual plausível e comum: confundir 'passar pela origem' com proporcionalidade (A), confundir simetria em relação ao eixo y com proporcionalidade (C), e confundir tangência ao eixo x em ponto qualquer com proporcionalidade (D). Nenhum é trivialmente eliminável sem compreensão do conceito.
  - originalidade: 3/5 — A estrutura comparativa com quatro parábolas é mais elaborada que o exercício padrão de livro didático, mas o contexto é puramente formal/abstrato, sem significância além do exercício algébrico-geométrico. Além disso, o enunciado fornece explicitamente a condição algébrica (b=0 e c=0) que resolve o problema, configurando um efeito Topaze: o aluno não precisa deduzir por si mesmo o critério de proporcionalidade, apenas aplicá-lo mecanicamente a cada caso.
