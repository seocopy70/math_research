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


## 2026-10-03 — BOUNDARY ATTACK: CANONICAL p^s-POWER DEFECT REDUCES TO GRADED GAUGE DATA

A bounded attack was made on the remaining boundary a=s versus a=∞.

### 1. Intrinsic candidate
Let W=W_{p^s+1}(G_{s,a}) and A=W^{ab}. In the boundary cases
A ≅ Z/p^s ⊕ (Z/p^{s+1})^d.
The subgroup
L_s := (A[p^s]+pA)/pA
is canonically one-dimensional over F_p. Thus the “short” abelian direction is intrinsic; it is not legitimate to refer to z or z x_1^{-1} as marked generators.

For a lift g of a generator of L_s, its p^s-th power lies in D_{p^s}(W), and changing the lift by D_2 or by a p-divisible abelian correction changes the p^s-power only modulo D_{p^s+1}. Hence the first candidate is the intrinsic restricted p^s-power operation on the short line.

### 2. Shear calculation
For a=s, the short direction is represented by z x_1^{-1}; for a=∞ it is represented by z. Hall–Petrescu/Jacobson gives
(Z-X)^{[p^s]} = Z^{[p^s]}-X^{[p^s]}+J_{p^s}(Z,-X),
where J_{p^s} is the non-additive Jacobson cross polynomial. It is genuinely nonzero in the free restricted Lie algebra. Already for p=3,
(X+Y)^{[3]}=X^{[3]}+Y^{[3]}+2[X,[Y,X]]+[Y,[Y,X]].
Thus the naive shear equivalence cannot be declared an isomorphism of critical windows merely by cancelling p^s-powers.

### 3. Decisive limitation
However, this does NOT separate a=s from a=∞. The operation above is part of the intrinsic restricted Lie algebra associated to the Zassenhaus filtration. For Demushkin-type one-relator groups the associated graded algebra is controlled by the quadratic initial relator and loses the higher q-term; the literature explicitly gives the same quadratic initial form for the q-family. Therefore the Jacobson cross term changes the coordinate representative of the short direction, but does not by itself produce a new filtered-group isomorphism invariant.

This is a genuine candidate closure:
- canonical short line L_s: PASS / CLOSED;
- intrinsic p^s-power operation on L_s: PASS / LOCAL;
- naive shear-isomorphism claim: FAIL / CLOSED (not justified);
- separation of a=s and a=∞ by the restricted graded object: FAIL / CLOSED;
- separation by the full filtered extension/lifting defect: OPEN.

The remaining problem is therefore sharper than before: one must detect a difference in the filtered lift of the common quadratic restricted Lie algebra, not in its associated graded restricted Lie algebra. Equivalently, the required invariant must retain extension/deformation data one filtration level beyond the quadratic shadow.

### Literature control
The standard Demushkin presentation/classification and the fact that its graded algebra is determined by the quadratic initial form are documented in Mináč–Pasini–Quadrelli–Tân. The Zassenhaus/restricted-Lie and higher-Massey framework of Gärtner and Efrat confirms that relation information can be encoded in higher operations, but it does not supply the required intrinsic filtered deformation invariant for this exact boundary.

### Classification after this attack
\[
\boxed{a=s\text{ versus }a=\infty:\ OPEN}
\]
with the graded restricted-Lie candidate closed as a no-go, not as a solution.
