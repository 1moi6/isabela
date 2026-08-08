# Ciclo 019 — EM13MAT403

- **Situação:** aprovada
- **Temas:** funcao_exponencial, funcao_logaritmica
- **Nível cognitivo:** entender
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Um biólogo estuda o crescimento de uma cultura de bactérias em laboratório. O número de bactérias, em milhares, após $t$ horas (com $t$ podendo assumir qualquer valor real, inclusive negativo, para fins de modelagem matemática) é dado por $f(t) = 2^t$. Para descobrir quanto tempo é necessário para que a cultura atinja uma quantidade $N$ (em milhares) de bactérias, o biólogo utiliza a função inversa $g(N) = \log_2(N)$. As duas funções são representadas no mesmo plano cartesiano. Com base na análise do domínio, da imagem e do comportamento de crescimento de $f$ e $g$, assinale a alternativa correta.

## Alternativas

- (a) O domínio de f (todos os reais) é igual à imagem de g, e a imagem de f (reais positivos) é igual ao domínio de g; ambas as funções são crescentes em seus domínios.  ← correta
- (b) O domínio de f é o conjunto dos reais positivos e a imagem de g é o conjunto de todos os reais, sendo f decrescente e g crescente.
  - *erro representado:* Confundir o domínio da função exponencial com sua imagem, atribuindo a f o intervalo dos positivos em vez dos reais, e erroneamente classificar f como decrescente.
- (c) O domínio de f coincide com a imagem de g, mas g é decrescente enquanto f é crescente.
  - *erro representado:* Achar que a função logarítmica de base maior que 1 é decrescente, generalizando incorretamente o comportamento de logaritmos com base entre 0 e 1.
- (d) Como f e g são inversas, ambas têm exatamente o mesmo domínio (os reais) e a mesma imagem (os reais positivos), sendo ambas crescentes.
  - *erro representado:* Não compreender que funções inversas trocam domínio e imagem entre si, assumindo erroneamente que ambas compartilham domínio e imagem idênticos.

## Gabarito

O domínio de f (todos os reais) é igual à imagem de g, e a imagem de f (reais positivos) é igual ao domínio de g; ambas as funções são crescentes em seus domínios.

## Resolução

**Passo 1 — Domínio e imagem de $f(t) = 2^t$.**

A função exponencial $f(t) = 2^t$ está definida para qualquer valor real de $t$, logo seu domínio é $D_f = \mathbb{R}$. Como $2^t > 0$ para todo $t$, sua imagem é $Im_f = (0, +\infty)$.

**Passo 2 — Domínio e imagem de $g(N) = \log_2(N)$.**

O logaritmo só é definido para argumentos positivos, então $D_g = (0, +\infty)$. Como o logaritmo assume qualquer valor real (positivo, negativo ou zero), sua imagem é $Im_g = \mathbb{R}$.

**Passo 3 — Relação entre domínio e imagem.**

Como $f$ e $g$ são funções inversas uma da outra, o domínio de uma corresponde exatamente à imagem da outra: $D_f = Im_g = \mathbb{R}$ e $D_g = Im_f = (0, +\infty)$.

**Passo 4 — Crescimento.**

Como a base $2 > 1$, a função exponencial $f(t) = 2^t$ é crescente em todo o seu domínio. Do mesmo modo, como a base do logaritmo é $2 > 1$, a função $g(N) = \log_2(N)$ também é crescente em todo o seu domínio.

**Conclusão.** O domínio de $f$ (os reais) coincide com a imagem de $g$, e a imagem de $f$ (reais positivos) coincide com o domínio de $g$; ambas as funções são crescentes.

## Formalização verificável

- `funcao` — expressão `2**x`, esperado `S.Reals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `2**x`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `2**x`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `log(x, 2)`, esperado `Interval.open(0, oo)`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `log(x, 2)`, esperado `S.Reals`, parâmetros `{'consulta': 'imagem'}`
- `funcao` — expressão `log(x, 2)`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 5 de 6 afirmações conferidas; o restante não é formalizável. (1) aprovado: Gabarito confirmado (domínio de 2**x: Interval(-oo, oo)). | (2) nao_verificavel: Verificação inconclusiva: não foi possível determinar a imagem de 2**x. Conferir manualmente. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) aprovado: Gabarito confirmado (domínio de log(x)/log(2): Interval.open(0, oo)). | (5) aprovado: Gabarito confirmado (imagem de log(x)/log(2): Interval(-oo, oo)). | (6) aprovado: Gabarito confirmado (crescente em Interval.open(0, oo)).
  - funcao/dominio=aprovado
  - funcao/imagem=nao_verificavel
  - funcao/crescimento=aprovado
  - funcao/dominio=aprovado
  - funcao/imagem=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado é compreensível e define claramente f, g e a tarefa. A ressalva sobre t negativo 'para fins de modelagem' é um pouco artificial, mas evita ambiguidade sobre o domínio de f. Não há dados faltantes.
  - adequacao_nivel: 4/5 — A tarefa exige relacionar domínio, imagem e crescimento de duas funções inversas, o que é coerente com 'entender' em estrutura relacional (SOLO). Não é mera memorização, mas também não exige análise gráfica genuína, ficando no limite superior do nível declarado.
  - alinhamento_bncc: 3/5 — A questão articula exponencial e logarítmica num único problema e compara domínio/imagem/crescimento, atendendo parcialmente à habilidade. Porém, a habilidade pede explicitamente comparação via 'representações em plano cartesiano', e a questão apenas menciona o plano cartesiano sem de fato explorar uma representação gráfica — a resolução é puramente algébrica/simbólica. Além disso, o enunciado já informa que g é a inversa de f, reduzindo a exigência de o aluno inferir essa relação a partir das representações.
  - distratores: 4/5 — Os três distratores representam erros plausíveis (troca domínio/imagem, crença de que log de base >1 é decrescente, e crença de que funções inversas compartilham domínio/imagem idênticos). Nenhum é absurdo ou trivialmente eliminável, embora o distrator 4 seja um pouco mais fácil de descartar por quem sabe a definição básica de função inversa.
  - originalidade: 3/5 — O contexto de crescimento bacteriano é razoavelmente comum em livros didáticos, e o enunciado revela explicitamente que g é a função inversa de f, o que constitui um efeito Topaze: essa informação praticamente entrega a relação domínio/imagem que deveria ser deduzida pelo aluno a partir da análise das representações.
