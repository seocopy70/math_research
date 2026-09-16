import os
import runpy
import subprocess
import tempfile
import numpy as np

P = 3
ROOT = 'research/'

# Reuse the exact A3-4-16 generators.
ns = runpy.run_path(ROOT + 'A3-4-16_STRONG_MODULAR_FINGERPRINT_2026-09-16.py')
BA = [np.array(x, dtype=np.int64) % P for x in ns['BA_gens']]
K = [np.array(x, dtype=np.int64) % P for x in ns['K_gens']]
rank3 = ns['rank3']
assert len(BA) == len(K) == 5
assert all(A.shape == (35, 35) for A in BA + K)
I35 = np.eye(35, dtype=np.int64)

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
    _, piv = rref3(A)
    return A[:, piv] % P

def rank(A):
    return len(rref3(A)[1])

def gap_rows(A):
    return '[' + ','.join('[' + ','.join(str(int(x) % P) for x in row) + ']' for row in A.tolist()) + ']'

def gap_matrix_list(mats):
    # GAP GModuleByMats uses row vectors on the right.  Our matrices act on
    # column vectors, so pass the transposed generators.
    return '[' + ','.join(gap_rows(A.T) for A in mats) + ']'

# Recover the same unique intertwiner Q from A3-4-17.
blocks = []
for A, G in zip(BA, K):
    blocks.append((np.kron(A.T, I35) - np.kron(I35, G)) % P)
E = np.vstack(blocks) % P
assert E.shape == (6125, 1225)
R, pivots = rref3(E)
assert len(pivots) == 1224
free = next(c for c in range(E.shape[1]) if c not in set(pivots))
x = np.zeros(E.shape[1], dtype=np.int64)
x[free] = 1
for rr, pc in enumerate(pivots):
    x[pc] = (-R[rr, free]) % P
Q = x.reshape((35, 35), order='F') % P
for A, G in zip(BA, K):
    assert np.array_equal((Q @ A - G @ Q) % P, np.zeros((35, 35), dtype=np.int64))
assert rank3(Q) == 10

kerQ = nullspace_basis(Q)       # 35 x 25: basis vectors as columns
imQ = col_basis(Q)              # 35 x 10: basis vectors as columns
assert kerQ.shape == (35, 25)
assert imQ.shape == (35, 10)

ba_literal = gap_matrix_list(BA)
k_literal = gap_matrix_list(K)

# GAP returns module bases as ROWS in its row-action convention.  Therefore
# the Python column-bases must be transposed before comparison.  This puts
# Soc(B/A), Soc(K), ker(Q), and im(Q) in the same 35-coordinate row space.
ker_literal = gap_rows(kerQ.T)
im_literal = gap_rows(imQ.T)

gap_code = r'''F := GF(3);;
BAraw := %s;;
Kraw := %s;;
KerRaw := %s;;
ImRaw := %s;;
ToField := function(m)
  return ImmutableMatrix(F,List(m,r->List(r,x->One(F)*x)));
end;;
BAgens := List(BAraw,ToField);;
Kgens := List(Kraw,ToField);;
MBA := GModuleByMats(BAgens,F);;
MK := GModuleByMats(Kgens,F);;
Ker := ImmutableMatrix(F,KerRaw);;
Im := ImmutableMatrix(F,ImRaw);;
SB := MTX.BasisSocle(MBA);;
SK := MTX.BasisSocle(MK);;
SocB := ImmutableMatrix(F,SB);;
SocK := ImmutableMatrix(F,SK);;
RankJoin := function(A,B)
  return RankMat(Concatenation(A,B));
end;;
EqualSpan := function(A,B)
  return Length(A) = Length(B) and RankJoin(A,B) = Length(A);
end;;
Print("A3-4-20S / DIRECT MEATAXE SOCLE VS Q ALIGNMENT\n");
Print("SOCLE_DIM_BA = ",Length(SB),"\n");
Print("SOCLE_DIM_K = ",Length(SK),"\n");
Print("KER_Q_DIM = ",Length(Ker),"\n");
Print("IMAGE_Q_DIM = ",Length(Im),"\n");
Print("SOCLE_BA_EQUALS_KER_Q = ",EqualSpan(SocB,Ker),"\n");
Print("SOCLE_K_EQUALS_IMAGE_Q = ",EqualSpan(SocK,Im),"\n");
Print("CROSS_SOCLE_BA_EQUALS_IMAGE_Q = ",EqualSpan(SocB,Im),"\n");
Print("CROSS_SOCLE_K_EQUALS_KER_Q = ",EqualSpan(SocK,Ker),"\n");
Print("SOCLE_BA_PROPER = ",(Length(SB) < MTX.Dimension(MBA)),"\n");
Print("SOCLE_K_PROPER = ",(Length(SK) < MTX.Dimension(MK)),"\n");
Print("A3-4-20S_CROSS_MATCH = ",(Length(SB)=10 and Length(SK)=25 and Length(Ker)=25 and Length(Im)=10 and EqualSpan(SocB,Im) and EqualSpan(SocK,Ker)),"\n");
Print("A3-4-20S_PASS = ",(Length(SB)=25 and Length(SK)=10 and Length(Ker)=25 and Length(Im)=10 and EqualSpan(SocB,Ker) and EqualSpan(SocK,Im)),"\n");
QUIT;
''' % (ba_literal, k_literal, ker_literal, im_literal)

with tempfile.NamedTemporaryFile('w', suffix='.g', delete=False, encoding='utf-8') as f:
    f.write(gap_code)
    path = f.name
try:
    proc = subprocess.run(['gap', '-q', path], text=True, capture_output=True)
finally:
    os.unlink(path)
print(proc.stdout, end='')
if proc.stderr:
    print('--- GAP STDERR ---')
    print(proc.stderr, end='')
if proc.returncode != 0 or 'Error,' in proc.stdout or 'Error,' in proc.stderr:
    raise SystemExit('GAP MeatAxe execution failed')
if 'A3-4-20S_PASS = true' not in proc.stdout:
    raise SystemExit('A3-4-20S socle alignment checks failed')
