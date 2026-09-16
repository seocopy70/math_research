# A3-4 W_d revalidation against the true relation space — 2026-09-16

## 1. Purpose

The earlier A3-4-4/A3-4-5 calculations were performed while the degree-4 relation space had been confused with the 5-dimensional subspace `[L2,R]`. The correct recursive relation space is

\[
(R)_4^{true}=[L_1,(R)_3],\qquad \dim (R)_4^{true}=15.
\]

The present check reconstructs

\[
W_d=\langle Sp_4(\mathbb F_3)\cdot d\rangle,
\qquad d=[X_1^{[3]},X_2],
\]

in the common degree-4 ambient coordinates and tests it directly against `(R)_4^{true}`.

## 2. Independent construction

- The relator is reconstructed from the corrected Phase 2-1 infrastructure.
- `(R)_4` is obtained recursively, not from `[L2,R]`.
- The full `Sp4(F3)` orbit of `d` is generated using the same five generators used in A3-4-4.
- All vectors are embedded in the 256-dimensional associative degree-4 word space.
- Rank and intersection computations are performed over `F_3`.
- No old 55-dimensional quotient is used in the gate.

The defining vector is checked independently:

\[
d=[X_1^{[3]},X_2]=[[[X_1,X_2],X_1],X_1]\ne0.
\]

## 3. CI verification

Workflow: `.github/workflows/a3-4-wd-true-relation.yml`

Script: `research/A3-4-REVALIDATION_Wd_TRUE_RELATION_2026-09-16.py`

Commit: `6c32980a8b49b45a06d1ab960fc9694ad18bf721`

GitHub Actions run: `35067892176`

Job: `104702271616`

Status: **success**. The complete gate executed successfully. fileciteturn113file0L2-L2

## 4. Results

The successful assertions establish the following exact values:

\[
\dim (R)_4^{true}=15,
\]

\[
\dim W_d=45,
\]

and

\[
\boxed{\dim(W_d\cap(R)_4^{true})=0}.
\]

Therefore the true quotient projection

\[
\pi:L_4\to Q_4^{true}=L_4/(R)_4^{true}
\]

is injective on `W_d`, so

\[
\boxed{\dim\pi(W_d)=45}.
\]

Since

\[
\dim Q_4^{true}=60-15=45,
\]

we obtain

\[
\boxed{\pi(W_d)=Q_4^{true}}.
\]

The same run confirms the already established W45 facts:

\[
\dim W_{45}=45,
\qquad
\dim\pi(W_{45})=45.
\]

The ambient intersection remains

\[
\boxed{\dim(W_{45}\cap W_d)=35}.
\]

Finally,

\[
\dim\pi(W_{45}+W_d)=45.
\]

## 5. What is now established

### Gate A — W_d survives the corrected relation layer

**PASSED.**

\[
W_d\cap(R)_4^{true}=0.
\]

Thus the old W_d construction is not merely an artifact of the old quotient: its ambient degree-4 subspace survives the corrected relation layer and projects injectively to the true quotient.

### Gate B — W_d is another full representative of Q4_true

**PASSED.**

Because both `W_d` and `W45` have dimension 45 and are disjoint from the 15-dimensional relation space,

\[
\pi(W_d)=\pi(W_{45})=Q_4^{true}.
\]

### Gate C — the ambient intersection dimension survives

**PASSED at the dimension level.**

\[
\dim I=\dim(W_{45}\cap W_d)=35.
\]

This is an ambient `L4` statement and must not be conflated with the intersection of their quotient images.

## 6. Crucial correction to the old quotient interpretation

The old quotient had dimension 55 and satisfied the numerical identity

\[
45+45-35=55.
\]

That supported the old statement that the two 45-dimensional modules filled the old 55-dimensional quotient.

That interpretation is now superseded.

For the true quotient,

\[
\dim Q_4^{true}=45,
\]

while both projected modules already have dimension 45. Hence

\[
\boxed{\pi(W_{45})=\pi(W_d)=Q_4^{true}},
\]

and consequently

\[
\boxed{\pi(W_{45})\cap\pi(W_d)=Q_4^{true}}.
\]

Thus the ambient intersection `I` of dimension 35 and the quotient-image intersection of dimension 45 are different objects.

## 7. What is still NOT revalidated

The following statement has **not** yet been promoted to a corrected final theorem:

\[
I\cong K.
\]

The dimension `dim I = 35` survives the corrected ambient computation, but the module-theoretic identification with `K` must be recomputed using the corrected chain and the same ambient coordinate conventions.

Only after that check can the Track A / Track B connection through `I ≅ K` be relocked.

## 8. A3-4-10 / A3-4-11 status

A3-4-10/11 remains blocked until the next revalidation gate:

1. reconstruct `I=W45∩Wd` in the corrected ambient setting;
2. verify `dim I=35` independently;
3. reverify `I ≅ K` as an actual `Sp4(F3)`-module/subspace statement;
4. explicitly distinguish ambient intersections from quotient-image intersections;
5. only then resume the degree-5 obstruction computation.

## 9. Final status

**W_d true-relation gate: PASSED.**

The important corrected facts are:

\[
\boxed{\dim(R)_4^{true}=15,
\quad \dim W_d=45,
\quad W_d\cap(R)_4^{true}=0,
\quad \dim\pi(W_d)=45,
\quad \dim(W_{45}\cap W_d)=35.}
\]

The old 55-dimensional quotient interpretation is superseded; the ambient `35`-dimensional intersection remains a separate object whose `I ≅ K` identification still requires explicit revalidation.
