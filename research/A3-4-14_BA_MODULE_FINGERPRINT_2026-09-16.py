import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'

# Verified A3-4-10 / A3-4-12 infrastructure.
ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P
D_tau = np.array(ns['D'], dtype=np.int64) % P

nsN = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
N = np.array(nsN['N'], dtype=np.int64) % P

nsH = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
gens = nsH['gens']
apply_linear_map = nsH['apply_linear_map']
index4 = nsH['index4']
words4 = list(index4.keys())
words5 = list(product((1, 2, 3, 4), repeat=5))
index5 = {w: i for i, w in enumerate(words5)}

assert W.shape == (256, 45)
assert I_W.shape == (45, 35)
assert K_coord.shape == (60, 35)
assert D_tau.shape == (4096, 45)
assert rank3(W) == 45
assert rank3(I_W) == 35
assert rank3(K_coord) == 35
assert rank3(D_tau) == 45
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45,45), dtype=np.int64))

# Reconstruct degree-4 H action on W, and K action in its own 60D L4 coordinates.
A_W = []
for g in gens:
    G = np.zeros((256, 256), dtype=np.int64)
    for j, w in enumerate(words4):
        out = apply_linear_map({w: 1}, g)
        for ww, c in out.items():
            G[index4[ww], j] = (G[index4[ww], j] + c) % P
    Y = (G @ W) % P
    C = np.zeros((45,45), dtype=np.int64)
    for j in range(45):
        # W is full column rank; solve W c = Y[:,j].
        C[:,j] = 0
        # rref below is defined later; postpone via direct coordinate map built once.
    A_W.append(G)


def rref_aug_solve(A, b):
    """Solve A x=b over F_3; return one solution or None."""
    A = np.array(A, dtype=np.int64) % P
    b = np.array(b, dtype=np.int64).reshape(-1) % P
    R = np.column_stack([A, b])
    m, n1 = R.shape
    n = n1 - 1
    r = 0
    piv = []
    for c in range(n):
        q = next((i for i in range(r, m) if R[i,c] % P), None)
        if q is None:
            continue
        R[[r,q]] = R[[q,r]]
        if R[r,c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i,c]:
                R[i] = (R[i] - R[i,c] * R[r]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    for i in range(r,m):
        if np.all(R[i,:n] % P == 0) and R[i,n] % P != 0:
            return None
    x = np.zeros(n, dtype=np.int64)
    for rr,c in enumerate(piv):
        x[c] = R[rr,n]
    return x % P

# Coordinate map W -> F3^45.
W_coord = np.zeros((45,256), dtype=np.int64)
for j in range(256):
    sol = rref_aug_solve(W, np.eye(256, dtype=np.int64)[:,j])
    if sol is not None:
        W_coord[:,j] = sol
# Verify it is a left inverse on W.
assert np.array_equal((W_coord @ W) % P, np.eye(45, dtype=np.int64))
A_W_coord = [(W_coord @ G @ W) % P for G in A_W]

# --- Build the fixed quotient basis C=[A | Q] exactly from Im Delta_u and Delta_tau. ---
# A = Im Delta_u, using the verified control map.
B_W = ns['B_W']
D_u = np.vstack([((np.array(B, dtype=np.int64) @ N) % P) for B in B_W])
assert rank3(D_u) == 10
A_basis_cols = []
cur = np.zeros((4096,0), dtype=np.int64)
for j in range(D_u.shape[1]):
    cand = D_u[:,j:j+1]
    if rank3(np.column_stack([cur,cand])) > rank3(cur):
        A_basis_cols.append(D_u[:,j])
        cur = np.column_stack([cur,cand])
assert cur.shape[1] == 10
A_basis = cur

Q_cols = []
cur_rank = rank3(A_basis)
for j in range(D_tau.shape[1]):
    cand = D_tau[:,j:j+1]
    new = np.column_stack([A_basis] + [np.array(Q_cols,dtype=np.int64).T] if Q_cols else [A_basis, cand])
    # Avoid ambiguous list construction: use explicit matrix below.
    base = A_basis if not Q_cols else np.column_stack([A_basis, np.array(Q_cols,dtype=np.int64).T])
    if rank3(np.column_stack([base,cand])) > cur_rank:
        Q_cols.append(D_tau[:,j])
        cur_rank += 1
    if len(Q_cols) == 35:
        break
Q_basis = np.array(Q_cols, dtype=np.int64).T % P
C = np.column_stack([A_basis, Q_basis]) % P
assert C.shape == (4096,45)
assert rank3(C) == 45

# Quotient coordinates: C=[A|Q], so last 35 coordinates are B/A coordinates.
def quotient_coords(y):
    z = rref_aug_solve(C, y)
    assert z is not None
    return z[10:] % P

# Build actual GL(4,F3) matrices from the existing generator action on degree 1.
# The degree-1 words are (1),(2),(3),(4), so this is read directly from apply_linear_map.
def gen_matrix(g):
    M = np.zeros((4,4), dtype=np.int64)
    for j in range(1,5):
        out = apply_linear_map({(j,): 1}, g)
        for ww,c in out.items():
            if len(ww) == 1:
                M[ww[0]-1,j-1] = (M[ww[0]-1,j-1] + c) % P
    return M % P

Mgens = [gen_matrix(g) for g in gens]

# Tensor^5 action matrix, implemented columnwise. For a tensor basis word w,
# M^{tensor 5} is computed by expanding each factor.
def tensor5_matrix(M):
    T = np.zeros((1024,1024), dtype=np.int64)
    for j,w in enumerate(words5):
        col = {((),): 1}
        # Easier direct product expansion.
        partial = {(): 1}
        for letter in w:
            nxt = {}
            for pref, coeff in partial.items():
                for out_letter in range(4):
                    a = int(M[out_letter,letter-1]) % P
                    if a:
                        ww = pref + (out_letter+1,)
                        nxt[ww] = (nxt.get(ww,0) + coeff*a) % P
            partial = nxt
        for ww,c in partial.items():
            T[index5[ww],j] = c % P
    return T % P

T5 = [tensor5_matrix(M) for M in Mgens]

# Actual ambient Hom(V,T^5) action: (g.f)(v)=g f(g^{-1}v).
# D_tau is stacked as 4 consecutive T^5 output blocks, one per input basis vector.
def transform_hom_column(hcol, M, T):
    Minv = np.array(rref_aug_solve(M, np.eye(4,dtype=np.int64)[:,0]), dtype=np.int64) if False else None
    # Small 4x4 inverse by solving each column.
    Minv = np.column_stack([rref_aug_solve(M, np.eye(4,dtype=np.int64)[:,j]) for j in range(4)]) % P
    blocks = [np.array(hcol[j*1024:(j+1)*1024],dtype=np.int64) % P for j in range(4)]
    out = [np.zeros(1024,dtype=np.int64) for _ in range(4)]
    # output input-column j = T * sum_k blocks[k] * Minv[k,j]
    for j in range(4):
        v = np.zeros(1024,dtype=np.int64)
        for k in range(4):
            v = (v + int(Minv[k,j]) * blocks[k]) % P
        out[j] = (T @ v) % P
    return np.concatenate(out) % P

# Induced B/A action on the fixed quotient basis Q.
BA_actions = []
for M,T in zip(Mgens,T5):
    cols = []
    for j in range(35):
        y = transform_hom_column(Q_basis[:,j], M, T)
        # True ambient equivariance implies y in B; quotient takes its last 35 C-coordinates.
        z = rref_aug_solve(C, y)
        assert z is not None
        cols.append(z[10:])
    Tg = np.array(cols,dtype=np.int64).T % P
    BA_actions.append(Tg)

# Independent K action: K is represented in the 60D L4 ambient coordinate system.
K_actions = []
for G in A_W:
    cols = []
    for j in range(35):
        y = (G @ (W @ K_coord[:,j])) % P
        y4 = rref_aug_solve(W, y)
        assert y4 is not None
        z = rref_aug_solve(K_coord, y4)
        assert z is not None
        cols.append(z)
    Kg = np.array(cols,dtype=np.int64).T % P
    K_actions.append(Kg)

# Verify both actions are invertible and satisfy their defining representations.
assert all(rank3(Tg) == 35 for Tg in BA_actions)
assert all(rank3(Kg) == 35 for Kg in K_actions)

# Fingerprint: trace, order, fixed space, ranks of powers of (T-I), and minimal
# polynomial degree by the first linear dependence of I,T,...,T^d.
def mat_order(T, max_order=5000):
    R = np.eye(35,dtype=np.int64)
    for k in range(1,max_order+1):
        R = (R @ T) % P
        if np.array_equal(R, np.eye(35,dtype=np.int64)):
            return k
    return None

def minimal_polynomial_degree(T, maxdeg=80):
    powers = [np.eye(35,dtype=np.int64)]
    for d in range(1,maxdeg+1):
        powers.append((powers[-1] @ T) % P)
        M = np.column_stack([p.reshape(-1) for p in powers])
        if rank3(M) < len(powers):
            return d
    return None

def fingerprint(T):
    I35 = np.eye(35,dtype=np.int64)
    D = (T - I35) % P
    ranks = []
    R = D.copy()
    for _ in range(1,36):
        r = rank3(R)
        ranks.append(r)
        if r == 0:
            break
        R = (R @ D) % P
    return {
        'trace': int(np.trace(T) % P),
        'order': mat_order(T),
        'fixed_dim': 35 - rank3(D),
        'rank(T-I)': rank3(D),
        'ranks_powers': ranks,
        'minpoly_degree': minimal_polynomial_degree(T),
    }

print('A3-4-14 / BA MODULE FINGERPRINT')
print('dim(B/A) =', 35)
print('dim(K) =', 35)
print('rank Delta_tau =', rank3(D_tau))
print('rank Delta_u =', rank3(D_u))
print('number of H generators =', len(gens))
print()

all_equal = True
for i,(Tb,Tk) in enumerate(zip(BA_actions,K_actions), start=1):
    fb = fingerprint(Tb)
    fk = fingerprint(Tk)
    if fb != fk:
        all_equal = False
    print('GENERATOR', i)
    print('  B/A trace =', fb['trace'], ' K trace =', fk['trace'])
    print('  B/A order =', fb['order'], ' K order =', fk['order'])
    print('  B/A fixed_dim =', fb['fixed_dim'], ' K fixed_dim =', fk['fixed_dim'])
    print('  B/A rank(T-I) =', fb['rank(T-I)'], ' K rank(T-I) =', fk['rank(T-I)'])
    print('  B/A ranks((T-I)^k) =', fb['ranks_powers'])
    print('  K   ranks((T-I)^k) =', fk['ranks_powers'])
    print('  B/A minpoly degree =', fb['minpoly_degree'], ' K minpoly degree =', fk['minpoly_degree'])
    print('  fingerprint_equal =', fb == fk)

print()
print('ALL_GENERATOR_FINGERPRINTS_EQUAL =', all_equal)
if all_equal:
    print('RESULT: the tested generator fingerprints do not distinguish B/A from K; character/class-level analysis is required next.')
else:
    print('RESULT: B/A and K differ on at least one generator-level representation fingerprint.')
print('NOTE: generator traces alone are not claimed to be the full character table.')
print('ALL A3-4-14 CHECKS COMPLETED')
