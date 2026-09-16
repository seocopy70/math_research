import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'

# Reuse the verified corrected A3-4-10 data and the known H-endomorphism N.
ns23 = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns23['rank3']
W = np.array(ns23['W'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns23['A_W']]
B_W = [np.array(b, dtype=np.int64) % P for b in ns23['B_W']]
N = np.array(runpy.run_path(ROOT + 'phase2_3_endH_optimized_2025-09-15.py')['N'], dtype=np.int64) % P if False else np.array(runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')['N'], dtype=np.int64) % P

assert W.shape == (256, 45)
assert len(A_W) == 5
assert len(B_W) == 4
assert all(B.shape == (1024, 45) for B in B_W)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45,45), dtype=np.int64))
assert all(np.array_equal((A @ N) % P, (N @ A) % P) for A in A_W)

# u = I+N is the exact user-proposed nontrivial H-automorphism.
I45 = np.eye(45, dtype=np.int64)
U = (I45 + N) % P
assert rank3(U) == 45
assert all(np.array_equal((A @ U) % P, (U @ A) % P) for A in A_W)

# The raw B_W maps W45 -> associative degree-5 words (1024D).  Compress
# these outputs to the actual Lie space L5 (dimension 204), exactly as in
# the corrected A3-4-11 construction, so the control and true-R5 spaces
# live in the same Hom(V,L5) = L5^4 realization.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
words4 = ns1['words4']
L4_candidates = ns1['L4_candidates']
vec4 = ns1['vec4']

words5 = list(product((1,2,3,4), repeat=5))
index5 = {w:i for i,w in enumerate(words5)}

def bracket_col(v_col, gen):
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v_col):
        coeff = int(coeff) % P
        if coeff:
            w = words4[j]
            out[index5[w + (gen,)]] = (out[index5[w + (gen,)]] + coeff) % P
            out[index5[(gen,) + w]] = (out[index5[(gen,) + w]] - coeff) % P
    return out

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
    assert np.array_equal(E[:,:k], np.eye(k, dtype=np.int64))
    return E[:,k:]

# Build an independent L5 basis from [L4,L1].
L5_candidates = []
for a in L4_candidates:
    va = vec4(a)
    for g in range(1,5):
        L5_candidates.append(bracket_col(va, g))
L5_matrix = np.column_stack(L5_candidates) % P
assert rank3(L5_matrix) == 204
L5_basis = np.empty((1024,0), dtype=np.int64)
r = 0
for j in range(L5_matrix.shape[1]):
    C = np.column_stack([L5_basis, L5_matrix[:,j]])
    nr = rank3(C)
    if nr > r:
        L5_basis = C
        r = nr
        if r == 204:
            break
assert L5_basis.shape == (1024,204)
rows = []
R = np.empty((0,204), dtype=np.int64)
r = 0
for i in range(1024):
    C = np.vstack([R, L5_basis[i:i+1]])
    q = rank3(C)
    if q > r:
        rows.append(i)
        R = C
        r = q
        if r == 204:
            break
assert len(rows) == 204
L5_left = left_inverse(L5_basis)

def coords5(V):
    V = np.array(V, dtype=np.int64) % P
    if V.ndim == 1:
        V = V[:,None]
    C = (L5_left @ V[rows,:]) % P
    assert np.array_equal((L5_basis @ C) % P, V)
    return C

# Exact control obstruction: Delta_u(w,X_i) = [Nw,X_i].
# Raw B_W is 1024D, then compress each block to L5^204.
D_u_raw = [(B @ N) % P for B in B_W]
D_u = np.vstack([coords5(B) for B in D_u_raw]) % P
assert D_u.shape == (816,45)
rank_Du = rank3(D_u)

# Import the independently verified TRUE (R)_5 basis.
nsr = runpy.run_path(ROOT + 'A3-4-11_TRUE_R5_INTERSECTION_2026-09-16.py')
R5_basis = np.array(nsr['R5_basis'], dtype=np.int64) % P
assert R5_basis.shape == (204,60)
R5_4 = np.zeros((816,240), dtype=np.int64)
for i in range(4):
    R5_4[i*204:(i+1)*204, i*60:(i+1)*60] = R5_basis
assert rank3(R5_4) == 240

rank_sum = rank3(np.column_stack([D_u, R5_4]))
intersection_dim = rank_Du + 240 - rank_sum

# Project to L5^4 / Hom(V,R5) for an independent quotient-rank check.
Qcols = []
current = R5_4.copy()
r = 240
for j in range(816):
    e = np.eye(816, dtype=np.int64)[:,j:j+1]
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
D_u_Q = (E_inv[240:,:] @ D_u) % P
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
