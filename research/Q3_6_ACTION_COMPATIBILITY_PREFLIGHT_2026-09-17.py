"""Q3-6 preflight: verify degree-5 tuple action against Delta_u/Delta_tau.

This is deliberately separate from the Q3-6 fingerprint calculation. It checks
that the 4096-dimensional ambient tuple action really intertwines the maps used
to define A=Im Delta_u and B=Im Delta_tau, before any quotient action or Hom
fingerprint is attempted.
"""
import runpy
import numpy as np

P = 3
DIM4 = 256
DIM5 = 1024
TUPLE = 4096

q35 = runpy.run_path('research/Q3_5_PRETEST_AUTO_TRANSFER_2026-09-17.py')
r3 = q35['r3']
null3 = q35['null3']
col_basis = q35['col_basis']
coords_from = q35['coords_from']
apply = q35['apply']
gens = q35['gens']
WORDS5 = q35['WORDS5']
INDEX5 = q35['INDEX5']
Wi = q35['Wi']
Ai = q35['Ai']
A3_actions = q35['A3']
N3 = q35['N3']
A3mat = q35['A3mat']
B3mat = q35['B3mat']
case_records = q35['case_records']
delta_u = q35['delta_u']
delta_tau = q35['delta_tau']


def degree5_tuple_actions():
    out = []
    for g in gens:
        D5 = np.zeros((DIM5, DIM5), dtype=np.int64)
        for j, w in enumerate(WORDS5):
            image = apply({w: 1}, g)
            for ww, c in image.items():
                D5[INDEX5[ww], j] = (D5[INDEX5[ww], j] + int(c)) % P

        g1 = np.zeros((4, 4), dtype=np.int64)
        for i in range(4):
            image = apply({(i + 1,): 1}, g)
            for w, c in image.items():
                assert len(w) == 1
                g1[w[0] - 1, i] = (g1[w[0] - 1, i] + int(c)) % P

        G = np.zeros((TUPLE, TUPLE), dtype=np.int64)
        for j in range(4):
            for i in range(4):
                if g1[j, i]:
                    G[j*DIM5:(j+1)*DIM5, i*DIM5:(i+1)*DIM5] = (g1[j, i] * D5) % P
        assert r3(G) == TUPLE
        out.append(G)
    return out


def subspace_preserved(G, M):
    B = col_basis(M, r3(M))
    Y = (G @ B) % P
    return r3(np.column_stack([B, Y])) == B.shape[1]


def intertwining_defect(G, Delta, H):
    """Return rank of G Delta - Delta H."""
    D = (G @ Delta - Delta @ H) % P
    return r3(D)


def quotient_basis(Bmat, Amat):
    A = col_basis(Amat, r3(Amat))
    B = col_basis(Bmat, r3(Bmat))
    F = A.copy()
    rr = F.shape[1]
    for j in range(B.shape[1]):
        C = np.column_stack([F, B[:, j]])
        nr = r3(C)
        if nr > rr:
            F = C
            rr = nr
        if rr == B.shape[1]:
            break
    assert rr == B.shape[1]
    return A, B, F


print('Q3-6 ACTION COMPATIBILITY PREFLIGHT')
print('BUILDING 4096-D TUPLE ACTION')
G5 = degree5_tuple_actions()
print('tuple action matrices =', len(G5), 'x', G5[0].shape)

# Q3 reference: verify the defining maps themselves are H-equivariant.
print('Q3 MAP COMPATIBILITY')
Du3 = delta_u(q35['W3'], N3)
Dt3 = delta_tau(q35['W3'], q35['Wd'], q35['tau3_gate'])
assert r3(Du3) == 10 and r3(Dt3) == 45
for k, (G, H) in enumerate(zip(G5, A3_actions)):
    du_def = intertwining_defect(G, Du3, H)
    dt_def = intertwining_defect(G, Dt3, H)
    a_ok = subspace_preserved(G, Du3)
    b_ok = subspace_preserved(G, Dt3)
    print('Q3_GENERATOR', k, 'Delta_u_defect_rank =', du_def,
          'Delta_tau_defect_rank =', dt_def, 'A_preserved =', a_ok,
          'B_preserved =', b_ok)
    assert du_def == 0 and dt_def == 0 and a_ok and b_ok

# Q3 quotient prerequisite.
A3b, B3b, F3 = quotient_basis(B3mat, A3mat)
print('Q3 A/B ranks =', A3b.shape[1], B3b.shape[1], 'quotient =', B3b.shape[1]-A3b.shape[1])
for k, G in enumerate(G5):
    Y = (G @ F3) % P
    assert r3(np.column_stack([F3, Y])) == F3.shape[1]
    print('Q3_QUOTIENT_PRESERVED generator', k, '= True')

# Exhaust all six Q3-5 compatible q=infinity cases.
print('QINF CASE COMPATIBILITY')
for ni, (Ninf, nullity, tau_candidates) in enumerate(case_records):
    for ti, tau in enumerate(tau_candidates):
        Ainf = delta_u(Wi, Ninf)
        Binf = delta_tau(Wi, q35['Wd'], tau)
        assert r3(Ainf) == 10 and r3(Binf) == 45
        print('CASE', ni, ti)
        for k, (G, H) in enumerate(zip(G5, Ai)):
            du_def = intertwining_defect(G, Ainf, H)
            dt_def = intertwining_defect(G, Binf, H)
            a_ok = subspace_preserved(G, Ainf)
            b_ok = subspace_preserved(G, Binf)
            print('  GEN', k, 'Du_defect =', du_def,
                  'Dt_defect =', dt_def, 'A_preserved =', a_ok,
                  'B_preserved =', b_ok)
            assert du_def == 0 and dt_def == 0 and a_ok and b_ok
        Aib, Bib, Fi = quotient_basis(Binf, Ainf)
        assert Bib.shape[1] - Aib.shape[1] == 35
        for k, G in enumerate(G5):
            Y = (G @ Fi) % P
            assert r3(np.column_stack([Fi, Y])) == Fi.shape[1]
        print('  QUOTIENT_PRESERVED = True')

print('RESULT = PASS')
print('ALL DELTA MAPS ARE H-EQUIVARIANT; A, B, AND B/A ARE PRESERVED.')
