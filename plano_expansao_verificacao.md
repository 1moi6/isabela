# Plano de expansão da verificação simbólica

Como incorporar as habilidades da BNCC hoje ausentes do sistema, **declarando por categorias o
grau de garantia que cada uma admite** em vez de silenciar as que o núcleo simbólico não alcança.

Estado atual (Fases 0, 1, 3 e 2a/2b **feitas**): 15 das 45 habilidades estão no catálogo
(`sistema/dados/bncc_em_matematica.json`). O Verificador tem quatro estratégias — `equacao`,
`funcao`, `progressao`, `propriedade` — registradas num dicionário em `verificacao/__init__.py`.
Um `tipo` desconhecido devolve `NAO_VERIFICAVEL`, nunca exceção: o ponto de extensão é limpo.

Meta: **40 habilidades no catálogo**, cada uma com sua categoria de verificabilidade declarada; 5
fora de escopo, com a razão registrada.

## 1. O diagnóstico: "não verificável" esconde quatro problemas

O erro a evitar é tratar as habilidades ausentes como um bloco. Elas resistem por razões
distintas, e três delas pedem soluções distintas. Estes quatro grupos são a **razão** que
acompanha cada classificação na tabela da Seção 5 — sem a razão, a categoria seria arbitrária.

**Grupo 1 — a resposta é computável; falta a estratégia.** A matemática tem resposta determinada
que o SymPy calcula sem dificuldade; simplesmente não há um `tipo` que a enderece. Sistemas
lineares, funções logarítmicas e trigonométricas, áreas e volumes, contagem e probabilidade,
estatística descritiva, grandezas e unidades. **Solução: mais módulos em `verificacao/`.**
Trabalho incremental, de baixo risco.

**Grupo 2 — o verificável é uma propriedade, não uma resposta.** A habilidade pede um objeto cuja
correção é um predicado, não um valor. Investigar padrões numa tabela e generalizar algebricamente
(501, 502) não tem "a resposta": tem uma expressão que precisa *reproduzir os pontos da tabela* e
*ser do grau declarado*. Idem a metade não verificada de 507 e 508 — a associação entre a
progressão e a função de domínio discreto. **Solução: um contrato de verificação que afirme
predicados** em vez de comparar gabaritos.

**Grupo 3 — o que resiste é a forma da questão, não a matemática.** Em 401 e 402 ("converter
representações algébricas em geométricas") o cálculo é trivialmente verificável; o que nenhum CAS
decide é se o enunciado *exige a conversão de registro*. Isso é propriedade do enunciado, não do
cálculo. **Solução: nenhuma verificação simbólica resolve.** O que cabe é declarar o grau —
e cobrar a exigência via Crítico, como já fazemos.

**Grupo 4 — não são questões de avaliação.** 201, 202 e 203 descrevem projetos de médio prazo
(propor ações comunitárias, executar pesquisa amostral, criar aplicativos). 315 e 406 são
verificáveis, mas por *execução*, não por CAS. **Solução: fora de escopo, com a razão dita.**

## 2. Duas categorias, em dois níveis

Este é o ponto que sustenta a proposta inteira, e não é detalhe de implementação.

A mesma habilidade produz questões com garantias diferentes. Com a EM13MAT302, o Gerador às vezes
preenche a formalização e o SymPy confere o gabarito; às vezes devolve `verificavel: null` e a
questão passa apenas pelo Crítico. Logo, são duas coisas distintas:

| | Onde vive | O que afirma |
|---|---|---|
| **`verificabilidade_esperada`** | catálogo, por habilidade | que garantia esta habilidade *admite*, em princípio |
| **`garantia_obtida`** | banco, por questão | que garantia esta questão *recebeu*, de fato |

Se a categoria existisse só na habilidade, o professor leria "esta habilidade é verificável
simbolicamente" como "esta questão foi verificada" — o erro silencioso que a dissertação combate,
reintroduzido no nível dos metadados.

A distância entre os dois níveis é **resultado empírico do Cap. 6**: em quais habilidades a
garantia esperada não se realiza na prática? O dado sai do log de ciclos que já gravamos.

### Os três níveis, nomeados para quem usa

O rótulo é lido por um professor, não por um engenheiro. E o terceiro precisa ler como instrução,
não como etiqueta:

- **gabarito conferido** — o SymPy recalculou de forma independente e bateu;
- **conferido em parte** — parte das afirmações foi recalculada; o resto é julgamento didático;
- **sem conferência automática — revise o gabarito**.

Isto não é conceito novo: `Veredicto.APROVADO_RESSALVA_NUMERICA` já existe no código justamente
para exprimir uma garantia intermediária. A proposta generaliza um mecanismo que já está lá.

### A classificação é leitura nossa

Como `bloom_sugerido` e `exigencias`, a categoria **não é texto da BNCC** e precisa carregar a
marca — junto com o grupo do diagnóstico, que é a razão da classificação.

## 3. Fases

A ordem abaixo decorre de uma decisão: se são as categorias que tornam a expansão aceitável,
então **a Fase 3 é pré-requisito da Fase 2**, não trilha paralela. Acrescentar habilidades antes
do sistema de categorias existir entregaria exatamente a ambiguidade que se quer evitar.

### Fase 0 — formalização verificável em lista (pré-requisito de tudo)

`ExpressaoVerificavel` é singular: um `tipo`, uma `expressao`, um `resposta_esperada`. Quase toda
habilidade dos Grupos 1 e 2 tem mais de uma afirmação a verificar, e as questões multitema já têm
hoje. Sem isto, cada fase seguinte nasce parcialmente verificada.

- `Questao.verificaveis: list[ExpressaoVerificavel]`, com `BeforeValidator` que embrulha um objeto
  solto — questões já gravadas e saídas antigas do LLM continuam parseando.
- Veredicto por conjunção: um `rejeitado` rejeita; `nao_verificavel` parcial vira ressalva. A
  política do Orquestrador não muda.
- Dissertação: Seções 4.3.3 e 4.4.4.

### Fase 3 (antecipada) — o sistema de categorias

- `verificabilidade_esperada` e `grupo` por habilidade no catálogo, com a marca de leitura nossa.
- `garantia_obtida` derivada do veredicto, gravada no banco e exibida junto da questão.
- Interface: o rótulo aparece na questão gerada e no banco curado; filtro por garantia.
- Texto: a tabela da Seção 5 entra em 3.3.2 (resumida) e num **apêndice** (completa). É o artefato
  mais reaproveitável do trabalho — uma classificação das 45 habilidades de Matemática do EM por
  verificabilidade simbólica, com a razão de cada uma, que não existe na literatura.

**A partir daqui, acrescentar habilidade é honesto: cada uma entra com sua garantia declarada.**

### Fase 1 — verificação por propriedade

Um `tipo: "propriedade"` cujo `parametros` declara predicados a satisfazer, em vez de um gabarito
a comparar. Todos triviais em SymPy:

| Predicado | Verifica | Fecha |
|---|---|---|
| `reproduz_pontos` | `f(x_i) == y_i` para a tabela dada | 501, 502 |
| `grau` | `sp.degree(f) == n` | 501, 502 |
| `forma` | `f` casa com `a*x**2` (sem termo de 1º grau) | 502 |
| `coincide_com_sequencia` | `f(n) == a1 + (n-1)*r` nos primeiros termos | 507, 508 |

Ganho: quatro habilidades **já catalogadas** passam de "conferido em parte" a "gabarito
conferido", sem catálogo novo. Melhor retorno por linha de código do plano, e o argumento mais
forte para o Cap. 4 — a arquitetura verifica propriedade, não só resultado.

### Fase 2 — novos tipos de resposta computável

Cada item é um módulo em `verificacao/` + registro no dicionário + testes + `exigencias` no
catálogo + descrição do tipo no `prompts/gerador.md`.

| Ordem | Tipo | Habilidades novas | Observação |
|---|---|---|---|
| ~~2a~~ **feita** | extensão de `funcao`: log e trigonometria | 305, 306, 403, 404 | consultas `dominio`, `imagem`, `periodo`, `crescimento` |
| ~~2b~~ **feita** | `funcao` com `Piecewise` | 405 | tabela do IR, conta de luz |
| 2c | `sistema` | 301 | `linsolve`; `equacoes.py` já aceita várias incógnitas |
| 2d | `contagem` e `probabilidade` | 310, 311, 312, 511 | aritmética racional exata; `binomial`, `factorial` |
| 2e | `estatistica` | 316, 408, 409, 510 | tendência central, dispersão, frequências, reta de ajuste |
| 2f | `geometria_metrica` | 307, 308, 309, 504, 505, 506 | avaliação de expressões de área e volume |
| 2g | `grandeza` | 101, 103, 104, 313, 314 | numérico com unidade e algarismos significativos |
| 2h | sem tipo novo — entram como `sem conferência` | 102, 105, 407, 509, 512, 401/402 já estão | Grupo 3: nenhuma estratégia as alcança |

**2a e 2b primeiro** por uma razão que não é só técnica: fecham a unidade de funções, que é o
recorte declarado da dissertação, em vez de espalhar o sistema por sete famílias ao mesmo tempo.

## 3.1. O que o piloto 2a/2b ensinou

Executados como piloto, os dois primeiros blocos custaram **menos que uma sessão** e produziram
uma lição que vale para todos os blocos seguintes: **as rotinas do SymPy falham em silêncio, e o
modo de falha perigoso não é a exceção — é a resposta errada.**

Três casos concretos, todos encontrados antes de escrever o módulo:

- `function_range(2**x, x, Reals)` devolve `EmptySet`. Não é a imagem: é o SymPy desistindo. Uma
  implementação ingênua **reprovaria o gabarito correto** `(0, +∞)` e mandaria o Gerador
  "corrigir" o que estava certo. Curiosamente, `3*2**x` a mesma rotina resolve.
- `is_increasing(log(x), Reals, x)` devolve `False` — log é crescente *no seu domínio*, e avaliá-la
  sobre os reais reprova a resposta certa. Crescimento precisa ser avaliado sobre o domínio.
- `continuous_domain` levanta `NotImplementedError` para `Piecewise`.

Daí o princípio que ficou no módulo e vale para os blocos 2c–2g: **quando o CAS não conclui, o
veredicto é `nao_verificavel`, nunca `rejeitado`.** Errar para o lado de não conferir é
recuperável; reprovar o certo destrói a confiança do professor no verificador — e é uma forma de
erro silencioso pior que a original, porque vem com autoridade.

Corolário prático para quem for fazer 2c–2g: **teste as rotinas do SymPy contra casos conhecidos
antes de escrever o módulo.** O tempo gasto ali é menor que o de depurar um veredicto errado
depois.

## 4. Riscos e o que medir

- **O Gerador erra mais quanto mais tipos existirem.** Cada tipo é mais uma sintaxe que o LLM pode
  preencher errado, e o sintoma é `nao_verificavel` — que não reprova a questão, só a deixa passar
  sem conferência. **Instrumentado**: cada afirmação verificada guarda tipo, consulta e veredicto
  (`ResultadoVerificacao.afirmacoes`), e `sistema/analisar_logs.py` reporta a taxa por tipo a
  partir do log. Taxa alta denuncia tipo mal especificado no *prompt*, não habilidade difícil.
  **Ainda sem dados reais**: a suíte usa `LLMFake`, então a taxa só aparece depois de gerações
  com provedor de verdade. É a primeira medição a fazer antes de encarar 2c–2g.
- **A categoria pode virar álibi.** Se `sem conferência automática` for confortável demais, o
  Gerador aprende a não formalizar. Medir a distância entre `verificabilidade_esperada` e
  `garantia_obtida` é a defesa — e é justamente o dado do Cap. 6.
- **Com 40 habilidades o seletor plano fica inutilizável**: agrupar por unidade (o campo `unidade`
  já existe) e permitir filtrar por garantia.
- **Habilidade nova sem `exigencias`** faz o alinhamento curricular voltar a ser impressão do
  Crítico. O teste `test_toda_habilidade_tem_exigencias_e_bloom_sugerido` já barra isso; estender
  para exigir `verificabilidade_esperada` e `grupo`.
- **Dissertação**: 3.3.2 (recorte passa a ser classificado, não restrito), 4.4 (estratégias e
  veredicto graduado), Cap. 6 (cobertura por habilidade como métrica) e um apêndice novo.

## 5. Classificação das 45 habilidades

Legenda de garantia esperada: **C** = gabarito conferido · **P** = conferido em parte ·
**S** = sem conferência automática · **—** = fora de escopo.
Grupo: razão da classificação, conforme a Seção 1. `★` = já no catálogo.

| Código | Habilidade (resumo) | Grupo | Esp. |
|---|---|---|---|
| EM13MAT101 | Interpretar variação de duas grandezas por gráficos e taxas | 3 | P |
| EM13MAT102 | Analisar gráficos e amostragem divulgados na mídia | 3 | S |
| EM13MAT103 | Interpretar unidades de medida de diferentes grandezas | 1 | C |
| EM13MAT104 | Interpretar taxas e índices socioeconômicos | 1 | P |
| EM13MAT105 | Transformações isométricas para analisar produções humanas | 3 | S |
| EM13MAT201 | Propor ações comunitárias com cálculo de medidas | 4 | — |
| EM13MAT202 | Planejar e executar pesquisa amostral | 4 | — |
| EM13MAT203 | Criar aplicativos, jogos e planilhas | 4 | — |
| EM13MAT301 | Equações lineares simultâneas | 1 | C |
| EM13MAT302 ★ | Problemas modelados por funções de 1º e 2º graus | 1 | C |
| EM13MAT303 ★ | Porcentagens e juros compostos | 1 | C |
| EM13MAT304 ★ | Problemas com funções exponenciais | 1 | C |
| EM13MAT305 | Problemas com funções logarítmicas | 1 | C |
| EM13MAT306 | Fenômenos periódicos; funções seno e cosseno | 1 | C |
| EM13MAT307 | Métodos para obtenção de área de superfície | 1 | P |
| EM13MAT308 | Triângulos: relações métricas, congruência, semelhança | 1 | C |
| EM13MAT309 | Áreas totais e volumes de sólidos | 1 | C |
| EM13MAT310 | Problemas de contagem | 1 | C |
| EM13MAT311 | Probabilidade de eventos aleatórios | 1 | C |
| EM13MAT312 | Probabilidade em experimentos sucessivos | 1 | C |
| EM13MAT313 | Algarismos significativos e notação científica | 1 | C |
| EM13MAT314 | Grandezas compostas (velocidade, densidade) | 1 | C |
| EM13MAT315 | Reconhecer problema algorítmico e expressá-lo | 4 | — |
| EM13MAT316 | Tendência central e dispersão | 1 | C |
| EM13MAT401 ★ | Converter álgebra → gráfico (1º grau) | 3 | P |
| EM13MAT402 ★ | Converter álgebra → gráfico (2º grau) | 3 | P |
| EM13MAT403 | Comparar representações de exponencial e logarítmica | 3 | P |
| EM13MAT404 | Características de seno e cosseno | 3 | P |
| EM13MAT405 | Funções definidas por mais de uma sentença | 1 | P |
| EM13MAT406 | Linguagem de programação para implementar algoritmos | 4 | — |
| EM13MAT407 | Vistas ortogonais de figura espacial | 3 | S |
| EM13MAT408 | Construir e interpretar gráficos de frequências | 3 | P |
| EM13MAT409 | Comparar dados por histograma, box-plot, ramos e folhas | 3 | P |
| EM13MAT501 ★ | Padrões em tabela → função de 1º grau | 2 | C |
| EM13MAT502 ★ | Padrões em tabela → função de 2º grau (y = ax²) | 2 | C |
| EM13MAT503 ★ | Máximo e mínimo de funções quadráticas | 1 | C |
| EM13MAT504 | Volumes e princípio de Cavalieri | 1 | P |
| EM13MAT505 | Ladrilhamentos do plano | 2 | P |
| EM13MAT506 | Variação de área e perímetro de polígono regular | 1 | C |
| EM13MAT507 ★ | Associar PA a funções afins de domínio discreto | 2 | C |
| EM13MAT508 ★ | Associar PG a funções exponenciais de domínio discreto | 2 | C |
| EM13MAT509 | Deformação em projeções cartográficas | 3 | S |
| EM13MAT510 | Investigar duas variáveis; reta de ajuste | 3 | P |
| EM13MAT511 | Tipos de espaços amostrais | 1 | P |
| EM13MAT512 | Investigar propriedades por contraexemplos | 2 | P |

**Totais:** 21 C · 15 P · 4 S · 5 fora de escopo. Catálogo final: **40 habilidades**.

Observe onde estão as 10 atuais: 8 em C e 2 em P (401 e 402). Ou seja — o recorte de hoje já
contém habilidades que o núcleo simbólico não alcança por inteiro; a diferença é que passarão a
dizer isso.

## 6. Recomendação de primeira fatia

**Fase 0 + Fase 3 + Fase 1.** Nenhuma habilidade nova, e mesmo assim:

- toda questão passa a declarar que garantia carrega;
- 501, 502, 507 e 508 passam de conferidas em parte a conferidas;
- questões multitema deixam de ser conferidas pela metade;
- 401 e 402 param de aparentar uma garantia que não têm.

Concluída essa fatia, cada bloco da Fase 2 vira expansão de catálogo — acrescentar habilidade
deixa de ser decisão de arquitetura e vira trabalho rotineiro, com a garantia dita em vez de
suposta.
