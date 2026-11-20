from pathlib import Path
from fractions import Fraction as F
from math import comb
from collections import defaultdict
import json
p=Path(__file__).parent
src=p/'Q1BUDGETHAND_CONTINUATION_ORIGINAL_FINITE_GENERATION_V1_20261008.exact.json'
source=json.loads(src.read_text());data={'records':[{'marker':'old_full_z','endpoint':k,'degree':v['degree'],'coefficients':[dict(q=m['q'],c=m['c'],y=m['z'],value=m['value']) for m in v['coefficients']]} for k,v in source['polynomials'].items()]};ans=[]
def one(co):
 flag=False
 for v in co:
  if v<0:flag=True
  elif v>0 and flag:return False
 return True
for r in data['records']:
 if r['marker']!='old_full_z':continue
 n=42 if r['endpoint']=='Tlo' else 70
 shift=defaultdict(F)
 for m in r['coefficients']:
  a=m['q'];j=m['c'];h=m['y'];v=F(m['value'])
  for t in range(a+1):shift[t,j,h]+=v*comb(a,t)*F(1,29)**(a-t)
 nx=r['degree'][0];nc=r['degree'][1];groups=[]
 for k in range(n+1):
  bc=defaultdict(F)
  for (a,j,h),v in shift.items():
   if h<=k:bc[a,j]+=v*F(comb(k,h),comb(n,h))
  P0=[bc[a,0] for a in range(nx+1)];P1=[F() for a in range(nx+1)]
  for (a,j),v in list(bc.items()):
   if j==1:P1[a]+=v
   elif j>=2 and v<0:P1[a]+=v/F(6**(j-1))
  Q=[P0[a]+P1[a]/6 for a in range(nx+1)]
  ends=[sum((v*F(86,29)**a for a,v in enumerate(cc)),F()) for cc in [P0,Q]]
  ok=one(P0) and one(Q) and min(ends)>0 and P0[0]>0 and Q[0]>0
  row={'k':k,'P0_one_change':one(P0),'Q_one_change':one(Q),'P0_at_xmax':str(ends[0]),'Q_at_xmax':str(ends[1]),'P0_constant':str(P0[0]),'Q_constant':str(Q[0]),'candidate_payable':ok,
       'P0':[str(x) for x in P0],'P1':[str(x) for x in P1],'Q':[str(x) for x in Q]}
  assert ok,(r['endpoint'],k)
  row['P0_signs']=''.join('+' if x>0 else '-' if x<0 else '0' for x in P0)
  row['Q_signs']=''.join('+' if x>0 else '-' if x<0 else '0' for x in Q)
  groups.append(row)
  print(r['endpoint'],k,'candidate payable',ok,'P0/Q pattern',one(P0),one(Q),'const pos',P0[0]>0,Q[0]>0,'end pos',min(ends)>0,flush=True)
 ans.append({'endpoint':r['endpoint'],'y_elevated_degree':n,'groups':groups})
out=Path(__file__).with_suffix('.exact.json');assert not out.exists();out.write_text(json.dumps({'state':'complete author finite payments with original source and closed degree; independent AI pending','records':ans},indent=2)+'\n')
md=['# 原完整预算有限附录：全部来源向量、41项次数账与114笔连续付款','',
'所有向量低幂到高幂，全部内部零槽显示。完整来源是正文的原分式有限乘积，不是旧1738表。只沿z有限升次；q,c使用连续比较，未作二轴Bernstein。','',
'## A. 全部原分子','']
for name,r in source['polynomials'].items():
 poly={(m['q'],m['c'],m['z']):F(m['value']) for m in r['coefficients']};nq,nc,nz=r['degree']
 md += ['### '+name,f'完整次数界({nq},{nc},{nz})；非零自然项{len(poly)}。固定(q次数,z次数)，每向量完整c^0…c^{nc}。','']
 for a in range(nq+1):
  for h in range(nz+1):md.append(f'({a},{h}): ['+', '.join(str(poly.get((a,j,h),F())) for j in range(nc+1))+']')
 md.append('')
md+=['## B. 校准有限分子W与Z','']
for name,ll in source['ledgers'].items():
 for target in ['W','Z']:
  poly={(m['q'],m['c']):F(m['value']) for m in ll[target+'_coefficients']}
  nq=max(a for a,j in poly);nc=max(j for a,j in poly)
  md += [f'### {name} {target}',f'每行q次固定，完整c^0…c^{nc}。','']
  for a in range(nq+1):md.append(f'{a}: ['+', '.join(str(poly.get((a,j),F())) for j in range(nc+1))+']')
  md.append('')
md += ['## C. 逐原项清分母与无尾次数账','',
'编号按正文：10个尾项、6个W项、4个eB项、1个根平方项、1个W2项、17个Kn项、2个信用项。每行分子次数由正文已显示基础乘积相加；C减去显示分母的余因子次数再相加，最后一列是清后上界。','']
for name,ll in source['ledgers'].items():
 md += ['### '+name,'','|项号|原分母因子|原分子次数(q,c,z)|清后次数上界|','|---|---|---|---|']
 for i,row in enumerate(ll['rows']):md.append(f"|{i+1}|{row['term_denominators']}|{tuple(row['term_numerator_degree'])}|{tuple(row['cleared_degree_bound'])}|")
 md += [f"全部项上界：{tuple(ll['factor_bound'])}。",'']
md += ['## D. 全部114个z函数的q,c连续付款','',
'置x=q−1/29，X=86/29。每组P0/P1/Q按x^0…x^nq列全；Q=P0+P1/6。P1来自正文全部高c负项归并公式，不能把P1本身假定正。每个P0与Q完整向量符合一次符号变化。精确端点可按H_n=p_n、H_a=p_a+(86/29)H_(a+1)逐步重算。','']
for r in ans:
 md += ['### '+r['endpoint']+f"：z升次n={r['y_elevated_degree']}",'']
 for row in r['groups']:
  md += [f"#### k={row['k']}",f"P0: [{', '.join(row['P0'])}]",f"P1: [{', '.join(row['P1'])}]",f"Q: [{', '.join(row['Q'])}]",
    f"P0符号串：{row['P0_signs']}；Q符号串：{row['Q_signs']}。",
    f"P0(0)={row['P0_constant']}>0；Q(0)={row['Q_constant']}>0。",
    f"P0(X)={row['P0_at_xmax']}>0。",f"Q(X)={row['Q_at_xmax']}>0。",'']
md += ['作者有限算术实际通过全部114组，独立AI核验待审。全13904个原槽及所有付款均在本附录显示；不将114组计数说成114次手算，保留全部有限算术依赖。','']
mp=Path(__file__).with_suffix('.generated.md');assert not mp.exists();mp.write_text('\n'.join(md))
print('All complete author source vectors, degree ledger and 114 exact payments saved',flush=True)
