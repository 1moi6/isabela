# Ciclo 002 — EM13MAT305

- **Situação:** aprovada
- **Temas:** funcao_logaritmica
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

A magnitude $M$ de um abalo sísmico, na escala Richter, pode ser calculada a partir da energia $E$ (em joules) liberada pelo abalo por meio da função logarítmica:

$$M(E) = \dfrac{\log_{10}(E) - 4{,}8}{1{,}5}$$

a) Calcule a magnitude de um abalo que libera uma energia $E = 10^{9{,}3}$ J.

b) Considere dois abalos sísmicos, de magnitudes $M_1$ e $M_2$, com $M_2 = M_1 + 1$ (ou seja, um grau a mais na escala Richter). Usando a fórmula dada, determine, em termos de uma razão numérica constante, quantas vezes a energia liberada pelo abalo de magnitude $M_2$ é maior do que a liberada pelo abalo de magnitude $M_1$. Mostre que essa razão não depende do valor de $M_1$.

c) Agora é sua vez de elaborar um problema. Escolha um dos contextos citados na literatura de escalas logarítmicas — a acidez de uma solução (pH) ou a desintegração radioativa de um elemento — e construa uma função logarítmica original que relacione duas grandezas desse contexto (por exemplo, concentração de íons $H^+$ e pH, ou quantidade de massa restante e tempo decorrido). Defina claramente os parâmetros da sua função e formule uma pergunta que exija do leitor interpretar como a variação de uma grandeza (por exemplo, dobrar, triplicar ou aumentar em uma unidade) afeta a outra. Em seguida, resolva a pergunta que você mesmo formulou.

## Gabarito

a) $M = 3$. b) A razão é constante e igual a $10^{1,5} = 10\sqrt{10} \approx 31{,}6$, ou seja, cada acréscimo de 1 na magnitude multiplica a energia por aproximadamente 31,6, independentemente do valor de $M_1$. c) Resposta pessoal (aberta), avaliada pelos critérios: contexto realista, função logarítmica coerente, pergunta sobre variação de grandeza e resolução correta.

## Resolução

**a) Cálculo da magnitude**

Substituindo $E = 10^{9{,}3}$ na fórmula:

$$M = \dfrac{\log_{10}(10^{9{,}3}) - 4{,}8}{1{,}5}$$

Como $\log_{10}(10^{9{,}3}) = 9{,}3$ (propriedade do logaritmo na base da potência):

$$M = \dfrac{9{,}3 - 4{,}8}{1{,}5} = \dfrac{4{,}5}{1{,}5} = 3$$

Logo, $M = 3$.

**b) Razão entre as energias para uma variação de 1 grau na magnitude**

Da fórmula original, isolamos $E$ em função de $M$:

$$M = \dfrac{\log_{10}(E) - 4{,}8}{1{,}5} \;\Rightarrow\; \log_{10}(E) = 1{,}5\,M + 4{,}8 \;\Rightarrow\; E = 10^{1{,}5\,M + 4{,}8}$$

Para $M_1$ e $M_2 = M_1 + 1$:

$$\log_{10}(E_1) = 1{,}5\,M_1 + 4{,}8$$
$$\log_{10}(E_2) = 1{,}5\,(M_1+1) + 4{,}8 = 1{,}5\,M_1 + 1{,}5 + 4{,}8$$

Subtraindo as duas equações (propriedade do logaritmo do quociente):

$$\log_{10}(E_2) - \log_{10}(E_1) = 1{,}5 \;\Rightarrow\; \log_{10}\left(\dfrac{E_2}{E_1}\right) = 1{,}5$$

$$\dfrac{E_2}{E_1} = 10^{1{,}5} = 10\sqrt{10} \approx 31{,}6$$

Como essa razão não depende de $M_1$ (ele foi cancelado na subtração), concluímos que **cada aumento de 1 unidade na magnitude Richter corresponde a uma energia liberada aproximadamente 31,6 vezes maior**, independentemente do nível inicial de magnitude.

**c) Elaboração de um problema análogo (exemplo de resposta esperada)**

Uma resposta válida deve: (i) escolher um contexto realista (pH, radioatividade, financeiro etc.); (ii) definir uma função logarítmica coerente com esse contexto; (iii) formular uma pergunta sobre a *variação* de uma grandeza (não apenas um cálculo pontual); (iv) resolver corretamente a pergunta formulada.

Exemplo: *'A concentração de íons $H^+$ de uma solução se relaciona ao pH pela fórmula $pH = -\log_{10}[H^+]$. Se o pH de uma solução aumenta de 4 para 6, quantas vezes a concentração de íons $H^+$ diminui?'*

Resolução do exemplo: $[H^+]_1 = 10^{-4}$, $[H^+]_2 = 10^{-6}$. A razão $\dfrac{[H^+]_1}{[H^+]_2} = 10^{-4-(-6)} = 10^{2} = 100$. Logo, a concentração de íons $H^+$ diminui 100 vezes quando o pH sobe de 4 para 6.

Qualquer problema elaborado pelo estudante que satisfaça os quatro critérios acima deve ser considerado correto.

## Formalização verificável

- `funcao` — expressão `(log(x, 10) - Rational(48,10)) / Rational(15,10)`, esperado `3`, parâmetros `{'consulta': 'valor', 'ponto': '10**Rational(93,10)'}`
- `equacao` — expressão `Eq(x, 10**Rational(3,2))`, esperado `[10*sqrt(10)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - equacao=aprovado
  - equacao=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente a função, os dados (constantes 1,5 e 4,8) e os três pedidos (calcular, generalizar razão, comparar magnitudes). Não há ambiguidade lexical ou estrutural, e a notação matemática é padrão.
  - adequacao_nivel: 2/5 — O Bloom declarado é 'criar', mas as tarefas pedidas são: substituir valores (item a, nível 'aplicar/lembrar'), manipular expoentes para mostrar uma razão constante (item b, nível 'analisar/compreender') e aplicar o padrão a um caso numérico (item c, nível 'aplicar'). Em nenhum momento o aluno produz algo novo, formula um modelo próprio ou elabora um problema — que seriam os indicadores SOLO de 'criar' (relacional estendido/produção autônoma). A estrutura de resposta é essencialmente multiestrutural/relacional, não de síntese/criação.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT305 exige trabalhar com funções LOGARÍTMICAS e compreender a variação das grandezas nesse contexto. Entretanto, a função dada, E(M) = 10^(1,5M+4,8), é uma função EXPONENCIAL de M (embora a escala Richter seja originalmente definida como logaritmo da energia). A resolução usa apenas propriedades de potências (divisão de potências de mesma base), sem qualquer manipulação de logaritmos. Assim, a questão trata efetivamente de função exponencial e progressão geométrica associada a incrementos lineares, não de função logarítmica propriamente dita — um desalinhamento de conteúdo com o que a habilidade declara. Além disso, a habilidade fala em 'resolver E elaborar problemas'; a questão só pede para resolver, sem exigir que o aluno elabore/generalize um problema novo, o que é esperado do nível 'criar'.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de energia sísmica e escala Richter é um exemplo clássico e recorrente em livros didáticos para introduzir escalas logarítmicas, reduzindo a originalidade contextual. Por outro lado, o pedido de generalizar a razão E(M+1)/E(M) até obter uma constante independente de M é um recurso didático interessante que vai além da mera aplicação mecânica, mitigando parcialmente o problema.
  - *sugestões:* 1) Reformule a função para que ela seja explicitamente logarítmica, coerente com a habilidade EM13MAT305 — por exemplo, apresente primeiro uma medida física (energia ou amplitude) e peça que o aluno calcule a magnitude M através de uma fórmula do tipo M = (log10(E) - 4,8)/1,5, exigindo manipulação de logaritmos (propriedades, mudança de base, etc.), não apenas de potências. 2) Para atender ao nível 'criar' declarado, adicione um item final em que o aluno deva ELABORAR um novo problema análogo (por exemplo, criar um contexto de pH ou radioatividade com uma função logarítmica original, definir os parâmetros e formular uma pergunta que exija interpretar a variação da grandeza), ou peça que ele construa e justifique um modelo logarítmico alternativo a partir de dados hipotéticos, e não apenas generalize uma razão já dada pela estrutura do enunciado. 3) Deixe explícito no enunciado ou na resolução o uso de logaritmos (ex.: pedir para expressar M em função de log(E) antes de comparar razões), garantindo que o conteúdo avaliado corresponda de fato a 'funções logarítmicas' e não a manipulação pura de potências/exponenciais. 4) Revise a especificação de dificuldade/Bloom para 'aplicar' ou 'analisar' caso opte por manter a estrutura atual (mais simples e coerente com o que é pedido), evitando o descompasso entre o nível cognitivo declarado e o exigido na prática.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Reformule a função para que ela seja explicitamente logarítmica, coerente com a habilidade EM13MAT305 — por exemplo, apresente primeiro uma medida física (energia ou amplitude) e peça que o aluno calcule a magnitude M através de uma fórmula do tipo M = (log10(E) - 4,8)/1,5, exigindo manipulação de logaritmos (propriedades, mudança de base, etc.), não apenas de potências. 2) Para atender ao nível 'criar' declarado, adicione um item final em que o aluno deva ELABORAR um novo problema análogo (por exemplo, criar um contexto de pH ou radioatividade com uma função logarítmica original, definir os parâmetros e formular uma pergunta que exija interpretar a variação da grandeza), ou peça que ele construa e justifique um modelo logarítmico alternativo a partir de dados hipotéticos, e não apenas generalize uma razão já dada pela estrutura do enunciado. 3) Deixe explícito no enunciado ou na resolução o uso de logaritmos (ex.: pedir para expressar M em função de log(E) antes de comparar razões), garantindo que o conteúdo avaliado corresponda de fato a 'funções logarítmicas' e não a manipulação pura de potências/exponenciais. 4) Revise a especificação de dificuldade/Bloom para 'aplicar' ou 'analisar' caso opte por manter a estrutura atual (mais simples e coerente com o que é pedido), evitando o descompasso entre o nível cognitivo declarado e o exigido na prática.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(1000000000*10**(3/10)) = 3). | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — Enunciado bem estruturado nos três itens. Item (a) e (b) têm dados e pedidos precisos. Item (c) explicita claramente os quatro critérios que a resposta deve satisfazer, o que reduz a ambiguidade típica de tarefas abertas de criação, mas a lista de subtarefas ('definir parâmetros', 'formular pergunta', 'resolver') poderia ser numerada para maior precisão de leitura.
  - adequacao_nivel: 4/5 — O nível 'criar' é efetivamente exigido no item (c), que pede a elaboração de uma função e de um problema original, coerente com SOLO estendido abstrato. Os itens (a) e (b) funcionam como andaime cognitivo (aplicar/analisar) antes da criação, o que é pedagogicamente válido, mas faz com que apenas 1/3 da questão atinja de fato o nível declarado — vale considerar se todo o instrumento deveria refletir 'criar' com mais peso relativo.
  - alinhamento_bncc: 5/5 — Cumpre as três exigências: (1) envolve função logarítmica com interpretação de variação (item b mostra que a razão de energias é constante, não dependendo de M1 — isso é interpretação de variação, não mera substituição); (2) contexto realista de abalos sísmicos, e item (c) amplia para pH/radioatividade; (3) explicitamente pede 'resolver e elaborar', atendendo à habilidade EM13MAT305 de forma integrada, não como itens justapostos.
  - distratores: 5/5 — Não se aplica — questão discursiva.
  - originalidade: 4/5 — O uso da escala Richter é contexto comum em livros didáticos, mas a articulação do item (b) — mostrar que a razão de energias independe de M1 — foge do cálculo pontual típico. O item (c), ao delegar a criação ao próprio estudante, evita o efeito Topaze e garante originalidade estrutural, ainda que o exemplo de resolução fornecido (pH) seja também um clássico de livro.
