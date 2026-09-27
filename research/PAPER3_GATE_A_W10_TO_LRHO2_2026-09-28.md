# PAPER 3 — Gate A: finite-window construction of L(rho_2)

Date: 2026-09-28
Status: PASS / CLOSED (at the declared category-level scope)

## Question
Can the finite filtered object W_10(G) construct the full mod-27 lift domain
\[
L(\rho_2)=\{\rho_3:G\to(\mathbf Z/27)^\times:\rho_3\bmod9=\rho_2\}
\]
without importing chi mod 27?

## Declared input
\[
W_{10}(G)=(G/P_{10}(G),P_1/P_{10},\ldots,P_9/P_{10})
\]
with the declared filtered/marked morphism structure. No presentation relator, q, or canonical chi mod 27 is an input.

## Step 1 — recover only rho_2
The already-audited projective degree-(2,3) carrier recovers the mod-9 orientation rho_2 at its declared intrinsic scope. Since W_10 canonically truncates to W_4, the same carrier may be evaluated on W_10 by restriction to the W_4 sub-window. This does not reopen the mod-9 gate and does not import higher orientation data.

## Step 2 — finite lift set
Put
\[
Q_{10}:=G/P_{10}(G),\qquad U_2=(\mathbf Z/9)^\times,\qquad U_3=(\mathbf Z/27)^\times.
\]
Let \(\bar\rho_2:Q_{10}\to U_2\) be the character induced by rho_2. Define
\[
L_{10}(\rho_2):=\{\bar\rho_3\in\operatorname{Hom}(Q_{10},U_3):
\bar\rho_3\bmod9=\bar\rho_2\}.
\]
This is a finite set constructed solely from W_10 and the recovered rho_2.

## Step 3 — equality with the full-group lift set
Every \(\rho_3\in L(\rho_2)\) factors through Q_10 by the audited finite semidirect-product argument: the graph map
\[
\psi(g)=(z(g),\rho_3(g))
\]
for every \(\rho_3\)-twisted crossed cocycle lands in the finite semidirect product for coefficients modulo 27, whose tenth Zassenhaus term is trivial. Hence \(P_{10}(G)\) acts trivially on the coefficient data, and in particular \(\rho_3(P_{10})=1\). Thus restriction gives a map
\[
L(\rho_2)\to L_{10}(\rho_2).
\]
Conversely every \(\bar\rho_3\in L_{10}(\rho_2)\) inflates uniquely along \(G\to Q_{10}\) to an element of \(L(\rho_2)\). Therefore
\[
\boxed{L(\rho_2)\cong L_{10}(\rho_2)}.
\]

## Intrinsicity / functoriality
A filtered isomorphism of W_10 transports \(Q_{10}\), the already-defined rho_2 carrier, and hence the set of lifts. No presentation or relator choice occurs in the definition. The construction is q-blind: q is not an argument. The only orientation datum used is the previously recovered mod-9 output rho_2.

## What this does NOT prove
- It does not construct the delta_3 family from W_10.
- It does not select a distinguished rho_3 from the 81-element torsor in rank four.
- It does not recover chi mod 27.
- It does not prove any absolute minimality of the W_10 carrier.
- It does not turn the formal lift-set construction into a new novelty claim; the finite lift-set/torsor mechanism is standard once rho_2 is supplied.

## Classification
**PASS / CLOSED** for Gate A in the declared category: W_10 determines the full lift domain L(rho_2) as a finite, presentation-independent, q-blind set.

The novelty-bearing problem therefore moves cleanly to Gate B:
\[
W_{10}(G)\longrightarrow\n\{\delta_{3,\rho_3}\}_{\rho_3\in L(\rho_2)}.
\]
