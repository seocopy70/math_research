"""Phase 2-7: extract M = ker(N)/im(N) and certify its Sp4(F3)-module action.

This stage deliberately stops short of identifying M with L(2,1). It computes
an exact 25-dimensional quotient action and independent endomorphism/random
cyclic-span checks. A later stage will compare this action with an explicit
L(2,1) model.
"""
from pathlib import Path
import runpy
import numpy as np

P=3
ROOT=Path(__file__).resolve().parents[1]
ns=runpy.run_path(str(ROOT/'research/phase2_3_endH_optimized_2026-09-15.py'))
A=[np.array(x,dtype=np.int64)%P for x in ns['A_list']]
N=np.array(ns['N'],dtype=np.int64)%P

def rank3(M):
    M=np.array(M,dtype=np.int64,copy=True)%P
    m,n=M.shape; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if M[i,c]),None)
        if q is None: continue
        M[[r,q]]=M[[q,r]]
        if M[r,c]==2:M[r]=(2*M[r])%P
        for i in range(m):
            if i!=r and M[i,c]:M[i]=(M[i]-M[i,c]*M[r])%P
        r+=1
        if r==m:break
    return r

def null3(M):
    M=np.array(M,dtype=np.int64,copy=True)%P
    m,n=M.shape;piv=[];r=0
    for c in range(n):
        q=next((i for i in range(r,m) if M[i,c]),None)
        if q is None:continue
        M[[r,q]]=M[[q,r]]
        if M[r,c]==2:M[r]=(2*M[r])%P
        for i in range(m):
            if i!=r and M[i,c]:M[i]=(M[i]-M[i,c]*M[r])%P
        piv.append(c);r+=1
        if r==m:break
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64);x[f]=1
        for rr,c in enumerate(piv):x[c]=(-M[rr,f])%P
        out.append(x)
    return out

def indep_cols(M,k):
    chosen=[];B=np.empty((M.shape[0],0),dtype=np.int64);r=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]]);rr=rank3(C)
        if rr>r:chosen.append(j);B=C;r=rr
        if r==k:break
    return chosen,B

def coords(B,V):
    k=B.shape[1];rows=[];R=np.empty((0,k),dtype=np.int64);rr=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]]);q=rank3(C)
        if q>rr:rows.append(i);R=C;rr=q
        if rr==k:break
    E=np.column_stack([B[rows],np.eye(k,dtype=np.int64)])
    for c in range(k):
        q=next(i for i in range(c,k) if E[i,c])
        E[[c,q]]=E[[q,c]]
        if E[c,c]==2:E[c]=(2*E[c])%P
        for i in range(k):
            if i!=c and E[i,c]:E[i]=(E[i]-E[i,c]*E[c])%P
    return (E[:,k:]@V[rows])%P

# U=im(N), K=ker(N).
_,U=indep_cols(N,rank3(N))
Kcols=null3(N)
K=np.column_stack(Kcols)%P
assert K.shape==(45,35) and rank3(K)==35
# Put U first inside K; this is a convenient adapted basis of K.
# Express U columns in K, then extend U by independent K columns.
KU=[];B=np.empty((45,0),dtype=np.int64);r=0
for j in range(U.shape[1]):
    C=np.column_stack([B,U[:,j]])
    if rank3(C)>r:B=C;r+=1
assert r==10
for j in range(K.shape[1]):
    C=np.column_stack([B,K[:,j]])
    if rank3(C)>r:B=C;r+=1
    if r==35:break
assert B.shape==(45,35)
assert rank3(B[:,:10])==10
# quotient basis is last 25 coordinates in this adapted K basis.
MA=[]
for g in A:
    X=(g@B)%P
    C=coords(B,X)
    assert np.array_equal((B@C)%P,X)
    assert np.all(C[10:,:] >= 0)
    D=C[10:,10:]%P
    # U is invariant, so quotient action is well-defined.
    assert rank3(np.column_stack([B[:,:10], X[:,10:]]))==35
    MA.append(D)

# End_H(M): direct simultaneous commutant system, 625 unknowns.
cols=[]
for q in range(625):
    Q=np.zeros((25,25),dtype=np.int64);Q.flat[q]=1
    blocks=[((Q@x-x@Q)%P).reshape(-1) for x in MA]
    cols.append(np.concatenate(blocks))
Sys=np.column_stack(cols)
end_dim=len(null3(Sys))

# Random cyclic-span check: a proper submodule would be detected if a random
# nonzero vector generates a span of dimension <25. This is a diagnostic,
# not the primary irreducibility proof.
rng=np.random.default_rng(20260915)
def orbit_span(v):
    Bv=v.reshape(25,1)%P
    changed=True
    while changed:
        old=rank3(Bv);new=Bv.copy()
        for g in MA:new=np.column_stack([new,(g@Bv)%P])
        # independent columns only
        _,new=indep_cols(new,new.shape[1])
        Bv=new
        changed=rank3(Bv)>old
    return rank3(Bv)
spans=[]
for _ in range(32):
    v=rng.integers(0,3,size=25,dtype=np.int64)
    if not np.any(v):v[0]=1
    spans.append(orbit_span(v))

print('PHASE 2-7 / M = ker(N)/im(N)')
print('dim U =',U.shape[1])
print('dim K =',K.shape[1])
print('dim M =',25)
print('quotient action matrices =',len(MA),'of size 25x25')
print('End_H(M) dimension =',end_dim)
print('random cyclic-span dimensions (32 trials) =',spans)
print('all random spans full =',all(x==25 for x in spans))
print('INTERMEDIATE RESULT: M is a 25-dimensional H-module; endomorphism and cyclic-span certificates recorded.')
print('IDENTIFICATION M ~= L(2,1): NOT YET CLAIMED IN THIS STAGE.')
