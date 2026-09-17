"""Q3-6: intrinsic extension-direction test, corrected implementation.

Goal: compare the extension-direction fingerprints intrinsically, without using
Gate-0A's intertwiner T to identify q=3 and q=infinity subspaces.

For each of the six Q3-5 compatible (N,tau) choices, this script constructs
H-actions on the actual degree-5 ambient tuple space, descends the H-action to
M=B/A, constructs S10=im(N) and K=ker(N) inside W, and computes rectangular
Hom spaces.

The previous draft incorrectly treated rectangular Hom maps as square maps,
used a 45x45 action on degree-5 data, and then used a 1024x1024 action for a
4-component bracket tuple. The last error is fixed here: A and B live in
( L_5^assoc )^{\oplus 4}, of dimension 4*4^5=4096, with the generator action
including both the degree-5 word action and the generator-index mixing.
"""
import runpy
import numpy as np
from itertools import product

P = 3
q35 = runpy.run_path('research/Q3_5_PRETEST_AUTO_TRANSFER_2026-09-17.py')

r3 = q35['r3']; null3 = q35['null3']; coords_from = q35['coords_from']; col_basis = q35['col_basis']
Ai = q35['Ai']; A3_actions = q35['A3']; Wi = q35['Wi']; W3 = q35['W3']; Wd = q35['Wd']
case_records = q35['case_records']
delta_u = q35['delta_u']; delta_tau = q35['delta_tau']
apply_linear_map = q35['apply']; gens = q35['gens']
WORDS5 = q35['WORDS5']; INDEX5 = q35['INDEX5']


def hom_basis_rect(Gsrc, Gtgt):
    ns = Gsrc[0].shape[0]
    nt = Gtgt[0].shape[0]
    cols = []
    for q in range(nt * ns):
        X = np.zeros((nt, ns), dtype=np.int64)
        X.flat[q] = 1
        equations = []
        for As, At in zip(Gsrc, Gtgt):
            equations.append(((X @ As - At @ X) % P).reshape(-1))
        cols.append(np.concatenate(equations))
    C = np.column_stack(cols)
    return null3(C)


def induced_action_from_subspace(Gambient, basis):
    out = []
    d = basis.shape[1]
    for G in Gambient:
        Y = (G @ basis) % P
        C = coords_from(basis, Y)
        assert C.shape == (d, d)
        assert np.array_equal((basis @ C) % P, Y)
        out.append(C)
    return out


def quotient_action(Bmat, Amat, Gambient):
    A = col_basis(Amat, r3(Amat))
    B = col_basis(Bmat, r3(Bmat))
    da, db = A.shape[1], B.shape[1]
    assert da == 10 and db == 45

    F = A.copy(); rankF = da
    for j in range(db):
        C = np.column_stack([F, B[:, j]])
        nr = r3(C)
        if nr > rankF:
            F = C; rankF = nr
        if rankF == db:
            break
    assert F.shape == (B.shape[0], db)

    acts = []
    for G in Gambient:
        Y = (G @ F) % P
        C = coords_from(F, Y)
        assert np.array_equal((F @ C) % P, Y)
        assert r3(C[da:, :da]) == 0
        M = C[da:, da:]
        assert M.shape == (35, 35)
        acts.append(M)
    return acts


def degree5_generator_matrices():
    """Build the H-action on the 4-component degree-5 bracket tuple space.

    Each bracket component is a 4^5=1024-dimensional word space, so the
    concatenated Delta_u/Delta_tau target has dimension 4096.  If gX_i =
    sum_j g1[j,i] X_j, then
        g([w,X_i]) = sum_j g1[j,i] [g w, X_j].
    Thus the tuple action has block (j,i) equal to g1[j,i] * D5.
    """
    out = []
    for g in gens:
        D5 = np.zeros((1024, 1024), dtype=np.int64)
        for j, w in enumerate(WORDS5):
            a = {w: 1}
            image = apply_linear_map(a, g)
            for ww, c in image.items():
                D5[INDEX5[ww], j] = (D5[INDEX5[ww], j] + int(c)) % P

        g1 = np.zeros((4, 4), dtype=np.int64)
        for i in range(4):
            image = apply_linear_map({(i + 1,): 1}, g)
            for w, c in image.items():
                assert len(w) == 1
                g1[w[0] - 1, i] = (g1[w[0] - 1, i] + int(c)) % P

        G = np.zeros((4096, 4096), dtype=np.int64)
        for j in range(4):
            for i in range(4):
                if g1[j, i]:
                    G[j*1024:(j+1)*1024, i*1024:(i+1)*1024] = (g1[j, i] * D5) % P
        assert r3(G) == 4096
        out.append(G)
    return out


def fingerprint(W_actions, N, Bmat, Amat, G5):
    S10 = col_basis(N, r3(N))
    K = np.column_stack(null3(N))
    assert S10.shape[1] == 10
    assert K.shape[1] == 35

    GS10 = induced_action_from_subspace(W_actions, S10)
    GK = induced_action_from_subspace(W_actions, K)
    GM = quotient_action(Bmat, Amat, G5)

    h_s10_m = hom_basis_rect(GS10, GM)
    h_m_s10 = hom_basis_rect(GM, GS10)
    h_s10_k = hom_basis_rect(GS10, GK)
    h_k_s10 = hom_basis_rect(GK, GS10)
    end_m = hom_basis_rect(GM, GM)
    end_k = hom_basis_rect(GK, GK)

    return {
        'dim_S10': 10,
        'dim_M': 35,
        'dim_K': 35,
        'Hom_S10_to_M': len(h_s10_m),
        'Hom_M_to_S10': len(h_m_s10),
        'Hom_S10_to_K': len(h_s10_k),
        'Hom_K_to_S10': len(h_k_s10),
        'End_M': len(end_m),
        'End_K': len(end_k),
    }


print('Q3-6 INTRINSIC EXTENSION-DIRECTION TEST — CORRECTED')
print('BUILDING DEGREE-5 H ACTION ON 4096-D TUPLE SPACE')
G5 = degree5_generator_matrices()
assert len(G5) == 5 and all(G.shape == (4096, 4096) for G in G5)
print('degree-5 tuple action matrices =', len(G5), 'x', G5[0].shape)

N3 = q35['N3']
A3mat = q35['A3mat']
B3mat = q35['B3mat']
fp3 = fingerprint(A3_actions, N3, B3mat, A3mat, G5)
print('Q3_REFERENCE', fp3)

all_qinf = []
for ni, (Ninf, nullity, tau_candidates) in enumerate(case_records):
    assert len(tau_candidates) == 3, (ni, nullity, len(tau_candidates))
    Ainf = delta_u(Wi, Ninf)
    for ti, tau in enumerate(tau_candidates):
        Binf = delta_tau(Wi, Wd, tau)
        assert r3(Ainf) == 10
        assert r3(Binf) == 45
        assert r3(np.column_stack([Binf, Ainf])) == 45
        fp = fingerprint(Ai, Ninf, Binf, Ainf, G5)
        rec = {'n': ni, 'tau': ti, **fp}
        all_qinf.append(rec)
        print('QINF_CASE', rec)

changed = []
for rec in all_qinf:
    keys = ('Hom_S10_to_M', 'Hom_S10_to_K', 'Hom_M_to_S10', 'Hom_K_to_S10')
    if any(rec[k] != fp3[k] for k in keys):
        changed.append(rec)

stable = len(changed) == 0
print('Q3_6_ALL_6_CASES_CHECKED =', len(all_qinf) == 6)
print('Q3_6_INTRINSIC_FINGERPRINTS_MATCH =', stable)
print('Q3_6_DIRECTIONAL_Q_SENSITIVE =', not stable)
print('RESULT =',
      'Q-SENSITIVE EXTENSION DIRECTION FOUND' if not stable
      else 'NO Q-SENSITIVE EXTENSION DIRECTION: PROCEED TO NEXT INVARIANT')
