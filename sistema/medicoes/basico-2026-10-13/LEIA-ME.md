# Nível "básico" contra "fácil" — 15 pares, provedor real

Gerado com `claude-sonnet-5` no commit `88b549f` (`execucao.json`), por `medir_basico.py` em três
processos; números de `analisar_basico.py` (saída em `analise.txt`).

**Pergunta:** o nível *básico*, criado depois da primeira rodada do painel (Seção 6.1 da
dissertação), sai de fato mais simples que o *fácil*? E as alternativas saem sorteadas, com as
letras coerentes?

**Desenho pareado.** Para cada uma das 15 habilidades, a especificação *fácil* do plano do acervo
foi gerada duas vezes na mesma execução, como fácil e como básico, com tudo o mais igual
(habilidade, temas, Bloom, natureza, formato, contexto). O formato alterna: 8 pares de múltipla
escolha, 7 discursivos.

## Resultado

| | fácil | básico |
|---|---|---|
| aprovadas | 15/15 | 14/15 |
| palavras no enunciado (mediana, 14 pares) | 134,5 | 75,5 |
| alinhamento BNCC ≤ 3 no Crítico | 3/14 | 3/14 |

- O básico é **mais curto em 13 dos 14 pares** e nunca mais longo.
- **Itens encadeados:** nas 7 discursivas, o básico os eliminou em 5 (ex.: EM13MAT405, 5 → 0) e
  nunca os acrescentou.
- Menos números no enunciado em 9 de 14; resolução mais curta em 11 de 14.
- **Não custou qualidade** pelo Crítico: alinhamento, clareza e garantia obtida praticamente iguais
  (originalidade caiu de 3,73 para 3,36).

**O limite está no Bloom alto.** Das três especificações com `criar`, só a EM13MAT502 simplificou:
a EM13MAT304 foi **descartada** (o Crítico deu 2 em `adequacao_nivel` nas três tentativas — pedir
criação num item de um passo é contraditório) e a EM13MAT303 saiu básica só no nome (3 itens,
razão 6/5, resposta 214,99). Nos níveis `entender`, `aplicar` e `analisar`, 12 de 12 aprovadas.

**Alternativas.** Nas 15 de múltipla escolha aprovadas, a correta caiu em a: 5, b: 5, c: 3, d: 2
(antes do sorteio, 38 de 43 na *a*). Nenhum gabarito ou resolução citou a alternativa pela letra
— a regra nova do prompt foi seguida —, e nenhuma letra ficou inconsistente.

## O que isto não mede

Os indicadores são de **texto**, não de dificuldade: dizem que o básico é mais curto, menos
encadeado e com menos números, não que a turma o ache fácil. Quem diz isso é o professor; a
pergunta fica para o painel.
