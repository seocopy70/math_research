import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Existing A3-4-10 affine/module intertwiner calculation.
ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns['rank3']
B_W = [np.array(B, dtype=np.int64) % P for B in ns['B_W']]
D_tau = np.vstack([np.array(D, dtype=np.int64) % P for D in ns['diffs']])
X = np.array(ns['X_intertwiner'], dtype=np.int64) % P
W = np.array(ns['W'], dtype=np.int64) % P

# Reuse the verified H-endomorphism N defining u = I+N.
nsN = runpy.run_path(ROOT + 'phase2_3_endH_optimized_2026-09-15.py')
N = np.array(nsN['N'], dtype=np.int64) % P
assert W.shape == (256,45)
assert N.shape == (45,45)
assert rank3(N) == 10
assert np.array_equal((N @ N) % P, np.zeros((45,45), dtype=np.int64))

# Both maps now live in exactly the same ambient Hom(V, tensor^5):
# Delta_tau(w) = ([Xw,X_i] - X([w,X_i]))_i
# Delta_u(w)   = ([Nw,X_i])_i
D_u = np.vstack([(B @ N) % P for B in B_W])

assert D_tau.shape == (4096,45)
assert D_u.shape == (4096,45)
rank_tau = rank3(D_tau)
rank_u = rank3(D_u)
assert rank_tau == 45
assert rank_u == 10

# Compute dim(Im Delta_tau + Im Delta_u), hence intersection dimension.
rank_sum = rank3(np.column_stack([D_tau, D_u]))
intersection_dim = rank_tau + rank_u - rank_sum

# Containment test Im Delta_u subset Im Delta_tau.
containment = rank_sum == rank_tau

print('A3-4-12 / IMAGE INTERSECTION DELTA_U VS DELTA_TAU')
print('ambient dimension =', 4096)
print('rank Delta_tau =', rank_tau)
print('rank Delta_u =', rank_u)
print('rank(Im Delta_tau + Im Delta_u) =', rank_sum)
print('dim(Im Delta_u intersect Im Delta_tau) =', intersection_dim)
print('Im Delta_u subset Im Delta_tau =', containment)
print('expected containment intersection = 10')

if containment and intersection_dim == 10:
    print('RESULT: Im Delta_u is contained in Im Delta_tau, with full 10-dimensional overlap.')
    print('RESULT: the ambient rank-45 obstruction splits at least as a 10D control component plus a 35D quotient component.')
else:
    print('RESULT: Im Delta_u is NOT fully contained in Im Delta_tau; the 45-vs-10 relation is not a simple nested decomposition.')

assert intersection_dim >= 0
print('ALL A3-4-12 CHECKS COMPLETED')
