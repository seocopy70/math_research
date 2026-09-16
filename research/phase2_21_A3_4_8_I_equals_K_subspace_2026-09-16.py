import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Reuse the fully verified A3-4-5 construction, which exposes:
# W       : 256 x 45 ambient basis for W45
# I_W     : 45 x 35 basis for I = W45 intersect Wd, in W45 coordinates
# K_coord : 45 x 35 basis for K = ker(N), in W45 coordinates
ns = runpy.run_path(ROOT + 'phase2_18_A3_4_5_intersection_K_and_Sym2_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P

assert W.shape == (256, 45)
assert I_W.shape == (45, 35)
assert K_coord.shape == (45, 35)

# Convert both 35-dimensional subspaces into the same 256-dimensional
# ambient free-Lie degree-4 realization.
I_ambient = (W @ I_W) % P
K_ambient = (W @ K_coord) % P

assert rank3(I_ambient) == 35
assert rank3(K_ambient) == 35

# Since dim(I)=dim(K)=35, equality as actual subspaces is equivalent to
# rank([I | K]) = 35.
combined_rank = rank3(np.column_stack([I_ambient, K_ambient]))
actual_equal = (combined_rank == 35)

print('PHASE 2-21 / A3-4-8 ACTUAL SUBSPACE EQUALITY')
print('dim W45 =', rank3(W))
print('dim I = dim(W45 intersect Wd) =', rank3(I_ambient))
print('dim K = dim ker(N) =', rank3(K_ambient))
print('rank([I | K]) =', combined_rank)
print('I_EQUALS_K_AS_ACTUAL_SUBSPACES =', actual_equal)

if not actual_equal:
    # Strictly distinguish the negative case: the abstract H-module
    # isomorphism from A3-4-5 would still hold, but the embedded subspaces
    # would be different.
    print('RESULT: I and K are distinct embedded 35-dimensional subspaces.')
else:
    print('RESULT: I = K as actual subspaces of W45 in the ambient degree-4 space.')

assert actual_equal
print('ALL A3-4-8 CHECKS PASSED')
