# PAPER 3 — REFEREE GAP CLOSURE 2026-09-28

## Scope
Follow-up to `research/PAPER3_REFEREE_STYLE_ADVERSARIAL_AUDIT_2026-09-28.md`. The authorized target was the load-bearing free-product twisted-(H^1) step, followed by an exact dependency/scope audit.

## 1. Twisted free-product (H^1) step

The manuscript now defines
[
M_\rho=\mathbf Z/p^k\mathbf Z(\rho),\qquad M_{\rho_i}=M_\rho|_{G_i},
]
and states the natural restriction isomorphisms
[
H^1(G,M_\rho)\cong\bigoplus_i H^1(G_i,M_{\rho_i}),
qquad
H^1(G,\mathbf F_p)\cong\bigoplus_iH^1(G_i,\mathbf F_p),
]
together with the explicit commutative reduction diagram.

This removes the earlier ambiguity that the coefficient module depends on the candidate (ho).

## 2. Passage from (G) to (Q_k)

Put (n=p^{k-1}+1) and (N=P_n(G)). The manuscript now explicitly uses Paper 2's arbitrary-candidate factorization theorem for inflation
[
H^1(Q_k(G),M_\rho)\xrightarrow{\sim}H^1(G,M_\rho),
]
and the corresponding trivial-coefficient identification. For each free factor,
[
N\cap G_i=P_n(G_i),
]
with the two inclusions justified by functoriality and the canonical retraction (G	o G_i). Hence the same factorization applies factorwise.

Therefore the global finite reduction map is identified with the direct sum of the factor finite reduction maps. Surjectivity is equivalent to factorwise surjectivity, and Paper 1's rank-four (q=3) selector theorem applies.

### Classification
**PASS / CLOSED — load-bearing free-product twisted-(H^1) gap repaired.**

## 3. Truncation lemma

The previous categorical reflector proof was replaced by an explicit universal-property proof. The quotient
[
T_n(G_1*_pG_2)
cong T_n(T_n(G_1)*_pT_n(G_2))
]
is now justified by the same universal property against pro-(p) groups with (P_n=1).

### Classification
**PASS / CLOSED.**

## 4. Parameter-collapse wording

The selected depth (n=p^{k-1}+1) is now treated directly on abelianization:
[
D_n(D_{f,d}^{ab})=p^k\mathbf Z_p^{d-1}\oplus0.
]
Thus for (f<k) the torsion generator retains exact order (p^f) in the marked finite abelianization. The earlier overbroad statement for arbitrary (n) was removed.

### Classification
**PASS / CLOSED.**

## 5. Scope repair

The manuscript now consistently says the imported recognition class is rank-four (q=3), not “(q=p)”. The heterogeneous (f_i) family remains the broader application family for the affine-window part.

The mixed-commutator statement is explicitly limited to “no additional truncation beyond the global Zassenhaus quotient for the stated affine target”; it is not presented as an absolute intrinsic-depth theorem.

### Classification
**PASS / CLOSED.**

## 6. Remaining publication boundary

The mathematical application theorem is now internally coherent at the declared scope. The remaining issue is not the attacked proof gap but publication positioning: Paper 3 is an application/synthesis paper, while the finite-window recognition theorem and selector-minimality results belong to the separate theorem-paper track. Publication novelty remains **OPEN / CONDITIONAL**.

## 7. Build status

Commit `f97b9f04dd873fd2d0123d325443032c4840d086` triggered GitHub Actions workflow `Build Paper 3`, run `36361479679`. At the time of this record the run is queued; no build conclusion is claimed yet.
