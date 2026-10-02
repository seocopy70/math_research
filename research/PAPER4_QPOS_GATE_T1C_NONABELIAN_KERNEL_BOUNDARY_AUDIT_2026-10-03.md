# PAPER 4 — GATE T1-C: FIRST NONABELIAN KERNEL BOUNDARY — 2026-10-03

## Purpose

This audit pushes Gate T beyond the closed scalar/coinvariant and critical-norm shortcuts. It does **not** claim that the exact relative threshold has been proved.

For
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad
r_D=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d],
\qquad s>a,
\]
put
\[
W_s=G_{s,a}/D_{p^s+1}(G_{s,a}),
\quad
Q_s=D/D_{p^s+1}(D),
\quad
K_s=\ker(W_s\to Q_s).
\]

## 1. The scalar cancellation is genuinely a lift-change phenomenon

The central class-2 detector used previously is insufficient as a nonsplitting witness. In the rank-two stress relation
\[
r_D=x^q[x,y],\qquad q=p^a,
\]
the scalar defect \(z^{p^s}\) can be cancelled at the abelianized/central level by changing the \(x\)-lift by a \(p^{s-a}\)-power of the kernel generator.

This is not merely an abstract cohomological warning: it is visible in the relation-module differential. The Fox row contains a coefficient whose augmentation is \(q=p^a\), so multiplication by \(p^{s-a}\) can remove the scalar \(p^s\)-defect. This is exactly the cancellation already recorded in T1-A.

Therefore the scalar class alone cannot certify nonsplitting.

## 2. Where the cancellation stops being scalar

The same lift change is not purely scalar before coinvariants. Conjugating the kernel generator by the second Demuškin generator contributes a non-augmentation term (equivalently, a \((y-1)\)-direction after choosing the standard rank-two convention and passing to the relation module).

Schematically, if \(k=z^{-p^{s-a}}\) is the scalar correction, then the first-order relator change has the form
\[
\delta r
=
\bigl(\text{augmentation part}\bigr)\,k
+
\bigl(\text{non-coinvariant }(y-1)\text{-part}\bigr)\,k
+\cdots.
\]
The augmentation part cancels \(z^{p^s}\); the non-coinvariant part is the first possible residual obstruction.

This is **not yet a theorem that the residual survives**. It identifies the exact layer that must be tested.

## 3. First nonabelian quotient of the kernel

The correct hierarchy is now:

\[
K_s
\longrightarrow
A_s=K_s/[K_s,K_s]
\longrightarrow
B_s=\gamma_2(K_s)/\gamma_3(K_s)
\longrightarrow\cdots
\]

The abelianized module \(A_s\) is the first diagnostic. Its coinvariant scalar quotient is already closed as an obstruction. The remaining question is whether the non-coinvariant \(Q_s\)-module structure in \(A_s\) already detects a nonzero extension defect.

If it does not, the next authorized layer is \(B_s\). This is the precise meaning of “first nonabelian quotient”: not an arbitrary class-2 construction, but the first lower-central quotient of the **actual finite kernel**.

## 4. A useful stress calculation, but not a theorem

At the rank-two level, a lift correction of size \(p^{s-a}\) has a commutator contribution whose formal filtration scale is governed by the power of a degree-two kernel commutator. Since
\[
2p^{s-a}<p^s+1
\]
for odd \(p\) and \(s>a\), such a contribution is not automatically killed by the critical quotient.

This is important: the earlier scalar cancellation cannot simply be declared to remove the entire defect. It may move the obstruction from the scalar layer into a much lower nonabelian/lower-filtration layer.

But the inequality alone proves only **possible visibility**, not nonvanishing. A quotient calculation is required to show that the corresponding kernel commutator is actually nonzero.

## 5. What is now closed

The following shortcuts are permanently closed for Gate T:

- scalar \(z^{p^s}\) as a nonsplitting witness;
- coinvariant/augmentation-only extension class;
- critical norm equation \(N_{p^s}(T_x)c_x(\bar z)=0\) as a nonzero witness;
- “one-dimensional \(H^2(D,\mathbf F_p)\) therefore finite extension is nonsplit” without a lift-change quotient;
- any replacement of the actual kernel by an assumed abelian kernel.

## 6. What remains genuinely open

The exact question is:

> Does the actual finite extension
> \[
> 1\to K_s\to W_s\to Q_s\to1
> \]
> admit a section?

Equivalently, after all generator/lift changes, does the defining relator defect vanish in the first nontrivial quotient of the actual kernel?

The minimum computation is therefore:

1. construct \(A_s=K_s/[K_s,K_s]\) as a finite \(\mathbf F_p[Q_s]\)-module, not merely its coinvariants;
2. write the actual relation-module differential induced by \(r_D\);
3. quotient its defect space by **all** lift-change coboundaries;
4. test whether the resulting class is nonzero;
5. if zero, compute \(B_s=\gamma_2(K_s)/\gamma_3(K_s)\) and repeat.

A nonzero class at step 3 is sufficient for nonsplitting. Vanishing is not sufficient for splitting.

## 7. Literature control

Relation modules of pro-\(p\) presentations are naturally modules for the presented group, and Fox derivatives provide the corresponding differential. This is the correct formalism for the remaining calculation. citeturn0search1turn0search21

The standard odd-prime Demuškin presentation
\[
x_1^q[x_1,x_2]\cdots[x_{d-1},x_d]=1
\]
is independently confirmed in the literature. citeturn1search24

No literature source found here proves the present finite-window extension class. Therefore no novelty or threshold theorem is claimed from the literature alone.

## 8. Classification

- critical-layer visibility: **PASS / LOCAL**;
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm shortcut: **FAIL / CLOSED**;
- non-coinvariant kernel module as the next diagnostic: **OPEN / LOAD-BEARING**;
- first nonabelian kernel quotient as fallback: **OPEN / LOAD-BEARING**;
- critical nonsplitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{\mathrm{rel}}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- unmarked filtered-group theorem: **OPEN**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

## 9. Next authorized action

The next computation is singular:

\[
\boxed{
\text{compute the actual }\mathbf F_p[Q_s]\text{-relation module }A_s
\text{ at }n=p^s+1,
\text{ including its non-coinvariant action.}
}
\]

Only after that calculation may the branch be promoted to a genuine cohomological obstruction or closed as a splitting phenomenon.


## 10. Gate T1-C correction recorded 2026-10-03

The T1-C audit is tightened as follows: “lift change kills the scalar defect” means only **coinvariant/augmentation-level cancellation**. Full finite-extension cancellation is unproved because (z) is not assumed central and the exact change is controlled by the action/norm operator. (A_s=K_s^{ab}) is the first diagnostic layer but has not yet been computed; the next step is its actual finite (mathbf F_p[Q_s])-module and extension class after all lift-change coboundaries. (B_s=\gamma_2(K_s)/\gamma_3(K_s)) is a conditional fallback, not an asserted universal first obstruction. The Gate-T frontier remains OPEN / LOAD-BEARING and blind carrier search remains STOP.

## 2026-10-03 — GATE T1-C CRITICAL RE-AUDIT: A_s / PUSHOUT / RAW-RESIDUAL BOUNDARY

A further critical review tightens the Gate T1-C object and obstruction logic without changing the frontier.

1. **A_s versus its mod-p reduction must be separated.** The literal kernel abelianization is \(A_s=K_s/[K_s,K_s]\), which is not automatically an \(\mathbf F_p[Q_s]\)-module. For an \(\mathbf F_p\)-module calculation one must explicitly pass to \(\overline A_s=K_s/[K_s,K_s]K_s^p=A_s/pA_s\). No identification of these two objects is authorized.

2. **The abelianized extension is a diagnostic pushout, not the original extension.** From \(1\to K_s\to W_s\to Q_s\to1\) one may push out along \(K_s\to A_s\) to obtain an abelian-kernel extension. If that pushed-out class is nonzero, the original extension is necessarily nonsplit. If it vanishes, the original extension may still be nonsplit. Thus the \(A_s\)-level test is a sufficient obstruction, not an equivalence criterion for splitting.

3. **The raw residual is not the extension class.** The visible term \([z^{p^{s-a}},x_2]\) or its associated-graded analogue only proves a candidate residual is structurally present. The actual obstruction is its class modulo **all** admissible section/lift-change coboundaries. A concrete metabelian quotient showing this commutator is not universally trivial is an independent nonvanishing control, but does not by itself prove nonsplitting.

4. **Associated-graded survival is not yet proved.** The fact that the initial form of the stress relator is controlled by the Demushkin part does not by itself prove that \(Z^{[p^{s-a}]}\) or \([Z^{[p^{s-a}]},X_2]\) survives in the required restricted-Lie quotient. This needs an explicit quotient/independence calculation.

5. **Correct load-bearing question.** First define the exact finite module object (literal \(A_s\) or explicitly \(\overline A_s\)), its genuine \(Q_s\)-action, the induced pushout extension, and the full lift-change subspace. Then test the residual class. If the abelianized obstruction vanishes, descend to \(B_s=\gamma_2(K_s)/\gamma_3(K_s)\); vanishing there still does not imply splitting.

### Updated classification
- critical-layer visibility: **PASS / LOCAL**;
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- critical norm shortcut: **FAIL / CLOSED**;
- raw action residual: **PASS / LOCAL**;
- raw residual modulo all lift coboundaries: **OPEN / LOAD-BEARING**;
- actual abelianized-kernel obstruction: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{rel}(s)=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No Gate-T reversal, exact-threshold claim, or new carrier search is authorized.


## 2026-10-03 — MINIMAL p=3 CHECK: RAW RESIDUAL IS NOT YET AN OBSTRUCTION

In the minimal case p=3, s=2, a=1, d=2, the rank-two Fox derivative satisfies partial_x r = N_3(x)+x^3-y. Writing X=x-1 and Y=y-1 over F_3 gives leading term -Y. A degree-3 kernel correction therefore generates a degree-4 Y-direction, the same filtered direction represented by the candidate [z^3,y]. Hence the raw non-coinvariant residual is structurally visible but is also generated by the lift-change differential. It cannot be promoted to an A_s obstruction merely from its nonzero raw representative.

The complete quotient by all lift changes remains the load-bearing test. Current classification: raw action residual PASS/LOCAL; candidate [z^3,y] alone FAIL/CLOSED as an obstruction; complete A_s diagnostic OPEN; full extension splitting OPEN/LOAD-BEARING; exact relative threshold OPEN/LOAD-BEARING.


## 11. 2026-10-03 — FOX IMAGE FIRST-LAYER ANALYSIS

The authorized continuation was carried out at the structural, rather than candidate-search, level. Put
\[
q=p^a,\qquad m=p^{s-a},\qquad qm=p^s.
\]
For the critical rank-two factor
\[
r_D=x_1^q[x_1,x_2],
\]
let k be a kernel lift correction whose first nonzero filtered degree is m. The Fox/lift-change differential has two relevant first-order pieces.

First, the derivative of x_1^q contributes the q-fold norm. Its augmentation is q, so choosing the scalar coefficient m removes the degree-p^s augmentation defect because qm=p^s. This is precisely the already-closed coinvariant cancellation.

Second, the derivative of the commutator [x_1,x_2] contributes the augmentation-ideal direction generated by x_2-1 acting on k. In the associated filtered degree this is the class represented by
\[
[k,x_2],
\]
and for k with leading z^m this is the previously proposed
\[
[z^m,x_2].
\]
Thus the candidate is not outside the first-order gauge image: it is produced by the same Fox differential that performs the scalar lift correction.

The minimal case p=3,s=2,a=1 gives the concrete check
\[
\partial_{x_1}r_D=N_3(x_1)+x_1^3-x_2,
\]
whose leading augmentation-ideal term is -Y over F_3. The general q=p^a calculation has the same structural source: the power part supplies augmentation q, while the commutator part supplies the x_2-1 direction.

The filtration inequalities
\[
m+1<p^s+1,
\qquad 2m<p^s+1
\]
for odd p and s>a show that this direction is visible before the critical cutoff. They do not show that it survives quotienting by lift changes.

### Result

The specific first-layer residual is now classified as
\[
\boxed{\text{FAIL / CLOSED as an independent obstruction}.}
\]
More precisely, the quotient of this one-dimensional candidate direction by the corresponding first-order Fox/lift-change image is zero.

This is **not** a computation of the complete \(A_s\). Higher filtered terms can in principle produce further cokernel classes. Therefore:

- first-layer raw residual: **PASS / LOCAL**;
- first-layer candidate obstruction modulo Fox image: **FAIL / CLOSED**;
- complete \(A_s\)-level extension class: **OPEN / DIAGNOSTIC**;
- full finite extension splitting: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**.

### Methodological consequence

The research is not returning to detailed carrier hunting. The correct next object is the full graded cokernel
\[
\mathcal C_s
=
\frac{\text{all filtered first-order defect directions at the critical window}}
{\text{image of all admissible Fox/lift-change differentials}}.
\]
A nonzero element of \(\mathcal C_s\) would be a genuine gauge-invariant A_s-level obstruction. If \(\mathcal C_s=0\) throughout the relevant filtered range, the entire A_s route is closed and only then may the conditional \(B_s\) route be opened.


## 12. 2026-10-03 — FULL FIRST-ORDER FOX IMAGE / MOD-p Abar CLOSURE

The first-layer analysis can be strengthened from one candidate direction to the whole augmentation-ideal tangent space.

Let (I=ker(mathbf F_p[Q_s]	omathbf F_p)). For the critical rank-two factor (r=x_1^q[x_1,x_2]), (q=p^a), the Fox derivatives satisfy modulo (I^2):
[
partial_{x_1}r\equiv -(x_2-1),qquad
partial_{x_2}requiv x_1-1.
]
Indeed the (q)-power norm contributes no linear term in characteristic (p), while the commutator derivatives supply the two degree-one directions. Thus the two Fox entries generate (I/I^2).

Because (Q_s) is a finite (p)-group, (I) is the Jacobson radical of (mathbf F_p[Q_s]). Nakayama implies that the ideal generated by the two Fox entries is all of (I). Therefore every first-order mod-(p) non-coinvariant lift-change direction in the augmentation ideal is gauge-generated. The previous residual ([z^{p^{s-a}},x_2]) is consequently not merely one removable direction: it belongs to a whole Fox-generated tangent space.

This closes the first-order mod-(p) abelianized cokernel as an obstruction. It does not compute the literal integral (A_s=K_s/[K_s,K_s]), does not establish full splitting, and does not prove the exact threshold. Higher filtered terms and genuinely nonlinear/lower-central defects remain outside this first-order calculation.

### Classification
- first-layer candidate obstruction: **FAIL / CLOSED**;
- first-order mod-(p) abelianized Fox cokernel: **FAIL / CLOSED**;
- literal (A_s)-level extension class: **OPEN / DIAGNOSTIC**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact relative threshold: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

### Next authorized boundary

Do not search for another residual in the same mod-(p) abelianized layer. If the research target is the mod-(p) finite-window obstruction, the Abar/Fox route is now closed. If integral (p)-power information is essential, it must be formulated separately as an integral (A_s) problem. Otherwise the conditional next layer is the actual (B_s=gamma_2(K_s)/gamma_3(K_s)), with its own object/input/gauge pre-check.


## 2026-10-03 — T1-C CRITICAL REVIEW: RECURSIVE LIFT-ABSORPTION IS NOT ESTABLISHED

A critical review of the proposed recursive lift-absorption argument found a load-bearing gap. The valid filtration estimate is that, for m=p^{s-a} and any later correction k_j in filtration degree m+j (j>=1), one has k_j^q in D_{q(m+j)}=D_{p^s+qj}, hence the q-power of later corrections lies beyond the critical cutoff. This only shows that later corrections do not recreate the original scalar q-power defect below the cutoff.

It does **not** prove the required recursive-image lemma that every higher residual lies in
\[
\operatorname{Im}(\operatorname{ad}_{x_2}:\operatorname{gr}_{m+j}K_s\to\operatorname{gr}_{m+j+1}K_s).
\]
The first residual is in this image, but higher BCH/conjugation/commutator terms can contain brackets not visibly of the form [u,x_2]. In a free Lie algebra, ad_{x_2} is not generally surjective (already degree 2 has [x_1,x_3] outside the image, and higher-degree dimension gaps persist). Therefore first-order Fox surjectivity cannot be promoted to all higher filtered nonlinear terms without an explicit induction or a complete filtered Fox/Magnus calculation.

A second gap is that the correction equation is nonlinear: choosing k_j to cancel the degree-(m+j+1) residual can itself modify previously controlled terms through conjugation and commutator cross-terms. Degree counting alone does not establish triangular solvability.

Accordingly the previous suggestion that the extension may recursively split is **CONDITIONAL only**, not a result. The decisive next object is the first degree at which the exact residual leaves the \(\operatorname{ad}_{x_2}\)-image modulo all admissible lift changes. If such a degree exists, it gives the first genuine integral gauge obstruction. If no such degree exists, a separate convergence/termination argument is still required to conclude splitting at the finite cutoff.

Updated classification:
- scalar/coinvariant obstruction: **FAIL / CLOSED**;
- first-order mod-p Fox cokernel: **FAIL / CLOSED**;
- recursive q-power filtration estimate: **PASS / LOCAL**;
- recursive-image lemma: **OPEN / LOAD-BEARING**;
- recursive lift absorption: **CONDITIONAL**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact n_sep^rel(s)=p^s+1: **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.

No claim that the stress-family extension splits is authorized. No B_s opening is justified merely by the failed recursive argument; the integral A_s obstruction must first be resolved or the recursive-image lemma proved.

## 2026-10-03 — T1-C DEGREE-5 TEST REFORMULATED: \(\operatorname{ad}_{x_2}\)-COKERNEL IS NOT THE GAUGE QUOTIENT

The proposed minimal split “compute \(R_5\bmod\operatorname{Im}(\operatorname{ad}_{x_2})\)” was critically audited before execution. It is **not** the correct gauge-invariant degree-5 obstruction.

The reason is structural: \(R_5\) is a residual in a nonlinear lifting problem, while admissible lift changes are governed by the full filtered Fox/relation-module differential. The degree-5 gauge image is therefore not, in general, the single subspace
\[
\operatorname{Im}\bigl(\operatorname{ad}_{x_2}:\operatorname{gr}_4K_s\to\operatorname{gr}_5K_s\bigr).
\]
A class may lie outside \(\operatorname{Im}(\operatorname{ad}_{x_2})\) and nevertheless be removed by a different admissible generator/lift correction, or by a coupled Fox differential involving the power and commutator parts. Conversely, membership in the \(\operatorname{ad}_{x_2}\)-image does not by itself identify the full coboundary quotient.

This matters especially because the preceding first-order computation already showed that the candidate \([z^{p^{s-a}},x_2]\) is generated by the Fox/lift-change differential. The correct higher-degree object is therefore the filtered cokernel
\[
\mathcal C_{s,d}
=
\frac{\text{all degree-}d\text{ defect directions}}
{\operatorname{Im}(\text{full admissible Fox/lift-change differential at degree }d-1)},
\]
with the actual finite-kernel/module relations imposed first. Only a nonzero class in this quotient is a genuine \(A_s\)-level obstruction.

Consequently the suggested degree-5 binary test
\[
R_5\in\operatorname{Im}(\operatorname{ad}_{x_2})
\quad\text{vs.}\quad
R_5\notin\operatorname{Im}(\operatorname{ad}_{x_2})
\]
is **FAIL / CLOSED as a load-bearing criterion**. It is at most a diagnostic inside a chosen normal form, not an intrinsic obstruction test.

This is not a retreat from the calculation. It removes one more false shortcut. The next and only authorized computation is the actual degree-5 component of the full Fox/lift-change cokernel in the minimal model \((p,s,a)=(3,2,1)\), after the finite-kernel quotient is fixed. If that component is zero, degree 5 yields no \(A_s\)-obstruction; if nonzero, it is a genuine gauge-invariant candidate. No \(B_s\) branch opens before this quotient is resolved.

Classification:
- degree-5 raw residual: **OPEN / DIAGNOSTIC**;
- \(R_5\) modulo \(\operatorname{ad}_{x_2}\) as obstruction: **FAIL / CLOSED**;
- degree-5 full Fox/lift-change cokernel: **OPEN / LOAD-BEARING**;
- complete mod-\(p\) first-order Fox cokernel: **FAIL / CLOSED**;
- integral \(A_s\)-level extension obstruction: **OPEN / LOAD-BEARING**;
- full finite extension splitting/non-splitting: **OPEN / LOAD-BEARING**;
- exact \(n_{\mathrm{sep}}^{rel}=p^s+1\): **OPEN / LOAD-BEARING**;
- blind carrier search: **STOP / NOT AUTHORIZED**.



## 2026-10-03 — DEGREE-5 FULL-FOX STRUCTURAL VERIFICATION

The degree-5 computation was reformulated intrinsically before execution. The rejected test was the single map ad_{x_2}; the correct degree-5 gauge space is generated by the full degree-one Q_s-action on degree-4 kernel defects.

Let L be the ordinary free Lie algebra on the degree-one generators and I=(z) the Lie ideal generated by the kernel direction. Then I is generated as a graded Lie ideal by z, hence for degree 5:
\\[
I_5=[I_4,L_1].
\\]
Therefore the full action map
\\[
I_4\\otimes L_1\\longrightarrow I_5,qquad u\\otimes v\\mapsto [u,v]
\\]
is surjective. The two degree-one Fox directions supplied by the critical relator x_1^3[x_1,x_2] are exactly the x_1- and x_2-action components at this filtered level. Consequently the degree-5 ordinary-Lie defect quotient by all admissible first-order lift changes is zero.

This is the missing structural check requested after the earlier \\operatorname{ad}_{x_2}-only no-go. It establishes that the visible degree-5 commutator route is a gauge artifact, not a genuine A_s obstruction.

The result must not be overextended: the restricted Lie algebra at p=3 has a new p-power operation. A degree-2 kernel class can contribute a degree-6 restricted-power class, so degree 6 is the first structurally different diagnostic. The present calculation does not show that such a class is actually produced by the stress relator; it only identifies the next place where ordinary-Lie gauge generation no longer exhausts the formal operations.

Classification:
- degree-5 full Fox ordinary-Lie cokernel: **FAIL / CLOSED**;
- degree-5 commutator path: **FAIL / CLOSED**;
- integral/restricted A_s obstruction: **OPEN / LOAD-BEARING**;
- full extension splitting/non-splitting: **OPEN / LOAD-BEARING**.
