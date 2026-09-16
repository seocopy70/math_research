"""A3-4-11 / Phase 2-25A: direct degree-5 relation-span verification.

Redesign note (2026-09-16): no inclusion among the degree-5 candidate
pieces is assumed.  Since (R)_1 = 0 and (R)_2 = <R>, the surviving
candidate pieces are treated independently:

    [L1,(R)_4], [L2,(R)_3], [L3,R].

They are concatenated in one L5 coordinate system and their combined rank
is taken as the degree-5 relation span used by this experiment.  A value
20, 40, or any other computed value is accepted as data; it is not rejected
because of a previously assumed inclusion.

Only after the combined rank is known is the corresponding (R)_5^4 built
inside L5^4 and compared with Im(Phi).
"""

import runpy
import numpy as np
from itertools import product

P = 3
ROOT = "research/"

ns24 = runpy.run_path(ROOT + "phase2_24_A3_4_11_L5_obstruction_compression_2026-09-16.py")
ns1 = runpy.run_path(ROOT + "phase2_1_invariant_space_verification_2026-09-15.py")

rank3 = ns24["rank3"]
coords_many = ns24["coords_many"]
D_L5 = np.array(ns24["D_L5"], dtype=np.int64) % P
dim_L5 = int(ns24["dim_L5"])
R4_matrix = np.array(ns1["R4_matrix"], dtype=np.int64) % P
L2 = ns1["L2"]
R = ns1["R"]
X = ns1["X"]
bracket = ns1["bracket"]

words3 = list(product(range(1,5), repeat=3))
words4 = list(product(range(1,5), repeat=4))
words5 = list(product(range(1,5), repeat=5))
idx3 = {w:i for i,w in enumerate(words3)}
idx4 = {w:i for i,w in enumerate(words4)}
idx5 = {w:i for i,w in enumerate(words5)}


def vec(A, words, idx):
    v = np.zeros(len(words), dtype=np.int64)
    for w, c in A.items():
        v[idx[w]] = int(c) % P
    return v


def degree5_columns(dicts):
    return np.column_stack([vec(a, words5, idx5) for a in dicts]) % P


def independent_columns(M):
    M = np.array(M, dtype=np.int64) % P
    selected = []
    C = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        T = np.column_stack([C, M[:, j]])
        nr = rank3(T)
        if nr > r:
            selected.append(j)
            C = T
            r = nr
    return selected, C


def block_diagonal_four(B):
    """Embed an L5 basis B into four independent generator blocks of L5^4."""
    B = np.array(B, dtype=np.int64) % P
    out = np.zeros((4 * dim_L5, 4 * B.shape[1]), dtype=np.int64)
    for block in range(4):
        out[block * dim_L5:(block + 1) * dim_L5,
            block * B.shape[1]:(block + 1) * B.shape[1]] = B
    return out

# ---------------------------------------------------------------------------
# 1. Degree-3 relation space (R)_3 = [L1,R]
# ---------------------------------------------------------------------------
R3_dicts = [bracket(X[i], R) for i in range(4)]
R3 = np.column_stack([vec(a, words3, idx3) for a in R3_dicts]) % P
rank_R3 = rank3(R3)

# ---------------------------------------------------------------------------
# 2. Candidate piece [L2,(R)_3]
# ---------------------------------------------------------------------------
L2_R3_dicts = []
for a in L2:
    for b in R3_dicts:
        L2_R3_dicts.append(bracket(a, b))
L2_R3_L5 = coords_many(degree5_columns(L2_R3_dicts))
rank_L2_R3 = rank3(L2_R3_L5)

# ---------------------------------------------------------------------------
# 3. Candidate piece [L3,R]
# ---------------------------------------------------------------------------
L3_dicts = []
for x in X:
    for a in L2:
        L3_dicts.append(bracket(x, a))
L3_assoc = np.column_stack([vec(a, words3, idx3) for a in L3_dicts]) % P
rank_L3 = rank3(L3_assoc)

L3_R_dicts = [bracket(a, R) for a in L3_dicts]
L3_R_L5 = coords_many(degree5_columns(L3_R_dicts))
rank_L3_R = rank3(L3_R_L5)

# ---------------------------------------------------------------------------
# 4. Candidate piece [L1,(R)_4]
# ---------------------------------------------------------------------------
# R4_matrix is the displayed six-column relation space used by the existing
# obstruction construction.  We select an actual independent basis and do
# not assume that another displayed generating set has the same rank.
base_indices, R4_basis = independent_columns(R4_matrix)
rank_R4_basis = rank3(R4_basis)
assert rank_R4_basis == len(base_indices)

R4_basis_dicts = []
for j in range(R4_basis.shape[1]):
    R4_basis_dicts.append({
        words4[i]: int(R4_basis[i, j]) % P
        for i in range(len(words4))
        if int(R4_basis[i, j]) % P
    })

L1_R4_dicts = []
for r4 in R4_basis_dicts:
    for x in X:
        L1_R4_dicts.append(bracket(x, r4))
L1_R4_L5 = coords_many(degree5_columns(L1_R4_dicts))
rank_L1_R4 = rank3(L1_R4_L5)

# Check the two explicitly requested displayed R4 bases when valid, but do
# not use these checks to alter the canonical calculation above.
def requested_R4_rank(indices):
    B = R4_matrix[:, indices]
    rr = rank3(B)
    if rr != len(indices):
        return {"indices": indices, "basis_rank": rr, "valid_basis": False, "relation_rank": None}
    dicts = []
    for j in range(B.shape[1]):
        dicts.append({
            words4[i]: int(B[i, j]) % P
            for i in range(len(words4))
            if int(B[i, j]) % P
        })
    cols = [bracket(x, r4) for r4 in dicts for x in X]
    C = coords_many(degree5_columns(cols))
    return {"indices": indices, "basis_rank": rr, "valid_basis": True, "relation_rank": rank3(C)}

requested_results = {
    "basis_[0,1,2,3,4]": requested_R4_rank([0,1,2,3,4]),
    "basis_[1,2,3,4,5]": requested_R4_rank([1,2,3,4,5]),
}

# ---------------------------------------------------------------------------
# 5. Direct rank: concatenate all three surviving candidate pieces.
# ---------------------------------------------------------------------------
ALL_R5_CANDIDATES = np.column_stack([
    L1_R4_L5,
    L2_R3_L5,
    L3_R_L5,
]) % P
DIM_R5_FROM_GENERATORS = rank3(ALL_R5_CANDIDATES)

# IMPORTANT: no assertion is made that either extra piece is contained in
# [L1,(R)_4].  Their inclusion/non-inclusion is reported as a diagnostic.
def in_span(U, V):
    return rank3(V) == rank3(np.column_stack([V, U]))

INCLUSION_L2_R3 = in_span(L2_R3_L5, L1_R4_L5)
INCLUSION_L3_R = in_span(L3_R_L5, L1_R4_L5)

# Extract an actual basis of the combined degree-5 relation span.
R5_indices, R5_basis = independent_columns(ALL_R5_CANDIDATES)
assert rank3(R5_basis) == DIM_R5_FROM_GENERATORS

# ---------------------------------------------------------------------------
# 6. Phase 2-25B: build (R)_5^4 and compare with Im(Phi).
# ---------------------------------------------------------------------------
R5_4 = block_diagonal_four(R5_basis)
rank_R5_4 = rank3(R5_4)
rank_sum = rank3(np.column_stack([D_L5, R5_4]))
intersection_dim = int(45 + rank_R5_4 - rank_sum)
assert rank_R5_4 == 4 * DIM_R5_FROM_GENERATORS
assert intersection_dim >= 0

# ---------------------------------------------------------------------------
# 7. Output: all values are empirical finite-dimensional calculations.
# ---------------------------------------------------------------------------
print("PHASE 2-25 / A3-4-11 DIRECT THREE-PIECE L5 RELATION-SPAN VERIFICATION")
print("dim L5 =", dim_L5)
print("dim (R)_3 =", rank_R3)
print("dim L3 =", rank_L3)
print("displayed R4 independent basis indices =", base_indices)
print("dim [L1,(R)_4] =", rank_L1_R4)
print("dim [L2,(R)_3] =", rank_L2_R3)
print("dim [L3,R] =", rank_L3_R)
print("[L2,(R)_3] subset [L1,(R)_4] =", INCLUSION_L2_R3)
print("[L3,R] subset [L1,(R)_4] =", INCLUSION_L3_R)
print("combined three-piece rank =", DIM_R5_FROM_GENERATORS)
print("R5 basis column count =", R5_basis.shape[1])
print("requested R4 basis checks =", requested_results)
print("rank (R)_5^4 =", rank_R5_4)
print("rank(ImPhi + (R)_5^4) =", rank_sum)
print("dim(ImPhi intersection (R)_5^4) =", intersection_dim)
print("NOTE: no pre-existing inclusion or target dimension (20/40/etc.) is assumed.")
print("NOTE: (R)_1=0, so the fourth formal candidate [L4,(R)_1] contributes zero.")
print("PHASE 2-25 COMPLETE")
