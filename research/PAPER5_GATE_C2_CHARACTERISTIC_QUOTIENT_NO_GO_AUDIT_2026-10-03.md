# PAPER 5 — GATE C2: CHARACTERISTIC-QUOTIENT NO-GO AND THE SURVIVING ORBIT CATEGORY
## 2026-10-03

### Question

Can the critical finite window (W_n), (n=p^s+1), canonically reconstruct the admissible Demuškin quotient (Q_n) by an internal characteristic/universal quotient?

### Pre-check

**Object.** A canonical reconstruction would amount to a quotient assignment (W_n\mapsto W_n/N(W_n)) with (N(W_n)) characteristic in (W_n), naturally preserved by filtered-group isomorphisms.

**Input.** Only the unmarked finite group (W_n). No chosen (z), presentation, or quotient map.

**Functoriality.** Any natural quotient assignment has characteristic kernel: every (a\in\operatorname{Aut}(W_n)) must preserve (N(W_n)).

**Gauge.** The previously proved critical orbit theorem identifies all admissible quotient maps up to (\operatorname{Aut}(W_n)\times\operatorname{Aut}(Q_n)).

**Orientation bridge.** The relative split/non-split obstruction is constant on that admissible orbit, so the obstruction already descends to the realization orbit/category.

**q-blindness.** (Q_n=D/D_n(D)) itself does not encode the stress parameter (q=p^a); the orbit-category construction is therefore q-blind at the input level.

### 1. Explicit moving-kernel family

At the minimal critical model (W_{10}), and in the general critical-window theorem, there is an admissible family
[
pi_c:W_n\twoheadrightarrow Q_n,qquad
pi_c(z)=c,quad pi_c(x_i)=\bar x_i,
]
for (c\in D_2(Q_n)), with (c\ne1) allowed.

The radical-preserving shear
[
\alpha_c(z)=zc,qquad \alpha_c(x_i)=x_i
]
is an automorphism of (W_n), and
[
pi_1\circ\alpha_c=\pi_c.
]
Hence
[
\ker\pi_c=\alpha_c^{-1}(\ker\pi_1).
]
For (c\ne1),
[
z\in\ker\pi_1,qquad
pi_c(z)=c\ne1,
]
so
[
\ker\pi_c\ne\ker\pi_1.
]

This is not merely a presentation artifact: the degree-9 (W_{10}) IA calculation independently verified the critical congruence ((zc)^9=z^9\pmod{D_{10}}), and the general orbit theorem promotes the same shear mechanism to the declared critical class.

### 2. No characteristic admissible kernel

Suppose an admissible quotient kernel (N) were characteristic in (W_n).

By the single-orbit theorem, (N) is in the same (\operatorname{Aut}(W_n))-orbit as (K=\ker\pi_1). Thus (N=a(K)) for some (a\in\operatorname{Aut}(W_n)).

Characteristicness gives (a^{-1}(N)=N), hence
[
K=a^{-1}(N)=N.
]
But (K) is not characteristic because (\alpha_c(K)=\ker\pi_c\ne K).

Contradiction.

Therefore:

[
\boxed{\text{No admissible quotient }W_n\twoheadrightarrow Q_n
\text{ has characteristic kernel.}}
]

### 3. Consequence for canonical reconstruction

Any presentation-free, isomorphism-natural quotient construction that selects (Q_n) uniquely from (W_n) would have a characteristic kernel. The preceding theorem rules this out.

This closes, for the declared critical stress family, the entire **canonical quotient / characteristic subgroup** route, not merely the specific radical-line guess.

In particular, no universal property can uniquely select the desired quotient if that universal property is internal to (W_n) and isomorphism-invariant.

### 4. What survives

The correct surviving object is not a canonical quotient but the realization groupoid
[
\mathcal R_n(W)
=
\left\{
W\twoheadrightarrow H:
H\cong Q_n
\right\}/
\bigl(\operatorname{Aut}(W)\times\operatorname{Iso}(H,Q_n)\bigr),
]
with the admissibility conditions retained.

The single-orbit theorem gives one component. The relative split/non-split Boolean is therefore constant on that component and can be attached to the component without choosing a marked map.

This is a genuine **relative intrinsic realization**: the input is the abstract (W_n), and the output does not depend on the chosen quotient map. It is not yet a fully target-free intrinsic object because the target class (Q_n) is externally prescribed.

### 5. Strong logical boundary

The result separates three notions that had previously been conflated:

1. **Canonical marked reconstruction:** impossible — **FAIL / CLOSED**.
2. **Map-independent relative obstruction:** achieved — **PASS / LOCAL** (and PASS / CLOSED once stated as the orbit-category theorem under the declared admissibility hypotheses).
3. **Fully target-free intrinsic category / coarsest realization:** still unresolved — **OPEN**.

Moreover, the failure is structural rather than computational: the obstruction is an automorphism orbit of quotient kernels. Increasing the degree or searching for another linear carrier cannot repair the absence of a characteristic representative.

### 6. Independent literature boundary

The Zassenhaus filtration is characteristic and its graded pieces are functorial under automorphisms, so filtration-based intrinsic constructions are legitimate sources of characteristic data. This does not rescue the present quotient: the desired kernel moves under an IA automorphism while the Zassenhaus filtration itself is characteristic. Thus the obstruction is specifically to selecting the Demuškin quotient kernel, not to intrinsic use of the filtered group in general.

### Classification

- characteristic/canonical admissible quotient: **FAIL / CLOSED**;
- radical-line-specific reconstruction: **FAIL / CLOSED**;
- universal-property reconstruction selecting a unique admissible quotient: **FAIL / CLOSED**;
- quotient-map realization orbit/category: **PASS / CLOSED** under the declared admissibility class;
- relative Boolean obstruction independent of the marked map: **PASS / CLOSED** under that class;
- fully target-free realization category: **OPEN / LOAD-BEARING**;
- coarsest intrinsic finite realization/minimality: **OPEN**.

### Stop

The Gate-C characteristic/universal-quotient branch is closed. No further carrier search, higher-degree scan, or canonical-kernel guess is authorized from this branch.

The remaining Paper 5 question is narrower and categorical:

> Can the admissible target class itself be characterized by a presentation-free internal property of (W_n), without selecting a characteristic kernel, so that the one-component realization groupoid becomes genuinely target-free?

If not, the mathematically correct endpoint is the relative intrinsic orbit-category theorem together with the canonical-reconstruction no-go.
