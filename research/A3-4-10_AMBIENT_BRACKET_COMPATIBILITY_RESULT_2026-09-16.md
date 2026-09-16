# A3-4-10 — Ambient Bracket Compatibility Result

Date: 2026-09-16
Phase: 2-23 / A3-4-10

## Purpose

A3-4-9 established an $Sp_4(\mathbb F_3)$-module isomorphism
\[
X:W_{45}\xrightarrow{\sim}W_d
\]
fixing the common 35-dimensional submodule
\[
K=W_{45}\cap W_d=\ker N.
\]
The purpose of A3-4-10 was to test whether this abstract module/extension equivalence also respects the ambient free-Lie-algebra bracket.

The q-sensitive degree-4 element is
\[
d=[X_1^{[3]},X_2].
\]
The comparison is between
\[
W_{45}=\langle Sp_4(\mathbb F_3)\cdot T\rangle,
\qquad
W_d=\langle Sp_4(\mathbb F_3)\cdot d\rangle.
\]

## Exact test

For each degree-1 generator $X_g$, $g=1,2,3,4$, the verified A3-4-9 intertwiner $X$ was tested against the ambient bracket:
\[
X([w,X_g])\stackrel{?}{=}[X(w),X_g]
\]
for every $w\in W_{45}$.

The calculation was performed in the degree-5 associative word space of dimension
\[
4^5=1024.
\]
Since the free Lie algebra embeds in the tensor algebra, equality of these associative expansions is an exact equality test for the corresponding Lie brackets.

The stacked discrepancy rank was also computed.

## Reproducibility

GitHub Actions:
- Run: `35057050558`
- Job: `104669318027`
- Conclusion: `success`

Code:
`research/phase2_23_A3_4_10_ambient_bracket_compatibility_2026-09-16.py`

Code commit used by the run:
`fe2f1b8db87b2d5b4ae384a17421bfa841e71289`

Workflow:
`.github/workflows/phase2-23-A3-4-10.yml`

The workflow is manual (`workflow_dispatch`) and executes the A3-4-10 script with Python 3.11 and NumPy. 

## Verified output

```text
PHASE 2-23 / A3-4-10 AMBIENT BRACKET COMPATIBILITY
dim W45 = 45
dim Wd = 45
dim common K = 35
system rows = 11700
system unknowns = 2025
rank of constrained system = 2024
solution nullity = 1
A3-4-9 intertwiner rank = 45
A3-4-9 intertwiner fixes K = True
degree-5 ambient associative word dimension = 1024
BRACKET_COMPATIBLE_FOR_ALL_4_GENERATORS = False
STACKED_BRACKET_OBSTRUCTION_RANK = 45
RESULT: the verified module/extension intertwiner is NOT compatible with the ambient degree-5 Lie bracket.
ALL A3-4-10 CHECKS COMPLETED
```

## Result

The A3-4-9 module/extension equivalence does **not** extend to the ambient degree-5 bracket structure tested here.

More precisely, for the verified full-rank intertwiner $X$ fixing $K$ pointwise, the stacked map
\[
\Phi:W_{45}\longrightarrow L_5^{\,4},
\qquad
w\longmapsto
\bigl([X(w),X_1]-X([w,X_1]),\ldots,[X(w),X_4]-X([w,X_4])\bigr)
\]
has rank 45 over $\mathbb F_3$ under the computed associative realization.

Thus
\[
\ker\Phi=0.
\]
In particular, there is no nonzero vector of $W_{45}$ on which the tested ambient bracket comparison agrees under this intertwiner.

## Structural significance

This is the first verified point in the current A3-4 sequence where the q-sensitive construction is distinguished **after** the abstract module and extension data have been identified as equivalent.

The progression is now:

\[
\begin{array}{c}
W_{45}\cong W_d\\
W_{45}/K\cong W_d/K\cong\operatorname{Sym}^2(V)\\
(W_{45},K)\cong(W_d,K)\\
\hline
\text{but ambient bracket compatibility fails.}
\end{array}
\]

This means that the q-sensitive signal is not visible at the level of the abstract 45-dimensional $Sp_4(\mathbb F_3)$-module or its extension class, but it is visible in the **embedding of that module into the ambient free Lie algebra together with the first degree-raising bracket operation**.

The obstruction rank being exactly 45 is particularly strong computationally: the entire 45-dimensional source is detected by the stacked bracket discrepancy for this chosen intertwiner.

## Important caveats

1. This does **not** yet prove that the obstruction is an intrinsic canonical orientation invariant.
2. It does **not** by itself identify the obstruction with the previously proposed $\lambda\pmod 3$.
3. It does **not** establish that every possible choice of intertwiner or every possible ambient comparison gives the same obstruction. A3-4-9 fixing $K$ has a one-dimensional solution space, and the normalization/uniqueness issue should be handled explicitly in the next verification.
4. The current rank was computed in the 1024-dimensional associative word space. The next step should compress the obstruction to the actual degree-5 free-Lie space and identify its $Sp_4(\mathbb F_3)$-module structure.

## Next experiment

The most informative next step is therefore **not** to repeat the abstract module test. Instead:

1. Project the degree-5 bracket discrepancies from the associative tensor space onto the free Lie algebra $L_5$.
2. Determine the rank and $Sp_4(\mathbb F_3)$-module structure of the resulting obstruction image.
3. Check its intersection with the degree-5 relation ideal and with natural q-sensitive/restricted subspaces.
4. Determine whether the obstruction has a canonical scalar component or a quotient on which a scalar $\lambda\in\mathbb F_3$ can be extracted.
5. Only after this should the obstruction be compared with the candidate $\lambda\pmod 3$ or with canonical orientation.

The working hypothesis is now sharpened to:

> **The q-sensitive information may first become visible not in the abstract restricted-Lie module $W_d$, but in its ambient Lie-algebra embedding through the degree-raising bracket.**

This record is a verified computational result, not yet a proof of canonical orientation or of the proposed invariant $\lambda$.
