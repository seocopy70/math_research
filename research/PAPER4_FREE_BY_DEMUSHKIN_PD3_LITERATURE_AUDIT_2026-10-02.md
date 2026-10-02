# PAPER 4 — FREE-BY-DEMUSHKIN / PD^3 LITERATURE AUDIT — 2026-10-02

## Source

M. Palaisti, *Detecting Cohomological Dimension Three in Free-by-Demuškin Pro-p Groups*, arXiv:2610.00021v1, submitted 2026-08-31.

Primary source checked: arXiv abstract and full HTML, including Sections 1–10.

## Executive classification

**PASS / LOCAL — literature mechanism is real and highly relevant, but it does not yet provide the proposed finite-window recognition theorem.**

The paper is a genuine structural bridge from a free-by-Demuškin extension to first-Frattini-module data and, in its lower-dimensional branch, to a relation-defect class. It does **not** itself show that these objects factor through a finite filtered window of the middle group, nor that the orientation of the Demuškin quotient is recoverable from such a window.

The proposed “PD3 extension” direction therefore survives only after a scope correction:

- free-by-Demuškin extensions with finite-rank free kernel: **KNOWN structural setting; cd_p G=3**;
- middle group itself a pro-p PD^3 group: the paper proves that the free kernel must be **rank one**, so a general finite-rank PD3 free kernel is not an available target;
- arbitrary PD^n quotient with free kernel: the paper proves the top-degree fixed-Frattini mechanism formally;
- finite-window reconstruction of quotient orientation / extension data: **OPEN**.

## 1. What the paper actually proves

For
\[
1\to N\to G\to D\to1,
\]
with N nontrivial free pro-p and D Demuškin, put
\[
W=N/\Phi(N).
\]

The central theorem is
\[
H^3(G,\mathbf F_p)^\vee\simeq W^D,
\]
hence
\[
\operatorname{cd}_pG=3\iff W^D\neq0.
\]

The proof uses the Hochschild–Serre spectral sequence and Demuškin top-degree duality. The top-degree term is
\[
E_2^{2,1}=H^2(D,H^1(N,\mathbf F_p)),
\]
and no differential can alter it. Demuškin duality then identifies its dual with the D-fixed part of W.

This is exactly a “PD2 engine lifted through a free extension”: the one-dimensional top cohomology of D converts a module-valued top-degree term into a fixed-point object.

## 2. Relation to our U1–U5 engine

The analogy is real but not literal.

### U1–U2

Our U1–U2 machinery proves that arbitrary twisted coefficient cocycles for an arbitrary candidate orientation factor through a specific finite Zassenhaus quotient. That is a **finite-input factorization statement**.

Palaisti's theorem instead starts from the full extension
\[
(N,G,D)
\]
and extracts the first Frattini module W and its D-action. No finite Zassenhaus factorization is proved.

**Therefore:** the paper supplies the target-side structural object, not our finite-window bridge.

### U3

Our U3 converts finite Kummer lifting into a one-relator/Fox obstruction.

Palaisti's lower-dimensional analysis also reaches an H^2 obstruction, but through the Hochschild–Serre transgression. The relation defect
\[
\delta_G\in W_D
\]
is dual to the transgression and, for a minimal one-relator presentation of D, is represented by a lift of the defining Demuškin relation.

This is a strong methodological match with our relation-module/Fox viewpoint, but it is not the same finite object.

### U4

Our U4 is a presentation-local coordinate identification of the canonical orientation.

Palaisti does not reconstruct the Demuškin orientation from the extension. The Demuškin quotient D is already given as a Demuškin group; its orientation/duality structure is used as background.

### U5

Our U5 uses PD^2 duality plus cup-product nondegeneracy to force uniqueness of the next orientation digit.

Palaisti uses Demuškin top-degree duality to identify H^3 with W^D and, in the lower-dimensional branch, uses transgression/coinvariants. The same duality engine is present, but the target is different: fixed Frattini data and relation defect, not orientation digits.

**Conclusion:** the paper confirms that the project should preserve the PD-duality engine while changing the extension object. It does not show that U1–U5 automatically extend.

## 3. Critical correction: “PD3 free-by-Demuškin” is too broad

The paper's Section 6.2 is decisive.

If N is finitely generated free pro-p, D is Demuškin, and G itself is a pro-p PD^3 group, then
\[
N\simeq\mathbf Z_p.
\]

Thus the proposed target cannot be “general PD3 free-by-Demuškin groups with arbitrary finite-rank free kernel.” Under the PD^3 hypothesis on G, the free kernel is forced to rank one.

This is not a minor technicality. It changes the research object.

The viable formulations are instead:

1. **free-by-Demuškin, cd_p G=3**, without assuming G is PD^3; or
2. **the rank-one PD^3 subfamily**, where N≅Z_p.

The first is broader and preserves the paper's main theorem. The second is structurally tighter but risks becoming a classification/extension problem rather than a direct U1–U5 continuation.

## 4. The relation-module/Fox connection is genuine — but localized

The paper's Lemma 7.2 is particularly relevant.

For a minimal one-relator presentation
\[
1\to R\to F\to D\to1,
\qquad R=\overline{\langle\!\langle r\rangle\!\rangle},
\]
a choice of lifts F→G sends r to w∈N. The dual transgression is represented by
\[
\delta_G=\overline w\in W_D,
\]
up to nonzero scalar normalization.

The proof explicitly uses the relation module
\[
R/R^p[R,F]
\]
and its perfect pairing with invariant H^1(R,F_p), followed by naturality of the five-term sequence.

This is the strongest direct point of contact with our U3 relation/Fox machinery.

But it is important that this occurs in **Section 7, the lower-dimensional branch**. The main cd=3 detector does not require the relation module or Fox calculation; it is already settled by W^D.

Hence:

- “relation module/Fox ideas reappear”: **PASS / LOCAL**;
- “the paper's main theorem is essentially our U3”: **FAIL / CLOSED**;
- “Lemma 7.2 is a promising bridge for a successor finite-window theorem”: **OPEN / LOAD-BEARING candidate**.

## 5. The strongest genuinely new ingredient for us

The most useful structural decomposition is

\[
\boxed{
W^D
\quad\text{(top-degree obstruction)}
}
\]

versus

\[
\boxed{
H^1(D,W^\vee),\;\delta_G\in W_D
\quad\text{(lower-dimensional extension data)}.
}
\]

The paper explicitly separates the top-degree fixed-point mechanism from the transgression/coinvariant mechanism.

This gives a much cleaner successor architecture than the RAAG carrier hunt:

\[
\text{finite window of }G
\longrightarrow
\text{finite approximation of }W^D
\text{ and/or }W_D,\delta_G
\longrightarrow
\text{D-orientation data}.
\]

The first arrow is the genuinely unresolved one.

## 6. PD^n generalization

The paper also proves the formal extension:

If
\[
1\to N\to G\to Q\to1
\]
has N nontrivial free pro-p and Q a pro-p Poincaré-duality group of dimension n, then
\[
H^{n+1}(G,\mathbf F_p)^\vee
\simeq
(N/\Phi(N))^Q,
\]
hence
\[
\operatorname{cd}_pG=n+1
\iff
(N/\Phi(N))^Q\neq0.
\]

This is mathematically important for the project's longer-term map: the fixed-Frattini top-degree mechanism is not peculiar to dimension two.

However, it is still a theorem about the **full extension**, not a finite-window theorem.

## 7. Pre-check for the proposed finite-window successor

### Object

Candidate intrinsic target:
\[
\mathcal E(G,N,D)=
\bigl(W=N/\Phi(N),\;D\curvearrowright W,\;W_D,\;\delta_G\bigr).
\]

**PASS / LOCAL** as an object attached to a specified extension.

### Input

If the input is the full extension (G,N,D), it is well-defined.

If the input is only an un-oriented finite window of G, the recovery of N and D is not yet specified.

**OPEN / LOAD-BEARING.**

### Functoriality

The constructions W^D, W_D and the transgression are natural for the relevant extension maps.

**PASS / LOCAL.**

### Gauge

W=N/Φ(N) is intrinsic once N is fixed. The class δ_G is only defined up to nonzero scalar because the top H^2(D,F_p) is one-dimensional.

**PASS / LOCAL.**

### Orientation bridge

No finite scalar map from the above data to χ_D mod p^k is given by the paper.

**OPEN / LOAD-BEARING.**

### q-blindness

The paper's definitions do not insert the numerical q of a Demuškin presentation. This is compatible with our q-blindness requirement.

But q-blindness alone is insufficient; the finite factorization must still be proved.

**PASS / LOCAL.**

### Separation

The fixed-point object W^D detects cd=3 versus ≤2. It does not by itself distinguish the orientation digits of D.

**OPEN / LOAD-BEARING.**

### Novelty

The full-extension structural theorem is prior art once cited.

The potentially novel target is the **finite-window factorization/reconstruction** of the relevant extension/orientation data.

**CONDITIONAL.**

### Stop

Do not compute a carrier until the finite input has been specified precisely.

**STOP CONDITION: active.**

## 8. Recommended next theorem — corrected

The next target should not be:

> “Finite-window recognition of PD^3 free-by-Demuškin groups.”

That formulation is structurally misleading because PD^3 forces N≅Z_p.

The cleaner target is:

> **Finite-window detection/reconstruction for free-by-Demuškin extensions:** determine whether a finite filtered quotient of G canonically determines a finite-level quotient of the Demuškin orientation and/or the extension defect represented by W^D, W_D and δ_G, under explicitly stated hypotheses on N and the extension.

A particularly controlled first subproblem is:

\[
\boxed{
W=N/\Phi(N)
\quad\text{and}\quad
\delta_G\in W_D
\text{ from a finite window}
}
\]

before attempting the full orientation.

If that finite recovery fails, stop. If it succeeds, then ask whether the recovered D-side data can feed the existing U1–U5 selector.

## 9. Independent verification / boundary

The paper itself states in its Further Questions that the realizability constraints on W, W^D, H^1(D,W^∨), and δ_G are not completely classified. Therefore these objects should not be treated as already-canonical finite carriers for arbitrary extensions.

The paper is best used as a **structural source and target specification**, not as a ready-made successor theorem.

## Final classification

**PASS / LOCAL — strong literature bridge confirmed.**

- Literature mechanism: **PASS / CLOSED**.
- Relation-module/Fox contact: **PASS / LOCAL**.
- Direct extension of U1–U5: **FAIL / CLOSED as an automatic inference**.
- General finite-window reconstruction: **OPEN / LOAD-BEARING**.
- PD^3 middle-group branch with arbitrary free rank: **CLOSED by rank-one restriction**.
- Free-by-Demuškin cd=3 finite-window successor: **OPEN / CONDITIONAL**.
- RAAG carrier hunt: **HOLD / SUPPRESSED while this branch is tested**.

## Immediate next authorized action

Do not invent a new carrier.

First derive, from the finite-window definitions already used in Paper 1–3, the **smallest finite approximation of the extension data** that could recover either W^D or δ_G. This must pass the full continuity pre-check before computation.
