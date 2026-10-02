# TOP-DOWN T0 AUDIT — CORRECTION AFTER TARGET DEFINITION REVIEW — 2026-10-02

## 0. Decision

The previous draft that closed T0 for the standard Demuškin family is **SUPERSEDED / INVALID**.

The error was substantive: it identified a presentation-level crossed-derivation value
\[
\theta(x_2)=(1-q)^{-1}
\]
with the intrinsic Demuškin orientation/cyclotomic character itself, without proving that identification.

Therefore the earlier conclusion
\[
W_k(G)\cong W_k(H)\Rightarrow\chi_k(G)=\chi_k(H)
\]
has **not** been established, even in the standard odd-p fixed-rank Demuškin family.

## 1. What survives

The top-down gate itself is correct.

For a declared target \(T_k\) and finite input \(W_k\), define
\[
I_k(w)=\{[T_k(G)]:W_k(G)\cong w\}.
\]
If some window has more than one target value, then no carrier whose isomorphism class is determined solely by \(W_k\) can recover the target.

Equivalently, a same-window/different-target pair gives a carrier-independent no-go theorem.

The target must be fixed before this test.

## 2. Target-definition gate is now mandatory

The project must distinguish:

1. **Demuškin orientation** \(\chi_G\): the intrinsic orientation attached to the abstract oriented Demuškin structure;
2. **cyclotomic character/orientation** when G is realized as a relevant Galois group;
3. **Labute's crossed-derivation/coefficient twist parameter** \(\theta\).

These may be related in the standard arithmetic setting, but the relation is not allowed to be assumed.

In particular, the formula
\[
\theta(x_2)=(1-q)^{-1}
\]
for a chosen standard presentation is not, by itself, a formula for the intrinsic \(\chi_G\).

The top-down target is therefore not yet formally fixed enough for a T0 closure.

## 3. Corrected Demuškin q-regime statement

The following algebraic fact remains valid:

\[
N_k=p^{k-1}+1.
\]
For q=p^s with s\ge k,
\[
q=p^s>N_k.
\]
Thus the q-power term in the standard Demuškin relator is beyond the declared Zassenhaus precision.

Also
\[
q\equiv0\pmod{p^k}
\]
and hence
\[
(1-q)^{-1}\equiv1\pmod{p^k}.
\]

But the latter statement concerns the scalar \((1-q)^{-1}\), not automatically the intrinsic orientation character. It therefore cannot close T0.

Similarly, the assertion that \(q=p^k\) and \(q=p^{k+1}\) have the same finite-level orientation is **unproved** until the target-definition/identification theorem is supplied.

## 4. Broad-category correction

The earlier \(C_9\times C_3\) versus exponent-3 Heisenberg example proves only that a broad finite pair can fail to determine the extension object:
\[
(Q,A)\not\Rightarrow[E].
\]

It is not a counterexample to
\[
W_k\not\Rightarrow\chi_k.
\]
No orientation difference was established there.

Therefore the correct status is:
- broad extension reconstruction: **FAIL / CLOSED**;
- broad orientation identifiability: **OPEN / NOT PROVED**.

## 5. Observability depth correction

Define, once the target is fixed,
\[
d_{obs}(T;W)=\min\{k:T_k\text{ factors through }W_k\}.
\]

No monotonicity theorem follows from Zassenhaus functoriality alone.

If
\[
\tau_{k+1,k}:W_{k+1}\to W_k
\]
is truncation, factorization at one level does not automatically imply factorization at another. Cross-level compatibility of both the target system and the finite inputs must be proved separately.

Thus:
- observability depth as a definition: **OPEN**;
- monotonicity: **OPEN**;
- automatic monotonicity from filtration functoriality: **FAIL / CLOSED**.

## 6. Immediate next gate

The next authorized gate is now:

### T−1 — Target identification

Fix exactly what \(\chi_k\) means in the current research program, in a basis-free/intrinsic form.

Then prove or cite, with exact hypotheses, any identification among:
\[
\text{Demuškin orientation}
\leftrightarrow
\text{cyclotomic orientation}
\leftrightarrow
\text{Labute coefficient twist}.
\]

Only after T−1 is closed may the finite-window T0 test be resumed.

### T0 — Orientation identifiability

After T−1:
\[
W_k(G)\cong W_k(H)
\Rightarrow
[\chi_k(G)]=[\chi_k(H)]?
\]

Possible outcomes:
- explicit same-window/different-target pair: **FAIL / CLOSED**;
- structural proof of constancy: **PASS / CLOSED**;
- neither: **OPEN**.

No new carrier construction is authorized before T0.

## 7. Relation to existing literature gate

The repository's literature audit already establishes an important boundary:

- Labute gives a full-group crossed-derivation/Kummerian criterion.
- Efrat–Quadrelli gives uniqueness of the Kummerian orientation for torsion-free Demuškin groups.
- Quadrelli–Weigel gives cyclotomic/dualizing orientation results.
- None of those audited results, by themselves, proves the project's finite-window factorization
\[
\chi_k=\Phi_k\circ W_k.
\]

Therefore the target-definition gate is not a demand to rediscover the existence of Demuškin orientation. It is a demand to identify precisely which established orientation object the finite-window program is attempting to recover.

## Classification

- Top-down carrier-independent no-go lemma: **PASS / CLOSED**.
- \(I_k(w)\) identifiability criterion: **PASS / CLOSED**.
- Previous T0 PASS for standard Demuškin family: **HISTORICAL / SUPERSEDED — invalid inference**.
- T−1 target identification: **OPEN / LOAD-BEARING**.
- T0 finite-window orientation identifiability: **OPEN / LOAD-BEARING**.
- Broad extension reconstruction no-go: **FAIL / CLOSED**.
- Broad orientation no-go: **OPEN / NOT PROVED**.
- Observability-depth monotonicity: **OPEN**.
- New carrier construction before T−1/T0: **NOT AUTHORIZED**.

## Audit rule

No future use of
\[
\theta(x_2)=(1-q)^{-1}
\]
may be promoted to a statement about \(\chi_G\) without an explicit theorem connecting the two notions under the exact declared category and target convention.
