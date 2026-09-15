"""Independent verification of Phase 2-10.

Purpose: independently certify W ~= Lambda^2(Sym^2 V) without random search.
The authoritative W action is imported from Phase 2-1. The model action is
constructed here from scratch, and all 9 elements of the 2-dimensional
intertwiner space over F_3 are exhaustively tested. Every candidate is also
checked by direct multiplication against all five generator equations.
"""
from pathlib import Path
import runpy
import hashlib
import numpy as np

P = 3
ROOT = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(ROOT / 'research' / 'phase2_1_invariant_space_verification_2026-09-15.py'))
AW = [np.asarray(x, dtype=np.int64) % P for x in ns['action_matrices']]
G = [np.asarray(x, dtype=np.int64) % P for x in ns['gens']]
assert len(AW) == 5 and all(a.shape == (45, 45) for a in AW)

# Independent modular rank (forward elimination only; no RREF).
def rank_mod3(A):
    A = np.asarray(A, dtype=np.int64).copy() % P
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i, c] != 0), None)
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(r + 1, m):
            if A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r

pairs = [(i, j) for i in range(4) for j in range(i, 4)]
pi = {p: k for k, p in enumerate(pairs)}

def sym2(g):
    S = np.zeros((10, 10), dtype=np.int64)
    for c, (i, j) in enumerate(pairs):
        for a in range(4):
            for b in range(4):
                z = int(g[a, i]) * int(g[b, j])
                if z:
                    p = (a, b) if a <= b else (b, a)
                    S[pi[p], c] = (S[pi[p], c] + z) % P
    return S

wp = [(i, j) for i in range(10) for j in range(i + 1, 10)]
wi = {p: k for k, p in enumerate(wp)}

def wedge2(S):
    L = np.zeros((45, 45), dtype=np.int64)
    for c, (i, j) in enumerate(wp):
        for a in range(10):
            for b in range(10):
                z = int(S[a, i]) * int(S[b, j])
                if not z or a == b:
                    continue
                p = (a, b) if a < b else (b, a)
                s = 1 if a < b else -1
                L[wi[p], c] = (L[wi[p], c] + s * z) % P
    return L

AM = [wedge2(sym2(g)) for g in G]
assert all(a.shape == (45, 45) for a in AM)

# Solve the intertwiner equations P A_i = B_i P.
# Vectorization uses column-major convention.
I = np.eye(45, dtype=np.int64)
E = np.vstack([(np.kron(a.T, I) - np.kron(I, b)) % P for a, b in zip(AW, AM)]) % P

# RREF only to obtain a basis of the nullspace; rank is independently computed.
def rref_basis(A):
    A = np.asarray(A, dtype=np.int64).copy() % P
    m, n = A.shape
    r = 0
    piv = []
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
        piv.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        x = np.zeros(n, dtype=np.int64)
        x[f] = 1
        for row, c in enumerate(piv):
            x[c] = (-A[row, f]) % P
        basis.append(x.reshape((45, 45), order='F'))
    return r, basis

rankE = rank_mod3(E)
rankE2, basis = rref_basis(E)
assert rankE == rankE2
assert len(basis) == 2

# Exhaustive, not random: every element of the 2D Hom space is tested.
full_rank = []
for a in range(3):
    for b in range(3):
        X = (a * basis[0] + b * basis[1]) % P
        if a == 0 and b == 0:
            continue
        residuals = [((X @ A - B @ X) % P) for A, B in zip(AW, AM)]
        assert all(np.count_nonzero(R) == 0 for R in residuals)
        r = rank_mod3(X)
        if r == 45:
            full_rank.append((a, b, X))

assert full_rank, 'No invertible intertwiner among all 8 nonzero Hom elements.'
coef_a, coef_b, witness = full_rank[0]
assert all(np.array_equal((witness @ A) % P, (B @ witness) % P) for A, B in zip(AW, AM))

# Independent nonzero determinant test via rank is already exact over F_3.
# Hash the explicit witness so the certificate can be tracked reproducibly.
wbytes = np.asarray(witness, dtype=np.uint8).tobytes(order='C')
whash = hashlib.sha256(wbytes).hexdigest()

print('PHASE 2-10 / INDEPENDENT VERIFICATION')
print('W dimension =', AW[0].shape[0])
print('model dimension =', AM[0].shape[0])
print('intertwiner matrix shape =', E.shape)
print('rank(E) [independent forward elimination] =', rankE)
print('rank(E) [RREF cross-check] =', rankE2)
print('dim Hom_H =', len(basis))
print('exhaustive nonzero Hom elements tested =', 8)
print('full-rank intertwiners found =', len(full_rank))
print('witness coefficients in nullspace basis =', (coef_a, coef_b))
print('witness rank =', rank_mod3(witness))
print('witness SHA256 =', whash)
print('all five intertwining equations = True')
print('CERTIFICATE: W ~= Lambda^2(Sym^2(V))')
