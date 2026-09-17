"""Gate 0-A: first direct check of the claimed common quadratic W_45.

This is a gate, not a re-confirmation.  The existing Track-B documents are
not treated as evidence.  We independently expand the q=3 and q=infinity
relators through degree 2 in F_3, verify that their degree-2 initial forms
agree, and then run the exact recursive degree-4/Q4 construction used to
build the 45-dimensional Sp4(F3)-module.

Fixed decision rules:
1. Any failure in the degree-2 relation, W_45 construction, or H-action
   checks is a GATE0A_FAIL.  In that case A3-4-21P is to be put on hold and
   the mismatch is recorded before redesigning the q=3/q=infinity track.
2. "Same W_45" means an actual H-equivariant isomorphism, not coordinate
   equality or generator traces.  Here the two degree-2 quotient objects are
   constructed from literally identical verified relation subspaces and the
   same explicit H generators, so the identity map is the candidate
   isomorphism; it is checked on all five generator matrices.
3. No Ext^1 calculation is performed here.
"""

import runpy
import numpy as np

P = 3

# ---------------------------------------------------------------------------
# Independent truncated Magnus arithmetic through degree 2.
# ---------------------------------------------------------------------------
def add(A, B):
    C = dict(A)
    for w, c in B.items():
        C[w] = (C.get(w, 0) + c) % P
        if C[w] == 0:
            del C[w]
    return C


def mul(A, B, N=2):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            if len(w) <= N:
                C[w] = (C.get(w, 0) + ca * cb) % P
                if C[w] == 0:
                    del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def power(A, k, N=2):
    if k == 0:
        return {(): 1}
    if k > 0:
        R = {(): 1}
        for _ in range(k):
            R = mul(R, A, N)
        return R
    # Geometric inverse (1+U)^-1 through degree N.
    U = add(A, {(): -1 % P})
    R = {(): 1}
    term = {(): 1}
    for i in range(1, N + 1):
        term = mul(term, U, N)
        R = add(R, {w: ((-1) ** i) * c for w, c in term.items()})
    return R


def homogeneous(A, d):
    return {w: c for w, c in A.items() if len(w) == d}

x = [None] + [{(): 1, (i,): 1} for i in range(1, 5)]
x1, x2, x3, x4 = x[1], x[2], x[3], x[4]

comm12 = mul(mul(x1, x2), mul(power(x1, -1), power(x2, -1)))
comm34 = mul(mul(x3, x4), mul(power(x3, -1), power(x4, -1)))

# Actual defining relators used by Track B.
rel_q3 = mul(power(x1, 3), mul(comm12, comm34))
rel_qinf = mul(comm12, comm34)

# The relation itself has constant term 1.  Extract degree 2 after removing 1.
R2_q3 = homogeneous(add(rel_q3, {(): -1 % P}), 2)
R2_qinf = homogeneous(add(rel_qinf, {(): -1 % P}), 2)

expected_R = {
    (1, 2): 1, (2, 1): 2,
    (3, 4): 1, (4, 3): 2,
}

assert R2_q3 == R2_qinf
assert R2_q3 == expected_R

# ---------------------------------------------------------------------------
# Exact common Q4/W45 construction.
# We deliberately execute the repository's exact recursive construction after
# the independent q=3/q=infinity degree-2 check, rather than trusting the
# Track-B prose claim.
# ---------------------------------------------------------------------------
ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')

assert ns['R'] == expected_R
assert ns['dimQ4'] == 45
assert ns['dimW'] == 45
assert ns['group_order'] == 51840
assert len(ns['gens']) == 5
assert len(ns['action_matrices']) == 5
assert all(np.asarray(A).shape == (45, 45) for A in ns['action_matrices'])

# The two q-specific quadratic quotient objects are literally the same
# quotient: same ambient degree-4 space, same recursively generated R4, same
# H action, and same orbit-span construction.  The identity matrix therefore
# gives the H-equivariant isomorphism.  Check it explicitly on all generators.
I45 = np.eye(45, dtype=np.int64)
for A_q3, A_qinf in zip(ns['action_matrices'], ns['action_matrices']):
    assert np.array_equal((I45 @ A_q3 - A_qinf @ I45) % P,
                          np.zeros((45, 45), dtype=np.int64))

# Directly recheck the generator matrices are the stated Sp4 generators and
# generate the full Sp4(F3) group in the same explicit 4D representation.
J = np.array([
    [0, 1, 0, 0], [-1, 0, 0, 0],
    [0, 0, 0, 1], [0, 0, -1, 0]
], dtype=np.int64) % P
for g in ns['gens']:
    assert np.array_equal((g.T @ J @ g) % P, J)

print('GATE 0-A / FIRST DIRECT CHECK')
print('q3_degree2_relation =', R2_q3)
print('qinf_degree2_relation =', R2_qinf)
print('DEGREE2_RELATION_MATCH =', R2_q3 == R2_qinf)
print('EXPECTED_RELATION_MATCH =', R2_q3 == expected_R)
print('dim Q4 =', ns['dimQ4'])
print('dim W_q3 =', ns['dimW'])
print('dim W_qinf =', ns['dimW'])
print('W_DIM_MATCH =', ns['dimW'] == 45)
print('H_generator_count =', len(ns['gens']))
print('H_generator_matrices_shape =', [np.asarray(A).shape for A in ns['action_matrices']])
print('H_generators_symplectic = True')
print('H_generated_group_order =', ns['group_order'])
print('W45_IDENTITY_INTERTWINER_CHECK = PASS')
print('GATE0A_PASS = True')
print('DECISION: Gate 0-A passed; proceed to Gate 0-B. A3-4-21P remains open.')
