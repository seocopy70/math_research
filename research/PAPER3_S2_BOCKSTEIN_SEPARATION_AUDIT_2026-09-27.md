# PAPER 3 — S2 BOCKSTEIN SEPARATION AUDIT: q=p vs q=p^2

Date: 2026-09-27

## Status
**PASS / CLOSED**

## Setup

For odd prime p,
\[
G_p=\langle x,y\mid x^p[x,y]=1\rangle,
\qquad
G_{p^2}=\langle x,y\mid x^{p^2}[x,y]=1\rangle.
\]
Let
\[
\beta_G:H^1(G,\mathbf F_p)\to H^2(G,\mathbf F_p)
\]
be the Bockstein connecting map for
\[
0\to\mathbf F_p\to\mathbf Z/p^2\to\mathbf F_p\to0.
\]

Fix the dual basis \(\chi_x,\chi_y\) of \(H^1(G,\mathbf F_p)\).

## Direct relator calculation

For the one-relator pro-p presentation, the Bockstein is read from the p-power coefficient in the quadratic initial form of the relator. Equivalently, lift a basis cocycle to a \(\mathbf Z/p^2\)-valued cocycle on the free pro-p group and evaluate its defect on the defining relator.

For
\[
r_q=x^q[x,y],
\]
the commutator contributes zero to the trivial-coefficient lift, while
\[
\chi_x(x^q)=q.
\]
Thus the Bockstein coefficient is
\[
\frac{q}{p}\pmod p.
\]
Also \(\chi_y(x^q)=0\), so \(\beta(\chi_y)=0\).

### q=p

\[
\beta_{G_p}(\chi_x)=\pm u,\qquad
\beta_{G_p}(\chi_y)=0,
\]
where \(u\neq0\) generates
\(H^2(G_p,\mathbf F_p)\cong\mathbf F_p\).

Hence
\[
\operatorname{rank}\beta_{G_p}=1,
\qquad
\operatorname{Im}\beta_{G_p}=H^2(G_p,\mathbf F_p)\neq0.
\]

### q=p^2

Now
\[
\frac{p^2}{p}=p\equiv0\pmod p,
\]
so
\[
\beta_{G_{p^2}}(\chi_x)=0,
\qquad
\beta_{G_{p^2}}(\chi_y)=0.
\]
Therefore
\[
\beta_{G_{p^2}}=0,
\qquad
\operatorname{Im}\beta_{G_{p^2}}=0.
\]

## Independent literature check

The standard one-relator/Demuškin formula identifies the Bockstein values with the coefficients of the p-power terms in the quadratic initial form of the relator. The checked source explicitly attributes this to NSW, Propositions 3.9.13–3.9.14 and Labute, §2, Proposition 3. This independently agrees with the direct relator-lift calculation.

## Requested distinctions

1. **Whole map:** the two maps are not isomorphic as linear maps, because their ranks are 1 and 0.

2. **Image only:** the images are different: one is one-dimensional and the other is zero.

Thus both S2 tests **PASS / CLOSED**.

## Consequence with S1

The preceding S1 result gives
\[
W_p(G_p)\cong W_p(G_{p^2}).
\]
Therefore, for any category \(\mathcal C\) containing this pair and the current Zassenhaus-window convention,
\[
\boxed{r_{T_\beta}(\mathcal C;D_\bullet)\ge p+1}.
\]

This is a lower bound only. It does **not** prove
\(r_{T_\beta}=p+1\).

## Logical boundary

This pair still does not establish a factorization-vs-recognition separation \(f_T\neq r_T\), because the factorization threshold must be defined for the same target \(T_\beta\). It establishes a concrete recognition lower bound for the Bockstein target.

## Classification

- Bockstein full-map difference: **PASS / CLOSED**
- Bockstein image difference: **PASS / CLOSED**
- recognition lower bound \(r_{T_\beta}\ge p+1\): **PASS / LOCAL**
- exact equality \(r_{T_\beta}=p+1\): **OPEN**
- same-target factorization-vs-recognition separation: **OPEN / LOAD-BEARING**

Next Gate: test an upper bound at \(p+1\), while keeping same-target factorization logically separate.

## Sources

- Labute, *Classification of Demushkin groups* (1967), §2, Proposition 3.
- NSW, Propositions 3.9.13–3.9.14 (formula independently checked in a secondary exposition).
