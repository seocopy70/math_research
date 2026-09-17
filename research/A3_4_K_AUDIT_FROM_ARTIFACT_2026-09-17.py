import ast
import os
from pathlib import Path
import numpy as np

P = 3
ARTIFACT = Path('artifacts/a3_4_data.npz')
META = Path('artifacts/a3_4_data_meta.json')


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


def ast_guard():
    # Consumer must not load or execute another research phase/module.
    path = Path(__file__)
    tree = ast.parse(path.read_text(encoding='utf-8'))
    banned_names = {'importlib', 'runpy', 'exec_module'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                assert alias.name.split('.')[0] not in banned_names, alias.name
        if isinstance(node, ast.ImportFrom):
            assert (node.module or '').split('.')[0] not in banned_names, node.module
        if isinstance(node, ast.Attribute):
            assert node.attr not in banned_names, node.attr
    print('SELF-GUARD = PASS')


assert ARTIFACT.exists(), ARTIFACT
assert META.exists(), META
ast_guard()

z = np.load(ARTIFACT, allow_pickle=False)
W = z['W'].astype(np.int64) % P
Wd = z['Wd'].astype(np.int64) % P
gens = z['gens'].astype(np.int64) % P
R4 = z['R4'].astype(np.int64) % P
I_W = z['I_W'].astype(np.int64) % P
I_Wd = z['I_Wd'].astype(np.int64) % P
I_ambient = z['I_ambient'].astype(np.int64) % P

assert W.shape == (256, 45)
assert Wd.shape == (256, 45)
assert gens.shape == (5, 4, 4)
assert rank3(W) == 45
assert rank3(Wd) == 45
assert rank3(R4) == 15
assert I_W.shape == (45, 35)
assert I_Wd.shape == (45, 35)
assert rank3(I_ambient) == 35
assert np.array_equal((W @ I_W) % P, I_ambient)
assert np.array_equal((Wd @ I_Wd) % P, I_ambient)

# Confirm that the artifact really contains G-stable W and Wd; no reconstruction from source code.
for g in gens:
    # The degree-4 action is reconstructed directly from the generator substitution.
    # This is a structural check on the stored subspaces, not a call to another script.
    def apply_word(word):
        out = {(): 1}
        for letter in word:
            image = {(i,): int(g[i-1, letter-1]) % P for i in range(1, 5) if int(g[i-1, letter-1]) % P}
            nxt = {}
            for a, ca in out.items():
                for b, cb in image.items():
                    w = a + b
                    nxt[w] = (nxt.get(w, 0) + ca * cb) % P
            out = {w: c for w, c in nxt.items() if c}
        return out
    G = np.zeros((256, 256), dtype=np.int64)
    from itertools import product
    words = list(product(range(1, 5), repeat=4))
    index = {w: i for i, w in enumerate(words)}
    for j, w in enumerate(words):
        for ww, c in apply_word(w).items():
            G[index[ww], j] = c
    assert rank3(np.column_stack([W, (G @ W) % P])) == 45
    assert rank3(np.column_stack([Wd, (G @ Wd) % P])) == 45

print('A3-4 K AUDIT — ARTIFACT CONSUMER')
print('GITHUB_SHA =', os.environ.get('GITHUB_SHA', 'UNKNOWN'))
print('artifact schema = A3-4-data-v1')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_ambient))
print('K_DEFINITION_IN_THIS_STAGE = I = W ∩ Wd')
print('ARTIFACT_READ_ONLY_CHECKS = PASS')
print('RESULT = PASS')
