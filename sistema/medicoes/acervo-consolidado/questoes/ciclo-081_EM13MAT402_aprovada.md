# Ciclo 081 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um professor de Física e um analista financeiro registraram duas situações reais.

**Situação 1 — Queda livre**
Um objeto é solto (sem velocidade inicial) do alto de um prédio. A distância percorrida $d$ (em metros) foi medida em função do tempo $t$ (em segundos):

| $t$ (s) | 1 | 2 | 3 |
|---|---|---|---|
| $d$ (m) | 5 | 20 | 45 |

**Situação 2 — Lucro de uma loja**
Uma loja varia o preço unitário $p$ (em reais) de um produto e registra o lucro mensal $L$ (em milhares de reais):

| $p$ (R\$) | 10 | 20 | 30 |
|---|---|---|---|
| $L$ (mil R\$) | 800 | 1200 | 800 |

Sabendo que, em ambos os casos, a grandeza da segunda linha é uma função polinomial do 2º grau da grandeza da primeira linha, resolva:

a) Determine a lei algébrica $d(t)$ e a lei algébrica $L(p)$ que descrevem cada situação.

b) Para cada função, identifique no plano cartesiano: as coordenadas do vértice da parábola, o sentido da concavidade e os pontos em que o gráfico intercepta os eixos coordenados.

c) Apenas uma das duas situações representa uma grandeza **diretamente proporcional ao quadrado** da outra. Diga qual é e justifique sua resposta usando dois argumentos: um algébrico (a forma da lei obtida em (a)) e um geométrico (a posição do gráfico em relação à origem do plano cartesiano).

## Gabarito

$d(t)=5t^2$, vértice $(0,0)$, concavidade para cima, parábola passando pela origem — diretamente proporcional a $t^2$. $L(p)=-4p^2+160p-400$, vértice $(20,1200)$, concavidade para baixo, intercepta o eixo $L$ em $(0,-400)$ e o eixo $p$ em $p=20\pm10\sqrt3$ — quadrática geral, não é proporcional ao quadrado de $p$. A situação diretamente proporcional ao quadrado é a Situação 1 (queda livre).

## Resolução

**Passo 1 — Montar o sistema para $d(t) = at^2+bt+c$**

Usando os pontos $(1,5)$, $(2,20)$ e $(3,45)$:

$a+b+c=5$
$4a+2b+c=20$
$9a+3b+c=45$

Subtraindo a 1ª da 2ª: $3a+b=15$. Subtraindo a 2ª da 3ª: $5a+b=25$. Subtraindo essas duas: $2a=10 \Rightarrow a=5$. Logo $b=15-3(5)=0$ e $c=5-5-0=0$.

$$d(t)=5t^2$$

**Passo 2 — Montar o sistema para $L(p) = ap^2+bp+c$**

Usando os pontos $(10,800)$, $(20,1200)$ e $(30,800)$:

$100a+10b+c=800$
$400a+20b+c=1200$
$900a+30b+c=800$

Subtraindo a 1ª da 2ª: $300a+10b=400 \Rightarrow 30a+b=40$.
Subtraindo a 2ª da 3ª: $500a+10b=-400 \Rightarrow 50a+b=-40$.
Subtraindo essas duas: $20a=-80 \Rightarrow a=-4$. Logo $b=40-30(-4)=160$ e $c=800-100(-4)-10(160)=800+400-1600=-400$.

$$L(p)=-4p^2+160p-400$$

Verificação: $L(10)=-400+1600-400=800$; $L(20)=-1600+3200-400=1200$; $L(30)=-3600+4800-400=800$. ✓

**Passo 3 — Elementos geométricos de $d(t)=5t^2$**

Como $b=c=0$, o vértice é $t_v=-\dfrac{b}{2a}=0$, $d(0)=0$, ou seja, vértice em $(0,0)$. Como $a=5>0$, a parábola tem concavidade voltada para cima. O gráfico passa pela origem e não intercepta o eixo $d$ em outro ponto nem o eixo $t$ em outro ponto (raiz dupla $t=0$).

**Passo 4 — Elementos geométricos de $L(p)=-4p^2+160p-400$**

Vértice: $p_v=-\dfrac{160}{2(-4)}=20$, $L(20)=-1600+3200-400=1200$, ou seja, vértice em $(20,1200)$. Como $a=-4<0$, a concavidade é voltada para baixo. Intersecção com o eixo $L$: $p=0 \Rightarrow L=-400$, ponto $(0,-400)$. Intersecções com o eixo $p$ (fazendo $L=0$): $-4p^2+160p-400=0 \Rightarrow p^2-40p+100=0 \Rightarrow p = 20\pm\sqrt{300} = 20\pm10\sqrt3$.

**Passo 5 — Distinguindo a proporcionalidade direta ao quadrado**

Uma grandeza $y$ é diretamente proporcional ao quadrado de $x$ quando $y=kx^2$, isto é, quando na forma $ax^2+bx+c$ temos $b=0$ e $c=0$. Isso ocorre apenas em $d(t)=5t^2$ (com $k=5$). Geometricamente, isso corresponde a uma parábola cujo vértice está exatamente na origem do plano cartesiano, o que é o caso de $d(t)$.

Já $L(p)=-4p^2+160p-400$ tem $b\neq 0$ e $c\neq 0$: é uma função quadrática geral, cujo vértice $(20,1200)$ está deslocado da origem — portanto $L$ **não** é diretamente proporcional a $p^2$.

**Conclusão:** apenas a Situação 1 (queda livre) representa uma grandeza diretamente proporcional ao quadrado da outra.

## Formalização verificável

- `funcao` — expressão `5*t**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-4*p**2 + 160*p - 400`, esperado `[20, 1200]`, parâmetros `{'consulta': 'vertice'}`
- `propriedade` — expressão `-`, esperado `5*t**2`, parâmetros `{'pontos': '[(1,5),(2,20),(3,45)]', 'grau': '2', 'forma': 'a*t**2'}`
- `propriedade` — expressão `-`, esperado `-4*p**2 + 160*p - 400`, parâmetros `{'pontos': '[(10,800),(20,1200),(30,800)]', 'grau': '2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (20, 1200)). | (3) aprovado: Propriedades confirmadas para 5*t**2: reproduz os 3 pontos dados; grau 2; forma a*t**2. | (4) aprovado: Propriedades confirmadas para -4*p**2 + 160*p - 400: reproduz os 3 pontos dados; grau 2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - propriedade=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Dados completos e organizados em tabelas, comandos (a, b, c) bem delimitados, sem ambiguidade lexical ou estrutural. O que é dado (pares de pontos) e o que é pedido (lei algébrica, elementos geométricos, classificação de proporcionalidade) estão explícitos.
  - adequacao_nivel: 4/5 — Os itens (a) e (b) correspondem bem ao nível 'aplicar' (montar sistema, calcular vértice/concavidade/interceptos). Porém o item (c) exige justificar com dois argumentos articulados (algébrico e geométrico) a distinção entre os dois casos, o que se aproxima de um processo de 'analisar' (SOLO relacional) mais do que de mera aplicação de fórmula. Isso não invalida a questão, mas cria leve descompasso com o nível Bloom declarado.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente as exigências da EM13MAT402: exige obter a lei algébrica a partir de dados numéricos (item a), converter essa lei em elementos geométricos no plano cartesiano — vértice, concavidade, interceptos (item b) — e, crucialmente, distinguir de forma justificada (algébrica e geometricamente) qual situação representa proporcionalidade direta ao quadrado (item c). Os dois temas (física e economia) são articulados num único problema comparativo, não apenas justapostos.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — Os contextos (queda livre e lucro em função do preço) são relativamente recorrentes em livros didáticos, mas a estrutura da tarefa — obter a lei via tabela, converter para geometria e comparar duas situações para decidir proporcionalidade — evita o formato mecânico de 'ache o vértice e as raízes'. Não há pistas evidentes que antecipem a resposta (efeito Topaze), pois o aluno precisa resolver o sistema antes de identificar b=c=0.
