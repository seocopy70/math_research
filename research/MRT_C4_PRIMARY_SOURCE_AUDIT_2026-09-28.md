# MRT c4 PRIMARY-SOURCE AUDIT — 2026-09-28

## Question

For the current Gate D2 hand calculation, determine whether Mináč–Rogelstad–Nguyễn Duy Tân explicitly give a formula for
\[
c_4(G)=\dim_{\mathbf F_p}P_4/P_5
\]
for Demuškin pro-p groups, rather than extrapolating the known c_3 formula.

## Primary-source check

Source:
J. Mináč, M. Rogelstad, N. D. Tân, *Dimensions of Zassenhaus filtration subquotients of some pro-p-groups*, arXiv:1405.6980v3 / Israel J. Math. 212 (2016), 825–855.

The paper's Section 5, Example 5.3 explicitly lists:
\[
c_4(G)=
\begin{cases}
\dfrac{d^4-5d^2+4}{4},&p\ne2,\\
\dfrac{d^4-3d^2+2d}{4},&p=2.
\end{cases}
\]

Thus for the present case p=3, d=4,
\[
c_4=\frac{4^4-5\cdot4^2+4}{4}
=\frac{256-80+4}{4}
=45.
\]

Hence
\[
\boxed{\dim_{\mathbf F_3}P_4/P_5=45.}
\]

## Important distinction

The earlier c_3 result
\[
c_3=\frac{d^3-d}{3}=20
\]
and the present c_4 result are independently stated by the source. No unverified k -> k+1 extrapolation is being used.

The primary-source page also gives the general Proposition 5.2 mechanism:
if n=p^k m with (m,p)=1, then
\[
c_n=w_m+w_{pm}+\cdots+w_{p^k m},
\]
with Example 5.3 spelling out c_1 through c_5.

## Consequence for the D2 hand calculation

For the exact extension
\[
1\to P_4/P_5\to W_5\to W_4\to1
\]
in the p=3, d=4, k=2 test, the fiber layer has dimension 45 over F_3.

This is only the dimension. It does NOT determine the W_5-module structure, the fixed-point space
\[
H^1(P_4/P_5,\mathbf F_3)^{W_5},
\]
the transgression image in H^2(W_4,F_3), or the intersection with the delta-family. Those remain the actual load-bearing calculations.

## Classification

- MRT primary-source existence of an explicit c_4 formula: **PASS / CLOSED**.
- c_4(p=3,d=4)=45: **PASS / CLOSED**.
- W_5 -> W_4 kernel layer P_4/P_5 dimension =45: **PASS / LOCAL**.
- W_5-action / fixed points / transgression / delta-family separation: **OPEN / LOAD-BEARING**.

## Source

MRT arXiv:1405.6980v3, Section 5, Example 5.3.
