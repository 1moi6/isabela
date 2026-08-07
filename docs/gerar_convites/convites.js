/* =============================================================================
   Página de convites: criar, listar e revogar acessos.

   A senha vive em sessionStorage, não em localStorage: ela some ao fechar a
   aba. É uma credencial de administração — não deve ficar guardada como a
   preferência de tema de alguém.
   ========================================================================== */

const alvo = { convites: [] };

function copiar(texto, botao) {
  navigator.clipboard.writeText(texto).then(
    () => {
      const antes = botao.textContent;
      botao.textContent = "copiado";
      setTimeout(() => { botao.textContent = antes; }, 1800);
    },
    () => avisar("O navegador não deixou copiar. Selecione o link à mão.", "erro"),
  );
}

function cartaoConvite(convite) {
  const cartao = el("article", "questao");

  const cabeca = el("div", "questao__cabeca");
  cabeca.append(el("span", "questao__id", convite.nome));
  cabeca.append(el("span", "questao__meta", `banco: ${convite.identificador}`));

  const revogar = el("button", "botao botao--discreto", "Revogar");
  revogar.style.marginLeft = "auto";
  revogar.addEventListener("click", async () => {
    // Sem diálogo do navegador: alert/confirm travam a automação e a página.
    if (revogar.dataset.confirmando !== "sim") {
      revogar.dataset.confirmando = "sim";
      revogar.textContent = "confirmar?";
      setTimeout(() => {
        revogar.dataset.confirmando = "";
        revogar.textContent = "Revogar";
      }, 4000);
      return;
    }
    try {
      await api(`/api/convites/${convite.codigo}`, { method: "DELETE" });
      avisar(`Convite de ${convite.nome} revogado. O banco dela continua guardado.`, "ok");
      carregar();
    } catch (erro) {
      avisar(`Não foi possível revogar: ${erro.message}`, "erro");
    }
  });
  cabeca.append(revogar);
  cartao.append(cabeca);

  const corpo = el("div", "questao__rodape");
  const campo = el("input", "avaliacao__comentario");
  campo.readOnly = true;
  campo.value = convite.link;
  campo.addEventListener("focus", () => campo.select());

  const botaoCopiar = el("button", "botao", "Copiar link");
  botaoCopiar.addEventListener("click", () => copiar(convite.link, botaoCopiar));

  corpo.append(campo, botaoCopiar);
  cartao.append(corpo);
  return cartao;
}

async function carregar() {
  const area = document.getElementById("lista-convites");
  try {
    const dados = await (await api("/api/convites")).json();
    alvo.convites = dados.convites;
    area.replaceChildren();

    if (!dados.publicacao_automatica) {
      const aviso = el("p", "especificacao__aviso");
      aviso.textContent =
        "A publicação automática do endereço não está configurada, então os links " +
        "abaixo só funcionam enquanto o túnel atual estiver no ar.";
      area.append(aviso);
    }

    if (!alvo.convites.length) {
      const vazio = el("div", "vazio");
      vazio.append(el("p", "vazio__titulo", "Nenhum convite ainda"));
      vazio.append(el("p", "vazio__texto",
        "Escreva o nome da pessoa acima e gere o primeiro. Cada uma terá seu próprio banco de questões."));
      area.append(vazio);
      return;
    }
    for (const c of alvo.convites) area.append(cartaoConvite(c));
  } catch (erro) {
    if (erro.status === 401 || erro.status === 403) {
      guardado.admin = "";
      mostrarSenha(erro.message);
      return;
    }
    avisar(`Não foi possível carregar: ${erro.message}`, "erro");
  }
}

function mostrarSenha(mensagem) {
  document.getElementById("area-admin").hidden = true;
  document.getElementById("area-senha").hidden = false;
  if (mensagem) avisar(mensagem, "erro");
  document.getElementById("campo-senha").value = "";
  document.getElementById("campo-senha").focus();
}

function mostrarAdmin() {
  document.getElementById("area-senha").hidden = true;
  document.getElementById("area-admin").hidden = false;
  carregar();
}

async function iniciar() {
  await descobrirApi("..");

  document.getElementById("form-senha").addEventListener("submit", async (e) => {
    e.preventDefault();
    guardado.admin = document.getElementById("campo-senha").value;
    try {
      await api("/api/convites");
      mostrarAdmin();
    } catch (erro) {
      guardado.admin = "";
      avisar(erro.message, "erro");
    }
  });

  document.getElementById("form-novo").addEventListener("submit", async (e) => {
    e.preventDefault();
    const campo = document.getElementById("campo-nome");
    try {
      const novo = await (await api("/api/convites", {
        method: "POST", body: JSON.stringify({ nome: campo.value }),
      })).json();
      campo.value = "";
      avisar(`Convite criado para ${novo.nome}.`, "ok");
      carregar();
    } catch (erro) {
      avisar(`Não foi possível criar: ${erro.message}`, "erro");
    }
  });

  if (guardado.admin) mostrarAdmin(); else mostrarSenha();
}

iniciar();
