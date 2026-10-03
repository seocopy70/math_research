# PAPER 4 — T1-C a=1 NEXT-ACTION NOTE — 2026-10-03

## Evidence

Latest GAP calculations for the rank-two p=3,d=2 stress family give repeated finite-window nonsplitting at the unresolved boundary a=1, including (s,a,n)=(1,1,4) and (2,1,10), with additional s=3 computation beginning.

These are PASS / LOCAL computational evidence only. They do not by themselves prove the general a=1 case.

## Why the old witness cannot be reused

The previous metabelian witness uses r=floor(s/a) and (y-1)^r z=p^r z in C_{p^s}. At a=1, r=s, so p^r z=p^s z=0. Thus that witness has a genuine boundary failure.

## Authorized next object

Construct an independent finite quotient/pushout for a=1 and compute the actual section-change/Fox cokernel needed for a nonzero pushed-out abelian-kernel extension class.

The target is not merely a raw residual: it must survive all admissible lift-change coboundaries and the finite-kernel relations.

## Stop conditions

Do not reopen:
- mod-p degree-5 obstruction;
- scalar/coinvariant/norm shortcuts;
- blind carrier search.

If no uniform a=1 witness is obtained, retain a=1 as OPEN and move only then to the unmarked reconstruction branch.

## Classification

- a>=2 relative threshold: PASS / CLOSED.
- a=1 relative threshold: OPEN.
- a=1 p=3,d=2 GAP evidence: PASS / LOCAL.
- independent a=1 pushout witness: OPEN / LOAD-BEARING.
