# Ciclo 036 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma equipe de engenharia testa, em túnel de vento, a força de resistência do ar (F, em newtons) que atua sobre uma peça, variando a velocidade do ar (v, em m/s) incidente sobre ela. Os resultados obtidos estão na tabela abaixo:

| v (m/s) | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| F (N) | 3 | 12 | 27 | 48 |

Analisando os dados da tabela, qual expressão algébrica representa corretamente a força de resistência F em função da velocidade v?

## Alternativas

- (a) F = 3v²  ← correta
- (b) F = 3v
  - *erro representado:* Assumir proporcionalidade linear direta calculando a razão F/v apenas com o primeiro par (1,3) e generalizando sem checar que essa razão não é constante para os demais pontos da tabela.
- (c) F = 6v²
  - *erro representado:* Usar diretamente o valor da 2ª diferença finita constante (6) como coeficiente a da função quadrática, esquecendo que a = (2ª diferença)/2.
- (d) F = v² + 2
  - *erro representado:* Reconhecer que a relação é quadrática, mas assumir por padrão que o coeficiente a=1, ajustando apenas uma constante aditiva para acertar somente o primeiro valor da tabela, sem verificar os demais pontos.

## Gabarito

F(v) = 3v²

## Resolução

**Passo 1 — Testar proporcionalidade direta (linear):**

Calculamos a razão $\dfrac{F}{v}$ para cada par: $\dfrac{3}{1}=3$, $\dfrac{12}{2}=6$, $\dfrac{27}{3}=9$, $\dfrac{48}{4}=12$.

Como essa razão **não é constante**, a relação não é do tipo $F = av$ (não é linear/proporcional direta simples).

**Passo 2 — Analisar as diferenças sucessivas de F:**

$12-3=9$, $27-12=15$, $48-27=21$ (1ª diferença não é constante, confirmando que não é linear).

As diferenças dessas diferenças (2ª diferença): $15-9=6$ e $21-15=6$ — **constante**! Isso é a assinatura de uma função quadrática do tipo $y=ax^2+bx+c$.

**Passo 3 — Testar proporcionalidade ao quadrado de v:**

Calculamos $\dfrac{F}{v^2}$ para cada par: $\dfrac{3}{1}=3$, $\dfrac{12}{4}=3$, $\dfrac{27}{9}=3$, $\dfrac{48}{16}=3$.

A razão é **constante e igual a 3**, o que mostra que $F$ é diretamente proporcional a $v^2$, isto é, $F = 3v^2$ (sem termos lineares ou constantes, já que fisicamente quando $v=0$ não há resistência).

**Passo 4 — Verificar:**

$3(1)^2=3$ ✓, $3(2)^2=12$ ✓, $3(3)^2=27$ ✓, $3(4)^2=48$ ✓.

Logo, $F(v) = 3v^2$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*x**2`, parâmetros `{'pontos': '[(1,3),(2,12),(3,27),(4,48)]', 'grau': '2', 'forma': 'a*x**2'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Propriedades confirmadas para 3*x**2: reproduz os 4 pontos dados; grau 2; forma a*x**2.
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado especifica claramente o que é dado (tabela v-F) e o que se pede (expressão algébrica de F em função de v). Não há ambiguidade lexical ou estrutural, e os dados numéricos são suficientes para a análise pedida.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (testar razões F/v, calcular diferenças sucessivas, testar F/v², generalizar) corresponde a 'analisar' na taxonomia de Bloom, exigindo diferenciação entre hipóteses (linear vs. quadrática) e organização de evidências — compatível com estrutura relacional da SOLO. O formato de múltipla escolha limita um pouco a demonstração explícita do raciocínio analítico completo, mas os distratores exigem que o aluno tenha passado por etapas de análise para descartá-los.
  - alinhamento_bncc: 4/5 — A questão cumpre os requisitos centrais: dados apresentados em tabela (sem fórmula pronta), exige generalização algébrica do padrão, e conduz ao reconhecimento de que F é do tipo y=ax². Não solicita explicitamente a representação no plano cartesiano mencionada na habilidade, mas essa omissão é aceitável quando a questão foca no núcleo de generalização e identificação do tipo funcional, que é o aspecto central avaliado.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: (a) generalizar proporcionalidade linear a partir de um único par, (b) usar a 2ª diferença finita sem dividir por 2 (erro clássico de diferenças finitas), (c) assumir coeficiente a=1 e ajustar apenas uma constante aditiva verificando só o primeiro ponto. Nenhum é absurdo ou trivialmente eliminável sem cálculo.
  - originalidade: 4/5 — O contexto de resistência do ar em túnel de vento é aplicado e menos batido que exemplos genéricos de área/perímetro, embora a relação F∝v² seja um contexto físico já conhecido em livros didáticos de Física. A tabela não entrega pistas óbvias (como valores de v² explícitos), evitando efeito Topaze.
