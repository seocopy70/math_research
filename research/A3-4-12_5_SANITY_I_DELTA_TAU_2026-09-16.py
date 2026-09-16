import runpy
import numpy as np

P = 3
ROOT = 'research/'

# Reuse the exact A3-4-10 construction.  This sanity check is deliberately
# downstream of the verified intertwiner X and does not alter any prior code.
ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
Wd = np.array(ns['Wd'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
K_Wd = np.array(ns['K_Wd'], dtype=np.int64) % P
K_coord = np.array(ns['K_coord'], dtype=np.int64) % P
X = np.array(ns['X_intertwiner'], dtype=np.int64) % P
D_tau = np.array(ns['D'], dtype=np.int64) % P

# A3-4-10 uses I_W as a 45 x 35 coordinate matrix for the intersection I.
assert I_W.shape == (45, 35)
assert rank3(I_W) == 35
assert K_Wd.shape == (45, 35)
assert rank3(K_Wd) == 35

# 1. Directly verify the affine constraint X(I) = K in Wd-coordinates.
X_I = (X @ I_W) % P
X_I_equals_K = np.array_equal(X_I, K_Wd)
assert X_I_equals_K

# 2. Verify this is NOT the pointwise identity condition X(I)=I.
# I and K are represented in different module coordinates here; compare their
# ambient degree-4 vectors after embedding through W and Wd.
I_ambient = (W @ I_W) % P
K_ambient = (Wd @ K_Wd) % P
X_I_ambient = (Wd @ X_I) % P
assert np.array_equal(X_I_ambient, K_ambient)

# The key logical check: if X fixed I pointwise, then Wd*X*I_W would equal
# W*I_W.  Test that ambient equality directly.
X_I_equals_I_ambient = np.array_equal(X_I_ambient, I_ambient)

# 3. Evaluate Delta_tau on a basis of I and compute its restricted rank.
# D_tau is the 4096 x 45 stacked ambient degree-5 obstruction matrix.
D_tau_I = (D_tau @ I_W) % P
rank_D_tau_I = rank3(D_tau_I)

# 4. Record whether I is contained in ker Delta_tau.
I_in_kernel = (rank_D_tau_I == 0)

print('A3-4-12.5 / SANITY CHECK: I, X(I)=K, AND DELTA_TAU|_I')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_W))
print('dim K =', rank3(K_Wd))
print('X(I) = K (direct ambient check) =', X_I_equals_K)
print('X(I) = I (pointwise ambient check) =', X_I_equals_I_ambient)
print('rank Delta_tau =', rank3(D_tau))
print('rank Delta_tau restricted to I =', rank_D_tau_I)
print('I subset ker(Delta_tau) =', I_in_kernel)

# The expected outcome is: X(I)=K, X(I)!=I, and Delta_tau|I has nonzero rank.
assert X_I_equals_K
assert not X_I_equals_I_ambient
assert rank_D_tau_I > 0
assert not I_in_kernel

print('RESULT: the earlier apparent contradiction is resolved.')
print('RESULT: A3-4-10 uses X(I)=K, not X|_I = identity.')
print('RESULT: I is not contained in ker Delta_tau; hence rank Delta_tau = 45 is consistent.')
print('ALL A3-4-12.5 CHECKS COMPLETED')
