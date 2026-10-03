# PAPER 4 — CRITICAL WINDOW BOUNDARY ATTACK: s-RECOVERY AND a=s — 2026-10-03

## Result

For the critical window
\[
W_s:=W_{p^s+1}(G_{s,a}),
\]
the abelianization already determines the depth parameter s in the full declared family, independently of Gate T/U.

For every finite a with 1<=a<=s,
\[
W_s^{ab}\cong \mathbf Z/p^a\oplus(\mathbf Z/p^{s+1})^d
\]
when a<s, while at a=s
\[
W_s^{ab}\cong \mathbf Z/p^s\oplus(\mathbf Z/p^{s+1})^d.
\]
For a=infinity,
\[
W_s^{ab}\cong \mathbf Z/p^s\oplus(\mathbf Z/p^{s+1})^d.
\]
Thus the exponent of W_s^{ab} is exactly p^{s+1}, so
\[
\boxed{s=\log_p(\exp W_s^{ab})-1.}
\]
This removes Gate T/U from the logical proof of s-identifiability.

## Consequence

For 1<=a<s, the previous SNF theorem plus the new exponent observation gives full simultaneous parameter recovery
\[
W_{p^s+1}(G_{s,a})\Longrightarrow (s,a)
\]
without the relative quotient map and without Gate T.

Classification:
- s recovery from unmarked critical window: **PASS / CLOSED**;
- simultaneous (s,a) recovery for 1<=a<s: **PASS / CLOSED**;
- a=infinity versus finite a<s: **PASS / CLOSED**;
- a=s versus a=infinity: **OPEN** by abelianization.

## Boundary attack a=s

At a=s and a=infinity the abelianization is identical:
\[
W_s^{ab}\cong \mathbf Z/p^s\oplus(\mathbf Z/p^{s+1})^d.
\]
Therefore any separation must use genuinely nonabelian information.

A natural candidate is the first higher Zassenhaus/relation layer. The stress relation is
\[
z^{p^s}=x_1^{p^a}[x_1,x_2]\cdots[x_{d-1},x_d].
\]
For a=s, the degree-p^s component contains x_1^{p^s}; for a=infinity it does not. However, the standard associated graded Lie algebra of a Demushkin group is governed by the quadratic initial form, so the ordinary graded Lie algebra is not expected by itself to distinguish the higher q-term. This prevents an unjustified claim that gr(W_s) separates the boundary.

The next intrinsic candidates are therefore:
1. a higher Zassenhaus relation/Massey invariant at length p^s;
2. a nonabelian class-2/metabelian quotient retaining the p^s-power relation;
3. an intrinsic higher Bockstein/extension-defect operation on H^1(W_s,F_p).

The literature confirms that Bockstein/Massey operations encode relation information in Zassenhaus quotients, and recent work on Demushkin groups shows that q-dependent higher A_infinity/Massey phenomena can survive even when low-order cohomology is insensitive to q. This is a candidate route, not yet a theorem for the present stress family.

## Independent literature control

The standard Demushkin classification identifies q through the relator
\[
x_1^q[x_1,x_2]\cdots,
\]
and the quadratic initial form of the Zassenhaus graded algebra loses the q-term for odd p when q>p^2-level; hence low-degree graded data cannot simply be asserted to recover q. The p-Zassenhaus/Massey literature provides the correct framework for testing higher relation layers.

## Stop condition

Do not reopen Gate T/U merely for s-recovery. Do not claim a=s separation until an explicit intrinsic nonabelian invariant is exhibited and independently verified.

Current boundary classification:
\[
\boxed{a=s\text{ versus }a=\infty:\ OPEN}
\]
