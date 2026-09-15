"""Phase 2-13D: independent torus-character check on U = im(N).

Purpose: verify the coordinate-convention hypothesis on the already identified
module U ~= Sym^2(V).  We do NOT infer the character from the Sym^2 model;
we restrict the authoritative W-action to U=im(N), compute the positive-root
fixed line there, and then extract its split-torus character over F_3.

For the natural highest weight (2,0)=2*epsilon_1, the predicted F_3^*
character is a^2=1, hence trivial.  This script tests that directly.
"""
from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(ROOT / 'research' / 'phase2_13B_positive_unipotent_2026-09-15.py'))
W_action = ns['W_action']
N = np.asarray(ns['N'], dtype=np.int64) % P
rank3 = ns['rank3']
roots = ns['roots']
Pmat = ns['Pmat']; Pinv = ns['Pinv']; J = ns['J']


def null_basis(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape; piv = []; r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i, c]), None)
        if q is None: continue
        A[[r, q]] = A[[q, r]]
        if A[r, c] == 2: A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        piv.append(c); r += 1
        if r == m: break
    out = []
    for f in [j for j in range(n) if j not in piv]:
        x = np.zeros(n, dtype=np.int64); x[f] = 1
        for rr, c in enumerate(piv): x[c] = (-A[rr, f]) % P
        out.append(x)
    return out


def independent_columns(M, k):
    B = np.empty((M.shape[0], 0), dtype=np.int64); r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        rr = rank3(C)
        if rr > r:
            B = C; r = rr
        if r == k: break
    assert r == k
    return B


def coord_solver(B):
    """Return exact solver C with B C = V for V in span(B), B is 45x10."""
    k = B.shape[1]
    rows = []; R = np.empty((0, k), dtype=np.int64); rr = 0
    for i in range(B.shape[0]):
        C = np.vstack([R, B[i:i+1]])
        q = rank3(C)
        if q > rr:
            R = C; rows.append(i); rr = q
        if rr == k: break
    assert rr == k
    M = B[rows].copy() % P
    aug = np.column_stack([M, np.eye(k, dtype=np.int64)]) % P
    for c in range(k):
        q = next(i for i in range(k) if aug[i, c])
        aug[[c, q]] = aug[[q, c]]
        if aug[c, c] == 2: aug[c] = (2 * aug[c]) % P
        for i in range(k):
            if i != c and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[c]) % P
    return rows, aug[:, k:] % P

U = independent_columns(N, 10)
rowsU, Uinv = coord_solver(U)

def U_action(g4):
    X = (W_action(g4) @ U) % P
    C = (Uinv @ X[rowsU]) % P
    assert np.array_equal((U @ C) % P, X)
    return C


def torus(a, b):
    ai = pow(int(a), -1, P); bi = pow(int(b), -1, P)
    d = np.diag([a, b, ai, bi]).astype(np.int64) % P
    return (Pmat @ d @ Pinv) % P

# Verify U+ fixed line directly inside U.
EU = [U_action(g) for g in roots]
fixed = null_basis(np.vstack([(g - np.eye(10, dtype=np.int64)) % P for g in EU]))
assert len(fixed) == 1
v = np.asarray(fixed[0], dtype=np.int64) % P
assert np.any(v)

# Generate the finite positive-unipotent subgroup and verify v is fixed by it.
def key(A): return tuple(np.asarray(A, dtype=np.int64).flatten().tolist())
group = {key(np.eye(4, dtype=np.int64)): np.eye(4, dtype=np.int64)}
frontier = list(group.values())
while frontier:
    a = frontier.pop()
    for g in roots:
        b = (a @ g) % P; k = key(b)
        if k not in group:
            group[k] = b; frontier.append(b)
assert len(group) == 81
for g in group.values():
    A = U_action(g)
    assert np.array_equal((A @ v) % P, v)

# Exact torus character extraction.
def scalar(A, v):
    Av = (A @ v) % P
    i = int(np.flatnonzero(v)[0])
    inv = 1 if int(v[i]) == 1 else 2
    lam = int(Av[i]) * inv % P
    assert np.array_equal((Av - lam * v) % P, np.zeros_like(v))
    return lam

T = [(1,1), (1,2), (2,1), (2,2)]
Ts = {ab: torus(*ab) for ab in T}
As = {ab: U_action(Ts[ab]) for ab in T}
assert np.array_equal(As[(1,1)], np.eye(10, dtype=np.int64) % P)
chi = {ab: scalar(As[ab], v) for ab in T}
observed = tuple(chi[ab] for ab in T)
assert observed == (1,1,1,1)
for a in T:
    for b in T:
        ab = ((a[0]*b[0]) % P, (a[1]*b[1]) % P)
        assert (chi[a] * chi[b]) % P == chi[ab]

print('PHASE 2-13D / U TORUS-CHARACTER CROSS-CHECK')
print('dim U =', U.shape[1])
print('|U+(F3)| =', len(group))
print('dim U^{U+} =', len(fixed))
print('TORUS_CHARACTER_TABLE =', [(a,b,chi[(a,b)]) for a,b in T])
print('OBSERVED_CHARACTER =', observed)
print('MATCHED_CHARACTER = trivial')
print('PREDICTED Sym^2(V) CHARACTER = a^2 = 1 on F3^*')
print('CERTIFICATE: U fixed-line character is trivial, matching (2,0) under the F3 torus convention.')
