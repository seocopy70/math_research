# HARD ATTACK 57 — INFORMATION DEPTH AND LAYER-B TOWER REUSE — 2026-09-20

## Scope

This attack executes the two tests authorized by the Strategic Reset:

1. **Test I:** formulate the sharp filtration-depth boundary as an explicit information theorem.
2. **Test II:** determine whether the Layer-B relation/power datum [(R,p)] canonically propagates to higher 3-adic digits, or whether a genuinely new rigidifying layer appears.

The target is not to compute another representation module. The input must remain q-blind filtered/finite information; q and the known orientation formula may be used only as external comparison data.

---

## Pre-check

### Object

For the standard rank-four family
\[
G_{3^s}=\langle x_1,x_2,x_3,x_4\mid x_1^{3^s}[x_1,x_2][x_3,x_4]=1\rangle
\]
and the power-free control
\[
G_\infty=\langle x_1,x_2,x_3,x_4\mid [x_1,x_2][x_3,x_4]=1\rangle,
\]
consider finite Zassenhaus quotients \(G/D_N\) and lower-3-central quotients \(G/P_n\).

For Layer B, consider the already established projective degree-(2,3) carrier
\[
\overline J_3=[(R,p)],\qquad
R=[X_1,X_2]+[X_3,X_4].
\]

### Input

Test I uses only the finite filtered quotient. The formulas involving \(\chi\) are comparison statements, not definitions.

Test II asks whether the already established relation/power tower itself supplies higher digits, without passing through q, the dualizing action, or the known classification formula.

### Functoriality / gauge

The finite quotients are characteristic quotients of the group, hence invariant under continuous automorphisms. The projective Layer-B carrier is already known to be presentation/gauge independent at mod 9 under the audited transgression/Bockstein convention.

### Orientation bridge

For Test I, the bridge is deliberately external: the standard-family formula
\[
\chi_{3^s}(x_2)=(1-3^s)^{-1}
\]
is used only to identify the information threshold.

For Test II, a genuine bridge is the load-bearing issue.

### q-blindness

Neither test defines its object using q or chi.

### Separation

The test family compares \(G_{3^s}\) with \(G_\infty\), and more generally compares distinct valuation levels.

### Novelty

The intended result is not the known formula for chi. It is an information-depth boundary and a structural test of whether the mod-9 relation/power carrier can be reused for higher digits.

### Stop

No representation scan or new spectral scan is needed unless Test II identifies a concrete surviving higher carrier.

---

# Test I — Sharp filtration-depth theorem

## I.1 Zassenhaus threshold

For the standard family, the previously audited Jennings/Zassenhaus calculation gives:

\[
G_{3^s}/D_N\cong G_\infty/D_N
\quad\Longleftrightarrow\quad
N\le 3^s
\]
for the tested family, with separation at the next level
\[
N=3^s+1.
\]

The sharpness is visible already in abelianization:
\[
(G_{3^s}/D_{3^s+1})^{ab}
\cong
\mathbf Z/3^s\oplus(\mathbf Z/3^{s+1})^3,
\]
whereas
\[
(G_\infty/D_{3^s+1})^{ab}
\cong
(\mathbf Z/3^{s+1})^4.
\]

Thus the first Zassenhaus depth that detects the power \(3^s\) is
\[
\boxed{D_{3^s+1}}.
\]

Now \(\chi_{3^s}\equiv\chi_\infty\pmod{3^n}\) whenever \(s\ge n\), while for \(s<n\) the two differ modulo \(3^n\). Therefore, among the family \(s=0,1,2,\ldots\) together with the power-free control, the worst case for determining \(\chi\bmod 3^n\) is \(s=n-1\).

Hence the sharp family-level Zassenhaus information boundary is

\[
\boxed{
\chi\bmod 3^n
\text{ requires, in the worst case, depth }
D_{3^{n-1}+1}.
}
\]

For example:
\[
n=2:\ D_4? 
\]
The threshold formula is \(D_{3^{1}+1}=D_4\) for the family-level distinction between q=3 and the control. This corrects a potentially misleading shorthand in which the first mod-9 relation jet is identified directly with a single Zassenhaus quotient index: the degree-(2,3) jet is not itself identical to the whole quotient \(G/D_4\).

For mod 27:
\[
\boxed{D_{10}}
\]
is the corresponding worst-case Zassenhaus threshold.

This distinction is important: **Layer B is a compressed carrier extracted from low-degree relation/power data; it is not identical to the full finite quotient at the threshold depth.**

## I.2 Lower-3-central threshold

For the lower-3-central filtration \(P_n\), the previously audited standard-family comparison gives
\[
G_{3^s}/P_n\cong G_\infty/P_n
\quad\Longleftrightarrow\quad
n\le s+1,
\]
with separation at
\[
n=s+2.
\]

Therefore the worst case \(s=n-1\) for \(\chi\bmod3^n\) gives

\[
\boxed{
\chi\bmod3^n
\text{ requires, in the worst case, }
G/P_{n+1}.
}
\]

For mod 27 this is
\[
\boxed{G/P_4}.
\]

The striking information-scale comparison is therefore

\[
\boxed{
\text{Zassenhaus depth }\sim 3^{n-1},
\qquad
\text{lower-3-central depth }\sim n.
}
\]

This is an information-depth statement, not a claim that the lower-3-central quotient alone carries a canonical pointed orientation.

## I.3 Sharpness and logical boundary

The result proves a **family-level lower bound on the depth of finite filtered information needed to distinguish the relevant orientation classes**.

It does **not** yet prove:

- that every admissible orientation carrier must contain the entire quotient \(G/D_{3^{n-1}+1}\);
- that \(G/P_{n+1}\) alone admits a PD²-free natural orientation selector;
- that the threshold is universal over all Demuškin groups and all admissible morphisms;
- that each 3-adic digit is an independent new information layer.

The last point is especially important: an exact characteristic-zero relation can compress infinitely many digits into one exact equation.

### Test-I classification

\[
\boxed{\text{Sharp finite-filtration information boundary: PASS / LOCAL}}
\]

It is sharper than a collection of quotient coincidences, but remains local to the standard family and comparison orientation formula.

---

# Test II — Can Layer B be reused as a higher-digit tower?

The relevant question is now precise:

> Is there a canonical sequence of higher finite relation/power carriers \(J_n\), with \(J_2=\overline J_3\), such that the same structural datum propagates recursively and directly yields \(\chi\bmod3^n\), without first recovering q or invoking the known orientation formula?

## II.1 What survives from Layer B

At mod 9, the carrier
\[
[(R,p)]
\]
contains exactly the first non-graded power direction coupled to the quadratic relation. The audited twisted degree-(2,3) obstruction proves that this data determines \(\chi\bmod9\) under the stated hypotheses.

So the first extension layer is real.

## II.2 The naive recursive hypothesis

A tempting recursion is:

\[
(R,p)
\longrightarrow
(R,p,p_2)
\longrightarrow
(R,p,p_2,p_3)
\longrightarrow\cdots
\]

where \(p_j\) records the next 3-adic correction of the power/relation term.

But there are two fundamentally different possibilities.

### A. Genuine tower reuse

The higher \(p_j\) are functorially determined from the same intrinsic relation/power carrier by canonical connecting maps, and the successive obstruction maps assemble directly into the logarithmic orientation:
\[
J_n\longrightarrow O_{3^n}.
\]

### B. Re-expansion of the exact relation

The higher \(p_j\) are simply successive coordinate expansions of the exact characteristic-zero Fox relation. Then the tower is not a new intrinsic compression; it is a finite-precision presentation of the already known exact carrier.

The project must distinguish A from B.

## II.3 The mod-27 coefficient-extension test

The strongest concrete candidate already tested was
\[
\mathcal B_{27}
=
(H^1(G,\mathbf F_3),H^1(G,\mathbf Z/9),
\mathrm{red},\iota,\smile,\beta_1,\beta_9).
\]

The standard family calculation shows that this package detects the three valuation classes
\[
v_3(q)=1,2,\ge3,
\]
and hence separates the corresponding standard-family values of \(\chi\bmod27\).

However, the full structured carrier classification has now been established only on that standard family. It does not produce a universal orientation bridge.

More importantly for Test II, the carrier does not by itself provide a canonical characteristic-zero lift of the mod-3 orientation direction. The project therefore cannot legitimately promote the observed q=3/q=9/q\ge27 pattern to a recursive orientation tower.

Thus the present Bockstein extension package is a **detector layer**, not a proved higher-digit reuse theorem.

## II.4 The filtration-depth test exposes the same obstruction

Test I shows that the information needed to distinguish \(q=3^{n-1}\) from the power-free control first appears at Zassenhaus depth
\[
3^{n-1}+1.
\]

Therefore a genuinely bounded-degree reuse of the fixed Layer-B jet would have to explain how information appearing arbitrarily deep in the filtration is functorially compressed back into the same finite degree-(2,3) object.

No such compression theorem has been proved.

The full mod-3 associated graded cannot supply it: that entire object is q-blind. Hence the higher information must enter through non-graded extension data.

This gives a sharp alternative:

\[
\boxed{
\text{fixed Layer-B carrier reused for all digits}
\quad\text{vs.}\quad
\text{new extension information at increasing depth}.
}
\]

At present the first alternative is **not proved**.

## II.5 Strongest conclusion currently justified

The combination of Test I and the failed mod-27 orientation-bridge attempt yields:

1. The first Layer-B extension is sufficient for mod 9.
2. The finite filtration depth at which the next orientation class becomes distinguishable grows with n.
3. The tested coefficient-extension enlargement detects those classes but has not produced a presentation-free rigidifying bridge.
4. Therefore there is currently **no theorem that the same Layer-B carrier recursively generates all higher digits**.
5. Any successful higher-digit theorem must exhibit an explicit functorial compression mechanism from deeper extension data to a fixed finite carrier, or else identify a new intrinsic carrier at the first depth where Layer-B ceases to suffice.

This is not a proof that fixed-carrier reuse is impossible. It is a proof that the present evidence does not establish it, and that the first decisive obstruction is now the missing compression/bridge theorem rather than another finite numerical calculation.

### Test-II classification

\[
\boxed{
\text{Layer-B tower reuse as a proved all-digit orientation mechanism:
OPEN / DECISIVE}
}
\]

The mod-27 Bockstein package remains:

\[
\boxed{
\text{finite q-layer detector: PASS / LOCAL;}
\quad
\text{all-digit orientation carrier: CONDITIONAL / OPEN.}
}
\]

---

# First genuinely new layer — current diagnosis

The current evidence does **not** justify declaring the 19D \(\mathcal S\) to be the first new orientation layer.

The first rigorous statement is weaker and more useful:

\[
\boxed{
\text{The first possible genuinely new orientation information must enter through
non-graded extension data beyond the mod-9 relation/power carrier.}
}
\]

Test I locates where such information can first become visible in finite filtration depth. Test II shows that the existing Layer-B mechanism has not yet been shown to compress that deeper information.

Therefore the next research target should be a **minimal higher extension bridge**, not a representation decomposition:

1. define the first finite extension datum at the sharp threshold for mod 27;
2. quotient out the already-known Layer-B information;
3. test whether the residual datum admits a natural orientation functional;
4. only if a nonzero residual survives this gate should the 19D \(\mathcal S\) branch be reopened as a candidate carrier.

This gives a clean adequacy criterion for Layer C.

---

# Final decision table

| Question | Status |
|---|---|
| Full mod-3 associated graded recovers chi | **FAIL / CLOSED** |
| Mod-9 Layer-B carrier [(R,p)] recovers chi mod 9 | **PASS / CLOSED** |
| Sharp Zassenhaus depth for chi mod 3^n on standard family | **PASS / LOCAL** |
| Sharp lower-3-central depth for chi mod 3^n on standard family | **PASS / LOCAL** |
| Fixed Layer-B carrier proven to generate all higher digits | **OPEN / DECISIVE** |
| Bockstein-extension package as finite q-layer detector | **PASS / LOCAL** |
| Bockstein-extension package as all-digit orientation carrier | **CONDITIONAL / OPEN** |
| 19D S as first genuinely new orientation layer | **OPEN / NOT YET JUSTIFIED** |
| Next authorized computation | **Minimal higher-extension residual at the mod-27 threshold** |

## Stop rule after HA57

Do **not**:
- scan the 19D representation;
- scan more Bockstein layers on the same standard q-family;
- compute more spectral differentials without a new target.

The next attack should construct the **mod-27 threshold residual**:
\[
\text{(finite extension data at }P_4\text{ or }D_{10})
\big/
\text{(Layer-B information)}.
\]

The decisive question is whether this residual is zero (Layer-B reuse/collapse) or nonzero with a natural orientation bridge (first genuinely new layer).

## Classification

**HARD ATTACK 57 — PASS / LOCAL for Test I; OPEN / DECISIVE for Test II.**

