# Paper 5 — Zassenhaus Stabilization Audit (2026-10-06)

## Claim audited

Proposed arbitrary-n closure:

> If (W_{p+1}=W_p), together with (D_p(W_p)\cong\mathbf F_p^3) and (D_{p+1}(W_p)=1), then (W_n=W_p) for every (n\ge p).

The proposed proof passes to the restricted Lie algebra of the free pro-(p) group and attempts an induction on
(M_k=D_k(F)R).

## Independent audit

### 1. The decisive induction step is invalid

The proof claims, for (c=\lceil(k+1)/p\rceil\ge p),

[
D_c\subseteq D_p\subseteq M_{p+1},
]

because (D_p(W_p)\cong\mathbf F_p^3).

This inclusion is false.

By definition
[
D_p(W_p)=M_p/M_{p+1}\cong\mathbf F_p^3
]
is **nonzero**. Hence (D_p\not\subseteq M_{p+1}). In fact the three surviving classes represented by (x^p,y^p,z^p) are precisely the obstruction to that inclusion.

Therefore the asserted containment
[
D_c^p\subseteq M_{p+1}
]
for the (c\ge p) branch is not established. This is a load-bearing failure: the induction cannot be completed.

### 2. The restricted-ideal statement is insufficient for stabilization

The proof argues that the degree-(p) Lie part lies in the initial restricted ideal (J), and then treats this as if it killed every later contribution.

That does not follow.

A restricted ideal containing the degree-(p) Lie component is automatically closed under brackets and (p)-powers of the elements already in the ideal, but it does **not** thereby contain unrelated (p)-powers such as the degree-(2p) layer coming from (L_2^{[p]}).

Thus even at the associated-graded level, killing the degree-(p) Lie component does not by itself imply that every degree (>p) component lies in the ideal.

The statement (M_{p+2}=M_{p+1}) only controls the corresponding next graded layer; it does not automatically annihilate all later restricted-Lie layers.

### 3. The (D_p(W_p)) hypothesis points in the opposite direction

The proposed proof uses
[
D_p(W_p)\cong\mathbf F_p^3
]
both as a surviving nonzero (p)-power layer and, in the induction, as though (D_p\subseteq M_{p+1}).

These are incompatible.

The correct statement is
[
D_p(W_p)=M_p/M_{p+1}\cong\langle X,Y,Z\rangle\cong\mathbf F_p^3,
]
so (D_p) survives modulo (M_{p+1}).

### 4. Standard Zassenhaus/Jennings facts do not supply the missing implication

The Zassenhaus filtration is a restricted filtration: commutators raise degree additively and (p)-powers multiply degree by (p), and the associated graded object is a restricted Lie algebra. These standard facts do not state that equality of two consecutive quotient filtration terms (D_{p+2}R=D_{p+1}R) propagates to all later terms.

Therefore invoking the Jennings recursion is legitimate background, but the required stabilization implication remains a separate theorem and is not obtained by the displayed induction.

## Classification

- proposed Zassenhaus stabilization proof: **FAIL / CLOSED as submitted**;
- implication (W_{p+1}=W_p\Rightarrow W_n=W_p) for all (n\ge p): **OPEN / LOAD-BEARING**;
- arbitrary-n Frattini-image theorem: **OPEN / LOAD-BEARING**;
- (n<p) boundary (W_n\cong\mathbf F_p^3), (Aut(W_n)=GL_3(\mathbf F_p)): unchanged, **PASS / CLOSED** in the declared scope;
- (n=p,p+1) theorem: unchanged, **PASS / CLOSED / GENERAL**;
- Run 37381098677: unchanged, **PASS / LOCAL**.

## Consequence

Do **not** promote the final table
[
\operatorname{Im}_n=
\begin{cases}
GL_3(\mathbf F_p),&n<p,\\
S'_{11}(p),&n\ge p
\end{cases}
]
to the Paper 5 theorem.

The correct current boundary remains:
[
n<p:\ PASS/CLOSED,qquad
n=p,p+1:\ PASS/CLOSED/GENERAL,qquad
n>p+1:\ OPEN/LOAD-BEARING.
]

The next authorized task is to seek a genuine stabilization theorem (or a counterexample/witness) rather than reuse the invalid induction. No blind numerical sweep is authorized merely to replace the missing proof.
