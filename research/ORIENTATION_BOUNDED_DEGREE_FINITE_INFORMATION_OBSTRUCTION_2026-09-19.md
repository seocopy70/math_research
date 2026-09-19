# ORIENTATION — BOUNDED-DEGREE / FINITE-INFORMATION OBSTRUCTION — 2026-09-19

## Objective

Test the stronger question:

> Can one single finite bounded-degree carrier determine the full 3-adic orientation character, rather than only one finite reduction?

The correct answer depends on what “finite carrier” is allowed to retain. The distinction between **bounded filtration degree** and **unbounded 3-adic coefficient precision** is essential.

## 1. Main obstruction under finite-information interpretation

Consider the standard family
[
G_q=langle x_1,x_2,x_3,x_4mid x_1^q[x_1,x_2][x_3,x_4]=1angle,
qquad q=3^s,
]
together with
[
G_infty=langle x_imid [x_1,x_2][x_3,x_4]=1angle.
]

The quadratic initial relation is the same:
[
R_2=[X_1,X_2]+[X_3,X_4].
]

For the Demuškin orientation, the standard crossed-derivation relation gives
[
chi_q(x_1)=chi_q(x_3)=chi_q(x_4)=1,
qquad
chi_q(x_2)=(1-q)^{-1},
]
while
[
chi_infty(x_i)=1.
]

Thus the full characters are different for every finite (q=3^s), even though
[
(1-3^s)^{-1}	o 1
]
3-adically.

## 2. Fixed bounded filtration degree cannot be universal

In the p-Zassenhaus filtration, the power term (x_1^{3^s}) first occurs in filtration degree (3^s).

Fix any degree bound (d). Choose (s) with
[
3^s>d.
]

Then through degree (d), the defining relation of (G_{3^s}) has the same visible initial filtered relation as (G_infty):
[
R_2=[X_1,X_2]+[X_3,X_4].
]

But
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
eq1=chi_infty(x_2)
]
in (mathbf Z_3^	imes).

Therefore:

[
oxed{
	ext{No universal carrier with a fixed finite Zassenhaus-degree bound can recover full }chi
}
]

provided the carrier is constructed from the bounded filtered information in the natural way and does not smuggle in the omitted q-data by definition.

This is a genuine information obstruction, not a failure of a particular candidate invariant.

## 3. Adding finite 3-adic precision does not repair the obstruction

Suppose a proposed carrier is allowed bounded degree (d) and only finite coefficient precision modulo (3^N).

Choose (s) so that
[
3^s>max(d,N).
]

Then:

1. the power term (x_1^{3^s}) is invisible below degree (d);
2. its coefficient is also zero modulo (3^N);
3. hence the bounded-degree, bounded-precision carrier agrees with the corresponding q=infty carrier;
4. nevertheless
[
chi_{3^s}(x_2)=(1-3^s)^{-1}
ot=1.
]

Indeed
[
(1-3^s)^{-1}equiv1pmod{3^N}
]
for (sge N), but the two 3-adic units are not equal.

So:

[
oxed{
	ext{fixed degree + fixed finite 3-adic precision cannot determine full }chi.
}
]

## 4. Important loophole: exact (mathbf Z_3)-precision

There is one logically different possibility.

If “bounded-degree carrier” is allowed to retain **exact (mathbf Z_3)-valued coefficients**, then bounded degree does not mean finite information. In that setting the degree-3 filtered relation for the fixed q=3 group can carry the exact power coefficient, and the exact crossed-derivation equation
[
1+2ho(x_2)=0
]
can be solved directly in (mathbf Z_3):
[
ho(x_2)=(1-3)^{-1}.
]

That is compatible with the hand derivation already established in this project.

But such an object is not a finite-information carrier: its coefficient ring itself has infinitely many 3-adic digits. It therefore does not contradict the finite-information obstruction above.

This distinction must be frozen before making any absolute “bounded-degree” theorem.

## 5. Consequence for the current project

The question should therefore be split into two precise statements.

### A. Finite-information bounded-degree carrier

[
oxed{	ext{IMPOSSIBLE universally.}}
]

For every fixed degree bound (d) and finite precision (N), sufficiently large (q=3^s) gives the same bounded carrier as (q=infty) but a different full orientation.

### B. Fixed q=3 with exact (mathbf Z_3)-coefficients

A bounded-degree exact-(mathbf Z_3) carrier may determine the full character. This is not yet a separate carrier theorem because the exact intrinsic/projective definition and its functoriality still need to be stated carefully.

## 6. What this does and does not prove

It does prove a universal obstruction for any carrier whose information is genuinely bounded both in filtration degree and 3-adic precision.

It does **not** prove that every conceivable exact-(mathbf Z_3)-valued bounded-degree object fails. Such an object has infinite information and belongs to a different category.

It also does not say that the already established projective mod-9 jet (J_3) itself recovers all higher digits. (J_3) as currently defined is an (mathbf F_3)-level/projective jet and only recovers (chimod9).

## 7. Decision

**PASS / CLOSED:** universal finite-information bounded-degree recovery of the full 3-adic character is obstructed.

**OPEN:** whether a natural exact-(mathbf Z_3), bounded-filtration-degree projective carrier for the fixed q=3 group can be defined so that it recovers the full (chi).

No broad scan is needed for this obstruction; it is a direct filtration/precision argument.
