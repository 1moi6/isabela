# Ciclo 071 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Uma confecção fabrica um certo modelo de camisa a um custo de produção de R$ 40,00 por unidade. Um estudo de mercado mostrou que, se o preço de venda for $p$ reais por unidade, a quantidade vendida mensalmente será $q(p) = 300 - 5p$ unidades, válida para $0 < p < 60$. O lucro mensal da confecção, em reais, é dado pelo produto entre o lucro obtido em cada unidade vendida (preço de venda menos custo de produção) e a quantidade vendida naquele mês. Qual deve ser o preço de venda $p$, em reais, para que o lucro mensal da confecção seja máximo?

## Alternativas

- (a) R$ 50,00  ← correta
- (b) R$ 30,00
  - *erro representado:* Maximizou a receita em vez do lucro: calculou o vértice de R(p) = p·(300-5p) = -5p²+300p, esquecendo de subtrair o custo unitário de R$ 40,00 antes de multiplicar pela quantidade vendida.
- (c) R$ 100,00
  - *erro representado:* Aplicou a fórmula do vértice sem dividir por 2, calculando x_v = -b/a = -500/(-5) = 100, em vez de x_v = -b/(2a).
- (d) R$ 60,00
  - *erro representado:* Resolveu L(p) = 0 (encontrando as raízes p = 40 e p = 60) e tomou a maior raiz como se fosse o ponto de máximo, confundindo o zero da função com o seu vértice.

## Gabarito

R$ 50,00 (alternativa a)

## Resolução

**1. Montar a função lucro**

O lucro por unidade vendida é $(p-40)$ reais, e a quantidade vendida é $q(p)=300-5p$. Logo, o lucro mensal é:

$$L(p) = (p-40)(300-5p)$$

Expandindo:

$$L(p) = 300p - 5p^2 - 12000 + 200p = -5p^2 + 500p - 12000$$

**2. Reconhecer a natureza da parábola**

$L(p)$ é uma função quadrática com $a = -5 < 0$, portanto a parábola tem concavidade voltada para baixo e possui um **ponto de máximo** no vértice.

**3. Calcular o preço que maximiza o lucro (coordenada $p$ do vértice)**

$$p_v = -\frac{b}{2a} = -\frac{500}{2\cdot(-5)} = -\frac{500}{-10} = 50$$

Como $0 < 50 < 60$, esse preço pertence ao domínio válido do problema.

**4. (Verificação) Calcular o lucro máximo correspondente**

$$L(50) = -5(50)^2 + 500(50) - 12000 = -12500 + 25000 - 12000 = 500$$

Ou seja, ao praticar o preço de R$ 50,00, a confecção vende $q(50)=300-250=50$ unidades, com lucro unitário de R$ 10,00, totalizando R$ 500,00 de lucro mensal — o maior valor possível para essa função.

**Conclusão:** o preço que maximiza o lucro mensal é **R$ 50,00**.

## Formalização verificável

- `funcao` — expressão `-5*p**2 + 500*p - 12000`, esperado `[50, 500]`, parâmetros `{'consulta': 'vertice'}`
- `funcao` — expressão `-5*p**2 + 500*p - 12000`, esperado `Interval.open(0, 60)`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (vértice calculado (50, 500)). | (2) aprovado: Gabarito confirmado (domínio Interval.open(0, 60) — restrição de contexto dentro do domínio máximo Reals).
  - funcao/vertice=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado define claramente custo unitário, função de demanda, domínio de validade e a definição explícita de lucro (preço menos custo, vezes quantidade). Não há ambiguidade lexical ou estrutural, e os dados são suficientes para resolver o problema sem suposições adicionais.
  - adequacao_nivel: 4/5 — O aluno precisa relacionar três grandezas (preço, custo, quantidade) para construir a função lucro e só então aplicar o procedimento do vértice — isso é mais do que manipulação algébrica pura, exigindo articulação de dados (nível relacional na SOLO), compatível com 'aplicar' na taxonomia de Bloom. Poderia exigir um passo extra de interpretação (ex.: justificar por que o vértice está no domínio) para atingir plenamente o nível 'analisar', mas para 'aplicar' está bem calibrado.
  - alinhamento_bncc: 5/5 — Cumpre integralmente a habilidade EM13MAT503: pede investigação de ponto de máximo de função quadrática em contexto de Matemática Financeira (lucro, custo, receita), exigindo que o estudante construa o modelo a partir da situação, não apenas aplique fórmula a uma função já dada.
  - distratores: 5/5 — Os quatro distratores representam erros conceituais distintos e plausíveis: confundir receita com lucro, esquecer o denominador 2 na fórmula do vértice, e confundir raiz da função com vértice. Nenhum é absurdo ou eliminável por inspeção superficial, exigindo de fato compreensão do procedimento correto.
  - originalidade: 3/5 — O contexto de 'custo fixo por unidade + função de demanda linear + maximização de lucro' é um modelo extremamente recorrente em livros didáticos e vestibulares, o que reduz a originalidade. Não há efeito Topaze explícito (o enunciado não indica o procedimento a usar), mas a situação em si é pouco inovadora.
