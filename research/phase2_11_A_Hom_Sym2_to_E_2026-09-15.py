"""Phase 2-11-A: compute Hom_H(Sym^2(V), E) for E=W/U over F_3.

Purpose:
    E = W/U has dimension 35, with known submodule M=ker(N)/im(N)
    of dimension 25 and quotient E/M ~= Sym^2(V) of dimension 10.

    The first split/non-split test is Hom_H(Sym^2(V), E).
    If this Hom-space is zero, the exact sequence
        0 -> M -> E -> Sym^2(V) -> 0
    is necessarily non-split.

All arithmetic is exact over F_3. This script reuses the authoritative
Phase 2-1 action matrices and Phase 2-3 endomorphism N, then independently
constructs the quotient W/U and the Sym^2 natural representation.
"""
from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).resolve().parents[1]

# ---------- exact linear algebra over F_3 ----------
def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1: A=A.reshape(-1,1)
    m,n=A.shape; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None: continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2: A[r]=(2*A[r])%P
        rows=np.flatnonzero(A[:,c]); rows=rows[rows!=r]
        if len(rows):
            vals=A[rows,c].copy()
            A[rows]=(A[rows]-vals[:,None]*A[r])%P
        r+=1
        if r==m: break
    return r

def null3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    m,n=A.shape; R=A.copy(); piv=[]; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if R[i,c]),None)
        if q is None: continue
        R[[r,q]]=R[[q,r]]
        if R[r,c]==2: R[r]=(2*R[r])%P
        rows=np.flatnonzero(R[:,c]); rows=rows[rows!=r]
        if len(rows):
            vals=R[rows,c].copy()
            R[rows]=(R[rows]-vals[:,None]*R[r])%P
        piv.append(c); r+=1
        if r==m: break
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64); x[f]=1
        for rr,c in enumerate(piv): x[c]=(-R[rr,f])%P
        out.append(x)
    return out

def independent_columns(M):
    chosen=[]; B=np.empty((M.shape[0],0),dtype=np.int64); r=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]])
        rr=rank3(C)
        if rr>r:
            chosen.append(j); B=C; r=rr
    return chosen,B

def coordinates_in_basis(B,V):
    """Coordinates of columns V in a full-column-rank basis B."""
    k=B.shape[1]
    rows=[]; R=np.empty((0,k),dtype=np.int64); rr=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]])
        q=rank3(C)
        if q>rr: rows.append(i); R=C; rr=q
        if rr==k: break
    assert rr==k
    E=np.column_stack([B[rows],np.eye(k,dtype=np.int64)])
    for c in range(k):
        q=next(i for i in range(c,k) if E[i,c])
        E[[c,q]]=E[[q,c]]
        if E[c,c]==2: E[c]=(2*E[c])%P
        for i in range(k):
            if i!=c and E[i,c]: E[i]=(E[i]-E[i,c]*E[c])%P
    return (E[:,k:]@V[rows])%P

# ---------- authoritative W action and N ----------
ns1=runpy.run_path(str(ROOT/'research'/'phase2_1_invariant_space_verification_2026-09-15.py'))
A=[np.array(x,dtype=np.int64)%P for x in ns1['action_matrices']]
G=[np.array(x,dtype=np.int64)%P for x in ns1['gens']]
assert len(A)==5 and all(x.shape==(45,45) for x in A)
ns3=runpy.run_path(str(ROOT/'research'/'phase2_3_endH_optimized_2026-09-15.py'))
N=np.array(ns3['N'],dtype=np.int64)%P
assert N.shape==(45,45) and rank3(N)==10 and np.array_equal((N@N)%P,np.zeros((45,45),dtype=np.int64))

# ---------- U = im(N), E = W/U ----------
_,U=independent_columns(N)
assert U.shape==(45,10)
# Extend U to a basis of W.
B=U.copy(); r=10
for j in range(45):
    C=np.column_stack([B,np.eye(45,dtype=np.int64)[:,j]])
    rr=rank3(C)
    if rr>r: B=C; r=rr
    if r==45: break
assert B.shape==(45,45)
# Coordinates of A_i action in the adapted basis U + complement.
E_actions=[]
for g in A:
    X=(g@B)%P
    C=coordinates_in_basis(B,X)
    assert np.array_equal((B@C)%P,X)
    # U is invariant, so quotient action is lower-right 35x35 block.
    assert rank3(np.column_stack([B[:,:10],X[:,10:]]))==45
    E_actions.append(C[10:,10:]%P)
assert all(x.shape==(35,35) for x in E_actions)

# ---------- natural 4D symplectic generators and Sym^2(V) ----------
# Basis is monomials e_i e_j with 0<=i<=j<4.
pairs=[(i,j) for i in range(4) for j in range(i,4)]
pair_index={p:k for k,p in enumerate(pairs)}

def sym2_matrix(g):
    S=np.zeros((10,10),dtype=np.int64)
    for col,(i,j) in enumerate(pairs):
        # (g e_i)(g e_j), with symmetric commutative monomials.
        for a in range(4):
            for b in range(4):
                c=int(g[a,i])*int(g[b,j])
                if c:
                    p=(a,b) if a<=b else (b,a)
                    S[pair_index[p],col]=(S[pair_index[p],col]+c)%P
    return S
S=[sym2_matrix(g) for g in G]
assert all(x.shape==(10,10) for x in S)

# ---------- Hom_H(Sym^2 V, E) ----------
# Unknown P is 35x10. Equation E_i P - P S_i = 0.
# Build scalar system by basis matrices of Hom(Sym2,E).
cols=[]
for q in range(35*10):
    Pmat=np.zeros((35,10),dtype=np.int64); Pmat.flat[q]=1
    blocks=[((e@Pmat-Pmat@s)%P).reshape(-1) for e,s in zip(E_actions,S)]
    cols.append(np.concatenate(blocks))
Sys=np.column_stack(cols)
r=rank3(Sys)
nullity=35*10-r
basis=null3(Sys)
assert len(basis)==nullity

full_rank=0
for v in basis:
    Pmat=v.reshape(35,10)%P
    full_rank=max(full_rank,rank3(Pmat))

print('PHASE 2-11-A / Hom_H(Sym^2(V), E=W/U)')
print('W dimension = 45')
print('dim U =',U.shape[1])
print('dim E =',E_actions[0].shape[0])
print('Sym^2(V) dimension =',S[0].shape[0])
print('intertwiner system shape =',Sys.shape)
print('rank(E_Hom) =',r)
print('dim Hom_H(Sym^2(V), E) =',nullity)
print('maximum rank among nullspace basis maps =',full_rank)
print('CONCLUSION: Hom = 0 => extension non-split' if nullity==0 else 'CONCLUSION: Hom is nonzero; split test requires projection/section check')
assert (nullity==0 and full_rank==0) or (nullity>0 and full_rank>0)
