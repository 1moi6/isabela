# Ciclo 003 — EM13MAT302

- **Situação:** aprovada
- **Temas:** funcao_afim
- **Nível cognitivo:** aplicar
- **Dificuldade:** media | **Natureza:** teorica | **Formato:** discursiva
- **Garantia obtida:** conferido
- **Iterações:** 2

## Enunciado

Uma empresa de transporte por aplicativo cobra uma tarifa composta por um valor fixo (bandeirada) somado a um valor proporcional à distância percorrida, medida em quilômetros. Um passageiro que percorreu 4 km pagou R$ 18,00 pela corrida, e outro passageiro que percorreu 10 km pagou R$ 36,00.

a) Determine a lei que expressa o custo $C(d)$ de uma corrida (em reais) em função da distância $d$ percorrida (em quilômetros), sabendo que essa relação é modelada por uma função polinomial de 1º grau.

b) Utilizando a lei obtida, calcule quanto pagará um passageiro que percorrer 15 km.

c) Determine a distância percorrida por um passageiro que pagou R$ 81,00 pela corrida.

## Gabarito

C(d) = 3d + 6; custo para 15 km = R$ 51,00; distância para R$ 81,00 = 25 km

## Resolução

**1. Reconhecendo o modelo**

Como o custo é composto por uma parte fixa (bandeirada) e uma parte que cresce proporcionalmente à distância, a situação é modelada por uma função afim:
$$C(d) = a\,d + b$$
onde $a$ é o valor cobrado por quilômetro e $b$ é a bandeirada fixa.

**2. Montando o sistema com os dados do enunciado**

Para $d = 4$ km, $C = 18$:
$$4a + b = 18$$

Para $d = 10$ km, $C = 36$:
$$10a + b = 36$$

**3. Resolvendo o sistema**

Subtraindo a primeira equação da segunda:
$$(10a + b) - (4a + b) = 36 - 18$$
$$6a = 18 \implies a = 3$$

Substituindo em $4a + b = 18$:
$$4(3) + b = 18 \implies b = 6$$

Logo, a lei da função é:
$$C(d) = 3d + 6$$

**4. Item (b): custo para 15 km**

$$C(15) = 3(15) + 6 = 45 + 6 = 51$$

O passageiro pagará **R$ 51,00**.

**5. Item (c): distância para custo de R$ 81,00**

$$3d + 6 = 81$$
$$3d = 75$$
$$d = 25$$

O passageiro percorreu **25 km**.

## Formalização verificável

- `propriedade` — expressão `-`, esperado `3*d + 6`, parâmetros `{'pontos': '[(4,18),(10,36)]', 'grau': '1'}`
- `funcao` — expressão `3*x + 6`, esperado `51`, parâmetros `{'consulta': 'valor', 'ponto': '15'}`
- `equacao` — expressão `Eq(3*x + 6, 81)`, esperado `[25]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado. | (2) aprovado: Gabarito confirmado (f(4) = 19).
  - equacao=aprovado
  - funcao/valor=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: dá a forma geral f(x)=ax+b, apresenta duas condições numéricas claras e pede explicitamente a lei de f e o valor de f(4). Não há ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — A tarefa exige montar e resolver um sistema linear a partir de duas condições, o que é compatível com o nível 'aplicar' (uso de procedimento conhecido em situação nova). A resposta é multiestrutural (determinar a, depois b, depois f(4)), coerente com a exigência, mas não avança a análise ou justificativa do porquê do modelo, ficando no limite inferior do nível declarado.
  - alinhamento_bncc: 2/5 — A habilidade EM13MAT302 exige resolver/elaborar problemas cujo MODELO seja uma função afim, em contextos diversos, e a especificação veda entregar o modelo pronto quando o nível é 'aplicar' ou superior. Aqui f(x)=ax+b é fornecida explicitamente no enunciado, e a tarefa se reduz a resolver um sistema de equações lineares em a e b — não há contextualização nem necessidade de o aluno reconhecer ou construir o modelo afim a partir de uma situação. Isso descumpre diretamente a exigência central da especificação, mesmo que o conteúdo 'função afim' esteja presente.
  - distratores: 5/5 — Não se aplica — questão discursiva, sem alternativas.
  - originalidade: 2/5 — É um exercício-padrão de livro didático (dado f(x)=ax+b, montar sistema com duas condições e resolver), sem contexto significativo. O enunciado não figura o 'efeito Topaze' de pistas excessivas, mas também não traz nenhum elemento de contextualização que diferencie a questão de milhares de exercícios equivalentes já conhecidos.
  - *sugestões:* Reescreva a situação em um contexto realista (por exemplo, custo de um serviço, conversão de unidades, tarifa com taxa fixa e variável, distância percorrida ao longo do tempo) em que os dados numéricos correspondam a duas informações do contexto (não à forma f(x)=ax+b diretamente). O aluno deve primeiro reconhecer que a situação é modelada por uma função afim e só então construir a lei f(x)=ax+b a partir das informações contextuais, em vez de receber essa forma já explicitada no enunciado. Mantenha a mesma estrutura matemática (duas equações lineares em a e b), mas troque a apresentação abstrata por um problema de aplicação real, garantindo que a etapa de 'traduzir o contexto em modelo matemático' seja parte da tarefa cognitiva exigida — isso atende à exigência da BNCC de não entregar o modelo pronto no nível 'aplicar' e evita o caráter de exercício mecânico repetido de livros didáticos.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Reescreva a situação em um contexto realista (por exemplo, custo de um serviço, conversão de unidades, tarifa com taxa fixa e variável, distância percorrida ao longo do tempo) em que os dados numéricos correspondam a duas informações do contexto (não à forma f(x)=ax+b diretamente). O aluno deve primeiro reconhecer que a situação é modelada por uma função afim e só então construir a lei f(x)=ax+b a partir das informações contextuais, em vez de receber essa forma já explicitada no enunciado. Mantenha a mesma estrutura matemática (duas equações lineares em a e b), mas troque a apresentação abstrata por um problema de aplicação real, garantindo que a etapa de 'traduzir o contexto em modelo matemático' seja parte da tarefa cognitiva exigida — isso atende à exigência da BNCC de não entregar o modelo pronto no nível 'aplicar' e evita o caráter de exercício mecânico repetido de livros didáticos.

### Iteração 2

- **Verificador:** aprovado — Todas as 3 afirmações conferidas. (1) aprovado: Propriedades confirmadas para 3*d + 6: reproduz os 2 pontos dados; grau 1. | (2) aprovado: Gabarito confirmado (f(15) = 51). | (3) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - propriedade=aprovado
  - funcao/valor=aprovado
  - equacao=aprovado
- **Crítico:** aprovou
  - clareza: 5/5 — Enunciado explicita claramente os dados (dois pares distância/custo), a incógnita (lei de formação) e os itens b) e c) exigem aplicações diretas da lei, sem ambiguidade lexical ou estrutural.
  - adequacao_nivel: 4/5 — O processo cognitivo exigido (montar sistema, resolver, aplicar a lei, inverter para achar d) corresponde bem ao nível 'aplicar' declarado, com estrutura relacional (SOLO) coerente. Poderia exigir um passo extra de interpretação/justificativa para elevar ainda mais o nível cognitivo, mas está adequado ao Ensino Médio.
  - alinhamento_bncc: 5/5 — A questão não entrega o modelo pronto: o aluno precisa construir a função afim a partir de dois pontos dados, cumprindo exatamente a exigência de 'resolver e elaborar problemas cujos modelos são funções polinomiais de 1º grau' (EM13MAT302). Os três itens articulam a construção e o uso do modelo em um único problema coeso, não são apenas tarefas isoladas.
  - distratores: 5/5 — Não se aplica (questão discursiva, sem alternativas).
  - originalidade: 3/5 — O contexto de tarifa de aplicativo é relevante e atual, mas a estrutura (bandeirada + valor por km, dois pontos dados) é um clichê recorrente em livros didáticos de função afim, sem elementos que rompam o padrão tradicional do problema.
