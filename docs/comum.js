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
  get modelo() { return localStorage.getItem("questoes.modelo") || ""; },
  set modelo(v) { v ? localStorage.setItem("questoes.modelo", v) : localStorage.removeItem("questoes.modelo"); },
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
  if (API_PADRAO) { guardado.api = API_PADRAO; return; }

  // O endereço guardado é um palpite, não um dogma: o túnel muda de endereço a
  // cada reinício, e confiar cegamente no valor antigo deixava a pessoa presa a
  // um túnel morto para sempre — justamente o que o backend.json evita.
  if (localStorage.getItem("questoes.api") && await apiResponde(guardado.api)) return;

  // Servida pelo próprio servidor? Então a API é a mesma origem.
  if (await apiResponde("")) { guardado.api = ""; return; }

  try {
    const caminho = raiz ? `${raiz}/backend.json` : "backend.json";
    // Sem cache: o endereço muda e um valor velho leva a um túnel morto.
    const cfg = await (await fetch(`${caminho}?t=${Date.now()}`)).json();
    if (cfg.endereco && await apiResponde(cfg.endereco)) {
      guardado.api = cfg.endereco;
      return;
    }
  } catch (_) { /* sem backend.json publicado */ }

  avisar("O servidor não está respondendo. Ele pode estar fora do ar no momento.", "erro");
}

/** A API atende neste endereço? Usa a rota pública, que não exige convite. */
async function apiResponde(base) {
  try {
    const r = await fetch(`${base}/api/identificacao`, { cache: "no-store" });
    return r.ok;
  } catch (_) {
    return false;
  }
}

/** Chamada à API com as credenciais que este navegador guarda. */
async function api(caminho, opcoes = {}) {
  const cabecalhos = { "Content-Type": "application/json" };
  if (guardado.convite) cabecalhos["X-Convite"] = guardado.convite;
  if (guardado.chave) cabecalhos["X-Chave-API"] = guardado.chave;
  if (guardado.provedor) cabecalhos["X-Provedor"] = guardado.provedor;
  // O modelo acompanha o provedor: os dois são escolha de quem usa. Sem este
  // par, quem escolhesse outro provedor receberia o modelo configurado no
  // servidor — um nome da família errada, que o serviço recusa.
  if (guardado.modelo) cabecalhos["X-Modelo"] = guardado.modelo;
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
