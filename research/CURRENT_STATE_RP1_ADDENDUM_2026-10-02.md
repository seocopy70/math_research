# CURRENT STATE ADDENDUM — RP-1 — 2026-10-02

This addendum records a load-bearing correction/closure after the latest Gate D counterexample audit.

## Active frontier

The Grassmannian/special-plane carrier is **FAIL / CLOSED**. The restricted-power/extension-defect refinement remains **OPEN / LOAD-BEARING**.

## RP-1 result

For the complete 3-vertex model
G=<s,a,b | asa^{-1}=s^{1+q}, bsb^{-1}=s^{1+q}, [a,b]=1>,
q=p^f, the classes
  \bar s^[q], \bar a^[q], \bar b^[q] in D_q/D_{q+1}
are linearly independent.

The proof uses natural quotient homomorphisms:
- G -> Z_p detecting a^q;
- G -> Z_p detecting b^q;
- G -> C_{p^{f+1}} rt C_p detecting s^q.

Jennings' augmentation-ideal characterization proves the detected q-th power classes are nonzero.

Because L_1 is abelian in this complete model, the restricted q-power map P_q is F_p-linear here. Hence
  P_q^{-1}(im B_q)=F_p \bar s
is now **PASS / LOCAL**, with the previously missing independence lemma supplied.

## Boundary

This does NOT make P_q a general linear map. In non-abelian L_1 the Jacobson cross terms can contribute, so a general restricted-power carrier remains open.

## Current classifications

- Grassmannian carrier: **FAIL / CLOSED**.
- Accidental-plane exclusion: **FAIL / CLOSED**.
- RP-1 complete 3-vertex independence: **PASS / LOCAL**.
- Complete 3-vertex restricted-power preimage: **PASS / LOCAL**.
- General restricted-power/extension-defect carrier: **OPEN / LOAD-BEARING**.
- General categorical no-go: **OPEN / NOT ESTABLISHED**.

## Next authorized gate

RP-2: analyze the intrinsic restricted-power source construction in the previously audited 3-vertex common-sink model, where the ordinary-origin sector has nonzero degree-2 brackets. Then test the smallest non-complete graph.

This is a new gate; the closed Grassmannian carrier must not be reopened.
