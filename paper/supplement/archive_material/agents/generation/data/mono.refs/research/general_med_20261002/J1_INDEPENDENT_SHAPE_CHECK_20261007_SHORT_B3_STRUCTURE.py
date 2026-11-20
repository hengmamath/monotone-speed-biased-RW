"""Exact finite checks for a shorter structural b3<7 proof.

Uses only definitions from the independently lead-audited original-F QQ[l]
implementation; does not execute any old certificate or its test main.
No parameter diagnostics, scalar degree55 certificates, or numerical sign tests.
"""
from pathlib import Path
from fractions import Fraction as Fr
from math import comb
import ast
import hashlib
import sympy as s

prior = Path(__file__).resolve().parent/'J1_INDEPENDENT_MOVING_POLE_IDENTITY_20261007.py'
assert hashlib.sha256(prior.read_bytes()).hexdigest() == '4b46aaa4eaa125608d7dc9b89a1852a1e2fd6eff7036f80cb3b9c67ffdda982b'
tree = ast.parse(prior.read_text())
definitions = [n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))]
env = {'s':s, 'l':s.symbols('l'), 'ORDER':4}
exec(compile(ast.Module(body=definitions,type_ignores=[]),str(prior),'exec'),env)
Rat, Jet, components = (env[k] for k in ['Rat','Jet','components'])
l = env['l']; L = Rat(l)
S = {j:sum((L**i for i in range(j)),Rat(0)) for j in range(1,6)}
rho = L/S[2]
N = {}
for pole in [2,3,5]:
    q=1-1/S[pole]; uu=Jet([1/q,1]); ll=Jet(L); tt=1-uu
    zz={j:1+tt*(Jet(S[j])-1) for j in range(1,6)}
    aa=zz[2]; kk=1-ll*uu
    K=(ll+1)/(2*ll)+tt/2+(ll+1)*(2*ll*tt-ll+1)*tt/(24*ll)
    ms=components(ll,uu,aa,kk,K,K-tt,zz,pole); m=max(ms)
    cs={r:sum((ms[v].a[v-r]/(S[pole]**v*(-q)**(v-r))
               for v in range(r,m+1)),Rat(0)) for r in range(1,m+1)}
    dd=Jet([1,-(q-rho)]); pp=Jet([1,rho])
    out=sum((Jet(cs[r])*s.Rational(r*(r+1),2)*dd**(m-r)*pp**(r-1)
             for r in cs),Jet(0))
    N[pole]=out.a[:m]
Pa=[rho**2*x for x in N[2]]
q3,q4,q5=(1-1/S[j] for j in [3,4,5])
D,e,z=q4-rho,q4-q3,q5-q4
pa3=Pa[3]-5*D*Pa[2]+10*D**2*Pa[1]-5*D**3*Pa[0]
n33=q3**2*(N[3][1]/20-5*e*N[3][2])
n53=10*q5**2*z**2*(N[5][0]*(D+2*z)+N[5][1])

def polynomial(a,x):
    out=Rat(0)
    for v in reversed(a):
        out=out*x+v
    return out

def same(a,b):
    assert (a-b).n.is_zero

Q10=[129,-460,6218,-13022,-9323,-47772,-26271,-48494,
     -8078,-10468,8597]
V14=[-176,-707,38,3717,10208,-22277,-92600,-218648,-867262,
     374613,1357760,237983,-15118,11023,3454]
W21=[-22,-110,-510,-1506,-3503,-6684,-9532,-9826,-3075,
     12549,36307,62172,81850,89141,82095,64797,43812,25068,
     12022,4577,1320,240]
dena=S[2]**8*(1+L**2)**3*S[3]**2
den3=240*L*S[2]**2*(1+L**2)*S[3]**6
den5=3*S[2]**2*(1+L**2)**3*S[3]**2*S[5]**7
same(pa3,-5*L**4*polynomial(Q10,L)/(6*dena))
same(n33,-polynomial(V14,L)/den3)
same(n53,-20*L**8*polynomial(W21,L)/den5)
print('PASS three complete original-F part identities for b3')

G18=[84720,120120,-421320,2354640,24534380,84852720,
     173695205,243223590,247818005,189357570,110067820,
     48936390,16670935,4368060,889300,141480,16785,1260,45]
same((Rat(15,2)-pa3)*6*dena,polynomial(G18,L-1))
# An independent binomial shift also checks the published c vector.
gp=(Rat(15,2)-pa3)*6*dena
assert gp.d.degree()==0
nl=list(reversed(gp.n.all_coeffs()))
assert [sum(comb(k,j)*nl[k] for k in range(j,len(nl))) for j in range(len(nl))]==G18
assert [j for j,v in enumerate(G18) if v<0]==[2]
assert all(v>0 for j,v in enumerate(G18) if j!=2)
gap_pa=Fr(G18[0])-Fr(-G18[2])*Fr(3,7)**2
assert gap_pa==Fr(359400,49)>0
print('PASS Pa3<15/2 one-negative-coefficient structure; short gap',gap_pa)

A17=[-176,-827,-922,-483,-2512,-51677,-147080,-301928,-974062,
     258693,1250960,154703,-69598,-18377,-9266,-4200,-960,-120]
same((-n33-Rat(1,2))*den3,polynomial(A17,L))
assert all(v<0 for v in A17[:9]+A17[12:])
assert all(v>0 for v in A17[9:12])
low_abs=-sum(A17[:9])
positive_lower=sum(Fr(A17[j])*Fr(23,20)**(j-8) for j in range(9,12))
negative_upper=-sum(Fr(A17[j])*Fr(3,2)**(j-8) for j in range(12,18))
assert low_abs==1479667
assert positive_lower==Fr(17497403801,8000)
assert negative_upper==Fr(44698473,64)
gap3=positive_lower-low_abs-negative_upper
assert gap3==Fr(18189669,2000)>0
print('PASS N3-part<-1/2 three signed blocks, one short payment',gap3)

assert all(v<0 for v in W21[:9])
assert all(v>0 for v in W21[9:])
assert -sum(W21[:9])==34768
assert W21[10]+sum(W21[:9])==1539>0
print('PASS N5-part<0 low negative block absorbed by 36307 lambda^10, gap 1539')
print('PASS continuous written argument: b3=Pa3+N3part+N5part<15/2-1/2=7')
print('LOCAL authored structural proof; lead independent review pending; baseline is preserved')
