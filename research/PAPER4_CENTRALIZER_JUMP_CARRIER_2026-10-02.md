# PAPER 4 — CENTRALIZER-JUMP CARRIER / ORDINARY CONTAMINATION ELIMINATION — 2026-10-02

## Decision

A genuinely new carrier survives the ordinary-contamination gate.

The correct construction is not a quotient of the whole degree-2 commutator sector. Instead, use the intrinsic jump between two centralizer filtrations of a degree-one direction.

For a finite Zassenhaus window through degree n, let L_1=D_1/D_2. For u in L_1 define
C_m(u)={x in L_1 : [u~,x~] in D_m},
with arbitrary lifts. The filtration-membership condition is lift-independent at the relevant levels.

For m=3 this is the ordinary degree-2 centralizer:
C_3(u)=ker(L_1 -> L_2, x -> [u,x]).
At the first nonzero special-defect degree q use C_q(u). The jump carrier is
J_q(u)=C_q(u)/C_3(u).

## Ordinary contamination removal

For a basis origin vertex v of a specially oriented graph:
- ordinary edge v-w gives [v,w]=1, hence w is already in C_3(v);
- special edge (v,w) gives [v,w]=±v^q mod D_{q+1}, hence w is in C_q(v) but not C_3(v);
- a nonedge has degree-2 commutator and therefore does not lie in C_q(v).

Thus the ordinary-edge contribution is removed before the q-layer is interpreted.

## RP-5

For A with special edges (a,s),(b,s):
C_q(a)/C_3(a)=F_p s-bar and C_q(b)/C_3(b)=F_p s-bar.

For B with (a,s),(b,t):
C_q(a)/C_3(a)=F_p s-bar and C_q(b)/C_3(b)=F_p t-bar.

Hence the construction distinguishes A/B without the previous global degree-2 centralizer.

## Mixed ordinary/special test

For G=<a,b,s | [a,b]=1, s a s^{-1}=a^{1+q}>:
C_3(a)=span(a,b), C_q(a)=span(a,b,s), so J_q(a)=F_p s.
For b, C_q(b)=C_3(b)=span(a,b), so J_q(b)=0.
Thus the ordinary edge is killed while the special edge survives.

## q-blindness

Define J_m(u)=C_m(u)/C_3(u) for all m>=3 from the windows, and let the local first jump be the first m with J_m(u) nonzero. q is therefore detected rather than inserted. A graph-wide q synchronization is still separate.

## Functoriality and gauge

D_m/D_{m+1}, commutator depth, C_m(u), and J_m(u) are invariant under filtered-group isomorphisms. Scaling u does not change C_m(u), so the carrier is projective in u.

## Remaining load-bearing theorem

The unresolved point is cancellation for arbitrary linear directions u=sum c_i v_i. The decisive theorem is:

**Centralizer-jump purity:** for a specially oriented graph and q>2, nonzero J_q(u) must come from genuine special termini attached to the support of u; no new J_q(u) may arise solely from cancellation among ordinary/nonedge degree-2 commutators.

This is a one-direction problem, substantially sharper than the failed Grassmannian accidental-plane theorem.

## Classification

- intrinsic centralizer filtration: PASS / LOCAL;
- ordinary contamination removal via C_q/C_3: PASS / LOCAL;
- q-blind formulation: PASS / LOCAL;
- RP-5 incidence separation: PASS / LOCAL, strengthened;
- mixed ordinary/special test: PASS / LOCAL;
- arbitrary linear-direction purity: OPEN / LOAD-BEARING;
- arbitrary graph incidence reconstruction: OPEN;
- full orientation reconstruction: OPEN.

No large scan is authorized before the purity theorem is resolved.

## Literature control

The Zassenhaus graded object is a restricted Lie algebra, with commutator and p-power operations respecting the filtration. The oriented pro-p RAAG literature uses the special-edge relation wvw^{-1}=v^{1+q}, with the second vertex the special/sinkhole vertex. The present centralizer-jump carrier is a Paper 4 construction, not a claim extracted from the literature.
