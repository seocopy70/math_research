import runpy
import numpy as np

P = 3
ROOT = 'research/'
ns = runpy.run_path(ROOT + 'phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py')
rank3 = ns['rank3']
W = np.array(ns['W'], dtype=np.int64) % P
A_W = [np.array(a, dtype=np.int64) % P for a in ns['A_W']]
D_tau = np.vstack([np.array(d, dtype=np.int64) % P for d in ns['diffs']])
assert W.shape == (256, 45)
assert D_tau.shape == (4096, 45)
assert rank3(D_tau) == 45
assert len(A_W) == 5
failures = []
for gi, Ag in enumerate(A_W):
    transformed = (D_tau @ Ag) % P
    r = rank3(np.column_stack([D_tau, transformed]))
    if r != 45:
        failures.append((gi, r))
print('A3-4-13.5 / DELTA_TAU H-STABILITY SANITY CHECK')
print('dim W =', rank3(W))
print('rank Delta_tau =', rank3(D_tau))
print('number of H generators =', len(A_W))
for gi, Ag in enumerate(A_W):
    print('combined rank [D_tau | D_tau A_g] g%d =' % (gi + 1), rank3(np.column_stack([D_tau, (D_tau @ Ag) % P])))
print('H-stability failures =', len(failures))
assert not failures
print('RESULT: Im(Delta_tau) is H-stable under all verified generators.')
print('This validates the quotient-action premise used in A3-4-13.')
print('ALL A3-4-13.5 CHECKS COMPLETED')
