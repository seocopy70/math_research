# PAPER 3 D2 — P4/P5 HAND CALCULATION — 2026-09-28

## Scope

Test the first corrected deeper-window case
\[
p=3,\quad d=4,\quad k=2,
\]
with
\[
Q_2=W_4=G/P_4,\qquad W_5=G/P_5.
\]

The correct extension direction is
\[
\boxed{1\to P_4/P_5\to W_5\to W_4\to1.}
\]

This corrects the shorthand arrow direction appearing in earlier planning text.

## 1. Fiber dimension

Primary-source MRT audit gives
\[
c_4=\dim_{\mathbf F_3}P_4/P_5
=\frac{4^4-5\cdot4^2+4}{4}=45.
\]

Classification: PASS / CLOSED for the dimension.

## 2. W5-action on the fiber

For the Zassenhaus filtration,
\[
[P_i,P_j]\subseteq P_{i+j}.
\]
In particular,
\[
[P_4,G]\subseteq P_5.
\]

Therefore conjugation by any element of G is trivial on
\[
P_4/P_5.
\]
Since W5=G/P5, the induced W5-action on P4/P5 is trivial.

Hence
\[
H^1(P_4/P_5,\mathbf F_3)^{W_5}
=
H^1(P_4/P_5,\mathbf F_3)
\]
and therefore
\[
\boxed{
\dim_{mathbf F_3}H^1(P_4/P_5,\mathbf F_3)^{W_5}=45.
}
\]

This is an exact hand result, not a dimension extrapolation.

Classification: PASS / CLOSED for the fixed-point calculation.

## 3. Five-term consequence

For
\[
1\to K\to W_5\to W_4\to1,
\qquad K=P_4/P_5,
\]
the five-term sequence is
\[
0\to H^1(W_4,\mathbf F_3)
\to H^1(W_5,\mathbf F_3)
\to H^1(K,\mathbf F_3)^{W_5}
\xrightarrow{\mathrm{tra}}
H^2(W_4,\mathbf F_3)
\xrightarrow{\inf}
H^2(W_5,\mathbf F_3).
\]

Because P4 is contained in the Frattini subgroup of G, and hence P4/P5 is contained in the Frattini subgroup of W5, the first inflation
\[
H^1(W_4,\mathbf F_3)\to H^1(W_5,\mathbf F_3)
\]
is an isomorphism. Consequently the transgression is injective.

Thus
\[
\boxed{
\dim\operatorname{im}(\mathrm{tra})=45
}
\]
and
\[
\boxed{
\dim\ker\bigl(H^2(W_4,\mathbf F_3)\to H^2(W_5,\mathbf F_3)\bigr)=45.
}
\]

This is the key m=1 result.

## 4. Position of the canonical delta class

The canonical mod-27 connecting class is the image of the nonzero full-group Demuškin obstruction under the finite-level comparison. Its image in
\[
H^2(G,\mathbf F_3)
\]
is nonzero by the Demuškin PD^2 structure.

Therefore the finite class representing the canonical delta obstruction cannot belong to the stable inflation kernel
\[
\ker\bigl(H^2(W_4)\to H^2(G)\bigr),
\]
and in particular it cannot be killed at every deeper finite level.

More specifically, if a finite class at W4 lies in the kernel of
\[
H^2(W_4)\to H^2(W_5),
\]
then it maps to zero in H^2(G) by functoriality. Hence the canonical delta class is not in the 45-dimensional one-step kernel.

This proves that the m=1 kernel does not contain the canonical branch.

## 5. What remains unresolved

The result does NOT prove that m=1 separates every false candidate.

A false candidate has a nonzero full-group variation class by the already-proved cochain variation formula once the candidate differs from the canonical lift:
\[
\delta_{\rho_3(1+9\nu)}(f)-\delta_{\rho_3}(f)
=\nu\smile\bar f.
\]
For \nu\ne0, Demuškin cup nondegeneracy gives some f with nonzero variation.

But the finite W4 representative of that nonzero class may, a priori, survive to W5 or only to a deeper quotient. The exact intersection
\[
\{\text{finite delta-family at }W_4\}
\cap
\ker(H^2(W_4)\to H^2(W_5))
\]
has not yet been computed.

Therefore:

- m=1 full selector: OPEN;
- exact delta/kernel intersection: OPEN / LOAD-BEARING;
- uniform m-bound: OPEN / LOAD-BEARING.

## 6. Important conceptual correction

The 45-dimensional kernel is NOT evidence that the canonical obstruction is lost.

It is precisely the expected inflation kernel created by the newly discarded central graded layer P4/P5. The canonical class is distinguished by its nonzero image in H^2(G,F3); only classes whose global obstruction is zero can eventually die.

Thus the deeper-window repair remains viable.

## Final classification

- MRT c4=45: PASS / CLOSED.
- W5 action on P4/P5 is trivial: PASS / CLOSED.
- fixed space dimension =45: PASS / CLOSED.
- transgression injective/rank 45: PASS / CLOSED.
- one-step inflation kernel dimension =45: PASS / CLOSED.
- canonical delta branch lies outside that kernel: PASS / LOCAL.
- m=1 separates all false candidates: OPEN / LOAD-BEARING.
- exact delta-family/kernel intersection: OPEN / LOAD-BEARING.
- uniform computable m-bound: OPEN / LOAD-BEARING.
