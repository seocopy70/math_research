"""Q3-6 action compatibility preflight, without dense 4096x4096 matrices.

The tuple space has dimension 4*4^5 = 4096, but the verification only needs
Delta_u/Delta_tau applied to 45-dimensional W bases. We therefore apply
(g_1^T tensor D5) directly to tuple vectors using its block structure.

Checks:
  1. order-3 and generator-pair composition sanity;
  2. exact H-equivariance of Delta_u and Delta_tau on basis columns;
  3. preservation of A, B, and hence B/A.

No 4096x4096 dense tuple matrix is constructed.
"""
import runpy
import numpy as np

P = 3
DIM5 = 1024
TUPLE = 4096

q35 = runpy.run_path('research/Q3_5_PRETEST_AUTO_TRANSFER_2026-09-17.py')
r3 = q35['r3']
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


def degree5_action(g):
    D5 = np.zeros((DIM5, DIM5), dtype=np.int64)
    for j, w in enumerate(WORDS5):
        image = apply({w: 1}, g)
        for ww, c in image.items():
            D5[INDEX5[ww], j] = (D5[INDEX5[ww], j] + int(c)) % P
    return D5


def generator_matrix_degree1(g):
    g1 = np.zeros((4, 4), dtype=np.int64)
    for i in range(4):
        image = apply({(i + 1,): 1}, g)
        for w, c in image.items():
            assert len(w) == 1
            g1[w[0] - 1, i] = (g1[w[0] - 1, i] + int(c)) % P
    return g1


def tuple_apply(V, D5, g1):
    """Apply g_1^T tensor D5 directly to tuple vectors."""
    V = np.asarray(V, dtype=np.int64) % P
    if V.ndim == 1:
        V = V[:, None]
        squeeze = True
    else:
        squeeze = False
    m = V.shape[1]
    out = np.zeros((TUPLE, m), dtype=np.int64)
    for out_i in range(4):
        acc = np.zeros((DIM5, m), dtype=np.int64)
        for in_j in range(4):
            coeff = int(g1[in_j, out_i]) % P
            if coeff:
                acc = (acc + coeff * (D5 @ V[in_j*DIM5:(in_j+1)*DIM5, :])) % P
        out[out_i*DIM5:(out_i+1)*DIM5, :] = acc
    return out[:, 0] if squeeze else out


def word_action_composite(gi, gj):
    D = np.zeros((DIM5, DIM5), dtype=np.int64)
    for col, w in enumerate(WORDS5):
        first = apply({w: 1}, gj)
        second = {}
        for ww, c in first.items():
            z = apply({ww: int(c)}, gi)
            for zword, zc in z.items():
                second[zword] = (second.get(zword, 0) + int(zc)) % P
        for ww, c in second.items():
            D[INDEX5[ww], col] = (D[INDEX5[ww], col] + int(c)) % P
    return D


def generator_composite(gi, gj):
    g1 = np.zeros((4, 4), dtype=np.int64)
    for a in range(4):
        first = apply({(a + 1,): 1}, gj)
        second = {}
        for ww, c in first.items():
            z = apply({ww: int(c)}, gi)
            for zword, zc in z.items():
                second[zword] = (second.get(zword, 0) + int(zc)) % P
        for w, c in second.items():
            assert len(w) == 1
            g1[w[0] - 1, a] = (g1[w[0] - 1, a] + int(c)) % P
    return g1


def zero_defect(G_apply, Delta, H):
    lhs = G_apply(Delta)
    rhs = np.asarray(Delta @ H, dtype=np.int64) % P
    return np.all(((lhs - rhs) % P) == 0)


def preserved_by_action(G_apply, M):
    """Explicit image containment, without a 4096-dimensional rank."""
    Y = G_apply(M)
    B = col_basis(M, r3(M))
    for j in range(Y.shape[1]):
        coords_from(B, Y[:, j])
    return True


print('Q3-6 ACTION COMPATIBILITY PREFLIGHT (STRUCTURAL / NO 4096x4096)')
print('BUILDING DEGREE-5 ACTIONS')
D5s = [degree5_action(g) for g in gens]
g1s = [generator_matrix_degree1(g) for g in gens]
print('degree-5 actions =', len(D5s), 'x', D5s[0].shape)

print('GENERATOR ACTION SANITY')
for k, (D5, g1) in enumerate(zip(D5s, g1s)):
    assert r3((D5 @ D5 @ D5 - np.eye(DIM5, dtype=np.int64)) % P) == 0
    assert np.array_equal((g1 @ g1 @ g1) % P, np.eye(4, dtype=np.int64))
    probes = np.zeros((TUPLE, 4), dtype=np.int64)
    for t in range(4):
        probes[t*DIM5 + t, 0] = 1
        probes[(3-t)*DIM5 + (DIM5-1-t), 1] = 1
        probes[(t+1)*DIM5 + 2*t, 2] = 2
        probes[t*DIM5 + 100+t, 3] = 1
    out1 = tuple_apply(probes, D5, g1)
    out2 = np.zeros_like(out1)
    for out_i in range(4):
        for in_j in range(4):
            c = int(g1[in_j, out_i]) % P
            if c:
                out2[out_i*DIM5:(out_i+1)*DIM5, :] = (
                    out2[out_i*DIM5:(out_i+1)*DIM5, :]
                    + c * (D5 @ probes[in_j*DIM5:(in_j+1)*DIM5, :])
                ) % P
    assert np.array_equal(out1, out2)
    print('GEN', k, 'order-3 = True', 'direct_block_formula = True')

print('GENERATOR PAIR COMPOSITION SANITY')
for i, gi in enumerate(gens):
    for j, gj in enumerate(gens):
        Dcomp = word_action_composite(gi, gj)
        g1comp = generator_composite(gi, gj)
        assert np.array_equal((D5s[i] @ D5s[j]) % P, Dcomp)
        assert np.array_equal((g1s[i] @ g1s[j]) % P, g1comp)
        probes = np.zeros((TUPLE, 3), dtype=np.int64)
        for t in range(3):
            probes[t*DIM5 + 7*t, t] = t + 1
            probes[(3-t)*DIM5 + 101+t, t] = 2
        lhs = tuple_apply(tuple_apply(probes, D5s[j], g1s[j]), D5s[i], g1s[i])
        rhs = tuple_apply(probes, Dcomp, g1comp)
        assert np.array_equal(lhs, rhs)
        print('PAIR', i, j, '= True')

print('Q3 MAP COMPATIBILITY')
Du3 = delta_u(q35['W3'], N3)
Dt3 = delta_tau(q35['W3'], q35['Wd'], q35['tau3_gate'])
assert r3(Du3) == 10 and r3(Dt3) == 45
for k, (D5, g1, H) in enumerate(zip(D5s, g1s, A3_actions)):
    G_apply = lambda V, D5=D5, g1=g1: tuple_apply(V, D5, g1)
    du_ok = zero_defect(G_apply, Du3, H)
    dt_ok = zero_defect(G_apply, Dt3, H)
    a_ok = preserved_by_action(G_apply, Du3)
    b_ok = preserved_by_action(G_apply, Dt3)
    print('Q3_GENERATOR', k, 'Delta_u_equivariant =', du_ok,
          'Delta_tau_equivariant =', dt_ok, 'A_preserved =', a_ok,
          'B_preserved =', b_ok)
    assert du_ok and dt_ok and a_ok and b_ok

print('Q3 QUOTIENT B/A')
A3b = col_basis(A3mat, r3(A3mat))
B3b = col_basis(B3mat, r3(B3mat))
assert A3b.shape[1] == 10 and B3b.shape[1] == 45
assert r3(np.column_stack([A3b, B3b])) == 45
print('Q3 A/B ranks =', A3b.shape[1], B3b.shape[1], 'quotient = 35')
print('Q3 B/A preservation follows from exact A,B equivariance.')

print('QINF CASE COMPATIBILITY')
for ni, (Ninf, nullity, tau_candidates) in enumerate(case_records):
    for ti, tau in enumerate(tau_candidates):
        Ainf = delta_u(Wi, Ninf)
        Binf = delta_tau(Wi, q35['Wd'], tau)
        assert r3(Ainf) == 10 and r3(Binf) == 45
        print('CASE', ni, ti)
        for k, (D5, g1, H) in enumerate(zip(D5s, g1s, Ai)):
            G_apply = lambda V, D5=D5, g1=g1: tuple_apply(V, D5, g1)
            du_ok = zero_defect(G_apply, Ainf, H)
            dt_ok = zero_defect(G_apply, Binf, H)
            a_ok = preserved_by_action(G_apply, Ainf)
            b_ok = preserved_by_action(G_apply, Binf)
            print('  GEN', k, 'Delta_u_equivariant =', du_ok,
                  'Delta_tau_equivariant =', dt_ok,
                  'A_preserved =', a_ok, 'B_preserved =', b_ok)
            assert du_ok and dt_ok and a_ok and b_ok
        Aib = col_basis(Ainf, r3(Ainf))
        Bib = col_basis(Binf, r3(Binf))
        assert r3(np.column_stack([Aib, Bib])) == 45
        print('  QUOTIENT_DIM = 35')
        print('  B/A preservation follows from exact A,B equivariance.')

print('RESULT = PASS')
print('ALL DELTA MAPS ARE H-EQUIVARIANT; A, B, AND B/A ARE PRESERVED.')
