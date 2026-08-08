# Ciclo 035 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Considere a progressão aritmética (PA): 5, 8, 11, 14, 17, ...

a) Escreva a função afim $f(n)$ que, para cada posição $n$ (com $n = 1, 2, 3, \dots$), fornece o valor do termo correspondente dessa PA. Indique também qual é o domínio dessa função, justificando por que ele não pode ser o conjunto dos números reais.

b) Utilizando a função $f(n)$ obtida no item a), calcule o vigésimo termo ($n=20$) da PA.

## Gabarito

f(n) = 3n + 2, com domínio n ∈ ℕ* (naturais positivos); f(20) = 62.

## Resolução

**Item a) — Associando a PA a uma função afim**

Numa PA, cada termo é obtido somando-se ao primeiro termo um múltiplo da razão:
$$a_n = a_1 + (n-1)\,r$$

Aqui $a_1 = 5$ e $r = 3$. Substituindo:
$$a_n = 5 + (n-1)\cdot 3 = 5 + 3n - 3 = 3n + 2$$

Essa expressão, $f(n) = 3n+2$, é exatamente uma **função afim** ($f(n) = an+b$ com $a=3$ e $b=2$), pois cada termo da PA cresce sempre o mesmo valor (a razão $r=3$) quando $n$ aumenta em 1 — o que corresponde geometricamente à inclinação constante de uma reta.

Porém, diferentemente de uma função afim "comum" definida em $\mathbb{R}$, aqui $n$ representa a **posição do termo na sequência** (1º termo, 2º termo, 3º termo, ...). Não faz sentido falar em "termo número $2{,}5$" ou "termo número $-3$". Por isso o domínio de $f$ deve ser restrito ao conjunto dos números naturais positivos:
$$D(f) = \mathbb{N}^* = \{1, 2, 3, 4, \dots\}$$

Ou seja, a PA é a função afim $f(n) = 3n+2$ com domínio discreto $\mathbb{N}^*$, enquanto a reta $y = 3x+2$ (com $x \in \mathbb{R}$) é o "gráfico contínuo" que contém todos os pontos $(n, a_n)$ da PA.

**Verificação com os termos dados:**
- $f(1) = 3(1)+2 = 5$ ✓
- $f(2) = 3(2)+2 = 8$ ✓
- $f(3) = 3(3)+2 = 11$ ✓

**Item b) — Cálculo do 20º termo**

Basta substituir $n = 20$ na função encontrada:
$$f(20) = 3(20) + 2 = 60 + 2 = 62$$

Logo, o vigésimo termo da PA é $a_{20} = 62$.

## Formalização verificável

- `funcao` — expressão `3*n + 2`, esperado `62`, parâmetros `{'consulta': 'valor', 'ponto': '20'}`
- `funcao` — expressão `3*n + 2`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `propriedade` — expressão `-`, esperado `3*n + 2`, parâmetros `{'pontos': '[(1,5),(2,8),(3,11)]', 'grau': '1', 'sequencia': 'pa', 'a1': '5', 'razao': '3'}`
- `progressao` — expressão `-`, esperado `62`, parâmetros `{'tipo_progressao': 'pa', 'a1': '5', 'razao': '3', 'n': '20', 'consulta': 'termo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 3 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 3*n + 2 tem termo de grau 0 (2), fora da forma a*n. | (2) aprovado: Gabarito confirmado (termo da PA = 62). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals).
  - propriedade=rejeitado
  - progressao/termo=aprovado
  - funcao/dominio=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 3 afirmações reprovadas. (1) rejeitado: Propriedade não confirmada: a expressão 3*n + 2 tem termo de grau 0 (2), fora da forma a*n. | (2) aprovado: Gabarito confirmado (termo da PA = 62). | (3) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). Resultado calculado independentemente: a expressão 3*n + 2 tem termo de grau 0 (2), fora da forma a*n | 62 | domínio Naturals — restrição de contexto dentro do domínio máximo Reals. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(20) = 62). | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Propriedades confirmadas para 3*n + 2: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (4) aprovado: Gabarito confirmado (termo da PA = 62).
  - funcao/valor=aprovado
  - funcao/dominio=aprovado
  - propriedade=aprovado
  - progressao/termo=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado especifica claramente a PA, a tarefa (função afim, domínio, justificativa, cálculo do 20º termo). Não há ambiguidade lexical ou estrutural; dados completos e suficientes.
  - adequacao_nivel: 4/5 — A construção da função a partir do termo geral é de fato 'aplicar', mas a exigência de justificar por que o domínio não pode ser ℝ demanda compreensão conceitual (aproxima-se de 'entender/analisar' na taxonomia SOLO, nível relacional). Ainda compatível com o nível declarado, mas levemente acima do estritamente 'aplicar'.
  - alinhamento_bncc: 5/5 — A questão cumpre exatamente a exigência: não se limita a aplicar a fórmula do termo geral, mas exige explicitamente a associação PA↔função afim e a discussão do domínio discreto, articulando os dois temas em um único problema, como pede EM13MAT507.
  - distratores: 5/5 — não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — A estrutura (dado uma PA, deduzir f(n)=an+b e calcular um termo) é bastante convencional e recorrente em livros didáticos. Falta um contexto significativo ou uma situação-problema que dê sentido prático à discussão do domínio discreto, o que reduziria o efeito 'exercício de manual'.
