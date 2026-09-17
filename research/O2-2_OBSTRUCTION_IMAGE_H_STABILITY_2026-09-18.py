import runpy
import numpy as np

P = 3
ROOT = 'research/'


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


def solve_coords(B, Y):
    """Coordinates of Y in the full-column-rank basis B over F_3."""
    B = np.array(B, dtype=np.int64) % P
    Y = np.array(Y, dtype=np.int64) % P
    assert B.ndim == 2 and Y.ndim == 2
    assert B.shape[1] == rank3(B)
    out = np.zeros((B.shape[1], Y.shape[1]), dtype=np.int64)
    for j in range(Y.shape[1]):
        A = np.column_stack([B, Y[:, j]]) % P
        m, naug = A.shape
        n = naug - 1
        r = 0
        piv = []
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
            piv.append(c)
            r += 1
            if r == m:
                break
        assert len(piv) == n
        out[:, j] = A[:n, -1] % P
    return out


# O2-1 is authoritative for the concrete ordered basis O = Im(barD_stack).
o2_1 = runpy.run_path(ROOT + 'O2-1_OBSTRUCTION_IMAGE_BASIS_2026-09-18.py')
O_basis = np.array(o2_1['O_basis'], dtype=np.int64) % P
assert O_basis.shape == (816, 10)
assert rank3(O_basis) == 10

# IMPORTANT: reuse the exact corrected degree-5 action machinery from the
# standalone A3-4-10 sanity artifact.  We do not reconstruct D5 here.
san = runpy.run_path(ROOT + 'A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py')
gens = san['gens']
WORDS5 = san['WORDS5']
INDEX5 = san['INDEX5']
degree_action_matrix = san['degree_action_matrix']

assert len(gens) == 5
assert len(WORDS5) == 1024
assert len(INDEX5) == 1024

# The ambient obstruction target is L5^4 = four 204-dimensional blocks.
# Its H-action is the direct-sum action of the SAME corrected D5(g) on each
# block.  D5(g) itself is obtained by calling the verified sanity artifact's
# degree_action_matrix(g, 5, WORDS5, INDEX5), not by rebuilding an alternative
# Kronecker/transpose convention here.
D5_actions = [
    degree_action_matrix(g, 5, WORDS5, INDEX5) % P
    for g in gens
]
assert all(A.shape == (1024, 1024) for A in D5_actions)

# A3-4-10 stores each obstruction block in L5 coordinates and O2-1 stacks
# four blocks.  Since each block is the same L5 representation, the ambient
# tuple action is block diagonal with the verified D5(g) repeated four times.
def tuple_action(A5, X):
    X = np.array(X, dtype=np.int64) % P
    assert X.shape[0] == 816
    out = np.zeros_like(X)
    for b in range(4):
        sl = slice(204 * b, 204 * (b + 1))
        out[sl, :] = (A5 @ X[sl, :]) % P
    return out


print('O2-2: H-STABILITY OF THE OBSTRUCTION IMAGE O')
print('O basis shape =', O_basis.shape)
print('dim O =', rank3(O_basis))
print('number of H generators =', len(gens))
print('generator convention = the 5 Sp4(F3) presentation generators from the sanity artifact')
print('tuple target = L5^4 = 4 x 204 coordinates')
print('degree-5 action source = A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py:degree_action_matrix')
print('tuple action = direct sum of the SAME verified D5(g) on all four obstruction blocks')

all_stable = True
induced_actions = []
for gi, (g, A5) in enumerate(zip(gens, D5_actions)):
    transformed = tuple_action(A5, O_basis)
    augmented_rank = rank3(np.column_stack([O_basis, transformed]))
    stable = augmented_rank == 10
    print('GENERATOR', gi, 'D5 shape =', A5.shape)
    print('GENERATOR', gi, 'rank([O | gO]) =', augmented_rank)
    print('GENERATOR', gi, 'O_STABLE =', stable)
    if not stable:
        all_stable = False
        # No induced 10x10 action is defined when stability fails.
        continue
    induced = solve_coords(O_basis, transformed)
    assert induced.shape == (10, 10)
    assert np.array_equal((O_basis @ induced) % P, transformed)
    induced_actions.append(induced)
    print('GENERATOR', gi, 'induced O action shape =', induced.shape)
    print('GENERATOR', gi, 'induced O action rank =', rank3(induced))

print('ALL_5_GENERATORS_STABLE =', all_stable)

if all_stable:
    assert len(induced_actions) == 5
    print('CONCLUSION: O is an H-submodule under the verified ambient L5^4 action.')
else:
    print('CONCLUSION: O is NOT an H-submodule under the verified ambient L5^4 action.')

PASS = all_stable
print('O2-2 PASS =', PASS)
if not PASS:
    raise AssertionError('O2-2 FAIL: obstruction image is not H-stable under the verified ambient tuple action')
