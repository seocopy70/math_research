import runpy
import numpy as np

ns = runpy.run_path('research/phase2_1_invariant_space_verification_2026-09-15.py')
add = ns['add']; neg = ns['neg']; bracket = ns['bracket']; vec4 = ns['vec4']; rank3 = ns['rank3']
apply_linear_map = ns['apply_linear_map']
X1, X2, X3, X4 = ns['X1'], ns['X2'], ns['X3'], ns['X4']
gens = ns['gens']; R4_matrix = ns['R4_matrix']; index4 = ns['index4']

T = bracket(bracket(bracket(X3, X4), X1), X1)

def multidegree(A):
    for w in A:
        d = [0, 0, 0, 0]
        for x in w:
            d[x - 1] += 1
        return tuple(d)
    return (0, 0, 0, 0)

assert multidegree(T) == (2, 0, 1, 1)

basis = []
combined = R4_matrix.copy()
queue = [T]
seen = set()
while queue:
    a = queue.pop(0)
    key = tuple(sorted(a.items()))
    if key in seen:
        continue
    seen.add(key)
    old_rank = rank3(combined)
    candidate = np.column_stack([combined, vec4(a)])
    new_rank = rank3(candidate)
    if new_rank > old_rank:
        basis.append(a)
        combined = candidate
    for g in gens:
        queue.append(apply_linear_map(a, g))

dim_orbit_span_Q4 = len(basis)
rank_combined = rank3(combined)
rank_R = rank3(R4_matrix)
W45_basis = ns['basis']
W45_matrix = np.column_stack([vec4(a) for a in W45_basis])
rank_W45 = rank3(W45_matrix)
rank_T_plus_W45 = rank3(np.column_stack([W45_matrix, vec4(T)]))
rank_W45_plus_orbit = rank3(np.column_stack([W45_matrix, np.column_stack([vec4(a) for a in basis])]))
fixed_by = []
for i, g in enumerate(gens, 1):
    if apply_linear_map(T, g) == T:
        fixed_by.append(i)

print('PHASE 2-20 / A3-4-7 MULTIDEGREE (2,0,1,1) TARGET ORBIT')
print('target_multidegree =', multidegree(T))
print('rank(R4) =', rank_R)
print('distinct orbit elements =', len(seen))
print('dim orbit span in Q4 =', dim_orbit_span_Q4)
print('rank([R4 | orbit_basis]) =', rank_combined)
print('dim W45 =', rank_W45)
print('rank([W45 | T]) =', rank_T_plus_W45)
print('rank([W45 | orbit_basis]) =', rank_W45_plus_orbit)
print('generators fixing T exactly =', fixed_by)

assert rank_R == 5
assert len(seen) > 1
assert dim_orbit_span_Q4 == 45
assert rank_combined == 50
assert rank_W45 == 45
assert rank_T_plus_W45 == 45
assert rank_W45_plus_orbit == 45
print('CERTIFICATE: T generates exactly the existing 45-dimensional W45 module in Q4.')
