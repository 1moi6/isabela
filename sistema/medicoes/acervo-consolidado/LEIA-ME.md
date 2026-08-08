# Acervo consolidado — 90 questões

**Este é o acervo a usar.** Reúne as habilidades não afetadas pela primeira corrida (42 ciclos,
commit `996020b`) com as oito regeradas depois das correções (48 ciclos, commit `16dfec9`).

15 habilidades × 2 formatos × 3 dificuldades. **85 aprovadas, 5 descartadas.**
Garantia: 72 conferidas, 12 conferidas em parte, 1 sem conferência.

As corridas de origem ficam preservadas em `../acervo-2026-08-08/` e
`../acervo-2026-08-08-refeito/`, com seus próprios LEIA-ME.

## Efeito das correções

Nas oito habilidades regeradas:

| | antes | depois |
|---|---|---|
| descartes | 12 | 5 |
| reprovações de afirmação | 34 | 9 |
| aprovadas na 1ª iteração | 19 de 47 | 30 de 48 |

`funcao/minimo`, `funcao/maximo`, `propriedade` e `funcao/dominio` foram a **zero reprovações**.
A EM13MAT306, que tinha perdido quatro dos seis ciclos, não perdeu nenhum.

## As 9 reprovações restantes também são falsas

Conferidas uma a uma. Três famílias novas, todas do mesmo tipo: o verificador reprovando gabarito
correto.

**Raízes complexas onde a questão quer as reais (4 casos).** `sp.solve(x² - 8x + 20)` devolve
`[4-2i, 4+2i]`; o discriminante é −16 e o gabarito `[]` — "não há raízes reais" — está certo, mas
é reprovado por diferença de cardinalidade. Idem `(1+i)³ = 1,331`, cujas três raízes incluem uma
real, que é a resposta.

**Ponto flutuante contra racional exato (4 casos).** O Gerador escreve `1.08` numa questão de juros,
o que é natural. `800·1,08¹⁰` difere de `800·(27/25)¹⁰` em **1,1 × 10⁻¹²** — ruído de representação
—, e `simplify` não devolve zero exato.

Existe módulo para exatamente isto: `verificacao/numerica.py`, com `equivalentes()`, que compara em
pontos aleatórios com semente fixa e devolve *aprovado com ressalva numérica*. O Capítulo 4 o
descreve como uma das estratégias do Verificador. **Ele está importado e nunca é chamado.**

**Equação restrita a um domínio (1 caso).** `2cos(π(t−3)/6) + 3 = 4` tem soluções `[1, 5]`; a
questão restringe a `[0, 3]` e o gabarito `[1]` está certo. O Gerador chegou a declarar
`dominio_considerado` nos parâmetros — um nome que o código não conhece.

Seis das nove estão na EM13MAT303 (porcentagens e juros compostos), onde escrever taxa como decimal
é a coisa natural a fazer.

## O que isso significa para quem for usar o acervo

As 85 aprovadas são material válido.

Os **5 descartes continuam não servindo de espécime de erro** sem conferência manual, pela mesma
razão de antes: podem ser questões corretas descartadas por reprovação falsa.

E o saldo das três corridas com provedor real: **onze defeitos encontrados, todos do mesmo lado da
balança** — o verificador rejeitando o que está certo, nunca aprovando o que está errado. É
resultado a levar para o Capítulo 6.
