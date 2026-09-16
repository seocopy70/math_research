import runpy
import numpy as np

P = 3
ROOT = 'research/'


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
    m, n = A.shape
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i, c]), None)
        if q is None:
            continue
        A[[r, q]] = A[[q, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r


def null3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape
    R = A.copy()
    piv = []
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    out = []
    for f in [j for j in range(n) if j not in piv]:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for rr, c in enumerate(piv):
            x[c] = (-R[rr, f]) % P
        out.append(x)
    return out


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C
            r = q
            if r == target:
                break
    assert r == target
    return B


def inverse3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    n = A.shape[0]
    E = np.column_stack([A, np.eye(n, dtype=np.int64)]) % P
    for c in range(n):
        q = next((i for i in range(c, n) if E[i, c]), None)
        assert q is not None
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(n):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    return E[:, n:]


def add(A, B):
    C = dict(A)
    for w, a in B.items():
        C[w] = (C.get(w, 0) + a) % P
        if C[w] == 0:
            del C[w]
    return C


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


# Corrected canonical W45 and its H-action.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
W_words = ns1['basis']
index4 = ns1['index4']
gens = ns1['gens']
apply_linear_map = ns1['apply_linear_map']
A_W45 = [np.array(a, dtype=np.int64) % P for a in ns1['action_matrices']]

def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v

W45 = np.column_stack([vec4(a) for a in W_words])
assert W45.shape == (256, 45) and rank3(W45) == 45

# Independently reconstruct Wd = <H.d>, d=[X1^[3],X2].
d = bracket({(1, 1, 1): 1}, {(2,): 1})
queue = [d]
seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            queue.append(b)
Wd_raw = np.column_stack([vec4(a) for a in queue])
Wd = basis_columns(Wd_raw, 45)
assert rank3(Wd) == 45

# Correct recursive relation space R4, dimension 15.
R = {(1, 2): 1, (2, 1): 2, (3, 4): 1, (4, 3): 2}
R3 = [bracket({(i,): 1}, R) for i in range(1, 5)]
R4_raw = [bracket({(i,): 1}, r) for i in range(1, 5) for r in R3]
R4 = basis_columns(np.column_stack([vec4(a) for a in R4_raw]), 15)
assert rank3(R4) == 15

# Use the direct quotient coordinate construction [R4 | W45].
# Since W45 ∩ R4 = 0 and both dimensions sum to 60, this is a basis of L4.
B = np.column_stack([R4, W45])
assert rank3(B) == 60

# Select 60 independent ambient rows and invert the resulting square matrix.
rows = []
RB = np.empty((0, 60), dtype=np.int64)
r = 0
for i in range(256):
    C = np.vstack([RB, B[i:i+1]])
    q = rank3(C)
    if q > r:
        rows.append(i)
        RB = C
        r = q
        if r == 60:
            break
assert r == 60
L = inverse3(RB)

# Coordinates in the basis [R4 | W45].
C_W45 = (L @ W45[rows]) % P
C_Wd = (L @ Wd[rows]) % P
Q_W45 = C_W45[15:, :]
Q_Wd = C_Wd[15:, :]
assert rank3(Q_W45) == 45
assert rank3(Q_Wd) == 45
# W45 is the quotient coordinate basis itself, so Q_W45 should be invertible.

# tau: W45 -> Wd induced by equality of quotient classes.
# For x in W45-coordinates, Q_W45*x = Q_Wd*y, hence y=tau*x.
tau = (inverse3(Q_Wd) @ Q_W45) % P
assert rank3(tau) == 45

# H-action on Wd in its independently chosen basis.
def restricted_action(Basis, A):
    # Select 45 independent ambient rows once per basis.
    rows_b = []
    RB_b = np.empty((0, 45), dtype=np.int64)
    rr = 0
    for i in range(256):
        C = np.vstack([RB_b, Basis[i:i+1]])
        q = rank3(C)
        if q > rr:
            rows_b.append(i)
            RB_b = C
            rr = q
            if rr == 45:
                break
    assert rr == 45
    inv_b = inverse3(RB_b)
    X = (A @ Basis) % P
    return (inv_b @ X[rows_b]) % P

A_Wd = [restricted_action(Wd, A) for A in ns1['action_matrices']]

# The decisive test: tau(h.w) = h.tau(w), i.e. tau*A_W45 = A_Wd*tau.
residuals = [(tau @ A - Bm @ tau) % P for A, Bm in zip(A_W45, A_Wd)]
ranks = [rank3(R) for R in residuals]
all_zero = all(np.array_equal(R, np.zeros_like(R)) for R in residuals)

print('TAU H-EQUIVARIANCE CHECK')
print('dim W45 =', rank3(W45))
print('dim Wd =', rank3(Wd))
print('dim R4_true =', rank3(R4))
print('rank([R4 | W45]) =', rank3(B))
print('rank(Q_W45) =', rank3(Q_W45))
print('rank(Q_Wd) =', rank3(Q_Wd))
print('rank(tau) =', rank3(tau))
print('generator count =', len(gens))
print('equivariance residual ranks for 5 generators =', ranks)
print('TAU_IS_H_EQUIVARIANT =', all_zero)

assert rank3(W45) == 45
assert rank3(Wd) == 45
assert rank3(R4) == 15
assert rank3(B) == 60
assert rank3(Q_W45) == 45
assert rank3(Q_Wd) == 45
assert rank3(tau) == 45
assert all_zero

print('RESULT: tau: W45 -> Wd is an isomorphism of Sp4(F3)-modules.')
print('RESULT: tau(h.w) = h.tau(w) for all 5 chosen generators, hence for H.')
print('ALL TAU H-EQUIVARIANCE CHECKS PASSED')
