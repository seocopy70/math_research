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

ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
R4_matrix = ns['R4_matrix']
R4_ind = ns['R4_ind']
basis = ns['basis']
index4 = ns['index4']

X1 = {(1,): 1}
X2 = {(2,): 1}
X3 = {(3,): 1}
X4 = {(4,): 1}

c = bracket(X3, X4)
d1 = bracket(c, X1)
d2 = bracket(c, X2)

# A3-2 restricted/Zassenhaus class representative.
s3 = add({(1,1,1): 1}, {w: (2*a) % 3 for w,a in d1.items()}, {w: (2*a) % 3 for w,a in d2.items()})

# A3-3: bracket the degree-3 class with X1 to expose the degree-4 correction.
d4 = bracket(s3, X1)
v_d4 = vec4(d4, index4)

rank_R = rank3(R4_matrix)
RW = np.column_stack([R4_ind] + [vec4(a,index4) for a in basis])
rank_RW = rank3(RW)
rank_RW_d4 = rank3(np.column_stack([RW, v_d4]))
rank_R_d4 = rank3(np.column_stack([R4_matrix, v_d4]))

power_part = {(1,1,1): 1}
comm_power = bracket(power_part, X1)
correction = add(s3, neg(power_part))
comm_correction = bracket(correction, X1)
assert comm_power == {}
assert d4 == comm_correction

print('PHASE 2-14 / A3-3 DEGREE-4 CORRECTION')
print('rank(R4) =', rank_R)
print('rank([R4_ind | W_basis]) =', rank_RW)
print('rank([R4_ind | W_basis | d4]) =', rank_RW_d4)
print('rank([R4 | d4]) =', rank_R_d4)
print('d4_in_W =', rank_RW_d4 == rank_RW)
print('d4_nonzero_in_Q4 =', rank_R_d4 == rank_R + 1)
print('[X1^[3], X1] = 0 =', comm_power == {})
print('d4_equals_correction_commutator =', d4 == comm_correction)
print('A3-2 class = X1^[3] + 2[[X3,X4],X1] + 2[[X3,X4],X2]')
print('A3-3 induced degree-4 class = 2[[[X3,X4],X1],X1] + 2[[[X3,X4],X2],X1]')

assert rank_R == 5
assert rank_RW == 50
assert rank_RW_d4 == rank_RW
assert rank_R_d4 == rank_R + 1
print('CERTIFICATE: A3 degree-4 correction is nonzero in Q4 and lies in W45.')
