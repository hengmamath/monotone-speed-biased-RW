"""Auxiliary-author LOCAL source for W_x<0, not an independent self-audit.
Fresh original B=(p-1+h)/h, p=(1+hx)^(1+t/x); no old/author checker.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import sympy as s
P=Path(__file__).resolve().parent
x,h,t,p=s.symbols('x h t p')
L=1+h*x;d=1-h;E=s.log(L)-h*x/L;e=E/(h**2*x**2)
# Use a formal p only to keep exact original logarithmic differentiation small.
px=p*(h/L-t*E/x**2)
ph=(t+x)*p/L
def Dx(f):return s.diff(f,x)+s.diff(f,p)*px
def Dh(f):return s.diff(f,h)+s.diff(f,p)*ph
B=(p-d)/h;Bx=Dx(B);Bh=Dh(B);Bxh=Dh(Bx)
W=(B+d*Bh)/B**2
Wx=Dx(W)
labels=[]
def check(label,f):
 assert s.cancel(f)==0,label
 labels.append(label);print('LOCAL identity',label)
check('original full B_x from fixed t logarithmic p derivative',Bx-p*(1/L-h*t*e))
check('original full B_h from p_h',Bh-((t+x)*p/L-(p-1)/h)/h)
check('original full B_xh, not fixing Ebar in h derivative',Bxh-p*t*(1-h*t)*e/L)
check('true q_h=-W',Dh(d/B)+W)
check('original W_x quotient rule',Wx-(d*B*Bxh-Bx*(B+2*d*Bh))/B**3)
G=d*t*(1-h*t)*e
H=(1-h*t*L*e)*(1+2*d*Bh/B)
check('full W_x equals p/(L B^2) times left-minus-right',Wx-p*(G-H)/(L*B**2))

dd,tt=s.symbols('dd tt')
a=s.Rational(3,2);r=s.Rational(2,3)
linear=r*tt**2/(1+a*tt)-tt/2
check('complete d-linear comparison coefficient is nonpositive',linear+tt*(s.Rational(1,2)+tt/12)/(1+a*tt))
at_d1=r+linear
check('d=1 exact positive comparison rational',at_d1-(r+tt/2-tt**2/12)/(1+a*tt))
check('entire allowable t-negative-square credit',
      r+tt/2-tt**2/12-(r+s.Rational(3,10)*tt)-tt*(s.Rational(12,5)-tt)/12)
psi=(r+s.Rational(3,10)*tt)/(1+a*tt)
check('lower comparison function strictly decreasing',s.diff(psi,tt)+s.Rational(7,10)/(1+a*tt)**2)
check('exact t endpoint margin',psi.subs(tt,s.Rational(12,5))-s.Rational(104,345))
rr,z=s.symbols('rr z')
check('complete Pade logarithm derivative',s.diff(s.log((2+z)/(2-z))-z,z)-z**2/(4-z**2))
check('y over 1+3y/2 increasing derivative',s.diff(tt/(1+a*tt),tt)-1/(1+a*tt)**2)
payments={
 'maximum_ht':F(1,4)*F(12,5),
 'maximum_L':1+F(1,40),
 'maximum_ht_L_e':F(3,5)*F(41,40)*F(1,2),
 'lower_1_minus_ht_L_e':1-F(123,400),
 'positive_gap_to_two_thirds':F(277,400)-F(2,3),
 'positive_B_multiplier_gap':F(3,2)-F(16,11),
 'entire_p_upper':(2+F(5,8))/(2-F(5,8)),
 'endpoint_positive_margin':(F(2,3)+F(3,10)*F(12,5))/(1+F(3,2)*F(12,5))}
assert payments=={'maximum_ht':F(3,5),'maximum_L':F(41,40),'maximum_ht_L_e':F(123,400),
 'lower_1_minus_ht_L_e':F(277,400),'positive_gap_to_two_thirds':F(31,1200),
 'positive_B_multiplier_gap':F(1,22),'entire_p_upper':F(21,11),'endpoint_positive_margin':F(104,345)}
out=P/'Q3DXHAND_CONTINUATION_INDEPENDENT_TRUE_WX_NEGATIVE_GEOMETRIC_SOURCE_LOCAL_20261008.exact.json';assert not out.exists()
report={'status':'LOCAL complete auxiliary-author true W_x<0 geometric candidate; awaiting parent independent audit',
 'actual_exit':0,'actual_failures':[],'general_identity_labels':labels,
 'full_original_B':str(B),'full_original_Bx':str(Bx),'full_original_Bh':str(Bh),'full_original_Bxh':str(Bxh),
 'full_original_W':str(W),'complete_Wx_comparison':str(p*(G-H)/(L*B**2)),
 'all_short_Fraction_payments':{k:str(v)for k,v in payments.items()},
 'candidate_true_Wx_bound':'W_x < -104*p/(345*L*B^2) < 0 for 0<x<=min(1/10,t), 0<h<=1/4, 0<t<=12/5',
 'all_geometric_B_Bh_coupling_retained':True,'full_exp_Pade_tail_proof_required':True,
 'point_search_performed':False,'new_large_polynomial_table_generated':False,'author_or_old_checker_executed':False,
 'independent_audit_of_own_candidate':False,'full_domain_W3_proved':False,'40706_retired':False,'whole_manual_theorem_complete':False}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('LOCAL all',len(labels),'original/geometric identities and',len(payments),'short Fraction payments complete; no self-audit claim.')
print(out.name,len(out.read_bytes()),hashlib.sha256(out.read_bytes()).hexdigest())
