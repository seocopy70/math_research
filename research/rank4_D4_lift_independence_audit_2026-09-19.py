#!/usr/bin/env python3
"""
Rank-4 D4 lifting-definition audit: lift-independence stress test.

Purpose: test whether the candidate relator-unit condition is intrinsic to
the induced linear map g on V, rather than to a chosen free-group lift.

Frozen q=3 relator: r3=x1^3[x1,x2][x3,x4].
Frozen baseline quadratic relation: R2=[X1,X2]+[X3,X4].
All arithmetic is over F3 and truncated at associative Magnus degree 3.
"""
from itertools import product
P=3; N=4; MAXD=3
ONE={():1}
def add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=(c.get(k,0)+v)%P
        if c[k]==0: del c[k]
    return c
def scale(a,s):
    return {k:(v*s)%P for k,v in a.items() if (v*s)%P}
def mul(a,b):
    c={}
    for wa,va in a.items():
        for wb,vb in b.items():
            w=wa+wb
            if len(w)<=MAXD: c[w]=(c.get(w,0)+va*vb)%P
    return {k:v for k,v in c.items() if v}
def inv(a):
    h=add(a,scale(ONE,-1)); z=ONE.copy(); term=ONE.copy()
    for k in range(1,MAXD+1):
        term=mul(term,h); z=add(z,scale(term,(-1)**k))
    return z
X=[{(i,):1} for i in range(N)]
GEN=[add(ONE,x) for x in X]
def eval_word(w,gens=GEN):
    z=ONE
    for i,s in w: z=mul(z, gens[i] if s==1 else inv(gens[i]))
    return z
def comm(i,j): return [(i,1),(j,1),(i,-1),(j,-1)]
R3=[(0,1)]*3+comm(0,1)+comm(2,3)
BASE=eval_word(R3)
R2={w:v for w,v in BASE.items() if len(w)==2}
def vec(a,d): return [a.get(w,0) for w in product(range(N),repeat=d)]
def rank(rows):
    if not rows:return 0
    A=[r[:] for r in rows]; m=len(A); n=len(A[0]); rr=0
    for col in range(n):
        piv=next((i for i in range(rr,m) if A[i][col]%P),None)
        if piv is None:continue
        A[rr],A[piv]=A[piv],A[rr]; invp=pow(A[rr][col],-1,P)
        A[rr]=[(x*invp)%P for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][col]%P:
                f=A[i][col]; A[i]=[(A[i][j]-f*A[rr][j])%P for j in range(n)]
        rr+=1
        if rr==m:break
    return rr
D=[vec(add(mul(X[i],R2),scale(mul(R2,X[i]),-1)),3) for i in range(N)]
assert rank(D)==4
# Lift A: identity free lift.
LIFT_A=GEN
# Lift B has the same linear action on V, but x1 -> x1 [x1,x2].
cw=comm(0,1)
twisted_x1=eval_word([(0,1)]+cw)
LIFT_B=[twisted_x1,GEN[1],GEN[2],GEN[3]]
imgA=eval_word(R3,LIFT_A); imgB=eval_word(R3,LIFT_B)
dA=add(imgA,scale(BASE,-1)); dB=add(imgB,scale(BASE,-1))
vA=vec(dA,3); vB=vec(dB,3)
payload={
  'status':'FAIL',
  'same_linear_action':True,
  'lift_A':'identity lift',
  'lift_B':'x1 -> x1 [x1,x2], x2,x3,x4 fixed',
  'degree2_difference_A':vec(dA,2),
  'degree2_difference_B':vec(dB,2),
  'correction_span_rank':rank(D),
  'lift_A_admissible':rank(D+[vA])==rank(D),
  'lift_B_admissible':rank(D+[vB])==rank(D),
  'difference_degree3_nonzero':any(vB),
  'difference_outside_correction_span':rank(D+[vB])>rank(D),
}
assert payload['lift_A_admissible'] is True
assert payload['lift_B_admissible'] is False
assert payload['difference_outside_correction_span'] is True
import json; print(json.dumps(payload,indent=2))