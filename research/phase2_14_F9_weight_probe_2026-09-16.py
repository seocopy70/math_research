"""Phase 2-14: exact F9 torus-character probe for E=W/U.

This is a finite-field extension-field probe. It scalar-extends the already
certified F3 degree-4 representation to F9 and evaluates the natural
Sp4(F9) action exactly. It is NOT yet a module-isomorphism certificate.

F9 = F3[w]/(w^2+1), with elements represented as pairs (a,b), a+b*w.
"""
from pathlib import Path
import runpy
import itertools
import numpy as np
P=3; ROOT=Path(__file__).resolve().parents[1]
def f9(x):
    if isinstance(x,tuple): return (x[0]%3,x[1]%3)
    return (int(x)%3,0)
def fadd(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def fneg(x): return ((-x[0])%3,(-x[1])%3)
def fsub(x,y): return fadd(x,fneg(y))
def fmul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def fzero(x): return x[0]==0 and x[1]==0
def finv(x):
    if fzero(x): raise ZeroDivisionError
    d=(x[0]*x[0]+x[1]*x[1])%3; di=1 if d==1 else 2
    return ((x[0]*di)%3,(-x[1]*di)%3)
def fdiv(x,y): return fmul(x,finv(y))
def fpow(x,n):
    out=(1,0); a=x
    while n:
        if n&1: out=fmul(out,a)
        a=fmul(a,a); n//=2
    return out
F9=[(a,b) for a in range(3) for b in range(3)]; F9star=[x for x in F9 if not fzero(x)]
assert len(F9star)==8 and all(fpow(x,8)==(1,0) for x in F9star)
def m9(A): return np.array([[f9(x) for x in row] for row in A],dtype=object)
def I9(n): return np.array([[(1,0) if i==j else (0,0) for j in range(n)] for i in range(n)],dtype=object)
def mm(A,B):
    C=np.empty((A.shape[0],B.shape[1]),dtype=object)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            s=(0,0)
            for q in range(A.shape[1]): s=fadd(s,fmul(A[i,q],B[q,j]))
            C[i,j]=s
    return C
def msub(A,B): return np.array([[fsub(A[i,j],B[i,j]) for j in range(A.shape[1])] for i in range(A.shape[0])],dtype=object)
def inv9(A):
    A=np.array(A,dtype=object,copy=True); n=A.shape[0]; aug=np.column_stack([A,I9(n)])
    for c in range(n):
        q=next(i for i in range(c,n) if not fzero(aug[i,c])); aug[[c,q]]=aug[[q,c]]
        z=finv(aug[c,c]); aug[c]=[fmul(z,x) for x in aug[c]]
        for i in range(n):
            if i!=c and not fzero(aug[i,c]):
                z=aug[i,c]; aug[i]=[fsub(aug[i,j],fmul(z,aug[c,j])) for j in range(2*n)]
    return aug[:,n:]
def null_basis9(A):
    A=np.array(A,dtype=object,copy=True); m,n=A.shape; piv=[]; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if not fzero(A[i,c])),None)
        if q is None: continue
        A[[r,q]]=A[[q,r]]; z=finv(A[r,c]); A[r]=[fmul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and not fzero(A[i,c]):
                z=A[i,c]; A[i]=[fsub(A[i,j],fmul(z,A[r,j])) for j in range(n)]
        piv.append(c); r+=1
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.array([(1,0) if j==f else (0,0) for j in range(n)],dtype=object)
        for rr,c in enumerate(piv): x[c]=fneg(A[rr,f])
        out.append(x)
    return out
def sum_f9(it):
    s=(0,0)
    for x in it: s=fadd(s,x)
    return s
def mv(A,v): return np.array([sum_f9(fmul(A[i,j],v[j]) for j in range(A.shape[1])) for i in range(A.shape[0])],dtype=object)
ns1=runpy.run_path(str(ROOT/'research'/'phase2_1_invariant_space_verification_2026-09-15.py'))
basis=ns1['basis']; R4_ind=ns1['R4_ind']; selected_rows=ns1['selected_rows']
ns3=runpy.run_path(str(ROOT/'research'/'phase2_3_endH_optimized_2026-09-15.py')); N3=np.array(ns3['N'],dtype=np.int64)%3
words4=list(itertools.product(range(1,5),repeat=4)); index4={w:i for i,w in enumerate(words4)}
def vec9(A):
    v=np.array([(0,0)]*256,dtype=object)
    for w,c in A.items(): v[index4[w]]=f9(c)
    return v
# IMPORTANT: R4_ind is 256 x 5, so iterate over its transpose to obtain 5 columns.
R4cols=[np.array([f9(x) for x in col],dtype=object) for col in np.asarray(R4_ind).T]
Wcols=[vec9(a) for a in basis]
B9=np.column_stack(R4cols+Wcols); Binv9=inv9(B9[selected_rows,:])
def coords9(v): return mv(Binv9,v[selected_rows])
def apply_map_f9(A,g):
    images=[]
    for j in range(4):
        image={}
        for i in range(4):
            c=g[i,j]
            if not fzero(c): image[(i+1,)]=c
        images.append(image)
    out={}
    for word,coeff in A.items():
        cur={():f9(coeff)}
        for letter in word:
            nxt={}
            for wa,ca in cur.items():
                for wb,cb in images[letter-1].items():
                    w=wa+wb; nxt[w]=fadd(nxt.get(w,(0,0)),fmul(ca,cb))
            cur={w:c for w,c in nxt.items() if not fzero(c)}
        for w,c in cur.items(): out[w]=fadd(out.get(w,(0,0)),c)
    return {w:c for w,c in out.items() if not fzero(c)}
def W_action9(g): return np.column_stack([coords9(vec9(apply_map_f9(a,g))) for a in basis])[5:,:]
def rank3(A):
    A=np.array(A,dtype=int,copy=True)%3; m,n=A.shape; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None: continue
        A[[r,q]]=A[[q,r]]; z=1 if A[r,c]==1 else 2; A[r]=(A[r]*z)%3
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%3
        r+=1
    return r
Q=np.zeros((45,0),dtype=np.int64); rk=0
for j in range(45):
    C=np.column_stack([Q,N3[:,j]]); q=rank3(C)
    if q>rk: Q=C; rk=q
    if rk==10: break
for j in range(45):
    C=np.column_stack([Q,np.eye(45,dtype=int)[:,j]]); q=rank3(C)
    if q>rk: Q=C; rk=q
    if rk==45: break
assert rk==45
rowsQ=[]; R=np.empty((0,45),dtype=int); rr=0
for i in range(45):
    C=np.vstack([R,Q[i:i+1]]); q=rank3(C)
    if q>rr: R=C; rowsQ.append(i); rr=q
    if rr==45: break
QB9=np.array([[(int(Q[i,j])%3,0) for j in range(45)] for i in rowsQ],dtype=object); QB9inv=inv9(QB9)
Q9=np.array([[(int(Q[i,j])%3,0) for j in range(45)] for i in range(45)],dtype=object)
def quotient_action9(g): return mv(QB9inv,mm(W_action9(g),Q9)[rowsQ])[10:,:]
Pmat=np.eye(4,dtype=int)[:,[0,2,1,3]]; Pinv=Pmat.T
def root(kind,t=(1,0)):
    A=I9(4)
    if kind=='a1': A[0,1]=t; A[3,2]=fneg(t)
    elif kind=='a2': A[1,3]=t
    elif kind=='a12': A[0,3]=t; A[1,2]=t
    elif kind=='a112': A[0,2]=t
    return mm(m9(Pmat),mm(A,m9(Pinv)))
roots=[root(k) for k in ['a1','a2','a12','a112']]
EU=[quotient_action9(g) for g in roots]
fixed=null_basis9(np.vstack([msub(g,I9(35)) for g in EU])); assert len(fixed)==1; v=fixed[0]
def torus(a,b):
    d=I9(4); d[0,0]=a; d[1,1]=b; d[2,2]=finv(a); d[3,3]=finv(b)
    return mm(m9(Pmat),mm(d,m9(Pinv)))
def scalar_on_line(A,v):
    Av=mv(A,v); i=next(i for i,x in enumerate(v) if not fzero(x)); lam=fdiv(Av[i],v[i])
    assert all(fzero(fsub(Av[j],fmul(lam,v[j]))) for j in range(len(v))); return lam
chi={(a,b):scalar_on_line(quotient_action9(torus(a,b)),v) for a in F9star for b in F9star}
for a in F9star:
    for b in F9star:
        for c in F9star:
            for d in F9star:
                assert chi[(fmul(a,c),fmul(b,d))]==fmul(chi[(a,b)],chi[(c,d)])
def match_exp(e1,e2): return all(chi[(a,b)]==fmul(fpow(a,e1),fpow(b,e2)) for a in F9star for b in F9star)
matches=[(e1,e2) for e1 in range(8) for e2 in range(8) if match_exp(e1,e2)]
print('PHASE 2-14 / EXACT F9 TORUS PROBE')
print('|F9*| =',len(F9star)); print('dim E = 35'); print('dim E^{U+(F9)} =',len(fixed)); print('character matches exponents (e1,e2) mod 8 =',matches); print('EXPECTED (2,1) = (3,1) in epsilon coordinates'); print('EXPECTED character a^3 b =',(3,1) in matches); print('CERTIFICATE: exact F9 torus character law verified on all 64 torus elements.')
