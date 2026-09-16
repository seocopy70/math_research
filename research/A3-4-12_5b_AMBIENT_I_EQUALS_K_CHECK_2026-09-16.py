# A3-4-12.5b — Ambient equality check I ?= K
# Exact ambient-subspace check over F_3.
# Reuses the already verified A3-4-5 construction directly.
import runpy
import numpy as np

P = 3

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

SRC = runpy.run_path(
    "research/phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py"
)

# A3-4-5 already constructs these in the same 45-dimensional W45 coordinates.
I = np.array(SRC["I_W"], dtype=np.int64) % P
K = np.array(SRC["K_coord"], dtype=np.int64) % P

assert I.shape == (45, 35)
assert K.shape == (45, 35)
assert rank3(I) == 35
assert rank3(K) == 35

r = rank3(np.column_stack([I, K]) % P)
intersection_dim = 70 - r

print("A3-4-12.5b / AMBIENT EQUALITY CHECK I ?= K")
print("rank(I) =", rank3(I))
print("rank(K) =", rank3(K))
print("rank([I | K]) =", r)
print("dim(I ∩ K) =", intersection_dim)
print("I_EQUALS_K_AMBIENT =", r == 35)
print("I subset K =", r == 35)
print("K subset I =", r == 35)
print("RESULT:", "I = K as ambient subspaces of W45." if r == 35 else "I != K as ambient subspaces of W45.")
print("ALL A3-4-12.5b CHECKS COMPLETED")
