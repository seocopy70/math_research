"""
A3-4-9: Verify W45 survives the TRUE degree-4 relation quotient.

Question:
    Is W45 ∩ [L1, (R)_3] = 0 ?

Ambient coordinates:
    The calculation is performed in the 256-dimensional degree-4
    associative word space on X1,...,X4, exactly as in the authoritative
    Phase 2-1 W45 construction. No quotient-coordinate identification is
    used for the intersection test.

Definitions:
    L = free Lie algebra over F_3 on X1,...,X4
    R = [X1,X2] + [X3,X4]
    (R)_3 = [L1,R]
    S = [L1,(R)_3]

The natural quotient map is
    L4/[L2,R] -> L4/[L1,(R)_3].

Since [L2,R] subset S, the kernel has dimension 15-5=10.
The decisive survival test is
    dim pi(W45) = dim W45 - dim(W45 ∩ S).
"""

import runpy
import numpy as np

MOD = 3

# Reuse the repository's authoritative W45 construction.
BASE = runpy.run_path("research/phase2_1_invariant_space_verification_2026-09-15.py")

X = BASE["X"]
bracket = BASE["bracket"]
vec4 = BASE["vec4"]
rank3 = BASE["rank3"]
W = np.array(BASE["W"], dtype=np.int64) % MOD

# Degree-1 and degree-2 Lie basis used for the relation layers.
L1 = [X[i] for i in range(4)]
L2 = BASE["L2"]
R = BASE["R"]

# (R)_3 = [L1,R].
R3 = [bracket(x, R) for x in L1]
R3m = np.stack([vec4(z) for z in R3], axis=1) % MOD

# S = [L1,(R)_3].
S = []
for x in L1:
    for r3 in R3:
        S.append(bracket(x, r3))
Sm = np.stack([vec4(z) for z in S], axis=1) % MOD

# [L2,R], the old degree-4 relation space.
old_rel = [bracket(z, R) for z in L2]
oldm = np.stack([vec4(z) for z in old_rel], axis=1) % MOD


def mod3_rank(A):
    A = np.array(A, dtype=np.int64) % MOD
    if A.size == 0:
        return 0
    A = A.copy()
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i, c] % MOD:
                piv = i
                break
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        inv = 1 if A[r, c] == 1 else 2
        A[r, :] = (A[r, :] * inv) % MOD
        for i in range(m):
            if i != r and A[i, c] % MOD:
                A[i, :] = (A[i, :] - A[i, c] * A[r, :]) % MOD
        r += 1
        if r == m:
            break
    return r


dim_W = mod3_rank(W)
dim_R3 = mod3_rank(R3m)
dim_S = mod3_rank(Sm)
dim_old = mod3_rank(oldm)
rank_WS = mod3_rank(np.concatenate([W, Sm], axis=1))
intersection = dim_W + dim_S - rank_WS
rank_S_old = mod3_rank(np.concatenate([Sm, oldm], axis=1))
old_subset_S = rank_S_old == dim_S

# Since S is the true relation space and old_rel is contained in S,
# the induced map has kernel S/old_rel of dimension dim_S-dim_old.
ker_dim = dim_S - dim_old
proj_dim = dim_W - intersection

print("A3-4-9 TRUE RELATION INTERSECTION CERTIFICATE")
print("===============================================")
print(f"dim (R)_3 = {dim_R3}")
print(f"dim [L1,(R)_3] = {dim_S}")
print(f"dim W45 = {dim_W}")
print(f"rank([W45 | [L1,(R)_3]]) = {rank_WS}")
print(f"dim(W45 intersection [L1,(R)_3]) = {intersection}")
print(f"dim pi(W45) = {proj_dim}")
print(f"dim [L2,R] = {dim_old}")
print(f"dim ker(L4/[L2,R] -> L4/[L1,(R)_3]) = {ker_dim}")
print(f"[L2,R] subset [L1,(R)_3] = {old_subset_S}")

assert dim_R3 == 4
assert dim_S == 15
assert dim_W == 45
assert rank_WS == 60
assert intersection == 0
assert proj_dim == 45
assert dim_old == 5
assert ker_dim == 10
assert old_subset_S

print("ALL CHECKS PASSED")
