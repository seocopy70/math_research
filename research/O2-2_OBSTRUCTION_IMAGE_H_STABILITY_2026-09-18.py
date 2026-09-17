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

# O1-0 contains the authoritative 204-dimensional Lie degree-5 basis and
# coordinate map. Reuse these exact coordinates; do not treat the 1024-word
# associative space as L5.
o1_0 = runpy.run_path(ROOT + 'O1-0_OBSTRUCTION_ANNIHILATES_I_2026-09-18.py')
L5_basis = np.array(o1_0['L5_basis'], dtype=np.int64) % P
L5_left = np.array(o1_0['L5_left'], dtype=np.int64) % P
rows = list(o1_0['rows'])
assert L5_basis.shape == (1024, 204)
assert L5_left.shape == (204, 204)
assert len(rows) == 204
assert rank3(L5_basis) == 204
assert np.array_equal((L5_left @ L5_basis[rows, :]) % P, np.eye(204, dtype=np.int64))

# The sanity artifact supplies the already verified D1/D4/D5 associative
# substitution machinery and the five Sp4(F3) presentation generators.
san = runpy.run_path(ROOT + 'A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py')
gens = san['gens']
WORDS5 = san['WORDS5']
INDEX5 = san['INDEX5']
degree_action_matrix = san['degree_action_matrix']

assert len(gens) == 5
assert len(WORDS5) == 1024
assert len(INDEX5) == 1024

# Convert each verified associative D5 action to its induced action on the
# actual Lie subspace L5. This gives the unique 204 x 204 matrix A5_lie with
# A5_assoc * L5_basis = L5_basis * A5_lie.
D5_actions = []
for g in gens:
    A5_assoc = degree_action_matrix(g, 5, WORDS5, INDEX5) % P
    transformed_basis = (A5_assoc @ L5_basis) % P
    A5_lie = (L5_left @ transformed_basis[rows, :]) % P
    assert A5_lie.shape == (204, 204)
    assert np.array_equal((L5_basis @ A5_lie) % P, transformed_basis)
    D5_actions.append(A5_lie)

assert all(A.shape == (204, 204) for A in D5_actions)

# The ambient obstruction target is L5^4 = four 204-dimensional blocks.
def tuple_action(A5_lie, X):
    X = np.array(X, dtype=np.int64) % P
    assert X.shape[0] == 816
    out = np.zeros_like(X)
    for b in range(4):
        sl = slice(204 * b, 204 * (b + 1))
        out[sl, :] = (A5_lie @ X[sl, :]) % P
    return out


print('O2-2: H-STABILITY OF THE OBSTRUCTION IMAGE O')
print('O basis shape =', O_basis.shape)
print('dim O =', rank3(O_basis))
print('number of H generators =', len(gens))
print('generator convention = the 5 Sp4(F3) presentation generators from the sanity artifact')
print('tuple target = L5^4 = 4 x 204 coordinates')
print('degree-5 associative source = sanity degree_action_matrix (1024 x 1024)')
print('induced Lie degree-5 action = 204 x 204 via authoritative L5_basis/L5_left')
print('tuple action = direct sum of the SAME induced D5^Lie(g) on all four obstruction blocks')

all_stable = True
induced_actions = []
for gi, (g, A5_lie) in enumerate(zip(gens, D5_actions)):
    transformed = tuple_action(A5_lie, O_basis)
    augmented_rank = rank3(np.column_stack([O_basis, transformed]))
    stable = augmented_rank == 10
    print('GENERATOR', gi, 'D5^Lie shape =', A5_lie.shape)
    print('GENERATOR', gi, 'rank([O | gO]) =', augmented_rank)
    print('GENERATOR', gi, 'O_STABLE =', stable)
    if not stable:
        all_stable = False
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
