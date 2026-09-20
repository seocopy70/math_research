# HA61-B2 — PRIMARY-ZERO REDUCTION AUDIT — 2026-09-20

## Status

**HA61-B2: PASS / LOCAL only. HA61-B remains OPEN / LOAD-BEARING.**

This attack executes the primary-zero reduction on the two frozen standard branches for which HA61-A has an exact crossed-word expansion. It does **not** establish the general B2 theorem for arbitrary filtered relation jets.

## 1. q=3 frozen branch

For
\[
r_3=x_1^3[x_1,x_2][x_3,x_4],\qquad
\rho_3(x_2)=t=13+9a\pmod{27},
\]
the exact crossed-word evaluation is
\[
z(r_3)=(2+t^{-1})z_1=-9a z_1\pmod{27}.
\]

At the primary level,
\[
t\equiv4\pmod9,\qquad 2+t^{-1}\equiv 2+4^{-1}=2+7=0\pmod9.
\]
Thus the primary obstruction is zero before the secondary division.

After division by 9,
\[
\frac{z(r_3)}9\equiv-a z_1\pmod3,
\]
and since \(z_1\equiv f_1\pmod3\),
\[
\boxed{\delta_3(f)=-a f_1.}
\]

### Lift test inside this frozen branch

Replace the chosen A_2-lift of the cocycle value by a lift with the same reduction:
\[
z_1\mapsto z_1+3c.
\]
Then
\[
-9a(z_1+3c)/9\equiv-a z_1\pmod3.
\]
So the secondary class is independent of this representative change.

This is a genuine local G2-type check for the tested word: the surviving coefficient depends only on \(f_1\), not on the A_2 lift integer.

## 2. q=9 frozen branch

For
\[
r_9=x_1^9[x_1,x_2][x_3,x_4],\qquad
\rho_3(x_2)=1+9a,
\]
one has
\[
z(r_9)=9(1-a)z_1\pmod{27}.
\]
Hence
\[
\delta_3(f)=(1-a)f_1.
\]

Again the coefficient is already divisible by 9 before secondary division, and changing \(z_1\) by \(3c\) changes the divided expression by
\[
(1-a)3c\equiv0\pmod3.
\]

Thus the same local lift-independence holds.

## 3. What B2 actually establishes

The two audited branches establish:

1. primary-zero is not merely a numerical afterthought; the exact relation coefficient is already in \(9\mathbf Z/27\);
2. after division by 9 and reduction mod 3, the result depends only on the mod-3 reduction \(f\);
3. the q=3 old action does not leave an additional constant after the full relation evaluation;
4. q=3 and q=9 have the same slope in the new extension parameter.

This supports the interpretation that no independent \(B_{\rho_2}\) is visible in these two frozen branches.

## 4. What remains unproved

This does **not** prove the general primary-zero reduction.

The missing statement is:

> For an arbitrary admissible filtered relation jet and arbitrary A_2-valued crossed cocycle \(z\) with \(\delta_2(f)=0\), every \(\rho_2\)-dependent secondary term is either zero, a gauge/coboundary variation, already-fixed first-stage normalization, or canonically absorbed into the next residual \(t_2\).

The present exact computations do not control:
- general degree-\(\ge4\) relation terms;
- arbitrary A_2 lift components beyond the tested normal form;
- general relator gauge;
- filtration valuation of all omitted terms.

Therefore the \(E_{\ge4}\) sector is still OPEN.

## Decision

\[
\boxed{\text{HA61-B2 = PASS / LOCAL}}
\]

but

\[
\boxed{\text{HA61-B = OPEN / LOAD-BEARING}.}
\]

Next authorized attack: **HA61-B3**, the general A_2-lift gauge test. The target is not another q=3/q=9 numerical check; it is the formula for the change of the full secondary obstruction under
\[
z\mapsto z+d\phi
\]
and whether the putative \(B_{\rho_2}\) changes by zero/coboundary/transported first-stage normalization. No HA61-C yet.
