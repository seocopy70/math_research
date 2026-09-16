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


# Reuse the exact Q4 / W45 infrastructure already certified in Phase 2-1.
ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
R4_matrix = ns['R4_matrix']
R4_ind = ns['R4_ind']
basis = ns['basis']
index4 = ns['index4']

X1 = {(1,): 1}
X2 = {(2,): 1}
X3 = {(3,): 1}
X4 = {(4,): 1}

# Exact A3-2 degree-3 classes, in the same convention as the existing Track B record.
c = bracket(X3, X4)
d1 = bracket(c, X1)
d2 = bracket(c, X2)
common = add(
    {w: (2 * a) % 3 for w, a in d1.items()},
    {w: (2 * a) % 3 for w, a in d2.items()},
)
s3 = add({(1, 1, 1): 1}, common)
sinf = common

# Restricted-Lie sanity check:
# [X1^[3], X2] must equal ad(X1)^3(X2) in the free Lie algebra.
power_part = {(1, 1, 1): 1}
restricted_comm = bracket(power_part, X2)
direct_comm = bracket(bracket(bracket(X1, X2), X1), X1)
assert restricted_comm == direct_comm
assert restricted_comm != {}

# A3-4-2: compare X2-brackets of q=3 and q=infinity representatives.
d3_x2 = bracket(s3, X2)
dinf_x2 = bracket(sinf, X2)
diff = add(d3_x2, neg(dinf_x2))

# The difference must be exactly the restricted-power contribution.
assert diff == restricted_comm

rank_R = rank3(R4_matrix)
RW = np.column_stack([R4_ind] + [vec4(a, index4) for a in basis])
rank_RW = rank3(RW)

v_d3 = vec4(d3_x2, index4)
v_inf = vec4(dinf_x2, index4)
v_diff = vec4(diff, index4)

rank_R_d3 = rank3(np.column_stack([R4_matrix, v_d3]))
rank_R_inf = rank3(np.column_stack([R4_matrix, v_inf]))
rank_R_diff = rank3(np.column_stack([R4_matrix, v_diff]))
rank_RW_d3 = rank3(np.column_stack([RW, v_d3]))
rank_RW_inf = rank3(np.column_stack([RW, v_inf]))
rank_RW_diff = rank3(np.column_stack([RW, v_diff]))

print('PHASE 2-15 / A3-4-2 X2 q-SENSITIVITY')
print('rank(R4) =', rank_R)
print('rank([R4_ind | W_basis]) =', rank_RW)
print('restricted_comm_equals_direct_ad3 =', restricted_comm == direct_comm)
print('restricted_comm_nonzero =', restricted_comm != {})
print('d3_x2_minus_dinf_x2_equals_restricted_comm =', diff == restricted_comm)
print('rank([R4 | d3_x2]) =', rank_R_d3)
print('rank([R4 | dinf_x2]) =', rank_R_inf)
print('rank([R4 | difference]) =', rank_R_diff)
print('rank([R4_ind | W_basis | d3_x2]) =', rank_RW_d3)
print('rank([R4_ind | W_basis | dinf_x2]) =', rank_RW_inf)
print('rank([R4_ind | W_basis | difference]) =', rank_RW_diff)
print('difference_nonzero_in_Q4 =', rank_R_diff == rank_R + 1)
print('q3_and_qinf_separated_in_Q4 =', rank_R_diff == rank_R + 1)

assert rank_R == 5
assert rank_RW == 50
assert restricted_comm == direct_comm
assert restricted_comm != {}
assert diff == restricted_comm
assert rank_R_diff == rank_R + 1

print('CERTIFICATE: A3-4-2 detects the q=3 p-power contribution in Q4 via X2.')
