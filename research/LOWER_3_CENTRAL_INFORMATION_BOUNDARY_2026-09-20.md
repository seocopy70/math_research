# Lower 3-central information boundary — 2026-09-20

## Purpose

This note records the first-stage comparison between the Zassenhaus filtration and the lower 3-central series for the standard rank-four family
\[
G_{3^s}=\langle x_1,x_2,x_3,x_4\mid x_1^{3^s}[x_1,x_2][x_3,x_4]=1\rangle
\]
and the power-free control
\[
G_\infty=\langle x_1,x_2,x_3,x_4\mid [x_1,x_2][x_3,x_4]=1\rangle.
\]

The result is an information-boundary statement at the level of isomorphism classes of finite quotients. It is not a pointed naturality theorem and does not by itself prove that the lower 3-central quotient is an intrinsic orientation carrier.

## 1. Zassenhaus threshold

For the free pro-3 group F, let
\[
D_N(F)=\prod_{i3^j\ge N}\gamma_i(F)^{3^j}.
\]
Since \(x_1^{3^s}\in D_{3^s}(F)\), for \(N\le3^s\) the defining relation reduces modulo \(D_N(F)\) to the power-free relation. Functoriality of the Zassenhaus filtration gives
\[
G_{3^s}/D_N\cong G_\infty/D_N\qquad(N\le3^s).
\]

At \(N=3^s+1\), after abelianization,
\[
(G_{3^s}/D_N)^{ab}\cong \mathbf Z/3^s\times(\mathbf Z/3^{s+1})^3,
\]
whereas
\[
(G_\infty/D_N)^{ab}\cong(\mathbf Z/3^{s+1})^4.
\]
Hence the finite quotients are not isomorphic. Thus, within this standard family,
\[
G_{3^s}/D_N\cong G_\infty/D_N\iff N\le3^s.
\]

## 2. Lower 3-central threshold

Define
\[
P_1=G,\qquad P_{n+1}=P_n^3[P_n,G].
\]
Using the standard product formula
\[
P_n=\prod_{i+j\ge n}\gamma_i(G)^{3^j},
\]
the power term has weight
\[
\operatorname{wt}_P(x_1^{3^s})=s+1.
\]
Therefore, for \(n\le s+1\),
\[
x_1^{3^s}\in P_n(F),
\]
so
\[
G_{3^s}/P_n\cong G_\infty/P_n.
\]

At \(n=s+2\), abelianization gives
\[
(G_{3^s}/P_{s+2})^{ab}
\cong
\mathbf Z/3^s\times(\mathbf Z/3^{s+1})^3,
\]
while
\[
(G_\infty/P_{s+2})^{ab}
\cong
(\mathbf Z/3^{s+1})^4.
\]
Hence
\[
G_{3^s}/P_n\cong G_\infty/P_n
\iff n\le s+1.
\]

The same sharpness mechanism is visible in the rank-two analogue
\[
H_q=\langle x,y\mid x^q[x,y]\rangle.
\]

## 3. Comparison

\[
\begin{array}{c|c|c}
\text{filtration}&\text{weight of }x_1^{3^s}&\text{first separating level}\\
\hline
D_\bullet&3^s&3^s+1\\
P_\bullet&s+1&s+2
\end{array}
\]

Thus the q-information threshold is exponential in the Zassenhaus index but linear in the lower 3-central index.

For the standard family, using the known orientation formula
\[
\chi_{3^s}(x_2)=(1-3^s)^{-1},
\]
the mod \(3^k\) character distinguishes only the layers \(s<k\). Consequently the quotient information boundary is
\[
D_{3^{k-1}+1}\quad\text{versus}\quad P_{k+1}.
\]
In particular, mod 27 gives \(D_{10}\) versus \(P_4\).

## 4. Logical boundary

The theorem is deliberately local to the standard Demuškin family and depends on the classification/orientation formula for the statement about \(\chi\). It proves a finite-quotient information boundary, not a pointed naturality theorem.

It does not yet prove
\[
\chi\bmod3^k\text{ is intrinsically recoverable from }G/P_{k+1}
\]
by a q-blind Kummer recognition predicate. That is the next substantive step.

## Status

- Zassenhaus threshold: PASS / LOCAL.
- Lower 3-central threshold: PASS / LOCAL, subject to the standard product formula for \(P_n\).
- Sharpness by abelianization: PASS / LOCAL.
- Rank-two sanity check: PASS / LOCAL.
- Linear information boundary for \(\chi\bmod3^k\): PASS / LOCAL, standard-family/classification dependent.
- Intrinsic finite Kummer recognition on \(G/P_{k+1}\): OPEN.
