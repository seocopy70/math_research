# PAPER 3 — D3 FINITE SELECTOR PROMOTION AND D4 BOUNDARY — 2026-09-28

## Status

**D3 finite selector: PASS / CLOSED at the declared fixed rank-4, p=3, q=3 scope.**

**D4 LTE factorization sharpness: PASS / CLOSED in the already-proved affine crossed-cocycle category; it is not a proof of minimality for the intrinsic Kummer selector.**

The key consequence of the repaired D2 is that no further cohomological reconstruction is required for the induction proving finite-level uniqueness.

## 1. D3 induction

Let
\[
Q_k=G/P_{p^{k-1}+1}(G)
\]
and let \(\mathsf K_k(Q_k,\rho_k)\) denote the finite Kummer lifting predicate.

Assume:
1. arbitrary-candidate factorization through \(Q_k\);
2. canonical orientation \(\chi_G\) is Kummerian;
3. level-2 uniqueness \(\rho_2=\chi_G\bmod p^2\);
4. the repaired D2 separating-output theorem for every nonzero
\[
\nu\in H^1(G,\mathbf F_p)
\]
around the canonical lower-level lift.

Suppose \(\mathsf K_k(Q_k,\rho_k)\) holds.

By factorization it holds on \(G\), and by the reduction/descent lemma the reduction \(\rho_{k-1}\) satisfies \(\mathsf K_{k-1}\). Induction gives
\[
\rho_{k-1}=\chi_G\pmod{p^{k-1}}.
\]

Therefore any lift \(\rho_k\) differs from the canonical lift by
\[
\rho_k=\chi_k(1+p^{k-1}\nu),
\qquad
\nu\in H^1(G,\mathbf F_p).
\]

If \(\nu\neq0\), repaired D2 supplies a finite witness \(f\) whose connecting output has nonzero class in the transgression quotient
\[
\mathcal O_k=
H^2(Q_k,\mathbf F_p)/\operatorname{im}(\operatorname{tra}_k).
\]
That contradicts \(\mathsf K_k\), which is exactly vanishing/surjectivity of the finite connecting map.

Hence \(\nu=0\), so
\[
\rho_k=\chi_G\pmod{p^k}.
\]

Conversely, the canonical orientation satisfies \(\mathsf K_k\) by classical Demuškin Kummerianity and finite factorization.

Thus
\[
\boxed{
\mathsf K_k(Q_k,\rho)=0
\iff
\rho=\chi_G\pmod{p^k}
}
\]
for the fixed project scope.

This is the unconditional finite-selector theorem once the previously audited inputs are taken as established.

## 2. Important correction to the dependency statement

The false-lift separation argument does **not** require arbitrary-candidate reduction-surjectivity
\[
H^1(G,A_k(\rho_k))\to H^1(G,\mathbf F_p).
\]

That would be circular: surjectivity is essentially the Kummer predicate itself.

What is required in the variation step is surjectivity for the **canonical lower-level coefficient module**
\[
H^1(G,A_{k-1}(\chi_{k-1}))
\to H^1(G,\mathbf F_p),
\]
which follows from classical Kummerianity of \(\chi_G\).

This distinction is now load-bearing and must remain explicit.

## 3. D4 boundary

The affine crossed-cocycle factorization depth
\[
n_{\mathrm{aff}}(k)=p^{k-1}+1
\]
is already proved sharp in its declared category for odd \(p\), including the rank-two boundary. The lower bound uses explicit crossed-cocycle witnesses and LTE.

Therefore D4 is **PASS / CLOSED for the affine representation category**.

But this does **not** prove:
- that \(P_{p^{k-1}+1}\) is the smallest quotient window for the intrinsic Kummer selector;
- that no other, smaller carrier than \(Q_k\) can recognize the orientation;
- that \(\mathcal O_k\) is absolutely minimal.

Those remain separate information-sufficiency questions.

## 4. q-direction status

The selector theorem in this project remains fixed at the rank-4, \(p=3\), \(q=3\) Demuškin group. The selector definition is q-blind because q is not supplied as input.

The q-parameter enters the presentation-dependent identification of the canonical orientation and the separate LTE/sharpness analysis. No uniform-in-q selector theorem is claimed here.

Thus:
- q-blind selector input: **CLOSED at fixed project scope**;
- uniform q-family theorem: **OPEN / NOT CLAIMED**;
- q-recovery from the finite quotient: **separate problem**.

## 5. Final frontier after D3 promotion

The load-bearing recognition theorem is now closed:

\[
\boxed{
Q_k
\;\xrightarrow{\;\mathsf K_k\;}
\chi_G\pmod{p^k}
}
\]

with the proof route
\[
\text{finite factorization}
+
\text{level-2 base}
+
\text{D2 transgression-quotient separation}
+
\text{induction}.
\]

The remaining research problems are no longer needed to prove recognition:

1. **absolute carrier minimality of \(\mathcal O_k\)** — OPEN, but first requires fixing a carrier category;
2. **minimal selector window** below \(P_{p^{k-1}+1}\) — OPEN;
3. **uniform-in-q recognition** — OPEN / NOT CLAIMED;
4. **publication novelty audit** — OPEN / CONDITIONAL.

## Final classification

- D2 repaired finite separation: **PASS / CLOSED**.
- D3 finite selector uniqueness: **PASS / CLOSED** at fixed rank-4, p=3, q=3.
- D4 affine LTE sharpness: **PASS / CLOSED** in its declared category.
- Intrinsic selector-window minimality: **OPEN**.
- Absolute carrier minimality: **OPEN**.
- Uniform q-family theorem: **OPEN / NOT CLAIMED**.
- Publication novelty: **OPEN / CONDITIONAL**.
