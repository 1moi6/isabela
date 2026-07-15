# Sistema multiagente de geração assistida de questões — Matemática EM

Implementação do sistema descrito na dissertação (PROFMAT/UFMT): o professor fornece parâmetros
didáticos e o sistema gera questões com gabarito e resolução, **verifica a correção via SymPy**,
**avalia a qualidade didática** com uma rubrica fundamentada e monta **listas de exercícios**.

## Arquitetura

| Agente | Mecanismo | Papel |
|---|---|---|
| **Gerador** | LLM | Produz enunciado, resolução, gabarito, distratores e a formalização SymPy |
| **Verificador Simbólico** | SymPy (sem LLM) | Resolve a questão de forma independente e compara com o gabarito |
| **Crítico Didático** | LLM + rubrica | Avalia clareza, adequação ao nível (Bloom/SOLO), alinhamento BNCC, distratores, originalidade |
| **Orquestrador** | Python puro | Decide: aprova, devolve com feedback (máx. 3 iterações) ou descarta |

Parâmetros do professor: **tema** (funções afim/quadrática/exponencial, PA, PG), **habilidade BNCC**,
**nível cognitivo (Bloom)**, **dificuldade**, **natureza** (teórica/aplicada), **formato**
(discursiva/múltipla escolha), contexto e restrições opcionais.

## Instalação

```bash
cd sistema
pip install -e ".[dev,app,anthropic]"   # troque 'anthropic' por 'openai' ou 'ollama'
```

## Configuração do LLM

| Variável | Valores | Padrão |
|---|---|---|
| `QUESTOES_PROVEDOR` | `anthropic` \| `openai` \| `ollama` | `anthropic` |
| `QUESTOES_MODELO` | nome do modelo | padrão do provedor |
| `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` | chave da API | — |

Com **Ollama** (modelos abertos, sem chave): instale o Ollama, `ollama pull qwen2.5:14b` e use
`QUESTOES_PROVEDOR=ollama`.

## Uso

**Interface web (professor):**

```bash
streamlit run app/streamlit_app.py
```

Três abas: *Gerar questão* (especifica → gera → vê os pareceres → salva), *Banco* (consulta o banco
curado com filtros) e *Montar lista* (seleciona questões e exporta Markdown/LaTeX, versões aluno e
professor).

**Programático:**

```python
from questoes.agentes import Gerador, VerificadorSimbolico, CriticoDidatico, Orquestrador
from questoes.especificacao import *
from questoes.llm import criar_provedor

llm = criar_provedor("anthropic")
orq = Orquestrador(Gerador(llm), VerificadorSimbolico(), CriticoDidatico(llm))
resultado = orq.produzir(Especificacao(
    tema=Tema.FUNCAO_QUADRATICA, habilidade_bncc="EM13MAT302",
    nivel_bloom=NivelBloom.APLICAR, dificuldade=Dificuldade.MEDIA,
    natureza=Natureza.APLICADA, formato=Formato.MULTIPLA_ESCOLHA,
))
print(resultado.aprovada, resultado.questao_final)
```

## Testes

```bash
python -m pytest        # 36 testes; não exigem chave de API (LLM fake)
```

## Rastreabilidade e reprodutibilidade

- Todas as iterações de cada ciclo são registradas (`logs/ciclos.jsonl` e no banco).
- Temperatura padrão 0,3; prompts versionados em `prompts/` (citáveis no Apêndice A da dissertação).
- O banco SQLite (`banco_questoes.db`) guarda a questão aprovada, os metadados e o histórico completo.

## Limites conhecidos

- A verificação simbólica cobre equações, propriedades de funções e progressões (o recorte).
  Questões não formalizáveis recebem o veredito `nao_verificavel` e a validação fica com o professor.
- O catálogo BNCC (`dados/bncc_em_matematica.json`) contém as habilidades do recorte, com descrições
  a conferir contra o texto oficial.
