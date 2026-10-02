# RESEARCH LOG ADDENDUM — 2026-10-02 — RP-1

## Restricted-power independence lemma closed locally

The missing lemma in the complete 3-vertex Grassmannian counterexample has been proved.

For G=<s,a,b | asa^{-1}=s^{1+q}, bsb^{-1}=s^{1+q}, [a,b]=1>, q=p^f, the classes s^[q], a^[q], b^[q] are linearly independent in D_q/D_{q+1}.

Coefficient detection:
- kill s,b and map a to Z_p;
- kill s,a and map b to Z_p;
- map s to u, a to t, b to 1 in C_{p^{f+1}} rt C_p with t u t^{-1}=u^{1+q}.

Jennings' theorem and u^q-1=(u-1)^q show the s^q class is nonzero in degree q.

Because L_1 is abelian in this complete model, P_q is F_p-linear here. Therefore P_q^{-1}(im B_q)=F_p s.

Classification:
- RP-1 independence: **PASS / LOCAL**.
- Complete 3-vertex preimage identity: **PASS / LOCAL**.
- General P_q carrier: **OPEN / LOAD-BEARING**.
- Blanket linearity of P_q: **FAIL / CLOSED**.

The result is independently supported by the standard Zassenhaus/restricted-Lie facts: the Zassenhaus associated graded is a restricted Lie algebra, while the restricted p-operation is only additive when the relevant bracket cross-terms vanish. citeturn0search1turn0search2

Next authorized action: RP-2 in the 3-vertex common-sink model, with special attention to the nonlinear/additive obstruction and to an intrinsic replacement for P_q rather than assuming global linearity.
