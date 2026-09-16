import runpy
import numpy as np

P = 3


def rank3(A):
    A = np.array(A, dtype=int) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i, c]), None)
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        A[r] = A[r] * (1 if A[r, c] == 1 else 2) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
    return r


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


# Reuse the corrected Phase 2-1 infrastructure, whose R4 is now defined
# recursively as (R)_4 = [L1,(R)_3], not the old 5-dimensional [L2,R].
ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
R4_matrix, R4_ind = ns['R4_matrix'], ns['R4_ind']
basis, index4 = ns['basis'], ns['index4']
gens, apply_linear_map = ns['gens'], ns['apply_linear_map']

X1, X2 = {(1,): 1}, {(2,): 1}
power_part = {(1, 1, 1): 1}
d = bracket(power_part, X2)
direct_d = bracket(bracket(bracket(X1, X2), X1), X1)
assert d == direct_d and d != {}


def vec4(A):
    v = np.zeros(256, dtype=int)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v


# Generate the full Sp4(F3)-orbit using the same five generators as A3-4-4.
queue = [d]
seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            queue.append(b)

W_d = np.column_stack([vec4(a) for a in queue])
W45 = np.column_stack([vec4(a) for a in basis])

rank_R4 = rank3(R4_matrix)
rank_Wd = rank3(W_d)
rank_W45 = rank3(W45)
rank_R4_plus_Wd = rank3(np.column_stack([R4_ind, W_d]))
rank_R4_plus_W45 = rank3(np.column_stack([R4_ind, W45]))
rank_R4_plus_both = rank3(np.column_stack([R4_ind, W45, W_d]))
rank_W45_plus_Wd = rank3(np.column_stack([W45, W_d]))

intersection_Wd_R4 = rank_R4 + rank_Wd - rank_R4_plus_Wd
intersection_W45_Wd = rank_W45 + rank_Wd - rank_W45_plus_Wd
image_Wd = rank_R4_plus_Wd - rank_R4
image_W45 = rank_R4_plus_W45 - rank_R4
image_sum = rank_R4_plus_both - rank_R4

print('A3-4 REVALIDATION: W_d against TRUE (R)_4')
print('rank((R)_4 true) =', rank_R4)
print('orbit element count =', len(queue))
print('rank(W_d) =', rank_Wd)
print('rank(W45) =', rank_W45)
print('rank((R)_4 + W_d) =', rank_R4_plus_Wd)
print('dim(W_d intersect TRUE (R)_4) =', intersection_Wd_R4)
print('dim(pi_true(W_d)) =', image_Wd)
print('rank((R)_4 + W45) =', rank_R4_plus_W45)
print('dim(pi_true(W45)) =', image_W45)
print('rank(W45 + W_d) =', rank_W45_plus_Wd)
print('dim(W45 intersect W_d) =', intersection_W45_Wd)
print('rank((R)_4 + W45 + W_d) =', rank_R4_plus_both)
print('dim(pi_true(W45 + W_d)) =', image_sum)
print('true Q4 dimension =', 45)

assert rank_R4 == 15
assert rank_W45 == 45
assert rank_Wd == 45
assert intersection_Wd_R4 == 0
assert image_Wd == 45
assert image_W45 == 45
assert image_sum == 45
assert intersection_W45_Wd == 35

print('GATE PASSED: W_d is disjoint from TRUE (R)_4 and projects injectively to Q4_true.')
print('AMBIENT INTERSECTION CHECK: dim(W45 intersect W_d) = 35.')
print('IMPORTANT: both pi(W45) and pi(W_d) equal the full 45-dimensional Q4_true.')
print('Therefore the old 55-dimensional quotient-sum interpretation is superseded.')
print('A3-4-10/11 remains blocked pending revalidation of I = W45 intersect W_d and I ~= K.')
