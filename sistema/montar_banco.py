"""Monta o banco curado (JSON + LaTeX/PDF) a partir do acervo consolidado.

Uso (de dentro de sistema/): python montar_banco.py . ../banco_curado

Gera banco_curado.json e banco_curado.tex; o PDF sai se houver pdflatex na máquina.
Aplica medicoes/acervo-consolidado/correcoes.json e sorteia a ordem das
alternativas com questoes.alternativas.embaralhar (mesma regra do Gerador atual).
"""
import json, sys
from pathlib import Path

SIS = Path(sys.argv[1]).resolve(); OUT = Path(sys.argv[2]).resolve(); OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(SIS / 'src'))
from questoes.modelos import Questao, garantia_de
from questoes.alternativas import embaralhar
from questoes.tex import PREAMBULO, para_tex, compilar

ACV = SIS / 'medicoes' / 'acervo-consolidado'
ciclos = [json.loads(l) for l in open(ACV / 'ciclos.jsonl', encoding='utf-8') if l.strip()]
correcoes = json.loads((ACV / 'correcoes.json').read_text(encoding='utf-8'))
cat = {h['codigo']: h for h in json.loads((SIS / 'dados' / 'bncc_em_matematica.json').read_text(encoding='utf-8'))['habilidades']}

ROT_GAR = {'conferido': 'gabarito conferido', 'conferido_em_parte': 'conferido em parte',
           'sem_conferencia': 'sem conferência automática: confira o gabarito'}
ROT_DIF = {'basico': 'básico', 'facil': 'fácil', 'media': 'média', 'dificil': 'difícil'}
ROT_FMT = {'discursiva': 'discursiva', 'multipla_escolha': 'múltipla escolha'}
ROT_NAT = {'teorica': 'teórica', 'aplicada': 'aplicada'}

banco = []
for k, c in enumerate(ciclos, 1):
    if not c['aprovada']:
        continue
    num = f'{k:03d}'
    final = correcoes.get(num, {}).get('questao_final', c['questao_final'])
    q = embaralhar(Questao.model_validate(final))
    v = c['iteracoes'][-1]['verificacao']['veredicto']
    banco.append({'id': f'Q{num}', 'questao': q, 'veredicto': v,
                  'corrigida': num in correcoes})

def garantia(item):
    from questoes.modelos import Veredicto
    return garantia_de(Veredicto(item['veredicto'])).value

ordem = sorted(banco, key=lambda b: (b['questao'].especificacao.habilidade_bncc, b['id']))
# JSON
dados = []
for b in ordem:
    d = b['questao'].model_dump(mode='json')
    d.update({'id': b['id'], 'garantia': garantia(b), 'corrigida_apos_avaliacao_docente': b['corrigida']})
    dados.append(d)
(OUT / 'banco_curado.json').write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding='utf-8')

# LaTeX (versão do professor, agrupada por habilidade)
partes = [PREAMBULO, r'\begin{document}', r'\section*{Banco curado de questões}',
          para_tex('Questões geradas pelo sistema multiagente e aprovadas pelo ciclo completo '
                   '(verificação simbólica e avaliação didática). Versão do professor, com gabarito e '
                   'resolução. Licença CC BY-SA 4.0.')]
hab_atual = None
for b in ordem:
    q = b['questao']; s = q.especificacao
    if s.habilidade_bncc != hab_atual:
        hab_atual = s.habilidade_bncc
        partes.append(r'\subsection*{' + hab_atual + '}')
        partes.append(r'{\small\itshape ' + para_tex(cat[hab_atual]['descricao']) + '}')
    meta = (f"{b['id']} · {ROT_FMT[s.formato.value]} · {ROT_DIF[s.dificuldade.value]} · "
            f"{s.nivel_bloom.value} · {ROT_NAT[s.natureza.value]} · {ROT_GAR[garantia(b)]}")
    if b['corrigida']:
        meta += ' · corrigida após a avaliação docente'
    partes.append('')
    partes.append(r'\bigskip\noindent\textbf{' + para_tex(meta) + r'}\par\nopagebreak')
    partes.append(para_tex(q.enunciado))
    if q.alternativas:
        partes.append(r'\begin{enumerate}[label=(\alph*)]')
        partes += [r'\item ' + para_tex(a.texto) for a in q.alternativas]
        partes.append(r'\end{enumerate}')
    partes.append('')
    partes.append(r'\textbf{Gabarito.} ' + para_tex(q.gabarito))
    partes.append('')
    partes.append(r'\textbf{Resolução.} ' + para_tex(q.resolucao))
partes.append(r'\end{document}')
ok = compilar('\n'.join(partes), OUT, 'banco_curado')
print('questoes', len(ordem), 'pdf', ok)
