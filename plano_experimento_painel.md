# Desenho do experimento — painel docente (Ciclo 3)

Protocolo para gerar o acervo de questões e coletar a avaliação dos professores que alimenta o
Capítulo 6. Escrito antes da coleta, de propósito: o plano de análise precisa estar fixado antes
de qualquer dado aparecer.

Referência: Seção 7 do projeto (`projeto_dissertacao_isabella.pdf`) e Seções 6.1–6.5 previstas em
`estrutura_dissertacao_isabella.pdf`. Onde este documento se afasta do projeto, diz-se
explicitamente e com justificativa.

## 1. As três perguntas que o experimento responde

**P1 — As questões servem?** Qualidade percebida pelos professores, por critério da rubrica
(Seção 3.4 da dissertação), e taxa de aceitação para uso real em sala.

**P2 — A verificação simbólica pega o que o professor não pega?** Esta é a pergunta que testa a
hipótese arquitetural (Seção 2.5). É a mais importante e a que o desenho do projeto, como está,
não responde.

**P3 — A garantia declarada significa alguma coisa?** As questões marcadas como *gabarito
conferido* são julgadas diferentemente das marcadas como *conferido em parte* ou *sem conferência
automática*? Se não houver diferença, o rótulo é decorativo — e é melhor saber disso.

## 2. Duas mudanças que proponho ao desenho do projeto

### 2.1 O desenho cego deveria ser interno, não contra banco humano

O projeto sugere embaralhar questões do sistema com itens de ENEM/OBMEP/livro didático. Tenho três
objeções.

É uma comparação **injusta e pouco informativa**: itens do ENEM passam por meses de edição
profissional e pré-testagem psicométrica. Perder para eles não diria nada sobre a arquitetura, e
empatar seria implausível a ponto de levantar suspeita sobre o instrumento.

É uma comparação **fora do alvo**. A tese desta dissertação não é "o sistema gera questões tão boas
quanto o ENEM". É que **a verificação simbólica intercepta um erro que o LLM sozinho produziria e o
professor não notaria**. Comparar com o ENEM não testa isso.

E há uma comparação melhor, **de graça**. Todo ciclo em que o Verificador reprovou a primeira
tentativa deixou registrado, no log, uma questão com erro matemático confirmado — com gabarito
errado, resolução fluente e localização exata do erro conhecida. São espécimes de *erro silencioso*
com padrão-ouro embutido, produzidos pelo mesmo gerador, no mesmo formato, sobre as mesmas
habilidades. Nenhum banco externo oferece controle experimental comparável.

**Proposta:** o desenho cego passa a contrastar **questões aprovadas pelo ciclo completo** contra
**questões que o Verificador reprovou** (correções não aplicadas), embaralhadas e sem identificação.
A pergunta ao professor não é "qual é melhor", e sim "esta questão tem erro matemático?".

Se a comparação com banco humano ainda interessar, ela cabe como estrato adicional pequeno
(6 itens) — mas como contexto, não como teste da hipótese.

### 2.2 Separar detectar erro de julgar qualidade

Escala Likert de 1 a 5 em "correção matemática" não mede detecção. Um professor que não percebeu o
erro marca 5 com sinceridade, e o dado fica indistinguível do de quem conferiu e aprovou. O projeto
lista "correção matemática" como critério 1 da rubrica; mantê-lo assim perde justamente P2.

**Proposta:** dois blocos com tarefas cognitivas distintas.

- **Bloco I — detecção**, cego: "esta questão tem erro matemático?" com resposta trinária
  (não / sim, aqui: ___ / não sei) e tempo por item registrado. Sem escala.
- **Bloco II — rubrica**: os cinco critérios restantes em Likert 1–5, mais a decisão de uso
  (aceita / aceita com ajuste / recusada) e comentário aberto.

O Bloco I vem primeiro, e o professor não sabe que há itens defeituosos na amostra — sabe apenas
que a amostra tem qualidade variável.

## 3. Fase A0 — teste de uso com convidados (Capítulo 7)

Dez convites, dez gerações incluídas em cada. **Não é parte do painel** e não responde P1, P2 nem
P3: cada convidado gera as próprias questões, então não há conjunto comum — e sem conjunto comum
não há concordância entre avaliadores. Quem especificou a questão e viu a trilha também não pode
avaliá-la às cegas.

Serve a outra coisa, que nenhuma outra fase alcança: **dado ecológico**. A estratificação da Fase A
é uma hipótese nossa de equilíbrio; o que os professores de fato pedem — quais habilidades, que
dificuldade, teórica ou aplicada — só se descobre deixando-os pedir. Se a demanda concentrar em
poucas habilidades, isso informa o recorte e vira resultado do Capítulo 7. E é o único jeito de
testar o produto em uso real: fluxo de convite, modo compartilhado, concorrência.

### Quem paga

Decisão que precisa ser tomada antes de qualquer link sair:

**(a) Cada convidado traz a própria chave.** É o teste de adoção honesto. A expectativa é que boa
parte trave aí — criar conta de API exige cartão, interface em inglês e entender o que é uma chave.
Se travarem, *isso é o resultado*: a chave é a barreira de adoção do produto educacional, e vale
mais do que as questões que seriam geradas.

**(b) O dono banca, com teto.** Ligar `chave_do_servidor` na configuração e definir
`cota_por_convite`. Dez convites × dez gerações ≈ 290 chamadas.

Até 2026-08-08 havia uma terceira possibilidade, indesejada: o convidado sem chave clicava em
Gerar, a requisição seguia sem credencial e o SDK caía na variável de ambiente do servidor. O dono
pagava, em silêncio e sem limite. Isso foi fechado — hoje o botão trava e a API recusa com 402 —,
mas registra-se aqui porque explica por que a decisão acima passou a ser explícita.

### Consentimento

Analisar o uso (que habilidades pediram, o que aceitaram) é pesquisa com pessoas: entra no mesmo
TCLE do painel.

## 4. Fase A — geração do acervo

### 4.1 Estratificação

**90 questões = 15 habilidades × 2 formatos × 3 dificuldades.**

Cobre as 15 habilidades do catálogo, o que sustenta as afirmações de alinhamento curricular, e
atende de uma vez o produto educacional (o projeto pede banco de 60–100 questões).

Dentro de cada célula:

- **Natureza** alterna teórica/aplicada, de modo que cada habilidade tenha 3 de cada.
- **Nível cognitivo** sorteado entre os `bloom_sugerido` da habilidade. Nível divergente fica
  **fora** deste acervo: é um fator interessante, mas confundiria a leitura da qualidade percebida.
  Vira sub-estudo separado, se houver fôlego.
- **Contexto e restrições** vazios, para não introduzir uma variável que o professor não vê.

Distribuição resultante por garantia esperada: 60 questões de habilidades `conferido` e 30 de
`conferido_em_parte` — proporção que já permite testar P3.

### 4.2 Procedimento

Gerar com o sistema **na versão corrigida** (posterior à medição de 2026-08-07), registrando no
cabeçalho do acervo: data, provedor, modelo e o SHA do commit. Sem isso o acervo não é reproduzível
e não serve como material de dissertação.

O log de ciclos guarda tudo — inclusive as tentativas reprovadas, que são o insumo do Bloco I.
`exportar_medicao.py` produz os `.md` legíveis e o índice.

**Custo estimado**, extrapolado da medição real: 4,5 min e 2,9 chamadas por ciclo → **cerca de 7
horas e 260 chamadas**. Dá para dividir em processos paralelos por habilidade; o Orquestrador é
sequencial dentro de um ciclo, mas ciclos são independentes.

### 4.3 Triagem obrigatória antes do painel

Dois filtros humanos, e nenhum é dispensável:

1. **Espécimes do Bloco I precisam ter o erro confirmado à mão.** A medição de 2026-08-07 mostrou
   que o Verificador produzia falsos negativos (domínio restrito pelo contexto). Isso foi corrigido,
   mas usar um espécime cujo "erro" não existe destruiria o padrão-ouro do bloco. Conferir a trilha
   de cada um, um por um.
2. **Revisão de conteúdo sensível ou impróprio** em todas as 90, pela orientação. Contexto gerado
   por LLM ocasionalmente traz situação inadequada para sala de aula, e isso não é papel do Crítico.

## 5. Fase B — composição do material do painel

Do acervo de 90, monta-se o material efetivamente avaliado:

| Bloco | Itens | Composição |
|---|---|---|
| I — detecção | 12 | 6 aprovadas pelo ciclo completo + 6 reprovadas pelo Verificador, embaralhadas |
| II — rubrica | 24 | estratificadas por unidade temática, formato, dificuldade e garantia obtida |

**36 itens por professor**, dentro da faixa de 30–50 do projeto.

Ponto de desenho que não pode ser negociado: **todos os professores avaliam exatamente os mesmos
36 itens**. Concordância entre avaliadores (Kendall's W, Krippendorff's α) exige avaliadores
completos sobre os mesmos itens; blocos incompletos rotativos inviabilizariam a estatística que o
projeto prevê.

Tempo estimado: ~15 min o Bloco I, ~45 min o Bloco II, ~10 min o questionário final. **Cerca de 70
minutos**, que é o limite do razoável para participação voluntária — e a razão de o acervo ser 90
mas o material ser 36.

## 6. Fase C — instrumento e procedimento

### 6.1 Bloco I (cego)

Por item: enunciado, alternativas quando houver, e o gabarito proposto. **Sem** a resolução — ela
denuncia o erro cedo demais e mudaria a tarefa.

> Esta questão apresenta algum erro matemático (no gabarito, na formulação ou nos dados)?
> ( ) Não  ( ) Sim — descreva onde: ______  ( ) Não sei dizer

Instrução honesta e suficiente: *"a amostra contém questões de qualidade variável"*. Não se revela a
proporção nem a origem.

### 6.2 Bloco II (rubrica)

Os cinco critérios em Likert 1–5 — clareza, adequação ao nível, alinhamento à habilidade BNCC
declarada, qualidade dos distratores (quando múltipla escolha), originalidade e relevância —, mais:

- **Decisão de uso**: aceita / aceita com ajuste / recusada. É o dado que separa "os agentes
  aprovaram" de "serve para a minha turma", e já é o contrato de `AvaliacaoProfessor` no sistema.
- **Comentário aberto**, opcional por item, obrigatório quando a decisão for *recusada*.

A habilidade BNCC declarada é exibida; a garantia obtida **não** é, em nenhum dos blocos. P3 se
testa comparando julgamentos entre estratos, não perguntando ao professor sobre o rótulo.

### 6.3 Questionário final

Perfil (tempo de docência, rede, familiaridade com IA), percepção geral sobre IA na elaboração de
questões, e disposição de uso. Aqui, e só aqui, revela-se que as questões foram geradas por IA com
verificação simbólica — antes disso, saber a origem enviesaria os dois blocos.

### 6.4 Plataforma

Duas opções, e a escolha tem consequência:

**Formulário externo** (Google Forms) com o material em PDF gerado por `listas.py`. Rápido, sem
desenvolvimento, funciona já.

**Dentro do próprio sistema**, o que teria a vantagem de exercitar o produto educacional e coletar
com o instrumento que ele já tem. **Mas exige desenvolvimento**: o banco filtra por dono
(`_FILTRO_DONO` em `banco.py`), de modo que hoje não há como vários professores avaliarem o mesmo
conjunto. Seria preciso um conjunto de avaliação compartilhado, somente leitura.

Recomendo o formulário externo para o Ciclo 3. O prazo da dissertação não é bom lugar para
estrear uma funcionalidade, e a coleta não pode falhar por bug.

## 7. Fase D — plano de análise (fixado antes da coleta)

**P1 — qualidade.** Média e desvio por critério; distribuição das decisões de uso; concordância
entre avaliadores por Kendall's W ou Krippendorff's α, conforme o projeto.

**P2 — detecção.** A medida central é a **taxa de detecção**: proporção de espécimes defeituosos em
que o professor apontou erro. O contraste com a taxa de falso alarme nas questões corretas separa
detecção de desconfiança generalizada. Comparação por McNemar ou Wilcoxon pareado dentro de cada
professor, como o projeto prevê para desenho cego.

Se a taxa de detecção for baixa, o erro silencioso deixa de ser premissa citada da literatura e
passa a ser resultado medido nesta dissertação, com professores brasileiros e questões de EM. É o
resultado mais forte que este trabalho pode produzir.

**P3 — garantia.** Comparação dos escores e das decisões de uso entre estratos de garantia obtida.
Hipótese nula explícita: não há diferença. Rejeitá-la sustenta o rótulo; não rejeitá-la é achado
igualmente publicável, e obriga a rever a Seção 4 da garantia declarada.

**Qualitativa.** Análise de conteúdo dos comentários com categorização emergente, e cruzamento
entre as categorias e os critérios de nota baixa.

## 8. Decisões pendentes e riscos

- **CEP.** O projeto deixa em aberto se o PROFMAT/UFMT exige submissão ao Comitê de Ética. Isso
  **bloqueia a coleta, não a geração**: a Fase A pode começar hoje. Confirmar antes da Fase C.
- **O Bloco I mostra questões erradas a professores** de propósito. É defensável e comum em estudos
  de detecção, mas precisa constar do TCLE e ser explicado no debriefing, junto com a lista de quais
  itens eram defeituosos e por quê.
- **Recrutamento é o gargalo real.** 8–15 professores com 70 minutos disponíveis é mais difícil que
  qualquer parte técnica deste plano. Começar o recrutamento em paralelo à Fase A.
- **Reaproveitamento parcial da medição de 2026-08-07.** Das 17 questões, 4 foram moldadas por
  uma reprovação **falsa** do Verificador (o defeito do domínio restrito, já corrigido): o Gerador
  foi informado de que um domínio correto estava errado e o "corrigiu" para o maximal. Nas
  `EM13MAT507` isso é especialmente ruim, porque a habilidade é sobre domínio discreto. Não usar
  sem reinspecionar.
- **Risco de piso.** Se a taxa de aprovação continuar em 17/17, as notas podem saturar no teto e a
  variância some, inutilizando a concordância. Mitigação: manter no Bloco II ao menos 6 itens de
  habilidades `conferido_em_parte` e as três dificuldades, para garantir dispersão.

## 9. Sequência recomendada

1. Confirmar exigência de CEP e iniciar recrutamento. *(paralelo, começa já)*
1b. Fase A0: distribuir os convites e observar o uso. Vem **antes** da Fase A: encontra bugs
   de aplicativo que teste nenhum pega, e o que os convidados pedirem informa a
   estratificação antes de gastar sete horas de geração.
2. Gerar as 90 questões com a versão corrigida, registrando modelo e SHA. *(~7 h de máquina)*
3. Triagem: confirmar espécimes do Bloco I à mão; revisar as 90 quanto a conteúdo.
4. Compor os 36 itens e montar o instrumento.
5. **Piloto com 1 ou 2 professores** — mede o tempo real e revela itens ambíguos antes de queimar a
   amostra. Não pular. O material do piloto **já existe**: das 17 questões da medição de
   2026-08-07, 10 foram aprovadas na primeira iteração sem qualquer feedback falso, e há 2
   espécimes de erro confirmáveis. Não servem ao painel — cobrem só 9 das 15 habilidades e têm
   dificuldade sempre média —, mas bastam para rodar o instrumento de ponta a ponta sem gastar
   nada.
6. Coleta, análise conforme a Seção 7, redação de 6.6 e 6.7.

Redigir 6.1 a 6.5 a partir deste documento **antes** da coleta, como o cabeçalho de
`cap6_avaliacao.tex` já prevê.
