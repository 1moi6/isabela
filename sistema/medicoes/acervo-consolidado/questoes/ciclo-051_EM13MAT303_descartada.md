# Ciclo 051 — EM13MAT303

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** criar
- **Dificuldade:** facil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** sem_conferencia
- **Iterações:** 3

## Enunciado

Um investidor aplica R$ 800,00 em um fundo que paga juros compostos de 8% ao mês. Chamando de $M(t)$ o montante, em reais, após $t$ meses de aplicação, tem-se $M(t) = 800 \cdot (1{,}08)^t$. Usando $\log 2 \approx 0{,}301$ e $\log 1{,}08 \approx 0{,}0334$, determine, aproximadamente, quantos meses são necessários para que o valor investido dobre.

## Alternativas

- (a) 9 meses  ← correta
- (b) 13 meses
  - *erro representado:* Tratou o crescimento como juros simples (linear): calculou $t = 1/0{,}08 = 12{,}5$ e arredondou para 13, ignorando que o crescimento é exponencial (juros compostos).
- (c) 2 meses
  - *erro representado:* Resolveu $1{,}08\,t = 2$ como se a incógnita estivesse multiplicando (equação linear), obtendo $t = 2/1{,}08 \approx 1{,}85$ e arredondando para 2, sem perceber que $t$ é expoente.
- (d) 25 meses
  - *erro representado:* Dividiu diretamente o total necessário (200%) pela taxa mensal em porcentagem: $200/8 = 25$, aplicando raciocínio de porcentagem simples em vez de juros compostos.

## Gabarito

A) 9 meses

## Resolução

**Passo 1 — Montar a equação.** O montante dobra quando $M(t) = 1600$, ou seja:
$$800 \cdot (1{,}08)^t = 1600$$

**Passo 2 — Isolar a potência.** Dividindo ambos os lados por 800:
$$(1{,}08)^t = 2$$

**Passo 3 — Aplicar logaritmo.** Como a incógnita está no expoente, aplica-se logaritmo aos dois lados (evidenciando o caráter exponencial do crescimento — não é possível resolver isso com uma regra de três simples):
$$\log\big((1{,}08)^t\big) = \log 2 \;\Rightarrow\; t \cdot \log(1{,}08) = \log 2$$

**Passo 4 — Resolver para $t$.**
$$t = \dfrac{\log 2}{\log 1{,}08} \approx \dfrac{0{,}301}{0{,}0334} \approx 9{,}01$$

**Conclusão.** São necessários aproximadamente **9 meses** para que o investimento dobre de valor. Note que, se o crescimento fosse linear (juros simples), o tempo seria bem diferente — é justamente o crescimento exponencial de $(1{,}08)^t$ que faz o valor dobrar tão rapidamente.

## Formalização verificável

- `funcao` — expressão `800*1.08**t`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`
- `funcao` — expressão `800*1.08**t`, esperado `1727.13999781823`, parâmetros `{'consulta': 'valor', 'ponto': '10'}`
- `equacao` — expressão `Eq(800*1.08**t, 1600)`, esperado `[log(2)/log(1.08)]`

## Trilha do ciclo

### Iteração 1

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(3) = 2662). | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado é preciso: capital, taxa, período e o que se pede (M(3)) estão explícitos, sem ambiguidade lexical ou estrutural. Todos os dados necessários estão presentes.
  - adequacao_nivel: 2/5 — A especificação declara Bloom 'criar', mas a tarefa exigida é puramente 'aplicar': substituir valores na fórmula M(t)=2000(1,1)^t e calcular uma potência. Não há elaboração, formulação de problema, comparação ou justificativa pedida ao aluno — a estrutura de resposta é unistrutural (só o número final), incompatível com o nível cognitivo declarado.
  - alinhamento_bncc: 3/5 — A habilidade EM13MAT303 pede 'resolver E elaborar' problemas de juros compostos destacando o crescimento exponencial. A questão apenas resolve um cálculo isolado; não há elaboração de problema nem qualquer elemento no enunciado que force o aluno a evidenciar o caráter exponencial (isso só aparece na resolução do professor, não é testado pela pergunta em si, que poderia ser respondida com qualquer regra memorizada de juros compostos sem entender a natureza exponencial).
  - distratores: 4/5 — Os três distratores representam erros sistemáticos plausíveis e comuns (confundir com juros simples, multiplicar em vez de potenciar, erro de conversão percentual). Nenhum é absurdo. Poderia haver um distrator ligado à interpretação errada de t (ex.: usar t=4) para ampliar a cobertura de erros conceituais sobre a variável exponencial.
  - originalidade: 2/5 — É um exercício-modelo clássico de livro didático (aplicação financeira genérica, sem contexto significativo), sem nenhum elemento novo de contextualização ou desafio. O enunciado já entrega a estrutura da solução (fórmula implícita, valores prontos para substituição), configurando efeito Topaze.
  - *sugestões:* 1) Ajustar o nível cognitivo real da questão ao Bloom declarado ('criar'): peça, por exemplo, que o aluno elabore a expressão geral M(t) a partir da situação narrativa (sem fornecer a fórmula), ou que compare/justifique por que o crescimento é exponencial e não linear, exigindo argumentação e não apenas substituição numérica. Alternativamente, rebaixe o Bloom declarado para 'aplicar', que é o que a tarefa atual realmente demanda. 2) Para atender plenamente EM13MAT303, inclua no enunciado (não apenas na resolução) uma exigência que evidencie o crescimento exponencial, como perguntar em que mês o montante dobra, ou comparar com um cenário de juros simples dentro do próprio problema, forçando o aluno a perceber a diferença. 3) Aumente a originalidade contextualizando com uma situação menos genérica (ex.: financiamento, poupança escolar, crescimento populacional análogo) e evite fornecer estrutura pronta que leve diretamente à fórmula; force o aluno a montá-la. 4) Considere adicionar um distrator relacionado a erro na contagem do número de períodos (t).
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: 1) Ajustar o nível cognitivo real da questão ao Bloom declarado ('criar'): peça, por exemplo, que o aluno elabore a expressão geral M(t) a partir da situação narrativa (sem fornecer a fórmula), ou que compare/justifique por que o crescimento é exponencial e não linear, exigindo argumentação e não apenas substituição numérica. Alternativamente, rebaixe o Bloom declarado para 'aplicar', que é o que a tarefa atual realmente demanda. 2) Para atender plenamente EM13MAT303, inclua no enunciado (não apenas na resolução) uma exigência que evidencie o crescimento exponencial, como perguntar em que mês o montante dobra, ou comparar com um cenário de juros simples dentro do próprio problema, forçando o aluno a perceber a diferença. 3) Aumente a originalidade contextualizando com uma situação menos genérica (ex.: financiamento, poupança escolar, crescimento populacional análogo) e evite fornecer estrutura pronta que leve diretamente à fórmula; force o aluno a montá-la. 4) Considere adicionar um distrator relacionado a erro na contagem do número de períodos (t).

### Iteração 2

- **Verificador:** rejeitado — 2 de 4 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 800*1.08**t: coincide com a PG declarada. | (2) rejeitado: Divergência no conjunto-solução — soluções do gabarito não confirmadas: [12.9935872129277*log(2)]; soluções calculadas ausentes do gabarito: [9.00646834200059]. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) rejeitado: Divergência: f(10) = 1727.13999781823; gabarito 6588516227028768/3814697265625.
  - propriedade=aprovado
  - equacao=rejeitado
  - funcao/crescimento=aprovado
  - funcao/valor=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 2 de 4 afirmações reprovadas. (1) aprovado: Propriedades confirmadas para 800*1.08**t: coincide com a PG declarada. | (2) rejeitado: Divergência no conjunto-solução — soluções do gabarito não confirmadas: [12.9935872129277*log(2)]; soluções calculadas ausentes do gabarito: [9.00646834200059]. | (3) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (4) rejeitado: Divergência: f(10) = 1727.13999781823; gabarito 6588516227028768/3814697265625. Resultado calculado independentemente: 800*1.08**t | [9.00646834200059] | crescente em Interval(-oo, oo) | f(10) = 1727.13999781823. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 3

- **Verificador:** rejeitado — 2 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (2) rejeitado: Divergência: f(10) = 1727.13999781823; gabarito 1727.13999781823. | (3) rejeitado: Divergência no conjunto-solução — soluções do gabarito não confirmadas: [12.9935872129277*log(2)]; soluções calculadas ausentes do gabarito: [9.00646834200059].
  - funcao/crescimento=aprovado
  - funcao/valor=rejeitado
  - equacao=rejeitado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 2 de 3 afirmações reprovadas. (1) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)). | (2) rejeitado: Divergência: f(10) = 1727.13999781823; gabarito 1727.13999781823. | (3) rejeitado: Divergência no conjunto-solução — soluções do gabarito não confirmadas: [12.9935872129277*log(2)]; soluções calculadas ausentes do gabarito: [9.00646834200059]. Resultado calculado independentemente: crescente em Interval(-oo, oo) | f(10) = 1727.13999781823 | [9.00646834200059]. Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).
