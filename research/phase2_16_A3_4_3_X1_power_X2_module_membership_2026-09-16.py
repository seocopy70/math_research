import runpy
import numpy as np

P = 3


def add(*As):
    C = {}
    for A in As:
        for w, a in A.items():
            C[w] = (C.get(w, 0) + a) % P
            if C[w] == 0:
                del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


def vec4(A, index4):
    v = np.zeros(256, dtype=int)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v


def rank3(A):
    A = np.array(A, dtype=int) % 3
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        pivot = None
        for i in range(r, m):
            if A[i, c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        inv = 1 if A[r, c] == 1 else 2
        A[r] = (A[r] * inv) % 3
        for i in range(m):
            if i != r and A[i, c] != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % 3
        r += 1
    return r


# Reuse the exact Phase 2-1 Q4 / W45 infrastructure.
ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
R4_matrix = ns['R4_matrix']
R4_ind = ns['R4_ind']
basis = ns['basis']
index4 = ns['index4']

X1 = {(1,): 1}
X2 = {(2,): 1}

# d = [X1^[3], X2] = ad(X1)^3(X2), in the same F_3 convention.
power_part = {(1, 1, 1): 1}
d = bracket(power_part, X2)
direct_d = bracket(bracket(bracket(X1, X2), X1), X1)
assert d == direct_d
assert d != {}

rank_R = rank3(R4_matrix)
W_matrix = np.column_stack([vec4(a, index4) for a in basis])
RW_matrix = np.column_stack([R4_ind, W_matrix])
rank_RW = rank3(RW_matrix)

v_d = vec4(d, index4)

# Certificate 1: d is genuinely outside (R)_4.
rank_R_d = rank3(np.column_stack([R4_matrix, v_d]))

# Certificate 2: d lies in (R)_4 + W45 iff this rank stays 50.
rank_RW_d = rank3(np.column_stack([RW_matrix, v_d]))

# Certificate 3: direct membership in W45 itself.
# This is deliberately separated from Certificate 2: the latter only proves
# d in R4 + W45 and does not rule out an R4 component.
rank_W = rank3(W_matrix)
rank_W_d = rank3(np.column_stack([W_matrix, v_d]))

direct_W_membership = (rank_W_d == rank_W)

print('PHASE 2-16 / A3-4-3 X1^[3], X2 MODULE MEMBERSHIP')
print('rank(R4) =', rank_R)
print('rank(W45 in ambient word space) =', rank_W)
print('rank([R4_ind | W_basis]) =', rank_RW)
print('restricted_comm_equals_direct_ad3 =', d == direct_d)
print('restricted_comm_nonzero =', d != {})
print('rank([R4 | d]) =', rank_R_d)
print('rank([R4_ind | W_basis | d]) =', rank_RW_d)
print('rank(W45) =', rank_W)
print('rank([W45 | d]) =', rank_W_d)
print('d_in_W45 =', direct_W_membership)
print('d_in_R4_plus_W45 =', rank_RW_d == rank_RW)
print('new_direction_mod_R4_plus_W45 =', rank_RW_d == rank_RW + 1)

assert rank_R == 5
assert rank_W == 45
assert rank_RW == 50
assert d == direct_d
assert d != {}
assert rank_R_d == 6
assert rank_RW_d in (50, 51)

# The decisive direct-membership certificate must agree with the combined-space result.
if direct_W_membership:
    assert rank_RW_d == rank_RW
else:
    # Since d is outside R4, failure of W-membership may still leave d in R4+W.
    assert rank_RW_d in (50, 51)

print('CERTIFICATE: A3-4-3 completed with separate R4, R4+W45, and direct W45 tests.')
