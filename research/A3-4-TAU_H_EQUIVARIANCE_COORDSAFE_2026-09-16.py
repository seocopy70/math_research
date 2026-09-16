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


def inverse3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    n = A.shape[0]
    E = np.column_stack([A, np.eye(n, dtype=np.int64)]) % P
    for c in range(n):
        q = next((i for i in range(c, n) if E[i, c]), None)
        assert q is not None
        E[[c, q]] = E[[q, c]]
        if E[c, c] == 2:
            E[c] = (2 * E[c]) % P
        for i in range(n):
            if i != c and E[i, c]:
                E[i] = (E[i] - E[i, c] * E[c]) % P
    return E[:, n:]


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C
            r = q
            if r == target:
                break
    assert r == target
    return B


def add(A, B):
    C = dict(A)
    for w, a in B.items():
        C[w] = (C.get(w, 0) + a) % P
        if C[w] == 0:
            del C[w]
    return C


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


# Canonical W45 and H generators/actions from the authoritative phase-2 script.
ns = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
W_words = ns['basis']
gens = ns['gens']
apply_linear_map = ns['apply_linear_map']
index4 = ns['index4']

def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items():
        v[index4[w]] = c % P
    return v

W45 = np.column_stack([vec4(a) for a in W_words])
assert W45.shape == (256, 45) and rank3(W45) == 45

# Independently reconstruct Wd = <H.d>.
d = bracket({(1, 1, 1): 1}, {(2,): 1})
queue = [d]
seen = {tuple(vec4(d).tolist())}
for a in queue:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            queue.append(b)
Wd = basis_columns(np.column_stack([vec4(a) for a in queue]), 45)
assert rank3(Wd) == 45

# True recursive relation space R4=[L1,[L1,R]], dimension 15.
R = {(1, 2): 1, (2, 1): 2, (3, 4): 1, (4, 3): 2}
R3 = [bracket({(i,): 1}, R) for i in range(1, 5)]
R4_raw = [bracket({(i,): 1}, r) for i in range(1, 5) for r in R3]
R4 = basis_columns(np.column_stack([vec4(a) for a in R4_raw]), 15)
assert rank3(R4) == 15

# Quotient coordinates using the canonical ambient basis [R4 | W45].
B = np.column_stack([R4, W45])
assert rank3(B) == 60
rows = []
RB = np.empty((0, 60), dtype=np.int64)
r = 0
for i in range(256):
    C = np.vstack([RB, B[i:i+1]])
    q = rank3(C)
    if q > r:
        rows.append(i)
        RB = C
        r = q
        if r == 60:
            break
assert r == 60
L = inverse3(RB)
Q_W45 = (L @ W45[rows])[15:, :] % P
Q_Wd = (L @ Wd[rows])[15:, :] % P
assert rank3(Q_W45) == 45 and rank3(Q_Wd) == 45

tau = (inverse3(Q_Wd) @ Q_W45) % P
assert rank3(tau) == 45

# Fixed coordinate maps: ambient 256D -> the named 45D basis.
def choose_rows(Basis):
    rr = 0
    RB = np.empty((0, 45), dtype=np.int64)
    rows = []
    for i in range(256):
        C = np.vstack([RB, Basis[i:i+1]])
        q = rank3(C)
        if q > rr:
            rows.append(i)
            RB = C
            rr = q
            if rr == 45:
                break
    assert rr == 45
    return rows, inverse3(RB)

rows_W, inv_W = choose_rows(W45)
rows_d, inv_d = choose_rows(Wd)

def coords(Basis, rows_b, inv_b, X):
    # X is ambient 256 x k and is known to lie in span(Basis).
    C = (inv_b @ X[rows_b]) % P
    assert rank3(Basis @ C % P) == rank3(X)
    return C

# Direct action: ambient action first, then re-coordinate in each basis.
def action_on_words(words):
    out = []
    for g in gens:
        cols = [vec4(apply_linear_map(w, g)) for w in words]
        out.append(np.column_stack(cols))
    return out

# W45 direct action and Wd direct action are computed independently in their own bases.
AW_ambient = action_on_words(W_words)
Ad_ambient = []
Wd_words = []
# Convert the chosen Wd basis columns back to sparse word dictionaries via ambient coordinates.
# Instead of relying on a sparse inverse conversion, act on the basis through its ambient vectors
# by constructing the transformed vector with the generator's matrix action on words below.
# Build a reusable ambient 256x256 action matrix from its action on all degree-4 words.
all_words = list(index4.keys())

def ambient_action_matrix(g):
    cols = []
    for w in all_words:
        a = apply_linear_map({w: 1}, g)
        cols.append(vec4(a))
    return np.column_stack(cols)

G_ambient = [ambient_action_matrix(g) for g in gens]
AW = [coords(W45, rows_W, inv_W, X) for X in AW_ambient]
Ad = [coords(Wd, rows_d, inv_d, G @ Wd) for G in G_ambient]

# First sanity check: direct Wd action equals the action obtained by tau-conjugation.
Ad_induced = [(tau @ A @ inverse3(tau)) % P for A in AW]
direct_vs_induced = [rank3((D - I) % P) for D, I in zip(Ad, Ad_induced)]

# Decisive intertwining residuals.
residuals = [(tau @ A - D @ tau) % P for A, D in zip(AW, Ad)]
residual_ranks = [rank3(R) for R in residuals]

# Explicit common intersection I=W45∩Wd, for diagnostic localization.
M = np.column_stack([W45, (-Wd) % P])
null_cols = []
# Nullspace of M via direct RREF.
def nullspace3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    m, n = A.shape
    Rr = A.copy(); piv=[]; rr=0
    for c in range(n):
        q = next((i for i in range(rr,m) if Rr[i,c]), None)
        if q is None: continue
        Rr[[rr,q]]=Rr[[q,rr]]
        if Rr[rr,c]==2: Rr[rr]=(2*Rr[rr])%P
        for i in range(m):
            if i!=rr and Rr[i,c]: Rr[i]=(Rr[i]-Rr[i,c]*Rr[rr])%P
        piv.append(c); rr+=1
        if rr==m: break
    free=[j for j in range(n) if j not in piv]
    out=[]
    for f in free:
        x=np.zeros(n,dtype=np.int64); x[f]=1
        for r,c in enumerate(piv): x[c]=(-Rr[r,f])%P
        out.append(x)
    return out

N = nullspace3(M)
I_basis = np.column_stack([W45 @ z[:45] % P for z in N]) if N else np.empty((256,0),dtype=np.int64)
# N has one free coordinate per common-intersection direction; rank should be 35.
dim_I = rank3(I_basis)
assert dim_I == 35

# Check whether I is H-stable; if stable, D|I must vanish (sanity check).
I_action_ranks = []
D_on_I_ranks = []
for G, D in zip(G_ambient, residuals):
    XI = G @ I_basis % P
    I_action_ranks.append(rank3(np.column_stack([I_basis, XI])) - dim_I)
    # D is W45->Wd in coordinates; convert I coordinates to W45 coords and residual to ambient Wd.
    # I_basis itself is already ambient; re-coordinate it in W45.
    CI = coords(W45, rows_W, inv_W, I_basis)
    DI_ambient = Wd @ (D @ CI % P) % P
    D_on_I_ranks.append(rank3(DI_ambient))

print('A3-4 TAU H-EQUIVARIANCE — COORDINATE-SAFE CHECK')
print('dim W45 =', rank3(W45))
print('dim Wd =', rank3(Wd))
print('dim R4_true =', rank3(R4))
print('rank([R4 | W45]) =', rank3(B))
print('rank(Q_W45) =', rank3(Q_W45))
print('rank(Q_Wd) =', rank3(Q_Wd))
print('rank(tau) =', rank3(tau))
print('generator count =', len(gens))
print('direct_vs_induced_Ad residual ranks =', direct_vs_induced)
print('tau equivariance residual ranks =', residual_ranks)
print('dim I =', dim_I)
print('I H-stability defect ranks =', I_action_ranks)
print('D_i restricted-to-I ranks =', D_on_I_ranks)
print('TAU_IS_H_EQUIVARIANT =', all(r == 0 for r in residual_ranks))
print('DIRECT_EQUALS_INDUCED =', all(r == 0 for r in direct_vs_induced))

assert all(r == 0 for r in direct_vs_induced)

# No mathematical conclusion is asserted if equivariance fails; the diagnostics above identify
# whether the failure is in the independently reconstructed action or localized outside I.
if all(r == 0 for r in residual_ranks):
    print('RESULT: tau is H-equivariant; W45 and Wd are isomorphic as Sp4(F3)-modules.')
else:
    print('RESULT: tau is NOT H-equivariant for at least one generator; inspect residual localization before interpretation.')

print('ALL COORDINATE-SAFE ACTION CONSTRUCTION CHECKS PASSED')
