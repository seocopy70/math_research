"""Phase 2-6 / A: test U = im(N) against L(2,0) via Sym^2 of the natural module.

Key simplification:
For Sp4 in characteristic 3, Delta(2,0) is 10-dimensional and simple,
so Delta(2,0)=L(2,0).  It is the symmetric-square highest-weight module
Sym^2(V), where V is the natural 4-dimensional module.  Therefore we can
construct the SAME five finite-group generators directly from the 4x4
transvections used in Phase 2-1, without first converting WeylModules
Chevalley matrices to group matrices.

The decisive test is a simultaneous intertwiner
    P A_i(U) = A_i(Sym^2 V) P,
with rank(P)=10.
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
        if M[r,c]==2: M[r]=(2*M[r])%P
        for i in range(m):
            if i!=r and M[i,c]: M[i]=(M[i]-M[i,c]*M[r])%P
        r+=1
        if r==m: break
    return r

def null3(M):
    M=np.array(M,dtype=np.int64,copy=True)%P
    m,n=M.shape; piv=[]; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if M[i,c]),None)
        if q is None: continue
        M[[r,q]]=M[[q,r]]
        if M[r,c]==2: M[r]=(2*M[r])%P
        for i in range(m):
            if i!=r and M[i,c]: M[i]=(M[i]-M[i,c]*M[r])%P
        piv.append(c); r+=1
        if r==m: break
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64); x[f]=1
        for rr,c in enumerate(piv): x[c]=(-M[rr,f])%P
        out.append(x)
    return out

def indep_cols(M,k):
    chosen=[]; B=np.empty((M.shape[0],0),dtype=np.int64); r=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]])
        rr=rank3(C)
        if rr>r: chosen.append(j); B=C; r=rr
        if r==k: break
    return chosen,B

def coords(B,V):
    # Find an invertible k-row minor and solve all columns.
    k=B.shape[1]; rows=[]; R=np.empty((0,k),dtype=np.int64); rr=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]])
        q=rank3(C)
        if q>rr: rows.append(i); R=C; rr=q
        if rr==k: break
    E=np.column_stack([B[rows],np.eye(k,dtype=np.int64)])
    for c in range(k):
        q=next(i for i in range(c,k) if E[i,c])
        E[[c,q]]=E[[q,c]]
        if E[c,c]==2:E[c]=(2*E[c])%P
        for i in range(k):
            if i!=c and E[i,c]:E[i]=(E[i]-E[i,c]*E[c])%P
    return (E[:,k:]@V[rows])%P

# U = im(N)
idx,U=indep_cols(N,10)
assert rank3(U)==10
UA=[]
for g in A:
    X=(g@U)%P
    C=coords(U,X)
    assert np.array_equal((U@C)%P,X)
    UA.append(C)

# Natural 4D generators are exactly Phase 2-1 transvections.
# J is the Phase 2-1 symplectic matrix; g=I+v(Jv)^T.
J=np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]],dtype=np.int64)%P
vecs=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,0,1,0)]
G=[(np.eye(4,dtype=np.int64)+np.outer(np.array(v),J@np.array(v)%P))%P for v in vecs]

# Sym^2(V): basis x1^2,x1x2,x1x3,x1x4,x2^2,x2x3,x2x4,x3^2,x3x4,x4^2.
pairs=[(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)]
def sym2_matrix(g):
    # Column for x_a x_b is product of the corresponding linear images.
    S=np.zeros((10,10),dtype=np.int64)
    for j,(a,b) in enumerate(pairs):
        # image of xa is sum_i g[i,a] xi; similarly xb.
        for i in range(4):
            for k in range(4):
                c=int(g[i,a])*int(g[k,b])%P
                if not c: continue
                if i>k: key=(k,i)
                else: key=(i,k)
                S[pairs.index(key),j]=(S[pairs.index(key),j]+c)%P
    return S

L20=[sym2_matrix(g) for g in G]

# Solve simultaneous intertwiner equations for P (10x10).
cols=[]
for q in range(100):
    E=np.zeros((100,100),dtype=np.int64); Q=np.zeros((10,10),dtype=np.int64); Q.flat[q]=1
    blocks=[((Q@u-l@Q)%P).reshape(-1) for u,l in zip(UA,L20)]
    cols.append(np.concatenate(blocks))
Sys=np.column_stack(cols)
nb=null3(Sys)
full=None
for x in nb:
    Q=x.reshape(10,10)%P
    if rank3(Q)==10: full=Q; break

print('PHASE 2-6 / A')
print('rank(N)=',rank3(N),' dim(U)=',U.shape[1])
print('U restricted action: 5 matrices of size 10x10')
print('L(2,0) model: Sym^2(natural), 5 matrices of size 10x10')
print('intertwiner system shape=',Sys.shape)
print('dim Hom_H(U,L(2,0))=',len(nb))
print('full-rank intertwiner found=',full is not None)
if full is not None: print('RESULT: U is isomorphic to L(2,0)=Sym^2(V).')
else: print('RESULT: identification not yet established; inspect Hom-space.')
