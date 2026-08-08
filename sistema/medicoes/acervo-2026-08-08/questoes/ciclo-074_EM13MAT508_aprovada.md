# Ciclo 074 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma bióloga monitora o crescimento de uma colônia de bactérias em laboratório. Na 1ª hora de observação, a colônia possui 500 bactérias e, a cada hora subsequente, a quantidade de bactérias dobra em relação à hora anterior, formando uma sequência numérica que descreve exatamente a população em cada hora inteira observada (n = 1, 2, 3, ...).

A bióloga também deseja representar essa mesma evolução por meio de uma função exponencial $f(x) = a\cdot b^{x}$, definida para todo número real $x$, de modo que, ao avaliar $f$ nos valores naturais correspondentes às horas medidas ($x = n$, $n = 1, 2, 3, \dots$), obtenha-se exatamente os termos da sequência de bactérias.

a) Escreva o termo geral $a_n$ da progressão geométrica que representa a população de bactérias na n-ésima hora.

b) Determine os coeficientes $a$ e $b$ da função exponencial $f(x)=a\cdot b^{x}$ que satisfaz $f(n)=a_n$ para todo $n$ natural correspondente às horas de observação, e indique qual é o domínio de interesse prático dessa função no contexto do problema.

c) Calcule a população de bactérias na 10ª e na 11ª hora de observação, usando a função $f$.

d) Determine em que hora a população atingirá exatamente 64000 bactérias, resolvendo a equação exponencial correspondente.

## Gabarito

a) $a_n = 500\cdot2^{n-1}$; b) $f(x)=250\cdot2^{x}$, com domínio prático $\mathbb{N}=\{1,2,3,\dots\}$; c) $f(10)=256000$ e $f(11)=512000$ bactérias; d) $n=8$ (8ª hora).

## Resolução

**Passo 1 — Termo geral da PG**

A população começa com $a_1 = 500$ e dobra a cada hora, logo a razão é $r = 2$. O termo geral de uma PG é $a_n = a_1 \cdot r^{\,n-1}$, portanto:
$$a_n = 500\cdot 2^{\,n-1}$$

**Passo 2 — Associando a PG à função exponencial**

Queremos uma função $f(x) = a\cdot b^{x}$ (definida para todo $x$ real) tal que $f(n) = a_n$ para os naturais $n \ge 1$ que correspondem às horas medidas. Reescrevendo o termo geral para isolar uma potência de expoente $n$ (em vez de $n-1$):
$$a_n = 500\cdot 2^{\,n-1} = 500\cdot 2^{-1}\cdot 2^{\,n} = 250\cdot 2^{\,n}$$

Logo $a = 250$ e $b = 2$, e a função é:
$$f(x) = 250\cdot 2^{x}$$

Embora $f$ esteja matematicamente definida para todo $x\in\mathbb{R}$, o **domínio de interesse prático** no problema é apenas o conjunto dos números naturais que representam as horas efetivamente observadas: $n = 1, 2, 3, \dots$, ou seja, $\mathbb{N} = \{1,2,3,\dots\}$ (S.Naturals). Fora desses valores, $f(x)$ não tem significado físico no experimento.

**Verificação:** $f(1)=250\cdot2=500=a_1$; $f(2)=250\cdot4=1000=a_2$; $f(3)=250\cdot8=2000=a_3$ — coincide com a PG, confirmando a associação.

**Passo 3 — População na 10ª e 11ª hora**

$$f(10) = 250\cdot 2^{10} = 250\cdot 1024 = 256000$$
$$f(11) = 250\cdot 2^{11} = 250\cdot 2048 = 512000$$

**Passo 4 — Hora em que a população atinge 64000 bactérias**

Resolvendo a equação exponencial:
$$250\cdot 2^{n} = 64000$$
$$2^{n} = \frac{64000}{250} = 256 = 2^{8}$$
$$n = 8$$

Portanto, a população atingirá 64000 bactérias na **8ª hora** de observação.

## Formalização verificável

- `equacao` — expressão `Eq(250*2**n, 64000)`, esperado `[8]`
- `propriedade` — expressão `-`, esperado `250*2**n`, parâmetros `{'pontos': '[(1,500),(2,1000),(3,2000)]', 'sequencia': 'pg', 'a1': '500', 'razao': '2'}`
- `funcao` — expressão `250*2**x`, esperado `256000`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `funcao` — expressão `250*2**x`, esperado `512000`, parâmetros `{'consulta': 'valor', 'ponto': '11'}`
- `funcao` — expressão `250*2**x`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 2 de 5 afirmações reprovadas. (1) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-1 - sqrt(3)*I, -1 + sqrt(3)*I]. | (2) rejeitado: Propriedade não confirmada: a expressão 500*2**n vale 1000 em n=1, mas o 1º termo da PG é 500. | (3) aprovado: Gabarito confirmado (domínio Naturals0 — restrição de contexto dentro do domínio máximo Reals). | (4) aprovado: Gabarito confirmado (f(10) = 512000). | (5) aprovado: Gabarito confirmado (f(11) = 1024000).
  - equacao=rejeitado
  - propriedade=rejeitado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 2 de 5 afirmações reprovadas. (1) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-1 - sqrt(3)*I, -1 + sqrt(3)*I]. | (2) rejeitado: Propriedade não confirmada: a expressão 500*2**n vale 1000 em n=1, mas o 1º termo da PG é 500. | (3) aprovado: Gabarito confirmado (domínio Naturals0 — restrição de contexto dentro do domínio máximo Reals). | (4) aprovado: Gabarito confirmado (f(10) = 512000). | (5) aprovado: Gabarito confirmado (f(11) = 1024000). Resultado calculado independentemente: [2, -1 - sqrt(3)*I, -1 + sqrt(3)*I] | a expressão 500*2**n vale 1000 em n=1, mas o 1º termo da PG é 500 | domínio Naturals0 — restrição de contexto dentro do domínio máximo Reals | f(10) = 512000 | f(11) = 1024000. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Propriedades confirmadas para 250*2**n: reproduz os 3 pontos dados; coincide com a PG declarada. | (3) aprovado: Gabarito confirmado (f(10) = 256000). | (4) aprovado: Gabarito confirmado (f(11) = 512000). | (5) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)).
  - equacao=aprovado
  - propriedade=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — O enunciado define bem o que é dado (PG com a1=500, r=2) e o que se pede em cada item. O único ponto que exige atenção do aluno é o deslocamento de índice entre a_n (que começa em n=1) e f(x)=a·b^x (que deve satisfazer f(n)=a_n exatamente nesses mesmos n), o que é comunicado com clareza, mas exige leitura cuidadosa para não confundir a=500 com a=250.
  - adequacao_nivel: 4/5 — A resolução do item (b) exige mais do que aplicação mecânica de fórmula: é necessário reescrever 2^(n-1) como 2^-1·2^n para encontrar a e b corretamente, o que se aproxima de 'analisar' na taxonomia SOLO (relacional), ligeiramente acima do nível 'aplicar' declarado, mas ainda compatível com ele já que a operação central é algébrica e direta. Os itens (c) e (d) são de aplicação pura. Estrutura coerente com Ensino Médio.
  - alinhamento_bncc: 5/5 — Cumpre exatamente a habilidade EM13MAT508: exige explicitamente a associação entre a PG e a função exponencial (item b), trata o domínio discreto de forma explícita ('domínio de interesse prático'), e articula os dois temas num único problema contínuo (a PG do item a alimenta a função do item b, que é usada em c e d). Não se limita a aplicar fórmulas isoladas.
  - distratores: 5/5 — Não se aplica (questão discursiva).
  - originalidade: 3/5 — O contexto de crescimento bacteriano é um clássico recorrente em livros didáticos sobre PG/exponencial. O diferencial de exigir a conversão de índice (a=250 em vez de 500) traz alguma originalidade estrutural, mas o cenário em si carece de um contexto mais inovador ou de dados que gerem discussão adicional (ex.: limitações do modelo, comparação com dados reais).
