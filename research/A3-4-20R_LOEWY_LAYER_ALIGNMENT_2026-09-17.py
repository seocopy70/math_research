import runpy
import subprocess
import tempfile
import numpy as np

P = 3
ROOT = 'research/'

# Reuse the exact A3-4-16 matrices and reconstruct the unique rank-10
# intertwiner from A3-4-17.  A3-4-20R fixes the invalid radical/socle
# definitions used in A3-4-20: it identifies actual simple submodules
# (socle candidates) and simple quotients (top candidates) directly.
ns16 = runpy.run_path(ROOT + 'A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py')
BA = [np.array(x, dtype=np.int64) % P for x in ns16['BA_gens']]
K = [np.array(x, dtype=np.int64) % P for x in ns16['K_gens']]
rank3 = ns16['rank3']

assert len(BA) == len(K) == 5
assert all(T.shape == (35, 35) for T in BA + K)
I35 = np.eye(35, dtype=np.int64)

# Exact F_3 RREF.
def rref3(A):
    R = np.array(A, dtype=np.int64) % P
    m, n = R.shape
    pivots = []
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if R[i, c]), None)
        if q is None:
            continue
        if q != r:
            R[[r, q]] = R[[q, r]]
        if R[r, c] == 2:
            R[r] = (2 * R[r]) % P
        for i in range(m):
            if i != r and R[i, c]:
                R[i] = (R[i] - R[i, c] * R[r]) % P
        pivots.append(c)
        r += 1
        if r == m:
            break
    return R, pivots

def nullspace_basis(A):
    R, piv = rref3(A)
    n = A.shape[1]
    ps = set(piv)
    out = []
    for f in range(n):
        if f in ps:
            continue
        v = np.zeros(n, dtype=np.int64)
        v[f] = 1
        for rr, pc in enumerate(piv):
            v[pc] = (-R[rr, f]) % P
        out.append(v)
    return np.column_stack(out) if out else np.zeros((n, 0), dtype=np.int64)

def col_basis(A):
    A = np.array(A, dtype=np.int64) % P
    if A.shape[1] == 0:
        return np.zeros((A.shape[0], 0), dtype=np.int64)
    _, piv = rref3(A)
    return A[:, piv] % P

def rank(A):
    return len(rref3(A)[1])

def inv_mod3(A):
    A = np.array(A, dtype=np.int64) % P
    n = A.shape[0]
    aug = np.column_stack([A, np.eye(n, dtype=np.int64)])
    R, piv = rref3(aug)
    assert len(piv) == n and piv == list(range(n))
    return R[:, n:] % P

def row_pivot_indices(A):
    # Independent rows of A are pivot columns of A^T.
    _, piv = rref3(A.T)
    return piv

def coords_in_basis(U, V):
    # U is full-column-rank d-dimensional basis in F_3^35.
    # Solve U*C=V using an invertible set of d rows of U.
    d = U.shape[1]
    rows = row_pivot_indices(U)
    assert len(rows) == d
    Ui = inv_mod3(U[rows, :])
    C = (Ui @ V[rows, :]) % P
    assert np.array_equal((U @ C - V) % P, np.zeros_like(V))
    return C

def extend_basis(U):
    # Extend columns of U to a basis using standard coordinate vectors.
    T = U.copy() % P
    for i in range(35):
        e = np.zeros((35, 1), dtype=np.int64)
        e[i, 0] = 1
        C = np.column_stack([T, e])
        if rank(C) > T.shape[1]:
            T = C
        if T.shape[1] == 35:
            break
    assert T.shape == (35, 35) and rank(T) == 35
    return T

def restrict_action(gens, U):
    return [coords_in_basis(U, (G @ U) % P) for G in gens]

def quotient_action(gens, U):
    T = extend_basis(U)
    Ti = inv_mod3(T)
    d = U.shape[1]
    out = []
    for G in gens:
        M = (Ti @ G @ T) % P
        # First d columns are the submodule U, so bottom-left is zero.
        assert np.array_equal(M[d:, :d], np.zeros((35-d, d), dtype=np.int64))
        out.append(M[d:, d:] % P)
    return out

def gap_matrix_literal(A):
    return '[' + ','.join('[' + ','.join(str(int(x) % P) for x in row) + ']' for row in A.tolist()) + ']'

def gap_matrix_list(mats):
    # GAP row-action convention: transpose our column-action matrices.
    return '[' + ','.join(gap_matrix_literal(A.T) for A in mats) + ']'

def gap_irreducible(mats):
    literal = gap_matrix_list(mats)
    code = r'''F := GF(3);;
Mraw := %s;;
ToField := function(m)
  return ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x)));
end;;
Mgens := List(Mraw,ToField);;
M := GModuleByMats(Mgens,F);;
Print(MTX.IsIrreducible(M),"\n");
QUIT;
''' % literal
    with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
        f.write(code)
        path = f.name
    try:
        proc = subprocess.run(['gap', '-q', path], text=True, capture_output=True)
    finally:
        import os
        os.unlink(path)
    if proc.returncode != 0:
        raise RuntimeError(proc.stdout + proc.stderr)
    vals = [x.strip() for x in proc.stdout.splitlines() if x.strip()]
    if not vals:
        raise RuntimeError('GAP returned no irreducibility result')
    return vals[-1] == 'true'

# Recover the unique intertwiner Q from P BA_g = K_g P.
blocks = []
for A, G in zip(BA, K):
    blocks.append((np.kron(A.T, I35) - np.kron(I35, G)) % P)
E = np.vstack(blocks) % P
assert E.shape == (6125, 1225)
R, pivots = rref3(E)
rankE = len(pivots)
assert rankE == 1224
free = next(c for c in range(E.shape[1]) if c not in set(pivots))
x = np.zeros(E.shape[1], dtype=np.int64)
x[free] = 1
for rr, pc in enumerate(pivots):
    x[pc] = (-R[rr, free]) % P
Q = x.reshape((35, 35), order='F') % P
for A, G in zip(BA, K):
    assert np.array_equal((Q @ A - G @ Q) % P, np.zeros((35, 35), dtype=np.int64))
assert rank3(Q) == 10

kerQ = nullspace_basis(Q)
imQ = col_basis(Q)
assert kerQ.shape[1] == 25 and imQ.shape[1] == 10

# Directly test the two actual Q-defined submodules and their quotients.
# A simple submodule is a socle component; a simple quotient is a top
# component.  This avoids the invalid sum(g-I)/intersection ker(g-I)
# definitions used in A3-4-20.
BA_ker_irred = gap_irreducible(restrict_action(BA, kerQ))
BA_quot_irred = gap_irreducible(quotient_action(BA, kerQ))
K_im_irred = gap_irreducible(restrict_action(K, imQ))
K_quot_im_irred = gap_irreducible(quotient_action(K, imQ))

print('A3-4-20R / ACTUAL LOEWY LAYER ALIGNMENT')
print('module_dimension = 35')
print('intertwiner_system_shape =', E.shape)
print('rank(E) =', rankE)
print('Hom_dimension = 1')
print('rank(Q) =', rank3(Q))
print('dim ker(Q) =', kerQ.shape[1])
print('dim im(Q) =', imQ.shape[1])
print('KER_Q_BA_SIMPLE =', BA_ker_irred)
print('BA_MOD_KER_Q_QUOTIENT_SIMPLE =', BA_quot_irred)
print('IMAGE_Q_K_SIMPLE =', K_im_irred)
print('K_MOD_IMAGE_Q_QUOTIENT_SIMPLE =', K_quot_im_irred)

# The key orientation conclusions are made only from actual simple
# submodule/quotient tests:
# ker Q simple => ker Q is a socle layer of B/A;
# (B/A)/ker Q simple => it is the corresponding top quotient;
# im Q simple => im Q is a socle layer of K;
# K/im Q simple => it is the corresponding top quotient.
print('B_A_EXTENSION = 0 -> S25 -> B/A -> S10 -> 0' if BA_ker_irred and BA_quot_irred else 'B_A_EXTENSION = NOT_ESTABLISHED')
print('K_EXTENSION = 0 -> S10 -> K -> S25 -> 0' if K_im_irred and K_quot_im_irred else 'K_EXTENSION = NOT_ESTABLISHED')

PASS = (BA_ker_irred and BA_quot_irred and K_im_irred and K_quot_im_irred)
print('A3-4-20R_PASS =', PASS)
print('RESULT: Q-defined kernel/image were tested as actual simple submodules and the corresponding quotients as actual simple modules.')
if not PASS:
    raise SystemExit('A3-4-20R layer simplicity/orientation test failed')
