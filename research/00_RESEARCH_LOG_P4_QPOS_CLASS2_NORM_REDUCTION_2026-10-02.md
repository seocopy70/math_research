# Paper 4 — q>0 Class-2 Norm-Action Reduction
## 2026-10-02

### Active gate
\(P4\)-Q+ / STRICT-NONABELIAN-COMPRESSION remains **OPEN / LOAD-BEARING**.

### Evidence
The first strict-compression candidate is
\[
C_n^{(2)}(E_n):1\to K_n/\gamma_3(K_n)\to W_n/\gamma_3(K_n)\to D/D_n(D)\to1.
\]
The closed untwisted H1/E2 layer sees the stress relation \(z^{p^s}=r_D\) only through the coinvariant class, hence only through \(p^s\bmod p^a\); it saturates for \(s\ge a\).

At class 2, however, the retained \(D/D_n(D)\)-action gives the norm operator
\[
N_{p^s}(T_x)=1+T_x+\cdots+T_x^{p^s-1}
\]
on-coinvariantly. The relation implies the class-2 defect identity
\[
N_{p^s}(T_x)c_x(\bar z)=[r_D,x]
\]
in the appropriate kernel layer. Passing to coinvariants sends \(T_x\mapsto1\), recovering \(N_{p^s}\mapsto p^s\) and hence the already-closed H1 saturation. Therefore the H1/E2 no-go does not factor the class-2 candidate.

### Classification
- class-2 candidate A1-A5/A8: **PASS / LOCAL**;
- non-coinvariant norm-action datum: **PASS / LOCAL** as the first surviving nonabelian datum;
- factor-through H1/E2/ordinary graded: **OPEN** (not implied by prior closures);
- T1 threshold separation: **OPEN / LOAD-BEARING**;
- A6 strictness: **OPEN**;
- A7 non-reencoding: **OPEN**.

### Next authorized action
For fixed external \(m>a\), choose the first depth \(n(m)\) that contains the \(p^m\)-layer and compute only the finite orbit/invariant of
\[
(A_n,B_n,\beta_n,\rho_n,\text{class-2 power map})
\]
needed to test whether \(N_{p^s}(\rho_n(x))\) distinguishes \(a<s<m\) from \(s\ge m\). No raw scalar Magnus/Fox coefficient search is authorized.

### Stop condition
If the norm-action invariant is gauge-equivalent for all \(s>a\) at the threshold depth, classify the class-2 candidate **FAIL / CLOSED** for T1. If it separates, independently prove A6/A7 before promotion.
