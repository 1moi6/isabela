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

Para o professor, sem linha de comando: duplo clique em `instalar.bat` (Windows) ou
`instalar.command` (macOS); depois, `iniciar.bat` / `iniciar.command` sempre que for usar.

Para desenvolvimento:

```bash
cd sistema
pip install -e ".[dev,app,anthropic]"   # troque 'anthropic' por 'openai' ou 'ollama'
```

## Configuração do LLM

**Pela interface (recomendado):** botão *Configurações* no canto superior direito — provedor,
modelo, chave de API e pasta sincronizada. A chave fica apenas na memória do processo enquanto
o programa estiver aberto; **nunca é gravada em disco**.

**Por variável de ambiente** (usada quando o campo da interface fica vazio; única via para uso
programático): `ANTHROPIC_API_KEY` ou `OPENAI_API_KEY`.

As demais preferências (provedor, modelo, pasta sincronizada) ficam em `config_local.json`,
fora do controle de versão.

Com **Ollama** (modelos abertos, sem chave): instale o Ollama, `ollama pull qwen2.5:14b` e
selecione `ollama` nas configurações.

## Uso

**Interface do professor:**

```bash
python executar.py       # escolhe uma porta livre e abre o navegador
```

Duas abas. Em *Gerar*, o professor descreve a questão, escolhe quantas quer (até 10 por vez) e
acompanha cada uma chegando com a **trilha do ciclo**: o que o gerador produziu, o que o
verificador simbólico recalculou e como o crítico pontuou. Em *Banco curado*, consulta o que
salvou, **registra a própria avaliação** de cada questão (aceita / aceita com ajuste / recusada,
com comentário) e seleciona questões para exportar a lista em Markdown, LaTeX ou Word.

## Uso compartilhado (vários professores)

Por padrão o sistema é de uso individual e não pede autenticação. Criar o primeiro
convite liga o modo compartilhado:

```bash
python gerenciar_convites.py criar "Maria Silva" http://seu-endereco
python gerenciar_convites.py listar
python gerenciar_convites.py remover CODIGO
python executar.py --rede            # passa a aceitar conexões externas
```

Cada pessoa recebe um link (`http://.../?convite=CODIGO`), abre uma vez e o navegador guarda
o acesso. O código sai da barra de endereço na primeira visita.

Três garantias sustentam esse modo:

- **Bancos isolados.** Cada pessoa só vê, avalia e exporta as próprias questões. O dono é
  derivado do nome, não do código: revogar e reemitir um convite preserva o banco da pessoa.
- **Chave de API de cada um fica no navegador dela** e viaja em cada requisição; o servidor
  usa e descarta. Ninguém guarda credencial de terceiro. A chave *passa* pelo servidor para
  chegar ao provedor — a interface diz isso a quem usa.
- **Preferências do servidor** (pasta sincronizada, modelo) só são editáveis na máquina onde
  ele roda; um convidado não redireciona o espelho do dono.

`--rede` é recusado sem convites cadastrados. Para voltar ao modo local, apague `convites.json`
— revogar todos os convites deixa o arquivo vazio, o que **bloqueia todo mundo** em vez de
reabrir o acesso.

`convites.json` fica fora do controle de versão: quem tem o código entra como a pessoa.

## Ao mudar a interface, troque a versão dos arquivos

`docs/index.html` e `docs/gerar_convites/index.html` referenciam CSS e JS com um sufixo
`?v=AAAAMMDDx`. **Atualize esse sufixo em toda mudança no frontend.** O GitHub Pages manda
cachear os arquivos, e sem a troca quem já visitou continua executando a versão antiga —
inclusive correções de defeito não chegam a quem mais precisa delas.

## Publicar na internet (túnel cloudflared)

```bash
python publicar.py
```

O aplicativo sobe escutando **apenas em `127.0.0.1`** e o `cloudflared` abre uma conexão de
dentro para fora, devolvendo um endereço HTTPS. Ao final, o script imprime o link pronto de
cada convite já com o endereço da vez.

Por que assim, e não abrindo uma porta no firewall:

- Nenhuma porta de entrada precisa ser liberada — a conexão parte de dentro da rede.
- Sem o túnel no ar, a máquina não fica escutando na rede: não há porta exposta.
- O endereço é HTTPS. Isso é requisito, não refinamento: quem usa digita a **própria chave de
  API** na página, e em HTTP puro ela atravessaria a rede em texto claro.

O script recusa subir sem convites cadastrados.

**Links de convite permanentes sem comprar domínio.** O túnel rápido sorteia um endereço novo a
cada subida, o que invalidaria os convites já enviados. Para evitar isso, o `publicar.py` grava o
endereço da vez num `docs/backend.json` no próprio repositório, e a interface o lê ao abrir —
então o link não precisa mais carregar o endereço:

```bash
export QUESTOES_GITHUB_TOKEN=github_pat_...   # token com permissão de escrita em conteúdo
```

e em `config_local.json`:

```json
{ "repositorio_frontend": "1moi6/isabela", "caminho_backend_json": "docs/backend.json" }
```

O token vem do ambiente, nunca do arquivo de configuração. Se faltar ou o GitHub recusar, o
`publicar.py` avisa e volta a imprimir links com `&api=` — publicar é conveniência, não requisito.
O Pages leva cerca de um minuto para servir a atualização depois do commit.

**Endereço fixo (túnel nomeado).** O túnel rápido sorteia um endereço novo a cada execução, o
que obriga a reenviar os links. Para um endereço estável é preciso conta na Cloudflare e um
domínio: `cloudflared tunnel login`, `cloudflared tunnel create questoes`, apontar um registro
DNS para ele e rodar `cloudflared tunnel run questoes` em paralelo a `python executar.py`.
Vale a pena se o painel for durar semanas; para uma rodada de avaliação, o túnel rápido basta.

**Deixar no ar depois de fechar o terminal:** `nohup python publicar.py > publicar.log 2>&1 &`
(ou um serviço systemd, se a máquina reiniciar com frequência).

## Pasta sincronizada (Google Drive)

Nas configurações, aponte uma pasta que o Google Drive para Desktop já sincronize. A cada questão
salva, o sistema grava ali um `.md` legível, um `.json` com o ciclo completo e regrava um
`_indice.csv` com uma linha por questão — incluindo veredicto do verificador, nota mínima do
crítico, número de iterações e a avaliação do professor. Em modo compartilhado, cada pessoa
ganha uma subpasta própria. Não há autenticação nem chamada de rede:
quem sincroniza é o cliente da nuvem, e o índice em CSV abre direto no Sheets ou no Excel.

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
python -m pytest        # 56 testes; não exigem chave de API (LLM fake)
```

## Rastreabilidade e reprodutibilidade

- Todas as iterações de cada ciclo são registradas (`logs/ciclos.jsonl` e no banco).
- Prompts versionados em `prompts/` (citáveis no Apêndice A da dissertação).
- O banco SQLite (`banco_questoes.db`) guarda a questão aprovada, os metadados, o histórico
  completo e a avaliação do professor.
- A temperatura é fixada em 0,3 nos provedores que ainda a expõem. Os modelos mais recentes da
  Anthropic removeram os parâmetros de amostragem: nesses casos a requisição vai sem o parâmetro
  (ver `llm/anthropic_llm.py`), e a reprodutibilidade se apoia no log integral e nos prompts
  versionados.

## Limites conhecidos

- A verificação simbólica cobre equações, propriedades de funções e progressões (o recorte).
  Questões não formalizáveis recebem o veredito `nao_verificavel` e a validação fica com o professor.
- O catálogo BNCC (`dados/bncc_em_matematica.json`) contém as habilidades do recorte, com descrições
  a conferir contra o texto oficial.
