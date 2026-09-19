#!/usr/bin/env python3
"""Rank-4 D4 admissible-category covariance audit.

This audit does NOT scan all GSp_4(F3).  It first fixes the admissible
linear-action category forced by the frozen q=3 degree-3 p-layer condition
g e1 = mu(g)e1.  It then enumerates that subgroup exactly and tests:
  * C3, Delta_IA and G3=C3+Delta_IA covariance;
  * the induced 44-dimensional quotient action;
  * transport of the q=3 vs q=infinity defect for the admissible
    representative -I;
  * compatibility of the q-sensitive source X1^[3] with the multiplier.

All arithmetic is exact over F3 and degree <=3.
"""

from itertools import combinations, product

P,N,D=3,4,3
ONE={():1}
X=[{(i,):1} for i in range(N)]
GEN=[{():1,(i,):1} for i in range(N)]
PAIRS=list(combinations(range(N),2))
WORDS3=list(product(range(N),repeat=3))

def add(a,b):
    c=dict(a)
    for w,v in b.items():
        c[w]=(c.get(w,0)+v)%P
        if c[w]==0: del c[w]
    return c
def sc(a,s):
    return {w:v*s%P for w,v in a.items() if v*s%P}
def mul(a,b):
    c={}
    for x,u in a.items():
        for y,v in b.items():
            w=x+y
            if len(w)<=D: c[w]=(c.get(w,0)+u*v)%P
    return {w:v for w,v in c.items() if v}
def inv(a):
    h=add(a,sc(ONE,-1)); z=dict(ONE); t=dict(ONE)
    for k in range(1,D+1):
        t=mul(t,h); z=add(z,sc(t,(-1)**k))
    return z
def comm(i,j): return [(i,1),(j,1),(i,-1),(j,-1)]
def ev(w,G):
    z=dict(ONE)
    for i,s in w: z=mul(z,G[i] if s==1 else inv(G[i]))
    return z
def vec(a): return [a.get(w,0) for w in WORDS3]
def rank(rows):
    a=[r[:] for r in rows if any(r)]
    if not a:return 0
    m,n=len(a),len(a[0]); rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if a[i][c]%P),None)
        if p is None: continue
        a[rr],a[p]=a[p],a[rr]
        q=pow(a[rr][c],-1,P); a[rr]=[x*q%P for x in a[rr]]
        for i in range(m):
            if i!=rr and a[i][c]:
                q=a[i][c]; a[i]=[(a[i][j]-q*a[rr][j])%P for j in range(n)]
        rr+=1
    return rr

R3=[(0,1)]*3+comm(0,1)+comm(2,3)
RI=comm(0,1)+comm(2,3)
B3=ev(R3,GEN); BI=ev(RI,GEN)
R2={w:v for w,v in B3.items() if len(w)==2}
C3=[vec(add(mul(X[i],R2),sc(mul(R2,X[i]),-1))) for i in range(N)]

def ia_lift(spec):
    i,j,k=spec
    h=[dict(z) for z in GEN]
    h[i]=mul(h[i],ev(comm(j,k),GEN))
    return h
def defect(R,B,L):
    return vec(add(ev(R,L),sc(B,-1)))
base3=defect(R3,B3,GEN)
V=[]
for i,j,k in [(i,j,k) for i in range(N) for j,k in PAIRS]:
    d=defect(R3,B3,ia_lift((i,j,k)))
    V.append([(x-y)%P for x,y in zip(d,base3)])
assert rank(C3)==4 and rank(V)==20 and rank(C3+V)==20
GAUGE=C3+V

# Frozen symplectic form.
J=[[0,1,0,0],[2,0,0,0],[0,0,0,1],[0,0,2,0]]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(N))%P for j in range(N)] for i in range(N)]
def mt(A): return [list(x) for x in zip(*A)]
def mv(A,v): return [sum(A[i][j]*v[j] for j in range(N))%P for i in range(N)]
def key(A): return tuple(x for row in A for x in row)
I=[[1 if i==j else 0 for j in range(N)] for i in range(N)]
e1=[1,0,0,0]

def transvection(v):
    Jv=mv(J,v)
    return [[(I[i][j]+v[i]*Jv[j])%P for j in range(N)] for i in range(N)]

# Sp stabilizer of the line <e1>: use all transvections with <e1,v>=0.
VECTORS=[list(v) for v in product(range(P),repeat=N) if any(v)]
SP_GENS=[transvection(v) for v in VECTORS if sum(e1[i]*sum(J[i][j]*v[j] for j in range(N)) for i in range(N))%P==0]
assert len(SP_GENS)==26

# Exact subgroup closure.
sp_stab={key(I):I}
front=[I]
while front:
    A=front.pop()
    for B in SP_GENS:
        C=mm(A,B); k=key(C)
        if k not in sp_stab:
            sp_stab[k]=C; front.append(C)
assert len(sp_stab)==648

# Multiplier-2 similitude fixing e1; the two cosets give the full
# GSp line-multiplier stabilizer.
M2=[[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,2]]
assert mm(mm(mt(M2),J),M2)==[[2*x%P for x in row] for row in J]
admissible=list(sp_stab.values())+[mm(M2,A) for A in sp_stab.values()]
assert len({key(A) for A in admissible})==1296

def tensor_action(r,M):
    out=[0]*64
    for pos,w in enumerate(WORDS3):
        c=r[pos]
        if not c: continue
        choices=[[(j,M[j][i]%P) for j in range(N) if M[j][i]%P] for i in w]
        for js in product(*choices):
            ww=tuple(x[0] for x in js)
            cc=c
            for _,a in js: cc=cc*a%P
            idx=WORDS3.index(ww)
            out[idx]=(out[idx]+cc)%P
    return out

def mat_vec_span(S,M):
    return rank(S+[tensor_action(r,M) for r in S])

bad_C=[]; bad_V=[]; bad_G=[]; bad_source=[]
for M in admissible:
    # Check g e1 = mu e1 and recover mu from M^T J M = mu J.
    MJ=mm(mm(mt(M),J),M)
    muval=next(a for a in range(1,3) if MJ==[[a*x%P for x in row] for row in J])
    assert [M[i][0]%P for i in range(N)]==[(muval if i==0 else 0) for i in range(N)]
    if mat_vec_span(C3,M)!=4: bad_C.append(M)
    if mat_vec_span(V,M)!=20: bad_V.append(M)
    if mat_vec_span(GAUGE,M)!=20: bad_G.append(M)
    src=[1 if w==(0,0,0) else 0 for w in WORDS3]
    moved=tensor_action(src,M)
    expected=[(muval if w==(0,0,0) else 0) for w in WORDS3]
    if moved!=expected: bad_source.append(M)

assert not bad_C and not bad_V and not bad_G and not bad_source

# The admissible q=3 representative -I has mu=2 and its q-sensitive
# defect is exactly X1^3.
MINUS=[inv(GEN[i]) for i in range(N)]
sig= [(x-y)%P for x,y in zip(defect(R3,B3,MINUS), defect(RI,BI,MINUS))]
assert sig==[1 if w==(0,0,0) else 0 for w in WORDS3]

print({
    "status":"PASS_LOCAL_ADMISSIBLE_COVARIANCE_AUDIT",
    "admissible_category":"{g in GSp4(F3): g e1 = mu(g)e1}",
    "Sp_line_stabilizer_size":648,
    "GSp_admissible_category_size":1296,
    "C3_rank":4,
    "Delta_IA_rank":20,
    "gauge_rank":20,
    "Q3_dimension":44,
    "bad_C3":len(bad_C),
    "bad_Delta_IA":len(bad_V),
    "bad_gauge":len(bad_G),
    "bad_restricted_source":len(bad_source),
    "q_sensitive_defect_for_minus_I":"X1^3",
    "interpretation":"Within the frozen degree-3 convention, the admissible linear-action category forced by the q=3 p-layer condition has 1296 elements. The ordinary correction space, first-IA variation space, and their sum are invariant under the entire category; the 44-dimensional quotient therefore carries the induced admissible-category action. The q-sensitive source X1^[3] transforms by the GSp multiplier, and the -I q=3-vs-q=infinity defect is exactly X1^3 and remains nonzero."
})
