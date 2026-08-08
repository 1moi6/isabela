# Ciclo 059 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Um teatro está sendo projetado com fileiras de poltronas dispostas em leque. A primeira fileira (mais próxima do palco) terá 14 poltronas, e cada fileira seguinte terá 5 poltronas a mais que a fileira imediatamente anterior, formando uma progressão aritmética. O projeto prevê exatamente 18 fileiras, numeradas de 1 a 18. As normas municipais de segurança contra incêndio limitam a no máximo 100 poltronas por fileira.

Modele o número de poltronas da fileira $n$ (com $n$ natural, $1 \le n \le 18$) por meio de uma função afim $f(n)$ associada a essa progressão aritmética. Em seguida, utilize $f(n)$ para determinar quantas poltronas terá a 18ª fileira (a última prevista no projeto) e para verificar se, mantendo o mesmo padrão de crescimento, seria possível acrescentar uma 19ª fileira sem violar a norma de segurança.

Qual das alternativas abaixo apresenta corretamente essas duas conclusões?

## Alternativas

- (a) A 18ª fileira terá 99 poltronas; não seria possível acrescentar a 19ª fileira, pois ela teria 104 poltronas, excedendo o limite de 100.  ← correta
- (b) A 18ª fileira terá 104 poltronas; ainda assim não seria possível acrescentar a 19ª fileira, pois ela teria 109 poltronas.
  - *erro representado:* Usou f(n) = a1 + n·r (sem subtrair 1 de n), calculando f(18) = 14 + 5(18) em vez de f(18) = 14 + 5(17), deslocando toda a sequência em uma posição.
- (c) A 18ª fileira terá 99 poltronas; seria possível acrescentar a 19ª fileira, pois ela teria exatamente 100 poltronas, respeitando o limite.
  - *erro representado:* Calculou corretamente f(18) = 99, mas ao estimar a 19ª fileira somou apenas 1 poltrona (99 + 1 = 100) em vez de somar a razão r = 5 da progressão.
- (d) A 18ª fileira terá 94 poltronas; não seria possível acrescentar a 19ª fileira, pois ela teria 99 poltronas, no limite da norma.
  - *erro representado:* Usou f(n) = a1 + (n-2)·r, tratando a segunda fileira como a de índice n=1, o que desloca a contagem uma posição para trás.

## Gabarito

A 18ª fileira terá 99 poltronas; não seria possível acrescentar a 19ª fileira, pois ela teria 104 poltronas, excedendo o limite de 100.

## Resolução

**Passo 1 — Identificar a PA:** o número de poltronas por fileira forma uma progressão aritmética de primeiro termo $a_1 = 14$ e razão $r = 5$.

**Passo 2 — Associar a PA a uma função afim:** o termo geral da PA é $a_n = a_1 + (n-1)r$. Como essa expressão é linear em $n$, ela define uma função afim $f(n) = a_1 + (n-1)r$, com domínio restrito ao conjunto discreto $\{1, 2, \dots, 18\}$ (os números das fileiras). Substituindo os valores:
$$f(n) = 14 + 5(n-1) = 5n + 9.$$

**Passo 3 — Calcular a 18ª fileira:**
$$f(18) = 5(18) + 9 = 90 + 9 = 99.$$
Logo, a última fileira do projeto (a 18ª) terá **99 poltronas**, dentro do limite de 100.

**Passo 4 — Testar a hipotética 19ª fileira:** embora o domínio original do problema seja $1 \le n \le 18$, a *lei de formação* $f(n) = 5n+9$ continuaria valendo se o padrão de crescimento fosse mantido. Assim:
$$f(19) = 5(19) + 9 = 95 + 9 = 104.$$

**Passo 5 — Comparar com a norma de segurança:** como $104 > 100$, uma 19ª fileira violaria o limite de poltronas por fileira. Portanto, **não seria possível** acrescentar essa fileira mantendo o mesmo padrão.

**Conclusão:** a 18ª fileira tem 99 poltronas, e não é possível acrescentar uma 19ª fileira sem violar a norma, pois ela teria 104 poltronas.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `5*n + 9`, parâmetros `{'sequencia': 'pa', 'a1': '14', 'razao': '5', 'grau': '1'}`
- `funcao` — expressão `5*n + 9`, esperado `99`, parâmetros `{'consulta': 'valor', 'ponto': '18'}`
- `funcao` — expressão `5*n + 9`, esperado `104`, parâmetros `{'consulta': 'valor', 'ponto': '19'}`
- `funcao` — expressão `5*n + 9`, esperado `Range(1, 19)`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 5*n + 9: grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (f(18) = 99). | (3) aprovado: Gabarito confirmado (f(19) = 104). | (4) aprovado: Gabarito confirmado (domínio Range(1, 19, 1) — restrição de contexto dentro do domínio máximo Reals).
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado apresenta dados completos (a1=14, r=5, 18 fileiras, limite de 100) e a pergunta é dupla mas bem delimitada. Pequena imprecisão fica no uso implícito da extensão do domínio para n=19, que só é esclarecido na resolução, não no enunciado — o aluno pode ficar em dúvida sobre se está autorizado a extrapolar f(n) fora do domínio original.
  - adequacao_nivel: 4/5 — O processo exigido (montar f(n), calcular f(18) e f(19), comparar com limite) é essencialmente aplicação de fórmula com verificação de condição — compatível com Bloom 'aplicar'. A estrutura de resposta é multiestrutural (dois cálculos + uma comparação), adequada ao nível declarado, sem exigir análise mais profunda (o que seria coerente, já que o nível pedido não é 'analisar').
  - alinhamento_bncc: 4/5 — O enunciado exige explicitamente a modelagem da PA por uma função afim f(n) antes de usá-la, atendendo à exigência de que a associação PA-função afim seja pedida e não apenas aplicada mecanicamente. Contudo, a questão trata do domínio discreto apenas de forma implícita na resolução (extrapolação de n=18 para n=19), sem que as alternativas exijam do aluno refletir sobre essa restrição de domínio — um ponto central da habilidade EM13MAT507 fica subexplorado nas opções de resposta, que testam apenas erros de cálculo aritmético.
  - distratores: 4/5 — Os três distratores incorretos representam erros sistemáticos plausíveis (deslocamento de índice no termo geral, confundir razão com incremento unitário, deslocamento inverso do índice), sem opções absurdas ou trivialmente descartáveis. Nenhum distrator, porém, explora um erro conceitual ligado ao domínio discreto ou à natureza da 'função afim' versus PA, o que seria mais alinhado à habilidade.
  - originalidade: 4/5 — O contexto do teatro com norma de segurança contra incêndio é razoavelmente significativo e evita o clichê mais comum de PA (juros, economia de moedas). O enunciado não entrega passo a passo explícito, evitando efeito Topaze forte, embora a menção direta a 'modele por meio de uma função afim f(n)' já indique claramente o caminho da resolução, reduzindo um pouco o desafio de descoberta.
