# Fonte LaTeX da dissertação (reconstruída)

Esta pasta contém a **fonte editável** da dissertação, reconstruída a partir do PDF
`DOC-20260609-WA0019` (o `.tex` original havia sido perdido) e já com o plano de revisão de
repetições aplicado (ver `../plano_revisao_dissertacao.md`).

## Estrutura

```
dissertacao/
├── main.tex                       # arquivo mestre (compile este)
├── referencias.bib                # bibliografia reconstruída — VER "% CONFERIR"
└── capitulos/
    ├── cap1_contexto.tex          # Cap. 1 — contexto e desafios
    ├── cap2_tecnica.tex           # Cap. 2 — fundamentação técnica
    └── cap3_didatica.tex          # Cap. 3 — referenciais didáticos
```

## Como compilar

No **Overleaf**: suba a pasta, selecione o motor **pdfLaTeX** e compile `main.tex`
(o Overleaf roda o BibTeX automaticamente). Localmente:

```
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

> Não há toolchain LaTeX no ambiente onde a fonte foi reconstruída, então ela **não foi
> compilada aqui**. Pode haver um ou outro ajuste de pacote/acento ao compilar pela primeira vez.

## O que ainda precisa de você (importante)

1. **Bibliografia (`referencias.bib`).** As entradas foram **inferidas** do texto (autor + ano que o
   próprio texto cita). Páginas, editora, volume, DOI e edição são rascunho. Cada entrada a validar
   está marcada com `% CONFERIR`. Há duas que exigem atenção especial:
   - `miranda2015taxonomia` — o texto não dá título nem autoria completa; preencher.
   - `brasil2018bncc` / `brasil1998pcn` — conferir a referência ABNT oficial.
2. **Unidades temáticas da BNCC** (Seção 3.3.2): o rascunho dizia "quatro" mas listava três. Foi
   corrigido para três (as efetivamente discutidas), com marca `% CONFERIR` — validar contra a BNCC.
3. **Referências a capítulos ainda não escritos** (4 — arquitetura; 5 — implementação; 6 — avaliação):
   estão como remissões em prosa ("no capítulo de arquitetura", "no capítulo de avaliação"), sem
   `\ref`, para não gerar `??`. Ao escrever esses capítulos, trocar pela referência cruzada com `\label`.
4. **Estilo de citação.** Está em `natbib`/`plainnat` (autor-data) por portabilidade. Para o padrão
   ABNT do PROFMAT, migrar para `abntex2cite` — sem mexer no conteúdo dos capítulos.
5. **Elementos pré-textuais** (folha de rosto, resumo, abstract, listas) entram conforme o template
   oficial; há um marcador no `main.tex`.

## O que mudou em relação ao PDF original

- **Citações** `[?]` e chaves cruas (`russell2021`, `wei2022chain`, …) → `\cite` reais.
- **Referências cruzadas** `Seção ??` / `Capítulo ??` → `\label`/`\ref` (para alvos existentes).
- **Resíduo de andaime** ("Descrição: capítulo técnico-central…") no início do Cap. 2 → removido.
- **Numeração do Cap. 2** corrigida: "Agentes e sistemas multiagentes" passou de 2.2.5/2.2.6 para 2.3.
- **Desduplicação:** conteúdo técnico (transformer, inferência, taxonomia de erros, CoT) deixou o
  Cap. 1 e foi para sua casa canônica no Cap. 2; a hipótese arquitetural é argumentada só em 2.5; os
  seis critérios de qualidade aparecem formatados só em 3.4; "TBR na entrada / SOLO na avaliação" é
  dito uma vez (3.2.3). Detalhes em `../plano_revisao_dissertacao.md`.
- **Correções pontuais:** "saltos inferenciais", "multiestruturais", unidades temáticas da BNCC.
