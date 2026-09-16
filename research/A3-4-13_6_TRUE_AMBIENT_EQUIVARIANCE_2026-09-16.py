import runpy
import numpy as np
from itertools import product

P = 3
ROOT = 'research/'

# Load the verified A3-4-10 construction.
ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=int) % P
A_W = [np.array(a, dtype=int) % P for a in ns['A_W']]
D_tau = np.vstack([np.array(d, dtype=int) % P for d in ns['diffs']])
B_W = ns['B_W']
B_Wd = ns['B_Wd']
X_intertwiner = np.array(ns['X_intertwiner'], dtype=int) % P

assert W.shape == (256, 45)
assert D_tau.shape == (4096, 45)
assert rank3(D_tau) == 45
assert len(A_W) == 5

# Load the same exact generators on V used by the verified construction.
ns1 = runpy.run_path(ROOT + 'phase2_1_invariant_space_verification_2026-09-15.py')
gens = ns1['gens']
apply_linear_map = ns1['apply_linear_map']

# Degree-5 tensor basis.
words5 = list(product(range(1, 5), repeat=5))
index5 = {w: i for i, w in enumerate(words5)}

def apply_degree5_dict(v, g):
    out = {}
    for i, coeff in enumerate(v):
        coeff = int(coeff) % P
        if coeff == 0:
            continue
        w = words5[i]
        cur = {(): coeff}
        for letter in w:
            image = apply_linear_map({(letter,): 1}, g)
            nxt = {}
            for pref, pc in cur.items():
                for ww, c in image.items():
                    z = pref + ww
                    nxt[z] = (nxt.get(z, 0) + pc * c) % P
            cur = {z:c for z,c in nxt.items() if c % P}
        for z, c in cur.items():
            out[z] = (out.get(z, 0) + c) % P
    result = np.zeros(1024, dtype=int)
    for w, c in out.items():
        result[index5[w]] = c % P
    return result

# The four components of Delta_tau are degree-5 vectors.  Since the output
# is Hom(V, T^5), H acts on both the output tensor and the input-generator
# index.  Build the induced action directly from the V matrix:
# (g.f)(v) = g( f(g^{-1}v) ).
Vgens = []
for g in gens:
    M = np.zeros((4,4), dtype=int)
    for j in range(4):
        image = apply_linear_map({(j+1,):1}, g)
        for w,c in image.items():
            assert len(w) == 1
            M[w[0]-1,j] = (M[w[0]-1,j] + c) % P
    Vgens.append(M)

def inv3(A):
    n = A.shape[0]
    aug = np.concatenate([A.copy() % P, np.eye(n, dtype=int)], axis=1)
    for c in range(n):
        p = next(i for i in range(c,n) if aug[i,c] % P)
        aug[[c,p]] = aug[[p,c]]
        if aug[c,c] == 2:
            aug[c] = (2*aug[c]) % P
        for i in range(n):
            if i != c and aug[i,c]:
                aug[i] = (aug[i] - aug[i,c]*aug[c]) % P
    return aug[:,n:] % P

def rho5_tensor(v, M):
    return apply_degree5_dict(v, M)

def transform_hom_column(D, gi, j):
    # D is 4096 x 45, stacked as 4 blocks of 1024, one per input X_i.
    # Output for basis vector w_j under conjugation action:
    # each input column mixes by M^{-1}; tensor output gets M^tensor5.
    M = Vgens[gi]
    Minv = inv3(M)
    blocks = [D[k*1024:(k+1)*1024, j] for k in range(4)]
    transformed = [rho5_tensor(b, M) for b in blocks]
    outblocks = []
    for k in range(4):
        acc = np.zeros(1024, dtype=int)
        for ell in range(4):
            acc = (acc + int(Minv[ell,k]) * transformed[ell]) % P
        outblocks.append(acc)
    return np.concatenate(outblocks) % P

# Verify the actual ambient identity rho_5(g) on Hom(V,T^5):
# rho_5(g) Delta_tau(w) = Delta_tau(A_g w).
failures = []
for gi, Ag in enumerate(A_W):
    for j in range(45):
        lhs = transform_hom_column(D_tau, gi, j)
        rhs = (D_tau @ Ag[:,j]) % P
        if not np.array_equal(lhs, rhs):
            failures.append((gi,j))

print('A3-4-13.6 / TRUE AMBIENT HOM(V,T^5) EQUIVARIANCE')
print('dim W =', rank3(W))
print('rank Delta_tau =', rank3(D_tau))
print('generators tested =', len(A_W))
print('basis vectors tested =', 45)
print('total equivariance identities tested =', len(A_W)*45)
print('failures =', len(failures))
if failures:
    print('first failures =', failures[:10])
    raise AssertionError('TRUE AMBIENT EQUIVARIANCE FAILED')
print('RESULT: TRUE AMBIENT EQUIVARIANCE PASS')
print('Delta_tau is H-equivariant in the ambient Hom(V,T^5) representation.')
print('ALL A3-4-13.6 CHECKS COMPLETED')
