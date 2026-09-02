/* =============================================================================
   Lê o Markdown-com-matemática que o Gerador escreve e monta os nós da página.

   Espelha `sistema/src/questoes/marcacao.py` — mesma expressão para separar
   moeda de fórmula, mesmos quatro blocos. Duas linguagens, uma leitura só; ao
   mexer numa, confira a outra.

   Tudo aqui sai por `document.createElement` e `textContent`. Nada de
   innerHTML: o texto vem de um modelo de linguagem, e conteúdo gerado não vira
   marcação. A matemática vai para dentro de um `<span>` já delimitada por
   `\(...\)`, e é o MathJax quem a compõe — ver `renderizarMatematica`.
   ========================================================================== */

/* A ordem das alternativas é o que resolve o caso difícil: `R$` aparece solto
   na prosa ("pagou R$ 13,00") e também dentro da fórmula (`$\approx R\$\,8881$`).
   Varrendo da esquerda para a direita, a fórmula é consumida inteira a partir do
   `$` que a abre, então o `R\$` de dentro nunca chega a ser testado como moeda.
   Sem isto, o cifrão da moeda abriria uma "fórmula" que engole meia frase. */
const MOEDA_OU_MATEMATICA =
  /R\\?\$\s*(?=\d)|\$\$(?:[^$\\]|\\[\s\S])+?\$\$|\\\[(?:[^\\]|\\[\s\S])+?\\\]|\$(?:[^$\n\\]|\\[\s\S])+?\$|\\\((?:[^\\]|\\[\s\S])+?\\\)/g;

const ITEM_DE_LISTA = /^\s*[-*+]\s+\S/;
const SEPARADOR_DE_TABELA = /^[\s|:-]+$/;

/** Tira os delimitadores e diz se a fórmula era de display. */
function semDelimitadores(trecho) {
  const pares = [["$$", "$$", true], ["\\[", "\\]", true],
                 ["\\(", "\\)", false], ["$", "$", false]];
  for (const [abre, fecha, display] of pares) {
    if (trecho.startsWith(abre) && trecho.endsWith(fecha)) {
      return [trecho.slice(abre.length, trecho.length - fecha.length).trim(), display];
    }
  }
  return [trecho, false];
}

/** Um trecho de matemática, pronto para o MathJax compor. */
function noMatematica(latex, display) {
  const no = el("span", display ? "mat mat--display" : "mat");
  // Delimitadores `\(...\)` e não `$...$`: o MathJax varre a página inteira, e
  // com cifrão ele tropeçaria no "R$ 13,00" da prosa — o mesmo erro que o
  // LaTeX cometia antes de `tex.py` existir.
  no.textContent = display ? `\\[${latex}\\]` : `\\(${latex}\\)`;
  return no;
}

/** Separa fórmula de prosa numa faixa de texto já classificada. */
function nosDaFaixa(texto, negrito) {
  const nos = [];
  const prosa = (t) => (negrito ? el("strong", null, t) : document.createTextNode(t));
  let pos = 0;
  for (const m of texto.matchAll(MOEDA_OU_MATEMATICA)) {
    if (m.index > pos) nos.push(prosa(texto.slice(pos, m.index)));
    if (m[0].startsWith("R")) {
      // Moeda é texto. O LLM escreve ora "R$ 20,00" ora "R$20,00".
      nos.push(prosa("R$ "));
    } else {
      const [latex, display] = semDelimitadores(m[0]);
      nos.push(noMatematica(latex, display));
    }
    pos = m.index + m[0].length;
  }
  if (pos < texto.length) nos.push(prosa(texto.slice(pos)));
  return nos;
}

/** Uma linha de texto nos seus nós: prosa, negrito e matemática.
 *
 *  O negrito é lido antes da matemática porque ele a contém, e não o contrário:
 *  `**R$ 35,00**` e `**b) Valores em $x=10$**` são o formato normal do Gerador.
 *  Lendo a matemática primeiro, os dois asteriscos caíam em faixas diferentes e
 *  o negrito nunca fechava — apareciam crus na tela. */
function nosDaLinha(texto) {
  const nos = [];
  let pos = 0;
  for (const m of texto.matchAll(/\*\*([\s\S]+?)\*\*/g)) {
    if (m.index > pos) nos.push(...nosDaFaixa(texto.slice(pos, m.index), false));
    nos.push(...nosDaFaixa(m[1], true));
    pos = m.index + m[0].length;
  }
  if (pos < texto.length) nos.push(...nosDaFaixa(texto.slice(pos), false));
  return nos;
}

function celulasDaLinha(linha) {
  return linha.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim());
}

/** Markdown-com-matemática → fragmento pronto para entrar na página. */
function montarMarcacao(texto) {
  const fragmento = document.createDocumentFragment();
  const linhas = (texto || "").split("\n");
  let i = 0;

  while (i < linhas.length) {
    const linha = linhas[i];

    if (!linha.trim()) { i += 1; continue; }

    if (linha.trimStart().startsWith("|")) {
      const corpo = [];
      while (i < linhas.length && linhas[i].trimStart().startsWith("|")) {
        // A linha `|---|---|` marca o cabeçalho no Markdown; não é conteúdo.
        if (!SEPARADOR_DE_TABELA.test(linhas[i].trim())) corpo.push(celulasDaLinha(linhas[i]));
        i += 1;
      }
      if (corpo.length) fragmento.append(montarTabela(corpo));
      continue;
    }

    if (ITEM_DE_LISTA.test(linha)) {
      const lista = el("ul", "marcacao__lista");
      while (i < linhas.length && ITEM_DE_LISTA.test(linhas[i])) {
        const item = el("li");
        item.append(...nosDaLinha(linhas[i].replace(/^\s*[-*+]\s+/, "")));
        lista.append(item);
        i += 1;
      }
      fragmento.append(lista);
      continue;
    }

    // Fórmula sozinha na linha: pode abrir numa linha e fechar em outra, que é
    // como o `\begin{cases}` das funções por partes costuma chegar.
    if (linha.trim().startsWith("$$") || linha.trim().startsWith("\\[")) {
      const fecha = linha.trim().startsWith("$$") ? "$$" : "\\]";
      const bloco = [linhas[i]];
      let aberta = linha.trim() === "$$" || !linha.trim().endsWith(fecha);
      while (aberta && i + 1 < linhas.length) {
        i += 1;
        bloco.push(linhas[i]);
        if (linhas[i].trim().endsWith(fecha)) aberta = false;
      }
      i += 1;
      const [latex] = semDelimitadores(bloco.join("\n").trim());
      const caixa = el("div", "marcacao__formula");
      caixa.append(noMatematica(latex, true));
      fragmento.append(caixa);
      continue;
    }

    const paragrafo = el("p", "marcacao__paragrafo");
    let primeira = true;
    while (i < linhas.length && linhas[i].trim()) {
      const atual = linhas[i];
      if (atual.trimStart().startsWith("|") || ITEM_DE_LISTA.test(atual)
          || atual.trim().startsWith("$$")) break;
      if (!primeira) paragrafo.append(el("br"));
      paragrafo.append(...nosDaLinha(atual));
      primeira = false;
      i += 1;
    }
    if (!primeira) fragmento.append(paragrafo);
  }

  return fragmento;
}

function montarTabela(corpo) {
  // A tabela de faixa de tarifa não cabe no celular: rola dentro da própria
  // caixa em vez de empurrar a página inteira para o lado.
  const caixa = el("div", "marcacao__tabela");
  const tabela = el("table");
  corpo.forEach((linha, n) => {
    const tr = el("tr");
    for (const celula of linha) {
      const td = el(n === 0 ? "th" : "td");
      td.append(...nosDaLinha(celula));
      tr.append(td);
    }
    (n === 0 ? tabela.createTHead() : tabela.createTBody()).append(tr);
  });
  caixa.append(tabela);
  return caixa;
}

/** Pede ao MathJax que componha o que acabou de entrar na página.
 *
 *  O MathJax carrega com `async`, e a primeira questão costuma chegar antes
 *  dele: sem esperar pelo carregamento, o cartão que o professor mais olha —
 *  o primeiro — seria justamente o único a ficar com a fórmula crua.
 *
 *  Silencioso de propósito: sem o MathJax a fórmula fica em `\(...\)` legível,
 *  e uma questão com notação crua ainda serve — um erro no console no meio da
 *  geração, não. */
function renderizarMatematica(no) {
  const mj = window.MathJax;
  if (!mj) return;
  if (mj.startup && mj.startup.promise) {
    mj.startup.promise.then(() => mj.typesetPromise([no])).catch(() => {});
    return;
  }
  const script = document.getElementById("MathJax-script");
  if (script) {
    script.addEventListener("load", () => renderizarMatematica(no), { once: true });
  }
}
