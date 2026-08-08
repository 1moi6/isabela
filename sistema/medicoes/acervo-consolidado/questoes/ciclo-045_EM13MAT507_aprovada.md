# Ciclo 045 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere a progressão aritmética $(a_n)$ com primeiro termo $a_1 = 7$ e razão $r = 4$, definida para $n = 1, 2, 3, \dots$

a) Determine a lei de uma função afim $f(n)$ tal que $f(n) = a_n$ para todo $n$ natural positivo, e explicite qual é o domínio dessa função.

b) Utilizando a função $f$ obtida no item (a), calcule o vigésimo termo da progressão, isto é, $a_{20}$.

## Gabarito

f(n) = 4n + 3, com domínio $\mathbb{N}^* = \{1,2,3,\dots\}$; $a_{20} = 83$

## Resolução

**a) Associando a PA a uma função afim**

O termo geral de uma PA é dado por $a_n = a_1 + (n-1)r$.

Substituindo $a_1 = 7$ e $r = 4$:

$a_n = 7 + (n-1)\cdot 4 = 7 + 4n - 4 = 4n + 3$

Essa expressão tem a forma $f(n) = 4n + 3$, que é exatamente uma função afim $f(x) = mx + b$ com coeficiente angular $m = 4$ (igual à razão $r$) e coeficiente linear $b = 3$.

Como o índice $n$ representa a posição do termo na sequência, só faz sentido para $n = 1, 2, 3, \dots$. Logo, o domínio de $f$ não é todo o conjunto dos reais (como seria numa função afim contínua), mas sim o conjunto dos números naturais positivos:

$D(f) = \mathbb{N}^* = \{1, 2, 3, \dots\}$

Ou seja, $(a_n)$ é a "restrição" da função afim $f(n) = 4n+3$ ao domínio discreto $\mathbb{N}^*$ — os pontos $(n, a_n)$ estão todos sobre a reta $y = 4x + 3$, mas apenas nos valores inteiros positivos de $x$.

**b) Cálculo de $a_{20}$**

Basta calcular $f(20)$:

$f(20) = 4 \cdot 20 + 3 = 80 + 3 = 83$

Portanto, $a_{20} = 83$.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `4*n + 3`, parâmetros `{'sequencia': 'pa', 'a1': '7', 'razao': '4', 'grau': '1'}`
- `funcao` — expressão `4*n + 3`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `4*n + 3`, esperado `83`, parâmetros `{'consulta': 'valor', 'ponto': '20'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 4*n + 3: grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (f(20) = 83).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado é preciso: dados (a1, r), o que se pede (lei de f, domínio, a20) e as condições estão explícitos, sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo exigido (aplicar a fórmula do termo geral e reconhecer/explicitar o domínio discreto) é compatível com o nível 'aplicar'. A exigência de explicitar o domínio eleva a resposta a um nível relacional (SOLO), não puramente mecânico, o que é positivo; poderia ser ainda mais rico pedindo justificativa do porquê o domínio é discreto.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente a exigência da especificação: não se limita a aplicar a fórmula do termo geral, mas exige explicitamente a associação da PA a uma função afim e o tratamento do domínio discreto (D(f) = N*), articulando PA e função afim num único problema, como pede EM13MAT507.
  - distratores: 5/5 — Não se aplica — questão discursiva.
  - originalidade: 3/5 — O contexto é puramente formal/algébrico, sem situação significativa ou aplicação prática, e a estrutura (calcular termo geral, depois término numérico) é bastante convencional em livros didáticos, ainda que o pedido de explicitar o domínio discreto seja um diferencial pouco comum.
