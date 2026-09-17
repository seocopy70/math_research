import hashlib
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


def column_basis_indices(M):
    M = np.array(M, dtype=np.int64) % P
    basis = np.empty((M.shape[0], 0), dtype=np.int64)
    indices = []
    current_rank = 0
    for j in range(M.shape[1]):
        candidate = np.column_stack([basis, M[:, j]])
        r = rank3(candidate)
        if r > current_rank:
            basis = candidate
            indices.append(j)
            current_rank = r
    return indices, basis


# O1-1 is the authoritative quotient-factorization computation.
# It already reuses the corrected A3-4-10 obstruction pipeline and proves
# D_stack = barD_stack o pi through W / I_W.
o1 = runpy.run_path(ROOT + 'O1-1_QUOTIENT_FACTORIZATION_2026-09-18.py')

D_stack = np.array(o1['D_stack'], dtype=np.int64) % P
barD_stack = np.array(o1['barD_stack'], dtype=np.int64) % P
C_cols = list(o1['C_cols'])
pi = np.array(o1['pi'], dtype=np.int64) % P

assert D_stack.shape == (816, 45)
assert barD_stack.shape == (816, 10)
assert pi.shape == (10, 45)
assert rank3(D_stack) == 10
assert rank3(barD_stack) == 10
assert np.array_equal((barD_stack @ pi) % P, D_stack)

# O = Im(barD_stack) is a 10-dimensional subspace of the obstruction
# target L5^4.  Because barD_stack has rank 10 and has exactly 10 columns,
# its ten columns themselves are a concrete ordered basis of O.
O_basis = barD_stack.copy()
O_basis_indices, pivot_basis = column_basis_indices(barD_stack)
assert O_basis_indices == list(range(10))
assert np.array_equal(pivot_basis, O_basis)
assert rank3(O_basis) == 10

# Record a reproducible digest of the concrete 816 x 10 coordinate matrix.
O_basis_bytes = np.ascontiguousarray(O_basis, dtype=np.int64).tobytes()
O_basis_sha256 = hashlib.sha256(O_basis_bytes).hexdigest()

# The ten basis vectors are indexed by the fixed quotient-coordinate basis
# used by O1-1.  Their target coordinates are 4 blocks of 204 coordinates
# (one block per generator obstruction), i.e. the ambient degree-5 target
# L5^4 representation used by the corrected A3-4-10 pipeline.
assert O_basis.shape == (4 * 204, 10)

print('O2-1: CONCRETE BASIS OF THE OBSTRUCTION IMAGE')
print('W dimension =', 45)
print('dim I_W =', 35)
print('quotient dimension =', 10)
print('D_stack shape =', D_stack.shape)
print('D_stack rank =', rank3(D_stack))
print('barD_stack shape =', barD_stack.shape)
print('barD_stack rank =', rank3(barD_stack))
print('quotient complement columns inherited from O1-1 =', C_cols)
print('O = Im(barD_stack) ambient dimension =', O_basis.shape[0])
print('O basis matrix shape =', O_basis.shape)
print('O basis column indices in barD_stack =', O_basis_indices)
print('O basis rank =', rank3(O_basis))
print('O basis SHA256 =', O_basis_sha256)
print('O1-1 factorization identity =', np.array_equal((barD_stack @ pi) % P, D_stack))
print('INTERSECTION_TEST_WITH_U = NOT DEFINED (O and U live in different ambient spaces)')
print('CONCLUSION: O is now represented concretely by the ordered 816 x 10 basis matrix O_basis = barD_stack.')
print('NEXT: O2-2 tests H-stability of O using the corrected degree-5 tuple action.')

PASS = (
    D_stack.shape == (816, 45)
    and rank3(D_stack) == 10
    and barD_stack.shape == (816, 10)
    and rank3(barD_stack) == 10
    and O_basis_indices == list(range(10))
    and np.array_equal((barD_stack @ pi) % P, D_stack)
)
print('O2-1 PASS =', PASS)
if not PASS:
    raise AssertionError('O2-1 FAIL: concrete 10-dimensional obstruction-image basis was not established')
