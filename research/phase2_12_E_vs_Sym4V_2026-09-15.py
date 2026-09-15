"""Phase 2-12: identify E=W/U against Sym^4(V) over F_3.

Motivation:
    Phase 2-11-A proved
        0 -> M_25 -> E_35 -> Sym^2(V)_10 -> 0
    is non-split.

    The natural 4-dimensional representation V has
        dim Sym^4(V) = binom(7,4) = 35.
    For type C2 this is the Weyl-module candidate Delta(4,0).

    This script independently constructs Sym^4(V), constructs E=W/U from
    the authoritative W action and N, and computes Hom_H(Sym^4(V), E).
    A full-rank intertwiner proves E ~= Sym^4(V), without relying on a
    character table or literature identification.
"""
from pathlib import Path
import runpy
import numpy as np
from itertools import product

P=3
ROOT=Path(__file__).resolve().parents[1]

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
    free=[j for j in range(n) if j not in piv]
    for f in free:
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
    k=B.shape[1]
    rows=[]; R=np.empty((0,k),dtype=np.int64); rr=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]])
        q=rank3(C)
        if q>rr: rows.append(i); R=C; rr=q
        if rr==k: break
    assert rr==k
    # Solve B_rows * X = V_rows over F3 by Gauss-Jordan.
    A=np.column_stack([B[rows],V[rows]])%P
    m=k; rhs=V.shape[1]
    for c in range(k):
        q=next(i for i in range(c,k) if A[i,c])
        A[[c,q]]=A[[q,c]]
        if A[c,c]==2: A[c]=(2*A[c])%P
        for i in range(k):
            if i!=c and A[i,c]: A[i]=(A[i]-A[i,c]*A[c])%P
    return A[:,k:]%P

# ---------- authoritative W action and N ----------
ns1=runpy.run_path(str(ROOT/'research'/'phase2_1_invariant_space_verification_2026-09-15.py'))
A=[np.array(x,dtype=np.int64)%P for x in ns1['action_matrices']]
assert len(A)==5 and all(x.shape==(45,45) for x in A)
ns3=runpy.run_path(str(ROOT/'research'/'phase2_3_endH_optimized_2026-09-15.py'))
N=np.array(ns3['N'],dtype=np.int64)%P
assert N.shape==(45,45) and rank3(N)==10 and np.array_equal((N@N)%P,np.zeros((45,45),dtype=np.int64))

# ---------- E = W/U ----------
_,U=independent_columns(N)
assert U.shape==(45,10)
B=U.copy(); r=10
for j in range(45):
    C=np.column_stack([B,np.eye(45,dtype=np.int64)[:,j]])
    rr=rank3(C)
    if rr>r: B=C; r=rr
    if r==45: break
assert B.shape==(45,45)
E_actions=[]
for g in A:
    X=(g@B)%P
    C=coordinates_in_basis(B,X)
    assert np.array_equal((B@C)%P,X)
    E_actions.append(C[10:,10:]%P)
assert all(x.shape==(35,35) for x in E_actions)

# ---------- Sym^4(V) ----------
# Monomial basis x^a with a=(a0,a1,a2,a3), sum a_i=4.
mons=[a for a in product(range(5),repeat=4) if sum(a)==4]
# Deterministic lexicographic order.
mi={a:i for i,a in enumerate(mons)}
assert len(mons)==35

# Expand a product of four linear forms. For a source monomial x^a,
# apply g to each factor and collect coefficients.
def sym4_matrix(g):
    S=np.zeros((35,35),dtype=np.int64)
    for col,a in enumerate(mons):
        # Repeated multiplication of linear forms, represented as polynomial dict.
        poly={(0,0,0,0):1}
        for i in range(4):
            for _ in range(a[i]):
                new={}
                for exp,c0 in poly.items():
                    for j in range(4):
                        c=int(g[j,i])
                        if c:
                            e=list(exp); e[j]+=1; e=tuple(e)
                            new[e]=(new.get(e,0)+c0*c)%P
                poly=new
        for e,c in poly.items():
            S[mi[e],col]=(S[mi[e],col]+c)%P
    return S

S=[sym4_matrix(g) for g in ns1['gens']]
assert all(x.shape==(35,35) for x in S)

# ---------- Hom_H(Sym^4(V), E) ----------
# Unknown P is 35x35. Equations E_i P - P S_i = 0.
cols=[]
for q in range(35*35):
    Pmat=np.zeros((35,35),dtype=np.int64); Pmat.flat[q]=1
    blocks=[((e@Pmat-Pmat@s)%P).reshape(-1) for e,s in zip(E_actions,S)]
    cols.append(np.concatenate(blocks))
Sys=np.column_stack(cols)
r=rank3(Sys)
nullity=35*35-r
basis=null3(Sys)
assert len(basis)==nullity

full_rank=0
witness=None
for v in basis:
    Pmat=v.reshape(35,35)%P
    rr=rank3(Pmat)
    if rr>full_rank:
        full_rank=rr; witness=Pmat.copy()

print('PHASE 2-12 / E=W/U VS Sym^4(V)')
print('W dimension = 45')
print('dim U = 10')
print('dim E =',E_actions[0].shape[0])
print('Sym^4(V) dimension =',len(mons))
print('intertwiner system shape =',Sys.shape)
print('rank(E_Hom) =',r)
print('dim Hom_H(Sym^4(V), E) =',nullity)
print('maximum rank among nullspace basis maps =',full_rank)
print('FULL_RANK_INTERTWINER_FOUND =',full_rank==35)
if full_rank==35:
    print('CERTIFICATE: E ~= Sym^4(V)')
else:
    print('CERTIFICATE: no full-rank intertwiner found; identification remains unresolved')
assert full_rank==35
