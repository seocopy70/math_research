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


def rref_solve(A, b):
    R = np.column_stack([np.array(A, dtype=np.int64) % P,
                          np.array(b, dtype=np.int64).reshape(-1, 1) % P])
    m, naug = R.shape
    n = naug - 1
    r = 0
    piv = []
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        piv.append(c)
        r += 1
        if r == m:
            break
    inconsistent = any(
        np.all(R[i, :n] % P == 0) and R[i, n] % P != 0
        for i in range(r, m)
    )
    if inconsistent:
        return len(piv), None, n - len(piv)
    x = np.zeros(n, dtype=np.int64)
    for rr, c in enumerate(piv):
        x[c] = R[rr, n]
    return len(piv), x, n - len(piv)


# Authoritative obstruction and Lie degree-5 coordinates.
o1 = runpy.run_path(ROOT + 'O1-0_OBSTRUCTION_ANNIHILATES_I_2026-09-18.py')
D_stack = np.array(o1['D_L5'], dtype=np.int64) % P
L5_basis = np.array(o1['L5_basis'], dtype=np.int64) % P
L5_left = np.array(o1['L5_left'], dtype=np.int64) % P
rows = list(o1['rows'])
assert D_stack.shape == (816, 45)
assert L5_basis.shape == (1024, 204)
assert L5_left.shape == (204, 204)
assert len(rows) == 204
assert rank3(D_stack) == 10
assert np.array_equal((L5_left @ L5_basis[rows, :]) % P,
                      np.eye(204, dtype=np.int64))

# Reuse the verified A3-4-10 ambient pipeline for the exact domain action.
a3410 = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
A_W = [np.array(A, dtype=np.int64) % P for A in a3410['A_W']]
assert len(A_W) == 5
assert all(A.shape == (45, 45) for A in A_W)

# Reuse the verified associative degree-5 action, then restrict it to L5.
san = runpy.run_path(ROOT + 'A3_4_10_BRACKET_PIPELINE_SANITY_2026-09-17.py')
gens = san['gens']
WORDS5 = san['WORDS5']
INDEX5 = san['INDEX5']
degree_action_matrix = san['degree_action_matrix']
assert len(gens) == 5

A5_lie = []
for g in gens:
    A5_assoc = degree_action_matrix(g, 5, WORDS5, INDEX5) % P
    transformed_basis = (A5_assoc @ L5_basis) % P
    A5 = (L5_left @ transformed_basis[rows, :]) % P
    assert np.array_equal((L5_basis @ A5) % P, transformed_basis)
    A5_lie.append(A5)


def solve_block_matrix(D, A_domain, A_target):
    # Test the natural 4-block equivariance law
    # D A_domain = (T tensor A_target) D,
    # solving T in M_4(F_3) from the data rather than assuming T.
    target_blocks = [
        (D[h * 204:(h + 1) * 204, :] @ A_domain) % P
        for h in range(4)
    ]

    columns = []
    for h in range(4):
        for k in range(4):
            candidate = np.zeros((816, 45), dtype=np.int64)
            candidate[h * 204:(h + 1) * 204, :] = (
                A_target @ D[k * 204:(k + 1) * 204, :]
            ) % P
            columns.append(candidate.reshape(-1))

    M = np.column_stack(columns) % P
    b = np.concatenate([B.reshape(-1) for B in target_blocks]) % P
    # The concatenation above orders blocks by h; columns use the same
    # flattening convention through candidate.reshape(-1).
    rank_system, sol, nullity = rref_solve(M, b)
    if sol is None:
        return None, rank_system, nullity, False

    T = sol.reshape((4, 4)) % P
    rhs = np.zeros((816, 45), dtype=np.int64)
    for h in range(4):
        block = np.zeros((204, 45), dtype=np.int64)
        for k in range(4):
            block = (block + T[h, k] * (A_target @ D[k * 204:(k + 1) * 204, :])) % P
        rhs[h * 204:(h + 1) * 204, :] = block
    exact = np.array_equal(rhs % P, D @ A_domain % P)
    return T, rank_system, nullity, exact


print('O2-2R: ACTUAL OBSTRUCTION EQUIVARIANCE LAW')
print('D_stack shape =', D_stack.shape)
print('rank(D_stack) =', rank3(D_stack))
print('domain action = authoritative A_W from corrected A3-4-10 pipeline')
print('target action = authoritative induced 204 x 204 Lie degree-5 action')
print('candidate law = D_stack A_W = (T_g tensor A5_lie) D_stack')
print('T_g is solved from data; it is NOT assumed.')

all_exact = True
solutions = []
for gi, (A_dom, A5) in enumerate(zip(A_W, A5_lie)):
    T, r_sys, nullity, exact = solve_block_matrix(D_stack, A_dom, A5)
    print('GENERATOR', gi, 'T exists =', T is not None)
    print('GENERATOR', gi, 'equation-system rank =', r_sys)
    print('GENERATOR', gi, 'equation-system nullity =', nullity)
    if T is not None:
        print('GENERATOR', gi, 'T_g =')
        print(T)
        print('GENERATOR', gi, 'exact equivariance =', exact)
        solutions.append(T)
    else:
        solutions.append(None)
    if not exact:
        all_exact = False

print('ALL_5_GENERATORS_HAVE_EXACT_4x4_BLOCK_MIXING =', all_exact)
if all_exact:
    print('CONCLUSION: the obstruction tuple admits the tested natural block-mixing equivariance law.')
else:
    print('CONCLUSION: the obstruction tuple does NOT admit a uniform 4x4 block-mixing law with the verified L5 action.')

PASS = all_exact
print('O2-2R PASS =', PASS)
if not PASS:
    raise AssertionError('O2-2R FAIL: no exact tested block-mixing equivariance law for every generator')
