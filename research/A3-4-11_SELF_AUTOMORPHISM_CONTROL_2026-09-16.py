import runpy
import numpy as np

P = 3
ROOT = 'research/'

# A3-4-10 supplies the verified W45 basis, ambient bracket maps B_W,
# and the canonical H-module data.  phase2_18 in turn supplies the
# corrected true-recursive relation layer and the known square-zero N.
ns23 = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns23['rank3']
W = np.array(ns23['W'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns23['A_W']]
B_W = [np.array(b, dtype=np.int64) % P for b in ns23['B_W']]
N = np.array(runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')['N'], dtype=np.int64) % P

gens = ns23['gens']
assert W.shape == (256, 45)
assert len(A_W) == 5
assert len(B_W) == 4
assert all(B.shape == (1024, 45) for B in B_W)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45,45), dtype=np.int64))
assert all(np.array_equal((A @ N) % P, (N @ A) % P) for A in A_W)

# Exact user-proposed control:
# u = 1 + N, hence Delta_u(w, X_i) = [Nw, X_i].
# In the degree-5 ambient associative coordinates this is simply B_W[i] N.
I45 = np.eye(45, dtype=np.int64)
U = (I45 + N) % P
assert rank3(U) == 45
assert np.array_equal((U @ U) % P, (I45 + 2*N) % P)
assert all(np.array_equal((A @ U) % P, (U @ A) % P) for A in A_W)

D_u = [((B @ N) % P) for B in B_W]
D_u_stacked = np.vstack(D_u) % P
rank_Du = rank3(D_u_stacked)

# Correct true (R)_5 and Hom(V,(R)_5) = direct sum of four 60D blocks.
nsr = runpy.run_path(ROOT + 'A3-4-11_TRUE_R5_INTERSECTION_2026-09-16.py')
R5_basis = np.array(nsr['R5_basis'], dtype=np.int64) % P
assert R5_basis.shape == (204, 60)
R5_4 = np.zeros((816, 240), dtype=np.int64)
for i in range(4):
    R5_4[i*204:(i+1)*204, i*60:(i+1)*60] = R5_basis
assert rank3(R5_4) == 240

# D_u is naturally an element of Hom(V,L5) = L5^4.  Intersect its image
# with Hom(V,(R)_5) by the standard dimension formula.
# Both are column spaces in the same 816-dimensional ambient realization.
rank_sum = rank3(np.column_stack([D_u_stacked, R5_4]))
intersection_dim = rank_Du + 240 - rank_sum

# Also project D_u to the quotient Hom(V,L5/(R)_5).  A zero projected
# rank would mean every control obstruction lies in true R5.

def left_inverse(B):
    B = np.array(B, dtype=np.int64) % P
    k = B.shape[1]
    R = np.empty((0,k), dtype=np.int64)
    r = 0
    for i in range(B.shape[0]):
        C = np.vstack([R, B[i:i+1]])
        q = rank3(C)
        if q > r:
            R = C
            r = q
            if r == k:
                break
    assert r == k
    E = np.column_stack([R, np.eye(k, dtype=np.int64)]) % P
    for c in range(k):
        q = next(i for i in range(c,k) if E[i,c])
        E[[c,q]] = E[[q,c]]
        if E[c,c] == 2:
            E[c] = (2*E[c]) % P
        for i in range(k):
            if i != c and E[i,c]:
                E[i] = (E[i] - E[i,c]*E[c]) % P
    return E[:,k:]

# Choose 576 standard-coordinate complement columns to R5_4.
Qcols = []
current = R5_4.copy()
r = 240
for j in range(816):
    e = np.eye(816, dtype=np.int64)[:, j:j+1]
    nrank = rank3(np.column_stack([current,e]))
    if nrank > r:
        Qcols.append(j)
        current = np.column_stack([current,e])
        r = nrank
        if r == 816:
            break
assert len(Qcols) == 576
Qbasis = np.eye(816, dtype=np.int64)[:,Qcols]
E = np.column_stack([R5_4,Qbasis]) % P
assert rank3(E) == 816
E_inv = left_inverse(E)
D_u_Q = (E_inv[240:,:] @ D_u_stacked) % P
rank_Du_Q = rank3(D_u_Q)
assert rank_Du_Q == rank_Du - intersection_dim

print('PHASE A3-4-11 / SELF-AUTOMORPHISM CONTROL')
print('dim W45 =', rank3(W))
print('rank(N) =', rank3(N))
print('nullity(N) =', 45-rank3(N))
print('N^2 = 0 =', np.array_equal((N@N)%P, np.zeros((45,45),dtype=np.int64)))
print('u = I+N invertible =', rank3(U) == 45)
print('u H-equivariant =', all(np.array_equal((A@U)%P,(U@A)%P) for A in A_W))
print('rank Delta_u in Hom(V,L5) =', rank_Du)
print('dim Hom(V,(R)_5) =', 240)
print('rank(Delta_u + Hom(V,(R)_5)) =', rank_sum)
print('dim(Im(Delta_u) intersect Hom(V,(R)_5)) =', intersection_dim)
print('rank Delta_u after quotient by true R5 =', rank_Du_Q)
print('CONTROL_EXPERIMENT_PASSED =', True)
