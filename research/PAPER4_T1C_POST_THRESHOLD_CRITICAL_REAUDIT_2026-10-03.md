# PAPER 4 — T1-C POST-THRESHOLD CRITICAL RE-AUDIT — 2026-10-03

## Purpose

The 2026-10-03 integral Fox calculation has advanced the declared rank-two stress family from an OPEN threshold question to a relative-window threshold theorem. This audit records the critical review needed before using that result downstream.

## 1. What is now actually closed

For
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a\ge1,
\]
with the declared relative input
\[
W_n(G_{s,a})\longrightarrow D/D_n(D),
\]
the rank-two stress factor gives an integral Fox-divisibility obstruction.

Writing \(q=p^a\), \(I\) for the augmentation ideal, and \(Y=x_2-1\), the pure-Y component of the relevant Fox row is
\[
q-Y.
\]
Cancelling the scalar defect \(p^s\bar z\) would therefore require
\[
(q-Y)A(Y)=p^s.
\]
With \(r=\lfloor s/a\rfloor\),
\[
\frac{p^s}{q-Y}
=p^{s-a}\sum_{j\ge0}p^{-aj}Y^j,
\]
and the first nonintegral coefficient occurs at \(j=r\). Thus the first unavoidable integral divisibility residual occurs in the \(Y^r\bar z\) direction.

This is not a mod-p restricted-power artifact.

## 2. Independent finite-kernel survival control

The metabelian quotient
\[
H=C_{p^s}\rtimes C_{p^s},
\qquad yzy^{-1}=z^{1+p},
\]
is a quotient of the rank-two stress group obtained by setting the other Demuškin generators to 1.

For \(r=\lfloor s/a\rfloor<s\),
\[
(y-1)^r z=p^r z\ne0
\]
in \(C_{p^s}\), while
\[
D_{p^s+1}(H)=1.
\]
Hence the corresponding residual remains visible in the actual finite critical quotient.

### Naturality lemma required for the clean proof

Let
\[
1\to K\to E\xrightarrow{\pi}Q\to1
\]
be an extension and let \(f:K\to A\) be a \(Q\)-equivariant homomorphism into an abelian \(Q\)-module. The pushout extension class is represented by the image under \(f\) of any section-defect cocycle. Therefore section/lift changes map to section/lift changes, and the induced map on obstruction quotients is functorial.

Consequently, if the residual maps to a nonzero class in the metabelian quotient, the original abelianized-kernel pushout class is nonzero. This supplies the precise logical bridge that the earlier calculation only described informally as “metabelian survival”.

This lemma does not enlarge the theorem scope; it closes a proof-packaging gap.

## 3. Upper and lower sides of the threshold

For every \(n\le p^s\), the defining relation satisfies
\[
z^{p^s}\in D_{p^s}(G_{s,a})\subseteq D_n(G_{s,a}),
\]
so the generator lifts define a section
\[
D/D_n(D)\to G_{s,a}/D_n(G_{s,a}).
\]
Thus the relative extension splits for all \(n\le p^s\).

At \(n=p^s+1\), the integral Fox obstruction plus finite-kernel survival gives nonsplitting.

Therefore
\[
\boxed{n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1}
\]
for the declared rank-two stress family.

The higher-rank statement is inherited only through the explicit quotient map setting the extra Demuškin generators to 1; this inheritance should be stated as a quotient/naturality argument, not as an unqualified slogan.

## 4. Scope boundary

The theorem is **not** a theorem for arbitrary free-by-Demushkin extensions.

It does not yet establish:

- an unmarked finite-window invariant of the abstract filtered group;
- a presentation-independent/coarsest realization;
- strict compression;
- non-reencoding;
- a universal theorem for all \(q>0\) free-by-Demushkin extensions;
- orientation recovery.

The Gate-T result is an extension-depth separation theorem in a declared relative category.

## 5. Critical status

- integral Fox-divisibility obstruction, declared stress family: **PASS / CLOSED** as a theorem ingredient;
- finite-kernel survival: **PASS / CLOSED** after the explicit pushout/naturality lemma is stated;
- splitting for all \(n\le p^s\): **PASS / CLOSED**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **PASS / CLOSED** for the declared stress family;
- arbitrary free-by-Demushkin extension theorem: **OPEN**;
- unmarked filtered-group realization: **OPEN**;
- intrinsic/coarsest compression: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

## 6. Next authorized boundary

The threshold itself is frozen. Do not recompute \(p^s+1\), degree-5 Fox paths, the scalar norm shortcut, or the same stress-family separation.

The next mathematical question is now:

> Can the relative threshold obstruction be factored through a genuinely intrinsic finite-window object after forgetting the chosen map to \(D/D_n(D)\), and if so what is the coarsest defensible realization?

This requires a fresh Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop pre-check before any new construction.

No carrier is to be invented merely to encode the already-known threshold.
