# Ciclo 066 — EM13MAT507

- **Situação:** aprovada
- **Temas:** progressao_aritmetica, funcao_afim
- **Nível cognitivo:** analisar
- **Dificuldade:** dificil | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 1

## Enunciado

Duas progressões aritméticas de números naturais são dadas por:

$a_n = 4n - 1,\; n \in \mathbb{N}^*$ (ou seja, $3, 7, 11, 15, 19, 23, 27, \dots$)

$b_m = 6m - 3,\; m \in \mathbb{N}^*$ (ou seja, $3, 9, 15, 21, 27, \dots$)

Cada uma dessas progressões pode ser vista como a restrição ao conjunto dos números naturais positivos de uma função afim: $f(n) = 4n-1$ e $g(m) = 6m-3$, respectivamente, com $n, m$ percorrendo $\mathbb{N}^*$.

Alguns números aparecem nas duas listas (por exemplo, $3$, $15$ e $27$). Chame de $c_k$, com $k = 0, 1, 2, \dots$, o $(k+1)$-ésimo desses termos comuns, em ordem crescente.

a) Mostre que a sequência $(c_k)$ também é uma progressão aritmética e determine seu primeiro termo $c_0$ e sua razão.

b) Escreva a função afim $h: \mathbb{N} \to \mathbb{R}$ tal que $h(k) = c_k$ para todo $k \in \mathbb{N}$.

c) Quantos termos comuns às duas progressões existem entre $1$ e $2023$, inclusive?

## Gabarito

a) $(c_k)$ é PA com $c_0=3$ e razão $12$. b) $h(k)=12k+3$, $k\in\mathbb{N}$. c) $169$ termos comuns.

## Resolução

**Passo 1 — Igualar as duas funções afins nos naturais.**

Um número é termo comum às duas progressões quando existem $n, m \in \mathbb{N}^*$ tais que $f(n) = g(m)$, isto é:
$$4n - 1 = 6m - 3$$
$$4n - 6m = -2 \quad\Longrightarrow\quad 2n - 3m = -1$$

**Passo 2 — Analisar quando a solução é natural (uso do domínio discreto).**

Isolando $n$: $n = \dfrac{3m-1}{2}$. Como $n$ deve ser um número natural, $3m - 1$ precisa ser par, o que ocorre exatamente quando $m$ é ímpar (pois $3m$ tem a mesma paridade de $m$). Isso é uma restrição que só faz sentido porque o domínio de $f$ e $g$ é discreto — na reta real qualquer $m$ serviria, mas aqui só interessam os pares $(n,m)$ de naturais.

Escrevendo os ímpares como $m = 2k+1$, $k = 0,1,2,\dots$:
$$n = \frac{3(2k+1)-1}{2} = \frac{6k+2}{2} = 3k+1$$

**Passo 3 — Calcular o termo comum $c_k$.**

Substituindo em $f(n) = 4n-1$:
$$c_k = 4(3k+1) - 1 = 12k + 3$$

(Confirmação por $g$: $b_m = 6(2k+1)-3 = 12k+6-3 = 12k+3$ — mesma expressão.)

**Passo 4 — Reconhecer a nova PA.**

$c_k = 12k+3$ é uma função afim de $k$, logo $(c_k)$ é uma PA de primeiro termo $c_0 = 3$ e razão $12$ (note que $12 = \text{mmc}(4,6)$, resultado esperado quando se intersectam duas PAs).

**Passo 5 — Função afim associada.**

$$h: \mathbb{N} \to \mathbb{R}, \qquad h(k) = 12k+3$$
com domínio discreto $\mathbb{N} = \{0,1,2,\dots\}$, coeficiente angular (razão) $12$ e coeficiente linear $3$.

**Passo 6 — Contar os termos comuns até 2023.**

Queremos o maior $k$ natural tal que $h(k) \le 2023$:
$$12k+3 \le 2023 \;\Longrightarrow\; 12k \le 2020 \;\Longrightarrow\; k \le \frac{2020}{12} = 168{,}33\ldots$$

Como $k$ é natural, o maior valor possível é $k=168$. Verificando os limites:
$$h(168) = 12(168)+3 = 2019 \le 2023 \quad\checkmark$$
$$h(169) = 12(169)+3 = 2031 > 2023 \quad(\text{excede})$$

Os valores válidos de $k$ são $0, 1, 2, \dots, 168$, totalizando:
$$168 - 0 + 1 = 169 \text{ termos comuns}$$

## Formalização verificável

- `propriedade` — expressão `-`, esperado `12*k + 3`, parâmetros `{'sequencia': 'pa', 'a1': '3', 'razao': '12', 'pontos': '[(0,3),(1,15),(2,27)]', 'grau': '1'}`
- `funcao` — expressão `12*k + 3`, esperado `S.Naturals`, parâmetros `{'consulta': 'dominio'}`
- `funcao` — expressão `12*k + 3`, esperado `2019`, parâmetros `{'consulta': 'valor', 'ponto': '168'}`
- `funcao` — expressão `12*k + 3`, esperado `2031`, parâmetros `{'consulta': 'valor', 'ponto': '169'}`
- `progressao` — expressão `-`, esperado `2019`, parâmetros `{'tipo_progressao': 'pa', 'a1': '3', 'razao': '12', 'n': '169', 'consulta': 'termo'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 5 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 12*k + 3: reproduz os 3 pontos dados; grau 1; coincide com a PA declarada. | (2) aprovado: Gabarito confirmado (domínio Naturals — restrição de contexto dentro do domínio máximo Reals). | (3) aprovado: Gabarito confirmado (f(168) = 2019). | (4) aprovado: Gabarito confirmado (f(169) = 2031). | (5) aprovado: Gabarito confirmado (termo da PA = 2019).
  - propriedade=aprovado
  - funcao/dominio=aprovado
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - progressao/termo=aprovado
- **Crítico:** aprovou
  - clareza: 4/5 — Enunciado bem estruturado, com dados completos e itens claramente delimitados. Pequena ambiguidade menor: não se explicita que k=0 corresponde ao primeiro termo comum antes de defini-lo, mas isso é esclarecido na sequência do texto. Notação c_k e uso de N* vs N é consistente.
  - adequacao_nivel: 4/5 — O item (a) exige analisar a estrutura de interseção de duas PAs e justificar por que ela também é uma PA (nível analisar/relacional), e o item (c) exige aplicar essa análise a um problema de contagem com atenção a limites discretos. Há, porém, um forte scaffolding na resolução esperada (passos de dedução matemática) que poderia reduzir a exigência de análise independente do aluno se o enunciado fosse mais diretivo — mas como está, o enunciado apenas dá o resultado do fenômeno (números aparecem nas duas listas) sem indicar o caminho, preservando o nível analítico.
  - alinhamento_bncc: 5/5 — A questão articula explicitamente PA e função afim: define as PAs como restrições de funções afins ao domínio discreto N*, pede para mostrar que a interseção também é uma PA (exigindo raciocínio sobre paridade/domínio discreto, não mera aplicação de fórmula), e pede a função afim h associada. O item (c) usa essa articulação para resolver um problema de contagem, tratando meticulosamente a diferença entre domínio real e discreto (uso de floor/desigualdade). Cumpre integralmente as exigências: articulação real, tratamento do domínio discreto, e não é mera aplicação de fórmula.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 4/5 — O problema de interseção de duas PAs é conhecido em livros de PA, mas a forma de apresentação — enfatizando a interpretação como restrição de funções afins a domínio discreto e articulando com o item (c) de contagem até 2023 — traz um contexto e uma costura conceitual pouco comuns em versões didáticas tradicionais. Não há 'efeito Topaze' explícito: o enunciado não entrega o caminho da resolução, apenas o fenômeno observado (números comuns como exemplo).
