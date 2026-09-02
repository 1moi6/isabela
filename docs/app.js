/* =============================================================================
   Gerador de questões — lógica da interface.

   Sem framework e sem passo de compilação: o arquivo roda como está. Todo texto
   vindo do modelo entra na página por textContent, nunca por innerHTML — o
   enunciado é conteúdo gerado, e conteúdo gerado não vira marcação. Quem lê o
   Markdown-com-matemática do Gerador e monta os nós é `marcacao.js`, e ele
   também só cria elementos e preenche textContent: a estrutura vem da leitura
   do texto, nunca de marcação embutida nele.
   ========================================================================== */

const estadoApp = {
  opcoes: null,
  gerados: [],      // ciclos desta sessão, ainda não necessariamente salvos
  banco: [],
  selecionadas: new Set(),
  compartilhado: false,
};


/** Aceita convite e endereço do backend pela URL, e limpa a barra de endereço. */
function capturarConvite() {
  const url = new URL(window.location.href);
  const codigo = url.searchParams.get("convite");
  const api = url.searchParams.get("api");
  if (!codigo && !api) return;
  if (codigo) guardado.convite = codigo;
  if (api) guardado.api = api.replace(/\/+$/, "");
  url.searchParams.delete("convite");
  url.searchParams.delete("api");
  window.history.replaceState({}, "", url.pathname + url.search);
}

/* ------------------------------------------------------------- utilitários */
const rotulo = (lista, valor) => (lista.find((o) => o.valor === valor) || {}).rotulo || valor;

/** Assinatura de quem mantém o servidor, para quem chega por um link. */
function blocoResponsavel(ident) {
  if (!ident || !ident.responsavel) return null;
  const bloco = el("div", "responsavel");
  bloco.append(el("span", "responsavel__rotulo", "Servidor mantido por"));
  bloco.append(el("span", "responsavel__nome", ident.responsavel));
  if (ident.instituicao) bloco.append(el("span", "responsavel__linha", ident.instituicao));
  if (ident.contato) bloco.append(el("span", "responsavel__linha", ident.contato));
  return bloco;
}

/** Tela de acesso: aparece quando o convite falta ou não vale mais. */
async function mostrarBloqueio() {
  if (document.getElementById("bloqueio")) return;
  const capa = el("div", "bloqueio");
  capa.id = "bloqueio";
  const caixa = el("div", "bloqueio__caixa");
  caixa.append(el("h2", "bloqueio__titulo", "Acesso por convite"));
  caixa.append(el("p", "bloqueio__texto",
    guardado.convite
      ? "Este convite não vale mais. Peça um link novo a quem administra o sistema."
      : "Este endereço é de uso restrito. Abra o link de convite que você recebeu — "
        + "ele identifica você e dá acesso ao seu banco de questões. "
        + "Se ainda não tem um, peça a quem administra o sistema."));
  capa.append(caixa);
  document.body.append(capa);

  // A identificação é pública justamente para aparecer aqui, antes do acesso.
  try {
    const ident = await (await fetch(guardado.api + "/api/identificacao")).json();
    const bloco = blocoResponsavel(ident);
    if (bloco) caixa.append(bloco);
    estadoApp.identificacao = ident;
  } catch (_) { /* sem identificação configurada, a tela segue útil */ }
}

/* ------------------------------------------------------------------ estado */
async function carregarEstado() {
  const dados = await (await api("/api/estado")).json();
  estadoApp.compartilhado = dados.compartilhado;

  document.getElementById("estado-banco").textContent =
    `${dados.total_no_banco} no banco`;
  document.getElementById("estado-provedor").textContent =
    dados.nome || (dados.modelo ? `${dados.provedor} · ${dados.modelo}` : dados.provedor);

  /* Sem chave, o botão precisa PARAR de funcionar. Antes isto era só um aviso
     em texto: quem clicasse mesmo assim tinha a geração paga pela chave de quem
     mantém o servidor, em silêncio. */
  const aviso = document.getElementById("aviso-chave");
  // O teto de questões do convite vale com qualquer chave, então trava o botão
  // antes da conversa sobre chave: quem esgotou não resolve trazendo a própria.
  const semQuestoes = dados.questoes_restantes === 0;
  const podeGerar = !semQuestoes && (dados.chave_presente || dados.provedor === "ollama");
  if (semQuestoes) {
    aviso.textContent =
      `Este convite já gerou as ${dados.limite_de_geracoes} questões combinadas. ` +
      "Peça mais a quem administra o sistema.";
    aviso.hidden = false;
  } else if (!podeGerar) {
    aviso.textContent = dados.compartilhado
      ? "Informe a sua chave de API em Configurações para gerar questões."
      : `Sem chave de API. Informe em Configurações ou defina ${dados.variavel_chave} no ambiente.`;
    aviso.hidden = false;
  } else if (dados.questoes_restantes !== null && dados.questoes_restantes !== undefined) {
    const n = dados.questoes_restantes;
    aviso.textContent = `Restam ${n} questão(ões) neste convite, de ${dados.limite_de_geracoes} combinadas.`;
    aviso.hidden = false;
  } else if (dados.servidor_banca && dados.geracoes_restantes !== null) {
    aviso.textContent =
      `Você tem ${dados.geracoes_restantes} geração(ões) incluída(s) neste convite. ` +
      "Depois disso, informe a sua própria chave de API em Configurações.";
    aviso.hidden = false;
  } else {
    aviso.hidden = true;
  }
  document.getElementById("botao-gerar").disabled = !podeGerar;

  // Preferências do servidor só são editáveis na máquina onde ele roda. Provedor
  // e modelo NÃO estão entre elas: são de quem usa, viajam por requisição, e
  // ficam fora deste bloco justamente para continuarem editáveis por convidado.
  document.getElementById("config-servidor").hidden = dados.compartilhado;
  document.getElementById("config-pasta").value = dados.pasta_sincronizada || "";
  estadoApp.provedorDoServidor = dados.provedor;
  document.getElementById("config-provedor").value = guardado.provedor || dados.provedor;
  document.getElementById("config-modelo").value = guardado.modelo || dados.modelo || "";
  atualizarSugestoesDeModelo();

  await mostrarIdentificacao();

  if (!dados.compartilhado && dados.pasta_sincronizada && !dados.pasta_acessivel) {
    avisar(`A pasta sincronizada '${dados.pasta_sincronizada}' não foi encontrada.`, "erro");
  }
  return dados;
}

/** Mostra quem mantém o servidor: no rodapé do cabeçalho e junto do campo de chave. */
async function mostrarIdentificacao() {
  let ident = estadoApp.identificacao;
  if (!ident) {
    try {
      ident = await (await fetch(guardado.api + "/api/identificacao")).json();
      estadoApp.identificacao = ident;
    } catch (_) { return; }
  }

  document.getElementById("config-responsavel").value = ident.responsavel || "";
  document.getElementById("config-instituicao").value = ident.instituicao || "";
  document.getElementById("config-contato").value = ident.contato || "";

  const assinatura = [ident.responsavel, ident.instituicao].filter(Boolean).join(" · ");
  document.getElementById("marca-responsavel").textContent = assinatura;

  const junto = document.getElementById("chave-responsavel");
  junto.replaceChildren();
  const bloco = blocoResponsavel(ident);
  if (bloco) junto.append(bloco);
}

/* ---------------------------------------------------------------- formulário */
function preencherSelect(elemento, itens, valorDe = (i) => i.valor, textoDe = (i) => i.rotulo) {
  elemento.replaceChildren();
  for (const item of itens) {
    const opcao = el("option", null, textoDe(item));
    opcao.value = valorDe(item);
    elemento.append(opcao);
  }
}

function grupoOpcoes(container, itens, valorInicial) {
  container.replaceChildren();
  container.dataset.valor = valorInicial;
  for (const item of itens) {
    const botao = el("button", "opcoes__item", item.rotulo);
    botao.type = "button";
    botao.dataset.valor = item.valor;
    if (item.valor === valorInicial) botao.classList.add("opcoes__item--ativo");
    botao.addEventListener("click", () => {
      container.dataset.valor = item.valor;
      for (const irmao of container.children) {
        irmao.classList.toggle("opcoes__item--ativo", irmao === botao);
      }
    });
    container.append(botao);
  }
}

function habilidadeEscolhida() {
  const codigo = document.getElementById("campo-habilidade").value;
  return estadoApp.opcoes.habilidades.find((h) => h.codigo === codigo);
}

/* A habilidade manda: são os temas dela que aparecem, e é a relação declarada
   no catálogo que decide se dá para escolher entre eles.
     - "conjuntiva": a habilidade É a articulação dos dois (EM13MAT507 associa PA
       a função afim). Desmarcar um descaracteriza a habilidade, então ficam
       marcados e travados.
     - "enumerativa": a habilidade cobre mais de um tema mas não exige combiná-los
       (EM13MAT302). Livre; marcar os dois pede um problema que os articule.
     - "unica": não há o que escolher. */
function atualizarTemas() {
  const habilidade = habilidadeEscolhida();
  const container = document.getElementById("campo-temas");
  const ajuda = document.getElementById("ajuda-temas");
  container.replaceChildren();
  if (!habilidade) return;

  // Sem `relacao_temas` (API desatualizada), não dá para saber se os temas se
  // combinam: deixa escolher em vez de travar o que talvez fosse livre.
  const travado = habilidade.relacao_temas
    ? habilidade.relacao_temas !== "enumerativa"
    : false;
  for (const tema of habilidade.temas) {
    const item = el("label", "temas__item");
    const caixa = document.createElement("input");
    caixa.type = "checkbox";
    caixa.value = tema;
    caixa.checked = travado || tema === habilidade.temas[0];
    caixa.disabled = travado;
    caixa.addEventListener("change", garantirUmTema);
    item.append(caixa, el("span", null, rotulo(estadoApp.opcoes.temas, tema)));
    container.append(item);
  }

  if (habilidade.relacao_temas === "conjuntiva") {
    ajuda.textContent =
      "Esta habilidade é a articulação entre os dois temas: a questão precisa tratar dos dois.";
  } else if (habilidade.relacao_temas === "enumerativa") {
    ajuda.textContent =
      "Marque os dois para pedir uma questão que os articule num mesmo problema.";
  } else {
    ajuda.textContent = "";
  }
}

/** Desmarcar o último tema deixaria o pedido sem tema nenhum; remarca na hora. */
function garantirUmTema(evento) {
  if (temasEscolhidos().length === 0) evento.target.checked = true;
  atualizarSugestoesDeContexto();
}

function temasEscolhidos() {
  return [...document.querySelectorAll("#campo-temas input:checked")].map((c) => c.value);
}

/* O nível de Bloom pedido pode destoar dos verbos da habilidade — "lembrar"
   numa habilidade cujo verbo é "resolver e elaborar". Não é proibido: o
   professor pode ter suas razões. Mas é avisado, e a divergência vai para o
   registro do ciclo. */
function avisarSobreBloom() {
  const habilidade = habilidadeEscolhida();
  const nivel = document.getElementById("campo-bloom").value;
  const aviso = document.getElementById("aviso-bloom");
  if (!habilidade || !habilidade.bloom_sugerido || habilidade.bloom_sugerido.includes(nivel)) {
    aviso.textContent = "";
    return;
  }
  const sugeridos = habilidade.bloom_sugerido
    .map((b) => rotulo(estadoApp.opcoes.bloom, b))
    .join(" ou ");
  aviso.textContent =
    `Os verbos de ${habilidade.codigo} sugerem ${sugeridos}. ` +
    "Dá para pedir assim mesmo, mas a questão tende a exigir mais revisões.";
}

/* Sem indicação, o Gerador volta sempre ao contexto mais provável de cada tema:
   no acervo de 8 de agosto, 7 das 9 questões de função afim eram tarifa fixa mais
   valor por unidade, e todas as de PG eram cultura de bactérias. O Crítico não
   pega isso — avalia uma questão por vez e não enxerga a repetição entre elas.
   Sugerir contextos é o que sobra para quebrar o padrão. */
function atualizarSugestoesDeContexto() {
  const lista = document.getElementById("sugestoes-contexto");
  const ajuda = document.getElementById("ajuda-contexto");
  const contextos = estadoApp.opcoes.contextos || [];
  const escolhidos = temasEscolhidos();
  lista.replaceChildren();
  if (!contextos.length) { ajuda.textContent = ""; return; }

  const servem = contextos.filter(
    (c) => !c.temas.length || c.temas.some((t) => escolhidos.includes(t)),
  );
  for (const c of servem) {
    const opcao = document.createElement("option");
    opcao.value = c.nome;
    lista.append(opcao);
  }
  ajuda.textContent = servem.length
    ? `${servem.length} sugestões para este tema. Em branco, o gerador escolhe — e tende a repetir o mesmo contexto.`
    : "";
  document.getElementById("sortear-contexto").disabled = !servem.length;
  // Só os nomes: o sorteio escreve direto no campo de texto.
  estadoApp.contextosDoTema = servem.map((c) => c.nome);
}

/* No aplicativo não há lote: o professor gera uma questão por vez, e não há
   como distribuir contextos sem repetir ao longo da sessão. O que dá para
   oferecer é o sorteio — e, de vez em quando, um par, que amplia bastante o
   espaço quando as duas coisas conversam. */
function sortearContexto() {
  const servem = estadoApp.contextosDoTema || [];
  if (!servem.length) return;
  const campo = document.getElementById("form-gerar").contexto;
  const primeiro = servem[Math.floor(Math.random() * servem.length)];

  // Um terço em par: contexto forçado é pior que contexto comum, e o Gerador
  // tem instrução de usar só o primeiro quando a combinação não fecha.
  const querPar = servem.length > 1 && Math.random() < 1 / 3;
  if (!querPar) { campo.value = primeiro; return; }
  const outros = servem.filter((c) => c !== primeiro);
  campo.value = `${primeiro} + ${outros[Math.floor(Math.random() * outros.length)]}`;
}

function mostrarDescricaoHabilidade() {
  const habilidade = habilidadeEscolhida();
  document.getElementById("descricao-habilidade").textContent = habilidade ? habilidade.descricao : "";
  atualizarTemas();
  avisarSobreBloom();
  atualizarSugestoesDeContexto();
}

/* A interface é publicada pelo GitHub Pages a cada push; a API só muda quando
   alguém reinicia o servidor. O descompasso é normal e vai acontecer de novo — o
   que não pode acontecer é a página degradar calada, mostrando meia dúzia de
   habilidades como se fossem todas. `garantias` só existe a partir da versão que
   declara a conferência, e serve de marcador de versão. */
function conferirVersaoDaApi() {
  const aviso = document.getElementById("aviso-versao");
  const desatualizada = !estadoApp.opcoes.garantias;
  aviso.textContent = desatualizada
    ? "O servidor desta API está desatualizado: algumas habilidades da BNCC e a " +
      "indicação de conferência do gabarito não aparecem aqui. Peça a quem o " +
      "mantém para atualizá-lo."
    : "";
  aviso.hidden = !desatualizada;
}

async function montarFormulario() {
  const o = estadoApp.opcoes;
  conferirVersaoDaApi();
  // A habilidade vem primeiro e não é mais filtrada por tema: é ela que define
  // quais temas ficam disponíveis.
  preencherSelect(
    document.getElementById("campo-habilidade"), o.habilidades, (h) => h.codigo, (h) => h.codigo
  );
  preencherSelect(document.getElementById("campo-bloom"), o.bloom);
  document.getElementById("campo-bloom").value = "aplicar";
  grupoOpcoes(document.getElementById("campo-dificuldade"), o.dificuldades, "media");
  grupoOpcoes(document.getElementById("campo-natureza"), o.naturezas, "aplicada");
  grupoOpcoes(document.getElementById("campo-formato"), o.formatos, "discursiva");
  mostrarDescricaoHabilidade();

  preencherSelect(document.getElementById("filtro-tema"), [{ valor: "", rotulo: "Todos" }, ...o.temas]);
  preencherSelect(
    document.getElementById("filtro-dificuldade"),
    [{ valor: "", rotulo: "Todas" }, ...o.dificuldades]
  );
  if (o.garantias) {
    preencherSelect(
      document.getElementById("filtro-garantia"),
      [{ valor: "", rotulo: "Todas" }, ...o.garantias]
    );
  }
  if (o.provedores) {
    preencherSelect(document.getElementById("config-provedor"), o.provedores);
    document.getElementById("config-provedor").value =
      guardado.provedor || estadoApp.provedorDoServidor || "anthropic";
  }
  atualizarSugestoesDeModelo();
}

/* O modelo pertence ao provedor: 'claude-sonnet-5' não significa nada para o
   Gemini. Trocar de provedor sem trocar o modelo era o jeito mais fácil de
   receber um erro do serviço sem entender por quê — daí a lista mudar junto e o
   campo se limpar quando o modelo guardado é de outra família. */
function atualizarSugestoesDeModelo() {
  const provedor = document.getElementById("config-provedor").value;
  const lista = document.getElementById("sugestoes-modelo");
  const ajuda = document.getElementById("ajuda-modelo");
  const campo = document.getElementById("config-modelo");
  const dados = (estadoApp.opcoes.provedores || []).find((p) => p.valor === provedor);
  const modelos = (dados && dados.modelos) || [];

  lista.replaceChildren();
  for (const nome of modelos) {
    const opcao = document.createElement("option");
    opcao.value = nome;
    lista.append(opcao);
  }
  if (campo.value && modelos.length && !modelos.includes(campo.value)) campo.value = "";
  ajuda.textContent = modelos.length
    ? `Em branco usa ${modelos[0]}. Qualquer outro nome aceito pelo provedor também serve.`
    : "Em branco usa o modelo padrão do provedor.";
}

function lerEspecificacao() {
  const form = document.getElementById("form-gerar");
  return {
    habilidade_bncc: document.getElementById("campo-habilidade").value,
    temas: temasEscolhidos(),
    // `tema` no singular vai junto para que esta página funcione também com uma
    // API ainda não atualizada. A versão nova ignora este campo quando há `temas`.
    tema: temasEscolhidos()[0],
    nivel_bloom: document.getElementById("campo-bloom").value,
    dificuldade: document.getElementById("campo-dificuldade").dataset.valor,
    natureza: document.getElementById("campo-natureza").dataset.valor,
    formato: document.getElementById("campo-formato").dataset.valor,
    contexto: form.contexto.value.trim() || null,
    restricoes: form.restricoes.value.trim() || null,
  };
}

/* ------------------------------------------------- trilha do ciclo (assinatura) */
function etapa(agente, veredicto, detalhe, estilo) {
  const item = el("li", `trilha__etapa trilha__etapa--${estilo}`);
  item.append(el("span", "trilha__agente", agente));
  item.append(el("span", "trilha__veredicto", veredicto));
  if (detalhe) item.append(el("span", "trilha__detalhe", detalhe));
  return item;
}

const VEREDICTO = {
  aprovado: ["conferiu o gabarito", "ok"],
  rejeitado: ["reprovou o gabarito", "erro"],
  nao_verificavel: ["não formalizável", "neutro"],
  aprovado_ressalva_numerica: ["conferiu por amostragem", "ok"],
  aprovado_parcial: ["conferiu em parte", "parcial"],
};

/* A garantia é o que o professor precisa ler de relance: diz o que ESTA questão
   recebeu de conferência, não o que a habilidade dela admitiria. Sem conferência
   automática vira aviso, não etiqueta neutra — é pedido de revisão. */
/* Espelha `garantia_de` em modelos.py — a questão recém-gerada ainda não passou
   pelo banco, então o rótulo é derivado aqui a partir do veredicto. */
const GARANTIA_POR_VEREDICTO = {
  aprovado: "conferido",
  aprovado_ressalva_numerica: "conferido_em_parte",
  aprovado_parcial: "conferido_em_parte",
  nao_verificavel: "sem_conferencia",
  rejeitado: "sem_conferencia",
};

const ESTILO_GARANTIA = {
  conferido: "ok",
  conferido_em_parte: "parcial",
  sem_conferencia: "erro",
};

function etiquetaDeGarantia(garantia) {
  if (!garantia) return null;
  const estilo = ESTILO_GARANTIA[garantia] || "neutra";
  return el("span", `etiqueta etiqueta--${estilo}`, rotulo(estadoApp.opcoes.garantias, garantia));
}

function montarTrilha(iteracao) {
  const trilha = el("ol", "trilha");
  trilha.append(etapa("Gerador", "questão redigida", null, "neutro"));

  const v = iteracao.verificacao;
  const [texto, estilo] = VEREDICTO[v.veredicto] || [v.veredicto, "neutro"];
  const detalhe = v.resultado_calculado
    ? `recalculou: ${v.resultado_calculado}`
    : v.justificativa;
  trilha.append(etapa("Verificador simbólico", texto, detalhe, estilo));

  const p = iteracao.parecer;
  if (!p) {
    trilha.append(etapa("Crítico didático", "não chegou a avaliar", null, "neutro"));
  } else {
    const notas = p.notas.map((n) => n.nota);
    const minima = notas.length ? Math.min(...notas) : 0;
    trilha.append(etapa(
      "Crítico didático",
      p.aprovado ? "aprovou" : "pediu revisão",
      `nota mínima ${minima}/5 em ${p.notas.length} critérios`,
      p.aprovado ? "ok" : "erro"
    ));
  }
  return trilha;
}

/** Trilha durante a execução, refletindo o que o servidor informa de progresso. */
function trilhaEmAndamento(progresso) {
  const p = progresso || { iteracao: 1, etapa: "gerando" };
  const trilha = el("ol", "trilha");

  const estados = {
    gerando:     ["trabalhando", "neutro", "neutro"],
    verificando: ["ok", "trabalhando", "neutro"],
    criticando:  ["ok", "ok", "trabalhando"],
  }[p.etapa] || ["trabalhando", "neutro", "neutro"];

  const textos = {
    gerando:     ["redigindo…", "aguardando", "aguardando"],
    verificando: ["questão redigida", "conferindo a conta…", "aguardando"],
    criticando:  ["questão redigida",
                  (VEREDICTO[p.veredicto] || ["conferiu"])[0],
                  "avaliando…"],
  }[p.etapa] || ["redigindo…", "aguardando", "aguardando"];

  ["Gerador", "Verificador simbólico", "Crítico didático"].forEach((agente, i) => {
    trilha.append(etapa(agente, textos[i], null, estados[i]));
  });

  if (p.iteracao > 1) {
    const nota = el("li", "trilha__etapa trilha__etapa--neutro");
    nota.append(el("span", "trilha__agente", "Iteração"));
    nota.append(el("span", "trilha__veredicto", `${p.iteracao} de 3`));
    trilha.append(nota);
  }
  return trilha;
}

/* --------------------------------------------------------- cartão da questão */
function detalhe(resumo, preencher) {
  const bloco = el("details", "detalhe");
  bloco.append(el("summary", "detalhe__resumo", resumo));
  const corpo = el("div", "detalhe__corpo");
  preencher(corpo);
  bloco.append(corpo);
  // Fórmula composta enquanto o bloco está fechado sai com a caixa medida em
  // zero — o navegador não mede o que não desenha. Compor de novo ao abrir
  // custa nada: o que já virou SVG o MathJax não revisita.
  bloco.addEventListener("toggle", () => { if (bloco.open) renderizarMatematica(corpo); });
  return bloco;
}

function corpoDaQuestao(questao) {
  const corpo = el("div", "questao__corpo");
  const enunciado = el("div", "questao__enunciado marcacao");
  enunciado.append(montarMarcacao(questao.enunciado));
  corpo.append(enunciado);
  if (questao.alternativas && questao.alternativas.length) {
    const lista = el("ul", "questao__alternativas");
    "abcd".split("").forEach((letra, i) => {
      const alt = questao.alternativas[i];
      if (!alt) return;
      const item = el("li", "questao__alternativa" + (alt.correta ? " questao__alternativa--correta" : ""));
      item.append(el("span", "questao__letra", `(${letra})`));
      const texto = el("div", "marcacao");
      texto.append(montarMarcacao(alt.texto));
      item.append(texto);
      lista.append(item);
    });
    corpo.append(lista);
  }
  return corpo;
}

function cabecaDaQuestao(questao, identificacao) {
  const cabeca = el("div", "questao__cabeca");
  cabeca.append(el("span", "questao__id", identificacao));
  const spec = questao.especificacao;
  const meta = [
    // Questões salvas antes da multisseleção têm `tema` no singular.
    (spec.temas || [spec.tema]).map((t) => rotulo(estadoApp.opcoes.temas, t)).join(" + "),
    spec.habilidade_bncc,
    rotulo(estadoApp.opcoes.bloom, spec.nivel_bloom),
    rotulo(estadoApp.opcoes.dificuldades, spec.dificuldade),
    rotulo(estadoApp.opcoes.formatos, spec.formato),
  ].join(" · ");
  cabeca.append(el("span", "questao__meta", meta));
  return cabeca;
}

function blocosDeApoio(cartao, questao, iteracao) {
  cartao.append(detalhe("Resolução e gabarito", (corpo) => {
    const resolucao = el("div", "marcacao");
    resolucao.append(montarMarcacao(questao.resolucao));
    corpo.append(resolucao);
    const gab = el("p", "marcacao__paragrafo");
    gab.append(el("strong", null, "Gabarito: "));
    gab.append(...nosDaLinha(questao.gabarito));
    gab.style.marginTop = "12px";
    corpo.append(gab);
  }));

  if (iteracao && iteracao.parecer) {
    cartao.append(detalhe("Parecer didático por critério", (corpo) => {
      const lista = el("ul", "criterios");
      for (const nota of iteracao.parecer.notas) {
        const item = el("li", "criterios__item");
        item.append(el("span", "criterios__nota", `${nota.nota}/5`));
        item.append(el("span", null, `${nota.criterio} — ${nota.comentario}`));
        lista.append(item);
      }
      corpo.append(lista);
    }));
  }
}

/* ----------------------------------------------------- cartão: recém-gerada */
function cartaoGerado(entrada, indice) {
  const cartao = el("article", "questao");
  const r = entrada.resultado;

  if (!r) {  // ainda em andamento
    const cabeca = el("div", "questao__cabeca");
    cabeca.append(el("span", "questao__id", "Gerando…"));
    cartao.append(cabeca);
    cartao.append(trilhaEmAndamento(entrada.progresso));
    return cartao;
  }

  const ultima = r.iteracoes[r.iteracoes.length - 1];

  if (!r.aprovada) {
    cartao.append(cabecaDaQuestao(ultima.questao, "Descartada"));
    cartao.append(corpoDaQuestao(ultima.questao));
    cartao.append(montarTrilha(ultima));
    cartao.append(el("p", "iteracao",
      `Descartada após ${r.iteracoes.length} iterações sem aprovação. Ajuste a especificação e gere de novo.`));
    historicoAnterior(cartao, r);
    return cartao;
  }

  cartao.append(cabecaDaQuestao(r.questao_final, entrada.id ? `Questão #${entrada.id}` : "Aprovada"));
  cartao.append(corpoDaQuestao(r.questao_final));
  cartao.append(montarTrilha(ultima));
  historicoAnterior(cartao, r);
  blocosDeApoio(cartao, r.questao_final, ultima);

  const rodape = el("div", "questao__rodape");
  const garantia = etiquetaDeGarantia(GARANTIA_POR_VEREDICTO[ultima.verificacao.veredicto]);
  if (garantia) rodape.append(garantia);
  if (entrada.id) {
    rodape.append(el("span", "etiqueta etiqueta--ok", "no banco"));
    rodape.append(el("span", "campo__ajuda", "Avalie esta questão na aba Banco curado."));
  } else {
    const salvar = el("button", "botao botao--principal", "Salvar no banco");
    salvar.addEventListener("click", async () => {
      salvar.disabled = true;
      try {
        const dados = await (await api("/api/banco", { method: "POST", body: JSON.stringify(r) })).json();
        entrada.id = dados.id;
        if (dados.aviso_sincronizacao) avisar(dados.aviso_sincronizacao, "erro");
        else avisar(`Salva como questão #${dados.id}.`, "ok");
        renderizarGerados();
        carregarEstado();
      } catch (erro) {
        avisar(`Não foi possível salvar: ${erro.message}`, "erro");
        salvar.disabled = false;
      }
    });
    rodape.append(salvar);
    rodape.append(el("span", "campo__ajuda", "Só o que você salvar entra no banco e vai para a pasta sincronizada."));
  }
  cartao.append(rodape);
  return cartao;
}

function historicoAnterior(cartao, resultado) {
  for (const it of resultado.iteracoes.slice(0, -1)) {
    const linha = el("p", "iteracao");
    linha.append(el("span", "iteracao__rotulo", `Iteração ${it.numero} `));
    linha.append(document.createTextNode(it.feedback_para_gerador || "revisada"));
    cartao.append(linha);
  }
}

function renderizarGerados() {
  const area = document.getElementById("resultados");
  area.replaceChildren();
  if (!estadoApp.gerados.length) {
    const vazio = el("div", "vazio");
    vazio.append(el("p", "vazio__titulo", "Nenhuma questão gerada ainda"));
    vazio.append(el("p", "vazio__texto",
      "Descreva a questão à esquerda e clique em Gerar. Cada questão passa por três agentes antes de chegar aqui — e o veredicto de cada um fica registrado junto com ela."));
    area.append(vazio);
    return;
  }
  estadoApp.gerados.forEach((entrada, i) => area.append(cartaoGerado(entrada, i)));
  renderizarMatematica(area);
}

/* ------------------------------------------------------------------ geração */
const espera = (ms) => new Promise((r) => setTimeout(r, ms));

/** Dispara o ciclo e acompanha até o fim, atualizando a trilha no caminho.
 *
 *  Um ciclo leva de 80 a 250 segundos — mais do que qualquer proxy reverso
 *  aceita numa requisição só. Por isso o servidor devolve um identificador na
 *  hora e nós perguntamos o andamento. */
async function executarCiclo(spec, entrada) {
  const inicio = await (await api("/api/gerar", {
    method: "POST", body: JSON.stringify(spec),
  })).json();

  while (true) {
    await espera(2000);
    const situacao = await (await api(`/api/gerar/${inicio.tarefa}`)).json();

    if (situacao.estado === "executando") {
      entrada.progresso = situacao.progresso;
      renderizarGerados();
      continue;
    }
    if (situacao.estado === "erro") throw new Error(situacao.detalhe);
    return situacao.resultado;
  }
}

async function gerar(evento) {
  evento.preventDefault();
  const botao = document.getElementById("botao-gerar");
  const form = document.getElementById("form-gerar");
  const quantidade = Math.max(1, Math.min(10, Number(form.quantidade.value) || 1));
  const spec = lerEspecificacao();

  botao.disabled = true;
  for (let i = 0; i < quantidade; i++) {
    botao.textContent = quantidade > 1 ? `Gerando ${i + 1} de ${quantidade}…` : "Gerando…";
    const entrada = { resultado: null, id: null, progresso: null };
    estadoApp.gerados.unshift(entrada);
    renderizarGerados();
    try {
      entrada.resultado = await executarCiclo(spec, entrada);
    } catch (erro) {
      estadoApp.gerados.shift();
      renderizarGerados();
      avisar(`Falha na geração: ${erro.message}`, "erro");
      break;
    }
    renderizarGerados();
  }
  botao.disabled = false;
  botao.textContent = "Gerar";
  // Reler o estado atualiza quantas questões ainda cabem no convite — e é o que
  // trava o botão na última, em vez de deixar o 429 aparecer como falha.
  carregarEstado().catch(() => {});
}

/* -------------------------------------------------------------------- banco */
function controlesDeAvaliacao(registro) {
  const area = el("div", "avaliacao");
  area.append(el("span", "avaliacao__rotulo", "Sua avaliação:"));

  const comentario = el("input", "avaliacao__comentario");
  comentario.placeholder = "por que aceitou, ajustou ou recusou (opcional)";
  comentario.value = registro.comentario_professor || "";

  const registrada = el("span", "avaliacao__registrada");
  const mostrarRegistrada = () => {
    registrada.textContent = registro.decisao_professor
      ? `registrada: ${rotulo(estadoApp.opcoes.decisoes, registro.decisao_professor)}`
      : "";
  };
  mostrarRegistrada();

  for (const decisao of estadoApp.opcoes.decisoes) {
    const botao = el("button", "opcoes__item", decisao.rotulo);
    botao.type = "button";
    botao.style.flex = "0 0 auto";
    if (registro.decisao_professor === decisao.valor) botao.classList.add("opcoes__item--ativo");
    botao.addEventListener("click", async () => {
      try {
        const resposta = await (await api(`/api/banco/${registro.id}/avaliacao`, {
          method: "POST",
          body: JSON.stringify({ decisao: decisao.valor, comentario: comentario.value.trim() || null }),
        })).json();
        registro.decisao_professor = decisao.valor;
        registro.comentario_professor = comentario.value.trim();
        for (const irmao of area.querySelectorAll(".opcoes__item")) {
          irmao.classList.toggle("opcoes__item--ativo", irmao === botao);
        }
        mostrarRegistrada();
        if (resposta.aviso_sincronizacao) avisar(resposta.aviso_sincronizacao, "erro");
        else avisar("Avaliação registrada.", "ok");
      } catch (erro) {
        avisar(`Não foi possível registrar: ${erro.message}`, "erro");
      }
    });
    area.append(botao);
  }

  area.append(comentario);
  area.append(registrada);
  return area;
}

function cartaoDoBanco(registro) {
  const cartao = el("article", "questao");
  const questao = registro.questao;

  const cabeca = cabecaDaQuestao(questao, `Questão #${String(registro.id).padStart(4, "0")}`);
  const selecao = el("label", "selecao");
  const caixa = el("input");
  caixa.type = "checkbox";
  caixa.checked = estadoApp.selecionadas.has(registro.id);
  caixa.addEventListener("change", () => {
    if (caixa.checked) estadoApp.selecionadas.add(registro.id);
    else estadoApp.selecionadas.delete(registro.id);
    atualizarBarraLista();
  });
  selecao.append(caixa, el("span", null, "usar na lista"));
  cabeca.append(selecao);
  selecao.style.marginLeft = "auto";
  cartao.append(cabeca);

  cartao.append(corpoDaQuestao(questao));

  const rodape = el("div", "questao__rodape");
  const [texto, estilo] = VEREDICTO[registro.veredicto_verificacao]
    || [registro.veredicto_verificacao, "neutro"];
  const classeEtiqueta = { ok: "ok", erro: "erro", parcial: "parcial" }[estilo] || "neutra";
  const garantia = etiquetaDeGarantia(registro.garantia);
  if (garantia) rodape.append(garantia);
  rodape.append(el("span", `etiqueta etiqueta--${classeEtiqueta}`, `verificador: ${texto}`));
  if (registro.nota_minima_critico != null) {
    rodape.append(el("span", "etiqueta etiqueta--neutra", `nota mínima ${registro.nota_minima_critico}/5`));
  }
  rodape.append(el("span", "etiqueta etiqueta--neutra", `${registro.iteracoes || 1} iteração(ões)`));
  cartao.append(rodape);

  blocosDeApoio(cartao, questao, null);
  cartao.append(controlesDeAvaliacao(registro));
  return cartao;
}

async function carregarBanco() {
  const tema = document.getElementById("filtro-tema").value;
  const dificuldade = document.getElementById("filtro-dificuldade").value;
  const garantia = document.getElementById("filtro-garantia").value;
  const busca = new URLSearchParams();
  if (tema) busca.set("tema", tema);
  if (dificuldade) busca.set("dificuldade", dificuldade);
  if (garantia) busca.set("garantia", garantia);

  estadoApp.banco = await (await api(`/api/banco?${busca}`)).json();
  const area = document.getElementById("lista-banco");
  area.replaceChildren();

  document.getElementById("contagem-banco").textContent =
    `${estadoApp.banco.length} questão(ões)`;

  if (!estadoApp.banco.length) {
    const vazio = el("div", "vazio");
    vazio.append(el("p", "vazio__titulo", "Banco vazio"));
    vazio.append(el("p", "vazio__texto",
      "As questões que você salvar na aba Gerar aparecem aqui, prontas para avaliar e montar listas."));
    area.append(vazio);
    return;
  }
  for (const registro of estadoApp.banco) area.append(cartaoDoBanco(registro));
  renderizarMatematica(area);
}

/* ---------------------------------------------------------- montagem da lista */
function atualizarBarraLista() {
  const barra = document.getElementById("barra-lista");
  barra.hidden = estadoApp.selecionadas.size === 0;
  document.getElementById("qtd-selecionadas").textContent = estadoApp.selecionadas.size;
}

async function baixarLista(formato) {
  const corpo = {
    titulo: document.getElementById("titulo-lista").value || "Lista de exercícios",
    ids: [...estadoApp.selecionadas].sort((a, b) => a - b),
    com_gabarito: document.getElementById("com-gabarito").checked,
    formato_arquivo: formato,
  };
  try {
    const resposta = await api("/api/lista", { method: "POST", body: JSON.stringify(corpo) });
    const blob = await resposta.blob();
    const nome = (resposta.headers.get("Content-Disposition") || "").match(/filename="(.+?)"/);
    const link = el("a");
    link.href = URL.createObjectURL(blob);
    link.download = nome ? nome[1] : `lista.${formato}`;
    link.click();
    URL.revokeObjectURL(link.href);
  } catch (erro) {
    avisar(`Não foi possível montar a lista: ${erro.message}`, "erro");
  }
}

/* ------------------------------------------------------------------- abas */
function trocarAba(nome) {
  for (const botao of document.querySelectorAll(".abas__item")) {
    botao.classList.toggle("abas__item--ativo", botao.dataset.aba === nome);
  }
  document.getElementById("aba-gerar").hidden = nome !== "gerar";
  document.getElementById("aba-banco").hidden = nome !== "banco";
  document.getElementById("barra-lista").hidden = nome !== "banco" || estadoApp.selecionadas.size === 0;
  if (nome === "banco") carregarBanco();
}

/* ------------------------------------------------------------------ início */
async function iniciar() {
  capturarConvite();
  await descobrirApi();
  try {
    estadoApp.opcoes = await (await api("/api/opcoes")).json();
  } catch (erro) {
    /* Sem convite, a primeira chamada já volta 401 — e é o caso mais comum de
       quem abre o endereço direto, sem o link. Um aviso que some em seis
       segundos deixava a pessoa diante de uma página vazia sem explicação. */
    if (erro.status === 401) await mostrarBloqueio();
    else avisar(`Não foi possível falar com o servidor: ${erro.message}`, "erro");
    return;
  }
  await montarFormulario();
  try {
    await carregarEstado();
  } catch (erro) {
    if (erro.status === 401) await mostrarBloqueio();
    return;
  }

  document.getElementById("config-provedor").addEventListener("change", atualizarSugestoesDeModelo);
  document.getElementById("campo-habilidade").addEventListener("change", mostrarDescricaoHabilidade);
  document.getElementById("campo-bloom").addEventListener("change", avisarSobreBloom);
  document.getElementById("sortear-contexto").addEventListener("click", sortearContexto);
  document.getElementById("form-gerar").addEventListener("submit", gerar);
  document.getElementById("filtro-tema").addEventListener("change", carregarBanco);
  document.getElementById("filtro-dificuldade").addEventListener("change", carregarBanco);
  document.getElementById("filtro-garantia").addEventListener("change", carregarBanco);

  for (const botao of document.querySelectorAll(".abas__item")) {
    botao.addEventListener("click", () => trocarAba(botao.dataset.aba));
  }
  for (const botao of document.querySelectorAll(".barra-lista__acoes .botao")) {
    botao.addEventListener("click", () => baixarLista(botao.dataset.formato));
  }

  const dialogo = document.getElementById("dialogo-config");
  document.getElementById("abrir-config").addEventListener("click", () => dialogo.showModal());
  document.getElementById("salvar-config").addEventListener("click", async () => {
    // Chave, provedor e modelo são de quem usa: ficam no navegador, nunca no
    // servidor. O modelo acompanha o provedor — guardar um sem o outro deixaria
    // o convidado com um nome de modelo da família errada.
    const campoChave = document.getElementById("config-chave");
    if (campoChave.value) guardado.chave = campoChave.value;
    guardado.provedor = document.getElementById("config-provedor").value;
    guardado.modelo = document.getElementById("config-modelo").value.trim();
    campoChave.value = "";
    estadoApp.identificacao = null;  // relê do servidor após salvar

    try {
      if (!estadoApp.compartilhado) {
        await api("/api/config", {
          method: "POST",
          body: JSON.stringify({
            // Na máquina onde o servidor roda, a escolha também vira o padrão
            // dele: é o que vale para uso programático e para a próxima sessão.
            pasta_sincronizada: document.getElementById("config-pasta").value.trim(),
            provedor: guardado.provedor,
            modelo: guardado.modelo,
            responsavel: document.getElementById("config-responsavel").value.trim(),
            instituicao: document.getElementById("config-instituicao").value.trim(),
            contato: document.getElementById("config-contato").value.trim(),
          }),
        });
      }
      await carregarEstado();
      avisar("Configurações salvas.", "ok");
    } catch (erro) {
      avisar(`Não foi possível salvar: ${erro.message}`, "erro");
    }
  });

  document.getElementById("esquecer-chave").addEventListener("click", () => {
    guardado.chave = "";
    carregarEstado();
    avisar("Chave removida deste navegador.", "ok");
  });

  renderizarGerados();
}

iniciar();
