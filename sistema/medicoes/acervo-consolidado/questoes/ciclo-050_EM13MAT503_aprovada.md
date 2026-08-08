# Ciclo 050 — EM13MAT503

- **Situação:** aprovada
- **Temas:** funcao_quadratica
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** discursiva
- **Garantia obtida:** conferido_em_parte
- **Iterações:** 1

## Enunciado

Uma agência organiza passeios de van para grupos de turistas. A van comporta no máximo 60 passageiros, e a agência só realiza o passeio se houver pelo menos 15 inscritos.

O preço da passagem depende do tamanho do grupo: para 15 passageiros, o preço é R$ 90,00 por pessoa. A cada passageiro adicional além de 15, a agência reduz o preço da passagem em R$ 1,00 para TODOS os integrantes do grupo (não apenas para o excedente), como forma de incentivar grupos maiores.

Além da receita das passagens, a agência tem um custo de R$ 500,00 fixo pelo aluguel da van, mais R$ 20,00 por passageiro (referentes a seguro e lanche).

Determine o número de passageiros que a agência deve buscar para cada passeio, de modo a maximizar seu lucro, e calcule o valor desse lucro máximo.

## Gabarito

O lucro é máximo para 42 ou 43 passageiros, resultando em L = R$ 1.306,00.

## Resolução

**Passo 1 — Definir a variável e o preço por passageiro**

Seja $x$ o número de passageiros, com $x$ inteiro e $15 \le x \le 60$.

O preço inicial é R\$90,00 para $x=15$, e cai R\$1,00 para cada passageiro além de 15:
$$p(x) = 90 - 1\cdot(x-15) = 105 - x$$

**Passo 2 — Montar a receita**

$$R(x) = x \cdot p(x) = x(105-x) = 105x - x^2$$

**Passo 3 — Montar o custo**

$$C(x) = 500 + 20x$$

**Passo 4 — Montar o lucro**

$$L(x) = R(x) - C(x) = 105x - x^2 - 500 - 20x = -x^2 + 85x - 500$$

Essa é uma função quadrática com $a=-1<0$, portanto tem ponto de **máximo**.

**Passo 5 — Localizar o vértice (candidato contínuo)**

$$x_v = -\dfrac{b}{2a} = -\dfrac{85}{2\cdot(-1)} = \dfrac{85}{2} = 42{,}5$$

**Passo 6 — Ajustar ao domínio (número de passageiros é inteiro)**

Como $x$ deve ser um número inteiro de pessoas, o vértice $x=42{,}5$ não é um valor válido. Como a parábola é simétrica em torno de $x_v=42{,}5$, os dois inteiros mais próximos, $x=42$ e $x=43$, estão à mesma distância ($0{,}5$) do vértice e, portanto, produzem o **mesmo valor máximo** de $L(x)$ dentro do domínio inteiro.

**Passo 7 — Calcular o lucro nesses pontos**

$$L(42) = -(42)^2 + 85(42) - 500 = -1764 + 3570 - 500 = 1306$$
$$L(43) = -(43)^2 + 85(43) - 500 = -1849 + 3655 - 500 = 1306$$

Ambos os valores coincidem, confirmando a simetria.

**Passo 8 — Confirmar que é de fato o máximo no domínio permitido**

Como a parábola abre para baixo e $x=42$ e $x=43$ estão dentro do intervalo permitido $[15,60]$ e são os inteiros mais próximos do vértice contínuo, nenhum outro valor inteiro no domínio produz lucro maior (o lucro decresce à medida que $x$ se afasta de $42{,}5$ para qualquer lado).

**Conclusão**

A agência deve buscar **42 ou 43 passageiros** por passeio, obtendo um lucro máximo de **R\$ 1.306,00**.

## Formalização verificável

- `funcao` — expressão `-x**2 + 85*x - 500`, esperado `1306`, parâmetros `{'consulta': 'maximo', 'dominio': 'Range(15, 61)'}`
- `equacao` — expressão `Eq(-x**2 + 85*x - 500, 1306)`, esperado `[42, 43]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado_parcial — 1 de 2 afirmações conferidas; o restante não é formalizável. (1) nao_verificavel: Verificação inconclusiva: não foi possível determinar o maximo de -x**2 + 85*x - 500 em Range(15, 61, 1). Conferir manualmente. | (2) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/maximo=nao_verificavel
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado especifica claramente domínio (15 a 60 passageiros), regra de precificação (redução de R$1,00 por passageiro adicional aplicada a TODOS), custos fixos e variáveis. Não há ambiguidade lexical ou estrutural; todos os dados necessários estão presentes.
  - adequacao_nivel: 4/5 — O processo cognitivo vai um pouco além de 'aplicar' simples fórmula do vértice: exige também investigar a restrição de domínio inteiro e concluir a coexistência de dois pontos de máximo equidistantes, o que se aproxima de 'analisar' no nível SOLO relacional. Ainda assim, é compatível com 'aplicar' em um contexto de investigação, como pede a habilidade, e adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — Cumpre integralmente a EM13MAT503: pede explicitamente a investigação do ponto de máximo de uma função quadrática construída a partir de uma situação de Matemática Financeira (receita, custo e lucro), exigindo modelagem e não mera manipulação algébrica isolada.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 3/5 — O contexto de 'passeio de van' é uma variação de um problema clássico e recorrente em livros didáticos (preço decrescente por unidade adicional em locação/excursão/apartamentos). A estrutura matemática segue o modelo tradicional desse tipo de exercício, reduzindo o ineditismo, embora o contexto turístico traga alguma variação superficial.
