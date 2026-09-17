"""Q3-5 pretests: determine whether N/tau/Delta data are forced by T.

This is a diagnostic only. It does NOT construct q-infinity A/B as a result.
It first checks whether the q=3 construction is transported automatically by
an independently computed Gate-0A intertwiner.  No q=3 A/B image is used to
construct the q-infinity objects.
"""
import runpy
import numpy as np

P=3; ROOT='research/'

def r3(A):
    A=np.array(A,dtype=np.int64,copy=True)%P
    if A.ndim==1:A=A[:,None]
    m,n=A.shape;r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i,c]),None)
        if p is None: continue
        A[[r,p]]=A[[p,r]]
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
        p=next((i for i in range(r,m) if R[i,c]),None)
        if p is None:continue
        R[[r,p]]=R[[p,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c);r+=1
        if r==m:break
    Z=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64);x[f]=1
        for i,c in enumerate(piv):x[c]=(-R[i,f])%P
        Z.append(x)
    return np.column_stack(Z) if Z else np.zeros((n,0),dtype=np.int64)

def solve_hom(G,H):
    n=G[0].shape[0]; cols=[]
    for q in range(n*n):
        T=np.zeros((n,n),dtype=np.int64);T.flat[q]=1
        blocks=[((T@a-b@T)%P).reshape(-1) for a,b in zip(G,H)]
        cols.append(np.concatenate(blocks))
    return null3(np.column_stack(cols))

def invert(A):
    n=A.shape[0];R=np.column_stack([A.copy()%P,np.eye(n,dtype=np.int64)])
    for c in range(n):
        p=next(i for i in range(c,n) if R[i,c]);R[[c,p]]=R[[p,c]]
        if R[c,c]==2:R[c]=(2*R[c])%P
        for i in range(n):
            if i!=c and R[i,c]:R[i]=(R[i]-R[i,c]*R[c])%P
    return R[:,n:]

def span(M): return r3(M)

# Independently-built q3/qinf quotient modules and Gate-0A intertwiner.
ns=runpy.run_path(ROOT+'GATE0A_Q3_QINF_INDEPENDENT_W45_2026-09-17.py')
A3=[np.array(x,dtype=np.int64)%P for x in ns['q3_gens']]
Ai=[np.array(x,dtype=np.int64)%P for x in ns['qinf_gens']]

H=solve_hom(A3,Ai)
assert H.shape[1]>=2
Ts=[]
for j in range(H.shape[1]):
    T=H[:,j].reshape(45,45)%P
    if r3(T)==45:Ts.append(T)
assert Ts
T=Ts[0]
Ti=invert(T)

# q3 canonical N from the established End_H calculation; qinf N is computed
# independently from its own End_H algebra.
nsN=runpy.run_path(ROOT+'phase2_3_endH_optimized_2026-09-15.py')
N3=np.array(nsN['N'],dtype=np.int64)%P
Ei3=solve_hom(A3,A3)
Eii=solve_hom(Ai,Ai)
assert Ei3.shape[1]==2 and Eii.shape[1]==2

# Find the q-infinity rank-10 square-zero direction independently.
Ninf_candidates=[]
for j in range(Eii.shape[1]):
    X=Eii[:,j].reshape(45,45)%P
    if r3(X)==10 and np.array_equal((X@X)%P,np.zeros((45,45),dtype=np.int64)):
        Ninf_candidates.append(X)
assert Ninf_candidates

# Compare the transported q3 N with the independently computed qinf nilpotent.
NT=(T@N3@Ti)%P
N_AUTO=any(np.array_equal(NT,X) or np.array_equal(NT,(-X)%P) for X in Ninf_candidates)

# q3 tau is the affine H-map produced by the A3-4-9 construction. Reconstruct
# its defining equations directly from the stored W/I/K data, then test whether
# its transported map lands in the qinf affine solution set. This avoids choosing
# an arbitrary Hom element as "tau_inf".
ns18=runpy.run_path(ROOT+'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
A_W=[np.array(x,dtype=np.int64)%P for x in ns18['A_W']]
A_I=[np.array(x,dtype=np.int64)%P for x in ns18['A_I']]
I3=np.array(ns18['I_W'],dtype=np.int64)%P
K3=np.array(ns18['K_coord'],dtype=np.int64)%P
# Reconstruct q3 affine tau exactly as phase2_23 does: target is Wd coordinates
# and X|I = K. The q3 phase2_23 file exposes the actual affine solution.
ns23=runpy.run_path(ROOT+'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
tau3=np.array(ns23['X_intertwiner'],dtype=np.int64)%P
assert r3(tau3)==45

# For q-infinity, first independently compute Wd orbit and identify its coordinate
# realization using the same ambient basis.  Then the transported tau is compared
# only against the qinf affine defining condition once qinf I/K are computed.
# Build ambient d and orbit from Gate0A's shared ambient infrastructure.
idx=ns['index4']; gens=ns['gens']; apply=ns['apply_linear_map']
d=np.zeros(256,dtype=np.int64);d[idx[(1,1,1,2)]]=1;d[idx[(2,1,1,1)]]=2
seen={tuple(d.tolist())};Q=[d.copy()];
for a in Q:
    for g in gens:
        b=np.array(apply(a,g),dtype=np.int64)%P;k=tuple(b.tolist())
        if k not in seen:seen.add(k);Q.append(b)
WdA=np.column_stack(Q)
# greedy basis
def basis_cols(M,target):
    B=np.empty((M.shape[0],0),dtype=np.int64);rr=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]]);q=r3(C)
        if q>rr:B=C;rr=q
        if rr==target:break
    assert rr==target;return B
Wd=basis_cols(WdA,45)
# left inverse for qinf quotient basis
Bi=np.array(ns['qinf_basis'],dtype=np.int64)%P
inds=[];R=np.empty((0,45),dtype=np.int64);rr=0
for i in range(256):
    C=np.vstack([R,Bi[i]])
    q=r3(C)
    if q>rr:inds.append(i);R=C;rr=q
    if rr==45:break
L=[]
for j in range(45):
    aug=np.column_stack([R,np.eye(45,dtype=np.int64)[:,j]])
    for c in range(45):
        p=next(i for i in range(c,45) if aug[i,c]);aug[[c,p]]=aug[[p,c]]
        if aug[c,c]==2:aug[c]=(2*aug[c])%P
        for i in range(45):
            if i!=c and aug[i,c]:aug[i]=(aug[i]-aug[i,c]*aug[c])%P
    L.append(aug[:,45])
L=np.column_stack(L).T
WdQ=(L@Wd)%P
assert r3(WdQ)==45
# qinf Wd action
Aw=[]
for g in range(5):
    # Gate0A qinf generator acts on quotient coordinates. Transport ambient Wd
    # through the quotient and solve its coordinate action.
    G=np.array(ns['qinf_gens'][g],dtype=np.int64)%P
    Y=(WdQ@G)%P
    # WdQ is 45x45 invertible in quotient coordinates.
    Aw.append((invert(WdQ)@Y)%P)
# The qinf tau affine conditions are tested by mapping the q3 affine tau through T
# on source/target only after fixing a target identification. Since d is common
# ambient and Wd is a common subspace, the natural target identification is the
# same ambient-coordinate quotient map; compare transported map as a candidate.
# This pretest deliberately records candidate multiplicity rather than declaring
# uniqueness from one solution.

# Delta automaticity is tested only after the tau target identification is known;
# report that this stage remains unresolved if multiple affine candidates survive.
print('Q3-5 PRETEST AUTO-TRANSFER')
print('dim Hom_H(W3,Winf) =',H.shape[1])
print('invertible intertwiners found =',len(Ts))
print('dim End_H(W3) =',Ei3.shape[1])
print('dim End_H(Winf) =',Eii.shape[1])
print('qinf rank-10 square-zero candidates =',len(Ninf_candidates))
print('Ninf = T*N3*T^-1 (up to scalar) =',N_AUTO)
print('tau3 rank =',r3(tau3))
print('Wd_inf rank =',r3(WdQ))
print('TAU_AUTO_TRANSFER_STATUS = NOT_YET_DECIDED')
print('DELTA_AUTO_TRANSFER_STATUS = NOT_YET_DECIDED')
print('RESULT = N pretest completed; tau/Delta require exact target-coordinate identification before any conclusion.')
