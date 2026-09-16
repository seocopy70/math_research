import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Exact rank/nullspace/coordinate helpers over F_3.
def rank3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape;r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i,c]),None)
        if q is None:continue
        A[[r,q]]=A[[q,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]:A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m:break
    return r

def null3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    m,n=A.shape;R=A.copy();piv=[];r=0
    for c in range(n):
        q=next((i for i in range(r,m) if R[i,c]),None)
        if q is None:continue
        R[[r,q]]=R[[q,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c);r+=1
        if r==m:break
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64);x[f]=1
        for rr,c in enumerate(piv):x[c]=(-R[rr,f])%P
        out.append(x)
    return out

def left_inverse(B):
    B=np.array(B,dtype=np.int64)%P
    k=B.shape[1]; rows=[];R=np.empty((0,k),dtype=np.int64);r=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]]);q=rank3(C)
        if q>r:
            rows.append(i);R=C;r=q
            if r==k:break
    assert r==k
    E=np.column_stack([R,np.eye(k,dtype=np.int64)])
    for c in range(k):
        q=next(i for i in range(c,k) if E[i,c]);E[[c,q]]=E[[q,c]]
        if E[c,c]==2:E[c]=(2*E[c])%P
        for i in range(k):
            if i!=c and E[i,c]:E[i]=(E[i]-E[i,c]*E[c])%P
    return rows,E[:,k:]

def coords(B,V):
    rows,L=left_inverse(B)
    return (L@np.array(V,dtype=np.int64)[rows])%P

def independent_columns(M,target=None):
    M=np.array(M,dtype=np.int64)%P
    B=np.empty((M.shape[0],0),dtype=np.int64);r=0;idx=[]
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]])
        q=rank3(C)
        if q>r:
            B=C;r=q;idx.append(j)
            if target is not None and r==target:break
    if target is not None:assert r==target
    return idx,B

def intertwiner_data(A_src,A_tgt):
    n=A_src[0].shape[0]
    cols=[]
    for q in range(n*n):
        Q=np.zeros((n,n),dtype=np.int64);Q.flat[q]=1
        blocks=[((Q@a-b@Q)%P).reshape(-1) for a,b in zip(A_src,A_tgt)]
        cols.append(np.concatenate(blocks))
    Sys=np.column_stack(cols)
    nb=null3(Sys);max_rank=0;full=None
    for x in nb:
        Q=x.reshape((n,n))%P;rr=rank3(Q);max_rank=max(max_rank,rr)
        if rr==n:
            full=Q;break
    return len(nb),max_rank,full

# Reuse the independently verified A3-4-10 and A3-4-5 infrastructure.
ns=runpy.run_path(ROOT+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3_ref=ns['rank3']
W=np.array(ns['W'],dtype=np.int64)%P
I_W=np.array(ns['I_W'],dtype=np.int64)%P
K_coord=np.array(ns['K_coord'],dtype=np.int64)%P
A_W=[np.array(a,dtype=np.int64)%P for a in ns['A_W']]
D_tau=np.array(ns['D'],dtype=np.int64)%P
B_W=[np.array(B,dtype=np.int64)%P for B in ns['B_W']]
B_Wd=[np.array(B,dtype=np.int64)%P for B in ns['B_Wd']]
X=np.array(ns['X_intertwiner'],dtype=np.int64)%P

# Reuse the verified control map Delta_u from A3-4-12.
ns12=runpy.run_path(ROOT+'A3-4-12_IMAGE_INTERSECTION_DELTA_U_DELTA_TAU_2026-09-16.py')
D_u=np.array(ns12['D_u'],dtype=np.int64)%P
assert D_tau.shape==(4096,45) and D_u.shape==(4096,45)
assert rank3(D_tau)==45 and rank3(D_u)==10

# ------------------------------------------------------------------
# Step 1: B/A really has dimension 35.
# Choose 10 independent columns of D_u and extend them by 35 columns
# of D_tau. The latter give quotient representatives for B/A.
# ------------------------------------------------------------------
idxA,A_basis=independent_columns(D_u,10)
assert A_basis.shape==(4096,10)

Q_idx=[]
C=A_basis.copy();r=10
for j in range(45):
    T=np.column_stack([C,D_tau[:,j]])
    rr=rank3(T)
    if rr>r:
        C=T;r=rr;Q_idx.append(j)
        if r==45:break
assert len(Q_idx)==35 and rank3(C)==45
B_over_A_basis=D_tau[:,Q_idx]
assert rank3(np.column_stack([A_basis,B_over_A_basis]))==45

# Coordinate map relative to [A_basis | B/A representatives].
# The quotient coordinate of a vector in B is its last 35 coordinates.
C_rows,C_L=left_inverse(C)

def quotient_coords_in_B_over_A(V):
    full=(C_L@np.array(V,dtype=np.int64)[C_rows])%P
    return full[10:,:]

# ------------------------------------------------------------------
# Step 2: Compute the H-action on B/A.
# Rather than build a 4096x4096 matrix, use the natural action on
# Hom(V,L5). A vector F is a 4x1024 block matrix; under g it becomes
#   (g.L5) F (g^{-1}.V).
# The degree-5 target action is constructed by substituting g(X_i)
# into each associative word.
# ------------------------------------------------------------------
ns1=runpy.run_path(ROOT+'phase2_1_invariant_space_verification_2026-09-15.py')
gens=ns1['gens']; apply_linear_map=ns1['apply_linear_map']; index4=ns1['index4']
from itertools import product
words5=list(product((1,2,3,4),repeat=5));index5={w:i for i,w in enumerate(words5)}

def vec5(A):
    v=np.zeros(1024,dtype=np.int64)
    for w,c in A.items():v[index5[w]]=c%P
    return v

def hom_action(F,g):
    # F has shape (4096,), blocks F_i: L5, i=0..3.
    blocks=np.array(F,dtype=np.int64).reshape(4,1024)
    # Target action on L5.
    T5=np.zeros((1024,1024),dtype=np.int64)
    for j,w in enumerate(words5):
        A={(w):1}
        out=apply_linear_map(A,g)
        for ww,c in out.items():T5[index5[ww],j]=(T5[index5[ww],j]+c)%P
    # g^{-1} on V; for symplectic g, compute exact inverse over F3.
    aug=np.concatenate([g.copy()%P,np.eye(4,dtype=np.int64)],axis=1)
    for c in range(4):
        q=next(i for i in range(c,4) if aug[i,c]);aug[[c,q]]=aug[[q,c]]
        if aug[c,c]==2:aug[c]=(2*aug[c])%P
        for i in range(4):
            if i!=c and aug[i,c]:aug[i]=(aug[i]-aug[i,c]*aug[c])%P
    gi=aug[:,4:]
    out_blocks=np.zeros((4,1024),dtype=np.int64)
    for i in range(4):
        for j in range(4):
            out_blocks[i]=(out_blocks[i]+int(gi[j,i])*((T5@blocks[j])%P))%P
    return out_blocks.reshape(-1)

A_Bquot=[]
for g in gens:
    cols=[]
    for j in range(35):
        y=hom_action(B_over_A_basis[:,j],g)
        # H-invariance of B: y must lie in B=Im Delta_tau.
        z=quotient_coords_in_B_over_A(y.reshape(-1,1))
        recon=(C@np.vstack([np.zeros((10,1),dtype=np.int64),z]))%P
        # Reconstruction is only modulo A, so compare y-recon in A.
        assert rank3(np.column_stack([A_basis,(y-recon)]))==10
        cols.append(z[:,0])
    A_Bquot.append(np.column_stack(cols)%P)
assert all(rank3(a)==35 for a in A_Bquot)

# ------------------------------------------------------------------
# Step 3: H-action on K=I. Since A3-4-12.5b established I=K
# as ambient subspaces, use K_coord as the actual 35D basis.
# ------------------------------------------------------------------
A_K=[]
for A in A_W:
    y=(A@K_coord)%P
    c=coords(K_coord,y)
    assert np.array_equal((K_coord@c)%P,y)
    A_K.append(c)
assert all(a.shape==(35,35) for a in A_K)

# ------------------------------------------------------------------
# Step 4: Actual module comparison, not dimension matching.
# Solve P A_Bquot = A_K P for all five generators and require rank 35.
# ------------------------------------------------------------------
hom_dim,max_rank,P_BA_K=intertwiner_data(A_Bquot,A_K)
FULL_RANK_INTERTWINER = P_BA_K is not None and rank3(P_BA_K)==35

# Independent sanity checks: quotient dimension and exact I=K.
assert rank3(I_W)==35 and rank3(K_coord)==35
# I=K ambient is checked by rank of concatenation in W-coordinates.
assert rank3(np.column_stack([I_W,K_coord]))==35

print('A3-4-13 / B/A VS K H-MODULE COMPARISON')
print('ambient Hom(V,L5) dimension =',4096)
print('dim B = rank Delta_tau =',rank3(D_tau))
print('dim A = rank Delta_u =',rank3(D_u))
print('dim(B+A) =',rank3(np.column_stack([D_tau,D_u])))
print('dim(B/A) =',len(Q_idx))
print('dim K =',rank3(K_coord))
print('I = K ambient check =',rank3(np.column_stack([I_W,K_coord]))==35)
print('number of B/A quotient representatives =',len(Q_idx))
print('dim Hom_H(B/A,K) =',hom_dim)
print('maximum intertwiner rank =',max_rank)
print('FULL_RANK_INTERTWINER_FOUND =',FULL_RANK_INTERTWINER)

if FULL_RANK_INTERTWINER:
    print('RESULT: B/A is H-isomorphic to K=I.')
else:
    print('RESULT: B/A is NOT H-isomorphic to K by the computed intertwiner test.')

assert len(Q_idx)==35
assert FULL_RANK_INTERTWINER
print('ALL A3-4-13 CHECKS COMPLETED')
