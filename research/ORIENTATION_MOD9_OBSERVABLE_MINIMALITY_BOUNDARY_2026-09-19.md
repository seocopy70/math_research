# ORIENTATION MOD-9 — OBSERVABLE-MINIMALITY BOUNDARY
## 2026-09-19

### Purpose

This document fixes the categorical ambiguity around the phrase “coarsest carrier”. The project must distinguish minimality for the **full obstruction observable** from minimality for the **single recovered orientation digit**.

### 1. Full-obstruction carrier category

Let an enriched degree-(2,3) carrier be represented by a projective/gauge class
\[
J=[(R,p)],
\]
with \(R\neq0\), modulo common nonzero scalar and the already verified bracket gauge. Its observable is the full family
\[
\Theta_J:(V^*\times V^*)\to \mathbf F_3,
\qquad
\Theta_J(\lambda,f)=f(p)+ (\lambda\wedge f)(R).
\]

Define a morphism of carriers to be admissible only when it is induced by the corresponding filtered linear change and preserves the full \(\Theta\)-family up to the common scalar coming from the chosen \(H^2\)-generator.

### 2. Injectivity

The map
\[
(R,p)\longmapsto \Theta_{(R,p)}
\]
is injective before projectivization: setting \(\lambda=0\) recovers the linear functional \(f\mapsto f(p)\), hence \(p\); subtracting that term leaves \((\lambda\wedge f)(R)\), which recovers \(R\) because \(V^*\wedge V^*\to\mathbf F_3\) separates \(\Lambda^2V\).

Therefore, after projectivization, the projective carrier is exactly the information needed to recover the full obstruction family \(\Theta\): no nontrivial quotient of this carrier can preserve every \(\Theta\)-observable.

This is a genuine minimality statement **inside the explicitly defined full-obstruction carrier category**.

### 3. Why this does not imply absolute minimality for orientation recovery

The orientation recovery uses only
\[
Z(J)=\{\lambda:\Theta_J(\lambda,-)=0\}.
\]
For nondegenerate Demuškin \(R\), the map
\[
\lambda\mapsto[(\lambda\wedge -)(R)]
\]
is an isomorphism \(V^*\to V\), so the zero set is a single point. Consequently many distinct pairs \((R,p)\) can have the same zero set. The recovered digit alone therefore admits a strictly smaller observable than the full relation jet.

Thus the projective degree-(2,3) carrier is **observable-minimal for the full twisted obstruction**, but not claimed to be minimal for the single output \(\chi\bmod9\).

### 4. Consequence for the research question

The phrase “coarsest carrier” is now frozen in two non-equivalent senses:

- **Full-obstruction minimality:** PASS / CLOSED once the naturality theorem is closed. The carrier cannot be compressed while retaining the entire \(\Theta\)-family.
- **Orientation-output minimality:** OPEN / deliberately not claimed. The zero-set/orientation digit is itself a smaller observable, and finding a natural carrier for it is a separate categorical problem.

The already established bare-graded lower bound remains: forgetting the degree-3 relation component cannot recover \(\chi\bmod9\).

### 5. Next boundary

The mod-9 branch therefore has no justification for inventing another degree-(2,3) numerical invariant. The genuinely new problem is higher order:
\[
\text{intrinsic enriched filtered data}
\longrightarrow
\chi\bmod 27,\ \chi\bmod81,\ldots
\longrightarrow\chi\in\mathbf Z_3^\times.
\]

Any higher-digit construction must pass the same four gates separately: definition, truncation/lift-independence, naturality, and recovery. No automatic “tower” is assumed.
