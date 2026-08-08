# Ciclo 032 — EM13MAT306

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Em certo porto, a altura da água (em metros), medida a partir do fundo, varia periodicamente ao longo do dia por causa da maré. Chamando de $t$ o tempo em horas contado a partir da meia-noite (t = 0), foram feitas as seguintes observações:

- à meia-noite (t = 0) ocorre a maré alta, com altura da água de 7 m;
- às 6 horas (t = 6) ocorre a maré baixa, com altura da água de 1 m;
- o fenômeno se repete a cada 12 horas.

a) Represente essa situação por uma função do tipo $h(t) = A\cos(Bt) + D$, indicando os valores de $A$ (amplitude da oscilação), $B$ (relacionado ao período) e $D$ (nível médio da água), de modo que o gráfico dessa função reproduza corretamente os dados observados.

b) Usando a função obtida, calcule a altura da água às 3 horas da manhã (t = 3).

c) Determine em que outro horário, entre 0h e 24h, a maré volta a ficar alta (altura máxima de 7 m).

## Gabarito

a) $h(t)=3\cos\left(\dfrac{\pi}{6}t\right)+4$, com $A=3$, $B=\dfrac{\pi}{6}$, $D=4$. b) $h(3)=4$ m. c) A maré volta a ficar alta ao meio-dia (t = 12h).

## Resolução

**a) Determinando A, B e D**

A altura máxima é $H_{max}=7$ m e a mínima é $H_{min}=1$ m.

A amplitude corresponde à metade da distância entre o máximo e o mínimo:
$$A=\dfrac{H_{max}-H_{min}}{2}=\dfrac{7-1}{2}=3$$

O deslocamento vertical (nível médio) é a média entre máximo e mínimo:
$$D=\dfrac{H_{max}+H_{min}}{2}=\dfrac{7+1}{2}=4$$

Como o fenômeno se repete a cada 12 horas, o período é $T=12$. Para a função cosseno, $T=\dfrac{2\pi}{B}$, logo:
$$B=\dfrac{2\pi}{T}=\dfrac{2\pi}{12}=\dfrac{\pi}{6}$$

Como em $t=0$ a maré está alta (valor máximo), e $\cos(0)=1$ já fornece o máximo de $A\cos(Bt)+D$, o modelo cosseno (sem deslocamento horizontal) se ajusta perfeitamente:
$$h(t)=3\cos\left(\dfrac{\pi}{6}t\right)+4$$

**b) Altura às 3 horas (t = 3)**

$$h(3)=3\cos\left(\dfrac{\pi}{6}\cdot 3\right)+4=3\cos\left(\dfrac{\pi}{2}\right)+4$$

Como $\cos\left(\dfrac{\pi}{2}\right)=0$:
$$h(3)=3\cdot 0+4=4\text{ m}$$

**c) Novo horário de maré alta**

A maré estará alta quando $h(t)=7$, ou seja, quando $\cos\left(\dfrac{\pi}{6}t\right)=1$.

Isso ocorre quando $\dfrac{\pi}{6}t=2k\pi$, $k\in\mathbb{Z}$, ou seja, $t=12k$.

Dentro do intervalo $0\le t<24$, as soluções são $t=0$ (dado inicial) e $t=12$.

Portanto, a maré volta a ficar alta às **12 horas (meio-dia)**, exatamente meio período (12 h) após a meia-noite, como esperado para uma função cosseno de período 12.

## Formalização verificável

- `funcao` — expressão `3*cos(pi*t/6)+4`, esperado `12`, parâmetros `{'consulta': 'periodo'}`
- `funcao` — expressão `3*cos(pi*t/6)+4`, esperado `4`, parâmetros `{'consulta': 'valor', 'ponto': '3'}`
- `funcao` — expressão `3*cos(pi*t/6)+4`, esperado `7`, parâmetros `{'consulta': 'maximo'}`
- `equacao` — expressão `Eq(3*cos(pi*t/6)+4, 7)`, esperado `[0, 12]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (período 12). | (2) aprovado: Gabarito confirmado (f(3) = 4). | (3) aprovado: Gabarito confirmado (extremo calculado 7). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/periodo=aprovado
  - funcao/valor=aprovado
  - funcao/maximo=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado explicita claramente os dados (maré alta/baixa, horários, período) e as três tarefas (a, b, c) são inequívocas quanto ao que é pedido e quais condições devem ser satisfeitas.
  - adequacao_nivel: 4/5 — O processo exigido é de aplicação direta de fórmulas (amplitude, período, deslocamento vertical) e substituição de valores, compatível com o nível 'aplicar' e com dificuldade fácil. A estrutura multiestrutural (a, b, c) é coerente com esse nível, mas o fato de o enunciado já fornecer o modelo pronto 'h(t)=A cos(Bt)+D' reduz a exigência cognitiva a um preenchimento de parâmetros, aproximando-se do limite inferior de 'aplicar'.
  - alinhamento_bncc: 4/5 — O fenômeno é periódico e real (maré), e amplitude, período e deslocamento vertical são objeto central da questão, não decorativos. Entretanto, a habilidade EM13MAT306 pede explicitamente 'comparar suas representações com as funções seno e cosseno no plano cartesiano', e a questão não solicita explicitamente uma representação gráfica ou uma comparação entre as duas famílias de função — apenas menciona o gráfico de passagem no item (a). Essa dimensão de comparação gráfica fica implícita, não exigida como tarefa.
  - distratores: 5/5 — Não se aplica: questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de marés é um dos exemplos mais clássicos e recorrentes em livros didáticos para funções trigonométricas, sem elemento de contextualização diferenciado. Além disso, fornecer a forma pronta 'h(t)=A cos(Bt)+D' e nomear explicitamente 'A (amplitude)', 'B (relacionado ao período)' e 'D (nível médio)' constitui um efeito Topaze, pavimentando quase toda a resolução do item (a).
  - *sugestões:* Para elevar a qualidade da questão: (1) No item (a), retire os rótulos explicativos entre parênteses ('amplitude da oscilação', 'relacionado ao período', 'nível médio da água') e peça que o aluno justifique o significado de cada parâmetro, exigindo raciocínio em vez de preenchimento guiado. (2) Inclua uma tarefa que peça explicitamente a construção ou leitura do gráfico de h(t) no plano cartesiano e uma comparação com a função seno equivalente (ex.: 'escreva também uma função em termos de seno que descreva o mesmo fenômeno e compare os gráficos'), atendendo de forma mais direta à exigência da BNCC de comparação seno/cosseno no plano cartesiano. (3) Considere variar o contexto (ex.: batimento cardíaco, ciclo de luz solar) em versões futuras para reduzir a repetição do clássico exemplo de marés.
