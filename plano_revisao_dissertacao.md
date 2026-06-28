# Plano de revisão da dissertação — diagnóstico de repetições e adequação acadêmica

**Documento:** análise crítica da versão `DOC-20260609-WA0019` (Capítulos 1, 2 e 3) à luz de
`projeto_dissertacao_isabella.pdf` e `estrutura_dissertacao_isabella.pdf`.
**Status:** documento de trabalho orientador-aluna.

---

## 1. Diagnóstico geral

A versão atual cobre os três capítulos de fundamentação (1 — contexto; 2 — técnico; 3 — didático)
e segue, em linhas gerais, a estrutura prevista. O texto tem boa qualidade de prosa em nível de
parágrafo: as frases são claras e os conceitos estão corretos. **O problema não é a escrita local,
é a arquitetura do texto.** Três patologias se sobrepõem:

1. **Repetição conceitual entre capítulos (o problema central).** Vários conceitos são
   *introduzidos* no Capítulo 1, *re-explicados por extenso* no Capítulo 2 e *retomados de novo* na
   síntese (2.5) e no início do Capítulo 3. O leitor lê a mesma ideia três ou quatro vezes, com
   redação diferente, o que dá a impressão de que o autor perdeu o controle do que já foi dito.
2. **Defeitos técnicos de compilação** que fazem o texto parecer um rascunho não revisado:
   citações quebradas (`[?]`, `russell2021`, `wei2022chain`), referências cruzadas vazias
   (`Seção ??`, `Capítulo ??`) e numeração de seções fora de ordem.
3. **Resíduos de andaime** (texto de planejamento copiado da estrutura para dentro do corpo) e
   **inconsistências de formatação** (títulos de subseção ora numerados, ora soltos como parágrafo).

As três precisam ser atacadas, mas em ordem: primeiro a repetição (reescrita), depois os defeitos
técnicos (mecânicos), por último a padronização fina.

---

## 2. Repetições de conteúdo — mapa do problema

Cada linha abaixo é um conceito que aparece em **mais de um lugar**. A coluna "Casa canônica"
indica onde ele *deve* ser desenvolvido por extenso; nos demais lugares deve ser apenas
**mencionado em uma frase com remissão** (`conforme Seção X`).

| Conceito | Onde aparece hoje | Casa canônica | O que fazer nos outros lugares |
|---|---|---|---|
| Natureza probabilística do LLM / "o modelo não computa, prevê" | §1.2 (p. 3-4), §2.1.2 (p. 10-11) | **§2.1.2** | Em §1.2, reduzir a uma frase ("geração probabilística, detalhada no Cap. 2") |
| Arquitetura transformer / atenção | §1.2 (p. 3), §2.1.1 (p. 9-10) | **§2.1.1** | Em §1.2, citar só como marco histórico (2017, Vaswani), sem explicar atenção |
| Limitações dos LLMs em Matemática | §1.4 "Fragilidades" (4 categorias, p. 7), §2.1.3 (3 categorias, p. 11-12) | **§2.1.3** (técnico) | §1.4 deve ficar no plano *pedagógico* (impacto para o professor), não repetir a taxonomia de erros |
| Erro silencioso / alucinação | §1.4 (p. 7-8), §2.1.2, §2.5 (p. 23) | **§1.4** (é o conceito que motiva o trabalho) | Em §2.5, citar em meia frase; não reabrir a explicação |
| *Cascading error* | §1.4 e §2.1.3 | **§2.1.3** | §1.4 menciona o fenômeno; a mecânica fica em 2.1.3 |
| Chain-of-thought | §1.4 (p. 6), §2.2.1 (p. 12) | **§2.2.1** | §1.4 não deve introduzir CoT — antecipa conteúdo técnico do Cap. 2 |
| Hipótese arquitetural (LLM + verificador + crítico + orquestrador) | §1.4 impl., §2.1.3 fim, §2.2 intro, **§2.5 inteira**, §3 intro | **§2.5** | Nos demais, uma frase de gancho, nunca o argumento completo |
| PAL → princípio do Verificador | §2.2.2 (p. 13) e §2.5 (p. 23) | **§2.2.2** | §2.5 só referencia |
| Self-consistency: custo incompatível | §2.2.4 (p. 14-15) e §2.5 (p. 23) | **§2.2.4** | §2.5 só referencia |
| Justificativa de adoção do SymPy (aberto, BSD, custo zero) | §2.4.1 (p. 20) e §2.4.2 | **§2.4.1** | Dizer uma vez |
| "Três exigências de Polya → 3 critérios da rubrica" | §3.1.1 (p. 27) e §3.4 (p. 38) | **§3.4** (consolidação) | §3.1.1 conclui apontando para 3.4, sem listar os critérios já formatados |
| "TBR na entrada, SOLO na avaliação" | §3.2.1, §3.2.2, §3.2.3, §3.3.3 | **§3.2.3** (síntese operacional) | É dito 4 vezes quase igual; manter só na síntese |
| Critérios de qualidade (clareza, nível, BNCC, etc.) | espalhados em §3.1, §3.2, §3.3 e consolidados em §3.4 | **§3.4** | Nas seções teóricas, derivar o critério uma vez e dizer "consolidado em 3.4"; não re-enunciar |
| Limites da verificação simbólica (geometria/construção) | §2.4.3 e §3.3.2 | **§2.4.3** | §3.3.2 só remete |
| Khan Academy / plataformas comerciais | §1.3 e §1.4 | §1.3 | Escolher um lugar |

**Padrão dominante:** o Capítulo 1 está funcionando como um "Capítulo 2 em miniatura" — ele
antecipa transformer, CoT, taxonomia de erros e a hipótese arquitetural, que são propriamente do
Capítulo 2. Esse é o foco número um da revisão.

---

## 3. Princípio de correção: fonte única + papel de cada capítulo

A regra que resolve a maior parte das repetições é **"cada conceito tem um dono"**: é desenvolvido
por extenso uma única vez, no capítulo cuja função ele serve, e em todo outro lugar aparece só como
remissão. Para aplicar isso, é preciso fixar a função de cada capítulo:

- **Capítulo 1 — contexto e desafios (registro pedagógico/educacional).** Responde "por que isso
  importa para o professor". Apresenta IA na educação, o uso real de LLMs em sala, e — como gancho
  motivador — o fenômeno do *erro silencioso* do ponto de vista de quem ensina. **Não** explica
  arquitetura, **não** lista estratégias de mitigação, **não** enuncia a hipótese arquitetural em
  detalhe. É curto e instigante.
- **Capítulo 2 — fundamentação técnica.** Responde "como isso funciona e por que a combinação é
  necessária". É aqui que moram transformer, inferência probabilística, taxonomia técnica de erros,
  CoT/PAL/tool-use/self-consistency, agentes, SMA e CAS/SymPy. Fecha em 2.5 com a hipótese
  arquitetural — **este é o único lugar onde a hipótese é argumentada por inteiro.**
- **Capítulo 3 — fundamentação didática.** Responde "o que é uma questão boa e como sei disso".
  Polya, TSD, Bloom/SOLO, BNCC, terminando na consolidação dos seis critérios (3.4). Cada
  referencial **deriva** um critério; a lista formatada de critérios existe **só em 3.4**.

Com esses papéis fixados, toda vez que um conceito "técnico" aparecer no Cap. 1, ou um critério
formatado aparecer fora do 3.4, é repetição a cortar.

---

## 4. Defeitos técnicos a corrigir (mecânicos, mas urgentes)

Estes não são de conteúdo, mas hoje são o que mais faz o texto "não parecer acadêmico":

1. **Citações quebradas.** Praticamente todas saem como `[?]`, e várias chaves aparecem cruas no
   texto (`russell2021`, `weizenbaum1966`, `bengio2003`, `vaswani2017`, `wei2022chain`,
   `frieder2023mathematical`, `gao2023pal`, `schick2023toolformer`, `wang2023selfconsistency`,
   `kojima2022zero`, `holtzman2020curious`, `meurer2017sympy`, `miranda2015taxonomia`,
   `dante2003didatica`, `wu2023autogen`). Causa: faltam os `\cite{}` (as chaves foram digitadas como
   texto) e/ou o `.bib` não está sendo compilado. **Ação:** montar o arquivo `.bib`, trocar todas as
   chaves cruas por `\cite{chave}` e garantir o passo `bibtex/biber`. Há ainda `[1]`, `[2]`, `[3]`
   soltos (p. 4-5) que precisam virar citações nomeadas no mesmo padrão.
2. **Referências cruzadas vazias.** `Seção ??` e `Capítulo ??` em dezenas de pontos. **Ação:**
   colocar `\label{}` em cada capítulo/seção e usar `\ref{}`/`\autoref{}`. Vários `??` apontam para
   capítulos ainda não escritos (4, 5, 6) — usar rótulos provisórios já nomeados para não esquecer.
3. **Numeração de seções fora de ordem no Cap. 2.** Hoje: 2.2.4 → **2.2.5 "Agentes e sistemas
   multiagentes"** → **2.2.6 "Definição de agente"** → 2.3. Pela estrutura, "Agentes e sistemas
   multiagentes" é a **Seção 2.3**, não subseção de 2.2 (que é "Estratégias de mitigação"). **Ação:**
   promover 2.2.5/2.2.6 para 2.3 e renumerar o que era 2.3 em diante (vira 2.4, etc.). Conferir
   contra a estrutura: 2.1 LLMs, 2.2 Mitigação, 2.3 Agentes/SMA, 2.4 CAS, 2.5 Síntese.
4. **Resíduo de andaime.** O Capítulo 2 começa com o parágrafo *"Descrição: capítulo
   técnico-central da fundamentação..."* — isso é texto de planejamento copiado da estrutura.
   **Ação:** apagar; substituir por um parágrafo de abertura real do capítulo.
5. **Títulos inconsistentes.** Em §1.4 os blocos "Potencialidades reconhecidas", "Fragilidades
   documentadas", "O fenômeno do erro silencioso", "Implicações para esta dissertação" e em §3.1.1
   "Implicações para a elaboração de questões" estão como parágrafos em negrito/itálico soltos, não
   como subseções. **Ação:** decidir um padrão (subseções `\subsection*{}` ou parágrafos com
   `\paragraph{}`) e aplicar em todo o documento.

---

## 5. Erros pontuais de revisão de texto

- p. 12: "reduz a probabilidade de **saltos inferências** incorretos" → "saltos **inferenciais**".
- p. 33: "respostas **multiEstruturais**" → "multiestruturais" (capitalização).
- p. 35: a estrutura cita **quatro** unidades temáticas mas lista três ("Números e Álgebra,
  Geometria e Medidas, e Probabilidade e Estatística") — falta "Funções" ou a redação está
  incorreta; conferir a BNCC e corrigir (são quatro: Números, Álgebra, Geometria e Medidas,
  Probabilidade e Estatística — o texto fundiu/omitiu).
- Tabelas com "Elaborado pela autora (2024)" — conferir o ano de defesa/edição e padronizar.
- Padronizar grafia: "Pólya" vs "Polya" (o texto usa as duas); "transformer" sempre em itálico.

---

## 6. Plano de ação por capítulo

**Capítulo 1 (encolher e despoluir tecnicamente).**
- Cortar de §1.4 a lista técnica das 4 categorias de erro (vai para 2.1.3) e a introdução de CoT.
  Manter o *erro silencioso* (é o gancho do trabalho) e as implicações **pedagógicas**.
- Em §1.2, reduzir transformer/atenção a marco histórico; remover a explicação probabilística
  detalhada (fica em 2.1.2).
- Resultado esperado: o capítulo fica claramente "de contexto", coerente com as 8-10 páginas
  previstas, e para de competir com o Cap. 2.

**Capítulo 2 (corrigir numeração e desduplicar a síntese).**
- Apagar o resíduo "Descrição:..." e abrir o capítulo de verdade.
- Renumerar 2.2.5/2.2.6 → 2.3 e cascata.
- §2.5 deve ser o **único** lugar que argumenta a hipótese por inteiro; remover as antecipações
  dela que hoje fecham §1.4, §2.1.3 e abrem §2.2. PAL (2.2.2) e self-consistency (2.2.4) já
  contêm o argumento — em 2.5 apenas referenciá-los, não repeti-los.

**Capítulo 3 (concentrar os critérios em 3.4).**
- Nas seções 3.1–3.3, cada referencial **deriva** suas implicações e encerra com "→ consolidado em
  3.4", sem listar critérios já formatados nem repetir "TBR na entrada / SOLO na avaliação"
  (mantê-lo só em 3.2.3).
- A enunciação formatada dos seis critérios vive **só em 3.4** + Tabela 3.1.
- Corrigir a lista das unidades temáticas da BNCC (§3.3.2).

---

## 7. Ordem de execução sugerida

1. **Mecânica primeiro (1 sessão):** montar o `.bib`, trocar chaves cruas por `\cite`, pôr
   `\label`/`\ref`, apagar o resíduo de andaime e corrigir a numeração do Cap. 2. Isso já faz o PDF
   "parecer" uma dissertação e facilita revisar o resto.
2. **Desduplicação do Cap. 1 ↔ Cap. 2 (foco principal):** aplicar o mapa da Seção 2 deste plano,
   movendo o conteúdo técnico para suas casas canônicas e deixando ganchos no Cap. 1.
3. **Desduplicação interna do Cap. 3:** concentrar critérios em 3.4.
4. **Padronização fina:** títulos, itálicos, "Pólya", anos das tabelas, erros pontuais da Seção 5.
5. **Leitura corrida final** capítulo a capítulo, verificando que cada conceito é explicado uma única
   vez e que toda remissão `\ref` resolve.

---

## 8. Critério de "pronto"

A revisão está concluída quando: (i) nenhum conceito técnico é explicado em mais de um lugar — os
demais são remissões; (ii) não há `[?]` nem `??` no PDF compilado; (iii) a numeração de seções bate
com a estrutura; (iv) o Capítulo 1 não contém arquitetura, mitigação nem a hipótese detalhada; e
(v) os seis critérios de qualidade aparecem formatados só em 3.4.
