## 2026-10-02 — PAPER 4 ARBITRARY-LINEAR-DIRECTION J_q PURITY REFUTED

The exact-depth centralizer jump survives ordinary-edge removal but fails as a pure one-direction incidence detector for arbitrary linear directions.

In the complete three-vertex specially oriented graph
\[
G=\langle s,a,b\mid[a,b]=1,\;sas^{-1}=a^{1+q},\;sbs^{-1}=b^{1+q}\rangle,
\]
the degree-q defect is
\[
B_q(\bar a,\bar s)=\overline{a^q},\quad
B_q(\bar b,\bar s)=\overline{b^q},\quad
B_q(\bar a,\bar b)=0.
\]
For
\(u=\alpha\bar a+\beta\bar b+\gamma\bar s\),
\[
B_q(u,x)
=(\alpha\gamma'-\gamma\alpha')\overline{a^q}
 +(\beta\gamma'-\gamma\beta')\overline{b^q}.
\]
The form has zero radical. Since every degree-one commutator in the complete graph already lies in \(D_q\), \(C_q(u)=L_1\) and \(C_{q+1}(u)=\ker B_q(u,-)\). Hence \(J_q(u)\neq0\) for every nonzero \(u\in L_1\).

In particular
\[
u=\bar s+\bar a\notin O=\operatorname{span}(\bar a,\bar b),
\qquad
B_q(u,\bar a)=\pm\overline{a^q}\neq0,
\]
so \(J_q(u)\neq0\) although \(u\) is not an origin direction. Even the sinkhole direction \(\bar s\) is q-active.

Therefore the load-bearing purity claim
\[
J_q(u)\neq0\Longleftrightarrow u\text{ is a genuine origin direction}
\]
is **FAIL / CLOSED**. This is structural, not an accidental cancellation.

The exact-depth mechanism remains valid for removing ordinary-edge contamination and for the previously established RP-5 pairwise separation. The correct next object must retain target-labelled/pairwise information and an independent anchor such as the restricted-power map \(P_q\), rather than the scalar predicate \(J_q(u)\neq0\).

Detailed audit: research/PAPER4_ARBITRARY_LINEAR_DIRECTION_JQ_AUDIT_2026-10-02.md.

Next authorized action: audit a combined intrinsic carrier such as \((P_q,B_q)\), with fresh Object/Input/Functoriality/Gauge/Orientation-bridge/q-blindness/Separation/Novelty/Stop checks. Do not reopen the false one-direction purity theorem.
