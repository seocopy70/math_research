import ast
import json
import os
from itertools import product
from pathlib import Path

import numpy as np

P = 3
ART = Path('artifacts/a3_4_data.npz')
TAU = Path('artifacts/a3_4_tau.npy')
RESULT = Path('artifacts/a3_4_bracket_result.json')

# Independent reviewer: no phase-module imports or dynamic execution.
SOURCE = Path(__file__).read_text(encoding='utf-8')
TREE = ast.parse(SOURCE)
for node in ast.walk(TREE):
    if isinstance(node, ast.ImportFrom) and any(a.name in {'research', 'runpy', 'importlib'} for a in node.names):
        raise RuntimeError('forbidden research-module import')
    if isinstance(node, ast.Import) and any(a.name in {'runpy', 'importlib'} for a in node.names):
        raise RuntimeError('forbidden dynamic import')
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'exec_module':
        raise RuntimeError('forbidden exec_module')

assert ART.exists(), 'upstream A3-4 artifact missing'
assert TAU.exists(), 'primary tau output missing'
assert RESULT.exists(), 'primary bracket result missing'

data = np.load(ART, allow_pickle=False)
W = data['W'].astype(np.int64) % P
Wd = data['Wd'].astype(np.int64) % P
I_W = data['I_W'].astype(np.int64) % P
I_Wd = data['I_Wd'].astype(np.int64) % P
tau = np.load(TAU, allow_pickle=False).astype(np.int64) % P
primary = json.loads(RESULT.read_text(encoding='utf-8'))

WORDS4 = list(product(range(1, 5), repeat=4))
INDEX4 = {w: i for i, w in enumerate(WORDS4)}
WORDS5 = list(product(range(1, 5), repeat=5))
INDEX5 = {w: i for i, w in enumerate(WORDS5)}


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


def bracket_matrix_fixed_generator(h):
    # Direct 1024 x 256 matrix for v -> [v,X_h] in the associative word basis.
    B = np.zeros((1024, 256), dtype=np.int64)
    for j, w in enumerate(WORDS4):
        B[INDEX5[w + (h,)], j] = 1
        B[INDEX5[(h,) + w], j] = (-1) % P
    return B

assert W.shape == (256, 45)
assert Wd.shape == (256, 45)
assert tau.shape == (45, 45)
assert rank3(tau) == 45
assert rank3(W @ I_W) == 35
assert rank3(Wd @ I_Wd) == 35
assert np.array_equal((tau @ I_W) % P, I_Wd % P)

# Independent direct-matrix verification of the exact requested identity.
# For each fixed h:
#     tau([v,X_h]) = [tau(v),X_h]
# The two sides are compared as 1024 x 45 matrices.
review = []
blocks = []
for h in range(1, 5):
    B = bracket_matrix_fixed_generator(h)
    lhs = (B @ W) % P
    rhs = (B @ Wd @ tau) % P
    D = (rhs - lhs) % P
    rank = rank3(D)
    review.append({
        'generator': h,
        'lhs_shape': list(lhs.shape),
        'rhs_shape': list(rhs.shape),
        'discrepancy_rank': int(rank),
        'compatible': bool(rank == 0),
    })
    blocks.append(D)

stacked = np.vstack(blocks)
stacked_rank = rank3(stacked)
review_compatible = stacked_rank == 0

# Cross-check against the primary calculation, but do not use the primary rank
# to determine this review result.
primary_by_gen = {x['generator']: x for x in primary['per_generator']}
for x in review:
    assert x['generator'] in primary_by_gen
    assert x['discrepancy_rank'] == primary_by_gen[x['generator']]['discrepancy_rank']
assert stacked_rank == primary['stacked_obstruction_rank']
assert review_compatible == primary['bracket_compatible_for_all_4_generators']

print('A3-4 BRACKET COMPATIBILITY — INDEPENDENT REVIEW')
print('SELF-GUARD = PASS')
print('GITHUB_SHA =', os.environ.get('GITHUB_SHA', 'local'))
print('tau rank =', rank3(tau))
print('tau fixes I identification =', np.array_equal((tau @ I_W) % P, I_Wd % P))
for x in review:
    print('GENERATOR', x['generator'], 'DIRECT_DISCREPANCY_RANK =', x['discrepancy_rank'], 'COMPATIBLE =', x['compatible'])
print('STACKED_DIRECT_DISCREPANCY_SHAPE =', tuple(stacked.shape))
print('STACKED_DIRECT_OBSTRUCTION_RANK =', stacked_rank)
print('PRIMARY_RESULT_MATCH = PASS')
print('INDEPENDENT_REVIEW_RESULT =', 'PASS' if review_compatible else 'FAIL')
