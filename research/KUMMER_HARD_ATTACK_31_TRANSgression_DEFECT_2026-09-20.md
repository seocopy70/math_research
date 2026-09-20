# HARD ATTACK 31 — NAIVE TRANSgression DEFECT IS TOO SHALLOW

## 2026-09-20

### Candidate attacked
For
\[
N=P_{k+1}(G),\quad Q=G/N,\quad M=N/(N^{3^k}[N,N]),
\]
and a candidate \(\rho:Q\to U_k\), the first concrete derived candidate was
\[
C_\rho:
\operatorname{Hom}_Q(M,A_k(\rho))
\xrightarrow{\delta_{e,\rho}}
H^2(Q,A_k(\rho)).
\]
The tempting selector is the basis-free cokernel/Fitting defect
\(D_\rho=\operatorname{coker}\delta_{e,\rho}\).

### Exact spectral-sequence identity
The Lyndon–Hochschild–Serre five-term/edge sequence gives
\[
H^2(Q,A)\xrightarrow{\inf}H^2(G,A),
\qquad
\operatorname{im}(\delta_{e,\rho})=\ker(\inf),
\]
so
\[
\operatorname{coker}\delta_{e,\rho}\cong\operatorname{im}\bigl(H^2(Q,A)\to H^2(G,A)\bigr).
\]
Thus the proposed Fitting defect is not an independent secondary invariant: it is precisely the part of \(H^2(G,A)\) represented by quotient inflation.

### Hard attack on the canonical PD^2 case
For the canonical orientation coefficient \(A=A_k(\chi)\), \(G\) is PD^2 and \(N\) is open, hence also PD^2 with the restricted orientation. The canonical top class restricts nontrivially to the top class of \(N\). Any inflated class from \(Q\) restricts trivially to \(N\). Therefore the inflation image in \(H^2(G,A_k(\chi))\) is zero. This is the standard edge-filtration distinction: the canonical fundamental class lies in the \(q=2\) row, whereas quotient-inflated classes lie in the \(q=0\) row.

For noncanonical \(\rho\), twisted PD^2 duality gives the corresponding top-degree obstruction vanishing rather than a new quotient-inflation class. Hence nonzero \(\operatorname{coker}\delta\) cannot serve as the canonical selector.

### Important precision
The argument closes the specific selector
\[
\operatorname{coker}\delta\ne0
\]
and any Fitting/annihilator invariant depending only on that cokernel. It does NOT yet prove that every possible basis-free invariant of the entire two-term complex \(C_\rho\) is useless. In particular \(\ker\delta\) and more elaborate derived combinations remain logically distinct and must be attacked separately.

### Structural consequence
The naive finite transgression complex sees the \(q=0\) quotient-inflation row. The desired PD^2 orientation sits in the complementary \(q=2\) top row. To bridge them, a secondary operation must cross the spectral-sequence filtration without inserting \(H^2(N,A)\) itself. This sharply identifies the missing mechanism.

### Status
- \(\operatorname{coker}\delta\) nonvanishing selector: **FAIL / CLOSED**.
- Fitting/annihilator of \(\operatorname{coker}\delta\): **FAIL / CLOSED** as a new orientation carrier.
- Entire two-term complex \(C_\rho\): **OPEN**, but only if a genuinely new derived invariant beyond its ordinary kernel/cokernel is specified.
- Universal orientation reconstruction: **OPEN**.

No numerical scan authorized until the next invariant is explicitly defined.
