# Paper 5 — Aut(W_n) structure: IA kernel / GL(V) image pre-check
Date: 2026-10-04

## Scope

Paper 5 is redefined away from the previous compression formalism. The active object is the concrete finite-group automorphism structure of the critical windows:
\[
1\to IA(W_n)\to \operatorname{Aut}(W_n)\to \operatorname{Im}(\operatorname{Aut}(W_n)\to GL(W_n/\Phi(W_n)))\to1.
\]
The secondary comparison is the induced action on the relevant quotient/target \(\operatorname{Aut}(W_n)\to\operatorname{Aut}(Q_n)\).

## Evidence currently supplied

User-reported completed calculations:
- \(p=3,n=4\): split \(a=1\): \(2^2 3^{30}\); non-split \((s=1,a=1)\): \(2\,3^{28}\); split \(a=2\): \(2^5 3^{30}\); non-split \((s=1,a=2)\): \(2^4 3^{28}\).
- \(p=5,n=6\): split \(a=1\): \(2^4 5^{109}\); non-split \((s=1,a=1)\): \(2^2 5^{107}\); split \(a=2\): \(2^7\,3\,5^{109}\); non-split \((s=1,a=2)\): \(2^5\,3\,5^{107}\).
- \(p=3,n=4\): reported admissible-kernel counts/orbits: 81 in one split orbit; 9 in one \((1,2)\) non-split orbit; 72 in the \((1,1)\) non-split family, split into orbit sizes 9,9,54.

These are **USER-REPORTED / NOT YET REPRODUCED FROM THE CURRENT REPOSITORY**. They are not theorem-level evidence until scripts/logs and an independent rerun are in the repository.

## Pre-check

- **Object:** PASS — concrete finite \(\operatorname{Aut}(W_n)\), IA kernel, linear image on \(V=W_n/\Phi(W_n)\), and quotient-action image.
- **Input:** PASS — \(W_n\) and its finite-group data; no hidden q is inserted into the automorphism computation.
- **Functoriality:** PASS in principle — automorphisms induce the canonical action on \(V\); the exact quotient-action map must be fixed before use.
- **Gauge:** PASS — IA is precisely the kernel of the abelianized action, so presentation-coordinate changes are absorbed by the intrinsic automorphism action.
- **Orientation bridge:** NOT REQUIRED — this branch is a concrete automorphism-group theorem, not orientation recovery.
- **q-blindness:** PASS — the object is \(W_n\); \(s,a\) are comparison labels, not inputs to the intrinsic automorphism computation.
- **Separation:** PASS / LOCAL numerically if the reported orders reproduce; the p-primary ratio is \(p^2\) for both \(p=3,5\).
- **Novelty:** OPEN — total automorphism orders alone are not yet a structural theorem.
- **Stop:** do not promote the \(p^2\) pattern until its source is identified.

## Authorized next computation: IA / GL decomposition

For every \(p=3,n=4\) case compute:
1. \(V=W/\Phi(W)\) and \(|GL(V)|\);
2. \(L=\operatorname{Im}(\operatorname{Aut}(W)\to GL(V))\);
3. \(|IA(W)|=|\ker(\operatorname{Aut}(W)\to GL(V))|\);
4. p-primary valuations of \(|IA(W)|\), \(|L|\), and \(|\operatorname{Aut}(W)|\);
5. for a fixed admissible quotient, the image in \(\operatorname{Aut}(Q)\);
6. the kernel of \(\operatorname{Aut}(W)\to\operatorname{Aut}(Q)\);
7. exactly where the \(p^2\) deficit occurs.

The decisive output is the factorization
\[
|\operatorname{Aut}(W)|=|IA(W)|\,|L(W)|
\]
together with the quotient-action image/kernel, not another total-order computation.

## Secondary test

Only after the \(p=3,n=4\) decomposition is independently closed, repeat the same structural measurement at \(p=5,n=6\). Do not enumerate all admissible kernels at p=5.

## Candidate theorem

**IA-defect theorem (candidate).** In the tested split/non-split family, the non-split automorphism group differs by an explicitly identified \(p^2\)-loss in a functorially defined automorphism layer (IA kernel or quotient-action kernel), with the same mechanism for \(p=3,5\).

Status: **OPEN** until the layer is identified and independently verified.

## Explicit non-claims

Orbit multiplicity is not itself a no-go. The \(p^2\) factor is not yet a theorem. This branch does not revive the discarded compression/trichotomy formalism, does not use the unresolved Paper 4 orientation bridge, and does not start with the large \((3,2,1,10)\) model.

## Classification

- Aut-order certificates: **PASS / LOCAL** based on user-supplied computation; repository reproduction pending.
- IA/GL decomposition: **OPEN / ACTIVE**.
- p^2 source theorem: **OPEN / LOAD-BEARING**.
- orientation-recovery dichotomy: **DEFERRED / HIGH-RISK** until the concrete automorphism theorem is obtained.
