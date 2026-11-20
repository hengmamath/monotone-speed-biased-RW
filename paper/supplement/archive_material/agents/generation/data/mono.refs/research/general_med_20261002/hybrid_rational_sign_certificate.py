"""Exact independently PASSED certificate for the two hybrid rational signs.

Canonical/rational reductions independently PASSED. Final polynomial signs
are certified by positive integer tensor coefficients, with any exceptional
t row resolved by exact univariate Bernstein subdivision.
No floating-point arithmetic is used. Public mathematical definitions are
repeated here so this file can be copied to another execution environment.
"""
from itertools import product
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json
import sympy as sp

lam, u, z, t = sp.symbols('lam u z t')
c = lam-1
H2 = lam**2+lam-u
H3 = lam**3+lam**2+lam-(lam+1)*u
H4 = lam**4+lam**3+lam**2+lam-(lam**2+lam+1)*u
En = c*H2**2*H3**2*H4**2+c*lam**3*z**2*H3**2*H4**2 \
     +c*lam**4*z**2*H2**2*H4**2+lam**6*z**2*H2**2*H3**2
Vn = lam*(lam-u)*H2**2*H3**2*H4**2 \
     +lam**2*u*z*H2*H3**2*H4**2-lam**4*u*z**2*H3**2*H4**2+u*En
Dr = (lam+1)*(2*lam+7)*(2*lam+1)*(2*lam+7*t)*(2*lam+t)
Zr = c*Dr+9*lam**2*(1-t)*(28*lam**2+17*lam+(17*lam+19)*t)
Cn = u*En*(Dr+Zr)
Ln = c*Vn*(Dr+2*Zr)+u*En*((lam+1)*Dr+2*Zr)
Dn = lam*Ln-2*t*Cn
Ec = -lam**3*c*Vn*Dr-lam**3*Cn+2*lam*t*Ln-3*t**2*Cn
Fn = H2*(Dn-lam**3*En*(Dr+Zr))
raw = [('B0', Fn+z*Ec),
       ('B1', (lam**2-t)**2*Fn+lam**2*z*(lam**2*Ec-t**2*Dn))]

def cube_coefficients(expr):
    """Divide the displayed numerator by positive lam, then lam=(707+268x)/500.

    Coordinates u=lam^2*a, z=D2*s, t=lam*theta range over[0,1].
    The rectangular cube is larger than the actual s>=a domain.
    """
    p = sp.Poly(expr, lam, u, z, t)
    terms = p.terms()
    assert min(powers[0] for powers, _ in terms)>=1
    deg = (p.degree(lam)-1, p.degree(u), p.degree(z), p.degree(t))
    out = {}
    for (n,j,k,h), value in terms:
        assert value.is_Integer
        value = int(value)
        n -= 1
        for i in range(n+1):
            key = i,j,k,h
            out[key] = out.get(key,0)+value*comb(n,i)*707**(n-i)*268**i*500**(deg[0]-n)
    return out,deg

def bernstein_scaled(coeffs, degrees):
    """Tensor coefficients multiplied by product(degree!), all integers."""
    indices = list(product(*(range(d+1) for d in degrees)))
    old = {key:coeffs.get(key,0) for key in indices}
    for axis,d in enumerate(degrees):
        ff = [factorial(i) for i in range(d+1)]
        weights = [[ff[i]//ff[i-k]*ff[d-k] for k in range(i+1)] for i in range(d+1)]
        new = {}
        for key in indices:
            total=0
            for k,weight in enumerate(weights[key[axis]]):
                src=list(key);src[axis]=k
                total+=weight*old[tuple(src)]
            new[key]=total
        old=new
    return old

def check_evaluations(coeffs, bc, deg):
    """Complete power/Bernstein conversion sanity checks at rational points."""
    scale=1
    for d in deg: scale*=factorial(d)
    for nums,dens in [((0,0,0,0),(1,1,1,1)),
                      ((1,1,2,3),(2,3,5,7)),
                      ((1,1,1,1),(1,1,1,1))]:
        def weight(key,bern=False):
            result=1
            for axis in range(4):
                j=key[axis];n=nums[axis];d=dens[axis];D=deg[axis]
                result*=n**j*(d-n if bern else d)**(D-j)
                if bern:result*=comb(D,j)
            return result
        power=sum(v*weight(key) for key,v in coeffs.items())
        bern=sum(v*weight(key,True) for key,v in bc.items())
        assert bern==power*scale

def line_eval(line,x):
    n=len(line)-1
    return sum(comb(n,j)*v*x**j*(1-x)**(n-j) for j,v in enumerate(line))

def half_lines(line):
    """Half-interval Bernstein coefficients, all scaled by the positive 2^n."""
    n=len(line)-1
    left=[2**(n-j)*sum(comb(j,k)*line[k] for k in range(j+1)) for j in range(n+1)]
    right=[2**j*sum(comb(n-j,k)*line[j+k] for k in range(n-j+1)) for j in range(n+1)]
    for x in [Fraction(0),Fraction(1,3),Fraction(1)]:
        assert line_eval(left,x)==2**n*line_eval(line,x/2)
        assert line_eval(right,x)==2**n*line_eval(line,(1+x)/2)
    return left,right

def certify_line(line,a=0,b=1,den=1,depth=0):
    if min(line)>0:
        return [{'interval':[a,b,den],'depth':depth,'count':len(line),
                 'minimum_scaled':str(min(line))}]
    if depth==10:
        raise AssertionError(('exceptional row NOT certified',a,b,den))
    left,right=half_lines(line)
    return certify_line(left,2*a,a+b,2*den,depth+1) \
          +certify_line(right,a+b,2*b,2*den,depth+1)

records=[]
for name,expr in raw:
    co,deg=cube_coefficients(expr)
    bc=bernstein_scaled(co,deg)
    check_evaluations(co,bc,deg)
    original_deg=deg
    negative_rows=sorted({key[:-1] for key,value in bc.items() if value<=0})
    row_records=[]
    for prefix in negative_rows:
        line=[bc[prefix+(j,)] for j in range(deg[-1]+1)]
        leaves=certify_line(line)
        row_records.append({'row':prefix,'leaves':leaves,'passed':True})
        print('EXACT exceptional row',prefix,'leaves',len(leaves),'passed',True,flush=True)
    minimum,index=min((v,key) for key,v in bc.items())
    bad=[(key,str(v)) for key,v in bc.items() if v<=0]
    rec={'name':name,'original_degrees':original_deg,'degrees':deg,'count':len(bc),
         'positive':sum(v>0 for v in bc.values()),
         'zero':sum(v==0 for v in bc.values()),
         'negative':sum(v<0 for v in bc.values()),
         'minimum_scaled':str(minimum),'minimum_index':index,
         'conversion_checks':3,'nonpositive_first20':bad[:20],
         'exceptional_rows':row_records,
         'proved_positive_rows':all(r['passed'] for r in row_records)}
    records.append(rec)
    print(json.dumps(rec),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(records,indent=2)+'\n')
assert len(records)==2
assert records[0]['count']==5400 and records[0]['negative']==records[0]['zero']==0
assert records[1]['count']==7344 and records[1]['negative']==2 and records[1]['zero']==0
assert [r['row'] for r in records[1]['exceptional_rows']]==[(0,0,3),(1,0,3)]
assert sum(len(r['leaves']) for r in records[1]['exceptional_rows'])==6
assert all(r['proved_positive_rows'] for r in records)
print('ALL POLYNOMIALS STRICTLY POSITIVE' if all(r['proved_positive_rows'] for r in records)
      else 'FINAL SIGNS NOT CERTIFIED BY THIS CUBE',flush=True)
