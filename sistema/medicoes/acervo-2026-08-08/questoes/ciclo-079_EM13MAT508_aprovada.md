# Ciclo 079 — EM13MAT508

- **Situação:** aprovada
- **Temas:** progressao_geometrica, funcao_exponencial
- **Nível cognitivo:** analisar
- **Dificuldade:** facil | **Natureza:** teorica | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Considere a progressão geométrica (PG) $(a_n)$ dada por $5, 15, 45, 135, \dots$, em que $n$ é um número natural não nulo ($n = 1, 2, 3, \dots$) e $a_1$ é o primeiro termo. Deseja-se representar essa PG por meio de uma função exponencial $f$, definida apenas para os índices naturais da sequência, tal que $f(n) = a_n$ para todo $n \geq 1$. Assinale a alternativa que apresenta corretamente a lei de $f$ e o domínio no qual ela deve ser definida para coincidir exatamente com essa PG.

## Alternativas

- (a) $f(n) = 5\cdot 3^{n-1}$, definida para $n \in \mathbb{N}^{*} = \{1,2,3,\dots\}$  ← correta
- (b) $f(n) = 5\cdot 3^{n}$, definida para $n \in \mathbb{N}^{*} = \{1,2,3,\dots\}$
  - *erro representado:* Esqueceu de subtrair 1 do expoente, como se o índice da PG começasse em n=0 em vez de n=1.
- (c) $f(x) = 5\cdot 3^{x-1}$, definida para todo $x \in \mathbb{R}$
  - *erro representado:* Trata a função como contínua em toda a reta real, ignorando que a PG só existe para índices naturais (domínio discreto).
- (d) $f(n) = 3\cdot 5^{n-1}$, definida para $n \in \mathbb{N}^{*} = \{1,2,3,\dots\}$
  - *erro representado:* Trocou os papéis do primeiro termo (a1=5) e da razão (q=3) na fórmula do termo geral.

## Gabarito

Alternativa A: $f(n) = 5\cdot 3^{n-1}$, com domínio $n \in \mathbb{N}^{*}$.

## Resolução

**Passo 1 — Identificar os elementos da PG.**

O primeiro termo é $a_1 = 5$. A razão é obtida dividindo um termo pelo anterior: $q = \dfrac{15}{5} = 3$ (confirma-se com $\dfrac{45}{15}=3$).

**Passo 2 — Fórmula do termo geral da PG.**

Para uma PG, $a_n = a_1 \cdot q^{\,n-1}$. Substituindo os valores:
$$a_n = 5 \cdot 3^{\,n-1}$$

Verificação: $a_1 = 5\cdot 3^0 = 5$; $a_2 = 5\cdot 3^1 = 15$; $a_3 = 5\cdot 3^2 = 45$. Confere com a sequência dada.

**Passo 3 — Associar a PG a uma função exponencial.**

Uma PG é exatamente a restrição de uma função exponencial do tipo $f(x) = a_1\cdot q^{x-1}$ ao conjunto dos índices naturais $\{1,2,3,\dots\}$. Ou seja, definimos
$$f(n) = 5\cdot 3^{\,n-1}, \quad n \in \mathbb{N}^{*} = \{1,2,3,\dots\}$$

É essencial destacar que, embora a expressão algébrica $5\cdot 3^{x-1}$ também faça sentido para $x$ real, a função que **representa a PG** só está definida nos naturais — o domínio discreto é parte da definição, pois a PG só existe para índices inteiros positivos.

**Passo 4 — Conferência com um valor específico.**

Para $n=5$: $f(5) = 5\cdot 3^{4} = 5\cdot 81 = 405$, que é de fato o quinto termo da PG ($5,15,45,135,405,\dots$).

**Conclusão.** A função que representa corretamente a PG, com o domínio apropriado, é $f(n) = 5\cdot 3^{n-1}$, definida para $n \in \mathbb{N}^{*}$.

## Formalização verificável

- `funcao` — expressão `5*3**(x-1)`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `5*3**(x-1)`, esperado `405`, parâmetros `{'consulta': 'valor', 'ponto': '5'}`
- `propriedade` — expressão `-`, esperado `5*3**(n-1)`, parâmetros `{'pontos': '[(1,5),(2,15),(3,45)]', 'sequencia': 'pg', 'a1': '5', 'razao': '3'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Interval(-oo, oo)). | (2) aprovado: Gabarito confirmado (f(5) = 405). | (3) aprovado: Propriedades confirmadas para 5*3**(n - 1): reproduz os 3 pontos dados; coincide com a PG declarada.
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - propriedade=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — O enunciado deixa claro os dados (a1=5, razão obtida da sequência), a tarefa (encontrar f(n) e seu domínio) e a condição de coincidência com a PG. Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 3/5 — A maior parte do esforço cognitivo exigido é aplicação direta da fórmula do termo geral (a1·q^(n-1)), o que corresponde a 'aplicar' na taxonomia de Bloom. A camada de 'analisar' fica restrita a uma decisão binária (domínio discreto vs. contínuo), que é relevante mas pouco elaborada — não exige comparar múltiplas representações ou justificar relações mais complexas. Em termos de SOLO, a resposta é essencialmente multiestrutural (calcular a1, q, montar a lei, escolher domínio), sem exigir uma integração relacional mais rica típica de 'analisar'.
  - alinhamento_bncc: 4/5 — A questão atende ao requisito específico de exigir explicitamente a articulação entre PG e função exponencial com domínio discreto — isso não é apenas 'aplicar a fórmula do termo geral', pois o enunciado força o aluno a decidir sobre o domínio apropriado, e os distratores exploram exatamente essa confusão. Ainda assim, o peso da tarefa recai fortemente sobre o cálculo do termo geral, e a articulação com domínio é tratada por uma escolha binária, não por uma construção mais elaborada da relação PG-função.
  - distratores: 5/5 — Cada distrator representa um erro sistemático plausível: erro de deslocamento de índice, confusão discreto/contínuo, e troca de papéis entre a1 e q. Nenhum é absurdo ou trivialmente eliminável sem raciocínio.
  - originalidade: 4/5 — Foge do padrão mecânico de 'ache o termo geral', ao introduzir explicitamente a reflexão sobre domínio discreto vs. contínuo, um ponto pouco explorado em livros didáticos tradicionais. Falta, porém, um contexto aplicado ou situação-problema que tornasse o enunciado mais significativo; é ainda um exercício estritamente formal.
