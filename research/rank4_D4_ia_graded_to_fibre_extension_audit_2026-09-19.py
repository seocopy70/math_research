#!/usr/bin/env python3
"""Rank-4 D4 graded-to-fibre extension datum audit.

Exact F3 Magnus degree <=3.  The audit asks whether higher IA layers can
affect the degree-3 relator defect, and whether the first-layer quotient
already gives a lift-independent defect class for the tested representatives.
"""
from itertools import product

P,N,D=3,4,3
ONE={():1}
GEN=[{():1,(i,):1} for i in range(N)]

def add(a,b):
    c=dict(a)
    for w,v in b.items():
        c[w]=(c.get(w,0)+v)%P
        if c[w]==0: del c[w]
    return c
def sc(a,s):
    return {w:v*s%P for w,v in a.items() if v*s%P}
def mu(a,b):
    c={}
    for x,u in a.items():
        for y,v in b.items():
            w=x+y
            if len(w)<=D: c[w]=(c.get(w,0)+u*v)%P
    return {w:v for w,v in c.items() if v}
def inv(a):
    h=add(a,sc(ONE,-1)); z=dict(ONE); t=dict(ONE)
    for k in range(1,D+1):
        t=mu(t,h); z=add(z,sc(t,(-1)**k))
    return z
def comm(i,j): return [(i,1),(j,1),(i,-1),(j,-1)]
def ev(w,G):
    z=dict(ONE)
    for i,s in w: z=mu(z,G[i] if s==1 else inv(G[i]))
    return z
def vec(a,d): return [a.get(w,0) for w in product(range(N),repeat=d)]
def rank(rows):
    if not rows: return 0
    a=[r[:] for r in rows]; m,n=len(a),len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]%P),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=pow(a[r][c],-1,P); a[r]=[x*q%P for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[(a[i][j]-q*a[r][j])%P for j in range(n)]
        r+=1
    return r
def comp(A,B):
    out=[]
    for w in B:
        z=[]
        for i,s in w:
            z += A[i] if s==1 else [(j,-t) for j,t in A[i][::-1]]
        out.append(z)
    return out
def defect(R,B,L):
    return vec(add(ev(R,L),sc(B,-1)),3)

R3=[(0,1)]*3+comm(0,1)+comm(2,3)
RI=comm(0,1)+comm(2,3)
B3=ev(R3,GEN); BI=ev(RI,GEN)
R2={w:v for w,v in B3.items() if len(w)==2}
X=[{(i,):1} for i in range(N)]
C3=[vec(add(mu(X[i],R2),sc(mu(R2,X[i]),-1)),3) for i in range(N)]
assert rank(C3)==4

# Universal degree-3 higher-IA test.  A higher IA automorphism has generator
# correction starting in degree >=3; degree 3 is the first potentially visible
# higher layer.  Exhaust all 4*4^3 homogeneous degree-3 corrections for both
# relators.
higher_checks=0
for i in range(N):
    for w in product(range(N),repeat=3):
        G=[dict(x) for x in GEN]
        G[i]=add(G[i],{w:1})
        for R,B in ((R3,B3),(RI,BI)):
            d=add(ev(R,G),sc(B,-1))
            assert all(len(k)!=3 or v==0 for k,v in d.items())
            higher_checks += 1

PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
S=[(i,j,k) for i in range(N) for j,k in PAIRS]
def basis(s):
    c=[[0]*6 for _ in range(N)]
    i,j,k=s; c[i][PAIRS.index((j,k))]=1
    return c
def ia(c):
    out=[]
    for i in range(N):
        w=[(i,1)]
        for a,(j,k) in zip(c[i],PAIRS):
            for _ in range(a%P): w += comm(j,k)
        out.append(w)
    return out

CASE_WORDS={
    "identity":[[(i,1)] for i in range(N)],
    "minus_I":[[(i,1),(i,1)] for i in range(N)],
    "transvection":[[(0,1),(1,1)],[(1,1)],[(2,1)],[(3,1)]],
}
res={}
for name,gw in CASE_WORDS.items():
    base=[ev(w,GEN) for w in gw]
    d30=defect(R3,B3,base); di0=defect(RI,BI,base)
    V=[]
    for s in S:
        L=[ev(w,GEN) for w in comp(ia(basis(s)),gw)]
        V.append([(x-y)%P for x,y in zip(defect(R3,B3,L),d30)])
    assert rank(V)==20
    G=C3+V
    assert rank(G)==20
    for s in S:
        L=[ev(w,GEN) for w in comp(ia(basis(s)),gw)]
        d=defect(R3,B3,L)
        diff=[(x-y)%P for x,y in zip(d,d30)]
        assert rank(G+[diff])==rank(G)
    q=[(x-y)%P for x,y in zip(d30,di0)]
    res[name]={
        "C3_rank":4,
        "IA_variation_rank":rank(V),
        "gauge_rank":rank(G),
        "quotient_dimension":64-rank(G),
        "basepoint_classes_equal_mod_gauge":True,
        "q_signal_nonzero":any(q),
        "q_signal_survives_mod_gauge":rank(G+[q])>rank(G),
    }

assert res["minus_I"]["q_signal_survives_mod_gauge"]
assert res["transvection"]["q_signal_survives_mod_gauge"]
print({
    "status":"PASS_GRADED_TO_FIBRE_LOCAL",
    "higher_IA_degree3_checks":higher_checks,
    "object":"Q3 = A3 / (C3 + Delta_IA), dimension 44",
    "interpretation":"Degree-3 higher-IA corrections are invisible, so all degree-3 lift dependence is exhausted by the first IA layer. For the tested representatives the defect class in Q3 is independent of the first-layer base lift and the q=3 versus q=infinity signal survives for -I and the transvection.",
    "cases":res,
})
