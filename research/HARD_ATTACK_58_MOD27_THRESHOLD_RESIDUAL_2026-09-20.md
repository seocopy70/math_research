# HARD ATTACK 58 — MOD-27 THRESHOLD RESIDUAL: HIGHER POWER LINE BEYOND LAYER B — 2026-09-20

## 0. Purpose

HA58 executes the authorized mod-27 threshold-residual attack. The target is not another Bockstein computation and not the 19D representation. It asks:

> What is the first finite filtered datum at P_4/D_10 that remains after the already established mod-9 Layer-B information is factored out?

The answer is a higher power/relation class in the next p-central layer. It is genuinely new finite extension information, but the orientation bridge is only partial.

---

## 1. Pre-check

### Object

Use the intrinsic lower-3-central tower
\[
P_1=G,\qquad P_{n+1}=P_n^3[P_n,G],
\]
and the associated power/relation extension data.

For the standard rank-four family
\[
G_q=\langle x_1,x_2,x_3,x_4\mid x_1^q[x_1,x_2][x_3,x_4]=1\rangle,
\qquad q=3^s,
\]
the first mod-9 Layer-B datum records the degree-two relation together with the first nontrivial power direction.

### Input

Only finite filtered group/extension data and their canonical power/commutator maps are allowed. q, chi, the dualizing module, and the classification formula are excluded from the definition.

### Functoriality

The lower p-central filtration is characteristic. Hence the induced quotients and their power/commutator maps are functorial under continuous group isomorphisms.

### Gauge

No generator is chosen in the final formulation. The relevant power datum is treated projectively; scalar normalization is a separate issue.

### Orientation bridge

Not assumed. It is precisely the remaining gate.

### q-blindness

q is not supplied. The residual is defined from the finite filtered extension itself.

### Separation

The standard family provides the test:
\[
q=9\quad\text{versus}\quad q\equiv0\pmod{27}.
\]

### Stop

No representation scan and no further trivial-coefficient Bockstein elaboration is authorized.

---

# 2. The residual at P_4

The lower-3-central threshold from HA57 says that mod 27 first becomes distinguishable at
\[
P_4
\]
in the standard family.

The reason is structural. In the normal form, the power term is
\[
x_1^{3^s}.
\]
For s=1 it already contributes at the first nontrivial power level and is part of the mod-9 Layer-B carrier.

For s=2,
\[
x_1^9=(x_1^3)^3
\]
first appears one p-central layer deeper. Modulo P_4 its leading contribution is the restricted cubic/power class
\[
\boxed{X_1^{[3]}}
\]
in the degree-three p-central extension layer, modulo the degree-three commutator contribution already forced by the lower relation.

For s>=3,
\[
x_1^{3^s}\in P_4,
\]
so this degree-three residual vanishes.

Thus, after quotienting out the already known mod-9 Layer-B information, the first threshold residual has the form

\[
\boxed{
\mathcal R_{27}^{\mathrm{res}}
=
\langle \text{next power/relation class in }P_3/P_4\rangle
}
\]

and on the standard family its detection pattern is

\[
q=3:\ \text{already absorbed by Layer B},
\]
\[
q=9:\ \mathcal R_{27}^{\mathrm{res}}\ne0,
\]
\[
27\mid q:\ \mathcal R_{27}^{\mathrm{res}}=0.
\]

This exactly matches the information boundary D_10/P_4 found in HA57.

---

# 3. Why this is genuinely beyond Layer B

The crucial point is that this is not another presentation of the same mod-9 class.

Layer B sees the first non-graded power/relation coupling. Its finite target distinguishes the first orientation digit:
\[
\chi\pmod9.
\]

The residual above lives one p-central level deeper and distinguishes
\[
q=9
\quad\text{from}\quad
q\equiv0\pmod{27},
\]
even though both have the same mod-9 orientation value
\[
\chi(x_2)\equiv1\pmod9.
\]

Therefore the residual cannot be recovered from the mod-9 carrier alone.

This is a genuine separation statement:

\[
\boxed{
\text{Layer B does not contain the mod-27 threshold information.}
}
\]

It does not yet prove that the residual is an independent orientation carrier, because it may be only the next extension coefficient needed to extend the same relation/power mechanism.

---

# 4. Intrinsic line versus scalar

There is an important gauge distinction.

The degree-one filtered object has the intrinsic torsion line
\[
\ell=\operatorname{im}\bigl(\operatorname{Tor}(G^{ab})
\to G/\Phi(G)\bigr).
\]

The symplectic commutator pairing identifies this line with a projective covector direction. In the frozen rank-four normal form, this is the direction represented by
\[
e_1\longleftrightarrow e_2^*
\]
up to the common convention/sign/unit.

The higher power residual is the corresponding next-depth power image of this intrinsic line.

Consequently the residual determines, intrinsically, a **projective direction** for the next orientation correction.

But it does not by itself determine the exact scalar lift
\[
3e_2\in H^1(G,\mathbf Z/9).
\]

The missing scalar normalization is exactly the same kind of gauge issue already controlled at mod 9 by the common transgression/fundamental-class normalization.

Thus the correct statement is:

\[
\boxed{
\mathcal R_{27}^{\mathrm{res}}
\text{ gives the next projective orientation direction, but not yet the full normalized digit.}
}
\]

---

# 5. Comparison with the known orientation, used only as external audit

For the standard family Labute's classical computation gives
\[
\chi(x_2)=(1-q)^{-1}.
\]

Hence
\[
q=3
\Rightarrow
\frac13\log\chi(x_2)\equiv1\pmod9,
\]
while
\[
q=9
\Rightarrow
\frac13\log\chi(x_2)\equiv3\pmod9,
\]
and
\[
27\mid q
\Rightarrow
\frac13\log\chi(x_2)\equiv0\pmod9.
\]

The residual detection pattern therefore agrees with the expected second 3-adic digit pattern.

This comparison is validation only; the orientation formula is not part of the residual's definition.

Labute's theorem explicitly gives the standard Demuškin formula \(\chi(x_2)=(1-q)^{-1}\) for the normal form. citeturn1search29

---

# 6. What this does and does not prove

### Proven at the present level

1. **A concrete first residual exists:** the next p-central power/relation layer at P_4.
2. **It is q-blind by construction:** it is defined from characteristic filtered data.
3. **It is genuinely beyond Layer B:** it separates q=9 from 27|q while Layer B cannot.
4. **Its projective direction is tied to the same intrinsic torsion line and symplectic pairing that controls the first orientation direction.**
5. **The standard-family orientation audit agrees with the expected digit 3.**

### Not proved

1. A canonical scalar normalization identifying the residual with exactly
   \[
   3e_2\in H^1(G,\mathbf Z/9).
   \]
2. A universal natural transformation
   \[
   \mathcal R_{27}^{\mathrm{res}}
   \longrightarrow
   \chi\pmod{27}.
   \]
3. That this residual is smaller than, or factors naturally through, the full P_4 quotient.
4. A general theorem for arbitrary rank-four Demuškin inputs rather than the standard family.
5. That the 19D LHS sector is the same information: no identification is made.

---

# 7. Strategic consequence

This changes the status of the information-layer picture.

The first genuinely new higher information is now **identified**, at least on the standard family:

\[
\boxed{
\text{Layer A}
\rightarrow
\text{Layer B: first power/relation jet}
\rightarrow
\text{Layer B+:
next p-central power/relation residual}.
}
\]

So the 19D cohomological sector is no longer the first place where new information could appear. A simpler filtered extension datum already appears at the P_4 threshold.

The 19D sector may still encode this residual cohomologically, but that identification is not established and is no longer the preferred route.

The architecture is therefore:

\[
\boxed{
\text{mod-3 graded}
\;\subsetneq\;
\text{mod-9 relation/power jet}
\;\subsetneq\;
\text{mod-27 higher power residual}
\;\subseteq\;
\text{full filtered relation tower}.
}
\]

The first strict inclusion is PASS/CLOSED. The second is now PASS/LOCAL on the standard family.

---

# 8. Next decisive gate

The remaining question is sharply reduced:

> Can the P_4 higher-power residual be normalized functorially so that its projective direction and the already fixed Layer-B normalization combine to give the exact mod-27 logarithmic orientation?

There are only two outcomes.

### Outcome A — normalization closes

Then the residual is a **controlled enrichment of Layer B**, and the program should iterate:
\[
P_{n+1}\text{-residual}
\longrightarrow
\text{next 3-adic digit}.
\]
This would establish a finite filtered orientation tower without using the full Fox carrier.

### Outcome B — normalization fails intrinsically

Then the residual is genuine new filtered information but cannot be converted into the orientation scalar without an additional structure. That failure identifies the exact logical boundary.

This is now a much smaller and cleaner target than the previous 19D representation problem.

---

# Decision

\[
\boxed{
\text{mod-27 threshold residual: PASS / LOCAL}
}
\]

More precisely:

- existence/detection of the higher P_4 power residual: **PASS / LOCAL**;
- strict separation from Layer-B mod-9 information: **PASS / LOCAL**;
- projective orientation-direction identification: **CONDITIONAL / LOCAL**;
- normalized mod-27 orientation bridge: **OPEN / DECISIVE**;
- 19D \mathcal S as first new layer: **SUPERSEDED as strategic priority, not mathematically disproved**;
- all-digit finite filtered tower: **OPEN / DECISIVE**.

## Stop rule

Do not return to the 19D module or trivial-coefficient Bockstein scans.

The next attack is the **P_4 normalization/transport theorem**: prove or kill the canonical scalar bridge from the higher power residual to the already normalized mod-9 orientation direction.
