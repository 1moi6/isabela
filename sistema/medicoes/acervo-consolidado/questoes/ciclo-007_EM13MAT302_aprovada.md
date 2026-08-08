# Ciclo 007 — EM13MAT302

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma oficina mecânica cobra por seus serviços de revisão um valor fixo de mão de obra, mais uma taxa que depende do número de horas de trabalho. Uma revisão que durou 2 horas custou R$ 150,00, e outra revisão, no mesmo padrão de cobrança, durou 5 horas e custou R$ 300,00. Sabendo que o custo total varia linearmente com o número de horas trabalhadas, qual seria o custo de uma revisão que durasse 8 horas?

## Alternativas

- (a) R$ 450,00  ← correta
- (b) R$ 400,00
  - *erro representado:* Calculou corretamente a taxa por hora (R$ 50,00), mas esqueceu de somar o valor fixo de mão de obra, calculando apenas 50×8.
- (c) R$ 600,00
  - *erro representado:* Assumiu proporcionalidade direta (sem termo fixo), usando apenas o primeiro par de valores: taxa = 150/2 = 75 por hora, e depois 75×8.
- (d) R$ 480,00
  - *erro representado:* Calculou uma taxa média a partir do segundo dado (300/5 = 60 por hora) e multiplicou diretamente por 8 horas, ignorando o valor fixo e a taxa correta obtida pela diferença entre os pontos.

## Gabarito

R$ 450,00

## Resolução

Como o custo total $C$ varia linearmente com o número de horas $x$, podemos escrever $C(x) = ax + b$, em que $a$ é a taxa cobrada por hora e $b$ é o valor fixo de mão de obra.

**Passo 1 — Determinar a taxa por hora ($a$).**
Usando os dois pares de valores dados, $(2, 150)$ e $(5, 300)$:
$$a = \frac{300 - 150}{5 - 2} = \frac{150}{3} = 50$$

Ou seja, cada hora de trabalho custa R\$ 50,00.

**Passo 2 — Determinar o valor fixo ($b$).**
Substituindo o ponto $(2, 150)$ em $C(x) = 50x + b$:
$$150 = 50 \cdot 2 + b \;\Rightarrow\; 150 = 100 + b \;\Rightarrow\; b = 50$$

Logo, o modelo do custo é:
$$C(x) = 50x + 50$$

**Passo 3 — Calcular o custo para $x = 8$ horas.**
$$C(8) = 50 \cdot 8 + 50 = 400 + 50 = 450$$

Portanto, a revisão de 8 horas custaria **R\$ 450,00**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `50*x + 50`, parâmetros `{'pontos': '[(2,150),(5,300)]', 'grau': '1'}`
- `funcao` — expressão `50*x + 50`, esperado `450`, parâmetros `{'consulta': 'valor', 'ponto': '8'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*x + 4: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(10) = 34).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado é direto, sem ambiguidade: dados f(1)=7 e f(4)=16, pede-se f(10). Todas as condições necessárias estão explícitas.
  - adequacao_nivel: 4/5 — A resolução exige montar e resolver um sistema linear e depois aplicar a lei encontrada, o que é compatível com 'aplicar' (Bloom) e com resposta relacional (SOLO). Processo cognitivo coerente com o nível declarado, embora seja uma aplicação bastante mecânica/algorítmica.
  - alinhamento_bncc: 2/5 — A especificação exige que a questão NÃO entregue o modelo pronto quando o nível é 'aplicar'. Aqui o enunciado já fornece explicitamente 'f(x)=ax+b, função afim', eliminando a etapa de identificar/construir o modelo a partir de uma situação — o aluno só resolve um sistema algébrico. Além disso, não há situação-problema ou contexto (a habilidade fala em 'contextos diversos'); é um exercício puramente formal de determinação de coeficientes, não uma modelagem. Isso descumpre diretamente as exigências listadas.
  - distratores: 4/5 — Os erros representados (esquecer o termo b; tratar como proporcionalidade direta; usar f(1) como b sem descontar a·1) são plausíveis e correspondem a equívocos comuns de estudantes. Nenhum é absurdo ou trivialmente descartável, embora sejam relativamente previsíveis para quem já domina o procedimento padrão.
  - originalidade: 2/5 — É o modelo clássico de exercício de livro didático: 'dado f(x)=ax+b e dois valores, ache f(algo)'. Não há contexto significativo nem situação real que justifique o uso da função afim; o enunciado já entrega a forma algébrica, pavimentando a solução (efeito Topaze), sem qualquer elemento de elaboração ou interpretação de contexto.
  - *sugestões:* Reescreva o enunciado como uma situação contextualizada (ex.: custo de um serviço, distância percorrida, tarifa de conta, crescimento populacional linear) na qual os dados numéricos (dois pares de valores) apareçam naturalmente, sem mencionar 'f(x)=ax+b' ou a palavra 'afim'. O aluno deve inferir, a partir do contexto, que o comportamento é linear e construir o modelo (identificar taxa de variação e valor inicial) antes de usá-lo para calcular o valor pedido. Isso cumpre a exigência de não entregar o modelo pronto e atende à habilidade EM13MAT302, que pede resolver problemas cujo modelo é uma função polinomial, não apenas manipular uma fórmula já dada. Mantenha os distratores, adaptando-os ao novo contexto.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reescreva o enunciado como uma situação contextualizada (ex.: custo de um serviço, distância percorrida, tarifa de conta, crescimento populacional linear) na qual os dados numéricos (dois pares de valores) apareçam naturalmente, sem mencionar 'f(x)=ax+b' ou a palavra 'afim'. O aluno deve inferir, a partir do contexto, que o comportamento é linear e construir o modelo (identificar taxa de variação e valor inicial) antes de usá-lo para calcular o valor pedido. Isso cumpre a exigência de não entregar o modelo pronto e atende à habilidade EM13MAT302, que pede resolver problemas cujo modelo é uma função polinomial, não apenas manipular uma fórmula já dada. Mantenha os distratores, adaptando-os ao novo contexto.

### Iteração 2

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 50*x + 50: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(8) = 450).
  - propriedade=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (dois pares hora-custo) e pergunta objetiva. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O aluno precisa construir o modelo afim a partir de dois pontos dados (determinar coeficiente angular e linear) e depois aplicá-lo, o que corresponde ao nível 'aplicar'. A estrutura de resposta exige articulação de duas etapas (achar a e b, depois calcular C(8)), compatível com nível relacional da SOLO, ainda que a tarefa seja padrão.
  - alinhamento_bncc: 5/5 — A questão exige explicitamente construir o modelo de função afim a partir de dados contextuais, sem entregá-lo pronto, atendendo integralmente à habilidade EM13MAT302 e à exigência de não fornecer o modelo already-formado.
  - distratores: 5/5 — Os quatro distratores representam erros sistemáticos plausíveis e distintos: esquecer o termo fixo, assumir proporcionalidade direta, e usar taxa média mal calculada. Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 4/5 — O contexto (oficina mecânica) é razoavelmente aplicado e evita o clichê mais comum (táxi, aluguel de carro), mas ainda segue o padrão clássico de 'custo fixo + variável' frequente em livros didáticos, sem inovação estrutural relevante.
