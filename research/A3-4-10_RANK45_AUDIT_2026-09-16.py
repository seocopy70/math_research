import runpy
import numpy as np

P = 3
ROOT = 'research/'

ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
Wd = np.array(ns['Wd'], dtype=np.int64) % P
I_W = np.array(ns['I_W'], dtype=np.int64) % P
X = np.array(ns['X_intertwiner'], dtype=np.int64) % P
D = np.array(ns['D'], dtype=np.int64) % P
B_W = ns['B_W']
B_Wd = ns['B_Wd']

E = ((Wd @ X) - W) % P
D_from_E = np.vstack([
    ((B_Wd[g] @ X) - B_W[g]) % P
    for g in range(4)
])

print('A3-4-10 RANK-45 DIMENSION AUDIT')
print('dim W45 =', rank3(W))
print('dim Wd =', rank3(Wd))
print('dim I =', rank3(I_W))
print('rank(tau - id) as ambient L4 map =', rank3(E))
print('nullity(tau - id) on W45 =', 45 - rank3(E))
print('rank((tau-id) restricted to I) =', rank3((E @ I_W) % P))
print('tau fixes I exactly =', np.count_nonzero((E @ I_W) % P) == 0)
print('obstruction D shape =', D.shape)
print('rank(D) reported by A3-4-10 =', rank3(D))
print('rank(D reconstructed from E) =', rank3(D_from_E))
print('D_equals_bracket_of_ambient_displacement =', np.array_equal(D, D_from_E))
print('DIMENSIONAL_BOUND rank(D) <= rank(E) =', rank3(D) <= rank3(E))
print('EXPECTED_UPPER_BOUND rank(tau-id) <= 10 =', rank3(E) <= 10)
print('EXPECTED_UPPER_BOUND rank(D) <= 10 =', rank3(D) <= 10)

assert np.array_equal(D, D_from_E)
assert np.array_equal((E @ I_W) % P, np.zeros_like(E @ I_W))
assert rank3(E) <= 10
assert rank3(D) <= rank3(E)

print('AUDIT PASSED: A3-4-10 obstruction rank is dimensionally consistent with tau-id.')
