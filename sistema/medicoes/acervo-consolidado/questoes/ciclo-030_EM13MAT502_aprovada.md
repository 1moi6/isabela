# Ciclo 030 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um engenheiro testa a queda livre de uma pequena esfera solta de um drone e mede a distância total percorrida pela esfera (em metros) para diferentes tempos de queda (em segundos), obtendo a tabela abaixo:

| Tempo $t$ (s) | Distância $d$ (m) |
|---|---|
| 1 | 5 |
| 2 | 20 |
| 3 | 45 |
| 4 | 80 |

a) Analisando os valores da tabela, identifique o padrão que relaciona $d$ e $t$ e escreva a lei algébrica que expressa $d$ em função de $t$.

b) Usando essa lei, determine a distância percorrida pela esfera após 5 segundos de queda.

## Gabarito

a) $d(t) = 5t^2$ (a distância é proporcional ao quadrado do tempo). b) $d(5) = 125$ m.

## Resolução

**Passo 1 — Investigar o padrão na tabela.**

Observe que $d$ não cresce na mesma proporção que $t$ (não é uma reta passando pela origem com razão constante $d/t$), pois:

$\dfrac{20}{5}=4$ mas $\dfrac{2}{1}=2$ — logo a relação não é linear simples ($d = kt$).

**Passo 2 — Testar a razão entre $d$ e $t^2$.**

Calculando $t^2$ para cada linha: $1, 4, 9, 16$.

Agora dividimos $d$ por $t^2$:

$\dfrac{5}{1}=5,\quad \dfrac{20}{4}=5,\quad \dfrac{45}{9}=5,\quad \dfrac{80}{16}=5$

A razão $d/t^2$ é constante e igual a $5$ em todos os casos.

**Passo 3 — Generalizar algebricamente.**

Como $\dfrac{d}{t^2}=5$ para todo par da tabela, concluímos que $d$ é diretamente proporcional ao quadrado de $t$, ou seja, a relação é do tipo $d = a\,t^2$, com $a=5$:

$$d(t) = 5t^2$$

Verificação: $d(1)=5(1)^2=5$; $d(2)=5(4)=20$; $d(3)=5(9)=45$; $d(4)=5(16)=80$. Todos conferem com a tabela.

**Passo 4 — Calcular a distância para $t=5$ s.**

$$d(5) = 5\cdot 5^2 = 5\cdot 25 = 125 \text{ m}$$

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*t**2`, parâmetros `{'pontos': '[(1,5),(2,20),(3,45),(4,80)]', 'grau': '2', 'forma': 'a*t**2'}`
- `funcao` — expressão `5*t**2`, esperado `125`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*t**2: reproduz os 4 pontos dados; grau 2; forma a*t**2. | (2) aprovado: Gabarito confirmado (f(5) = 125).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta os dados em tabela, define claramente as variáveis (tempo e distância) e separa nitidamente o que é pedido em (a) e (b). Não há ambiguidade lexical ou estrutural; os dados são suficientes para resolver ambos os itens.
  - adequacao_nivel: 4/5 — O item (a) exige identificar um padrão não linear a partir de dados numéricos e generalizar algebricamente, o que corresponde a um processo analítico (decompor a relação, testar razões, concluir proporcionalidade quadrática) e a uma resposta de nível relacional na taxonomia SOLO. O item (b), no entanto, é puramente aplicativo (substituição numérica), o que é aceitável como consolidação, mas reduz um pouco o peso analítico do conjunto. Os valores da tabela são 'perfeitos' (razão exata 5 em t²), o que facilita bastante a tarefa e pode tornar o processo mais mecânico do que genuinamente investigativo.
  - alinhamento_bncc: 4/5 — A questão cumpre os requisitos centrais da especificação: dados chegam como tabela, a expressão algébrica não é dada previamente, pede-se a generalização e ela conduz ao reconhecimento de d=at². Falta, porém, qualquer menção à representação no plano cartesiano, que é parte explícita do texto da habilidade EM13MAT502 (embora não estivesse listada como exigência obrigatória na especificação do professor, sua ausência é uma lacuna em relação à habilidade integral).
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — O contexto de queda livre com dados que reproduzem exatamente a lei d=5t² é um exemplo clássico e previsível (aproximação simplificada da queda livre), amplamente encontrado em livros didáticos. Não há efeito Topázio explícito, mas a estrutura 'tabela com t² óbvio, resultado exato 5' antecipa fortemente o caminho de resolução, reduzindo o desafio investigativo genuíno.
  - *sugestões:* Para fortalecer a questão: (1) inserir um pequeno pedido de representação gráfica dos pontos no plano cartesiano antes de generalizar, alinhando-se integralmente ao texto da habilidade EM13MAT502; (2) usar valores de d que não resultem exatamente em números inteiros na razão d/t² (ex.: pequenas variações experimentais) para exigir maior raciocínio analítico e evitar que o padrão seja percebido de forma imediata; (3) tornar o contexto menos padronizado, por exemplo variando o cenário (não a clássica queda livre) ou pedindo que o estudante compare duas possíveis leis (linear vs. quadrática) antes de decidir qual se ajusta aos dados, tornando o processo de análise mais explícito e menos mecânico.
