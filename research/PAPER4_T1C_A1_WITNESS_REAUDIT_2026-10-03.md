# PAPER 4 — T1-C A=1 WITNESS RE-AUDIT — 2026-10-03

## Finding
The proposed finite group H_s with
H_s: z^(p^(s+1))=1, x^p=z^(p^s), yzy^{-1}=z^(1-p), yxy^{-1}=x
is an abstract quotient of the rank-two stress presentation for a=1. The relation x^p[x,y]=z^(p^s) is preserved because [x,y]=1.

## Load-bearing failure
The T1-C survival transfer requires H_s to be a Q-equivariant quotient/pushout of the kernel over the reference quotient Q_s=D/D_{p^s+1}(D). This fails. In H_s, [x,y]=1. In D, the defining relation gives [x,y]=x^{-p}. At the critical window x^p is not killed by D_{p^s+1}; hence the canonical images of x,y in Q_s do not commute. Therefore no compatible map H_s -> Q_s sending the displayed x,y to the canonical quotient generators exists.

So H_s detects an abstract finite quotient phenomenon but cannot be used to prove nonzero relative extension class by pushout/naturality.

## Consequence
The a=1 independent-closure claim is superseded. The marked relative finite-kernel survival and exact threshold remain OPEN at a=1. The certified theorem remains restricted to a>=2, s>a. This is a genuine correction, not a reopening of the frozen nonboundary threshold.

## Classification
- abstract H_s quotient: PASS / LOCAL;
- critical visibility inside H_s: PASS / LOCAL;
- Q-equivariant pushout compatibility: FAIL / CLOSED for this witness;
- a=1 marked survival: OPEN / LOAD-BEARING;
- a=1 exact relative threshold: OPEN / LOAD-BEARING;
- Gate B intrinsic reconstruction/separation: OPEN / LOAD-BEARING.
