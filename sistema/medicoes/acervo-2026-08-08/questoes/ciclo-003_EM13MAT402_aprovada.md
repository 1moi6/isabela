# Ciclo 003 — EM13MAT402

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Duas empresas testam sistemas de queda controlada de drones e registram a distância percorrida na queda, $d$ (em metros), em função do tempo de voo $t$ (em segundos), com $t \geq 0$:

- Drone A (solto em queda livre, sem qualquer impulso antes do início da contagem do tempo): $d_A(t) = 4t^2$

- Drone B (recebeu um pequeno empurrão para baixo antes de $t=0$, de modo que já havia percorrido 6 m de queda no instante em que o cronômetro começou a contar): $d_B(t) = 4t^2 + 6$

a) Esboce, no mesmo plano cartesiano $(t, d)$, os gráficos de $d_A$ e $d_B$ para $t \geq 0$, indicando claramente as coordenadas do vértice de cada parábola.

b) Calcule $d_A(0)$ e $d_B(0)$. Com base apenas nesses valores, diga qual das duas funções, $d_A$ ou $d_B$, é diretamente proporcional ao quadrado do tempo, e justifique.

c) Responda com sim ou não, justificando brevemente cada resposta: as duas parábolas têm a mesma concavidade? O vértice de $d_B$ está na origem do plano cartesiano?

## Gabarito

d_A é diretamente proporcional a t² (vértice na origem, d_A(0)=0); d_B não é (vértice em (0,6), d_B(0)=6). Ambas têm mesma concavidade (a=4>0), mas apenas o vértice de d_A está na origem.

## Resolução

**a) Esboço dos gráficos**

Como o coeficiente de $t^2$ é positivo ($a=4$) em ambas as funções, as duas parábolas têm concavidade voltada para cima. Como estamos restritos a $t \geq 0$, desenha-se apenas o ramo direito de cada parábola.

- Para $d_A(t) = 4t^2$: o vértice é o ponto $(0,0)$, pois não há termo linear nem constante. A parábola parte da origem e cresce: $d_A(1) = 4$, $d_A(2) = 16$.

- Para $d_B(t) = 4t^2 + 6$: como não há termo em $t$, o vértice também ocorre em $t=0$, mas $d_B(0) = 6$. Logo o vértice é $(0,6)$. A parábola tem o mesmo formato de $d_A$, porém deslocada 6 unidades para cima: $d_B(1) = 10$, $d_B(2) = 22$.

No plano, as duas curvas são parábolas idênticas em formato, sendo a de $d_B$ a translação vertical da de $d_A$ em 6 unidades.

**b) Valores em $t=0$ e identificação da proporcionalidade**

$d_A(0) = 4(0)^2 = 0$

$d_B(0) = 4(0)^2 + 6 = 6$

Uma grandeza é diretamente proporcional ao quadrado de outra quando a razão $d(t)/t^2$ é constante para todo $t$, o que exige $d(0) = 0$ (a reta/curva deve passar pela origem). Como $d_A(0) = 0$, temos $d_A(t)/t^2 = 4$ para todo $t>0$: $d_A$ é diretamente proporcional a $t^2$.

Já $d_B(0) = 6 \neq 0$, então $d_B(t)/t^2$ não é constante (por exemplo, $d_B(1)/1^2 = 10$ e $d_B(2)/2^2 = 5{,}5$). Logo, $d_B$ **não** é diretamente proporcional ao quadrado do tempo.

**c) Comparação geométrica**

- Mesma concavidade? **Sim**, pois ambas têm $a = 4 > 0$, logo as duas parábolas abrem para cima com a mesma "abertura".

- O vértice de $d_B$ está na origem? **Não**, o vértice de $d_B$ é $(0,6)$, deslocado verticalmente em relação à origem, enquanto o vértice de $d_A$, esse sim, está na origem $(0,0)$.

## Formalização verificável

- `funcao` — expressão `4*t**2`, esperado `[0, 0]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `4*t**2 + 6`, esperado `[0, 6]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `4*t**2`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `4*t**2 + 6`, esperado `Interval(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `propriedade` — expressão `-`, esperado `4*t**2`, parâmetros `{'forma': 'a*t**2', 'pontos': '[(0,0),(1,4),(2,16)]'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (-3/5, -9/5)). | (3) aprovado: Propriedades confirmadas para 5*t**2: reproduz os 3 pontos dados; grau 2; forma a*t**2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - propriedade=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente as duas funções, especifica que devem ser tratadas como parábolas completas (mesmo fora do domínio físico) e delimita com precisão o que é pedido em cada item (vértice/eixo, identificação da proporcionalidade, descrição geométrica). Não há ambiguidade lexical ou estrutural; os dados são suficientes.
  - adequacao_nivel: 2/5 — O nível de Bloom declarado é 'entender', mas o processo efetivamente exigido é muito superior: o item (b) pede que o aluno justifique/explique por que a posição do vértice indica proporcionalidade (relação causal entre conceitos), e o item (c) exige comparação relacional entre duas estruturas geométricas sem apoio numérico adicional. Na taxonomia SOLO, isso corresponde a nível relacional, não a uma simples restatação ou reconhecimento ('entender'). Há incoerência entre o nível declarado e o nível real de exigência cognitiva.
  - alinhamento_bncc: 4/5 — A questão cumpre as duas exigências centrais: (i) exige trânsito entre álgebra e geometria, pois o vértice numérico do item (a) é reaproveitado no item (b) para justificar a proporcionalidade via posição geométrica, e o item (c) pede descrição puramente geométrica sem novos cálculos; (ii) distingue explicitamente o caso proporcional ($d_A$) do não proporcional ($d_B$), articulando os dois conceitos em um único problema físico coerente, em vez de justapor itens isolados. Poderia reforçar ainda mais a exigência de 'conversão' pedindo explicitamente um esboço ou construção gráfica, mas o texto já garante a articulação exigida pela habilidade.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O contexto de queda livre é um clássico da Física, mas o tratamento matemático — analisar as parábolas fora do domínio físico e usar a posição do vértice como critério de proporcionalidade — é um recorte pouco comum em livros didáticos, evitando o enunciado-padrão de 'encontre o vértice'. Há leve efeito Topaze no item (b), pois o enunciado já indica que 'a posição do vértice permite reconhecer' a proporcionalidade, entregando parte do raciocínio esperado em vez de deixar o aluno descobrir essa relação.
  - *sugestões:* Ajustar a coerência entre o nível de Bloom declarado e a exigência real da questão. Duas opções: (1) Elevar o nível declarado de 'entender' para 'analisar' ou 'relacionar', já que os itens (b) e (c) exigem justificativa causal e comparação relacional entre representações algébrica e geométrica — isso é coerente com a riqueza da questão, que é boa e não deveria ser simplificada. (2) Caso se queira manter o nível 'entender', simplificar os itens (b) e (c): por exemplo, transformar (b) em uma pergunta de reconhecimento direto ('Qual das duas é proporcional a t²? Justifique apenas com o valor de d(0).') e reduzir (c) a uma comparação binária simples (mesma concavidade? sim/não; vértice na origem? sim/não), sem exigir a construção do argumento geométrico completo. Também recomenda-se reduzir a pista explícita em (b) ('a posição do vértice permite reconhecer') para preservar melhor a autonomia do aluno na descoberta da relação (evitar efeito Topaze).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Ajustar a coerência entre o nível de Bloom declarado e a exigência real da questão. Duas opções: (1) Elevar o nível declarado de 'entender' para 'analisar' ou 'relacionar', já que os itens (b) e (c) exigem justificativa causal e comparação relacional entre representações algébrica e geométrica — isso é coerente com a riqueza da questão, que é boa e não deveria ser simplificada. (2) Caso se queira manter o nível 'entender', simplificar os itens (b) e (c): por exemplo, transformar (b) em uma pergunta de reconhecimento direto ('Qual das duas é proporcional a t²? Justifique apenas com o valor de d(0).') e reduzir (c) a uma comparação binária simples (mesma concavidade? sim/não; vértice na origem? sim/não), sem exigir a construção do argumento geométrico completo. Também recomenda-se reduzir a pista explícita em (b) ('a posição do vértice permite reconhecer') para preservar melhor a autonomia do aluno na descoberta da relação (evitar efeito Topaze).

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (0, 0)). | (2) aprovado: Gabarito confirmado (vértice calculado (0, 6)). | (3) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (4) aprovado: Gabarito confirmado (domínio Interval(0, oo) — restrição de contexto dentro do domínio máximo Reals). | (5) aprovado: Propriedades confirmadas para 4*t**2: reproduz os 3 pontos dados; forma a*t**2.
  - funcao/vertice=aprovado
  - funcao/vertice=aprovado
  - funcao/dominio=aprovado
  - funcao/dominio=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com contexto claro, dados completos (funções, domínio t≥0) e comandos precisos em a), b) e c). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O nível 'entender' é majoritariamente respeitado: esboçar gráfico e identificar proporcionalidade são tarefas de compreensão/interpretação, sem exigir análise complexa. A estrutura SOLO é predominantemente multiestrutural (múltiplos elementos: vértice, valores, concavidade, proporcionalidade), coerente com 'entender'. Pequeno ponto de atenção: o item c) pede justificativa, o que aproxima-se de 'analisar', mas as justificativas exigidas são simples e diretas, não comprometendo a adequação geral.
  - alinhamento_bncc: 5/5 — A questão cumpre integralmente as exigências: exige trânsito entre forma algébrica (equações de d_A e d_B) e representação geométrica (esboço com vértices) no item a); no item b) leva explicitamente à distinção entre proporcionalidade direta ao quadrado do tempo (d_A) e não-proporcionalidade (d_B), fundamentando a partir da posição do vértice/valor em t=0; o item c) reforça essa articulação geometricamente (concavidade e vértice na origem). Os dois aspectos exigidos pela habilidade — trânsito algébrico-geométrico e distinção de proporcionalidade — estão articulados num único problema coeso, não apenas justapostos.
  - distratores: 5/5 — Não se aplica: questão discursiva, sem alternativas de múltipla escolha.
  - originalidade: 4/5 — O contexto de queda de drones com impulso prévio é razoavelmente significativo e evita o clichê do 'objeto em queda livre' puro, embora ainda seja uma variação previsível de problemas de cinemática/MRUV. Não há efeito Topaze evidente: as perguntas não entregam a resposta, exigindo que o aluno construa a justificativa a partir dos valores calculados. Poderia ganhar mais originalidade com dados de um contexto menos didático-padrão (ex.: dados reais ou tabela).
