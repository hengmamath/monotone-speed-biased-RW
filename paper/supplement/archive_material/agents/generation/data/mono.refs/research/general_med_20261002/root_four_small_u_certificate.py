"""CORRECTED s4 payment on u<=1/2; sign is tested, not presumed.

Original calibration and clearing checks precede the whole-box test.
No unconditional threshold claim; previously accepted707/500 is intact.
"""
from pathlib import Path
src=Path(__file__).with_name('root_four_term_payment_certificate.py').read_text()
exec(compile(src.split("print('New numerator degree'")[0], 'original_S4_checks', 'exec'))
assert last==4
deg=P.degree_list();cf={}
for (i,j,k),v in P.terms():
 vv=F(int(v.p),int(v.q))
 for a in range(i+1):
  idx=(a,j,k)
  cf[idx]=cf.get(idx,F(0))+vv*comb(i,a)*F(23,20)**(i-a)*F(7,20)**a*F(1,2)**j
for axis in range(3):
 out={}
 for idx,v in cf.items():
  for a in range(idx[axis],deg[axis]+1):
   ii=list(idx);ii[axis]=a;ii=tuple(ii)
   out[ii]=out.get(ii,F(0))+v*F(comb(a,idx[axis]),comb(deg[axis],idx[axis]))
 cf=out
full=[cf.get(idx,F(0)) for idx in product(*(range(n+1) for n in deg))]
assert deg==(39,15,14) and len(full)==9600
assert all(v>0 for v in full)
print('CORRECTED S4 u<=1/2:',sum(v<0 for v in full),'negative;',
      sum(v>0 for v in full),'positive;',len(full),'total',flush=True)
