# A3-4-12.5b — Ambient equality check I ?= K
# 2026-09-16
#
# Purpose:
#   Independently determine whether the two 35-dimensional subspaces
#       I = W45 ∩ Wd
#       K = ker(N)
#   are equal as ambient subspaces of W45.
#
# Criterion:
#   rank([I | K]) = 35  <=>  I = K,
#   because dim I = dim K = 35.
#
# This script intentionally reuses the exact construction from the verified
# A3-4-5 setup and performs the ambient equality test directly. No module
# isomorphism argument is used to infer equality.

import numpy as np

P = 3

def inv_mod(a):
    return pow(int(a) % P, -1, P)


def rref3(A):
    A = np.array(A, dtype=int) % P
    m, n = A.shape
    pivots = []
    r = 0
    for c in range(n):
        rows = np.where(A[r:, c] % P != 0)[0]
        if len(rows) == 0:
            continue
        i = r + int(rows[0])
        A[[r, i]] = A[[i, r]]
        A[r] = (A[r] * inv_mod(A[r, c])) % P
        for j in range(m):
            if j != r and A[j, c] % P:
                A[j] = (A[j] - A[j, c] * A[r]) % P
        pivots.append(c)
        r += 1
        if r == m:
            break
    return A, pivots


def rank3(A):
    return len(rref3(A)[1])


def nullspace3(A):
    A, piv = rref3(A)
    n = A.shape[1]
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = np.zeros(n, dtype=int)
        v[f] = 1
        for i, p in enumerate(piv):
            v[p] = (-A[i, f]) % P
        basis.append(v)
    return np.array(basis, dtype=int)


def col_basis(A):
    A = np.array(A, dtype=int) % P
    _, piv = rref3(A)
    return A[:, piv]


def vec_word_basis(n):
    # Ambient tensor-degree-4 coordinates: words in X1,...,X4.
    return 4 ** n


def bracket_words(a, b):
    # Associative-word representation. Vectors are indexed by base-4 words.
    # [a,b] = ab-ba.
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            w1 = wa + wb
            w2 = wb + wa
            out[w1] = (out.get(w1, 0) + ca * cb) % P
            out[w2] = (out.get(w2, 0) - ca * cb) % P
    return {w:c for w,c in out.items() if c % P}


def add_poly(*terms):
    out = {}
    for t in terms:
        for w,c in t.items():
            out[w] = (out.get(w,0)+c) % P
    return {w:c for w,c in out.items() if c % P}


def scale_poly(c, a):
    return {w:(c*v)%P for w,v in a.items() if c*v%P}


def gen(i):
    return {(i,):1}


def lie3(a,b,c):
    return bracket_words(bracket_words(a,b),c)


def assoc_vec(poly, degree):
    v = np.zeros(4**degree, dtype=int)
    for w,c in poly.items():
        idx = 0
        for x in w:
            idx = 4*idx + x
        v[idx] = c % P
    return v


def substitute_poly(poly, images):
    out = {}
    for w,c in poly.items():
        cur = {():1}
        for x in w:
            nxt = {}
            for u,cu in cur.items():
                for v,cv in images[x].items():
                    z = u+v
                    nxt[z] = (nxt.get(z,0)+cu*cv)%P
            cur = nxt
        out = add_poly(out, scale_poly(c, cur))
    return out

# The following construction mirrors the verified phase2-18 / A3-4-5
# calculation: true recursive relation R4, Q4, Sp4(F3) orbit spans W45/Wd,
# and the centralizer endomorphism N.
#
# To avoid silently replacing the established construction, this script loads
# the verified A3-4-5 source and executes its definitions through runpy.
import runpy

SRC = runpy.run_path("research/phase2_18_A3-4-5_intersection_K_and_Sym2_2026-09-16.py")

# Accept the canonical variable names used by the A3-4-5 script.
W45 = SRC.get("W45_basis", SRC.get("W_basis"))
Wd = SRC.get("Wd_basis")
N = SRC.get("N")

if W45 is None or Wd is None or N is None:
    raise RuntimeError("Could not recover W45, Wd, N from A3-4-5 construction")

W45 = np.array(W45, dtype=int) % P
Wd = np.array(Wd, dtype=int) % P
N = np.array(N, dtype=int) % P

if W45.shape[0] != 45:
    # Basis may be stored row-wise; normalize to columns.
    if W45.shape[1] == 45:
        W45 = W45.T % P
if Wd.shape[0] != 45:
    if Wd.shape[1] == 45:
        Wd = Wd.T % P
if N.shape != (45,45):
    raise RuntimeError(f"Unexpected N shape: {N.shape}")

# Intersection I = W45 ∩ Wd.
# In a common ambient coordinate system, solve W45*a = Wd*b.
M = np.concatenate([W45, (-Wd) % P], axis=1)
Z = nullspace3(M)
I_raw = (W45 @ Z[:, :45].T) % P
I = col_basis(I_raw)

# K = ker N.
K = nullspace3(N).T % P
K = col_basis(K)

if I.shape[1] != 35 or K.shape[1] != 35:
    raise RuntimeError(f"Expected dim(I)=dim(K)=35, got {I.shape[1]}, {K.shape[1]}")

print("A3-4-12.5b / AMBIENT EQUALITY CHECK I ?= K")
print("dim I =", I.shape[1])
print("dim K =", K.shape[1])

joined_rank = rank3(np.concatenate([I, K], axis=1))
print("rank([I | K]) =", joined_rank)
print("I = K as ambient subspaces =", joined_rank == 35)

# Explicit mutual containment checks as a redundant certificate.
def contained(A, B):
    # col(A) subset col(B)
    return rank3(B) == rank3(np.concatenate([B, A], axis=1))

print("I subset K =", contained(I, K))
print("K subset I =", contained(K, I))

if joined_rank == 35:
    print("RESULT: I and K are equal as ambient subspaces of W45.")
else:
    print("RESULT: I and K are distinct ambient subspaces of W45.")

print("ALL A3-4-12.5b CHECKS COMPLETED")
