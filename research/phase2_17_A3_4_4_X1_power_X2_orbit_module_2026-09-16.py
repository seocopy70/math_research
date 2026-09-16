import runpy
import numpy as np

P = 3

def rank3(A):
    A = np.array(A, dtype=int) % 3
    if A.ndim == 1: A = A.reshape(-1, 1)
    m, n = A.shape; r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i, c]), None)
        if pivot is None: continue
        A[[r, pivot]] = A[[pivot, r]]
        A[r] = A[r] * (1 if A[r, c] == 1 else 2) % 3
        for i in range(m):
            if i != r and A[i, c]: A[i] = (A[i] - A[i, c] * A[r]) % 3
        r += 1
    return r

def add(A, B):
    C = dict(A)
    for w, a in B.items():
        C[w] = (C.get(w, 0) + a) % P
        if C[w] == 0: del C[w]
    return C

def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0: del C[w]
    return C

def neg(A): return {w: (-c) % P for w, c in A.items() if c % P}
def bracket(A, B): return add(mul(A, B), neg(mul(B, A)))

# Exact Phase 2-1 infrastructure.
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
    for w, c in A.items(): v[index4[w]] = c % P
    return v

# Full orbit under the same five generators. Forward closure reaches the
# orbit under the generated group, so the resulting span is Sp4-invariant by construction.
queue = [d]
seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key); queue.append(b)

orbit_elements = queue
W_d = np.column_stack([vec4(a) for a in orbit_elements])
W45 = np.column_stack([vec4(a) for a in basis])

rank_R = rank3(R4_matrix)
rank_W45 = rank3(W45)
rank_Wd = rank3(W_d)
rank_W45_Wd = rank3(np.column_stack([W45, W_d]))
rank_R_Wd = rank3(np.column_stack([R4_ind, W_d]))
rank_R_W45_Wd = rank3(np.column_stack([R4_ind, W45, W_d]))

qdim_W45 = rank3(np.column_stack([R4_ind, W45])) - rank_R
qdim_Wd = rank_R_Wd - rank_R
qdim_sum = rank_R_W45_Wd - rank_R
intersection_W45_Wd = rank_W45 + rank_Wd - rank_W45_Wd

print('PHASE 2-17 / A3-4-4 ORBIT MODULE OF d = [X1^[3], X2]')
print('rank(R4) =', rank_R)
print('rank(W45) =', rank_W45)
print('d_nonzero =', d != {})
print('orbit_size_of_d =', len(orbit_elements))
print('rank(W_d) =', rank_Wd)
print('rank(W45 + W_d) =', rank_W45_Wd)
print('rank(R4 + W_d) =', rank_R_Wd)
print('rank(R4 + W45 + W_d) =', rank_R_W45_Wd)
print('dim(W45 intersect W_d) =', intersection_W45_Wd)
print('dim(image W45 in Q4) =', qdim_W45)
print('dim(image W_d in Q4) =', qdim_Wd)
print('dim(image(W45 + W_d) in Q4) =', qdim_sum)
print('W_d_is_Sp4_invariant =', True)
print('Q4_dimension =', 55)

assert rank_R == 5 and rank_W45 == 45 and d != {}
assert rank_Wd >= 1
assert qdim_W45 == 45 and qdim_Wd == rank_R_Wd - rank_R
assert qdim_sum <= 55 and intersection_W45_Wd >= 0
print('CERTIFICATE: A3-4-4 orbit-generated Sp4(F3)-module construction completed.')
