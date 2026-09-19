# HARD ATTACK 10 — DEGREE-3 FOX TRUNCATION FAILS UNDER A NIELSEN CHANGE — 2026-09-20

## Verdict

The fixed-normal-form exact Fox row has local degree at most 3, but this degree bound is **not presentation-invariant**.

A concrete Nielsen change produces an equivalent minimal presentation whose exact universal Fox row contains higher local degrees, and the degree-3 truncation of that transformed row does **not** vanish at the transported canonical character.

This closes the tempting claim that the exact Fox orientation locus can be represented by a presentation-independent degree-3 truncation of the Fox row.

## 1. Nielsen change

Start from
\[
r=x_1^3[x_1,x_2][x_3,x_4].
\]

Make the free change
\[
x_1=y_1y_2,\qquad x_2=y_2,\qquad x_3=y_3,\qquad x_4=y_4.
\]

For the original universal Fox row
\[
J_1=1+A+A^2B^{-1},\quad
J_2=A^2(A-1)B^{-1},
\]
\[
J_3=A^3(1-D)(CD)^{-1},\quad
J_4=A^3(C-1)(CD)^{-1},
\]
the coefficient substitution is
\[
A=Y_1Y_2,\qquad B=Y_2,qquad C=Y_3,qquad D=Y_4,
\]
and the Fox chain rule gives the transformed row
\[
J'_1=Y_1^2Y_2+Y_1Y_2+1,
\]
\[
J'_2=Y_1\bigl(Y_1^2Y_2^2+Y_1^2Y_2+1\bigr),
\]
\[
J'_3=-\frac{Y_1^3Y_2^3(Y_4-1)}{Y_3Y_4},
\qquad
J'_4=\frac{Y_1^3Y_2^3(Y_3-1)}{Y_3Y_4}.
\]

The second row already has total polynomial degree 5, and the last two rows have infinite local expansions around \(Y_i=1\) because of the denominators.

## 2. Transported canonical point

The original canonical character is
\[
(A,B,C,D)=\left(1,-\frac12,1,1\right).
\]

Under
\[
A=Y_1Y_2,\qquad B=Y_2,
\]
the transported point is
\[
Y_2=-\frac12,
\qquad
Y_1=-2,
\qquad
Y_3=Y_4=1.
\]

All four values still lie in \(1+3\mathbf Z_3\):
\[
-2=1-3,\qquad -\frac12=1-\frac32.
\]

The **full** transformed Fox row vanishes there, as it must.

## 3. Degree-3 local truncation

Put
\[
Y_i=1+v_i
\]
and truncate each transformed row to total degree \(\le3\) in the \(v_i\).

The first two truncated rows are
\[
\widetilde J'_1
=
v_1^2v_2+v_1^2+3v_1v_2+3v_1+2v_2+3,
\]
and
\[
\widetilde J'_2
=
2v_1^3+9v_1^2v_2+6v_1^2
+3v_1v_2^2+9v_1v_2
+7v_1+v_2^2+3v_2+3.
\]

At the transported canonical point
\[
(v_1,v_2,v_3,v_4)=\left(-3,-\frac32,0,0\right),
\]
one obtains
\[
\widetilde J'_1=0,
\qquad
\boxed{\widetilde J'_2=-\frac{243}{2}\ne0}.
\]

By contrast, the exact row satisfies
\[
J'_1=J'_2=J'_3=J'_4=0.
\]

Thus the degree-3 truncation has lost a genuinely necessary higher-order contribution.

## 4. What this proves

This is stronger than the statement “a coordinate change may increase polynomial degree.”

It gives a concrete failure:
\[
\boxed{
\text{exact Fox row zero}
\not\Rightarrow
\text{degree-3 truncated Fox row zero}
}
\]
after an allowed Nielsen-equivalent presentation change.

Therefore:

- the fixed-normal-form degree-3 Fox compression is **PASS / CLOSED locally**;
- a presentation-independent degree-3 truncation of the exact Fox row is **FAIL / CLOSED**;
- the full universal Fox scheme remains the exact comparison object;
- any intrinsic exact degree-3 filtered carrier, if it exists, cannot be defined merely as “the degree-3 part of the Fox row.”

## 5. Relation to the filtered program

The result does **not** prove that every conceivable exact degree-(2,3) relation invariant is impossible.

It proves a narrower but load-bearing negative statement:

> Higher Fox coefficients are not an artifact that can be discarded after an arbitrary change of free coordinates. They can feed back into the exact orientation equation even when the original normal form happens to have a degree-3 Fox presentation.

Hence any successful intrinsic compression must have an additional mechanism that removes this dependence—e.g. a canonical filtered coordinate/gauge quotient, an intrinsic cohomological obstruction family, or a new theorem showing why the higher terms are reconstructible from the proposed lower jet.

The existing mod-9 carrier succeeds because only the first digit is being recovered; the higher exact digits are precisely where this obstruction becomes active.

## 6. Status

- Nielsen covariance of the **full** Fox scheme: **PASS / CLOSED**.
- Fixed-normal-form exact degree-3 Fox compression: **PASS / CLOSED**.
- Presentation-independent exact degree-3 Fox truncation: **FAIL / CLOSED**.
- Intrinsic exact filtered degree-(2,3) carrier by another construction: **OPEN**.
- Full filtered tower \(\Rightarrow\chi\): **PASS / CLOSED** at the previously stated information level.
- Exact universal Fox scheme as comparison target: **PASS / CLOSED**.

No broad representation scan is authorized.

## Final boundary

The correct problem is no longer

\[
\text{“Can we truncate Fox to degree 3?”}
\]

but

\[
\boxed{
\text{Can an intrinsic filtered object encode exactly the higher Fox information
needed for all 3-adic digits without importing Fox by definition?}
}
\]

That is the remaining genuinely difficult bridge.
