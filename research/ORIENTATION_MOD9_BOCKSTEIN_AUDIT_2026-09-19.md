# ORIENTATION MOD-9 BOCKSTEIN AUDIT — 2026-09-19

## Objective

Test the explicit Bockstein/finite-coefficient candidate required by
`plans/ORIENTATION_MOD9_RECOVERY_GATE_2026-09-19.md), without using a preferred free lift and without any finite scan.

Frozen presentation:
\[
G=\langle x_1,x_2,x_3,x_4\mid r=x_1^3[x_1,x_2][x_3,x_4]\rangle,
\]
with target
\[
\chi(x_2)=(1-3)^{-1}\equiv4\pmod 9.
\]

## 1. Canonical candidate

Use the coefficient exact sequence
\[
0\to\mathbf F_3\xrightarrow{\,3\,}\mathbf Z/9
\to\mathbf F_3\to0
\]
and its connecting homomorphism
\[
\beta:H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3).
\]

This is intrinsically defined from the group and coefficient sequence. It does not choose a free lift of an automorphism.

For a standard one-relator Demushkin presentation, the Bockstein on the dual basis detects the coefficients of the power terms in the defining relation. A classical Demushkin formula states that if the relation has power coefficient \(a_i\), then
\[
\beta(\gamma_i)=a_i,
\]
and the corresponding self-cup contribution is controlled by the binomial factor from the power term. See the classical proposition reproduced in the available literature source.

For the frozen relation, the only degree-3 power term is \(x_1^3\). Hence the Bockstein has the form, up to the fixed sign/top-class convention,
\[
\beta(\gamma_1)=\omega,\qquad
\beta(\gamma_2)=\beta(\gamma_3)=\beta(\gamma_4)=0,
\]
where \(\omega\) is a generator of the one-dimensional \(H^2(G,\mathbf F_3)\).

Thus
\[
\operatorname{im}\beta=\langle\omega\rangle,
\qquad
\ker\beta=\langle\gamma_2,\gamma_3,\gamma_4\rangle.
\]

The exact scalar written as 1 depends on the chosen identification of the intrinsic one-dimensional target \(H^2\) with \(\mathbf F_3\); the map \(\beta\) itself does not.

## 2. What this object actually remembers

The Bockstein detects the existence and location of the \(3\)-power term in the defining relation. In particular it detects the same q=3 torsion/power phenomenon already visible from
\[
G^{ab}\cong\mathbf Z_3^3\oplus\mathbf Z/3.
\]

It does **not** contain the number
\[
4=(1-3)^{-1}\pmod9
\]
as a canonical scalar.

This is not merely because a convenient basis was chosen. The target of \(\beta\) is only a one-dimensional \(\mathbf F_3\)-space. Replacing the top-class generator \(\omega\) by \(c\omega\), \(c\in\mathbf F_3^\times\), rescales every displayed scalar while leaving the intrinsic map unchanged. Therefore no scalar in \(\mathbf F_3^\times\) extracted from \(\beta\) can canonically encode the specific 3-adic unit \(4\in(\mathbf Z/9)^\times\).

The mod-9 cup-product matrix carries the same limitation. Its extra diagonal term is the power-term contribution, but after passing to the first Bockstein layer it records the q=3 power coefficient rather than the orientation value \(4\).

## 3. Invariance audit

### 3.1 H^2-generator change

PASS.

The map
\[
\beta:H^1\to H^2
\]
is canonical. Choosing another generator of \(H^2\) only changes coordinates, not the map, its rank, or its kernel/image as intrinsic subspaces.

A scalar formula such as \(\beta(\gamma_1)=1\) is therefore coordinate-dependent; the coordinate-free statement is that \(\beta\) is nonzero precisely in the distinguished power-term direction.

### 3.2 H^1 basis change

PASS for the map, FAIL for extracting \(\chi(x_2)\equiv4\pmod9\).

Under a change of basis, the coordinate vector of \(\beta\) changes covariantly. Its intrinsic content is the rank-one Bockstein image/kernel configuration, not a distinguished value attached to a generator called \(x_2\).

In particular, there is no canonical operation on \(\beta\) alone that singles out the unit \(4\) rather than another element of \(1+3\mathbf Z/9\).

### 3.3 Presentation/lift changes

PASS for the Bockstein itself.

No free-group lift of an automorphism is part of the definition. Hence the specific lift-dependence obstruction that killed the relator-unit scalar is absent.

But this does not rescue the recovery target: lift-independence of \(\beta\) only proves that \(\beta\) is a genuine intrinsic cohomological object; it does not create missing 3-adic information.

## 4. Separation from the target orientation

The target orientation is a \(\mathbf Z_3^\times\)-valued character on the group:
\[
\chi:G\to\mathbf Z_3^\times,
\qquad
\chi(x_2)\equiv4\pmod9.
\]

The Bockstein is instead an \(\mathbf F_3\)-linear map
\[
H^1(G,\mathbf F_3)\to H^2(G,\mathbf F_3).
\]

These are different types of data. For the frozen q=3 presentation, \(\beta\) sees the power relation but not the first 3-adic orientation digit.

Consequently the implication
\[
\beta\quad\Longrightarrow\quad\chi\bmod9
\]
is not established and, for this candidate as a standalone invariant, fails the recovery requirement: the canonical Bockstein object collapses to the q=3 power/torsion shadow and does not retain the value 4.

## 5. Gate decision

**M9-A: PASS.** A canonical finite-coefficient object was defined.

**M9-B: PASS.** Its intrinsicity under coefficient-target trivialization and basis/lift changes is clear at the level of the Bockstein map.

**M9-C: FAIL.** The Bockstein does not canonically distinguish the orientation value
\[
\chi(x_2)\equiv4\pmod9
\]
from the other possible \(1+3\mathbf Z/9\) values. It retains q=3 power/torsion information but not the required 3-adic orientation digit.

**M9-D: CLOSED for this Bockstein candidate.**

This is a candidate-level FAIL, not a theorem that no finite-coefficient construction can ever recover \(\chi\bmod9\).

## 6. Consequence for the research program

The following claims are now frozen:

1. Mod-9 cup/Bockstein data genuinely detects the q=3 power term.
2. The Bockstein itself is canonical and avoids the failed free-lift dependence.
3. Nevertheless, the Bockstein does not recover \(\chi\bmod9\).
4. Therefore the research must not reinterpret the q=3 Bockstein signal as the orientation value 4.
5. Any next route must retain additional \(1+3\mathbf Z_3\)-valued or twisted-dualizing information that is absent from ordinary trivial-coefficient Bockstein data.
6. No finite scan is authorized for this closed candidate.

The exact open problem remains:
\[
\boxed{\text{find a genuinely intrinsic filtered/graded object retaining the first }3\text{-adic orientation layer}.}
\]

## External verification

A classical Demushkin proposition explicitly identifies the Bockstein of the dual basis with the power coefficients in the defining relation, supporting the calculation above:
https://www.numdam.org/article/BSMF_1966__94__211_0.pdf

A modern source also records the standard Demushkin cup-product characterization and the one-dimensional top cohomology target:
https://geodesic.mathdoc.fr/articles/10.4153/CJM-1967-007-8/

