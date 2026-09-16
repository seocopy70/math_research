"""A3-4-11 / Phase 2-25: independent degree-5 relation-span verification.

This phase deliberately separates the pure L5 calculation from the later
L5^4 comparison.  No dimension of (R)_5 is assumed in advance.

Checks:
1. [L2,(R)_3] subset [L1,(R)_4]
2. [L3,R] subset [L1,(R)_4]
3. combined rank = 20
4. repeat the [L1,(R)_4] rank with two explicitly selected R4 bases
5. identify dim (R)_5 from the generated degree-5 ideal pieces

Only after these checks does the script construct (R)_5^4 and compare it
with Im(Phi), using the already verified L5^4 obstruction from phase2_24.
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
L5_basis = ns24["L5_basis"]
D_L5 = np.array(ns24["D_L5"], dtype=np.int64) % P
dim_L5 = int(ns24["dim_L5"])
R4_matrix = np.array(ns1["R4_matrix"], dtype=np.int64) % P
L2 = ns1["L2"]
R = ns1["R"]
X = ns1["X"]

# Reuse associative-algebra helpers from phase2_1.
bracket = ns1["bracket"]

# Word/vector helpers for degrees 2,3,5.
words2 = list(product(range(1,5), repeat=2))
words3 = list(product(range(1,5), repeat=3))
words5 = list(product(range(1,5), repeat=5))
idx2 = {w:i for i,w in enumerate(words2)}
idx3 = {w:i for i,w in enumerate(words3)}
idx5 = {w:i for i,w in enumerate(words5)}

def vec(A, words, idx):
    v = np.zeros(len(words), dtype=np.int64)
    for w,c in A.items():
        v[idx[w]] = int(c) % P
    return v

def bracket_vec(A, B, wordsA, idxA, wordsB, idxB):
    # A*B - B*A in the associative tensor algebra.
    out = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            out[w] = (out.get(w, 0) + ca*cb) % P
            w2 = wb + wa
            out[w2] = (out.get(w2, 0) - ca*cb) % P
    return {w:c % P for w,c in out.items() if c % P}

def degree5_columns(dicts):
    return np.column_stack([vec(a, words5, idx5) for a in dicts]) % P

def independent_columns(M):
    M = np.array(M, dtype=np.int64) % P
    selected = []
    C = np.empty((M.shape[0],0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        T = np.column_stack([C, M[:,j]])
        nr = rank3(T)
        if nr > r:
            selected.append(j)
            C = T
            r = nr
    return selected, C

def in_span(U, V):
    # Every column of U lies in span(V).
    return rank3(V) == rank3(np.column_stack([V,U]))

def embed_block(vcols, block):
    out = np.zeros((4*dim_L5, vcols.shape[1]), dtype=np.int64)
    out[block*dim_L5:(block+1)*dim_L5,:] = vcols
    return out

# ---------------------------------------------------------------------------
# 1. Degree-3 relation space (R)_3 = [L1,R]
# ---------------------------------------------------------------------------
R3_dicts = [bracket(X[i], R) for i in range(4)]
R3 = np.column_stack([vec(a, words3, idx3) for a in R3_dicts]) % P
rank_R3 = rank3(R3)

# ---------------------------------------------------------------------------
# 2. L2 x (R)_3 and L3 x R, both landing in L5.
# ---------------------------------------------------------------------------
L2_R3_dicts = []
for a in L2:
    for b in R3_dicts:
        L2_R3_dicts.append(bracket(a,b))
L2_R3_assoc = degree5_columns(L2_R3_dicts)
L2_R3_L5 = coords_many(L2_R3_assoc)
rank_L2_R3 = rank3(L2_R3_L5)

# L3 = [L1,L2].  Generate the full displayed list, then use its span.
L3_dicts = []
for x in X:
    for a in L2:
        L3_dicts.append(bracket(x,a))
L3_assoc = np.column_stack([vec(a, words3, idx3) for a in L3_dicts]) % P
rank_L3 = rank3(L3_assoc)

L3_R_dicts = [bracket(a,R) for a in L3_dicts]
L3_R_assoc = degree5_columns(L3_R_dicts)
L3_R_L5 = coords_many(L3_R_assoc)
rank_L3_R = rank3(L3_R_L5)

# ---------------------------------------------------------------------------
# 3. [L1,(R)_4] with two basis selections.
# ---------------------------------------------------------------------------
# R4_matrix has 6 displayed columns of rank 5.  The requested index sets
# are tested explicitly when they form a basis; otherwise we report why
# a set is invalid rather than silently replacing it.

def local_R5_from_R4_basis(indices):
    B = R4_matrix[:, indices]
    basis_rank = rank3(B)
    if basis_rank != len(indices):
        return None, basis_rank, None
    cols = []
    # Degree-4 vector -> bracket with each generator on the left.
    # Build using words4 directly.
    words4 = list(product(range(1,5), repeat=4))
    idx4 = {w:i for i,w in enumerate(words4)}
    basis_dicts = []
    for j in range(B.shape[1]):
        d = {words4[i]: int(B[i,j]) % P for i in range(256) if int(B[i,j]) % P}
        basis_dicts.append(d)
    for d in basis_dicts:
        for x in X:
            cols.append(bracket(x,d))
    A = degree5_columns(cols)
    C = coords_many(A)
    return C, basis_rank, A

# First canonical independent basis obtained greedily.
base_indices, _ = independent_columns(R4_matrix)
C_canonical, base_rank, _ = local_R5_from_R4_basis(base_indices)
rank_canonical = rank3(C_canonical)

# Explicit requested sets are checked separately.
requested = {
    "basis_[0,1,2,3,4]": [0,1,2,3,4],
    "basis_[1,2,3,4,5]": [1,2,3,4,5],
}
requested_results = {}
for name, inds in requested.items():
    C, rr, _ = local_R5_from_R4_basis(inds)
    requested_results[name] = {
        "indices": inds,
        "basis_rank": rr,
        "valid_basis": C is not None,
        "relation_rank": None if C is None else rank3(C),
    }

# ---------------------------------------------------------------------------
# 4. Inclusion and combined-rank tests.
# ---------------------------------------------------------------------------
INCLUSION_L2_R3 = in_span(L2_R3_L5, C_canonical)
INCLUSION_L3_R = in_span(L3_R_L5, C_canonical)
COMBINED = np.column_stack([C_canonical, L2_R3_L5, L3_R_L5])
COMBINED_RANK = rank3(COMBINED)

# If the two extra spaces are contained in the local relation span, the
# degree-5 relation span generated by these pieces has exactly the local rank.
DIM_R5_FROM_GENERATORS = COMBINED_RANK
R5_EQUALS_LOCAL_BY_GENERATOR_RANK = (DIM_R5_FROM_GENERATORS == rank_canonical)

# ---------------------------------------------------------------------------
# 5. Only now construct (R)_5^4 and compare to Im(Phi).
# ---------------------------------------------------------------------------
R5_local_4 = np.zeros((4*dim_L5, C_canonical.shape[1]), dtype=np.int64)
for j in range(C_canonical.shape[1]):
    block = j % 4
    R5_local_4[:,j] = embed_block(C_canonical[:,j:j+1], block)[:,0]

rank_R5_local = rank_canonical
rank_R5_4 = rank3(R5_local_4)
combined_4 = rank3(np.column_stack([D_L5, R5_local_4]))
intersection_4 = 45 + rank_R5_4 - combined_4

# ---------------------------------------------------------------------------
# Assertions: only mathematical statements actually established by these
# finite-dimensional calculations are asserted.
# ---------------------------------------------------------------------------
assert rank_R3 == 4
assert rank_L3 == 20
assert INCLUSION_L2_R3
assert INCLUSION_L3_R
assert COMBINED_RANK == rank_canonical
assert rank_R5_4 == rank_R5_local
assert intersection_4 >= 0

print("PHASE 2-25 / A3-4-11 PURE L5 RELATION-SPAN VERIFICATION")
print("dim L5 =", dim_L5)
print("dim (R)_3 =", rank_R3)
print("dim L3 =", rank_L3)
print("canonical independent R4 basis indices =", base_indices)
print("dim [L1,(R)_4] =", rank_canonical)
print("dim [L2,(R)_3] =", rank_L2_R3)
print("dim [L3,R] =", rank_L3_R)
print("[L2,(R)_3] subset [L1,(R)_4] =", INCLUSION_L2_R3)
print("[L3,R] subset [L1,(R)_4] =", INCLUSION_L3_R)
print("combined rank =", COMBINED_RANK)
print("requested basis checks =", requested_results)
print("DIM_R5_FROM_GENERATORS =", DIM_R5_FROM_GENERATORS)
print("R5_EQUALS_LOCAL_BY_GENERATOR_RANK =", R5_EQUALS_LOCAL_BY_GENERATOR_RANK)
print("dim (R)_5 local =", rank_R5_local)
print("rank (R)_5^4 =", rank_R5_4)
print("rank(ImPhi + (R)_5^4) =", combined_4)
print("dim(ImPhi intersection (R)_5^4) =", intersection_4)
print("NOTE: explicit basis index [1,2,3,4,5] is accepted only if those five displayed columns are independent.")
print("NOTE: (R)_5 equality here means equality of the degree-5 ideal generators [L1,(R)_4], [L2,(R)_3], [L3,R] after their computed inclusions.")
print("PHASE 2-25 COMPLETE")
