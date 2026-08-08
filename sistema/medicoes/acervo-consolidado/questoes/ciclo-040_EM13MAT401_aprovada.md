# Ciclo 040 — EM13MAT401

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** entender
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Duas empresas de transporte por aplicativo, Moto Rápida e Carro Center, cobram uma corrida com base na distância percorrida. A tabela abaixo mostra o valor cobrado, em reais, para algumas distâncias, em quilômetros:

Moto Rápida: 2 km → R$ 7,00; 5 km → R$ 17,50; 8 km → R$ 28,00

Carro Center: 2 km → R$ 9,00; 5 km → R$ 16,50; 8 km → R$ 24,00

Um estudante decide representar, em um mesmo plano cartesiano, o custo da corrida (eixo y, em reais) em função da distância percorrida (eixo x, em km) para cada uma das duas empresas, obtendo duas retas.

Assinale a alternativa que descreve corretamente essas duas retas, indicando qual delas representa uma relação de proporcionalidade direta entre custo e distância, e em que ponto (distância, custo) as duas retas se cruzam.

## Alternativas

- (a) A reta de Moto Rápida passa pela origem, com inclinação 3,5, representando proporcionalidade direta; a reta de Carro Center corta o eixo y em (0; 4) e tem inclinação 2,5; as retas se cruzam no ponto (4; 14).  ← correta
- (b) A reta de Carro Center passa pela origem, com inclinação 2,5, representando proporcionalidade direta; a reta de Moto Rápida corta o eixo y em (0; 4) e tem inclinação 3,5; as retas se cruzam no ponto (4; 14).
  - *erro representado:* Inverte os papéis das empresas ao identificar qual função é proporcional, atribuindo a taxa fixa e a inclinação à empresa trocada.
- (c) A reta de Moto Rápida passa pela origem, com inclinação 3,5, representando proporcionalidade direta; a reta de Carro Center corta o eixo y em (0; 4) e tem inclinação 2,5; as retas se cruzam no ponto (4; 10).
  - *erro representado:* Ao calcular a ordenada do ponto de interseção, usa apenas o termo variável (2,5·4) e esquece de somar a taxa fixa de R$ 4,00, obtendo y = 10 em vez de y = 14.
- (d) Tanto a reta de Moto Rápida (inclinação 3,5) quanto a de Carro Center (inclinação 2,5) passam pela origem, sendo ambas proporcionais; por isso, as retas só têm um ponto em comum, a origem (0; 0).
  - *erro representado:* Ignora o coeficiente linear (taxa fixa) da função do Carro Center, tratando erroneamente toda função de 1º grau como proporcional e concluindo que a interseção ocorre na origem.

## Gabarito

A reta de Moto Rápida passa pela origem, com inclinação 3,5, representando proporcionalidade direta; a reta de Carro Center corta o eixo y em (0; 4) e tem inclinação 2,5; as retas se cruzam no ponto (4; 14).

## Resolução

**Passo 1 — Taxa de variação (inclinação) de cada reta**

Para a Moto Rápida, usando os pontos $(2;7)$ e $(5;17{,}5)$:
$$a_{MR}=\frac{17{,}5-7}{5-2}=\frac{10{,}5}{3}=3{,}5$$

Para o Carro Center, usando os pontos $(2;9)$ e $(5;16{,}5)$:
$$a_{CC}=\frac{16{,}5-9}{5-2}=\frac{7{,}5}{3}=2{,}5$$

**Passo 2 — Coeficiente linear (intercepto) de cada reta**

Para a Moto Rápida, testando $y=3{,}5x$ em $x=2$: $3{,}5\cdot 2 = 7$ ✓ (confere também em $x=5$ e $x=8$). Como não há termo independente, $b_{MR}=0$: a reta **passa pela origem**, logo $y=3{,}5x$ é uma função **proporcional** (linear no sentido estrito).

Para o Carro Center, usando $y=2{,}5x+b$ e o ponto $(2;9)$:
$$9=2{,}5\cdot 2+b \Rightarrow b=9-5=4$$
Verificando em $x=8$: $2{,}5\cdot 8+4=24$ ✓. Assim, $y=2{,}5x+4$: a reta **corta o eixo y em $(0;4)$**, não passando pela origem — é apenas afim, **não proporcional**.

**Passo 3 — Ponto de interseção das retas**

Igualando as duas leis:
$$3{,}5x = 2{,}5x+4$$
$$3{,}5x-2{,}5x=4 \Rightarrow x=4$$
$$y=3{,}5\cdot 4=14$$

As retas se cruzam no ponto $(4;14)$, ou seja, para 4 km de percurso, ambas cobrariam R$ 14,00.

**Conclusão:** A reta da Moto Rápida ($y=3{,}5x$) passa pela origem e representa proporcionalidade direta; a do Carro Center ($y=2{,}5x+4$) corta o eixo y em $(0;4)$ e não é proporcional; as retas se cruzam em $(4;14)$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `Rational(7,2)*x`, parâmetros `{'pontos': '[(2,7),(5,Rational(35,2)),(8,28)]', 'grau': '1', 'forma': 'a*x'}`
- `propriedade` — expressão `-`, esperado `Rational(5,2)*x + 4`, parâmetros `{'pontos': '[(2,9),(5,Rational(33,2)),(8,24)]', 'grau': '1'}`
- `equacao` — expressão `Eq(Rational(7,2)*x, Rational(5,2)*x + 4)`, esperado `[4]`
- `funcao` — expressão `Rational(7,2)*x`, esperado `14`, parâmetros `{'consulta': 'valor', 'ponto': '4'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 7*x/2: reproduz os 3 pontos dados; grau 1; forma a*x. | (2) aprovado: Propriedades confirmadas para 5*x/2 + 4: reproduz os 3 pontos dados; grau 1. | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (4) aprovado: Gabarito confirmado (f(4) = 14).
  - propriedade=aprovado
  - propriedade=aprovado
  - equacao=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta dados tabulares completos (três pontos por empresa, permitindo verificar a linearidade), define claramente os eixos e pede três informações específicas (lei de cada reta, qual é proporcional, ponto de interseção). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — O nível declarado é 'entender' (classificar/interpretar), mas a resolução exige encadear vários procedimentos algébricos: calcular duas inclinações, testar/ajustar o coeficiente linear e resolver um sistema para achar a interseção. Isso corresponde mais a 'aplicar' (SOLO relacional) do que a 'entender'. A classificação proporcional-vs-afim (o núcleo de 'entender') está presente, mas fica diluída entre etapas de cálculo mais exigentes que extrapolam o processo cognitivo declarado.
  - alinhamento_bncc: 4/5 — A questão exige inferir a lei algébrica a partir de dados tabulares e associá-la à representação geométrica (inclinação, intercepto, retas no plano), cumprindo o trânsito algébrico-geométrico pedido pela EM13MAT401. Distingue corretamente o caso proporcional (y=3,5x) do afim (y=2,5x+4). O único ponto que extrapola levemente a habilidade é a exigência de achar o ponto de interseção das retas, que não é objeto central da habilidade, mas não compromete o cumprimento do núcleo exigido.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis: troca de rótulos entre as empresas, esquecimento do termo constante ao calcular a ordenada da interseção, e a generalização incorreta de que toda função afim é proporcional. Nenhum é absurdo ou trivialmente descartável.
  - originalidade: 4/5 — O contexto de aplicativos de transporte é atual e evita o clichê de 'dois carros partindo ao mesmo tempo'. O uso de tabela (em vez da lei já pronta) exige do aluno a etapa de modelagem, evitando pistas diretas que resolveriam o problema (efeito Topaze é minimizado), embora o tema em si (comparação de tarifas) já seja relativamente comum em materiais didáticos.
