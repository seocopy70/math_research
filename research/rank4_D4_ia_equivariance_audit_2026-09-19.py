#!/usr/bin/env python3
"""
Rank-4 D4 quotient-legitimacy / equivariance audit.

This is a structural audit, not a rank-4 representative scan.
It verifies that the frozen first-IA defect variation space and the
ordinary conjugation correction space are invariant under the authoritative
Sp_4(F3) transvections and a multiplier-2 GSp representative.

The action is the frozen coefficient/tensor action:
X_i -> sum_j M[j,i] X_j on the degree-1 Magnus space, extended
multiplicatively to degree 3.
"""

from itertools import combinations, product
P=3; N=4; D=3
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
            if len(w)<=D: c[w]=(c.get(w,0)+va*vb)%P
    return {k:v for k,v in c.items() if v}
def inv(a):
    h=add(a,scale(ONE,-1)); z=ONE.copy(); t=ONE.copy()
    for k in range(1,D+1):
        t=mul(t,h); z=add(z,scale(t,(-1)**k))
    return z
X=[{(i,):1} for i in range(N)]
GEN=[add(ONE,x) for x in X]
PAIRS=list(combinations(range(N),2))
WORDS3=list(product(range(N),repeat=3))
def comm(i,j): return [(i,1),(j,1),(i,-1),(j,-1)]
def ev(word,gens=GEN):
    z=ONE
    for i,s in word: z=mul(z,gens[i] if s==1 else inv(gens[i]))
    return z
R3=[(0,1)]*3+comm(0,1)+comm(2,3)
RINF=comm(0,1)+comm(2,3)
B3=ev(R3); BI=ev(RINF)
R2={w:v for w,v in B3.items() if len(w)==2}
def vec(a): return [a.get(w,0) for w in WORDS3]
def rank(rows):
    a=[r[:] for r in rows if any(r)]
    if not a:return 0
    rr=0; n=len(a[0])
    for col in range(n):
        piv=next((i for i in range(rr,len(a)) if a[i][col]%P),None)
        if piv is None: continue
        a[rr],a[piv]=a[piv],a[rr]
        z=pow(a[rr][col],-1,P)
        a[rr]=[(x*z)%P for x in a[rr]]
        for i in range(len(a)):
            if i!=rr and a[i][col]:
                f=a[i][col]
                a[i]=[(a[i][j]-f*a[rr][j])%P for j in range(n)]
        rr+=1
    return rr
C3=[vec(add(mul(X[i],R2),scale(mul(R2,X[i]),-1))) for i in range(N)]
SPECS=[(i,j,k) for i in range(N) for j,k in PAIRS]
def ia_lift(spec):
    i,j,k=spec
    h=[dict(z) for z in GEN]
    h[i]=mul(h[i],ev(comm(j,k)))
    return h
def defect(rel,base,lift):
    return vec(add(ev(rel,lift),scale(base,-1)))
def variation(spec):
    b=defect(R3,B3,GEN)
    return [(x-y)%P for x,y in zip(defect(R3,B3,ia_lift(spec)),b)]
V=[variation(s) for s in SPECS]
assert rank(V)==20
assert rank(C3)==4
GAUGE=C3+V
assert rank(GAUGE)==20

# Frozen alternating form matching R2=[X0,X1]+[X2,X3].
J=[
 [0,1,0,0],
 [2,0,0,0],
 [0,0,0,1],
 [0,0,2,0],
]
def mat_vec(M,v):
    return [sum(M[i][j]*v[j] for j in range(4))%P for i in range(4)]
def transvection(v):
    # T_v(w)=w+<w,v>v, <w,v>=w^T J v.
    Jv=mat_vec(J,v)
    return [[(1 if i==j else 0)+v[i]*Jv[j] for j in range(4)] for i in range(4)]
def tensor_action(r,M):
    out=[0]*64
    for pos,w in enumerate(WORDS3):
        c=r[pos]
        if not c: continue
        choices=[[(j,M[j][i]%P) for j in range(4) if M[j][i]%P] for i in w]
        for js in product(*choices):
            ww=tuple(x[0] for x in js)
            cc=c
            for _,a in js: cc=cc*a%P
            out[WORDS3.index(ww)]=(out[WORDS3.index(ww)]+cc)%P
    return out
def span_rank_with_action(S,M):
    return rank(S+[tensor_action(r,M) for r in S])

vectors=[v for v in product(range(3),repeat=4) if any(v)]
assert len(vectors)==80
bad_V=[]; bad_C=[]; bad_G=[]
for v in vectors:
    M=transvection(v)
    if span_rank_with_action(V,M)!=20: bad_V.append(v)
    if span_rank_with_action(C3,M)!=4: bad_C.append(v)
    if span_rank_with_action(GAUGE,M)!=20: bad_G.append(v)

# Multiplier-2 similitude: blockwise scaling in each symplectic pair.
Mmu=[[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,2]]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4))%P for j in range(4)] for i in range(4)]
JMu=matmul([list(x) for x in zip(*Mmu)],matmul(J,Mmu))
assert JMu==[[x*2%P for x in row] for row in J]
mu_V=span_rank_with_action(V,Mmu)
mu_C=span_rank_with_action(C3,Mmu)
mu_G=span_rank_with_action(GAUGE,Mmu)

assert not bad_V and not bad_C and not bad_G
assert mu_V==20 and mu_C==4 and mu_G==20

print({
 "status":"PASS_LOCAL_EQUIVARIANCE_AUDIT",
 "IA_variation_rank":20,
 "C3_rank":4,
 "gauge_rank":20,
 "candidate_quotient_dimension":44,
 "Sp4_nonzero_transvections_tested":80,
 "bad_IA_variation_transvections":len(bad_V),
 "bad_C3_transvections":len(bad_C),
 "bad_gauge_transvections":len(bad_G),
 "GSp_multiplier_2_checked":True,
 "multiplier_2_IA_rank":mu_V,
 "multiplier_2_C3_rank":mu_C,
 "multiplier_2_gauge_rank":mu_G,
 "interpretation":"The first-IA variation space, C3, and their sum are invariant under all 80 nonzero-vector Sp4(F3) transvections and the tested multiplier-2 GSp representative. Thus the 44-dimensional quotient carries the frozen tensor action for this generator audit. This establishes equivariance for the tested generating family, not coordinate-free canonicity under arbitrary reparametrization."
})
