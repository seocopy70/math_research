import ast
import json
import os
from itertools import product
from pathlib import Path

import numpy as np

P = 3
ART = Path('artifacts/a3_4_data.npz')
OUT = Path('artifacts/a3_4_bracket_result.json')

# Self-guard: this consumer is artifact-only. It may not import/execute
# research phase modules or use dynamic imports.
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
data = np.load(ART, allow_pickle=False)
W = data['W'].astype(np.int64) % P
Wd = data['Wd'].astype(np.int64) % P
gens = data['gens'].astype(np.int64) % P
I_W = data['I_W'].astype(np.int64) % P
I_Wd = data['I_Wd'].astype(np.int64) % P

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


def apply_word_linear_map(word, g):
    cur = {(): 1}
    for letter in word:
        image = {}
        for i in range(4):
            c = int(g[i, letter - 1]) % P
            if c:
                image[(i + 1,)] = c
        nxt = {}
        for a, ca in cur.items():
            for b, cb in image.items():
                w = a + b
                nxt[w] = (nxt.get(w, 0) + ca * cb) % P
        cur = {w: c for w, c in nxt.items() if c}
    return cur


def degree_action_matrix(g):
    G = np.zeros((256, 256), dtype=np.int64)
    for j, w in enumerate(WORDS4):
        for ww, c in apply_word_linear_map(w, g).items():
            G[INDEX4[ww], j] = (G[INDEX4[ww], j] + c) % P
    return G


def coords(B, Y):
    B = np.array(B, dtype=np.int64) % P
    Y = np.array(Y, dtype=np.int64) % P
    out = np.zeros((B.shape[1], Y.shape[1]), dtype=np.int64)
    for j in range(Y.shape[1]):
        A = np.column_stack([B, Y[:, j]]) % P
        m, naug = A.shape
        r = 0
        piv = []
        for c in range(naug - 1):
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
        assert len(piv) == B.shape[1]
        for rr, c in enumerate(piv):
            out[c, j] = A[rr, -1]
    return out


def solve3(A, b):
    R = np.column_stack([A.copy() % P, b.reshape(-1, 1) % P])
    m, naug = R.shape
    nvar = naug - 1
    r = 0
    piv = []
    for c in range(nvar):
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
    assert not any(np.all(R[i, :nvar] == 0) and R[i, nvar] != 0 for i in range(r, m))
    x = np.zeros(nvar, dtype=np.int64)
    for rr, c in enumerate(piv):
        x[c] = R[rr, nvar]
    return len(piv), x, nvar - len(piv)


# Recover the coordinate actions entirely from the stored ambient artifact.
A4 = [degree_action_matrix(g) for g in gens]
AW = [coords(W, (G @ W) % P) for G in A4]
AWd = [coords(Wd, (G @ Wd) % P) for G in A4]

assert W.shape == (256, 45) and Wd.shape == (256, 45)
assert I_W.shape == (45, 35) and I_Wd.shape == (45, 35)
assert rank3(W @ I_W) == 35 and rank3(Wd @ I_Wd) == 35

# Reconstruct the unique A3-4-9 intertwiner fixed by the artifact's I-identification.
n = 45
rows, rhs = [], []
idx = lambda r, c: r * n + c
for A, Ad in zip(AW, AWd):
    for r in range(n):
        for c in range(n):
            row = np.zeros(n * n, dtype=np.int64)
            for k in range(n):
                row[idx(k, c)] = (row[idx(k, c)] + Ad[r, k]) % P
                row[idx(r, k)] = (row[idx(r, k)] - A[k, c]) % P
            rows.append(row)
            rhs.append(0)
for r in range(n):
    for c in range(35):
        row = np.zeros(n * n, dtype=np.int64)
        for k in range(n):
            row[idx(r, k)] = (row[idx(r, k)] + I_W[k, c]) % P
        rows.append(row)
        rhs.append(int(I_Wd[r, c]))

M = np.array(rows, dtype=np.int64) % P
b = np.array(rhs, dtype=np.int64) % P
rank_system, sol, nullity = solve3(M, b)
tau = sol.reshape((45, 45)) % P

assert rank3(tau) == 45
assert all(np.array_equal((Ad @ tau) % P, (tau @ A) % P) for A, Ad in zip(AW, AWd))
assert np.array_equal((tau @ I_W) % P, I_Wd % P)


def bracket_with_fixed_generator(v, h):
    # Exact associative expansion of [v, X_h] = v X_h - X_h v.
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v):
        c = int(coeff) % P
        if not c:
            continue
        w = WORDS4[j]
        out[INDEX5[w + (h,)]] = (out[INDEX5[w + (h,)]] + c) % P
        out[INDEX5[(h,) + w]] = (out[INDEX5[(h,) + w]] - c) % P
    return out


# The actual A3-4 test:
# tau([v, X_h]) = [tau(v), X_h].
# Here X_h is fixed; it is NOT transformed by any generator.
per_generator = []
diff_blocks = []
for gi, h in enumerate(range(1, 5)):
    lhs = np.column_stack([
        bracket_with_fixed_generator((W @ np.eye(45, dtype=np.int64)[:, j]) % P, h)
        for j in range(45)
    ])
    rhs = np.column_stack([
        bracket_with_fixed_generator((Wd @ tau[:, j]) % P, h)
        for j in range(45)
    ])
    D = (rhs - lhs) % P
    rank = rank3(D)
    per_generator.append({
        'generator': h,
        'discrepancy_shape': list(D.shape),
        'discrepancy_rank': int(rank),
        'compatible': bool(rank == 0),
    })
    diff_blocks.append(D)

D_stacked = np.vstack(diff_blocks)
obstruction_rank = rank3(D_stacked)
compatible = obstruction_rank == 0

result = {
    'schema': 'A3-4-bracket-compatibility-v1',
    'field': 'F3',
    'artifact_schema_expected': 'A3-4-data-v2',
    'github_sha': os.environ.get('GITHUB_SHA', 'local'),
    'tau_rank': int(rank3(tau)),
    'tau_intertwiner': True,
    'tau_fixes_I_identification': True,
    'tau_constrained_system_rank': int(rank_system),
    'tau_constrained_system_unknowns': int(n * n),
    'tau_constrained_system_nullity': int(nullity),
    'per_generator': per_generator,
    'stacked_discrepancy_shape': list(D_stacked.shape),
    'stacked_obstruction_rank': int(obstruction_rank),
    'bracket_compatible_for_all_4_generators': bool(compatible),
    'identity_tested': 'tau([v,X_h]) = [tau(v),X_h]',
    'result': 'PASS' if compatible else 'FAIL',
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')

print('A3-4 BRACKET COMPATIBILITY — ARTIFACT-ONLY')
print('SELF-GUARD = PASS')
print('GITHUB_SHA =', result['github_sha'])
print('artifact schema expected =', result['artifact_schema_expected'])
print('dim W45 =', rank3(W), 'dim Wd =', rank3(Wd), 'dim I =', rank3(W @ I_W))
print('tau constrained-system rank =', rank_system, 'unknowns =', n * n, 'nullity =', nullity)
print('tau rank =', rank3(tau))
print('TAU_INTERTWINER = True')
print('TAU_FIXES_I_IDENTIFICATION = True')
for item in per_generator:
    print('GENERATOR', item['generator'], 'DISCREPANCY_RANK =', item['discrepancy_rank'], 'COMPATIBLE =', item['compatible'])
print('STACKED_DISCREPANCY_SHAPE =', tuple(D_stacked.shape))
print('STACKED_BRACKET_OBSTRUCTION_RANK =', obstruction_rank)
print('BRACKET_COMPATIBLE_FOR_ALL_4_GENERATORS =', compatible)
print('IDENTITY = tau([v,X_h]) = [tau(v),X_h]')
print('RESULT =', result['result'])
print('RESULT_JSON =', OUT)
