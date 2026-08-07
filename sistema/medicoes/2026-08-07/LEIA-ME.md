# Medição com provedor real — 7 de agosto de 2026

Primeira execução do sistema contra a API da Anthropic (`claude-sonnet-5`),
para medir o que a suíte de testes não alcança: se o **Gerador** consegue
preencher as formalizações dos tipos acrescentados nas Fases 1 e 2a/2b.

## Como foi feita

Duas questões para cada uma das 9 habilidades que exercitam o que é novo —
`EM13MAT305`, `306`, `403`, `404`, `405` (consultas `dominio`, `imagem`,
`periodo`, `crescimento`, `Piecewise`) e `501`, `502`, `507`, `508` (tipo
`propriedade`). Nível cognitivo igual ao primeiro `bloom_sugerido` da
habilidade, dificuldade média, alternando natureza e formato.

## Custo medido

18 ciclos pedidos, **17 concluídos**, 50 chamadas ao LLM, 76 minutos.
Média de 4,5 minutos e 2,9 chamadas por ciclo.

## Resultado

**17 de 17 aprovadas.** Nenhuma descartada por esgotar as três iterações.

Taxa de não-verificável por tipo em `taxa_por_tipo.txt`; o índice por questão,
com a coluna `sem_conferencia`, em `questoes/_indice.csv`.

## Os três defeitos que a medição expôs

Nenhum deles seria encontrado pela suíte, que usa `LLMFake`: todos dependem de
escolhas que o Gerador faz e que não dá para antecipar sentado.

1. **Colisão de nomes de incógnita** (corrigido em `_parse.py`). O Gerador usou
   `I` para a intensidade de um abalo sísmico e `N` para uma população — nomes
   que o SymPy reserva para a unidade imaginária e para uma função. O caso
   perigoso é o `E`: como é o número de Euler, `Eq(E**2, 4)` simplifica para
   `False` e o gabarito correto `[-2, 2]` seria **reprovado**.

2. **Domínio restringido pelo contexto** (corrigido em `funcoes.py`). A consulta
   `dominio` exigia igualdade com o domínio máximo e reprovou quatro gabaritos
   corretos: `t` é tempo e não pode ser negativo, `n` conta termos e é natural.
   Nas `EM13MAT507` e `508` isso era sistemático — elas tratam de funções de
   domínios discretos, então declarar o domínio como os naturais é exatamente o
   que a habilidade pede. Agora o declarado precisa **caber** no máximo.

3. **Formalização malformada derrubava o ciclo** (corrigido em `gerador.py`). O
   LLM devolveu `{"ponto": {"d": 2}}` onde o contrato pede texto; a validação
   estourou e a questão inteira se perdeu, com enunciado e resolução bons. Agora
   a formalização inválida é descartada e as demais seguem.

## O que a medição confirmou que funciona

- O tipo `propriedade`, o mais novo, teve **0% de não-verificável** em 15 usos.
  O Gerador entendeu o contrato de predicados.
- A degradação segura da imagem exponencial: `2**x` caiu em não-verificável em
  vez de reprovar `(0, +oo)`, que estava certo.
- A `EM13MAT403` produziu seis formalizações — domínio, imagem e crescimento
  para a exponencial e para a logarítmica —, que é o que a habilidade pede.

## Ressalva

Os números aqui são **anteriores** às três correções: descrevem o sistema que
foi medido, não o atual. Uma nova medição, para comparar, é trabalho aberto —
e é o que diria se as taxas de `funcao/imagem` (35,7%) e `funcao/dominio`
(12,5%) caem, e quanto.
