"""O2-4: transport-independence test for the rank-10 obstruction.

Completeness note: every H-equivariant endomorphism is aI+bN. An automorphism has a!=0. After composition with tau, the nonzero scalar a only rescales D, so Im(D) is unchanged. Thus normalized representatives tau_b=tau o (I+bN), b=0,1,2, exhaust the image-level freedom.

Also checks that tau_0,tau_1,tau_2 are genuinely distinct matrices.
"""
from pathlib import Path
import runpy
import numpy as np
P=3
ROOT=Path(__file__).parent
ns_tau=runpy.run_path(str(ROOT/"A3-4-10_CANONICAL_TAU_REVALIDATION_2026-09-16.py"))
W=np.array(ns_tau["W"],dtype=np.int64)%P
Wd=np.array(ns_tau["Wd"],dtype=np.int64)%P
tau=np.array(ns_tau["tau_coord"],dtype=np.int64)%P
A_W=[np.array(A,dtype=np.int64)%P for A in ns_tau["A_W"]]
words4=ns_tau["words4"]
ns_N=runpy.run_path(str(ROOT/"phase2_3_endH_optimized_2026-09-15.py"))
N=np.array(ns_N["N"],dtype=np.int64)%P

def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A.reshape(-1,1)
    m,n=A.shape;r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i,c]),None)
        if p is None:continue
        if p!=r:A[[r,p]]=A[[p,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        rows=np.flatnonzero(A[:,c]);rows=rows[rows!=r]
        if len(rows):
            vals=A[rows,c].copy();A[rows]=(A[rows]-vals[:,None]*A[r])%P
        r+=1
        if r==m:break
    return r
words5=[(a,b,c,d,e) for a in (1,2,3,4) for b in (1,2,3,4) for c in (1,2,3,4) for d in (1,2,3,4) for e in (1,2,3,4)]
tuple_index={w:i for i,w in enumerate(words5)}
def br(v,g):
    out=np.zeros(1024,dtype=np.int64)
    for j,c in enumerate(v):
        c=int(c)%P
        if c:
            w=words4[j]
            out[tuple_index[w+(g,)]]=(out[tuple_index[w+(g,)]]+c)%P
            out[tuple_index[(g,)+w]]=(out[tuple_index[(g,)+w]]-c)%P
    return out
def obstruction_for(tau_b):
    E=(Wd@tau_b-W)%P
    D=np.vstack([np.column_stack([br(E[:,j],g) for j in range(45)]) for g in range(1,5)])%P
    return E,D
I45=np.eye(45,dtype=np.int64)
results=[];images=[];taus=[]
for b in range(3):
    S=(I45+b*N)%P
    S_inv=(I45-b*N)%P
    assert np.array_equal((S@S_inv)%P,I45)
    assert all(np.array_equal((S@A)%P,(A@S)%P) for A in A_W)
    tau_b=(tau@S)%P;taus.append(tau_b)
    E,D=obstruction_for(tau_b)
    assert rank3(tau_b)==45
    results.append((b,rank3(E),rank3(D)));images.append(D)
distinct=[]
for i in range(3):
    for j in range(i+1,3):
        diff=(taus[i]-taus[j])%P
        distinct.append((i,j,rank3(diff),bool(np.any(diff))))
all_distinct=all(x[3] for x in distinct)
pairwise=[[rank3(np.column_stack([images[i],images[j]])) for j in range(3)] for i in range(3)]
all_equal=all(pairwise[i][j]==10 for i in range(3) for j in range(3))
print("O2-4 TRANSPORT-INDEPENDENCE / QUOTIENT-FIXED TEST")
print("End_H(W)=F3[I,N], N^2=0, rank(N)=10")
print("Every equivariant automorphism=aI+bN, a!=0; normalize a=1")
print("Nonzero scalar a only rescales D, hence does not change Im(D).")
print("tau_b=tau o(I+bN), b=0,1,2 exhaust normalized image-level freedom.")
print("N nonzero =",bool(np.any(N)))
for i,j,r,nz in distinct: print(f"tau_{i} != tau_{j}: {nz}; rank(tau_{i}-tau_{j})={r}")
print("all three transports genuinely distinct =",all_distinct)
for b,re,rd in results: print(f"b={b}: rank(tau_b-id)={re}, rank(D_b)={rd}")
print("pairwise join ranks of obstruction images:");[print(row) for row in pairwise]
print("all three obstruction images equal =",all_equal)
assert all_distinct and all_equal and all(rd==10 for _,_,rd in results)
print("O2-4 RESULT = PASS")
print("The rank-10 obstruction image is unchanged across all normalized quotient-fixed H-equivariant transports.")
