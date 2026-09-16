import runpy
import numpy as np

P = 3
ROOT = 'research/'

ns = runpy.run_path(ROOT + 'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
rank3 = ns['rank3']
coords = ns['coords']
W = np.array(ns['W'], dtype=np.int64) % P
Wd = np.array(ns['Wd_basis'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns['A_W']]

# Reconstruct the ambient 256-dimensional generator actions directly from
# the authoritative word-space action routine. This avoids assuming that
# phase2_1 exports an undocumented ambient matrix variable.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
index4 = ns1['index4']
gens = ns1['gens']
apply_linear_map = ns1['apply_linear_map']
words = list(index4.keys())
A_ambient = []
for g in gens:
    G = np.zeros((256,256), dtype=np.int64)
    for j,w in enumerate(words):
        out = apply_linear_map({w:1}, g)
        for ww,c in out.items():
            G[index4[ww],j] = (G[index4[ww],j] + c) % P
    A_ambient.append(G)

assert W.shape == (256,45)
assert Wd.shape == (256,45)
assert I_W.shape == (45,35)
assert K_coord.shape == (45,35)
assert len(A_W) == len(A_ambient) == 5

A_Wd = []
for G in A_ambient:
    X = (G @ Wd) % P
    C = coords(Wd, X)
    assert np.array_equal((Wd @ C) % P, X)
    A_Wd.append(C)

# A3-4-8 established I=K as actual ambient subspaces.
K_ambient = (W @ K_coord) % P
K_Wd = coords(Wd, K_ambient)
assert np.array_equal((Wd @ K_Wd) % P, K_ambient)
assert rank3(K_Wd) == 35

# Test whether the two exact sequences are equivalent with the common K fixed
# pointwise. Seek X: W45 -> Wd satisfying
#   A_Wd[i] X = X A_W[i]
#   X I_W = K_Wd.
n = 45
Nvar = n*n
rows=[]; rhs=[]
def vi(r,c): return r*n+c

for A, Ad in zip(A_W, A_Wd):
    for r in range(n):
        for c in range(n):
            row=np.zeros(Nvar,dtype=np.int64)
            for k in range(n):
                row[vi(k,c)] = (row[vi(k,c)] + Ad[r,k]) % P
                row[vi(r,k)] = (row[vi(r,k)] - A[k,c]) % P
            rows.append(row); rhs.append(0)

for r in range(n):
    for c in range(35):
        row=np.zeros(Nvar,dtype=np.int64)
        for k in range(n):
            row[vi(r,k)] = (row[vi(r,k)] + I_W[k,c]) % P
        rows.append(row); rhs.append(int(K_Wd[r,c]))

M=np.array(rows,dtype=np.int64)%P
b=np.array(rhs,dtype=np.int64)%P

def rref_solve(A,b):
    R=np.column_stack([A.copy()%P,b.reshape(-1,1)%P])
    m,naug=R.shape; n=naug-1; r=0; piv=[]
    for c in range(n):
        q=next((i for i in range(r,m) if R[i,c]),None)
        if q is None: continue
        R[[r,q]]=R[[q,r]]
        if R[r,c]==2: R[r]=(2*R[r])%P
        for i in range(m):
            if i!=r and R[i,c]: R[i]=(R[i]-R[i,c]*R[r])%P
        piv.append(c); r+=1
        if r==m: break
    bad=any(np.all(R[i,:n]%P==0) and R[i,n]%P!=0 for i in range(r,m))
    if bad: return len(piv),None,n-len(piv)
    x=np.zeros(n,dtype=np.int64)
    for rr,c in enumerate(piv): x[c]=R[rr,n]
    return len(piv),x,n-len(piv)

rank_system, sol, nullity_system = rref_solve(M,b)

print('PHASE 2-22 / A3-4-9 EXTENSION EQUIVALENCE')
print('dim W45 =',rank3(W))
print('dim Wd =',rank3(Wd))
print('dim common K =',rank3(K_ambient))
print('system rows =',M.shape[0])
print('system unknowns =',M.shape[1])
print('rank of constrained system =',rank_system)
print('solution nullity =',nullity_system)
print('EXTENSION_ISOMORPHISM_FIXING_K_EXISTS =',sol is not None)

if sol is not None:
    X=sol.reshape((n,n))%P
    print('rank(extension intertwiner) =',rank3(X))
    print('RESTRICTION_TO_K_CHECK =',np.array_equal((X@I_W)%P,K_Wd%P))
    print('GENERATOR_INTERTWINING_CHECKS =',all(np.array_equal((Ad@X)%P,(X@A)%P) for A,Ad in zip(A_W,A_Wd)))
    assert rank3(X)==45
    assert np.array_equal((X@I_W)%P,K_Wd%P)
    assert all(np.array_equal((Ad@X)%P,(X@A)%P) for A,Ad in zip(A_W,A_Wd))
    print('RESULT: the two extensions are equivalent via an H-isomorphism fixing K pointwise.')
else:
    print('RESULT: no H-isomorphism W45 -> Wd fixing the common K pointwise exists.')

print('ALL A3-4-9 CHECKS COMPLETED')
