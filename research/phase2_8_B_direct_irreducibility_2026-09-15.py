"""Phase 2-8B: direct irreducibility certificate for M=ker(N)/im(N).

Avoids AtlasRep, group isomorphisms, and construction of an external
25-dimensional module. Uses the exact 25x25 H-action matrices certified in
Phase 2-7 and computes the associative algebra they generate. Dimension 625
means the generated algebra is Mat_25(F3), hence M is irreducible.

This stage does NOT by itself identify M with L(2,1).
"""
from pathlib import Path
import runpy
import numpy as np

P = 3
ROOT = Path(__file__).resolve().parents[1]
ns = runpy.run_path(str(ROOT / 'research' / 'phase2_7_M_quotient_2026-09-15.py'))
MA = [np.array(x, dtype=np.int64) % P for x in ns['MA']]

def rref_basis(vecs, ncols):
    B = np.zeros((0, ncols), dtype=np.int64)
    piv = []
    for v in vecs:
        w = np.array(v, dtype=np.int64, copy=True) % P
        for r, c in enumerate(piv):
            if w[c]:
                w = (w - w[c] * B[r]) % P
        nz = np.flatnonzero(w)
        if nz.size == 0:
            continue
        c = int(nz[0])
        if w[c] == 2:
            w = (2 * w) % P
        for r in range(B.shape[0]):
            if B[r, c]:
                B[r] = (B[r] - B[r, c] * w) % P
        B = np.vstack([B, w])
        piv.append(c)
        if len(piv) == ncols:
            break
    return B % P

# The identity is included. Repeatedly multiply every current basis element
# on the left by each generator; this enumerates all generator words.
basis = [np.eye(25, dtype=np.int64)]
for step in range(1000):
    candidates = list(basis)
    for B in basis:
        for A in MA:
            candidates.append((A @ B) % P)
    RB = rref_basis([X.reshape(-1) for X in candidates], 625)
    old = len(basis)
    basis = [RB[i].reshape(25, 25) for i in range(RB.shape[0])]
    new = len(basis)
    print(f'closure step {step + 1}: dimension {new}')
    if new == old:
        break
else:
    raise RuntimeError('closure did not stabilize within 1000 steps')

print('PHASE 2-8B / DIRECT IRREDUCIBILITY')
print('generator count =', len(MA))
print('associative algebra dimension =', len(basis))
print('full matrix algebra dimension =', 625)
print('FULL_MATRIX_ALGEBRA =', len(basis) == 625)
if len(basis) != 625:
    raise SystemExit(2)
print('CERTIFICATE: <A_1,...,A_5>_alg = Mat_25(F_3).')
print('CONCLUSION: M is irreducible as an H-module.')
print('NOTE: M ~= L(2,1) is NOT claimed solely from this computation.')
