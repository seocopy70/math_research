# KUMMER TOP-COHOMOLOGY HARD ATTACK 26 — QUOTIENT FACTORIZATION OBSTRUCTION — 2026-09-20

## Active gate
Test whether, for fixed k, the twisted top obstruction S_k(G,rho)=|H^2(G,A_k(rho))| can be reconstructed functorially from Q_k=G/P_{k+1}(G) together with rho:Q_k->U_k.

## Attack
Let A=A_k(rho), where P_{k+1}(G) acts trivially because rho factors through Q_k. Put N=P_{k+1}(G), Q=G/N.

The Hochschild–Serre five-term sequence gives

0 -> H^1(Q,A) -> H^1(G,A) -> H^1(N,A)^Q -> H^2(Q,A) -> H^2(G,A) -> H^1(Q,H^1(N,A)).

Therefore H^2(G,A) is not, in general, a functor of the abstract quotient Q and the coefficient action rho alone. The map H^2(Q,A)->H^2(G,A) depends on the extension 1 -> N -> G -> Q -> 1 and the transgression/extension data involving N.

The earlier factorization result P_{k+1}(A_k⋊U_k)=1 proves only that candidate coefficient actions and crossed derivations factor through Q. It does not imply that top-degree cohomology of G factors through Q.

## Stronger structural diagnosis
The missing information is not another value of rho. It is the extension class of the discarded deep kernel N=P_{k+1}.

Two finite-data possibilities remain:
(A) Q-only carrier: J_k(G)=J(Q_k).
(B) Q plus finite extension-obstruction carrier: J_k(G)=(Q_k,E_k), where E_k records exactly the transgression/2-cell/extension datum needed to recover the top obstruction.

The second possibility is more promising because the standard one-relator calculation shows that the orientation selector is itself a relation obstruction. This suggests that the correct finite carrier may be a finite presentation-extension object rather than the bare quotient group.

## Standard-family consequence
For the standard family G_q, Q_k often distinguishes the relevant q 3-adic class at exactly the P_{k+1} threshold. Therefore a Q-only selector can exist on this family simply by classification recovery from Q_k. That does not establish the desired non-tautological universal carrier.

Failure of abstract Q-only determination for arbitrary pro-3 groups would not kill the Kummer mechanism; it would only force the carrier category to retain a finite extension/2-cell datum.

## Result classification
- P_{k+1}(A_k⋊U_k)=1: PASS / LOCAL (previous result).
- Candidate rho and Z^1 factor through Q_k: PASS / LOCAL.
- H^2(G,A_k(rho)) automatically factors through Q_k: FAIL / CLOSED as an inference.
- Q-only intrinsic Kummer selector: OPEN; no theorem yet proves impossibility within the restricted Demushkin category.
- Extension-obstruction enriched carrier (Q_k,E_k): OPEN / newly identified mechanism.
- No numerical scan authorized.

## Exact next theorem
Construct an intrinsic finite extension/2-cell object E_k attached to Q_k that: (1) is q-blind and presentation/gauge independent; (2) is determined by the declared filtered input; (3) reproduces the one-relator twisted obstruction; (4) yields the unique rho=chi mod 3^k; and (5) is no larger than necessary relative to the admissible carrier category.

The likely mathematical form is a finite transgression/extension class or a finite relation module attached to the P_{k+1}-extension.

This is the next Discovery→Attack target.