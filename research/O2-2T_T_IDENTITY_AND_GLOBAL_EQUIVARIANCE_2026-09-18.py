# O2-2T audit: identify the solved block action T_g and record the global equivariance proof.
#
# Purpose:
# 1. Verify that the uniquely solved T_g from O2-2R is the corrected
#    contragredient flavor action g^{-T} in the same 4-dimensional basis.
# 2. Record the precise group-theoretic closure argument from generator-wise
#    equivariance to equivariance for every g in H.
#
# Conventions:
#   The verified sanity artifact uses column convention
#       e_j -> sum_i g[i,j] e_i.
#   Therefore the matrix appearing on the obstruction 4-block index is
#       T_g = g^{-T}.
#   This is exactly the transpose-type action that appears after correcting
#   the earlier tuple-action transpose convention; the audit compares the
#   actual matrices, rather than relying on naming alone.

import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Recompute the authoritative generator matrices from the same standalone
# sanity artifact used by O2-2R/O2-2S.
san = runpy.run_path(ROOT + 'A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py')
gens = [np.array(g, dtype=np.int64) % P for g in san['gens']]
assert len(gens) == 5
assert all(g.shape == (4, 4) for g in gens)

# Import the solved T_g.  O2-2R has a unique solution for every generator
# (system rank 16, nullity 0), so these are the certified T_g matrices.
o2r = runpy.run_path(ROOT + 'O2-2R_OBSTRUCTION_EQUIVARIANCE_2026-09-18.py')
# The original artifact stores the solutions in the local variable `solutions`.
T_solved = [np.array(T, dtype=np.int64) % P for T in o2r['solutions']]
assert len(T_solved) == 5
assert all(T.shape == (4, 4) for T in T_solved)


def inv4(A):
    # Exact inverse over F_3 by Gauss-Jordan.
    A = np.array(A, dtype=np.int64, copy=True) % P
    n = A.shape[0]
    R = np.column_stack([A, np.eye(n, dtype=np.int64)]) % P
    r = 0
    for c in range(n):
        q = next((i for i in range(r, n) if R[i, c]), None)
        assert q is not None
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(n):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        r += 1
    assert np.array_equal(R[:, :n] % P, np.eye(n, dtype=np.int64))
    return R[:, n:] % P


T_expected = [(inv4(g).T % P) for g in gens]

print('O2-2T: T_g IDENTITY / GLOBAL EQUIVARIANCE AUDIT')
print('generator convention = column convention e_j -> sum_i g[i,j] e_i')
print('candidate corrected flavor action = g^{-T}')

all_match = True
for i, (g, T, E) in enumerate(zip(gens, T_solved, T_expected)):
    match = np.array_equal(T, E)
    all_match = all_match and match
    print('GENERATOR', i)
    print('g =')
    print(g)
    print('T_solved =')
    print(T)
    print('g^{-T} =')
    print(E)
    print('T_g = g^{-T} =', match)

assert all_match

# The corrected transpose-type action is representation-valued because
# (gh)^{-T} = g^{-T} h^{-T}.
# This is checked directly on all ordered pairs of the five generators.
for i, g in enumerate(gens):
    for j, h in enumerate(gens):
        lhs = inv4((g @ h) % P).T % P
        rhs = (T_expected[i] @ T_expected[j]) % P
        assert np.array_equal(lhs, rhs)

print('generator-pair multiplicativity of g^{-T} = PASS')

# Record the closure argument used to extend the already verified O2-2R
# identity from the five generators to all of H.
print('GLOBAL EQUIVARIANCE LOGIC:')
print('1. O2-2R directly verified D_stack A_W(s) = rho_T(s) D_stack for each of the 5 generators s.')
print('2. A_W is a representation of H, and rho_T(g)=T_g tensor A5(g) is a representation of H:')
print('   T_{gh}=T_g T_h and A5(gh)=A5(g)A5(h), hence rho_T(gh)=rho_T(g)rho_T(h).')
print('3. Let E={g in H : D_stack A_W(g)=rho_T(g)D_stack}. If g,h in E,')
print('   then D_stack A_W(gh)=D_stack A_W(g)A_W(h)=rho_T(g)D_stack A_W(h)=rho_T(g)rho_T(h)D_stack=rho_T(gh)D_stack.')
print('4. Thus E is closed under products (and contains the five generators); equivalently, every word in the generators satisfies the identity.')
print('5. Since the five generators generate H=Sp4(F3), E=H. Therefore the equivariance identity holds for every g in H.')
print('6. Consequently O=Im(D_stack) is H-stable under rho_T, and the induced action is well-defined on O.')

print('T_IDENTITY = g^{-T}: PASS')
print('GLOBAL_EQUIVARIANCE_ARGUMENT_RECORDED = PASS')
print('O2-2T PASS = True')
