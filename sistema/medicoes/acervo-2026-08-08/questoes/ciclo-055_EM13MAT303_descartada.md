# Ciclo 055 — EM13MAT303

- **Situação:** DESCARTADA após 3 iterações
- **Temas:** funcao_exponencial
- **Nível cognitivo:** aplicar
- **Dificuldade:** dificil | **Natureza:** aplicada | **Formato:** multipla_escolha
- **Garantia obtida:** conferido
- **Iterações:** 3

## Enunciado

Marina recebeu R$ 8.000,00 de bônus e decidiu aplicá-los por 3 anos em um CDB do Banco Alfa. O banco anuncia esse produto com taxa nominal de 20% ao ano, com capitalização semestral, e garante que não haverá retiradas nem aportes durante o período. Considerando que os juros são capitalizados a cada semestre, o montante $M$ resgatado por Marina, em função do número $t$ de semestres decorridos, pode ser escrito como $M(t) = 8000\cdot(1{,}1)^t$. Qual será o valor total resgatado por Marina ao final dos 3 anos de aplicação?

## Alternativas

- (a) R$ 12.800,00
  - *erro representado:* Tratou os juros como simples, aplicando 20% ao ano de forma linear sobre o capital inicial durante 3 anos (M = 8000·(1+0,20·3)), ignorando a capitalização composta.
- (b) R$ 13.824,00
  - *erro representado:* Usou corretamente juros compostos, mas aplicou a taxa nominal de 20% diretamente ao ano (sem dividir pelos 2 semestres), calculando M = 8000·(1,20)^3.
- (c) R$ 10.648,00
  - *erro representado:* Encontrou corretamente a taxa efetiva semestral de 10%, mas confundiu o número de períodos, usando n = 3 (anos) em vez de n = 6 (semestres): M = 8000·(1,10)^3.
- (d) R$ 14.172,49  ← correta

## Gabarito

R$ 14.172,49

## Resolução

**Passo 1 — Identificar a taxa efetiva do período de capitalização.**

A taxa é *nominal anual* de 20%, mas a capitalização é *semestral*. Isso significa que a taxa realmente aplicada a cada semestre é a taxa nominal dividida pelo número de capitalizações no ano:
$$i_{sem} = \frac{20\%}{2} = 10\% = 0{,}10 \text{ ao semestre}.$$

**Passo 2 — Determinar o número de períodos de capitalização.**

Como a aplicação dura 3 anos e a capitalização ocorre a cada semestre, o número de períodos é:
$$n = 3 \text{ anos} \times 2 \text{ semestres/ano} = 6 \text{ semestres}.$$

**Passo 3 — Escrever a lei de formação exponencial.**

Em juros compostos, o montante cresce exponencialmente a cada período segundo:
$$M(t) = M_0\cdot(1+i_{sem})^{t} = 8000\cdot(1{,}1)^{t},$$
onde $t$ é contado em semestres. Note que essa é uma função exponencial de base $1{,}1 > 1$, logo o crescimento é evidentemente exponencial (não linear) — cada semestre multiplica o saldo anterior pelo mesmo fator.

**Passo 4 — Calcular o montante para $t = 6$.**
$$M(6) = 8000\cdot(1{,}1)^6 = 8000\times 1{,}771561 = 14172{,}488.$$

Arredondando para centavos: $M(6) \approx R\$\,14.172{,}49$.

**Conclusão:** o valor resgatado por Marina ao final dos 3 anos é aproximadamente R$ 14.172,49.

## Formalização verificável

- `funcao` — expressão `8000*(Rational(11,10))**t`, esperado `1771561/125`, parâmetros `{'consulta': 'valor', 'ponto': '6'}`
- `funcao` — expressão `8000*(Rational(11,10))**t`, esperado `crescente`, parâmetros `{'consulta': 'crescimento'}`

## Trilha do ciclo

### Iteração 1

- **Verificador:** rejeitado — 1 de 2 afirmações reprovadas. (1) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-1 - 5**(5/6)*sqrt(-1 - sqrt(3)*I)/5, -1 + 5**(5/6)*sqrt(-1 - sqrt(3)*I)/5, -1 - 5**(5/6)*sqrt(-1 + sqrt(3)*I)/5, -1 + 5**(5/6)*sqrt(-1 + sqrt(3)*I)/5, -sqrt(2)*5**(5/6)/5 - 1]. | (2) aprovado: Gabarito confirmado (f(10) = -100 + 128*5**(1/3)).
  - equacao=rejeitado
  - funcao/valor=aprovado
- **Crítico:** não chegou a avaliar
- **Devolvido ao Gerador:** O verificador simbólico REPROVOU o gabarito. Motivo: 1 de 2 afirmações reprovadas. (1) rejeitado: Divergência no conjunto-solução — soluções calculadas ausentes do gabarito: [-1 - 5**(5/6)*sqrt(-1 - sqrt(3)*I)/5, -1 + 5**(5/6)*sqrt(-1 - sqrt(3)*I)/5, -1 - 5**(5/6)*sqrt(-1 + sqrt(3)*I)/5, -1 + 5**(5/6)*sqrt(-1 + sqrt(3)*I)/5, -sqrt(2)*5**(5/6)/5 - 1]. | (2) aprovado: Gabarito confirmado (f(10) = -100 + 128*5**(1/3)). Resultado calculado independentemente: [-1 + sqrt(2)*5**(5/6)/5, -1 - 5**(5/6)*sqrt(-1 - sqrt(3)*I)/5, -1 + 5**(5/6)*sqrt(-1 - sqrt(3)*I)/5, -1 - 5**(5/6)*sqrt(-1 + sqrt(3)*I)/5, -1 + 5**(5/6)*sqrt(-1 + sqrt(3)*I)/5, -sqrt(2)*5**(5/6)/5 - 1] | f(10) = -100 + 128*5**(1/3). Corrija o gabarito e a resolução (ou o enunciado, se os dados estiverem inconsistentes).

### Iteração 2

- **Verificador:** aprovado — Todas as 4 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(3) = 17280). | (2) aprovado: Gabarito confirmado (f(6) = 1771561/100). | (3) aprovado: Gabarito confirmado (crescente em Reals). | (4) aprovado: Conjunto-solução do gabarito coincide exatamente com o calculado.
  - funcao/valor=aprovado
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
  - equacao=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — O enunciado define claramente o capital inicial, o prazo, as duas taxas e a pergunta (qual plano rende mais e qual a diferença). Não há ambiguidade lexical ou estrutural, e todos os dados necessários (10.000, 3 anos, 20% a.a. nas duas modalidades) estão presentes.
  - adequacao_nivel: 4/5 — A tarefa exige aplicar a fórmula de juros compostos duas vezes com unidades de tempo diferentes e depois comparar os resultados — compatível com o nível 'aplicar' de Bloom, com estrutura relacional na SOLO (o aluno relaciona dois modelos exponenciais). Não chega a exigir 'analisar' propriamente, mas está coerente com o nível declarado e com dificuldade 'difícil' pela armadilha da conversão de taxa/período.
  - alinhamento_bncc: 5/5 — Cumpre plenamente a EM13MAT303: envolve juros compostos e evidencia o crescimento exponencial ao contrastar explicitamente como a frequência de capitalização (mesma taxa nominal) altera o montante final — não é uma conta isolada de porcentagem.
  - distratores: 5/5 — Os três distratores mapeiam erros sistemáticos plausíveis e distintos: confundir taxa nominal com montante igual, usar o número de anos em vez de semestres como expoente, e usar 20% em vez de 10% como taxa semestral. Nenhum é absurdo ou trivialmente eliminável por inspeção.
  - originalidade: 2/5 — O contexto (comparar capitalização anual vs. semestral com a mesma taxa nominal) é um problema muito clássico de livros didáticos sobre juros compostos, sem elemento de contextualização significativa além do nome 'Marina'. Além disso, o próprio enunciado já explica entre parênteses que 'o rendimento de 10% é aplicado a cada semestre sobre o saldo atualizado', entregando ao aluno exatamente a conversão de taxa nominal para taxa efetiva por período — o principal obstáculo cognitivo da questão —, configurando efeito Topaze e enfraquecendo o propósito do distrator que testa esse erro.
  - *sugestões:* Para elevar a originalidade sem perder o rigor: (1) insira um contexto mais significativo e específico (ex.: comparação real entre dois produtos financeiros, com nomes de instituições ou situação de decisão financeira concreta) em vez do esquema genérico 'Plano A vs Plano B'; (2) remova a explicação entre parênteses '(ou seja, o rendimento de 10% é aplicado a cada semestre sobre o saldo atualizado)', deixando apenas 'taxa nominal de 20% ao ano, com capitalização semestral' — assim o aluno precisa deduzir por si mesmo a taxa efetiva de 10% ao semestre e o número de períodos (6), preservando o desafio que o terceiro distrator pretende medir; (3) opcionalmente, peça também que o aluno expresse M(t) como função exponencial explícita para reforçar a conexão com função exponencial declarada no tema.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Para elevar a originalidade sem perder o rigor: (1) insira um contexto mais significativo e específico (ex.: comparação real entre dois produtos financeiros, com nomes de instituições ou situação de decisão financeira concreta) em vez do esquema genérico 'Plano A vs Plano B'; (2) remova a explicação entre parênteses '(ou seja, o rendimento de 10% é aplicado a cada semestre sobre o saldo atualizado)', deixando apenas 'taxa nominal de 20% ao ano, com capitalização semestral' — assim o aluno precisa deduzir por si mesmo a taxa efetiva de 10% ao semestre e o número de períodos (6), preservando o desafio que o terceiro distrator pretende medir; (3) opcionalmente, peça também que o aluno expresse M(t) como função exponencial explícita para reforçar a conexão com função exponencial declarada no tema.

### Iteração 3

- **Verificador:** aprovado — Todas as 2 afirmações conferidas. (1) aprovado: Gabarito confirmado (f(6) = 1771561/125). | (2) aprovado: Gabarito confirmado (crescente em Interval(-oo, oo)).
  - funcao/valor=aprovado
  - funcao/crescimento=aprovado
- **Crítico:** reprovou
  - clareza: 5/5 — Enunciado sem ambiguidade: capital, taxa nominal, periodicidade de capitalização e prazo estão explícitos, e a pergunta final é única e objetiva.
  - adequacao_nivel: 2/5 — Ao fornecer M(t)=8000·(1,1)^t já pronta no enunciado (com t em semestres já definido), a tarefa do aluno se reduz a substituir t=6 e calcular uma potência — processo de 'lembrar/executar', não de 'aplicar' um modelo a uma situação nova. A resolução, no entanto, apresenta passos (obter taxa efetiva, converter anos em semestres) que o enunciado já resolveu, criando incoerência entre o que se pede e o que se avalia. A dificuldade declarada 'difícil' não se sustenta, pois o raciocínio-chave (conversão de taxa nominal e contagem de períodos) foi entregue ao aluno.
  - alinhamento_bncc: 3/5 — O tema (juros compostos, crescimento exponencial) está presente e os distratores até exploram erros de conversão de taxa/período — mas essa exploração só aparece nas alternativas, não no processo que o aluno de fato precisa executar, já que a fórmula com a taxa efetiva e o expoente correto vem pronta no enunciado. Assim, a habilidade de 'resolver problemas envolvendo... juros compostos, destacando o crescimento exponencial' é apenas parcialmente exercida: o crescimento exponencial é apresentado, não descoberto ou justificado pelo estudante.
  - distratores: 5/5 — Os quatro distratores mapeiam erros sistemáticos plausíveis e distintos: juros simples, uso da taxa nominal sem dividir pelos semestres, e confusão entre número de anos e número de semestres. Nenhum é absurdo ou trivialmente descartável, e todos exigem cálculo genuíno para serem descartados.
  - originalidade: 2/5 — O contexto (CDB, bônus) é razoável e não é o clichê mais batido, mas o enunciado comete um efeito Topaze evidente: ao entregar a lei de formação M(t)=8000·(1,1)^t com t já definido em semestres, elimina exatamente o passo mais importante e mais difícil do problema (conversão de taxa nominal em efetiva e de anos em semestres), que é justamente o que os distratores tentam testar. Isso cria contradição entre o enunciado (que resolve o problema) e as alternativas (que pressupõem que o aluno ainda precise resolver esse mesmo problema).
  - *sugestões:* Remova a fórmula M(t)=8000·(1,1)^t do enunciado. Apresente apenas os dados brutos (capital R$ 8.000,00, taxa nominal 20% ao ano, capitalização semestral, prazo de 3 anos, sem aportes/retiradas) e peça o montante final. Assim o aluno precisará, ele mesmo: (1) converter a taxa nominal anual em taxa efetiva semestral (10% ao semestre), (2) converter o prazo de anos para semestres (6 períodos), e (3) montar e aplicar a lei exponencial M = M0(1+i)^n — processo que efetivamente corresponde ao nível 'aplicar' e evidencia o crescimento exponencial pelo próprio raciocínio do estudante, não por informação entregue. Mantenha os mesmos quatro distratores, pois já representam bem os erros típicos de conversão de taxa/período e de confusão com juros simples.
- **Devolvido ao Gerador:** O avaliador didático REPROVOU a questão. Sugestões de revisão: Remova a fórmula M(t)=8000·(1,1)^t do enunciado. Apresente apenas os dados brutos (capital R$ 8.000,00, taxa nominal 20% ao ano, capitalização semestral, prazo de 3 anos, sem aportes/retiradas) e peça o montante final. Assim o aluno precisará, ele mesmo: (1) converter a taxa nominal anual em taxa efetiva semestral (10% ao semestre), (2) converter o prazo de anos para semestres (6 períodos), e (3) montar e aplicar a lei exponencial M = M0(1+i)^n — processo que efetivamente corresponde ao nível 'aplicar' e evidencia o crescimento exponencial pelo próprio raciocínio do estudante, não por informação entregue. Mantenha os mesmos quatro distratores, pois já representam bem os erros típicos de conversão de taxa/período e de confusão com juros simples.
