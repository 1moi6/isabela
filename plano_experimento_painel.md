# Desenho da avaliação — duas rodadas

Protocolo para colocar as questões geradas diante de professores. Escrito antes da coleta, de
propósito: o plano de análise precisa estar fixado antes de qualquer dado aparecer.

Referência: Seção 7 do projeto (`projeto_dissertacao_isabella.pdf`) e Seções 6.1–6.5 previstas em
`estrutura_dissertacao_isabella.pdf`. Onde este documento se afasta do projeto, diz-se
explicitamente e com justificativa.

## 0. Duas rodadas, e por quê

| | **Rodada 1 — protótipo** | **Rodada 2 — painel formal** |
|---|---|---|
| Quando | agora | depois, se houver prazo |
| Participantes | 5 professores | 8 a 15 |
| Ética | sem CEP; participação informada | submissão ao CEP |
| Detecção de erro | **transparente** | cega |
| Estatística | descritiva e qualitativa | concordância entre avaliadores |
| Destino | **Capítulo 7** (produto) | **Capítulo 6** (avaliação) e artigo |

A separação decorre de duas restrições que se reforçam.

**Ética precede coleta.** Aprovação de comitê em geral não é retroativa. Dados colhidos agora, sem
CEP, provavelmente **não poderão ser reaproveitados** num artigo submetido depois — a Rodada 2 é
coleta nova, não ampliação desta. Isso não é perda: libera a Rodada 1 para ser leve, rápida e
francamente exploratória.

**Cinco pessoas não sustentam a estatística prevista.** Kendall's W ou Krippendorff's α com n=5 não
produzem estimativa utilizável. A Rodada 1 relata decisões e razões, não médias.

> **Risco a decidir, não a adiar:** o objetivo 6 do projeto é avaliar a qualidade das questões por
> painel docente com instrumento estruturado. A Rodada 1 **não** cumpre isso. Se a Rodada 2 não
> couber no prazo, ou o Capítulo 6 assume a Rodada 1 como avaliação formativa preliminar e declara
> o painel como limitação explícita, ou o objetivo fica descumprido. Melhor escolher agora.

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

## 3. Rodada 1 — protótipo com 5 professores (sem CEP)

Cada participante passa por dois momentos, na mesma sessão, com ~30 minutos cada.

### 3.1 Momento A — uso livre do aplicativo

A pessoa recebe um convite e gera as próprias questões, escolhendo a especificação que quiser.

O que se colhe: **o que os professores de fato pedem** — quais habilidades, que dificuldade,
teórica ou aplicada — e onde eles travam. A estratificação da Rodada 2 é uma hipótese nossa de
equilíbrio; só o uso livre mostra se ela corresponde à demanda. É também o único jeito de testar o
produto em operação: fluxo de convite, modo compartilhado, dois ou três gerando ao mesmo tempo.

**Quem paga.** Ou cada um traz a própria chave de API — e o quanto disso trava é, em si, o
resultado sobre a barreira de adoção do produto —, ou o dono liga `chave_do_servidor` com
`cota_por_convite`. Cinco convites × dez gerações ≈ 145 chamadas. Decidir antes de mandar o
primeiro link.

### 3.2 Momento B — avaliação de um conjunto comum

Todos avaliam **os mesmos 12 a 15 itens**, e aqui a detecção é **transparente**:

> "Esta amostra contém questões com erro matemático. Aponte quais e onde."

Sem CEP, não se retém informação de ninguém: o participante sabe exatamente o que está fazendo.
Não se informa a proporção — dizer "cinco das quinze" transformaria a tarefa em escolha forçada,
e omitir uma contagem não é reter informação sobre a natureza do estudo.

O que se perde: a estimativa ecológica. Um professor avisado está caçando, então a taxa de detecção
aqui **não** responde "ele notaria no uso normal" — essa pergunta fica para a Rodada 2, cega.

O que se ganha, e é bastante: **quais erros escapam mesmo de quem está procurando**. Se um
professor atento deixa passar um gabarito de PG com o primeiro termo omitido, isso é evidência
forte do erro silencioso — e mais defensável que a versão cega, porque não depende de nenhuma
omissão.

### 3.3 Instrumento da Rodada 1

Por item, nesta ordem:

1. **Tem erro matemático?** não / sim, aqui: ___ / não sei dizer
2. **Decisão de uso:** aceita / aceita com ajuste / recusada
3. **Por quê?** — obrigatório quando a decisão não for "aceita"

A escala Likert dos seis critérios **fica de fora desta rodada**. Com cinco pessoas, médias por
critério são ruído; a decisão de uso e a justificativa são sinal, e é delas que sai o que ajustar
no sistema. Quem quiser continuidade com a rubrica da Seção 3.4 pode acrescentá-la, ao custo de
dobrar o tempo de sessão.

Ao final, três perguntas curtas: usaria isto no seu planejamento? o que faltou? o que atrapalhou?

### 3.4 Material da Rodada 1

12 a 15 itens, dos quais 4 ou 5 com erro matemático confirmado.

O acervo atual não basta: das 17 questões da medição de 2026-08-07, 10 estão limpas mas há apenas
2 espécimes de erro aproveitáveis. Espécimes aparecem em cerca de um quarto dos ciclos (é a taxa
observada de reprovação legítima na primeira iteração), então **uma geração enxuta de ~24 questões**
rende os 5 espécimes necessários e sobra material limpo. Custo estimado: **~2 horas e ~70
chamadas** — bem abaixo das 7 horas do acervo completo.

**Triagem obrigatória:** conferir cada espécime à mão antes de usá-lo. A medição de 2026-08-07
mostrou que o Verificador produzia falsos negativos (domínio restrito pelo contexto); está
corrigido, mas um espécime cujo "erro" não existe destruiria a tarefa inteira. Descartar também as
4 questões daquela medição que foram moldadas por reprovação falsa.

### 3.5 Cuidados sem CEP

Não há comitê, o que aumenta e não diminui a responsabilidade:

- participação voluntária, com o propósito dito antes de começar;
- respostas anonimizadas no relato — professor 1 a 5, sem escola nem nome;
- deixar claro que se avalia o **sistema**, não o participante;
- ao final, mostrar quais itens tinham erro e qual era, para quem quiser saber;
- não publicar dado individual identificável, nem em anexo.

Se algum dia esses dados forem para artigo, é preciso recoletar sob CEP.

## 4. Rodada 2 — Fase A: geração do acervo

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

## 5. Rodada 2 — Fase B: composição do material

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

## 6. Rodada 2 — Fase C: instrumento e procedimento

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

## 7. Rodada 2 — Fase D: plano de análise (fixado antes da coleta)

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

- **A que capítulo a Rodada 1 serve.** Assumido aqui: Capítulo 7. Se o Capítulo 6 for depender
  dela, precisa declarar-se explicitamente como avaliação formativa preliminar, com o painel
  formal listado como limitação. Decidir antes de redigir, não depois.
- **CEP para a Rodada 2.** O projeto deixou em aberto se o PROFMAT/UFMT exige submissão. Vale
  perguntar cedo: análise leva semanas ou meses, e o Ciclo 3 está previsto para os meses 8–10.
  Ao perguntar, mencionar que o instrumento **não revela previamente ao participante que há itens
  defeituosos** — é esse detalhe que muda a resposta, e é melhor apresentá-lo do que ser
  questionado depois.
- **Dados da Rodada 1 provavelmente não migram** para um artigo sob CEP. Planejar recoleta.
- **Recrutamento é o gargalo real**, nas duas rodadas. Mais difícil que qualquer parte técnica
  deste plano.
- **Reaproveitamento parcial da medição de 2026-08-07.** Das 17 questões, 4 foram moldadas por uma
  reprovação **falsa** do Verificador (o defeito do domínio restrito, já corrigido): o Gerador foi
  informado de que um domínio correto estava errado e o "corrigiu" para o maximal. Nas
  `EM13MAT507` isso é especialmente ruim, porque a habilidade é sobre domínio discreto. Não usar
  sem reinspecionar.
- **Risco de piso na Rodada 2.** Se a taxa de aprovação continuar alta, as notas saturam no teto,
  a variância some e a concordância fica inutilizável. Mitigação: manter no Bloco II ao menos 6
  itens de habilidades `conferido_em_parte` e as três dificuldades.
- **O acervo de 60–100 questões é entregável do produto**, independente das duas rodadas. Não
  depende de ética nem de recrutamento: pode rodar quando convier.

## 9. Sequência recomendada

**Agora (Rodada 1):**

1. Decidir quem paga as gerações dos convidados e configurar (`chave_do_servidor`, `cota_por_convite`).
2. Geração enxuta de ~24 questões. *(~2 h de máquina)*
3. Triar espécimes à mão e montar o conjunto comum de 12 a 15 itens.
4. Sessão com 1 professor como ensaio — mede o tempo real e revela item ambíguo antes de queimar
   os outros 4. Com n=5, perder um participante por instrumento mal calibrado é 20 % da amostra.
5. As 4 sessões restantes; relato descritivo e qualitativo.

**Em paralelo, sem depender de nada:**

6. Gerar o acervo de 90 questões do produto educacional. *(~7 h de máquina)*
7. Perguntar sobre CEP e começar recrutamento da Rodada 2.

**Depois, se houver prazo (Rodada 2):** Fases A a D como descritas, e redação de 6.1–6.5 antes da
coleta, como o cabeçalho de `cap6_avaliacao.tex` já prevê.
