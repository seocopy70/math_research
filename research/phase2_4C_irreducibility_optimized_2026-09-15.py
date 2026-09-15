"""Phase 2-4C optimized: decisive irreducibility test for M=ker(N)/im(N).

Same mathematical criterion as phase2_4C_irreducibility_2026-09-15.py, but
uses an incremental exact Gaussian basis in F_3^625 instead of recomputing
matrix rank from scratch for every candidate product.

If dim F_3[A1,...,A5] = 625, then the generated algebra is all of
M_25(F_3), proving M irreducible (indeed absolutely irreducible).
If the dimension is <625, this test is not by itself decisive for
reducibility; the script reports UNRESOLVED and stops.
"""
from pathlib import Path
import runpy
import numpy as np

P = 3
nM = 25
ambient = nM * nM

ns = runpy.run_path(str(Path(__file__).with_name("phase2_4B_middle_quotient_2026-09-15.py")))
G = [np.array(x, dtype=np.int64) % P for x in ns["M_actions"]]
assert len(G) == 5 and all(x.shape == (nM, nM) for x in G)

class IncrementalBasis:
    """Exact linear basis of F_3^ambient, stored in pivot-echelon form."""
    def __init__(self, dim):
        self.dim = dim
        self.rows = {}          # pivot index -> normalized vector
        self.count = 0

    def add(self, x):
        v = np.array(x, dtype=np.int64, copy=True).reshape(-1) % P
        assert v.size == self.dim
        # Reduce against existing pivots in ascending order.
        for p in sorted(self.rows):
            c = int(v[p])
            if c:
                v = (v - c * self.rows[p]) % P
        nz = np.flatnonzero(v)
        if nz.size == 0:
            return False
        p = int(nz[0])
        if v[p] == 2:
            v = (2 * v) % P
        self.rows[p] = v
        self.count += 1
        return True

def vec(M):
    return np.asarray(M, dtype=np.int64).reshape(-1) % P

basis = IncrementalBasis(ambient)
B = []

def add_matrix(X):
    X = np.asarray(X, dtype=np.int64) % P
    if basis.add(vec(X)):
        B.append(X.copy())
        return True
    return False

# Initial algebra generators.
add_matrix(np.eye(nM, dtype=np.int64) % P)
for g in G:
    add_matrix(g)

# Exact closure under left/right multiplication by the generators.
qi = 0
last_report = len(B)
while qi < len(B) and len(B) < ambient:
    X = B[qi]
    qi += 1
    for g in G:
        if add_matrix((X @ g) % P) and len(B) >= ambient:
            break
        if add_matrix((g @ X) % P) and len(B) >= ambient:
            break
    if len(B) != last_report and (len(B) <= 25 or len(B) % 25 == 0 or len(B) == ambient):
        print("algebra basis dimension =", len(B), flush=True)
        last_report = len(B)

alg_dim = len(B)
print("PHASE 2-4C OPTIMIZED")
print("dim M =", nM)
print("generated associative algebra dimension =", alg_dim)
print("full matrix algebra dimension =", ambient)

if alg_dim == ambient:
    print("RESULT = PROOF")
    print("A=M_25(F_3); therefore M has no nonzero proper invariant subspace.")
    print("M is irreducible, in fact absolutely irreducible.")
    print("STATUS=IRREDUCIBLE_PROVED_BY_FULL_MATRIX_ALGEBRA")
else:
    print("RESULT = NOT YET DECISIVE")
    print("A is a proper subalgebra; this alone does not prove reducibility.")
    print("STATUS=UNRESOLVED_AFTER_ALGEBRA_TEST")
