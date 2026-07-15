# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the **dissertação de mestrado (PROFMAT/UFMT)** de Isabella Dias Ribeiro dos Santos,
orientada pelo Prof. Dr. Moiseis dos Santos Cecconello, **e a implementação do sistema que ela
descreve**: um sistema multiagente para geração assistida de questões de Matemática do Ensino Médio
(LLM gerador + verificador simbólico via SymPy + crítico didático + orquestrador).

Dois artefatos:
- `dissertacao/` — o texto em LaTeX (Caps. 1–3 escritos; 4–7 pendentes).
- `sistema/` — o código Python do sistema (produto educacional; ver `sistema/README.md`).

## Trabalhar no código (`sistema/`)

```
cd sistema
pip install -e ".[dev]"     # sympy, pydantic, pytest — suficiente para os testes
python -m pytest            # 36 testes; NÃO exigem chave de API (usam LLM fake)
python -m pytest tests/test_orquestrador.py -k descarte   # um teste específico
streamlit run app/streamlit_app.py    # UI (requer .[app] e um provedor configurado)
```

Pontos estruturais que não são óbvios pelos nomes de arquivo:
- **O Verificador não usa LLM.** `agentes/verificador.py` delega a `verificacao/` (SymPy puro).
  A ponte entre a prosa da questão e o SymPy é o campo `verificavel` (`ExpressaoVerificavel` em
  `modelos.py`), que o Gerador preenche — o Verificador nunca interpreta enunciado.
- **A política de decisão vive só no Orquestrador** (`agentes/orquestrador.py`): rejeição do
  verificador volta ao Gerador sem passar pelo Crítico; `nao_verificavel` segue ao Crítico;
  3 iterações sem aprovação = descarte. Testes de política usam `LLMFake` (test_orquestrador.py).
- **Provedores de LLM são plugáveis** via `llm/criar_provedor` (`anthropic`/`openai`/`ollama`);
  dependências de provedor são opcionais no `pyproject.toml` — não as torne obrigatórias.
- **Prompts são artefatos da pesquisa** (`prompts/*.md`): serão citados no Apêndice A da
  dissertação. Mudanças neles afetam o texto acadêmico — trate como mudança de conteúdo.
- O catálogo BNCC (`dados/bncc_em_matematica.json`) tem descrições parafraseadas **a conferir**
  contra `bncc_ensino_medio.pdf`; não invente códigos/descrições novas.

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
- `bncc_ensino_medio.pdf` — referência da BNCC para conferir habilidades e unidades temáticas.

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
- **Referências a capítulos ainda não escritos** (4 — arquitetura; 5 — implementação; 6 — avaliação)
  são feitas **em prosa** ("no capítulo de arquitetura"), **sem `\ref`**, para não gerar `??`. Ao
  escrever esses capítulos, criar o `\label` e trocar pela referência cruzada.
- Nome do autor grafado **Pólya** (com acento) no texto corrido.
- Estilo de citação em `natbib` por portabilidade; a migração para `abntex2cite` (padrão ABNT/PROFMAT)
  é uma tarefa aberta e não deve alterar o conteúdo dos capítulos.

## Fluxo de trabalho / Git

- Desenvolver na branch designada (atualmente `claude/dissertation-repetition-review-dcv1bt`), commitar,
  push e abrir PR em rascunho. A aluna mescla na `main` e sincroniza o Overleaf via GitHub.
- Ao terminar uma rodada de mudanças no texto, verifique antes do commit: nenhum `[?]`/`??`/chave crua
  no corpo, todo `\ref` com `\label` correspondente, e nenhuma repetição de conteúdo entre casas
  canônicas (ver plano de revisão).

## Tarefas abertas

Elementos pré-textuais (resumo, abstract, folha de rosto, listas); Capítulos 4–6; validação da
bibliografia (`% CONFERIR`); confirmação das unidades temáticas da BNCC em 3.3.2; migração para
`abntex2cite`.
