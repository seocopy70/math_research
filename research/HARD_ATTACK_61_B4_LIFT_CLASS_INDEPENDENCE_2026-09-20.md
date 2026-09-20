# HA61-B4 — A_2-LIFT CLASS INDEPENDENCE AUDIT — 2026-09-20

## Verdict

**HA61-B4: PASS / LOCAL.**

The apparent remaining lift-class ambiguity was attacked by the exact coefficient-extension diagram, then checked by direct crossed-word evaluation on the frozen q=3 and q=9 branches.

The result is stronger than a representative-gauge argument but remains local to the audited standard family.

## 1. Exact lift-class difference

Let
\[
0\to\mathbf F_3\xrightarrow{i}A_2\to\mathbf F_3\to0,
\qquad i(c)=3c,
\]
and
\[
0\to\mathbf F_3\to A_3\to A_2\to0.
\]

If two A_2-valued cocycles \(z,z'\) have the same mod-3 reduction \(f\), then
\[
z'-z=3c=i(c)
\]
for an \(\mathbf F_3\)-valued 1-cocycle \(c\), after passing to cohomology/representatives.

The pullback of the A_3-extension along \(i:\mathbf F_3\to A_2\) is canonically the A_2-extension
\[
0\to\mathbf F_3\to A_2\to\mathbf F_3\to0.
\]
Therefore naturality of connecting maps gives
\[
\boxed{
\delta_3(z')-\delta_3(z)=\delta_2(c).
}
\]

This is the precise lift-class analogue of B3.

Hence lift-class independence is NOT automatic. It holds exactly when the first-stage connecting map annihilates the difference class.

## 2. Frozen q=9 branch

Here
\[
r_9=x_1^9[x_1,x_2][x_3,x_4],
\qquad \rho_2=1.
\]

For an arbitrary A_2-valued crossed cocycle, the exact relation evaluation is
\[
z(r_9)=9z_1\pmod9=0
\]
at the primary stage. Equivalently the mod-9 connecting map is
\[
\delta_2(c)=0
\]
for every \(c\in H^1(G,\mathbf F_3)\).

Thus
\[
\delta_3(z+3c)=\delta_3(z).
\]

The direct mod-27 formula
\[
z(r_9)=9(1-a)z_1\pmod{27}
\]
gives the same result: replacing \(z_1\) by \(z_1+3c_1\) changes the relation value by
\[
27(1-a)c_1=0\pmod{27}.
\]

So all A_2 lift classes over the same primary class give the same secondary obstruction in this branch.

## 3. Frozen q=3 branch

Here
\[
r_3=x_1^3[x_1,x_2][x_3,x_4],
\qquad \rho_2(x_2)=4.
\]

The exact primary crossed-word coefficient of \(z_1\) is
\[
2+4^{-1}=2+7=9\equiv0\pmod9,
\]
and the other generator coefficients vanish. Hence
\[
\boxed{\delta_2\equiv0}
\]
as a map \(H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3)\) on this frozen branch.

Therefore again
\[
\delta_3(z+3c)=\delta_3(z)
\]
for every lift-class difference \(c\).

The mod-27 crossed-word calculation independently agrees: with
\[
\rho_3(x_2)=13+9a,
\]
the relation coefficient is
\[
2+(13+9a)^{-1}\pmod{27},
\]
which is always divisible by 9; multiplying the lift shift \(3c_1\) therefore gives zero modulo 27.

## 4. What this actually proves

The dangerous statement

> “all A_2 lifts are equivalent because gauge invariance”

is false in general.

The correct statement is:

\[
\boxed{
\text{lift-class dependence is measured exactly by }\delta_2.
}
\]

For the two audited standard branches, \(\delta_2=0\) identically, so the secondary obstruction is genuinely independent of the A_2 lift class.

This removes the remaining lift-class ambiguity from the frozen q=3/q=9 calculations.

## 5. Consequence for t_2

On these branches, once the representative gauge and lift-class ambiguity are both removed, the non-\mu part of \(\delta_3\) is a function of the mod-3 class \(f\) alone.

The audited formulas therefore support
\[
\delta_3(z)
=
[f(t_2)+(\mu\wedge f)(R)]\omega
\]
without an additional A_2-lift parameter.

However, this does NOT yet prove that the resulting functional is represented by a presentation-free filtered residual \(t_2\). That is the next intrinsicity gate.

## 6. Remaining boundary

The general theorem still requires proving, for arbitrary admissible filtered Demuškin input, that
\[
\delta_2\equiv0
\]
(or an equivalent canonical mechanism killing the lift-class difference) at the relevant stage.

If \(\delta_2\) is not zero for some admissible input, then the secondary obstruction is naturally defined on a lift torsor rather than on \(f\) alone, and the simple intrinsic t_2 formula must be modified.

Therefore B4 is local, not universal.

## Decision

\[
\boxed{\text{HA61-B4 = PASS / LOCAL}}
\]

\[
\boxed{\text{HA61-B5 = OPEN / LOAD-BEARING}}
\]

\[
\boxed{\text{HA61-C remains unopened.}}
\]

No all-n induction is authorized.
