import ast
from pathlib import Path
from itertools import product
import numpy as np

P = 3
ROOT = Path('research')

def add(A, B):
    C = dict(A)
    for w, c in B.items():
        C[w] = (C.get(w, 0) + c) % P
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

def vec(A, degree):
    words = list(product((1, 2, 3, 4), repeat=degree))
    index = {w: i for i, w in enumerate(words)}
    v = np.zeros(4 ** degree, dtype=np.int64)
    for w, c in A.items():
        v[index[w]] = c % P
    return v

def independent_basis(candidates, degree, target=None):
    cols = []
    M = np.empty((4 ** degree, 0), dtype=np.int64)
    r = 0
    for a in candidates:
        c = vec(a, degree)
        C = np.column_stack([M, c])
        q = rank3(C)
        if q > r:
            cols.append(a)
            M = C
            r = q
            if target is not None and r == target:
                break
    return cols, M

X = [{(i + 1,): 1} for i in range(4)]
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]
R = add(L2[0], L2[5])

R3 = [bracket(R, x) for x in X]
R3m = np.column_stack([vec(a, 3) for a in R3])
dim_R3 = rank3(R3m)

# (R)_4 is [L1,(R)_3], not [L2,R].
R4_true_candidates = [bracket(x, r3) for x in X for r3 in R3]
R4_true_m = np.column_stack([vec(a, 4) for a in R4_true_candidates])
dim_R4_true = rank3(R4_true_m)

# Negative control: the tempting but incomplete [L2,R] construction.
R4_old_candidates = [bracket(R, b) for b in L2]
R4_old_m = np.column_stack([vec(a, 4) for a in R4_old_candidates])
dim_R4_old = rank3(R4_old_m)

R4_ind, _ = independent_basis(R4_true_candidates, 4, target=dim_R4_true)
R5_local = [bracket(x, r4) for x in X for r4 in R4_ind]
R5_local_m = np.column_stack([vec(a, 5) for a in R5_local])
dim_R5_local = rank3(R5_local_m)

# Degree-5 full homogeneous pieces; Jacobi should put them inside the local piece.
L3_candidates = [bracket(a, x) for a in L2 for x in X]
L3_basis, _ = independent_basis(L3_candidates, 3, target=20)
mid5 = [bracket(a, b) for a in L2 for b in R3]
last5 = [bracket(a, R) for a in L3_basis]
mid5m = np.column_stack([vec(a, 5) for a in mid5])
last5m = np.column_stack([vec(a, 5) for a in last5])
assert rank3(np.column_stack([R5_local_m, mid5m])) == dim_R5_local
assert rank3(np.column_stack([R5_local_m, last5m])) == dim_R5_local

# Degree-6 local recursion check.
R6_local = [bracket(x, r5) for x in X for r5 in R5_local]
R6_local_m = np.column_stack([vec(a, 6) for a in R6_local])
dim_R6_local = rank3(R6_local_m)

# Static audit: only direct old R4 constructions are forbidden.
suspicious = []
for path in sorted(ROOT.glob('*.py')):
    if path.name == Path(__file__).name:
        continue
    text = path.read_text(encoding='utf-8')
    if 'bracket(R, B)' in text or 'bracket(R, b)' in text:
        suspicious.append((str(path), 'direct [R,L2]-style construction'))

phase21 = (ROOT / 'phase2_1_invariant_space_verification_2026-09-15.py').read_text(encoding='utf-8')
phase21_old = 'for B in L2:\n    R4.append(bracket(R, B))'
phase21_has_old = phase21_old in phase21

print('RELATION RECURSION AUDIT — 2026-09-16')
print('dim (R)_3 =', dim_R3)
print('dim true (R)_4 =', dim_R4_true)
print('dim old partial [L2,R] =', dim_R4_old)
print('dim local (R)_5 =', dim_R5_local)
print('dim local (R)_6 =', dim_R6_local)
print('degree-5 Jacobi containment [L2,(R)_3] inside [L1,(R)_4] =', True)
print('degree-5 Jacobi containment [L3,R] inside [L1,(R)_4] =', True)
print('phase2_1 still contains old [L2,R] R4 construction =', phase21_has_old)
print('DIRECT OLD-R4 FILES:')
for item in suspicious:
    print('  ', item[0], '::', item[1])

assert dim_R3 == 4
assert dim_R4_true == 15
assert dim_R4_old == 5
assert dim_R5_local == 60
assert not phase21_has_old, 'phase2_1 still defines (R)_4 as [L2,R]'
assert not suspicious, 'repository contains a remaining direct old [L2,R] construction'
print('RESULT: recursive relation dimensions are independently verified.')
print('RESULT: degree-5 local relation space has dimension 60 for the true 15-dimensional (R)_4.')
print('RESULT: repository static audit found no remaining direct old [L2,R] construction.')
print('ALL RELATION RECURSION AUDIT CHECKS PASSED')
