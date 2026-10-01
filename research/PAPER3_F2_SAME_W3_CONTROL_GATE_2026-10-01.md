# PAPER 3 — F2 SAME-W3 CONTROL GATE

Date: 2026-10-01

## Purpose

After the uniform F1 result, the next authorized enlargement is the genuinely different Blumer–Quadrelli F2 family. The question is whether an F2 non-1-cyclotomic group can share W3 with a cyclotomic control, reproducing the decisive same-window obstruction.

## Pre-check

Object: W_n=G/D_n, with T_cyc the existence of a 1-cyclotomic orientation.

Input: only the finite filtered group W_n; no q or orientation is inserted into the definition.

Functoriality: filtered-group isomorphisms induce the comparison.

Gauge: no chosen presentation coordinate may be used as the final separator.

Orientation bridge: global F2 non-1-cyclotomicity is literature input; the new target is finite-window visibility of that obstruction.

q-blindness: W_n itself is q-blind. Any separator must be formulated intrinsically from W_n.

Separation: first test the smallest case (p,d,q)=(3,2,3).

Novelty: a repeat of the known F2 non-1-cyclotomic theorem is not a result; only same-window/different-target, sharp threshold, or a reusable carrier is load-bearing.

Stop: do not run large computation until a concrete cyclotomic control with W3 equality is identified.

## First structural test

For d=2, take the F2 quadratic relation space
R_F2=< [X1,Y1]+[X2,Y2], [Z1,Z2] >
with {Z1,Z2} an unpaired pair, e.g. [X1,X2].

For the most immediate cyclotomic controls supplied by the elementary-type literature, namely free products of two rank-2 Demushkin cyclotomic pairs, the quadratic relation space is
R_ctrl=< [X1,Y1], [X2,Y2] >.

These two 2-planes are not equivalent under GL(V) in the rank-4 case: the Pfaffian of the pencil a([X1,Y1]+[X2,Y2])+b[X1,X2] is proportional to a^2, whereas the Pfaffian of a[X1,Y1]+b[X2,Y2] is proportional to ab. The first has a repeated projective root; the second has two distinct roots. Thus W3 cannot be isomorphic between this F2 example and this natural cyclotomic free-product control.

This is a local obstruction to the obvious control, not a no-go theorem for all cyclotomic groups.

## Classification

- F2 same-W3 cyclotomic obstruction: OPEN / DECISIVE.
- Natural free-product cyclotomic control: FAIL / CLOSED as a W3-matching control in the smallest rank-4 test.
- Broad F2 finite-window recognition: OPEN / CONDITIONAL.
- No large computation authorized yet.

## Next authorized search

Search for cyclotomic groups outside the immediate free-product control class whose W3 quadratic relation space has the F2 repeated-root type. Candidate source classes include cyclotomic semidirect products and other elementary-type constructions. If no such control exists under a meaningful category, that negative result itself may become a structural boundary.
