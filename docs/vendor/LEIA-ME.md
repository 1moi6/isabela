# Bibliotecas de terceiros

Estão aqui, versionadas, e não vindas de um CDN, por dois motivos: a página
precisa funcionar no servidor local do professor (que pode não ter internet
liberada, e com Ollama não precisa mesmo de nenhuma) e a interface não tem passo
de build — não há `npm install` para buscá-las na hora.

## mathjax/tex-svg.js

- **O que é:** MathJax 3.2.2, empacotamento `tex-svg` — entrada em LaTeX, saída
  em SVG. Escolhido em vez do `tex-chtml` porque o SVG dispensa arquivos de
  fonte: é um arquivo só, sem nada a buscar depois.
- **Origem:** <https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js>
- **Tamanho:** 2,0 MB
- **SHA-256:** `d4295dc33744836935c1399feece5159577b34c5c8ffb9f1c6324cd82e03a882`
- **Licença:** Apache-2.0
- **Para atualizar:** baixe o arquivo do endereço acima com a versão nova,
  substitua este e anote aqui o novo SHA-256 e o tamanho. Depois suba o `?v=` em
  `docs/index.html`, senão quem já visitou continua com a cópia antiga.
