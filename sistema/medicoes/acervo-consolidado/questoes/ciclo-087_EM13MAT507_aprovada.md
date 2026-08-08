# Ciclo 087 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere a progressão aritmética $(a_n)$ com primeiro termo $a_1 = 7$ e razão $r = 4$: $(7, 11, 15, 19, 23, \dots)$. Essa PA pode ser vista como a restrição da função afim $f(x) = 4x + 3$ ao conjunto dos números naturais não nulos, de modo que $a_n = f(n)$ para todo $n \geq 1$ (o gráfico da PA é o conjunto de pontos discretos $(n, a_n)$ sobre a reta que representa $f$).

Qual é o menor termo dessa PA que é maior do que 100?

## Alternativas

- (a) 103  ← correta
- (b) 99
  - *erro representado:* Arredondou o valor real da solução (24,25) para baixo, tomando n=24 em vez do menor natural maior que 24,25, obtendo um termo que na verdade não satisfaz a condição 'maior que 100'.
- (c) 107
  - *erro representado:* Usou a fórmula incorreta do termo geral, a_n = a1 + n·r (sem o deslocamento n-1), aplicando-a a n=25: 7+25·4=107.
- (d) 100
  - *erro representado:* Tratou o índice como podendo ser o valor real da fronteira da inequação (x=24,25) e substituiu diretamente na função afim, calculando f(24,25)=100 em vez de reconhecer que o domínio da PA é discreto e buscar o menor natural correspondente.

## Gabarito

103

## Resolução

**Passo 1 — Associar a PA à função afim.**
O termo geral da PA é $a_n = a_1 + (n-1)r = 7 + 4(n-1) = 4n + 3$. Logo, a PA corresponde à função afim $f(x) = 4x+3$ restrita aos naturais não nulos, isto é, $a_n = f(n)$, com $n \in \{1, 2, 3, \dots\}$.

**Passo 2 — Resolver a condição sobre os números reais.**
Queremos o menor termo maior que 100, ou seja, o menor $n$ tal que $f(n) > 100$. Primeiro resolvemos a inequação como se $x$ fosse real:
$$4x + 3 > 100 \implies 4x > 97 \implies x > 24{,}25.$$

**Passo 3 — Voltar ao domínio discreto da PA.**
Como $n$ representa a posição de um termo, ele precisa ser um número **natural**. O menor número natural maior que $24{,}25$ é $n = 25$ (e não $24$, que não satisfaz a inequação, nem $24{,}25$, que não é índice de termo algum).

**Passo 4 — Calcular o termo.**
$$a_{25} = f(25) = 4(25) + 3 = 103.$$

Como verificação: $a_{24} = 4(24)+3 = 99 < 100$ e $a_{25} = 103 > 100$, confirmando que $a_{25}=103$ é o menor termo da PA maior que 100.

## Formalização verificável

- `progressao` — expressão `-`, esperado `103`, parâmetros `{'tipo_progressao': 'pa', 'a1': '7', 'razao': '4', 'n': '25', 'consulta': 'termo'}`
- `funcao` — expressão `4*x + 3`, esperado `103`, parâmetros `{'consulta': 'valor', 'ponto': '25'}`
- `funcao` — expressão `4*x + 3`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (termo da PA = 103). | (2) aprovado: Gabarito confirmado (f(25) = 103). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals).
  - progressao/termo=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado apresenta claramente os dados (a1, r, os primeiros termos), a condição de domínio discreto e a pergunta é inequívoca: encontrar o menor termo da PA maior que 100. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido (resolver a inequação linear no domínio real e depois ajustar para o domínio natural) corresponde ao nível 'aplicar': o aluno usa uma relação conhecida (PA/função afim) em uma situação nova que exige atenção à natureza discreta do domínio. A estrutura de resposta é multiestrutural/relacional (relaciona dois conceitos), coerente com o nível declarado. O conteúdo é plenamente compatível com o Ensino Médio.
  - alinhamento_bncc: 3/5 — A questão trata explicitamente o domínio discreto da PA e exige, na resolução, a diferenciação entre a solução real da inequação (x>24,25) e o índice natural correspondente (n=25) — isso é uma articulação genuína entre PA e função afim, não apenas aplicação mecânica do termo geral. Entretanto, a associação PA↔função afim é dada pronta no enunciado ('Essa PA pode ser vista como a restrição da função afim f(x)=4x+3...'), o que reduz a exigência de que o próprio aluno *identifique e associe* a sequência à função, tarefa central da habilidade EM13MAT507. O aluno poderia resolver o problema apenas com a fórmula do termo geral da PA, sem processar de fato o conceito de 'restrição de domínio', usando a menção à função afim como mera curiosidade decorativa.
  - distratores: 5/5 — Os quatro distratores refletem errosسistemáticos plausíveis: arredondamento incorreto do índice (99), uso de fórmula errada do termo geral (107), e confusão entre o valor real de fronteira da inequação e um índice de termo (100). Nenhum é trivialmente eliminável nem absurdo.
  - originalidade: 3/5 — O contexto é puramente formal, sem aplicação significativa, e reproduz um formato clássico de exercício de PA. Além disso, entregar pronta a fórmula da função afim equivalente configura um leve 'efeito Topaze', pois pavimenta metade do raciocínio que a habilidade pretende que o aluno construa (a identificação da relação PA-função afim).
