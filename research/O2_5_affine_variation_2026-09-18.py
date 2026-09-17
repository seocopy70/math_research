"""O2-5: affine variation of the obstruction across the admissible tau-family.

B1 fixes tau pointwise on I_W, so the admissible family is the affine line

tau_b = tau o (I + bN),  b in F3.

This test deliberately does NOT introduce a scalar a=2 transport: scalar
multiplication of tau violates the frozen pointwise constraint tau I_W=I_Wd.

Checks:
A) D_1-D_0 = D_2-D_1 and D_2-D_0 = 2(D_1-D_0).
B) Delta D = D_1-D_0 has rank 10.
C) Im(Delta D) is stable under the same H-action rho_T used for D_stack.
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
gens=[np.array(g,dtype=np.int64)%P for g in ns_tau["gens"]]
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
idx5={w:i for i,w in enumerate(words5)}

def br(v,g):
    out=np.zeros(1024,dtype=np.int64)
    for j,c in enumerate(v):
        c=int(c)%P
        if c:
            w=words4[j]
            out[idx5[w+(g,)]]=(out[idx5[w+(g,)]]+c)%P
            out[idx5[(g,)+w]]=(out[idx5[(g,)+w]]-c)%P
    return out

def obstruction_for(tau_b):
    E=(Wd@tau_b-W)%P
    D=np.vstack([np.column_stack([br(E[:,j],g) for j in range(45)]) for g in range(1,5)])%P
    return E,D

def inverse3(M):
    M=np.array(M,dtype=np.int64)%P;n=M.shape[0]
    A=np.concatenate([M,np.eye(n,dtype=np.int64)],axis=1)
    for c in range(n):
        p=next((i for i in range(c,n) if A[i,c]),None)
        if p is None: raise RuntimeError('singular F3 matrix')
        if p!=c:A[[c,p]]=A[[p,c]]
        if A[c,c]==2:A[c]=(2*A[c])%P
        for i in range(n):
            if i!=c and A[i,c]:A[i]=(A[i]-A[i,c]*A[c])%P
    return A[:,n:]

# Build degree-5 ambient action A5(g) on the 4^5 word basis.
def word_image(word,g):
    cur={():1}
    for letter in word:
        image={}
        for i in range(4):
            c=int(g[i,letter-1])%P
            if c:image[(i+1,)]=c
        nxt={}
        for a,ca in cur.items():
            for b,cb in image.items():
                w=a+b;nxt[w]=(nxt.get(w,0)+ca*cb)%P
        cur={w:c for w,c in nxt.items() if c}
    return cur

def degree5_action(g):
    A=np.zeros((1024,1024),dtype=np.int64)
    for j,w in enumerate(words5):
        for ww,c in word_image(w,g).items():A[idx5[ww],j]=(A[idx5[ww],j]+c)%P
    return A

def inv_transpose(g):
    return inverse3(g).T%P

def rho_T_apply(D,g):
    """Apply rho_T(g)=g^{-T} tensor A5(g) to a stacked 4-block output."""
    A5=degree5_action(g)
    T=inv_transpose(g)
    X=D.reshape(4,1024,-1)
    Y=np.zeros_like(X)
    for i in range(4):
        for j in range(4):
            if T[i,j]:Y[i]=(Y[i]+T[i,j]*(A5@X[j]))%P
    return Y.reshape(4096,-1)%P

I45=np.eye(45,dtype=np.int64)
Ds=[]
for b in range(3):
    S=(I45+b*N)%P
    S_inv=(I45-b*N)%P
    assert np.array_equal((S@S_inv)%P,I45)
    assert all(np.array_equal((S@A)%P,(A@S)%P) for A in A_W)
    tau_b=(tau@S)%P
    # A3-4-10 exports the authoritative common intersection basis I_coord.
    # Since canonical tau fixes I pointwise, every admissible tau_b must fix it pointwise too.
    assert np.array_equal((tau_b@ns_tau["I_coord"])%P,ns_tau["I_coord"]%P)
    E,D=obstruction_for(tau_b)
    assert rank3(tau_b)==45
    assert rank3(D)==10
    Ds.append(D)

D0,D1,D2=Ds
Delta=(D1-D0)%P
left=(D1-D0)%P
right=(D2-D1)%P
affine_step=np.array_equal(left,right)
affine_span=np.array_equal((D2-D0)%P,(2*Delta)%P)
rank_delta=rank3(Delta)

# C: test H-stability of Im(Delta) under the rho_T action.
stable=[]
for g in gens:
    moved=rho_T_apply(Delta,g)
    stable.append(rank3(np.column_stack([Delta,moved]))==rank_delta)

print("O2-5 AFFINE VARIATION OF ADMISSIBLE TRANSPORT FAMILY")
print("B1 constraint = tau|I_W is pointwise fixed identification")
print("Admissible family = tau o(I+bN), b=0,1,2")
print("Scalar a=2 transport = NOT TESTED (inadmissible under B1 constraint)")
print("rank(D_0),rank(D_1),rank(D_2) =",[rank3(D) for D in Ds])
print("AFFINE_IDENTITY_D1_MINUS_D0_EQUALS_D2_MINUS_D1 =",affine_step)
print("AFFINE_IDENTITY_D2_MINUS_D0_EQUALS_2_DELTA =",affine_span)
print("DELTA_D_RANK =",rank_delta)
print("DELTA_D_SHAPE =",Delta.shape)
print("DELTA_O_DIM =",rank_delta)
for i,s in enumerate(stable):print(f"DELTA_O_H_STABLE_g{i+1} =",s)
print("DELTA_O_H_STABLE_ALL_5 =",all(stable))
assert affine_step and affine_span
assert rank_delta==10
assert all(stable)
print("O2-5 RESULT = PASS")
