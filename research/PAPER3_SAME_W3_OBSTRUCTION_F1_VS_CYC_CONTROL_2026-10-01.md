# PAPER 3 — SAME-W3 OBSTRUCTION: F1 vs A CYCLOTOMIC FREE-PRODUCT CONTROL

Date: 2026-10-01
Status: **PASS / LOCAL for the obstruction; exact recognition threshold OPEN / LOAD-BEARING**

## 1. Purpose

After Phase B, adding more named families whose quadratic shadows differ was deemed redundant. The decisive test is whether the W_3 carrier can fail to see 1-cyclotomicity.

For the smallest concrete case (p,d,q)=(3,2,3), define

\[
G_{F1}=\langle x_1,y_1,x_2,y_2\mid [x_1^3,y_1][x_2,y_2]=1\rangle_{\hat 3},
\]

and the cyclotomic control

\[
G_{cyc}=D_{1,3}*_{\hat 3}F(x_1,y_1),
\]

where

\[
D_{1,3}=\langle x_2,y_2\mid x_2^3[x_2,y_2]=1\rangle_{\hat 3}.
\]

The control is 1-cyclotomic because it is a free pro-p product of a cyclotomic Demushkin pair and a free pro-p group.

## 2. Global target separation

Blumer–Quadrelli prove that every F1 group is not 1-cyclotomic. The Demushkin group has its canonical 1-cyclotomic orientation, and the free product of cyclotomic pairs is cyclotomic. Therefore

\[
T_{cyc}(G_{F1})\ne T_{cyc}(G_{cyc}).
\]

This is a genuine target separation, not a presentation-label distinction.

## 3. W_3 equality

For F1 with (p,d,q)=(3,2,3), the defining relator has initial degree-2 form

\[
[X_2,Y_2].
\]

The additional term [x_1^3,y_1] begins in Zassenhaus degree 4.

For the control G_cyc, the only relator is
\[
x_2^3[x_2,y_2],
\]
whose initial degree-2 form is also [X_2,Y_2]. Its p-power correction begins in degree 3, but W_3=G/D_3 does not retain D_3.

Hence both truncated filtered groups have the same degree-1 abelianization and the same degree-2 commutator quotient, with the same induced filtered group law through D_2/D_3. In particular,

\[
\boxed{W_3(G_{F1})\cong W_3(G_{cyc}).}
\]

This gives the first genuine recognition obstruction:

\[
\boxed{r_{T_{cyc}}\ge 4}
\]

for any admissible category containing this pair.

## 4. Why this is stronger than Phase A/B

Phase A/B showed that W_3 recognizes T_cyc on the named D/F1/F2 family union because those families have different quadratic shadows.

This pair has the same W_3 quadratic/commutator data but opposite global target values. Therefore the W_3 carrier is **not** a general recognition mechanism.

The obstruction is exactly the phenomenon sought by the Paper 3 program:

\[
\text{same finite intrinsic low-degree window}
\quad\not\Rightarrow\quad
\text{same global property}.
\]

The first invisible difference is pushed above the W_3 window: F1 moves the q=3 information into the degree-4 commutator [x_1^3,y_1], while the cyclotomic control retains the q=3 Demushkin relation on the x_2,y_2 block.

## 5. Literature verification

The Blumer–Quadrelli source explicitly gives the F1 associated graded restricted Lie algebra as the free product of a rank-2 free Lie algebra and a Demushkin Lie algebra on the remaining 2d-2 generators. This is exactly the structural reason the F1 degree-2 shadow agrees with the free-product control.

Quadrelli's 2024 work states that free pro-p products of Demushkin groups are among the known 1-cyclotomic examples; the same cyclotomic-pair formalism makes the free product with a free pro-p group the relevant control.

These are literature inputs, not claimed new results.

## 6. What remains open

The lower bound r>=4 is closed for the declared pair.

The next question is whether W_4 already separates this pair, or whether the first intrinsic separating carrier occurs later. A direct upper bound must be proved; no threshold equality is claimed here.

The likely candidate mechanism is a filtered extension/p-power datum at the first level retained by W_4, but this must be proved intrinsically. No presentation-local coordinate is allowed.

## 7. Classification

- Same-W_3 target-separating pair: **PASS / CLOSED**.
- Lower bound r_{T_cyc}>=4 on any category containing the pair: **PASS / CLOSED**.
- W_4 separation: **OPEN / LOAD-BEARING**.
- Exact threshold: **OPEN / LOAD-BEARING**.
- General W_3 recognition: **FAIL / CLOSED**.
- General finite-window recognition program: **OPEN / DECISIVE**.

No novelty/priority claim is made from the pair alone.


## 8. Phase-A concrete upper bound: W_4 separates

For the concrete pair (p,d,q)=(3,2,3), W_4 is sufficient.

In the F1 group,
\[
[x_1^3,y_1][x_2,y_2]=1,
\]
and [x_1^3,y_1] lies in D_4. Hence in G_F1/D_4,
\[
[x_2,y_2]=1.
\]

In the cyclotomic control,
\[
x_2^3[x_2,y_2]=1,
\]
so in G_cyc/D_4,
\[
[x_2,y_2]=x_2^{-3}.
\]
The class of x_2^3 in D_3/D_4 is nonzero: the Demushkin associated restricted Lie algebra has the single quadratic relation [X_2,Y_2], and no degree-3 relation kills X_2^{[3]}. Therefore [x_2,y_2] is nonzero in D_3/D_4 for the control.

This is an intrinsic filtered statement: W_4 records whether the commutator class determined by the W_3 quadratic relation survives into the next filtration layer. Consequently
\[
W_4(G_{F1})\not\cong W_4(G_{cyc}).
\]

Combining W_3 equality with W_4 separation gives the exact threshold for this two-object category:
\[
\boxed{r_{T_{cyc}}(\{G_{F1},G_{cyc}\};D_\bullet)=4.}
\]

The uniform q=p^f analogue is strongly suggested by the same degree bookkeeping (W_q equality and a q-power correction at W_{q+1}), but the intrinsic W_{q+1} carrier has not yet been proved uniformly. It remains OPEN rather than being promoted from analogy.
