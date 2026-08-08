# Acervo estratificado — 8 de agosto de 2026

90 questões planejadas (15 habilidades × 2 formatos × 3 dificuldades), **89 concluídas**.
Gerado com `claude-sonnet-5` no commit `996020b`, em três processos paralelos.

Serve a dois fins: o banco do produto educacional (o projeto pede 60–100 questões) e a fonte do
material da Rodada 1 de avaliação.

## Resultado bruto

77 aprovadas, 12 descartadas. Das aprovadas: 47 na primeira iteração, 23 na segunda, 7 na terceira.
Garantia obtida: 65 conferidas, 11 conferidas em parte, 1 sem conferência.

O ciclo que faltou morreu com `max_tokens`: o modelo esgotou o limite de saída antes de fechar o
JSON, e o `RuntimeError` derrubou o ciclo. É o mesmo padrão da formalização malformada — saída
imprevista do LLM matando a questão inteira em vez de degradar.

## O achado principal: 22 das 35 reprovações são FALSAS

A correção do domínio restrito (feita ontem) funcionou: `funcao/dominio` teve 6 não-verificáveis e
**zero reprovações**, contra 4 falsas na medição anterior. Mas o acervo expôs três defeitos novos,
todos da mesma família — o verificador reprovando gabarito correto.

**1. `maximo` e `minimo` usam só o primeiro ponto crítico (15 reprovações falsas).**
`funcoes.py` faz `candidatos = solve(diff(f, x), x)` e avalia `candidatos[0]`. Numa parábola há um
ponto crítico e funciona; numa função trigonométrica há vários. Para `3*cos(pi*t/6) + 7/2`, o solve
devolve `[0, 6]`, e `f(0) = 13/2` é o **máximo** — então o mínimo correto (`1/2`) é reprovado.
Foi o que destruiu a EM13MAT306: **4 dos 6 ciclos dela foram descartados** por isso.
A correção é usar `sp.minimum` / `sp.maximum`.

**2. `maximo` e `minimo` ignoram o domínio declarado (incluído nas 15 acima).**
Em `-p²/2 + 380p - 25000` com domínio `[400, ∞)`, o vértice está em `p=380`, **fora** do domínio.
O verificador calculou `f(380) = 47200`; o máximo real no domínio é `f(400) = 47000`, que era o
gabarito. O Gerador tinha razão, e ainda por cima usou corretamente o parâmetro `dominio` que
acrescentamos ontem para a imagem — o código é que só o lê na consulta de imagem.

**3. `sequencia` fixa a indexação em 1 (7 reprovações falsas).**
`_conferir_sequencia` exige `f(1) = a1`. O Gerador frequentemente escreve a forma fechada indexada
em 0 — `800*(21/20)**n` com `f(0) = 800`, que é natural para "após n meses" e é o que os `pontos`
que ele mesmo declara indicam. Ambas as convenções são legítimas; o verificador aceita uma só.

**4. `n` é inteiro e positivo no catálogo de símbolos (parte das 7 reprovações de `equacao`).**
`_LOCAIS` define `n = Symbol("n", integer=True, positive=True)`, o que é certo para índice de
progressão. Mas quando o Gerador nomeia `n` uma incógnita qualquer, `solve(5n + 17 = 150)` devolve
`[]` — não há inteiro — e o gabarito correto `133/5` é reprovado.

Restam 12 reprovações a inspecionar uma a uma (7 de `equacao`, 2 de `propriedade`, 2 de `valor`,
1 de `imagem`), com dois padrões visíveis: o SymPy devolvendo todas as raízes complexas onde o
gabarito traz só a real, e gabaritos arredondados (`2025.82`) contra o valor exato.

## Consequência para o uso deste acervo

As 77 aprovadas são material válido: passaram pelo Verificador e pelo Crítico.

Os **12 descartes não são material de erro** — a maioria foi descartada por reprovação falsa, e a
questão descartada estava certa. **Não usar como espécime do Bloco I sem conferir à mão.** Vale
sobretudo para os 4 descartes da EM13MAT306.

Depois de corrigidos os defeitos acima, vale regerar as habilidades afetadas — 306, 503 e 303,
cerca de 20 ciclos, não as 90.

## Arquivos

- `ciclos.jsonl` — log completo, uma linha por ciclo (também em `ciclos-1..3.jsonl`, por processo)
- `questoes/` — um `.md` por ciclo, com trilha completa; `_indice.csv` com as colunas de análise
- `taxa_por_tipo.txt` — taxa de não-verificável por tipo/consulta
- `execucao.json` — data, modelo, commit, semente
