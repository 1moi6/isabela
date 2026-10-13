# Junta as transcrições das respostas com o _chave.csv e imprime as contagens da Seção 6.1.
import csv,collections as C,sys
from pathlib import Path
D=Path(__file__).parent; K=D.parent/"_chave.csv"
chave={r['item']:r for r in csv.DictReader(open(K))}
R=[]
AVS=[a for a in (1,2,3,4,5) if (D/f'transcricao-avaliador-{a}.csv').exists()]
for a in AVS:
    for r in csv.DictReader(open(D/f'transcricao-avaliador-{a}.csv')):
        r['av']=a; r.update({k:chave[r['item']][k] for k in ('habilidade','dificuldade','garantia','formato','natureza','nivel_bloom','avaliadores')})
        R.append(r)
print('respostas',len(R),'itens distintos',len({r['item'] for r in R}))
def tab(campo,por='av'):
    t=C.defaultdict(C.Counter)
    for r in R: t[r[por]][r[campo] or '(branco)']+=1
    for k in sorted(t): print(f'  {k}: {dict(t[k])}')
    print('  total:',dict(C.Counter(r[campo] or '(branco)' for r in R)))
for c in ('tem_erro','dificuldade_percebida','decisao'): print('==',c); tab(c)
print('== declarada x percebida')
ordem=['facil','media','dificil','fora_do_alcance','']
m=C.Counter((r['dificuldade'],r['dificuldade_percebida']) for r in R)
for d in ('facil','media','dificil'): print(' ',d,[m[(d,p)] for p in ordem])
idx={'facil':0,'media':1,'dificil':2,'fora_do_alcance':3}
dif=[idx[r['dificuldade_percebida']]-idx[r['dificuldade']] for r in R if r['dificuldade_percebida']]
print('  igual',sum(x==0 for x in dif),'acima',sum(x>0 for x in dif),'abaixo',sum(x<0 for x in dif),'de',len(dif))
for a in AVS:
    d=[idx[r['dificuldade_percebida']]-idx[r['dificuldade']] for r in R if r['dificuldade_percebida'] and r['av']==a]
    print('  av',a,'igual',sum(x==0 for x in d),'acima',sum(x>0 for x in d),'abaixo',sum(x<0 for x in d))
print('== decisao por garantia'); tab('decisao','garantia')
print('== decisao por dificuldade declarada'); tab('decisao','dificuldade')
print('== decisao por formato'); tab('decisao','formato')
print('== decisao por natureza'); tab('decisao','natureza')
print('== decisao x dificuldade percebida'); tab('decisao','dificuldade_percebida')
print('== ancora')
for it in ('Q007','Q015','Q024','Q034','Q065','Q087'):
    rs=sorted([r for r in R if r['item']==it],key=lambda r:r['av'])
    print(' ',it,chave[it]['habilidade'],chave[it]['dificuldade'],'|',' ; '.join(f"av{r['av']}:{r['tem_erro'] or '-'}/{r['dificuldade_percebida'] or '-'}/{r['decisao'] or '-'}" for r in rs))
print('== recusadas e ajustes com por_que')
for r in R:
    if r['decisao'] in ('recusada','aceita_com_ajuste') or r['por_que'] or r['tem_erro']=='sim':
        print(f"  av{r['av']} {r['item']} {r['habilidade']} decl={r['dificuldade']} perc={r['dificuldade_percebida']} {r['decisao']} erro={r['tem_erro']} {r['onde']!r} :: {r['por_que']}")
