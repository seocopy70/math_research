# HA61-B5-1 — CORRECTION: THE SECONDARY WINDOW IS NOT D_4/D_5 — 2026-09-20

## Status

**HA61-B5-1: PASS / LOCAL for the filtration-source correction; HA61-B remains OPEN / LOAD-BEARING.**

The previously proposed test
\[
D_4/D_5\to (1/9)z(\cdot)\bmod3
\]
is **not well-defined**. The explicit counterexample used in B5 already proves this: \(g^9\in D_9\subset D_5\) but
\[
z(g^9)/9\equiv f(g)\pmod3.
\]
Thus the secondary functional does not factor through \(D_4/D_5\).

The correct finite-information window is the lower-3-central threshold \(P_4\), i.e. the layer retained in \(G/P_4\), equivalently the relevant Zassenhaus information through the \(D_{10}\) window established earlier for the standard family.

## 1. Source audit

At the mod-27 stage, the new secondary normalization is division by 9. Several elements lying in deep Zassenhaus layers can still survive:

- \(g^9\in D_9\), with \(z(g^9)/9=f(g)\);
- \(\gamma_2(F)^3\subset D_6\) can contribute through the already-present first-digit action;
- deeper elements such as \(g^{27}\in D_{27}\) have zero divided contribution modulo 3.

Therefore Zassenhaus membership alone does not identify the correct quotient. The lower-3-central filtration separates the successive coefficient-lifting layers more faithfully for this purpose.

## 2. Correct lower-3-central bookkeeping

Use
\[
P_1=G,\qquad P_{n+1}=P_n^3[P_n,G].
\]

Then the mod-27 finite quotient is controlled by the threshold \(G/P_4\); the new residual lives in the \(P_3/P_4\) layer.

For the standard family:
- the mod-9 stage uses the preceding \(P_2/P_3\)-level information;
- the new \(q=9\) residual \(x_1^9\) lies in \(P_3\) and is retained modulo \(P_4\);
- this is the same threshold previously recorded as the \(P_4\)/\(D_{10}\) mod-27 information boundary.

Thus the phrase “P_4 residual” means the information retained by the quotient \(G/P_4\), not an assertion that the residual element itself lies in \(P_4\).

## 3. Explicit source calculation

For a principal first-digit action
\[
\rho_2(g)=1+3\lambda(g)\pmod9,
\]
and an \(A_3\)-lift with
\[
\rho_3=\rho_2(1+9\mu),
\]
the following valuation rules hold modulo 27.

### (a) Ninth powers

For \(u=1+3a\),
\[
1+u+\cdots+u^8\equiv9\pmod{27}.
\]
Hence
\[
z(g^9)/9=f(g)\pmod3.
\]
This is the genuine new linear power functional.

### (b) Cubes of commutators

For \(c=[g,h]\), the first-stage calculation gives
\[
z(c)=3(\lambda(g)f(h)-\lambda(h)f(g))\pmod9.
\]
Since \(\rho(c)=1\),
\[
z(c^3)=3z(c),
\]
so
\[
\frac{z(c^3)}9
=
\lambda(g)f(h)-\lambda(h)f(g)
\pmod3.
\]
Therefore \(\gamma_2^3\) can survive at the secondary normalization, but its contribution is **not a new carrier**: it is exactly the old first-digit \(\lambda\wedge f\) term applied to the already-established quadratic relation component \(R\).

This is the key source-separation fact.

### (c) Triple commutators

For \(c=[h,k]\) and \(d=[g,c]\), the commutator formula gives, modulo 27,
\[
\frac{z([g,[h,k]])}{9}
=
-\lambda(g)
\bigl(\lambda(h)f(k)-\lambda(k)f(h)\bigr)
\pmod3
\]
up to the fixed commutator-sign convention.

Thus a degree-three Lie component can appear at the secondary level when \(\lambda\ne0\). It is not legitimate to declare all degree-three bracket terms zero.

However, this term is an old-action / relation-gauge sector rather than the new power residual: it depends on \(\lambda\) and the degree-three bracket component, not on a new independent p-power scalar. To remove it intrinsically one still needs the presentation/relator-gauge quotient that identifies degree-three bracket changes of the form \([v,R]\).

## 4. New power sector

After quotienting the already-established first-stage action sector, the genuinely new source is the ninth-power vector
\[
t_2\in V^{(2)}
\]
represented by the \(P_3/P_4\) power/relation residual. Its evaluation is
\[
f\longmapsto f(t_2).
\]

For the frozen standard family:
- \(q=3\): the next residual is zero after the first-stage datum has been absorbed;
- \(q=9\): \(t_2=X_1^{(2)}\) in the corresponding second restricted-power notation;
- \(27\mid q\): \(t_2=0\).

The coefficient 1 in the \(q=9\) case is forced by the ninth-power sum above, not imported from the known orientation formula.

## 5. Deeper terms

For a ninth-power tower,
\[
z(g^{27})/9\equiv0\pmod3
\]
because the geometric sum has 3-adic valuation 3.

For commutator-derived terms one gains at least one additional factor of 3 per commutator layer. In particular, once the old \(\gamma_2^3\) sector has been quotiented into the already-established \(\lambda\wedge f\) term, the deeper P_4 commutator/power terms are zero under the secondary /9 normalization or factor through the same lower-layer data.

This establishes the valuation boundary for the standard two-stage calculation, but not yet a presentation-free theorem for every admissible one-relator input.

## 6. Corrected A/B criterion

The correct “one functional versus several” test is therefore not dimension counting on \(D_4/D_5\).

Instead, define the secondary source quotient by:
1. take the actual \(P_3/P_4\) relation/power residual;
2. quotient the subspace generated by the already-established \(R\)-action and lift-gauge sectors;
3. evaluate by the /9 secondary functional.

Then:
- **A:** the quotient image is exactly \(f\mapsto f(t_2)\), so one new power functional remains;
- **B:** an additional independent functional remains after the old-action/gauge quotient.

For the frozen standard family, direct coefficient-extension evaluation gives A.

## 7. Logical boundary

What is now established:
- \(D_4/D_5\) is the wrong secondary quotient;
- the mod-27 finite-information threshold is the lower-3-central \(P_4\) quotient / corresponding \(D_{10}\) window;
- ninth powers give the new linear functional;
- \(\gamma_2^3\) is old-action data, not a new independent functional;
- deeper ninth-power terms vanish at the /9 normalization;
- the standard family realizes the one-new-functional branch.

What remains open:
- a presentation-free proof that every degree-three bracket contribution is absorbed by the intrinsic relator-gauge quotient;
- a universal definition of the secondary source quotient for arbitrary minimal one-relator Demuškin input;
- a proof that no additional independent functional survives there.

## 8. Decision

- **D_4/D_5 secondary factorization:** FAIL / CLOSED.
- **Correct P_4/D_10 finite-information window:** PASS / LOCAL.
- **Standard-family one-new-functional outcome:** PASS / LOCAL.
- **Universal absorption of degree-three bracket/gauge terms:** OPEN / LOAD-BEARING.
- **Universal B5 closure:** OPEN / LOAD-BEARING.
- **HA61-C:** not opened.

Next authorized attack: prove the degree-three bracket term is exactly the relator-gauge image \([v,R]\) under the intrinsic secondary obstruction, and then test whether the residual quotient is canonically one-dimensional in the new power direction.
