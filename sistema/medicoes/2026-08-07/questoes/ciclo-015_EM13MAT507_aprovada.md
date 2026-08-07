# Ciclo 015 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Considere a progressão aritmética (PA) $7, 11, 15, 19, 23, \dots$, cujo primeiro termo é $a_1 = 7$ e cuja razão é $r = 4$. Um estudante afirma que essa PA pode ser entendida como a restrição de uma função afim $f(n) = 4n + 3$ ao conjunto dos números naturais não nulos ($n \in \mathbb{N}^*$), de modo que $a_n = f(n)$ para todo $n \geq 1$. Com base nessa relação, determine o valor do vigésimo termo da PA e identifique a alternativa que descreve corretamente esse valor e a relação entre a PA e a função afim correspondente, incluindo a natureza do domínio envolvido.

## Alternativas

- (a) $a_{20} = f(20) = 4(20)+3 = 83$. A função afim $f(x) = 4x+3$ tem domínio real $\mathbb{R}$, mas a PA corresponde apenas à restrição de $f$ ao domínio discreto $\mathbb{N}^*$, de modo que $a_n = f(n)$ somente para valores inteiros positivos de $n$.  ← correta
- (b) $a_{20} = f(20) = 4(20)+3 = 83$. Como a PA é gerada por uma função afim, ela é idêntica a $f$ em todo o seu domínio: ambas estão definidas para todo $x \in \mathbb{R}$, sem qualquer restrição adicional.
  - *erro representado:* não reconhece que a PA é uma restrição discreta da função afim, tratando o domínio da PA como sendo todo o conjunto dos reais
- (c) Usando $a_n = a_1 + n\cdot r$, obtém-se $a_{20} = 7 + 20\cdot 4 = 87$, e a PA equivale à restrição de $f$ ao conjunto $\mathbb{N}^*$.
  - *erro representado:* aplica incorretamente a fórmula do termo geral da PA, usando $n$ em vez de $(n-1)$ no fator multiplicado pela razão
- (d) Como a razão é $r=4$, a função associada é $g(n) = 4n$ (sem termo constante), de modo que $a_{20} = g(20) = 80$, sendo essa a restrição de $g$ ao domínio $\mathbb{N}^*$.
  - *erro representado:* esquece de incluir o termo independente (constante) ao construir a função afim associada à PA, usando apenas o coeficiente da razão

## Gabarito

a_20 = f(20) = 83; a PA é a restrição de f(x) = 4x+3 ao domínio discreto N* (não ao domínio real R).

## Resolução

**Passo 1 — Identificar a função afim associada à PA.**

Toda PA de primeiro termo $a_1$ e razão $r$ tem termo geral
$$a_n = a_1 + (n-1)r.$$

Substituindo $a_1 = 7$ e $r = 4$:
$$a_n = 7 + (n-1)\cdot 4 = 4n + 3.$$

Essa expressão é exatamente a mesma lei da função afim $f(n) = 4n+3$: ou seja, $a_n = f(n)$.

**Passo 2 — Reconhecer a diferença de domínio.**

A função afim $f(x) = 4x+3$, como função real, tem domínio $\mathbb{R}$: podemos calcular $f$ para qualquer número real (por exemplo, $f(2{,}5) = 13$). Já a PA só existe para índices $n = 1, 2, 3, \dots$, ou seja, $n \in \mathbb{N}^*$. Assim, a PA **não é** a função $f$ inteira, mas sim sua **restrição ao domínio discreto** $\mathbb{N}^*$: os pontos $(n, a_n)$ são exatamente os pontos de $f$ com abscissa natural positiva.

**Passo 3 — Calcular o vigésimo termo.**

Usando a fórmula do termo geral:
$$a_{20} = 7 + (20-1)\cdot 4 = 7 + 76 = 83.$$

Ou, equivalentemente, avaliando a função afim em $n=20$:
$$f(20) = 4(20) + 3 = 83.$$

**Conclusão.** $a_{20} = f(20) = 83$, e a PA corresponde à função afim $f(n) = 4n+3$ restrita ao domínio $\mathbb{N}^*$ — não ao domínio real completo.

## Formalização verificável

- `funcao` — expressão `4*x + 3`, esperado `83`, parâmetros `{'consulta': 'valor', 'ponto': '20'}`
- `progressao` — expressão `-`, esperado `83`, parâmetros `{'tipo_progressao': 'pa', 'a1': '7', 'razao': '4', 'n': '20', 'consulta': 'termo'}`
- `propriedade` — expressão `-`, esperado `4*n + 3`, parâmetros `{'pontos': '[(1,7),(2,11),(3,15),(4,19)]', 'grau': '1', 'sequencia': 'pa', 'a1': '7', 'razao': '4'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (f(20) = 83). | (2) rejeitado: Divergência: domínio calculado: Reals; gabarito: Naturals. | (3) aprovado: Gabarito confirmado (termo da PA = 83). | (4) aprovado: Propriedades confirmadas para 4*n + 3: reproduz os 4 pontos dados; grau 1; coincide com a PA declarada.
  - funcao/valor=aprovado
  - funcao/dominio=rejeitado
  - progressao/termo=aprovado
  - propriedade=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 4 afirmações reprovadas. (1) aprovado: Gabarito confirmado (f(20) = 83). | (2) rejeitado: Divergência: domínio calculado: Reals; gabarito: Naturals. | (3) aprovado: Gabarito confirmado (termo da PA = 83). | (4) aprovado: Propriedades confirmadas para 4*n + 3: reproduz os 4 pontos dados; grau 1; coincide com a PA declarada. Resultado calculado independentemente: f(20) = 83 | domínio calculado: Reals | 83 | 4*n + 3. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(20) = 83). | (2) aprovado: Gabarito confirmado (termo da PA = 83). | (3) aprovado: Propriedades confirmadas para 4*n + 3: reproduz os 4 pontos dados; grau 1; coincide com a PA declarada.
  - funcao/valor=aprovado
  - progressao/termo=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado define claramente a PA, a função afim proposta, os dados (a1, r) e a tarefa (calcular a20 e julgar a relação de domínio). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A tarefa exige diferenciar o domínio real da função afim do domínio discreto da PA, o que é uma operação de análise (comparar/diferenciar), coerente com o nível declarado. Contudo, por ser múltipla escolha, a resposta se reduz a reconhecer uma afirmação pronta em vez de produzir a análise de forma autônoma, o que aproxima a estrutura de resposta de um nível relacional mais do que de análise plena (SOLO).
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente a exigência declarada: obriga o aluno a associar a PA à função afim e a discutir explicitamente a natureza do domínio (R vs N*), não se limitando à aplicação mecânica da fórmula do termo geral.
  - distratores: 5/5 — Os três distratores representam erros sistemáticos plausíveis e distintos: confundir domínio (tratar como R), erro na fórmula do termo geral (n em vez de n-1) e esquecer o termo constante na função afim. Nenhum é absurdo ou trivialmente eliminável, pois todos produzem valores numéricos plausíveis.
  - originalidade: 3/5 — O contexto é puramente teórico/formal, sem aplicação significativa a uma situação real. A pergunta segue um roteiro previsível (calcular termo + julgar afirmação sobre domínio), o que reduz a originalidade, embora evite o efeito Topaze ao não entregar passo a passo a solução no próprio enunciado.
