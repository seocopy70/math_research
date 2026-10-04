# Paper 4 — TeX Audit Ledger — 2026-10-04

## Manuscript branch

- Branch: `paper4-tex-2026-10-04`
- Manuscript: `paper4/main.tex`
- Purpose: convert the certified Paper 4 state into a coherent manuscript without reopening closed research branches.

## Source reconciliation

### Certified and included

1. **Lower-window blindness**
   [
   W_n(G_{s,r})cong F/(D_n(F),r),qquad nle p^s.
   ]
   Status: CLOSED.

2. **Critical relative threshold**
   [
   n_{mathrm{sep}}^{mathrm{rel}}(s)=p^s+1
   ]
   for the declared odd-(p) stress family, including the independently closed (a=1) boundary.
   Status: CLOSED.

3. **Direct same-window unmarked separation**
   For (1le a<s<t),
   [
   |W_{p^s+1}(G_{s,a})|
   =p|W_{p^s+1}(G_{t,a})|.
   ]
   Hence
   [
   n_{mathrm{sep}}(s)=p^s+1
   ]
   in this declared nonboundary range.
   Status: CLOSED.

4. **Ordinary mod-(p) cohomology blindness**
   The full graded ring (H^ullet(G_{s,a},mathbf F_p)) is independent of (s,a) in the declared family, by the audited quadratic one-relator theorem.
   Status: CLOSED.

5. **Remaining critical boundary**
   [
   W_{p^s+1}(G_{s,s})stackrel{?}{cong}
   W_{p^s+1}(G_{s,infty})
   ]
   remains OPEN for (sge2); ((p,s)=(3,1)) is CLOSED.
   Status: OPEN / LOAD-BEARING.

6. **Arbitrary-relation degree-only upgrade**
   Not claimed. The degree-only generalization is closed as a target; a broader theorem would require additional filtered/lift hypotheses.
   Status: FAIL / CLOSED as a degree-only target.

## Explicit exclusions

The manuscript does not promote:

- the superseded old universal same-window claim;
- unresolved (a=s) versus (a=infty), (sge2), to a theorem;
- universal (E_psi) to a theorem;
- Paper 3 validation material to a Paper 4 proof;
- exploratory carrier-hunting records to mathematical results.

## Literature check

The cohomology closure cites Quadrelli, *Two families of pro-(p) groups that are not absolute Galois groups*, J. Group Theory 25 (2022), 25--62, arXiv:2011.03233v3. The audited result used is Proposition 2.1 in the arXiv version.

The Zassenhaus/Jennings--Lazard formula used in the finite-witness arguments is standard and independently confirmed in modern literature.

## Build gate

A dedicated GitHub Actions workflow `.github/workflows/paper4-tex-build.yml` compiles `paper4/main.tex`, runs `pdfinfo`, computes SHA-256, and uploads the PDF audit artifact.

**FINAL is prohibited until the build succeeds and the PDF artifact/hash are inspected.**


_Last branch audit update._
