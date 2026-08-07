# Ciclo 006 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Uma turbina eólica tem uma pá de comprimento 12 metros, presa ao centro do rotor. O rotor gira com velocidade angular constante, de modo que a pá completa uma volta completa a cada 8 segundos. Adotando um referencial cartesiano com origem no centro do rotor, a altura $h(t)$ da ponta da pá em relação ao centro do rotor, medida em metros, em função do tempo $t$ (em segundos), é dada por

$$h(t) = 12\cos\left(\dfrac{\pi t}{4}\right)$$

O tempo $t$ pode assumir qualquer valor real, positivo, negativo ou nulo, pois o rotor gira continuamente, antes e depois do instante $t=0$.

Com base na comparação entre o ciclo trigonométrico e o gráfico de $h$ no plano cartesiano, responda:

a) Qual é o domínio da função $h$? Justifique.

b) Qual é a imagem da função $h$? Relacione sua resposta com o raio da circunferência descrita pela ponta da pá, comparando-a ao ciclo trigonométrico de raio 1.

c) Qual é o período da função $h$? Interprete esse valor no contexto do movimento da pá.

## Gabarito

a) $D(h)=\mathbb{R}$; b) $Im(h)=[-12,12]$; c) $T=8$ segundos, coincidindo com o tempo de uma volta completa da pá.

## Resolução

**a) Domínio**

O ângulo que a pá varre é $\theta(t) = \dfrac{\pi t}{4}$. Como o rotor gira continuamente — para trás e para frente no tempo, dando voltas completas repetidamente —, o ângulo $\theta$ pode assumir qualquer valor real, correspondendo a um ponto bem definido no ciclo trigonométrico para cada $t$. Logo, não há restrição sobre $t$:

$$D(h) = \mathbb{R}$$

**b) Imagem**

No ciclo trigonométrico de raio 1, para qualquer ângulo $\theta$ vale $-1 \le \cos\theta \le 1$, pois o cosseno é a abscissa do ponto sobre a circunferência unitária. Aqui, a ponta da pá descreve uma circunferência de raio $R = 12$ m (uma versão do ciclo trigonométrico "ampliada" 12 vezes), e $h(t) = 12\cos(\theta(t))$ é a abscissa (altura) desse ponto multiplicada pelo raio. Assim:

$$-1 \le \cos\left(\frac{\pi t}{4}\right) \le 1 \;\Rightarrow\; -12 \le 12\cos\left(\frac{\pi t}{4}\right) \le 12$$

$$Im(h) = [-12, 12]$$

**c) Período**

A função cosseno padrão $\cos(\theta)$ tem período $2\pi$ em relação a $\theta$, ou seja, o ponto sobre o ciclo trigonométrico retorna à mesma posição a cada $2\pi$ radianos percorridos. Como $\theta(t) = \dfrac{\pi}{4}t$, o período $T$ em relação a $t$ satisfaz:

$$\frac{\pi}{4}T = 2\pi \;\Rightarrow\; T = 8$$

Ou seja, $h(t+8) = h(t)$ para todo $t$: a cada 8 segundos, a pá retorna à mesma altura, o que corresponde exatamente ao tempo de uma volta completa do rotor — consistente com o dado do enunciado.

## Formalização verificável

- `funcao` — expressão `12*cos(pi*x/4)`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `12*cos(pi*x/4)`, esperado `Interval(-12, 12)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `12*cos(pi*x/4)`, esperado `8`, parâmetros `{'consulta': 'periodo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) rejeitado: Divergência: domínio calculado: Reals; gabarito: Interval(0, oo). | (2) aprovado: Gabarito confirmado (imagem de 8 - 6*cos(pi*t/15): Interval(2, 14)). | (3) aprovado: Gabarito confirmado (período 30).
  - funcao/dominio=rejeitado
  - funcao/imagem=aprovado
  - funcao/periodo=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) rejeitado: Divergência: domínio calculado: Reals; gabarito: Interval(0, oo). | (2) aprovado: Gabarito confirmado (imagem de 8 - 6*cos(pi*t/15): Interval(2, 14)). | (3) aprovado: Gabarito confirmado (período 30). Resultado calculado independentemente: domínio calculado: Reals | imagem de 8 - 6*cos(pi*t/15): Interval(2, 14) | período 30. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de 8 - 6*cos(pi*t/15): Reals). | (2) aprovado: Gabarito confirmado (imagem de 8 - 6*cos(pi*t/15): Interval(2, 14)). | (3) aprovado: Gabarito confirmado (período 30).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/periodo=aprovado
- **Crítico:** reprovou
  - clareza: 4/5 — O enunciado é longo, mas não ambíguo: dados, variável e pedidos estão bem delimitados. A única fragilidade é o contexto físico forçado (assento antes de t=0), suavizado por uma justificativa matemática explícita.
  - adequacao_nivel: 3/5 — Os itens b) e c) exigem de fato relacionar ciclo trigonométrico e gráfico cartesiano (nível 'entender', estrutura relacional/SOLO). Porém o item a) tem sua resposta praticamente entregue na frase 'de modo que h seja uma função periódica bem definida para toda a reta real', reduzindo esse subitem a mera cópia, abaixo do nível declarado.
  - alinhamento_bncc: 3/5 — A questão pede exatamente as três características da habilidade (domínio, imagem, período) e exige explicitamente a comparação ciclo↔plano cartesiano, o que é positivo. Mas o domínio, um dos três pilares da habilidade, é fornecido de forma disfarçada no próprio enunciado, esvaziando a avaliação dessa competência específica.
  - distratores: 5/5 — Não se aplica: questão discursiva, sem alternativas.
  - originalidade: 2/5 — Contexto de roda-gigante para função trigonométrica é um clássico recorrente em livros didáticos. Além disso, há efeito Topaze evidente: o enunciado antecipa a resposta do domínio ('bem definida para toda a reta real') e explica de forma quase completa como o cosseno se relaciona ao ciclo trigonométrico, pavimentando o raciocínio que deveria ser produzido pelo aluno.
  - *sugestões:* 1) Remova ou reformule a frase 'de modo que h seja uma função periódica bem definida para toda a reta real, útil para descrever o movimento tanto antes quanto depois do instante t=0', pois ela entrega a resposta do item (a) antes de ser pedida. Basta dizer que t pode ser negativo, nulo ou positivo, sem afirmar a conclusão sobre o domínio. 2) Reduza o scaffolding do segundo parágrafo (que já explica que cosseno é abscissa do ciclo): deixe apenas uma menção mais neutra ao ciclo trigonométrico, exigindo que o próprio aluno estabeleça essa relação como parte da resposta, não como dado do enunciado. 3) Troque o contexto da roda-gigante por outro cenário aplicado menos recorrente em livros didáticos (ex.: variação de maré, oscilação de um pistão, sinal de áudio, posição de uma pá de turbina eólica), mantendo a estrutura de pedir domínio/imagem/período com justificativa via comparação ciclo-plano cartesiano. 4) Verifique que cada um dos três subitens exija raciocínio genuíno do aluno, sem que nenhuma resposta esteja implícita ou declarada no enunciado.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Remova ou reformule a frase 'de modo que h seja uma função periódica bem definida para toda a reta real, útil para descrever o movimento tanto antes quanto depois do instante t=0', pois ela entrega a resposta do item (a) antes de ser pedida. Basta dizer que t pode ser negativo, nulo ou positivo, sem afirmar a conclusão sobre o domínio. 2) Reduza o scaffolding do segundo parágrafo (que já explica que cosseno é abscissa do ciclo): deixe apenas uma menção mais neutra ao ciclo trigonométrico, exigindo que o próprio aluno estabeleça essa relação como parte da resposta, não como dado do enunciado. 3) Troque o contexto da roda-gigante por outro cenário aplicado menos recorrente em livros didáticos (ex.: variação de maré, oscilação de um pistão, sinal de áudio, posição de uma pá de turbina eólica), mantendo a estrutura de pedir domínio/imagem/período com justificativa via comparação ciclo-plano cartesiano. 4) Verifique que cada um dos três subitens exija raciocínio genuíno do aluno, sem que nenhuma resposta esteja implícita ou declarada no enunciado.

### Iteração 3

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de 12*cos(pi*x/4): Reals). | (2) aprovado: Gabarito confirmado (imagem de 12*cos(pi*x/4): Interval(-12, 12)). | (3) aprovado: Gabarito confirmado (período 8).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/periodo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado bem estruturado, com dados completos (raio, período, referencial) e perguntas claramente segmentadas em a), b) e c). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — O nível 'entender' é compatível com identificar domínio, imagem e período, mas a frase 'O tempo t pode assumir qualquer valor real, positivo, negativo ou nulo, pois o rotor gira continuamente...' entrega quase literalmente a resposta do item a), reduzindo a tarefa de 'compreender por que D(h)=R' para 'repetir o que já foi dito'. Isso rebaixa o processo cognitivo efetivamente exigido, tornando a resposta esperada mais unistrutural do que multiestrutural nesse item, mesmo pedindo 'justifique'.
  - alinhamento_bncc: 4/5 — Os itens b) e c) exigem explicitamente a comparação entre o ciclo trigonométrico (raio 1) e o gráfico cartesiano (raio 12), articulando corretamente domínio, imagem e período como pede a EM13MAT404. O item a), porém, é fragilizado pelo spoiler no enunciado, que dispensa a comparação ciclo/plano cartesiano para justificar o domínio, atendendo à habilidade apenas parcialmente nesse subitem.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto da turbina eólica é razoavelmente significativo e menos batido que exemplos clássicos (roda-gigante, relógio), mas a frase que antecipa a conclusão do domínio configura efeito Topaze, pavimentando a resposta e reduzindo o valor da questão como situação de descoberta/verificação pelo aluno.
  - *sugestões:* Remover ou reformular a frase que já afirma 'o tempo t pode assumir qualquer valor real, positivo, negativo ou nulo, pois o rotor gira continuamente' — essa informação antecipa a resposta do item a) e elimina a necessidade de o aluno raciocinar sobre o domínio a partir da comparação com o ciclo trigonométrico. Basta dizer que o rotor gira continuamente a partir de t=0 (ou mencionar apenas que o movimento é contínuo, sem afirmar explicitamente 'qualquer valor real'), deixando ao estudante a tarefa de concluir D(h)=R justificando com base no ciclo trigonométrico (ângulo pode dar voltas ilimitadas). Isso preserva o nível cognitivo 'entender' pretendido e fortalece a exigência de comparação ciclo/plano cartesiano também no item a), evitando o efeito Topaze.
