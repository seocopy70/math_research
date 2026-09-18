# PLAN-O2 — Transport-Intrinsic Obstruction

> **Role:** Current active plan for the O2 transport-intrinsic research track.
>
> **Authority:** This file specifies the current O2 question and experiment sequence. Current mathematical state is authoritative in \`RESEARCH_MAP.md\`; calculation conventions are authoritative in \`research/03_CONVENTIONS_AND_IMPLEMENTATION.md\`.

## 1. Global position

A3-4 provenance audit is closed. O2-2 and O2-3 are verified. For a fixed admissible transport \(\tau\),
\[
O_\tau=\operatorname{Im}D_\tau,\qquad
\ker D_\tau=I=\ker N,
\]
and the fixed-\(\tau\) obstruction is a verified 10-dimensional \(H\)-module isomorphic to
\[
U=\operatorname{im}N.
\]

O2-4 then showed that the absolute image \(O_\tau\) is not independent of the admissible B1 transport choice.

O2-5/O2-6 shifted the object of study from the absolute obstruction to its affine transport-variation direction
\[
\Delta D=D_1-D_0,\qquad \Delta O=\operatorname{Im}\Delta D,
\]
which is 10-dimensional, \(H\)-stable, and basepoint-independent within the complete verified B1 family.

## 2. Purpose

Determine whether the 10-dimensional variation module \(\Delta O\), or an equivalent structure extracted from it, is forced by the filtered/graded data rather than by the auxiliary transport \(\tau\).

The target is **not** merely another dimension-10 coincidence. The required endpoint is a construction or identification whose dependence on admissible auxiliary choices has been exhausted and whose inputs are intrinsic to the filtered structure.

## 3. Dependencies

Frozen/verified inputs:

- A3-4 corrected artifact: commit \`62886877f97e58e87d59b0075d45e38be6176410\`.
- O2-2: run \`35278644641\`, job \`105395199074\`.
- O2-3: run \`35279936962\`, job \`105399291836\`.
- O2-4: run \`35281594800\`.
- O2-5: run \`35283099072\`, job \`105409292646\`.
- O2-6: run \`35284130822\`, job \`105412565419\`.
- Complete H-orbit closure is an explicit invariant in \`research/03_CONVENTIONS_AND_IMPLEMENTATION.md\`.

The historical tuple-action archaeology is not a dependency.

## 4. Experiment protocol

Before each new experiment record:

1. global position;
2. exact purpose;
3. dependencies and authoritative artifacts;
4. coordinate/action conventions;
5. complete H-closure method where an orbit/submodule is used;
6. decision criterion;
7. PASS/FAIL/INVALID TEST consequences.

Do not execute a new calculation until these are explicit.

## 5. Current gate

\[
\boxed{\text{Is }\Delta O\text{ determined intrinsically by the filtered/graded structure?}}
\]

### PASS consequence

A transport-independent construction is identified, with complete admissible-choice coverage and verified \(H\)-equivariance/intrinsic input dependence. Then proceed to the independent q=3 versus q=\(\infty\) comparison.

### FAIL consequence

If the candidate still changes under an admissible choice not already exhausted, the candidate is not yet an intrinsic invariant. Do not infer q=3/q=\(\infty\) distinction or orientation recovery from it.

### INVALID TEST consequence

If coordinate systems, field arithmetic, H-closure, stale artifacts, or admissibility conditions are wrong/incomplete, discard the mathematical interpretation and repair/re-run. Do not label the result a mathematical failure.

## 6. Completed O2 checkpoints

- **O2-4:** absolute \(O_\tau\) transport-independence — FAIL.
- **O2-5:** affine variation \(\Delta O\) is 10D and H-stable — PASS.
- **O2-6:** variation direction is basepoint-independent within complete B1 family — PASS.
- **O2-7/O2-8:** q=3 p-power class has complete H-orbit shadow equal to \(U\) — corrected/verified, but not yet a q=3 versus q=\(\infty\) proof.

## 7. Parallel track boundary

Q3-5/Gate0A q=3 versus q=\(\infty\) reconstruction is a separate parallel track. It may consume frozen O2 artifacts when explicitly cited, but its own reconstruction and validation are independent. It must not silently replace an unresolved O2 intrinsicity gate.

## 8. Exit condition

The O2 track is complete only when either:

- a filtration-intrinsic transport-free invariant is verified; or
- the obstruction route is shown not to yield such an invariant under the exhausted admissible choices, with the failure recorded precisely.

Only then should the project choose the next mathematical route toward q-distinction and \(\chi\).


## 8. O2-9(pre) — COMPLETE

O2-9(pre) confirmed
[
\Phi_0\circ F=I_U
]
exactly as a full (10\times10) matrix (Actions run `35320678550`). This closes the compatibility pre-check between O2-7 and O2-8.

## 9. O2-9 — FULL AUT_H(W) TRANSPORT COVERAGE

### Global position

O2-4 showed that (O_\tau) is not invariant over the three previously tested (a=1) B1-admissible transports. O2-5/O2-6 isolated the 10D variation module. O2-7/O2-8/O2-9(pre) identify that variation with (U=\operatorname{im}N) in a mutually compatible way.

### Purpose

Exhaust the entire admissible (H)-equivariant transport torsor, rather than only (\tau(I+bN)) for (b=0,1,2).

### Exact coverage

Since
[
\operatorname{End}_H(W)=\mathbb F_3[I,N],quad N^2=0,
]
the unit group is exactly
[
\{aI+bN:a\in\mathbb F_3^\times,b\in\mathbb F_3\},
]
with six elements. Because (\tau:W\to W_d) is an (H)-isomorphism, composition with (\tau^{-1}) identifies (\operatorname{Hom}_H(W,W_d)) with (\operatorname{End}_H(W)), so
[
\dim\operatorname{Hom}_H(W,W_d)=2.
]
The experiment records this explicitly and constructs the two independent Hom maps (\tau) and (\tau N).

### Affine formula protocol

For the actual affine obstruction definition,
[
D(S)=D_{\mathrm{linear}}(S)-D_{\mathrm{linear}}(I),
]
the exact formula is
[
D_{a,b}=aD_0+b\Delta D+(a-1)D_{\mathrm{linear}}(I).
]
The simplified relation (D_{a,b}=aD_0+b\Delta D) is therefore treated as a testable special case, not as an assumption.

### Decision criteria

**PASS for exhaustive coverage:** all six unit transports are verified H-equivariant, and the six-element parameterization is confirmed complete.

**Canonicality outcome:** inspect whether the six obstruction images collapse to an invariant 20D structure or whether additional variation appears. Equality of the six absolute images is not expected and is not the criterion, because O2-4 already established absolute transport dependence.

**FAIL:** an additional admissible transport outside the six-element family is found, or the candidate structure changes under one of the six and no transport-independent replacement is identified.

**INVALID TEST:** any failure of coordinate/action conventions, Hom-space construction, unit parameterization, or affine identity verification.
