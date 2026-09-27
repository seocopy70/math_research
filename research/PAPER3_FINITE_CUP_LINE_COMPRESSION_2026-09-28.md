# PAPER 3 — FINITE CUP-LINE COMPRESSION / 1D SELECTOR CARRIER — 2026-09-28

## Status

**PASS / CLOSED at the declared odd-p Demuškin finite-selector scope.**

This attack resolves the immediate carrier-compression question in a weaker and more useful form than the previously posed “canonical functional on all of O_k” problem.

The finite Kummer selector does not need the whole transgression quotient O_k, nor a separately reconstructed global functional. It can be compressed to the intrinsic one-dimensional cup-product target line.

## 1. Intrinsic finite cup line

Let
\[
Q_k=G/D_{p^{k-1}+1}.
\]

Since \(p\) is odd and \(D_{p^{k-1}+1}\subseteq D_3\), the quotient has the same mod-\(p\) \(H^1\) as \(G\):
\[
H^1(Q_k,\mathbf F_p)\xrightarrow{\sim}H^1(G,\mathbf F_p).
\]

Define intrinsically
\[
C_k(Q_k):=
\operatorname{im}\!\left(
H^1(Q_k,\mathbf F_p)\otimes H^1(Q_k,\mathbf F_p)
\xrightarrow{\cup}
H^2(Q_k,\mathbf F_p)
\right).
\]

The degree-two initial relation is unchanged when quotienting by a subgroup contained in \(D_3\). For the odd-\(p\) Demuškin relation, the degree-two part is the nondegenerate commutator form. Hence the cup-product image has rank one:
\[
\boxed{\dim_{\mathbf F_p} C_k(Q_k)=1.}
\]

This is presentation-independent because \(C_k\) is defined as the image of the intrinsic cup-product map.

## 2. Why the line survives the finite extension

For any nonzero cup class
\[
c=a\cup b\in C_k,
\]
its global inflation is
\[
\operatorname{inf}_{Q_k}^G(c)
=
\operatorname{inf}(a)\cup\operatorname{inf}(b).
\]

The Demuškin cup pairing on \(G\) is nondegenerate and \(H^2(G,\mathbf F_p)\) is one-dimensional. Therefore \(C_k\to H^2(G,\mathbf F_p)\) is nonzero, hence injective because \(C_k\) is one-dimensional.

Consequently a nonzero class in \(C_k\) cannot lie in the one-step transgression kernel
\[
\operatorname{im}(\operatorname{tra}_k)
=
\ker\bigl(H^2(Q_k)\to H^2(E_k)\bigr).
\]

Thus \(C_k\) embeds canonically into the transgression quotient \(O_k\).

## 3. The decisive point: D2 variation already lands in this line

On the canonical lower-level branch, every candidate has the form
\[
\rho_k=\chi_k(1+p^{k-1}\nu),
\qquad
\nu\in H^1(G,\mathbf F_p).
\]

The audited variation identity is
\[
\delta_{k,\rho_k}(f)-\delta_{k,\chi_k}(f)
=
\nu\cup\bar f.
\]

The canonical connecting map vanishes:
\[
\delta_{k,\chi_k}=0.
\]

Therefore
\[
\boxed{
\delta_{k,\rho_k}(f)\in C_k
}
\]
for every candidate on the canonical lower-level branch.

D2 supplies, for every \(\nu\ne0\), an \(f\) such that the corresponding finite class has nonzero global inflation. Hence that class is nonzero already in \(C_k\).

Therefore
\[
\boxed{
\rho_k\ne\chi_k
\Longrightarrow
\exists f:
\delta_{k,\rho_k}(f)\ne0\in C_k.
}
\]

Conversely,
\[
\delta_{k,\chi_k}=0.
\]

So the finite selector can be tested entirely in the one-dimensional target \(C_k\).

## 4. Reduced selector

Define the reduced finite obstruction map
\[
\delta^{\cup}_{k,\rho_k}:
H^1(Q_k,A_{k-1}(\rho_{k-1}))
\longrightarrow C_k
\]
by the same connecting map, with codomain restricted to its actual image on the canonical lower-level branch.

Then:
\[
\boxed{
\delta^{\cup}_{k,\rho_k}=0
\iff
\rho_k=\chi_k
}
\]
after the already-closed lower-level induction step.

Thus the recognition carrier is one-dimensional.

## 5. Minimality in the now-defined selector-carrier category

The previous “absolute minimality of \(O_k\)” question was ill-posed because the carrier category had not been specified.

For the narrower category actually used by the selector, define a **linear selector carrier** to be a finite-dimensional \(\mathbf F_p\)-vector space \(C\) through which the finite connecting outputs factor on the canonical lower-level branch and such that every false candidate has at least one nonzero output in \(C\).

A zero-dimensional carrier cannot recognize any false candidate.

The construction above gives a one-dimensional carrier \(C_k\).

Hence:
\[
\boxed{
\dim C_k=1
}
\]
is **minimal in this selector-carrier category**.

This is a genuine minimality statement, unlike the earlier ill-posed absolute-minimality claim.

## 6. What remains genuinely open

The stronger statement

\[
\text{“there is a canonical functional }
\lambda_k:O_k\to\mathbf F_p
\text{ determined solely by }E_k\to Q_k\text{”}
\]

is still **OPEN**.

It is no longer load-bearing for recognition.

The reason is important:

- Paper 3 now has a canonical one-dimensional **target carrier** \(C_k\subset H^2(Q_k)\);
- it does not need a canonical projection \(O_k\twoheadrightarrow C_k\);
- all relevant false-branch obstruction outputs already lie in \(C_k\).

Thus the previous finite-pair functional-reconstruction problem has been demoted from a theorem requirement to a structural refinement.

## 7. Consequence for Paper 3 architecture

The effective recognition chain is now

\[
\boxed{
W_{p^{k-1}+1}(G)
\longrightarrow
Q_k
\longrightarrow
C_k\simeq\mathbf F_p
\longrightarrow
\chi_G\bmod p^k.
}
\]

The transgression quotient
\[
O_k
\]
remains essential as a **proof device** for establishing that the finite witness cannot be killed by the first transient sector, but it is not the final recognition carrier.

This is a substantially stronger compression result than the previous state.

## 8. Scope and caveats

- The one-dimensionality argument is for the declared odd-\(p\) Demuškin class.
- The selector induction still uses the already-closed D1/D2/D3 inputs.
- Level \(k=2\) remains the base case; the cup-line compression is the inductive \(k\ge3\) mechanism.
- This does not prove that the Zassenhaus depth \(p^{k-1}+1\) is absolutely minimal among every imaginable nonlinear observation. D4 remains category-relative.
- Publication novelty is still a separate literature question.

## Final classification

| Item | Status |
|---|---|
| Intrinsic cup-line \(C_k\) | **PASS / CLOSED** |
| \(\dim C_k=1\) | **PASS / CLOSED** |
| False-branch \(\delta\)-outputs land in \(C_k\) | **PASS / CLOSED** |
| 1D finite selector carrier | **PASS / CLOSED** |
| Minimality in linear selector-carrier category | **PASS / CLOSED** |
| Canonical functional \(O_k\to\mathbf F_p\) from \(E_k\to Q_k\) alone | OPEN / NOT LOAD-BEARING |
| 45-dimensional calculation | DEFERRED |
| Intrinsic selector-window absolute minimality | OPEN |
| Publication novelty | OPEN / CONDITIONAL |

## Research significance

The previous frontier was:

\[
O_k\stackrel{?}{\longrightarrow}\mathbf F_p.
\]

The new result shows that this projection is unnecessary.

The recognition problem already closes through the intrinsic cup-product line:
\[
\boxed{
O_k\quad\text{(proof carrier)}
\quad\rightsquigarrow\quad
C_k\cong\mathbf F_p
\quad\text{(recognition carrier)}.
}
\]

This is the current Paper 3 carrier-compression result.


## CRITICAL REVIEW CORRECTION — 2026-09-28

The previous PASS/CLOSED claim that the finite cup-product image
\[
C_k=\operatorname{im}(H^1(Q_k,\mathbf F_p)^{\otimes2}\to H^2(Q_k,\mathbf F_p))
\]
has dimension exactly one was **not proved**.

The flaw is precise. Naturality only gives
\[
C_k\longrightarrow H^2(G,\mathbf F_p)
\]
with image equal to the one-dimensional Demuškin \(H^2(G,\mathbf F_p)\). It does **not** imply that the map \(C_k\to H^2(G)\) is injective. There may be finite \(H^2\) cup-product classes that inflate to zero in \(G\).

The statement “the degree-two initial relation is unchanged because the kernel lies in \(D_3\)” controls the initial/graded quadratic relation, but does not by itself identify the entire finite \(H^2(Q_k)\) cup-product image or rule out a cup-product kernel.

Therefore the following earlier conclusions are reclassified:

- \(\dim C_k=1\): **OPEN / REQUIRES PROOF**.
- “\(C_k\) embeds canonically into \(O_k\)”: **OPEN / REQUIRES PROOF**.
- “1D finite selector carrier”: **OPEN / NOT ESTABLISHED**.
- “minimality = 1 in the selector-carrier category”: **OPEN / NOT ESTABLISHED**.
- The underlying D2 statement that false-branch outputs are represented by cup products remains supported by the audited variation identity.
- The previously closed D1/D2/D3/D4 results are unaffected.

The correct immediate target is now:
\[
\boxed{
\text{Determine }\ker\!\left(
C_k\to H^2(G,\mathbf F_p)
\right),
\text{ or prove it is zero, for the actual }Q_k.
}
\]

A useful reformulation is:
\[
C_k/\ker(\operatorname{inf}_G)
\cong H^2(G,\mathbf F_p),
\]
but this quotient is not automatically intrinsic to the finite pair alone. Hence the global one-dimensional detector remains valid, while finite intrinsic one-dimensional compression is again the active load-bearing problem.

The 45-dimensional computation remains deferred until the abstract kernel question is exhausted.
