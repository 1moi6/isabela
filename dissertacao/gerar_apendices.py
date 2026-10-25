"""Regera os apêndices derivados do repositório (não editar os .tex gerados à mão).

Uso, da raiz do repositório:  python dissertacao/gerar_apendices.py .

Gera em dissertacao/capitulos/:
  apendice_prompts_texto.tex     <- sistema/prompts/*.md
  apendice_exemplos_texto.tex    <- banco_curado/banco_curado.tex (rodar antes sistema/montar_banco.py)
  apendice_tabela_respostas.tex  <- sistema/medicoes/acervo-consolidado/avaliacao/
"""
import csv
def tabela_respostas(D, out):

    chave = {r['item']: r for r in csv.DictReader(open(D/'_chave.csv', encoding='utf-8'))}
    dec = {}
    for a in range(1, 6):
        for r in csv.DictReader(open(D/'respostas'/f'transcricao-avaliador-{a}.csv', encoding='utf-8')):
            dec[(r['item'], a)] = r
    SIG_DEC = {'aceita': 'A', 'aceita_com_ajuste': 'J', 'recusada': 'R', '': '--'}
    SIG_DIF = {'basico': 'B', 'facil': 'F', 'media': 'M', 'dificil': 'D'}
    SIG_FMT = {'discursiva': 'Disc.', 'multipla_escolha': 'ME'}
    SIG_GAR = {'conferido': 'C', 'conferido_em_parte': 'P', 'sem_conferencia': 'S'}
    linhas = []
    for item in sorted(i for i in chave if any((i, a) in dec for a in range(1, 6))):
        k = chave[item]
        cel = []
        for a in range(1, 6):
            r = dec.get((item, a))
            if r is None:
                cel.append('')
            else:
                s = SIG_DEC.get(r['decisao'], r['decisao'])
                if r['tem_erro'] == 'sim':
                    s += '$^{e}$'
                cel.append(s)
        nome = item + ('$^{*}$' if item == 'Q061' else '')
        linhas.append(' & '.join([nome, k['habilidade'].replace('EM13MAT', ''), SIG_FMT[k['formato']],
                                  SIG_DIF[k['dificuldade']], SIG_GAR[k['garantia']]] + cel) + r' \\')
    cab = (r'Item & Hab. & Formato & Decl. & Gar. & Av.~1 & Av.~2 & Av.~3 & Av.~4 & Av.~5 \\')
    tex = [r'% Gerado a partir de sistema/medicoes/acervo-consolidado/avaliacao/ (_chave.csv e',
           r'% respostas/transcricao-avaliador-*.csv). Não editar à mão: regerar se os dados mudarem.',
           r'{\small',
           r'\begin{longtable}{llllcccccc}',
           r'\caption{Decisões de uso na primeira rodada, por questão}\label{tab:apendice-respostas}\\',
           r'\toprule', cab, r'\midrule', r'\endfirsthead',
           r'\multicolumn{10}{l}{\footnotesize\emph{continuação}}\\', r'\toprule', cab, r'\midrule', r'\endhead',
           r'\bottomrule', r'\endfoot'] + linhas + [r'\end{longtable}', r'}']
    out.write_text('\n'.join(tex) + '\n', encoding='utf-8')


import re, sys, textwrap
from pathlib import Path
R = Path(sys.argv[1])
CAP = R / 'dissertacao' / 'capitulos'

# --- Apêndice A: prompts em verbatim, linhas quebradas em 92 colunas
def bloco(md: str) -> str:
    linhas = []
    for l in md.replace('—', '--').replace('–', '-').splitlines():
        if len(l) <= 86:
            linhas.append(l); continue
        recuo = len(l) - len(l.lstrip())
        partes = textwrap.wrap(l.strip(), width=86 - recuo - 2, break_long_words=True)
        linhas.append(' ' * recuo + partes[0])
        linhas += [' ' * (recuo + 2) + p for p in partes[1:]]
    return '{\\footnotesize\n\\begin{verbatim}\n' + '\n'.join(linhas) + '\n\\end{verbatim}\n}\n'
g = (R/'sistema/prompts/gerador.md').read_text(encoding='utf-8')
c = (R/'sistema/prompts/critico.md').read_text(encoding='utf-8')
(CAP/'apendice_prompts_texto.tex').write_text(
    '% Gerado a partir de sistema/prompts/*.md. Não editar à mão: regerar se os prompts mudarem.\n'
    '\\section*{Prompt do Agente Gerador}\n\\addcontentsline{toc}{section}{Prompt do Agente Gerador}\n' + bloco(g) +
    '\\section*{Prompt do Agente Crítico Didático}\n\\addcontentsline{toc}{section}{Prompt do Agente Crítico Didático}\n' + bloco(c),
    encoding='utf-8')

# --- Apêndice B: questões do bloco-âncora e a Q061 corrigida, extraídas do banco curado
tex = (R/'banco_curado/banco_curado.tex').read_text(encoding='utf-8')
corpo = tex.split('\\begin{document}', 1)[1].rsplit('\\end{document}', 1)[0]
blocos = re.split(r'(?=\\bigskip\\noindent\\textbf\{Q\d{3})', corpo)
quero = ['Q007', 'Q015', 'Q024', 'Q034', 'Q065', 'Q087', 'Q061']
achados = {}
for b in blocos:
    m = re.match(r'\\bigskip\\noindent\\textbf\{(Q\d{3})', b)
    if m and m.group(1) in quero:
        b = b.split('\\subsection*{')[0]          # corta o cabeçalho da habilidade seguinte
        b = re.sub(r'\n\{\\small\\itshape.*?\}\n', '\n', b, flags=re.S)
        achados[m.group(1)] = b.strip()
saida = ['% Gerado a partir de banco_curado/banco_curado.tex. Não editar à mão.',
         '\\begingroup\\sloppy\\setlength{\\parindent}{0pt}\\setlength{\\parskip}{0.5em}']
for q in quero:
    saida.append(achados[q]); saida.append('')
saida.append('\\endgroup')
(CAP/'apendice_exemplos_texto.tex').write_text('\n'.join(saida) + '\n', encoding='utf-8')
tabela_respostas(R/'sistema/medicoes/acervo-consolidado/avaliacao', CAP/'apendice_tabela_respostas.tex')
print('ok', sorted(achados))
