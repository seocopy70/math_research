# PAPER 3 — PHASE B: D/F1/F2 FINITE-WINDOW RECOGNITION

Date: 2026-10-01
Status: **PASS / CLOSED at the declared three-family category; novelty remains OPEN / CONDITIONAL**

## Result

Extend the Phase-A category to
\[
C_{p,d,q}=\{D_{d,q},F1_{d,q},F2_{d,q}\},
\]
where F2 is the Blumer–Quadrelli two-relator variation obtained from the Demushkin relator by adjoining a commutator [z_1,z_2] between two distinct unpaired generators.

For odd p, d>=2, q=p^f:

- W_2 is the same abelianization window for all three families.
- D has one-dimensional quadratic relation space, represented by
  \[
  R_D^{(2)}=\sum_{i=1}^d[X_i,Y_i].
  \]
- F1 has one-dimensional quadratic relation space
  \[
  R_{F1}^{(2)}=\sum_{i=2}^d[X_i,Y_i],
  \]
  because [x_1^q,y_1] begins in degree q+1>=3.
- F2 has the quadratic relation space
  \[
  \langle R_D^{(2)},[Z_1,Z_2]\rangle,
  \]
  of dimension 2; the extra commutator is independent because the chosen pair is not one of the Demushkin symplectic pairs.

Thus W_3 distinguishes the three family types intrinsically:
- D: quadratic/cup relation space dimension 1 and nondegenerate rank 2d;
- F1: dimension 1 but rank 2d-2;
- F2: dimension 2.

Since W_2 does not distinguish the families, the exact recognition threshold for the declared three-family category is
\[
\boxed{r_{T_{\rm cyc}}(C_{p,d,q};D_\bullet)=3.}
\]

At (p,d,q)=(3,2,3), the same conclusion holds exactly.

## Logical boundary

This extends the finite carrier from D/F1 to F2, but it does not make the result substantially deeper: all three distinctions are already visible in the quadratic relation/cup structure. The mechanism therefore remains a derived structural reformulation rather than a demonstrated new global obstruction.

## Classification

- Phase B D/F1/F2 recognition: **PASS / CLOSED**.
- Uniform odd-p,d,q statement: **PASS / CLOSED**.
- New-paper novelty from D/F1/F2 alone: **OPEN / CONDITIONAL; weak**.
- Reusable W_3 carrier: **PASS / LOCAL** — reusable across these three families, but not yet shown to recognize 1-cyclotomicity on a broader class.

Next authorized target: do not keep adding families merely because W_3 separates their presentations. Search for a cyclotomic/non-cyclotomic pair with the same W_3 quadratic/cup data, or equivalently determine whether the W_3 carrier can fail to see 1-cyclotomicity. A genuine same-window/different-target pair is the decisive next test.
