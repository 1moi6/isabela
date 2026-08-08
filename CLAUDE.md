# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the **dissertação de mestrado (PROFMAT/UFMT)** de Isabella Dias Ribeiro dos Santos,
orientada pelo Prof. Dr. Moiseis dos Santos Cecconello, **e a implementação do sistema que ela
descreve**: um sistema multiagente para geração assistida de questões de Matemática do Ensino Médio
(LLM gerador + verificador simbólico via SymPy + crítico didático + orquestrador).

Dois artefatos:
- `dissertacao/` — o texto em LaTeX (Caps. 1–7 escritos; falta o material pré-textual).
- `sistema/` — o código Python do sistema (produto educacional; ver `sistema/README.md`).

## Trabalhar no código (`sistema/`)

```
cd sistema
pip install -e ".[dev]"     # sympy, pydantic, pytest, fastapi — suficiente para os testes
python -m pytest            # 157 testes; NÃO exigem chave de API (usam LLM fake)
python -m pytest tests/test_orquestrador.py -k descarte   # um teste específico
python executar.py          # sobe a interface (requer .[app] e um provedor configurado)
```

Pontos estruturais que não são óbvios pelos nomes de arquivo:
- **O Verificador não usa LLM.** `agentes/verificador.py` delega a `verificacao/` (SymPy puro).
  A ponte entre a prosa da questão e o SymPy é o campo `verificaveis` (`ExpressaoVerificavel` em
  `modelos.py`), que o Gerador preenche — o Verificador nunca interpreta enunciado. É uma
  **lista**: uma questão faz mais de uma afirmação verificável quando articula dois temas ou
  quando a habilidade cobra propriedade além do resultado. O Verificador agrega por conjunção
  (a mais fraca manda) e o Orquestrador continua vendo um veredicto só.
- **`tipo: "propriedade"`** (`verificacao/propriedades.py`) verifica predicados sobre a
  expressão que o estudante deve produzir — reproduz os pontos da tabela, tem o grau declarado,
  coincide com a progressão — em vez de comparar um gabarito. É o que torna 501, 502, 507 e 508
  conferíveis. Predicado ausente não é verificado; nenhum predicado devolve `nao_verificavel`.
- **A política de decisão vive só no Orquestrador** (`agentes/orquestrador.py`): rejeição do
  verificador volta ao Gerador sem passar pelo Crítico; `nao_verificavel` segue ao Crítico;
  3 iterações sem aprovação = descarte. Testes de política usam `LLMFake` (test_orquestrador.py).
- **Provedores de LLM são plugáveis** via `llm/criar_provedor` (`anthropic`/`openai`/`ollama`);
  dependências de provedor são opcionais no `pyproject.toml` — não as torne obrigatórias.
  Os modelos atuais da Anthropic **rejeitam `temperature`**: `anthropic_llm.py` só envia o
  parâmetro para as famílias legadas listadas ali (padrão = não enviar).
- **A interface é FastAPI + HTML/CSS/JS sem passo de build** (`api/main.py` + `docs/` na raiz do
  repositório, não dentro de `sistema/`: é a pasta que o GitHub Pages publica, então existe uma
  cópia só, servida pelo processo local e pelo Pages). Um `POST /api/gerar` produz **uma**
  questão; o lote é o cliente repetindo a chamada, para o professor ver cada questão chegar.
  Nada de Node: `instalar.bat` continua sendo só `pip install`. Ao mexer em `docs/app.css` ou
  `docs/app.js`, suba o `?v=` em `docs/index.html` — senão a correção não chega a quem já visitou.
- **Texto vindo do LLM entra na página por `textContent`, nunca por `innerHTML`** (`docs/app.js`).
- **Modo local vs. compartilhado** (`convites.py`): sem `convites.json` não há autenticação
  (uso individual); criar o primeiro convite liga a exigência. O modo depende da **existência**
  do arquivo, não do conteúdo — senão revogar o último convite reabriria o acesso a todos.
- **A chave de API viaja por requisição** (cabeçalho `X-Chave-API`, guardada no `localStorage`
  de quem usa) e nunca é gravada. Não volte a guardá-la em variável de módulo: com duas pessoas,
  a segunda sobrescrevia a primeira e o uso de uma era cobrado da outra, sem erro visível.
- **Em modo compartilhado, requisição sem chave é recusada (402)** — `_autorizar_chave` em
  `api/main.py`. Antes, `criar_provedor(api_key=None)` fazia o SDK cair na variável de ambiente
  e o dono pagava a geração do convidado, em silêncio e sem teto; a interface só avisava, sem
  travar o botão. Bancar virou decisão explícita (`chave_do_servidor`) com `cota_por_convite`,
  contada em `convites.json` e só para quem **não** traz a própria chave.
- **Todo acesso ao banco filtra por dono** (`_FILTRO_DONO` em `banco.py`). Método novo que
  consulte `questoes` sem esse filtro vaza o banco de uma pessoa para outra.
- A **pasta sincronizada** (`sincronizacao.py`) espelha as questões num diretório que o Google
  Drive replica — sem OAuth, sem chamada de rede. Falha ali vira aviso, nunca impede de salvar.
- **Prompts são artefatos da pesquisa** (`prompts/*.md`): serão citados no Apêndice A da
  dissertação. Mudanças neles afetam o texto acadêmico — trate como mudança de conteúdo.
- **A habilidade da BNCC é a origem da especificação, não um rótulo dela.** É o primeiro
  parâmetro; os temas são derivados dela (`especificacao.py`), e o campo `relacao_temas` do
  catálogo decide se dá para escolher entre eles: `conjuntiva` (a habilidade *é* a articulação —
  `EM13MAT507` associa PA a função afim; pedir só a PA é recusado), `enumerativa` (combinar é
  opção) ou `unica`. Não reintroduza a escolha do tema antes da habilidade: era o que permitia
  montar pedidos incoerentes.
- **O catálogo carrega `exigencias` por habilidade** — o que a questão precisa exibir para
  realizá-la. Vão ao Gerador como requisito e ao Crítico como âncora do critério
  `alinhamento_bncc`. Sem elas, uma questão correta, clara e sobre o conteúdo certo passa sem
  cumprir a habilidade (a `EM13MAT402` pede converter álgebra em gráfico; "ache as raízes"
  satisfaz o Verificador e não realiza a habilidade). Habilidade nova **precisa** de exigências.
- O catálogo BNCC (`dados/bncc_em_matematica.json`) tem **transcrições literais** da seção 5.2.1.1,
  conferidas contra `bncc_ensino_medio.pdf` — não parafraseie, não invente códigos/descrições. O
  recorte é a unidade "Funções polinomiais de 1º e 2º graus" que a própria BNCC exemplifica
  (501, 401, 507, 502, 402, 503, 302), mais 303/304/508 por analogia; o segundo agrupamento é
  construção nossa e está marcado como tal. `bloom_sugerido` e `exigencias` também são leitura
  nossa, não texto da Base.
- **Duas categorias de verificabilidade, em dois níveis** — não as confunda. A
  `verificabilidade_esperada` está no catálogo, por habilidade, e diz o que ela *admite*; a
  `garantia_obtida` (`garantia_de` em `modelos.py`, coluna `garantia` no banco) diz o que a
  questão *recebeu*. Se a categoria vivesse só na habilidade, "esta habilidade é verificável"
  seria lido como "esta questão foi verificada" — o erro silencioso nos metadados. A distância
  entre as duas é dado do Cap. 6.
- **Compatibilidade com o que já foi gravado** (três pontes, nenhuma removível): a especificação
  aceita `tema` no singular além de `temas`; `Questao` aceita `verificavel` no singular além de
  `verificaveis`; e `banco.py` preenche `temas` e `garantia` na migração a partir das colunas
  antigas. Sem elas o histórico do professor fica ilegível.
- **Tipo novo de verificação** = módulo em `verificacao/` + uma linha no dicionário
  `_ESTRATEGIAS` + testes + descrição no `prompts/gerador.md`. Os módulos existentes têm 50–160
  linhas: o SymPy é a parte barata; calibrar o *prompt* para o LLM emitir a formalização certa
  é o que custa, e falha em silêncio (`nao_verificavel` não reprova a questão).
- **Quando o CAS não conclui, o veredicto é `nao_verificavel` — nunca `rejeitado`.** Não é
  preciosismo: `function_range(2**x)` devolve `EmptySet` (mas acerta `3*2**x`), e tratar isso
  como cálculo válido reprovaria o gabarito correto, mandando o Gerador "corrigir" o que estava
  certo. Idem `is_increasing`, que precisa ser avaliado **no domínio** (`log(x)` sobre R dá
  `False`). Ao escrever um tipo novo, teste as rotinas do SymPy contra casos conhecidos ANTES.
- **`sistema/analisar_logs.py`** reporta a taxa de `nao_verificavel` por tipo/consulta e
  `sistema/exportar_medicao.py` transforma o log em `.md` legíveis + índice CSV. Requerem
  gerações com provedor real; a suíte usa `LLMFake`. Resultados em `sistema/medicoes/`.
- **A suíte não alcança os defeitos que importam.** A medição de 2026-08-07 (`medicoes/`)
  achou três, todos dependentes de escolhas do Gerador impossíveis de antecipar: incógnita
  chamada `E` (número de Euler no SymPy) reprovava gabarito certo; domínio restrito pelo
  contexto (`t >= 0`, `n` natural) reprovava as EM13MAT507/508, que são *sobre* domínio
  discreto; e uma formalização malformada derrubava o ciclo inteiro. **Ao acrescentar tipo
  novo, meça com provedor real — não confie na suíte.**

## Documentos que governam o trabalho (leia antes de editar o texto)

- `projeto_dissertacao_isabella.pdf` — **o projeto**: problema, objetivos, arquitetura, metodologia.
  Orienta *o que* o trabalho é.
- `estrutura_dissertacao_isabella.pdf` — **a estrutura**: capítulos, seções e subseções previstos.
  Orienta *onde* cada conteúdo vai. A numeração e os títulos das seções devem bater com este documento.
- `DOC-20260609-WA0019_260609_180825.pdf` — a **versão rascunho original** da dissertação (Caps. 1–3),
  com muitas repetições e defeitos de compilação. A fonte LaTeX em `dissertacao/` foi **reconstruída a
  partir deste PDF** (o `.tex` original havia sido perdido) já com a revisão aplicada.
- `plano_revisao_dissertacao.md` — o **diagnóstico e plano de revisão**. Contém o mapa de repetições e
  o princípio de correção. Consulte-o antes de mexer no conteúdo dos capítulos.
- `bncc_ensino_medio.pdf` — referência da BNCC (seção 5.2.1, Matemática e suas Tecnologias no EM:
  45 habilidades sob 5 competências específicas). `bncc_ensino_medio.md` é o texto já extraído dele
  — use este para buscar e citar; o PDF fica como fonte de conferência.

## Compilar o documento

Não há toolchain LaTeX no ambiente padrão desta sessão — **a fonte não compila aqui**. A compilação
acontece no Overleaf (a aluna importa este repositório via GitHub) ou localmente:

```
cd dissertacao
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

Arquivo mestre: `dissertacao/main.tex`. Motor: **pdfLaTeX** + **BibTeX** (`natbib`/`plainnat`,
autor-data). Ao editar, prefira mudanças que não dependam de compilar para validar (checar `\label`
↔ `\ref`, chaves de `\cite` ↔ entradas do `.bib`).

## Princípio de edição mais importante: "cada conceito tem um dono"

A revisão inteira deste texto girou em torno de **eliminar repetições**. Ao editar, **não
reintroduza conteúdo que já tem uma casa canônica**. Cada conceito é desenvolvido por extenso em um
único lugar; nos demais, é apenas referenciado com `\ref`. Papel de cada capítulo:

- **Cap. 1** (`cap1_contexto.tex`) — contexto pedagógico ("por que importa para o professor"). **Não**
  explica arquitetura transformer, **não** lista estratégias de mitigação, **não** enuncia a hipótese
  arquitetural por inteiro. Casa canônica do *erro silencioso* (`\label{sec:erro-silencioso}`).
- **Cap. 2** (`cap2_tecnica.tex`) — fundamentação técnica. Casa canônica de: transformer, inferência
  probabilística, taxonomia de erros, CoT/PAL/tool-use/self-consistency, agentes/SMA, CAS/SymPy. A
  **hipótese arquitetural é argumentada por inteiro só em 2.5** (`\label{sec:hipotese}`).
- **Cap. 3** (`cap3_didatica.tex`) — fundamentação didática. Os **seis critérios de qualidade aparecem
  formatados só em 3.4** (`\label{sec:criterios}`). O par "TBR na entrada / SOLO na avaliação" é dito
  uma única vez, em 3.2.3 (`\label{sub:sintese-tax}`).

Cada arquivo de capítulo tem um cabeçalho em comentário `% =====` que reafirma seu papel — respeite-o.

## Convenções desta fonte

- **Bibliografia inferida.** As entradas de `referencias.bib` foram deduzidas do texto (autor + ano) e
  os detalhes (páginas, editora, DOI) são rascunho. Cada entrada a validar está marcada com
  `% CONFERIR`. Não invente dados bibliográficos; mantenha a marca até a aluna confirmar.
- **Todos os capítulos já existem e estão no `\include` do `main.tex`**, com `\label` próprios:
  use `\ref` normalmente entre eles. A regra antiga de referenciar em prosa valia enquanto os
  Caps. 4–6 estavam por escrever; se encontrar remissão em prosa a um capítulo existente, troque
  pela referência cruzada.
- Nome do autor grafado **Pólya** (com acento) no texto corrido.
- Estilo de citação em `natbib` por portabilidade; a migração para `abntex2cite` (padrão ABNT/PROFMAT)
  é uma tarefa aberta e não deve alterar o conteúdo dos capítulos.

## Fluxo de trabalho / Git

- Desenvolver numa branch `claude/<assunto>` (nunca commitar direto na `main`), commitar, push e
  abrir PR em rascunho. A aluna mescla na `main` e sincroniza o Overleaf via GitHub. O histórico
  da `main` é linear — mesclar com rebase, sem commit de merge.
- Ao terminar uma rodada de mudanças no texto, verifique antes do commit: nenhum `[?]`/`??`/chave crua
  no corpo, todo `\ref` com `\label` correspondente, e nenhuma repetição de conteúdo entre casas
  canônicas (ver plano de revisão).

## Tarefas abertas

Elementos pré-textuais (resumo, abstract, folha de rosto, listas); validação da bibliografia
(`% CONFERIR`); migração para `abntex2cite`.

A expansão do catálogo tem plano próprio em `plano_expansao_verificacao.md`, com a
classificação das 45 habilidades por verificabilidade. Feitas: Fases 0, 1, 3 e 2a/2b — 15 das 45
habilidades. Aberta: o resto da Fase 2 (2c a 2g, ~25 habilidades).

Segue fora do alcance do SymPy, por natureza e não por falta de implementação: `401` e `402`
(conversão de registro é propriedade do enunciado). Elas declaram `conferido_em_parte`.
