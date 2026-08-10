# Plano: testar a arquitetura com modelos mais fracos e mais baratos

Preparado, **não executado**. Este documento é o roteiro para rodar sozinho.

## Por que fazer isto

A pergunta que parece estar em jogo — "dá para usar um modelo mais barato?" — não é a
interessante. O acervo inteiro de 90 questões custa US$ 6,93 no Sonnet e 15 centavos no mais
barato da lista: a diferença é real, mas sobre uma base pequena demais para decidir qualquer
coisa nesta dissertação.

A pergunta que importa é outra, e testa a hipótese arquitetural **pelo lado oposto**:

> Se a verificação simbólica faz o que a tese afirma, então um modelo mais fraco deve ser
> *tolerável*. Ele erra mais, o Verificador pega, o ciclo corrige. A arquitetura compra
> confiabilidade que o modelo sozinho não tem.

Isso é medível com o que já existe, e os dois resultados possíveis são publicáveis:

- **Converge com mais iterações** → a arquitetura funciona como anunciado. É evidência direta
  para o Capítulo 6, e sustenta o produto educacional como algo que roda sem depender do modelo
  mais caro.
- **Não converge** → você descobriu o **piso de capacidade** da arquitetura, que é um limite
  honesto a declarar no texto.

Como o eixo é capacidade e não preço, os braços foram escolhidos para **descer a escada**: mesma
família e um degrau abaixo (Haiku), outra família e um degrau bem abaixo (Flash-Lite, V4 Flash),
e por fim um modelo aberto rodando em máquina local — que é o caso que interessa ao professor
sem orçamento, e o requisito explícito do projeto.

## O que se mede, e o que não se mede aqui

O indicador central é a **taxa de `nao_verificavel` por tipo de formalização**. Ele responde à
única exigência que o modelo precisa cumprir para esta arquitetura funcionar: saber escrever
`Rational(21,20)`, `Interval.open(0, oo)`, `Piecewise(...)` dentro de um JSON estrito, em
português, de 3 a 10 formalizações por questão, cerca de 2.300 tokens de saída.

O que **não** se decide aqui: qual modelo escreve questões didaticamente melhores. Isso é
julgamento humano, e quem responde é o painel docente.

## O problema metodológico que este plano resolve

As corridas do Sonnet que já existem **não servem de referência**:

| Corrida | Commit | Problema |
|---|---|---|
| `acervo-2026-08-08` | `996020b` | Verificador ainda tinha os quatro defeitos de extremo/sequência |
| `acervo-2026-08-08-refeito` | `16dfec9` | Anterior às correções de raiz complexa, float e domínio de equação |
| `acervo-consolidado` | mistura dos dois | procedência dupla |

Comparar qualquer modelo contra uma delas confundiria **modelo** com **correção do Verificador** —
as métricas são todas baseadas em veredicto, e o veredicto mudou.

**Por isso todos os braços rodam no mesmo commit**, um depois do outro, incluindo uma corrida nova
do Sonnet como referência. Custa mais e é a única forma de o resultado significar alguma coisa.

## Os braços

| Braço | Provedor | Modelo | US$/1M in / out | 30 ciclos | 90 ciclos |
|---|---|---|---|---|---|
| Referência | `anthropic` | `claude-sonnet-5` | 3,00 / 15,00 | 2,31 | 6,93 |
| Um degrau abaixo | `anthropic` | `claude-haiku-4-5` | 1,00 / 5,00 | 0,62 | 1,84 |
| Barato com formato garantido | `gemini` | `gemini-2.5-flash-lite` | 0,10 / 0,40 | ~0,05 | ~0,16 |
| Barato e forte em matemática | `deepseek` | `deepseek-v4-flash` | 0,14 / 0,28 | ~0,05 | ~0,15 |
| Aberto, local | `ollama` | `qwen2.5:14b` | — | 0 | 0 |

**Os cinco braços, a 30 ciclos cada, custam cerca de US$ 3.** Completos, cerca de US$ 9.

Base de cálculo: 7.309 tokens de entrada e 3.674 de saída por questão no Sonnet, medidos com
`count_tokens` sobre uma amostra real do acervo, incluindo iterações de revisão e as chamadas ao
Crítico. O Haiku usa um tokenizador mais antigo e converte o mesmo texto em ~21% menos tokens —
por isso sai por 27% do custo do Sonnet, e não por 33% como a razão de preço sugeriria. Para os
não-Anthropic os números estão marcados com `~` porque o tokenizador difere e usei o perfil do
Haiku como aproximação. A DeepSeek cobra US$ 0,0028/1M em cache-hit e o *system prompt* deste
sistema é fixo: o custo real dela tende a ficar abaixo da tabela.

Preços conferidos nas páginas oficiais em 9 de agosto de 2026 —
[Anthropic](https://claude.com/pricing), [Gemini](https://ai.google.dev/gemini-api/docs/pricing),
[DeepSeek](https://api-docs.deepseek.com/quick_start/pricing). Os agregadores discordavam entre si
e do fabricante; não use nenhum deles.

### Por que estes quatro, e não outros

- **Haiku 4.5** isola a capacidade do modelo: mesma família, mesmo tokenizador, mesma disciplina
  de formato, zero mudança de código. É o braço mais limpo do ponto de vista experimental.
- **Gemini 2.5 Flash-Lite** é o melhor par preço/garantia-de-formato: 1/30 do Sonnet com
  *structured outputs* no endpoint compatível.
- **DeepSeek V4 Flash** é o mais barato com cache e o mais forte em matemática entre os baratos.
  **Ressalva séria:** a própria documentação avisa que haverá aumento "significativo" de preço,
  sem data. Um número que vai para o texto da dissertação precisa da data da consulta ao lado.
- **GPT-5 nano/mini ficaram de fora** apesar do preço de tabela: são modelos de raciocínio, e os
  tokens de *reasoning* são cobrados como saída — o custo real fica bem acima da linha da tabela.
  O código suporta os dois, se você quiser incluí-los mesmo assim.
- **Local:** `qwen2.5:14b` é o padrão já configurado. `phi4` (14B) é a alternativa a considerar —
  benchmarks de terceiros o põem acima do Qwen2.5 14B em MATH (80,4% contra 75,6%) rodando em
  16 GB de VRAM. Nenhum dos dois foi testado nesta tarefa: escolher entre eles **é** parte do que
  este braço mede.

## O que já está pronto

- `gerar_acervo.py` aceita `--provedor` e `--modelo`. Plano e semente são fixos, então todos os
  braços recebem **exatamente as mesmas especificações**, na mesma ordem, com os mesmos contextos
  sorteados. É o que torna a comparação justa.
- `comparar_execucoes.py` põe **duas** execuções lado a lado: aprovação, descarte, iterações,
  garantia obtida, taxa de não-verificável por tipo e reprovações por tipo. Para cinco braços,
  rode-o quatro vezes contra a mesma referência.
- `analisar_logs.py` e `exportar_medicao.py` funcionam igual para qualquer execução.
- Cada pasta ganha um `execucao.json` com data, provedor, modelo e commit — o comparador lê o nome
  do modelo daí, e é o que torna a execução reproduzível.

### O que foi corrigido no código para este plano existir

Antes desta rodada, três dos cinco braços eram **inalcançáveis**:

1. `openai_llm.py` construía `openai.OpenAI()` **sem `base_url`**. Gemini e DeepSeek publicam
   endpoints compatíveis com a API de chat da OpenAI, mas sem esse parâmetro só dava para chegar
   neles pela variável global `OPENAI_BASE_URL` — o que quebraria o provedor OpenAI na mesma
   sessão. Agora `criar_provedor` aceita `'gemini'` e `'deepseek'` como nomes próprios, cada um
   com o seu endereço, a sua variável de chave (`GEMINI_API_KEY`, `DEEPSEEK_API_KEY`) e o seu
   modelo padrão. O parâmetro `url` serve de `base_url` para um compatível fora da lista (Groq,
   OpenRouter, um vLLM da universidade).
2. `temperature` era enviado **sempre**. A família de raciocínio da OpenAI (`gpt-5`, `o1`, `o3`,
   `o4`) devolve 400 com valor diferente de 1 e troca `max_tokens` por `max_completion_tokens` —
   o mesmo problema que `FAMILIAS_COM_TEMPERATURA` já resolvia do lado da Anthropic.
3. **Nenhum modo JSON e nenhum teto de saída.** O contrato de formato dependia só da instrução em
   prosa — o Sonnet aguenta, um modelo pequeno não. Agora todos os compatíveis recebem
   `response_format: json_object` e `max_tokens=8000`, e o Ollama recebe `format: "json"` e
   `num_predict=8000`. **Este era o defeito mais grave para o braço local:** o Ollama trunca em
   128 tokens por omissão, então toda questão saía cortada no meio e o modelo aberto pareceria
   incapaz da tarefa quando o problema era de configuração.

Truncamento e resposta vazia agora levantam exceção com a causa dita, em vez de devolver um JSON
pela metade — o Orquestrador já sabe reagir a exceção pedindo concisão (`_gerar_com_folga`), e a
DeepSeek avisa explicitamente que o modo JSON dela às vezes devolve conteúdo vazio.

`tests/test_provedores.py` cobre os três pontos; antes não havia teste nenhum desta camada.

## Como rodar

Da pasta `sistema/`. **Escolha o tamanho primeiro.** O recorte de 5 habilidades dá sinal
suficiente para as taxas por tipo e custa um terço:

```sh
HABS=EM13MAT302,EM13MAT304,EM13MAT402,EM13MAT501,EM13MAT507   # 30 ciclos por braço
# ou, para o teste completo, omita --apenas em todos os comandos (90 ciclos por braço)
```

Uma função para não repetir o laço:

```sh
braco() {           # braco <pasta> <provedor> <modelo>
  DEST=medicoes/$1; mkdir -p $DEST
  for i in 1 2 3; do
    ./.venv/bin/python gerar_acervo.py $DEST --parte=$i/3 --apenas=$HABS \
      --provedor=$2 --modelo=$3 >> $DEST/worker.log 2>&1 &
  done; wait
  echo "--- $1 concluído"
}
```

```sh
export ANTHROPIC_API_KEY=...
braco comp-sonnet   anthropic claude-sonnet-5        # referência, no commit atual
braco comp-haiku    anthropic claude-haiku-4-5

export GEMINI_API_KEY=...
braco comp-gemini   gemini    gemini-2.5-flash-lite

export DEEPSEEK_API_KEY=...
braco comp-deepseek deepseek  deepseek-v4-flash

# local: `ollama serve` rodando e `ollama pull qwen2.5:14b` feito antes
braco comp-local    ollama    qwen2.5:14b
```

**Comparar** — sempre contra a mesma referência:

```sh
for m in haiku gemini deepseek local; do
  ./.venv/bin/python comparar_execucoes.py medicoes/comp-sonnet medicoes/comp-$m
done
```

**Guardar as questões para leitura humana:**

```sh
./.venv/bin/python exportar_medicao.py medicoes/comp-gemini/ciclos.jsonl \
                                        medicoes/comp-gemini/questoes
```

### Ressalvas de execução

- **O braço local não paraleliza.** Uma GPU serve um pedido de cada vez: rode com `--parte=1/1` e
  espere. Estime horas, não minutos.
- Instale a dependência do provedor: `pip install -e ".[gemini]"` (ou `[deepseek]`, `[ollama]`) —
  Gemini e DeepSeek usam a mesma biblioteca `openai`.
- Tempo dos braços de API: o Sonnet fez 48 ciclos em 39 minutos com 3 processos. Estime ~25 min
  por braço no recorte de 30, ~75 min no completo. Os menores tendem a ser mais rápidos.

## O que olhar, e o que cada resultado significa

Em ordem de importância:

**1. Taxa de não-verificável por tipo.** É o indicador central. Se um modelo disparar em um tipo
específico, o problema é daquele tipo no *prompt*, não do modelo em geral — e é corrigível. Se
disparar em todos, o modelo não sustenta a formalização.

**2. Descartes.** Quantas questões não sobreviveram a três iterações. É o teste de convergência.

**3. Iterações até aprovar.** Se um modelo converge em 2 ou 3 onde o Sonnet converge em 1, **a
arquitetura está fazendo exatamente o que a tese diz.** Este é o resultado que se quer.

**4. Reprovações por tipo.** Se o Verificador reprova mais com o modelo menor, ele está pegando
erro de verdade — o que é bom sinal para a arquitetura, não mau sinal para o modelo.

## Ressalvas

**A arquitetura protege o Gerador, não o Crítico.** Um erro do Gerador o SymPy pega; um erro de
julgamento do Crítico ninguém pega. Este teste troca o modelo nos **dois** papéis ao mesmo tempo,
então um resultado ruim não distingue qual dos dois degradou. Se der ruim, a rodada seguinte é o
modelo menor só no Gerador, mantendo o Crítico no Sonnet — hoje `gerar_acervo.py` usa o mesmo
provedor para os dois, e separá-los é uma linha.

**Não regenere o acervo com o resultado.** O acervo de 90 questões já está fechado e é o material
da Rodada 1 de avaliação. As execuções deste teste vão para pastas próprias e não substituem nada.

**As questões geradas pelos outros modelos não entram no material do painel** sem decisão
explícita — mudar o modelo no meio muda a procedência do acervo.

**Preço e disponibilidade têm data.** Modelos baratos são descontinuados e reprecificados com
frequência (os Gemini 2.0 Flash saíram do ar em 1º de junho de 2026; a DeepSeek já avisou de
aumento). Qualquer número desses que entre na dissertação precisa da data da consulta ao lado, e
o modelo do produto educacional deve ser um que sobreviva à defesa.
