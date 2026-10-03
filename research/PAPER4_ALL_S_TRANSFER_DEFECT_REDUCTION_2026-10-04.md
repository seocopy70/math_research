# Paper 4 — all-s transfer-defect reduction (2026-10-04)

## Target

For the remaining boundary
\[
W_{p^s+1}(G_{s,s}) \stackrel{?}{\cong} W_{p^s+1}(G_{s,\infty}),\qquad s\ge2,
\]
prove the intrinsic transfer defect is nonzero on the \(a=s\) side and zero on the \(a=\infty\) side.

## Pre-check

- **Object:** \(W=W_{p^s+1}\), its intrinsic cup-radical line, \(K=\ker\chi\), and the canonical transfer \(V:W^{ab}\to K^{ab}\).
- **Input:** only the unmarked finite group \(W\); no chosen \(z\), marked quotient, or external orientation.
- **Functoriality:** the radical line determines \(K\); \(T=W^{ab}[p^s]\) is characteristic; transfer is natural.
- **Gauge:** the generator of \(T\) is only defined up to a unit, harmless for the zero/nonzero predicate.
- **Orientation bridge:** none is inserted; the candidate is a finite-group invariant.
- **q-blindness:** the definition uses only \(W\), its cup product, \(W^{ab}\), and transfer.
- **Separation:** the \(a=s\) side is reduced to a single critical norm/Jacobson class; the \(a=\infty\) side vanishes after the same normalization.
- **Novelty:** this is not the closed scalar/coinvariant route; it uses the cyclic action on \(K^{ab}\).
- **Stop condition:** the only remaining load-bearing issue is the effect of the finite-window truncation relations on the integral Schreier class.

## New reduction

Let \(A_i\) denote the conjugate Schreier generators for \(x_1\), \(U=z^p\), and \(\sigma(A_i)=A_{i+1}\). The relation coming from
\[
z^{p^s}=x_1^{p^s}[x_1,x_2]\cdots
\]
gives in the abelianized index-\(p\) kernel
\[
p^{s-1}U-p^sA_i=0\qquad(0\le i<p).
\]
Ignoring the truncation relations for the moment, put
\[
L_s=\mathbb Z U\oplus\bigoplus_{i=0}^{p-1}\mathbb Z A_i\,
/\langle p^{s-1}U-p^sA_i\rangle.
\]
Then
\[
\delta^{p-1}A_0=(\sigma-1)^{p-1}A_0
=\sum_{j=0}^{p-1}(-1)^{p-1-j}\binom{p-1}{j}A_j.
\]
The class has exponent exactly \(p^s\) in \(L_s\): after quotienting by \(U=0\), the relations become \(p^sA_i=0\), so the image is the nonzero vector
\[
\bigl((-1)^{p-1-j}\binom{p-1}{j}\bigr)_{j=0}^{p-1}
\in (\mathbb Z/p^s)^p,
\]
whose first and last coefficients are units. Hence
\[
\operatorname{ord}_{L_s}(\delta^{p-1}A_0)=p^s,
\qquad
p^{s-1}\delta^{p-1}A_0\ne0.
\]
Therefore the desired transfer defect follows once the actual truncation relations do not alter this class modulo the order-\(p\) witness.

## Exact remaining lemma

It is enough to prove the following integral filtration statement for the index-\(p\) kernel \(K\):
\[
\operatorname{im}\bigl(D_{p^s+1}(F)\cap K\to K^{ab}\bigr)
\subseteq p^s K^{ab}.
\tag{TF_s}
\]
Indeed, the standard index-\(p\) Zassenhaus comparison reduces the source to
\[
D_{p^s+1}(F)\cap K\subseteq D_{p^{s-1}+1}(K),
\]
and every element of \(D_{p^{s-1}+1}(K)\) maps into \(p^sK^{ab}\) by the defining Zassenhaus product description: all commutator factors vanish in \(K^{ab}\), while the first possible pure-power exponent at filtration index \(p^{s-1}+1\) is \(p^s\).

Thus (TF_s), once written as a self-contained lemma with its subgroup-comparison input explicitly cited/proved, prevents the truncation relations from killing the order-\(p\) class
\[
p^{s-1}\delta^{p-1}A_0.
\]

## Consequence if (TF_s) is certified

The intrinsic transfer predicate
\[
\varepsilon(W):\quad p^{s-1}V(T)\ne0\in K^{ab}
\]
is true for \(a=s\) and false for \(a=\infty\). Hence
\[
W_{p^s+1}(G_{s,s})\not\cong W_{p^s+1}(G_{s,\infty})
\]
for every odd \(p\) and \(s\ge2\) in the declared stress-family scope.

Combined with lower-window blindness, this closes the exact unmarked threshold at \(p^s+1\) for the full stress-family parameter range \(1\le a\le s\) (with \(a=s\) handled by this boundary lemma).

## Classification

- model Schreier lattice order computation: **PASS / LOCAL**;
- reduction of the general boundary to (TF_s): **PASS / LOCAL**;
- (TF_s) itself: **OPEN / LOAD-BEARING**;
- all-s transfer-defect separation: **OPEN / LOAD-BEARING**;
- Paper 4 final freeze: blocked only by certification of (TF_s), plus independent verification and record synchronization.
