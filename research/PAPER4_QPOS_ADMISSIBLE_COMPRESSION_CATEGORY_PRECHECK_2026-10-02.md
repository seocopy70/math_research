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

Operationally, on the admissible test class there must exist \(E\not\cong E'\) such that
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

### T1. Weak target: deep-tail separation

For the q>0 stress family
\[
G_{s,a}=\langle z,x_1,\ldots,x_d\mid z^{p^s}=r_D\rangle,
\qquad q_D=p^a,
\]
the weak target must still be a **uniform finite-depth target on a declared finite test range**. For a fixed benchmark depth parameter \(m>a\), require a single depth bound \(n=n(m)\), independent of the hidden tail parameter \(s\), such that the compressed windows separate the distinct deep-tail values in the declared range
\[
a<s,t\le m.
\]
Equivalently, the target is not pairwise “some \(n(s,t)\)” separation; it is separation through one finite level chosen before seeing the particular pair.

This prevents T1 from collapsing into the tautological fact that the full inverse system may eventually separate individual examples.

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
- T1 uniform finite-depth separation target: **DEFINED / CORRECTED**
- T2 exact truncated-depth target: **DEFINED / SECONDARY**
- existence of a strict intrinsic compression: **OPEN / LOAD-BEARING**
- universal no-compression theorem: **OPEN**
- carrier hunt without category definition: **STOP / CLOSED**
