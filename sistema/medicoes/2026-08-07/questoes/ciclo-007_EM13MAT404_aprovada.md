# Ciclo 007 — EM13MAT404

- **Situação:** aprovada
- **Temas:** funcao_trigonometrica
- **Nível cognitivo:** entender
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um ponto P percorre o ciclo trigonométrico usual (circunferência de raio 1 centrada na origem), partindo de (1,0) e girando no sentido anti-horário. Ao registrar, para cada ângulo $x$ (em radianos) já percorrido por P, a ordenada desse ponto num plano cartesiano com eixos $(x,y)$, obtém-se o gráfico da função $y=\operatorname{sen}(x)$.

Considere agora um segundo ciclo trigonométrico, desta vez com raio 2 e centro no ponto $(0,3)$ do eixo vertical do plano cartesiano. Um ponto Q percorre essa circunferência maior, deslocada, do mesmo modo (mesma velocidade angular, mesmo sentido, partindo do ponto da circunferência situado sobre a reta $y=3$ à direita do centro). Registrando, para cada ângulo $x$ percorrido, a ordenada de Q no plano cartesiano $(x,y)$, obtém-se o gráfico da função
$$f(x) = 3 + 2\,\operatorname{sen}(x).$$

Com base na comparação entre os dois ciclos trigonométricos (o de raio 1 e o de raio 2 deslocado) e os respectivos gráficos no plano cartesiano, determine corretamente o domínio, a imagem e o período de $f$.

## Alternativas

- (a) Domínio $\mathbb{R}$, Imagem $[1,5]$, Período $2\pi$  ← correta
- (b) Domínio $\mathbb{R}$, Imagem $[2,4]$, Período $2\pi$
  - *erro representado:* Somou diretamente o deslocamento vertical (3) com os limites do seno sem antes multiplicar pela amplitude (raio 2), calculando $3\pm1$ em vez de $3\pm2$.
- (c) Domínio $[0,2\pi]$, Imagem $[1,5]$, Período $2\pi$
  - *erro representado:* Confundiu o domínio da função (todos os reais) com o intervalo angular de uma única volta no ciclo trigonométrico.
- (d) Domínio $\mathbb{R}$, Imagem $[1,5]$, Período $4\pi$
  - *erro representado:* Assumiu erroneamente que o raio maior do ciclo trigonométrico (2, em vez de 1) faz o ponto demorar o dobro do ângulo para completar uma volta, multiplicando o período pela amplitude.

## Gabarito

Domínio $\mathbb{R}$, Imagem $[1,5]$, Período $2\pi$ (alternativa A)

## Resolução

**Passo 1 — Domínio.** No ciclo trigonométrico, o ponto Q pode percorrer a circunferência indefinidamente, dando quantas voltas se queira, em qualquer sentido. Isso significa que o ângulo $x$ pode assumir **qualquer** número real, positivo, negativo ou nulo — não há restrição alguma. Logo, o domínio de $f$ é $\mathbb{R}$.

**Passo 2 — Imagem.** No ciclo de raio 1, a ordenada de P (isto é, $\operatorname{sen}(x)$) varia entre $-1$ e $1$, pois esse é o raio da circunferência. No ciclo de Q, o raio é 2, então a ordenada de Q relativa ao centro varia entre $-2$ e $2$, ou seja, $2\,\operatorname{sen}(x) \in [-2,2]$. Como o centro desse ciclo está deslocado para $(0,3)$, a ordenada absoluta de Q é o valor relativo somado a 3:
$$f(x) = 3 + 2\,\operatorname{sen}(x) \in [3-2,\; 3+2] = [1,5].$$
Assim, a imagem de $f$ é o intervalo $[1,5]$.

**Passo 3 — Período.** O período está associado ao tempo (ou ângulo) necessário para o ponto completar uma volta completa na circunferência e retornar à mesma posição. Isso depende apenas do ângulo percorrido, não do raio do ciclo nem do deslocamento do centro: tanto P quanto Q completam uma volta a cada $2\pi$ radianos, pois o raio e a translação vertical alteram a amplitude e a posição do gráfico, mas não a velocidade angular. Logo, o período de $f$ continua sendo $2\pi$, o mesmo da função $\operatorname{sen}(x)$.

**Conclusão:** Domínio $=\mathbb{R}$, Imagem $=[1,5]$, Período $=2\pi$.

## Formalização verificável

- `funcao` — expressão `3 + 2*sin(x)`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `3 + 2*sin(x)`, esperado `Interval(1,5)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `3 + 2*sin(x)`, esperado `2*pi`, parâmetros `{'consulta': 'periodo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio de 2*sin(x) + 3: Reals). | (2) aprovado: Gabarito confirmado (imagem de 2*sin(x) + 3: Interval(1, 5)). | (3) aprovado: Gabarito confirmado (período 2*pi).
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/periodo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define com precisão os dois ciclos trigonométricos (raio, centro, sentido, ponto de partida), explicita como cada gráfico é obtido e formula claramente o que se pede (domínio, imagem, período). Não há ambiguidade lexical ou estrutural, embora o texto seja longo.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido — identificar/relacionar características de f a partir da comparação com o ciclo trigonométrico — é coerente com 'entender' na taxonomia de Bloom. Em termos SOLO, a resposta é multiestrutural (três características distintas obtidas por raciocínios análogos, mas não integrados numa única generalização), o que é adequado ao nível declarado, sem exigir análise mais profunda. Conteúdo plenamente compatível com o Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente o que a habilidade exige: mobiliza a comparação entre representação no ciclo trigonométrico (raio, centro, ângulo percorrido) e a representação cartesiana da função, para extrair domínio, imagem e período — as três características fundamentais pedidas. Não se reduz a calcular um valor de seno; a articulação entre as duas representações é central à resolução, não apenas cosmética.
  - distratores: 5/5 — As três alternativas incorretas representam erros sistemáticos plausíveis e didaticamente relevantes: (i) somar o deslocamento vertical sem escalar pela amplitude; (ii) confundir domínio da função com o intervalo angular de uma volta; (iii) supor que o raio maior aumenta o período. Nenhum distrator é absurdo ou eliminável trivialmente.
  - originalidade: 4/5 — O contexto de um segundo ciclo com raio e centro deslocados, comparado explicitamente ao ciclo unitário, foge do enunciado padrão de livro didático que apenas pede para 'analisar f(x)=3+2sen(x)'. Ainda assim, o tema (amplitude e translação vertical do seno) é um clássico do currículo; não há pistas diretas de que 'domínio é R' ou 'imagem é [1,5]' no enunciado, preservando parte do desafio, mas a estrutura de resolução é bastante guiada, o que reduz um pouco a originalidade conceitual.
