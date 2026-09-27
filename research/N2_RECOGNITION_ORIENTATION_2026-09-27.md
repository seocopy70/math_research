# N2 PRE-CHECK — RECOGNITION OF \(\chi\bmod p^k\) ON THE STANDARD DEMUŠKIN FAMILY
## 2026-09-27

## Status

- N2 definition/pre-check: **PASS / CLOSED**
- Lower-bound mechanism at depth \(p^{k-1}\): **PASS / LOCAL**
- Upper bound at depth \(p^{k-1}+1\): **OPEN**
- Equality
  \[
  r_{\chi\bmod p^k}=p^{k-1}+1
  \]
  : **OPEN**
- No computation beyond the established finite-quotient/q-collapse results is claimed.

This document fixes the admissible class before any new computation.

---

## 1. Correct nontrivial admissible class

A class consisting of a single fixed rank-four \(q=3\) Demuškin group is unsuitable for the recognition-threshold problem: its target value is already fixed up to isomorphism. The threshold would therefore be degenerate.

The first meaningful class is the standard odd-\(p\) Demuškin family
\[
G_{f,d}
=
\left\langle x_1,\ldots,x_d\mid
x_1^{p^f}[x_1,x_2][x_3,x_4]\cdots=1
\right\rangle,
\]
with \(d\ge2\) even and the usual \(f\)-parameter, together with the power-free limiting member \(G_{\infty,d}\).

The canonical orientation satisfies, in the standard presentation,
\[
\chi_{G_{f,d}}(x_1)=1,\qquad
\chi_{G_{f,d}}(x_2)=(1-p^f)^{-1},
\]
and is trivial on the remaining displayed generators. This formula is used here only as a known description of the target, not as part of the finite-window input.

The class must be interpreted as an admissible class of groups, not as a collection of marked presentations.

---

## 2. N2 input and target

Filtration:
\[
D_\bullet=P_\bullet=\text{Zassenhaus filtration}.
\]

Finite window:
\[
W_n(G)=
\bigl(G/P_n(G),P_1/P_n,\ldots,P_{n-1}/P_n\bigr).
\]

Target:
\[
T_k(G)=\chi_G\bmod p^k,
\]
under isomorphism of oriented groups:
\[
(G,T_k(G))\cong(H,T_k(H))
\]
means that some group isomorphism \(G\to H\) intertwines the two characters.

The target is therefore not merely the abstract residue value of one coordinate.

---

## 3. Required lower bound

To prove
\[
r_{T_k}\ge p^{k-1}+1,
\]
it is enough to exhibit, for every \(k\ge2\), two admissible groups \(G,H\) such that
\[
W_{p^{k-1}}(G)\cong W_{p^{k-1}}(H)
\]
but
\[
(G,T_k(G))\not\cong(H,T_k(H)).
\]

The established q-collapse information supplies the natural candidate:
\[
G=G_{k-1,d},\qquad H=G_{\infty,d}.
\]

At depth
\[
N=p^{k-1},
\]
the existing Zassenhaus comparison gives
\[
G_{k-1,d}/P_N\cong G_{\infty,d}/P_N.
\]

On the other hand,
\[
\chi_{G_{k-1,d}}(x_2)
=(1-p^{k-1})^{-1}
\not\equiv1
=\chi_{G_{\infty,d}}(x_2)
\pmod{p^k}.
\]

Thus the targets are distinct at level \(p^k\).

This yields the lower-bound conclusion
\[
\boxed{
r_{\chi\bmod p^k}\ge p^{k-1}+1
}
\]
for the standard family, provided the quoted finite-quotient comparison is stated with the exact filtered-window structure rather than only as an unfiltered group isomorphism.

Classification of this lower-bound route:
**PASS / LOCAL** pending a self-contained verification of the precise filtered isomorphism statement.

---

## 4. Why the upper bound is genuinely separate

The already proved affine result gives
\[
f_{\mathrm{aff}}(k)=p^{k-1}+1.
\]

The finite Kummer selector theorem gives an intrinsic selector on the corrected finite quotient for the fixed \(q=3\) group, but it does not by itself establish recognition on the whole varying-\(f\) family.

Therefore the implication
\[
f_{\mathrm{aff}}(k)=p^{k-1}+1
\quad\Longrightarrow\quad
r_{\chi\bmod p^k}=p^{k-1}+1
\]
is not currently justified.

In particular, the upper-bound problem is:

> Does the abstract filtered window \(W_{p^{k-1}+1}(G)\) determine the isomorphism class of the canonically oriented group \((G,\chi\bmod p^k)\) throughout the declared standard Demuškin family, without supplying \(q\) or a presentation?

This is the actual load-bearing N2 question.

---

## 5. Two possible upper-bound routes

### Route A — Classification through the finite window

Show that the window determines the relevant \(f\)-class up to the threshold:
- for \(f<k\), recover \(f\) from an intrinsic torsion feature of the finite abelianization;
- for \(f\ge k\), show that all corresponding targets \(\chi\bmod p^k\) coincide.

Then combine this with the known classification/orientation formula.

This route is mathematically legitimate for recognition, but its novelty must be treated cautiously because it may amount to a classification-based reconstruction rather than a new finite selector.

### Route B — Intrinsic finite selector

Construct a natural predicate on the bare filtered quotient
\[
W_{p^{k-1}+1}(G)
\]
whose unique solution is \(T_k(G)\) across the whole varying-\(f\) class.

This is structurally stronger and closer to the project's original finite-window recognition program.

No claim is made yet that Route B is necessary for the numerical recognition threshold.

---

## 6. Critical logical distinction

There are now three different claims that must not be conflated:

1. **Factorization**
   \[
   \mathcal O_k(G)
   \text{ factors through }G/P_{p^{k-1}+1}.
   \]

2. **Recognition**
   \[
   W_{p^{k-1}+1}(G)\cong W_{p^{k-1}+1}(H)
   \Longrightarrow
   (G,\chi_G\bmod p^k)\cong(H,\chi_H\bmod p^k).
   \]

3. **Intrinsic selector**
   There is a functorial rule on the bare finite window that actually produces the target.

Paper 2 establishes (1) for the affine observation and sharpness in its declared representation category.

The new N2 problem is (2).

Claim (3) is stronger and should not be silently substituted for (2).

---

## 7. Current Gate classification

\[
\boxed{
\text{N2 lower bound: PASS / LOCAL}
}
\]

The established q-collapse comparison supplies the correct sharpness candidate
\[
G_{k-1,d}\quad\text{vs.}\quad G_{\infty,d}.
\]

\[
\boxed{
\text{N2 upper bound: OPEN}
}
\]

The existing fixed-\(q=3\) finite selector cannot simply be promoted to a varying-\(f\) recognition theorem.

Therefore the equality
\[
\boxed{
r_{\chi\bmod p^k}=p^{k-1}+1
}
\]
remains **OPEN**.

The next authorized step is not another affine cocycle computation. It is an independent verification of the finite-window separation pair and then a precise test of Route A before attempting the stronger Route B.

No closed Fox/\(t_2\) route is reopened.
