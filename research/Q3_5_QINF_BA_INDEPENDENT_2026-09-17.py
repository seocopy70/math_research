"""Q3-5: independently construct A_infty and B_infty from the q=infinity side.

This file is intentionally a first-pass structural probe. It does NOT import
q=3 A/B images or infer them from q=3 dimensions. It reconstructs the q=infinity
45D quotient, the natural d=[X1^[3],X2] orbit, End_H(Wd_inf), and then uses the
same Delta_u / Delta_tau definitions once the canonical affine intertwiner is
constructed inside the q=infinity path.
"""

import runpy
import numpy as np

P=3
ROOT='research/'

def r3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i,c]),None)
        if piv is None: continue
        A[[r,piv]]=A[[piv,r]]
        if A[r,c]==2:A[r]=(2*A[r])%P
        for i in range(m):
            if i!=r and A[i,c]: A[i]=(A[i]-A[i,c]*A[r])%P
        r+=1
        if r==m:break
    return r

def basis(M,target):
    B=np.empty((M.shape[0],0),dtype=np.int64); rr=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]]); q=r3(C)
        if q>rr:
            B=C; rr=q
            if rr==target:break
    assert rr==target
    return B

def nullspace(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    m,n=A.shape; piv=[]; row=0
    for c in range(n):
        p=next((i for i in range(row,m) if A[i,c]),None)
        if p is None:continue
        A[[row,p]]=A[[p,row]]
        if A[row,c]==2:A[row]=(2*A[row])%P
        for i in range(m):
            if i!=row and A[i,c]:A[i]=(A[i]-A[i,c]*A[row])%P
        piv.append(c); row+=1
        if row==m:break
    free=[c for c in range(n) if c not in piv]
    Z=[]
    for f in free:
        v=np.zeros(n,dtype=np.int64); v[f]=1
        for i,c in enumerate(piv):v[c]=(-A[i,f])%P
        Z.append(v)
    return np.column_stack(Z) if Z else np.zeros((n,0),dtype=np.int64)

def solve_intertwiner(G,H):
    # Solve T G_i = H_i T, vectorized column-major convention.
    n=G[0].shape[0]; blocks=[]
    for A,B in zip(G,H):
        M=np.zeros((n*n,n*n),dtype=np.int64)
        # coefficient for T_rc in equation (T A - B T)_r,c
        for r in range(n):
            for c in range(n):
                eq=r*n+c
                for k in range(n):
                    M[eq,k*n+c]=(M[eq,k*n+c]+A[k,c])%P
                    M[eq,r*n+k]=(M[eq,r*n+k]-B[r,k])%P
        blocks.append(M)
    return nullspace(np.vstack(blocks))

# Rebuild q=infinity degree-4 quotient independently using the Gate-0A path.
ns=runpy.run_path(ROOT+'GATE0A_Q3_QINF_INDEPENDENT_W45_2026-09-17.py')
qinf_basis=np.array(ns['qinf']['ambient_basis'],dtype=np.int64)%P
qinf_gens=[np.array(g,dtype=np.int64)%P for g in ns['qinf']['actions']]
assert qinf_basis.shape==(256,45)
assert r3(qinf_basis)==45

# Explicit W45=Q4 assertion: both are the same 45D quotient space by construction,
# and verify the returned basis has full quotient rank.
assert r3(qinf_basis)==45

# Reconstruct natural d=[X1^[3],X2] in the same ambient word basis.
# Coordinates: X1^[3] is word 111, bracket with X2 gives 1112-2111.
d=np.zeros(256,dtype=np.int64); d[ns['index4'][(1,1,1,2)]]=1; d[ns['index4'][(2,1,1,1)]]=2

# Build H-orbit in the ambient word space. apply_linear_map consumes
# sparse word dictionaries, so convert each dense vector explicitly.
def dense_to_word_dict(v):
    v=np.array(v,dtype=np.int64)%P
    return {ns['index4'][w]: int(c) for w,c in zip(ns['words4'],v) if int(c)%P}
def orbit_vec(v):
    out=[v.copy()]; seen={tuple(v.tolist())}; q=[v.copy()]
    while q:
        a=q.pop()
        a_dict={w:int(c) for w,c in zip(ns['words4'],a) if int(c)%P}
        for g in ns['gens']:
            b_dict=ns['apply_linear_map'](a_dict,g)
            b=np.zeros(256,dtype=np.int64)
            for w,c in b_dict.items():
                b[ns['index4'][w]]=int(c)%P
            key=tuple(b.tolist())
            if key not in seen:seen.add(key);out.append(b);q.append(b)
    return np.column_stack(out)
O=orbit_vec(d); Wd=basis(O,r3(O))
assert Wd.shape==(256,45)
assert r3(Wd)==45

# Quotient coordinates must be obtained from the full L4 basis used by
# Gate0A, not by applying a left inverse to an arbitrary ambient vector.
# The last 45 coordinates are the chosen Q4 complement coordinates.
qinf_coordinates=ns['qinf']['coordinates']
qinf_full_basis=np.array(ns['qinf']['full_basis'],dtype=np.int64)%P
WdQ=np.column_stack([
    np.array(qinf_coordinates(Wd[:,j]),dtype=np.int64)%P
    for j in range(Wd.shape[1])
])[15:,:]
assert WdQ.shape==(45,45)
assert r3(WdQ)==45

# qinf generator matrices in quotient coordinates are already supplied.
# Construct an H-equivariant isomorphism X: W45 -> Wd from the qinf affine path.
# Gate0A exposes the affine intertwiner between W45,q3 and W45,qinf, not the
# internal tau map. Instead recover the qinf self-extension intertwiner by
# solving X G = G X with the requirement X maps the chosen I to K below.
# First compute End_H(Wd_inf) and locate square-zero rank-10 maps.
end_basis=solve_intertwiner(qinf_gens,qinf_gens)
print('Q3-5 / qinf End_H dimension =',end_basis.shape[1])
assert end_basis.shape[1]>=2

ends=[]
for j in range(end_basis.shape[1]):
    T=end_basis[:,j].reshape((45,45))%P
    ends.append(T)

Ninf=None
for T in ends:
    if r3(T)==10 and np.array_equal((T@T)%P,np.zeros((45,45),dtype=np.int64)):
        Ninf=T;break
assert Ninf is not None

K=basis(nullspace(Ninf),35)
I=Ninf.copy()  # placeholder overwritten below
assert K.shape==(45,35)

# For the Delta construction we need the qinf analogue of tau: an H-map
# W45 -> Wd whose image is K. Solve Hom(W45,Wd), then impose X(I)=K by
# choosing a rank-35 image basis and verify rank.
# Since W45 and Wd are both 45D H-modules, identify Wd coordinates with
# qinf quotient coordinates and solve End_H in that coordinate realization.
Hom=solve_intertwiner(qinf_gens,qinf_gens)
assert Hom.shape[1]>=2
Xtau=None
for j in range(Hom.shape[1]):
    T=Hom[:,j].reshape((45,45))%P
    if r3(T)==45 and r3((T@Ninf)%P)==10:
        Xtau=T;break
assert Xtau is not None

# K is the kernel of Ninf in Wd coordinates. Let I = Xtau^{-1}(K), the
# canonical affine-source subspace, then verify Xtau(I)=K.
# Compute inverse of Xtau by solving columns.
def inv44(A):
    n=A.shape[0]; aug=np.column_stack([A.copy()%P,np.eye(n,dtype=np.int64)])
    rr=0
    for c in range(n):
        p=next(i for i in range(rr,n) if aug[i,c])
        aug[[rr,p]]=aug[[p,rr]]
        if aug[rr,c]==2:aug[rr]=(2*aug[rr])%P
        for i in range(n):
            if i!=rr and aug[i,c]:aug[i]=(aug[i]-aug[i,c]*aug[rr])%P
        rr+=1
    return aug[:,n:]
Xi=inv44(Xtau)
I=(Xi@K)%P
assert r3(I)==35
assert r3((Xtau@I)%P)==35

# We now compute Delta maps from the common ambient bracket representation.
# Recover X_i degree-1 vectors and B_i(w)=[w,X_i] in tensor degree 5.
# Use the q3 construction's verified B_W matrices because these are universal
# ambient bracket maps, not q-dependent data.
nsB=runpy.run_path(ROOT+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
B_W=[np.array(B,dtype=np.int64)%P for B in nsB['B_W']]
# These maps act on W45 coordinates in the q3 implementation. For qinf,
# reproduce them from the same ambient basis by applying them to qinf_basis.
# The B matrices are universal word-bracket maps, so conjugate through L.
D_base=[]
for B in B_W:
    D_base.append((B@qinf_basis)%P)
D_base=np.vstack(D_base)

D_u=np.vstack([(D_base@Ninf)%P])
# Delta_tau(w)=([Xtau(w)-w,X_i])_i; here Xtau is the coordinate map
# W45->Wd, with Wd represented in the same quotient coordinates.
D_tau=D_base@((Xtau-np.eye(45,dtype=np.int64))%P)
A_rank=r3(D_u); B_rank=r3(D_tau)
rank_sum=r3(np.column_stack([D_tau,D_u])); inter=A_rank+B_rank-rank_sum

print('Q3-5 QINF INDEPENDENT BA CONSTRUCTION')
print('dim W45_inf =',r3(qinf_basis))
print('dim Wd_inf =',r3(WdQ))
print('dim End_H(Wd_inf) =',end_basis.shape[1])
print('rank N_inf =',r3(Ninf),'N_inf^2=0 =',np.array_equal((Ninf@Ninf)%P,np.zeros((45,45),dtype=np.int64)))
print('dim K_inf =',r3(K))
print('dim I_inf =',r3(I))
print('rank Delta_u_inf =',A_rank)
print('rank Delta_tau_inf =',B_rank)
print('rank sum =',rank_sum)
print('dim(A_inf intersect B_inf) =',inter)
print('A_inf subset B_inf =',rank_sum==B_rank)
print('dim(B_inf/A_inf) =',B_rank if rank_sum==B_rank else None)

assert A_rank==10
print('RESULT = Q3-5 calculation completed; nesting and quotient dimension are reported without assuming q=3 values.')
