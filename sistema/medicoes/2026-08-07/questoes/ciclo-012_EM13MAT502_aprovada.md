# Ciclo 012 — EM13MAT502

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um engenheiro está estudando o movimento de um objeto em queda livre, medindo a distância total percorrida a partir do instante em que é solto. Ele registrou os seguintes dados em um experimento:

| Tempo decorrido $t$ (s) | Distância percorrida $d$ (m) |
|---|---|
| 1 | 5 |
| 2 | 20 |
| 3 | 45 |
| 4 | 80 |

a) Analisando os pares $(t, d)$ da tabela, investigue como $d$ varia em relação a $t$ e identifique o padrão numérico existente entre essas grandezas.

b) A partir desse padrão, escreva a expressão algébrica que generaliza $d$ em função de $t$, justificando por que essa relação é do tipo $d = a t^2$ (e não uma relação linear, por exemplo).

c) Usando a expressão obtida, determine a distância percorrida pelo objeto após $t = 6$ s de queda.

## Gabarito

d(t) = 5t², com d(6) = 180 m

## Resolução

**Passo 1 — Testar se a relação é linear (proporcional a $t$)**

Calculando a razão $\dfrac{d}{t}$ para cada par:

$\dfrac{5}{1}=5$, $\dfrac{20}{2}=10$, $\dfrac{45}{3}=15$, $\dfrac{80}{4}=20$

Essa razão não é constante — ela cresce, o que indica que $d$ **não** é diretamente proporcional a $t$ (não é uma função do 1º grau do tipo $d = kt$).

**Passo 2 — Testar a razão entre $d$ e $t^2$**

Calculando $t^2$ para cada valor de $t$: $1, 4, 9, 16$.

Agora a razão $\dfrac{d}{t^2}$:

$\dfrac{5}{1}=5$, $\dfrac{20}{4}=5$, $\dfrac{45}{9}=5$, $\dfrac{80}{16}=5$

Essa razão é **constante e igual a 5**. Isso mostra que $d$ é proporcional ao **quadrado** de $t$, ou seja, a relação é do tipo:

$$d = a\,t^2$$

com $a = 5$.

**Passo 3 — Escrever a lei de formação**

$$d(t) = 5t^2$$

Verificação com os dados da tabela: $d(1)=5$, $d(2)=20$, $d(3)=45$, $d(4)=80$ — todos conferem.

**Passo 4 — Calcular a distância em $t = 6$ s**

$$d(6) = 5\cdot 6^2 = 5\cdot 36 = 180 \text{ m}$$

**Resposta final:** a lei de formação é $d(t) = 5t^2$, e a distância percorrida em $t=6$ s é **180 m**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*t**2`, parâmetros `{'pontos': '[(1,5),(2,20),(3,45),(4,80)]', 'grau': '2', 'forma': 'a*t**2'}`
- `funcao` — expressão `5*t**2`, esperado `180`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*t**2: reproduz os 4 pontos dados; grau 2; forma a*t**2. | (2) aprovado: Gabarito confirmado (f(6) = 180).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é claro: apresenta a tabela de dados, delimita três subitens com comandos precisos (investigar, generalizar, calcular) e não deixa dúvidas sobre o que é pedido em cada etapa.
  - adequacao_nivel: 4/5 — Os itens (a) e (b) exigem efetivamente análise — comparar hipóteses (linear vs. quadrática), justificar a escolha do modelo — compatível com o nível 'analisar' e com resposta relacional na SOLO. O item (c), porém, é de mera aplicação (substituir valor), o que dilui um pouco a exigência cognitiva do conjunto, embora não comprometa o núcleo analítico da questão.
  - alinhamento_bncc: 4/5 — Cumpre as três exigências centrais listadas: dados em tabela, expressão algébrica não fornecida, e condução ao reconhecimento de d=at². Falta, porém, contemplar a representação no plano cartesiano mencionada no texto da habilidade EM13MAT502, o que deixa a habilidade parcialmente trabalhada.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — O contexto de queda livre com d=5t² é um exemplo clássico e recorrente em livros didáticos de física/matemática, pouco original. A condução da resolução (testar d/t e depois d/t²) é o caminho padrão esperado, sem inovação de abordagem ou contexto alternativo.
  - *sugestões:* Para elevar a qualidade: (1) incluir um subitem pedindo a representação gráfica dos pares (t,d) no plano cartesiano, completando a habilidade EM13MAT502 na íntegra; (2) substituir o contexto de queda livre por um cenário menos padronizado (ex.: crescimento de área de uma mancha, custo de material em função do lado de um quadrado) para aumentar a originalidade; (3) considerar remover ou reformular o item (c) para exigir uma nova análise (por exemplo, comparar com outro conjunto de dados) em vez de apenas substituição numérica, mantendo o nível 'analisar' em todos os itens.
