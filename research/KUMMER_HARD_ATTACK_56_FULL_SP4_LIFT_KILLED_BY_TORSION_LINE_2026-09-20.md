# HARD ATTACK 56 — FULL H-LIFT IS IMPOSSIBLE: TORSION-LINE OBSTRUCTION

Date: 2026-09-20

## Target
Attack the HA55 load-bearing gate: does the previously computed full symplectic group
\[
H_U\cong Sp_4(\mathbf F_3),\qquad |H_U|=51840
\]
(or its projective image \(PSp_4(3)\)) act on the frozen \(q=3\) central extension
\[
1\to W\to Q_2\to V\to1
\]
through actual automorphisms of the Demuškin group/finite quotient?

## 1. Intrinsic obstruction already present in degree one

The repository has an independently recorded intrinsic fact for the frozen \(q=3\) group:
\[
G^{ab}\cong \mathbf Z_3^3\oplus \mathbf Z/3,
\]
and the Frattini image of the torsion subgroup \(\operatorname{Tor}(G^{ab})\cong\mathbf Z/3\) is the distinguished line
\[
\ell=\langle e_1\rangle\subset V=G/P_2.
\]
Every actual automorphism of \(G\) preserves \(\operatorname{Tor}(G^{ab})\), hence preserves \(\ell\).

Therefore the degree-one image of \(\operatorname{Aut}(G)\) is contained in the stabilizer of \(\ell\). In particular, the full \(Sp_4(\mathbf F_3)\) action cannot be the action of actual automorphisms of the frozen \(q=3\) Demuškin group.

## 2. Explicit witness inside the full symplectic group

Using the authoritative convention
\[
J=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
\qquad t_v=I+v(Jv)^T,
\]
take \(v=e_2\). Then \(J e_2=e_1\), so
\[
t_{e_2}e_1=e_1+e_2.
\]
Hence \(t_{e_2}\in Sp_4(\mathbf F_3)\) does not preserve \(\ell=\langle e_1\rangle\).

Thus this element cannot be induced by an automorphism of \(G\), and therefore cannot furnish an automorphism of \(Q_2\) compatible with the filtered quotient of the actual group.

## 3. Consequence for HA55

The proposed lift of the **full** previously computed symplectic \(H\)-action to \(Q_2\) is impossible.

This is not an implementation failure and not merely “no proof found”: it is a structural obstruction from the intrinsic torsion line.

Therefore:
\[
\boxed{\text{full }Sp_4(\mathbf F_3)\text{-lift to }Q_2\text{ FAILS / CLOSED}.}
\]
Likewise, treating the 19D \(\mathcal S\) as a full \(Sp_4(\mathbf F_3)\)-module arising functorially from \(Q_2\) is not justified.

## 4. Important remaining branch

The obstruction only kills the **full** symplectic action. It does not yet prove that the line-stabilizer subgroup
\[
P=\operatorname{Stab}_{Sp_4(\mathbf F_3)}(\ell)
\]
can or cannot lift.

The orbit-stabilizer data already recorded in the project give the full-group stabilizer size 1296 for a line/vector representative in the corresponding action, while the projective effective stabilizer has size 648 after the central kernel is removed. This is consistent with the parabolic-line-stabilizer picture, but does not by itself prove an automorphism lift.

The next branch is therefore:

1. identify the actual degree-one automorphism image \(H_{\mathrm{aut}}\) precisely;
2. compare it with \(\operatorname{Stab}_{Sp_4}(\ell)\) (or the corresponding GSp stabilizer, depending on the actual multiplier convention);
3. prove or disprove its lift to \(Q_2\);
4. only if that passes, construct the induced action on \(\mathcal S\).

No full-Sp4 module decomposition of \(\mathcal S\) should be attempted as an intrinsic claim.

## 5. Conceptual significance

This result is actually informative for the orientation problem. The full symplectic symmetry used in the earlier degree-4 orbit/module analysis is an **ambient graded symmetry**, not the actual automorphism symmetry of the frozen \(q=3\) Demuškin group.

The intrinsic torsion line is precisely the sort of low-degree datum that distinguishes the actual automorphism category from the larger ambient \(Sp_4\) category. Therefore any future \(\mathcal S\)-action relevant to intrinsic orientation must use the actual stabilizer/lift category, not the full ambient symplectic group.

This also prevents a serious tautology: importing the full \(Sp_4\) symmetry into the finite extension would erase the intrinsic line that the actual group necessarily preserves.

## Decisions

- full \(Sp_4(\mathbf F_3)\) lift to \(Q_2\): **FAIL / CLOSED**;
- full \(Sp_4\)-module interpretation of \(\mathcal S\) as an intrinsic finite-extension module: **FAIL / CLOSED**;
- actual automorphism image / line-stabilizer identification: **OPEN / LOAD-BEARING**;
- lift of the actual automorphism image to \(Q_2\): **OPEN / LOAD-BEARING**;
- \(\mathcal S\) as module for the actual automorphism image: **OPEN / LOAD-BEARING**;
- twisted \(\beta_\rho^2\) on \(\mathcal S\): **OPEN / LOAD-BEARING**;
- orientation-selector role of \(\mathcal S\): **OPEN / DECISIVE**.

## Classification

**FAIL / CLOSED for the full ambient symplectic lift.**

This is a genuine structural boundary, not a failure of the overall research program. The next authorized attack is the smaller actual automorphism/stabilizer category.
