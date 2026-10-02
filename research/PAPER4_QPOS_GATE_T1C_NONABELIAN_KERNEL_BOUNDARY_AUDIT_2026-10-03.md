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
