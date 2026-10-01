# PAPER 3 — F2 SAME-W3 CONTROL GATE

Date: 2026-10-01

## Purpose

Test whether the F2 family admits a cyclotomic control with the same \(W_3\) quadratic relation type, which would authorize a finite-window separation computation.

## Independent verification of the audited F2 Pfaffian

Use the ordered basis
\[
(X_1,Y_1,X_2,Y_2).
\]
For
\[
R_{F2}=\langle \omega_1+\omega_2,\eta\rangle,
\qquad
\omega_1=X_1\wedge Y_1,quad
\omega_2=X_2\wedge Y_2,quad
\eta=X_1\wedge X_2,
\]
the pencil \(a(\omega_1+\omega_2)+b\eta\) has skew matrix
\[
\begin{pmatrix}
0&a&b&0\\
-a&0&0&0\\
-b&0&0&a\\
0&0&-a&0
\end{pmatrix}.
\]
For a \(4\times4\) skew matrix \(M\),
\[
\operatorname{Pf}(M)=M_{12}M_{34}-M_{13}M_{24}+M_{14}M_{23}
\]
(in 1-based indexing). Direct substitution gives
\[
\boxed{\operatorname{Pf}_{F2}(a,b)=a^2}.
\]
Thus the repeated-root type is verified directly, independently of the earlier prose calculation.

For the split free-product control
\[
R_{\mathrm{split}}=\langle \omega_1,\omega_2\rangle,
\]
the pencil has Pfaffian
\[
\boxed{\operatorname{Pf}_{\mathrm{split}}(a,b)=ab}.
\]
For the shared-direction elementary semidirect shape, represented by
\[
R_{\mathrm{shared}}=\langle X_1\wedge Y_1,\,X_1\wedge X_2\rangle,
\]
every pencil has a common factor \(X_1\), hence rank \(\le2\), and
\[
\boxed{\operatorname{Pf}_{\mathrm{shared}}(a,b)=0}.
\]

Therefore the three Pfaffian types actually audited are
\[
a^2,qquad ab,qquad 0,
\]
and \(a^2\) is not \(GL_4\)-equivalent to either of the latter two.

## Recovered examined-construction list

The repository's earlier construction-level audit records the following two relevant rank-4/two-relator shapes inside the **standard elementary-type construction scheme**:

1. **Split/free-product shape:** free product of two rank-2 one-relator factors (rank-2 Demuškin factors, or the rank-2 cyclotomic semidirect factor \(\mathbf Z_p\rtimes\mathbf Z_p\)). The two quadratic relation forms live on disjoint 2-planes, giving Pfaffian \(ab\).

2. **Shared-direction semidirect shape:** a rank-2 free factor extended by one cyclotomic semidirect \(\mathbf Z_p\) direction, then free-producted with one free generator. The two quadratic action forms share the semidirect direction, giving Pfaffian \(0\).

This is the actual list recoverable from the authoritative audit trail. No additional concrete rank-4/two-relator elementary-type shape is explicitly recorded there.

## Completeness audit

The direct Pfaffian calculation is **PASS / CLOSED** for the three recorded shapes.

The **completeness of the construction list is not independently established at theorem level** by the surviving repository record. The prior phrase “standard elementary-type construction mechanism cannot realize” was therefore too strong. What is justified is only:

> the audited/recovered candidate list consists of the two shapes above, and both are excluded by the direct Pfaffian test.

Accordingly, the mathematical status is:

- F2 × recovered/explicitly examined elementary-type candidates: **FAIL / CLOSED**.
- Completeness of the examined candidate list within the full standard elementary-type class: **OPEN**.
- F2 × arbitrary cyclotomic pro-\(p\) group: **OPEN / CONDITIONAL**.
- F2 \(W_4\) computation: **NOT AUTHORIZED**.
- Operational F2 branch: **CLOSED**; no further search is authorized unless new evidence supplies a genuinely new construction or a proof of completeness.
- Broad F2 finite-window recognition: **OPEN / CONDITIONAL**.

## Logical boundary

This audit does **not** prove a universal structural no-go for all standard elementary-type cyclotomic groups, because the completeness of the recovered candidate list has not been independently established. It also does not exclude arbitrary cyclotomic pro-\(p\) controls.

The correct negative statement is therefore candidate-level:

> In the explicitly recovered rank-4/two-relator elementary-type constructions actually examined, the F2 repeated-root quadratic type \(a^2\) is incompatible with the available Pfaffian types \(ab\) and \(0\).

No claim about an unexamined construction mechanism is made.

F1 is not reopened. A future reopening would require new mathematical evidence, not a relabeling of this audit.

## Provenance

The cyclotomic construction classes and their closure properties are grounded in the project's audited cyclotomic literature. The present audit adds an independent direct Pfaffian computation and restores the actual candidate list preserved in the repository. The completeness limitation is recorded explicitly rather than inferred.
