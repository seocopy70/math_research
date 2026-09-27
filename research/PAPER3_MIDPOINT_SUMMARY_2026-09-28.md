# PAPER 3 — MIDPOINT SUMMARY / 2026-09-28

## Purpose of this checkpoint

This note freezes the current Paper 3 state before the next intrinsic-carrier attack. It is a continuity checkpoint, not a new theorem.

## 1. Ultimate question

Paper 3 asks how much finite intrinsic filtered/relation data is necessary and sufficient to recover the canonical Demuškin orientation
\[
\chi_G:G\to\mathbf Z_p^\times,
\]
or its finite reduction \(\chi_G\bmod p^k\).

The current conceptual form is
\[
W_n(G)\longrightarrow O(G)\longrightarrow\chi_G\bmod p^k.
\]

## 2. What is now closed

### D1 — finite factorization
For the declared torsion-free Demuškin class (odd \(p\), even rank \(d\ge2\), \(q\in\{0,p,p^2,\ldots\}\), all \(k\ge2\)), arbitrary candidate affine crossed cocycles factor through
\[
Q_k=G/D_{p^{k-1}+1}.
\]
Status: **PASS / CLOSED**.

### D2 — corrected finite obstruction
The naive inflation-injectivity claim
\[
H^2(Q_k,\mathbf F_p)\hookrightarrow H^2(G,\mathbf F_p)
\]
is permanently **FAIL / CLOSED**.

The corrected finite central extension is
\[
1\to K_k\to E_k\to Q_k\to1,
\qquad
E_k=G/D_{p^{k-1}+2},
\quad
K_k=D_{p^{k-1}+1}/D_{p^{k-1}+2},
\]
with intrinsic carrier
\[
\mathcal O_k=
H^2(Q_k,\mathbf F_p)/\operatorname{im}(\operatorname{tra}_k).
\]

For every false first-order lift
\[
\rho_k=\chi_k(1+p^{k-1}\nu),\qquad \nu\ne0,
\]
D2 gives at least one witness whose obstruction has nonzero global inflation. This is existential per false candidate; it does not say every witness survives.

Status: **PASS / CLOSED**.

### D3 — finite selector
The finite Kummer predicate on \(Q_k\) uniquely selects
\[
\chi_G\bmod p^k
\]
at the declared Demuškin scope.

Status: **PASS / CLOSED**.

### D4 — affine depth
The affine crossed-cocycle depth
\[
n_{\rm aff}(k)=p^{k-1}+1
\]
is sharp in the declared affine category.

Status: **PASS / CLOSED**.

This is not yet an absolute minimality theorem for every possible intrinsic selector/carrier.

## 3. Important corrections frozen

- \(Q_4^*\not\cong H^1(G,\mathbf F_3)\); that was a type error.
- Bare finite \(H^2\)-inflation injectivity is not available.
- D2 uses the transgression quotient, not a stable global \(H^2\) window.
- The false-branch proof uses canonical lower-level Kummerian reduction-surjectivity, not arbitrary-candidate Kummer surjectivity.
- “Every obstruction output has nonzero global shadow” is false/overstated. The correct statement is: every false candidate has at least one detecting witness.
- Absolute minimality of \(\mathcal O_k\) is not a well-posed numerical question until a carrier category is fixed.

## 4. Current frontier

Global inflation gives
\[
\lambda_k:\mathcal O_k\to H^2(G,\mathbf F_p),
\]
and \(\dim H^2(G,\mathbf F_p)=1\). Hence a one-dimensional **global** recognition detector exists:
\[
\rho\ne\chi_k
\Longrightarrow
\exists f:\lambda_k(\delta_{k,\rho}(f))\ne0.
\]

But \(\lambda_k\) is not part of the finite pair
\[
E_k\to Q_k.
\]

Therefore the remaining load-bearing question is:

\[
\boxed{
\text{Does }E_k\to Q_k\text{ itself canonically determine an equivalent nonzero
functional on the D2 witness family?}
}
\]

The 45-dimensional \(Q_4^*\) calculation remains deferred.

## 5. Interpretation

Paper 3 has therefore moved past the basic existence/uniqueness question. The recognition theorem is closed. The remaining research is about **compression and intrinsic finite recoverability**:

\[
\text{large finite obstruction carrier}
\quad\rightsquigarrow\quad
\text{small canonical detector}.
\]

No claim is made yet that the finite pair can or cannot supply the one-dimensional detector.

## 6. Next attack authorized

Attack the finite-pair reconstruction problem abstractly first:

1. identify exactly what \(E_k\to Q_k\) canonically supplies (extension class, transgression, inflation image);
2. test whether any canonical functional on \(\mathcal O_k\) follows from that data alone;
3. use automorphism/naturality constraints to test uniqueness of such a functional;
4. determine whether the global detector necessarily requires stabilization/deeper quotients;
5. only if this remains undecidable abstractly, reopen the concrete rank-4 \(p=3\) module calculation.

## Status at checkpoint

**Recognition theorem: CLOSED.**

**Affine sharpness: CLOSED.**

**Finite-pair 1D intrinsic reconstruction: OPEN / LOAD-BEARING.**

**Carrier minimality: OPEN.**

**Publication novelty: OPEN / CONDITIONAL.**
