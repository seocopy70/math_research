"""Phase 2-4C: decisive irreducibility test for M=ker(N)/im(N).

Computes the associative algebra A=F_3[A1,...,A5] exactly. If dim A=25^2,
then A=M_25(F_3), which proves M irreducible (indeed absolutely irreducible).
If dim A<625, the script deliberately reports the result as unresolved and
runs deterministic cyclic-submodule diagnostics only.
"""
from pathlib import Path
import runpy
import numpy as np
P=3; nM=25
ns=runpy.run_path(str(Path(__file__).with_name("phase2_4B_middle_quotient_2026-09-15.py")))
G=[np.array(x,dtype=np.int64)%P for x in ns["M_actions"]]
assert len(G)==5 and all(x.shape==(25,25) for x in G)

def r3(M):
    M=np.array(M,dtype=np.int64,copy=True)%P
    if M.ndim==1: M=M[:,None]
    m,n=M.shape; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if M[i,c]),None)
        if p is None: continue
        if p!=r: M[[r,p]]=M[[p,r]]
        if M[r,c]==2: M[r]=(2*M[r])%P
        rows=np.flatnonzero(M[:,c]); rows=rows[rows!=r]
        if len(rows):
            vals=M[rows,c].copy(); M[rows]=(M[rows]-vals[:,None]*M[r])%P
        r+=1
        if r==m: break
    return r

def add_basis(B,X):
    X=np.array(X,dtype=np.int64)%P
    old=np.column_stack([Y.reshape(-1) for Y in B]) if B else np.empty((625,0),dtype=np.int64)
    ro=r3(old); rn=r3(np.column_stack([old,X.reshape(-1)]))
    if rn>ro: B.append(X); return True
    return False

# Exact closure under multiplication by the five generators.
B=[np.eye(nM,dtype=np.int64)%P]
for g in G: add_basis(B,g)
qi=0
while qi<len(B) and len(B)<625:
    X=B[qi]; qi+=1
    for g in G:
        add_basis(B,(X@g)%P)
        if len(B)==625: break
        add_basis(B,(g@X)%P)
        if len(B)==625: break
alg_dim=len(B)
print("PHASE 2-4C")
print("dim M =",nM)
print("generated associative algebra dimension =",alg_dim)
print("full matrix algebra dimension =",625)
if alg_dim==625:
    print("RESULT = PROOF")
    print("A=M_25(F_3); therefore M has no nonzero proper invariant subspace.")
    print("M is irreducible, in fact absolutely irreducible.")
else:
    print("RESULT = NOT YET DECISIVE")
    print("A is a proper subalgebra; this alone does not prove reducibility.")

# Reproducible cyclic-submodule diagnostics.
def cyclic_dim(v):
    V=[]; q=[np.array(v,dtype=np.int64)%P]; rank=0
    while q:
        x=q.pop(); nr=r3(np.column_stack(V+[x])) if V else r3(x[:,None])
        if nr<=rank: continue
        V.append(x); rank=nr
        if rank==nM: return nM
        for g in G: q.append((g@x)%P)
    return rank
probes=[]
for i in range(nM):
    e=np.zeros(nM,dtype=np.int64); e[i]=1; probes.append(e)
for i in range(nM):
    e=np.zeros(nM,dtype=np.int64); e[i]=1; e[(i+1)%nM]=1; probes.append(e)
for i in range(nM-1):
    e=np.zeros(nM,dtype=np.int64); e[i]=1; e[i+1]=2; probes.append(e)
dims=[cyclic_dim(v) for v in probes]
print("probe count =",len(probes))
print("probe dimension distribution =",{d:dims.count(d) for d in sorted(set(dims))})
print("probe minimum dimension =",min(dims))
print("probe maximum dimension =",max(dims))
print("STATUS=IRREDUCIBLE_PROVED_BY_FULL_MATRIX_ALGEBRA" if alg_dim==625 else "STATUS=UNRESOLVED_AFTER_ALGEBRA_TEST")
