/* =============================================================================
   Peças usadas pelas duas páginas: a do professor e a de convites.

   A descoberta do endereço da API é sutil o bastante para não viver em dois
   lugares — duplicá-la garantiria que uma das cópias ficasse para trás.
   ========================================================================== */

/* Endereço fixo do backend, quando houver túnel nomeado. Vazio significa:
   descobrir em tempo de execução (ver descobrirApi). */
const API_PADRAO = "";

const guardado = {
  get convite() { return localStorage.getItem("questoes.convite") || ""; },
  set convite(v) { localStorage.setItem("questoes.convite", v); },
  get chave() { return localStorage.getItem("questoes.chave") || ""; },
  set chave(v) { v ? localStorage.setItem("questoes.chave", v) : localStorage.removeItem("questoes.chave"); },
  get provedor() { return localStorage.getItem("questoes.provedor") || ""; },
  set provedor(v) { v ? localStorage.setItem("questoes.provedor", v) : localStorage.removeItem("questoes.provedor"); },
  get api() { return localStorage.getItem("questoes.api") || API_PADRAO; },
  set api(v) { v ? localStorage.setItem("questoes.api", v) : localStorage.removeItem("questoes.api"); },
  get admin() { return sessionStorage.getItem("questoes.admin") || ""; },
  set admin(v) { v ? sessionStorage.setItem("questoes.admin", v) : sessionStorage.removeItem("questoes.admin"); },
};

function el(tag, classe, texto) {
  const node = document.createElement(tag);
  if (classe) node.className = classe;
  if (texto !== undefined && texto !== null) node.textContent = texto;
  return node;
}

function avisar(mensagem, tipo = "") {
  let caixa = document.getElementById("avisos");
  if (!caixa) {
    caixa = el("div", "avisos");
    caixa.id = "avisos";
    document.body.append(caixa);
  }
  const item = el("div", `aviso ${tipo ? "aviso--" + tipo : ""}`, mensagem);
  caixa.append(item);
  setTimeout(() => item.remove(), 6000);
}

/** Descobre onde está a API: link → constante → mesma origem → backend.json.
 *
 *  A penúltima etapa evita um erro silencioso: servida pelo próprio servidor,
 *  a página leria um backend.json possivelmente velho e apontaria para um
 *  túnel morto em vez de para si mesma.
 *
 *  `raiz` é o prefixo até a pasta publicada — "" na página principal e ".."
 *  numa subpágina, porque o backend.json fica na raiz do site. */
async function descobrirApi(raiz = "") {
  if (localStorage.getItem("questoes.api")) return;
  if (API_PADRAO) { guardado.api = API_PADRAO; return; }

  try {
    const r = await fetch("/api/identificacao");
    if (r.ok) { guardado.api = ""; return; }
  } catch (_) { /* origem não atende a API: seguimos para o backend.json */ }

  try {
    const caminho = raiz ? `${raiz}/backend.json` : "backend.json";
    // Sem cache: o endereço muda e um valor velho leva a um túnel morto.
    const cfg = await (await fetch(`${caminho}?t=${Date.now()}`)).json();
    if (cfg.endereco) guardado.api = cfg.endereco;
  } catch (_) {
    avisar("Não encontrei o endereço do servidor. Peça um link novo a quem administra.", "erro");
  }
}

/** Chamada à API com as credenciais que este navegador guarda. */
async function api(caminho, opcoes = {}) {
  const cabecalhos = { "Content-Type": "application/json" };
  if (guardado.convite) cabecalhos["X-Convite"] = guardado.convite;
  if (guardado.chave) cabecalhos["X-Chave-API"] = guardado.chave;
  if (guardado.provedor) cabecalhos["X-Provedor"] = guardado.provedor;
  if (guardado.admin) cabecalhos["X-Chave-Admin"] = guardado.admin;

  const resposta = await fetch(guardado.api + caminho, { headers: cabecalhos, ...opcoes });
  if (!resposta.ok) {
    let detalhe = `${resposta.status} ${resposta.statusText}`;
    try {
      const corpo = await resposta.json();
      if (corpo.detail) {
        detalhe = typeof corpo.detail === "string" ? corpo.detail : JSON.stringify(corpo.detail);
      }
    } catch (_) { /* resposta sem corpo JSON */ }
    const erro = new Error(detalhe);
    erro.status = resposta.status;
    throw erro;
  }
  return resposta;
}
