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
