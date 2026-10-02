# Paper 4 — q>0 Admissible Compression Category Pre-check
## 2026-10-02

### Purpose

This document fixes the meaning of **strict intrinsic nonabelian compression** before any further computation. It is a definition/pre-check gate, not a carrier computation.

The current frontier is the finite relative extension induced by a Zassenhaus window
\[
E_n(G):\quad
1\to K_n(G)\to W_n(G)\to D_n^{\mathrm{quot}}(G)\to1,
\]
where
\[
W_n(G)=G/D_n(G),\qquad
K_n(G)=N/(N\cap D_n(G)),\qquad
D_n^{\mathrm{quot}}(G)=D/D_n(D).
\]
The full relative extension is already classified as **PASS / LOCAL** as an intrinsic object but **FAIL / CLOSED** as a novel carrier because it re-encodes the finite window.

The authorized question is therefore whether a strictly smaller, intrinsic quotient of this object can retain deep nonabelian relation information.

---

## 1. Admissible category

Fix a finite depth \(n\). Let \(\mathcal E_n\) be the category whose objects are finite relative extensions
\[
E=(1\to K\to W\xrightarrow{\pi}D_n\to1)
\]
arising functorially from extensions \(1\to N\to G\to D\to1\) and the depth-\(n\) Zassenhaus window, with the quotient map \(\pi\) retained as structure.

Morphisms in \(\mathcal E_n\) are commutative extension morphisms induced by morphisms of the underlying structured free-by-Demushkin extensions and compatible with the filtration.

An **admissible compression** at depth \(n\) is a functor
\[
C_n:\mathcal E_n\longrightarrow\mathcal I_n
\]
together with a natural surjection/quotient map
\[
c_E:E\twoheadrightarrow C_n(E)
\]
in a specified target category \(\mathcal I_n\), satisfying the conditions below.

### A1. Intrinsicity

The definition of \(C_n(E)\) uses only the structured finite relative extension \(E_n(G)\), not:
- a presentation;
- a chosen relator;
- a chosen lift or section;
- Fox/Magnus coordinates;
- a preferred generator;
- the orientation character \(\chi\);
- the numerical q-parameter.

Any isomorphic objects of \(\mathcal E_n\) receive isomorphic compressed objects.

### A2. Functoriality

Every admissible morphism \(E\to E'\) induces a canonical morphism
\[
C_n(E)\to C_n(E').
\]
No choice-dependent identification is allowed.

### A3. Gauge invariance

All presentation/lift gauges that induce the same structured finite relative extension must act trivially on the compressed isomorphism class.

In particular, the construction must survive relator replacement, lift/section changes, conjugation, Nielsen changes, unit rescaling of cyclic generators, and compatible kernel/quotient automorphisms.

A scalar extracted before passing to the corresponding orbit is not admissible.

### A4. q-blindness

The construction of \(C_n\) may not contain q, a, or any equivalent quotient-specific torsion parameter as an input.

q may occur only in the external stress test used to determine whether the q-blind object separates examples.

### A5. Orientation-blind input

The construction may not use the orientation character \(\chi\), its values, or a crossed-derivation coordinate system as input.

The orientation bridge is a separate theorem obligation:
\[
C_n(E)\longrightarrow \text{target orientation data}.
\]

### A6. Strictness

The compression must actually discard information. This is stronger than merely replacing E by an isomorphic encoding.

Operationally, on the declared stress/test class there must exist \(E\not\cong E'\) such that
\[
C_n(E)\cong C_n(E').
\]
Equivalently, \(C_n\) is not injective on isomorphism classes.

A proper quotient with a reversible reconstruction is therefore not a strict compression.

### A7. Non-reencoding

A construction fails novelty if \(C_n(E)\) determines \(E\) up to isomorphism on the relevant class, even when it is presented as a scalar, module, orbit, or other repackaging.

Thus “smaller notation” is insufficient. The test is information-theoretic at the level of isomorphism classes.

### A8. Filtration compatibility

If the candidate uses several depths, the maps
\[
C_n(E)\to C_{n+1}(E)
\]
must be induced functorially by the natural finite-window maps. No new presentation data may be inserted when passing between depths.

---

## 2. Deep-relation target

There are two logically distinct targets and they must not be conflated.

### T1. Weak target: threshold detection

For the q>0 stress family, fix an external threshold m>a. Require one finite depth n=n(m), chosen independently of the hidden tail parameter s, such that the compression distinguishes the two classes s<m and s>=m. The threshold m belongs only to the external stress test, not to the definition of the compression.

This is deliberately weaker than recovering the exact value of s. It also avoids the previous finite-range formulation, which was effectively equivalent to recovering a truncated parameter by a finite lookup table.

### T2. Strong target: truncated depth recovery

For fixed \(m>a\), define on this stress family the benchmark
\[
T_m(G_{s,a})=\min(s,m).
\]
A positive result would require a natural reconstruction statement for \(T_m\), without putting \(a\), \(s\), or \(\chi\) into the definition of \(C_n\).

T2 is strictly stronger than T1.

The benchmark parameter \(a\) belongs only to the external stress family. q-blindness applies to the definition of the compression, not to the choice of a test family used to challenge it.

**Default target for the next gate is T1.** We should not demand exact s until a nontrivial strict compression survives T1.

---

## 3. Separation / no-reencoding test

For a proposed \(C_n\), run two independent tests.

### S1. Target separation

Find a certified pair in the stress class with different deep-tail target values but
\[
C_n(E_n(G))\not\cong C_n(E_n(G')).
\]

This is only a positive separation result.

### S2. Non-reencoding

Find a certified pair
\[
E\not\cong E'
\quad\text{with}\quad
C_n(E)\cong C_n(E').
\]
If no such pair exists on the declared admissible class, the construction is not a strict compression; it is a faithful re-encoding and fails the novelty requirement.

The two tests are independent: a quotient may separate the target while still faithfully encoding the whole window.

---

## 4. Minimal admissible category

We do **not** claim absolute minimality among all conceivable invariant categories.

The admissible category for this stage is explicitly:

> finite relative Zassenhaus extensions with extension-compatible morphisms, and compressions given by functorial quotient constructions that are intrinsic, q-blind, orientation-blind, gauge-invariant, filtration-compatible, and non-reconstructive.

Minimality, if later claimed, is only relative to this category.

---

## 5. Gate decision rules

### PASS / LOCAL
A candidate passes definition if A1–A8 are satisfied, but target separation has not yet been established.

### PASS / CLOSED
A candidate satisfies A1–A8 and yields a proven natural factorization/separation theorem at the declared target.

### FAIL / CLOSED
Any of the following is proved:
- q/orientation is inserted into the definition;
- gauge dependence remains;
- the construction is only a presentation coefficient;
- it is not functorial;
- it is only a re-encoding of the full finite relative extension;
- it cannot separate the declared deep-tail benchmark.

### OPEN
A precisely defined candidate satisfies the admissibility conditions but its separation/factorization theorem is unresolved.

### STOP
Do not compute a candidate before A1–A8 have been checked. In particular, raw Fox/Magnus coefficients are not admissible merely because they occur naturally in a presentation.

---

## 6. Immediate consequence for Paper 4

The phrase “strict intrinsic nonabelian compression” is now mathematically operational.

The next authorized computation, if any, must begin with a **specific quotient construction**
\[
E_n\mapsto C_n(E_n)
\]
and a proof of A1–A8.

The first target is **T1 deep-tail separation**, not exact recovery of s.

If the first nontrivial admissible quotient that can plausibly carry the relation defect fails S1 or violates A1–A8, that is evidence toward a structural no-compression theorem. It is not by itself such a theorem.

No raw Magnus/Fox scalar computation is authorized before a candidate quotient and its gauge orbit are fixed.

### Current classification

- admissible compression category: **PASS / LOCAL**
- T1 threshold-detection target: **DEFINED / CORRECTED AGAIN**
- T2 exact truncated-depth target: **DEFINED / SECONDARY**
- existence of a strict intrinsic compression: **OPEN / LOAD-BEARING**
- universal no-compression theorem: **OPEN**
- carrier hunt without category definition: **STOP / CLOSED**


## 7. First concrete admissible quotient candidate: relative class-2 kernel quotient

The first authorized candidate is
\[
C_n^{(2)}(E_n):\quad
1\to K_n/\gamma_3(K_n)\to W_n/\gamma_3(K_n)\to D/D_n(D)\to1,
\]
where
\[
K_n=N/(N\cap D_n(G)),\qquad W_n=G/D_n(G).
\]
Equivalently, quotient the finite relative extension by the third lower-central subgroup of its kernel.

### A1–A8 pre-check

- **A1 Intrinsicity: PASS / LOCAL.** The lower-central subgroup \(\gamma_3(K_n)\) is characteristic/functorial in \(K_n\); no presentation, relator, lift, q, or orientation enters the definition.
- **A2 Functoriality: PASS / LOCAL.** Homomorphisms preserve the lower-central series, so extension morphisms induce maps on the quotient. This is standard for lower-central quotients. See Hamza 2023 for the role of lower-central/Zassenhaus filtrations in pro-p modules. 
- **A3 Gauge invariance: PASS / LOCAL.** Presentation/lift changes that induce the same structured finite extension cannot change its characteristic subgroup quotient.
- **A4 q-blindness: PASS.**
- **A5 orientation-blind input: PASS.**
- **A6 strictness: OPEN.** Strictness must be witnessed on the declared relevant test class; it cannot be certified merely by observing that a class-2 quotient is formally smaller.
- **A7 non-reencoding: OPEN.** It is a proper quotient construction, but it has not yet been proved that it does not reconstruct the full finite relative extension on the relevant class.
- **A8 filtration compatibility: PASS / LOCAL.** The natural maps \(W_{n+1}\to W_n\) restrict to kernel maps and preserve lower-central subgroups.

### Why this candidate is genuinely new relative to the closed E2 layer

The class-2 quotient retains the D-action on
\[
K_n/\gamma_3(K_n)
\]
and the commutator pairing
\[
(K_n/K_n')\times(K_n/K_n')\to K_n'/\gamma_3(K_n),
\]
whereas the closed E2/H1 layer retains only the corresponding abelianized kernel extension/coinvariant information.

Therefore it is not automatically identical to the previously closed \(H_1\)-extension layer. This is a structural distinction, not yet a separation theorem.

### T1 status

The candidate has **not** yet been shown to detect the q>0 deep-tail threshold \(s\ge m\). In particular, the ordinary mod-p associated-graded blindness does not by itself decide the integral class-2 quotient: the latter retains extension-level integral p-power information discarded by the mod-p graded object.

Hence:
\[
\boxed{C_n^{(2)}\text{ is OPEN / LOAD-BEARING, not PASS.}}
\]

### Stop boundary

Do not immediately expand \(C_n^{(2)}\) in raw Magnus/Fox coordinates. First determine its gauge-orbit invariant content and whether the class-2 kernel quotient can distinguish the threshold \(s\ge m\). If its only surviving data factors through the already closed abelian/E2/graded layers, close it. Otherwise it becomes the first genuine nonabelian compression candidate.
