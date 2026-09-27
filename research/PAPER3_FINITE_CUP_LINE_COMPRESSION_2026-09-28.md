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


## 2026-09-28 — ABSTRACT KERNEL ATTACK RESOLVED BY RELATION-MODULE / CUP DUALITY

The previously open kernel question is now resolved abstractly. The missing step was not to argue from global naturality, but to compute the **rank of the finite cup map directly from a minimal pro-p presentation**.

Write the fixed Demuškin group as (G=F/R), where (F) is free pro-p on (d) generators and (R) is normally generated by the single Demuškin relator (r). For
[
Q_k=G/D_n(G),qquad n=p^{k-1}+1\ge3,
]
the quotient has presentation
[
Q_k=F/R_k,qquad R_k=R,D_n(F).
]
Functoriality of the Zassenhaus filtration gives this kernel description, and (D_n(F)\subseteq D_3(F)).

Hence the degree-two relation image is
[
R_kD_3(F)/D_3(F)=mathbf F_p\cdotoperatorname{in}_2(r),
]
a one-dimensional subspace of (D_2(F)/D_3(F)). The extra finite relators contribute no degree-two term.

Now use the standard relation-module/cup-product pairing for a minimal pro-p presentation. Under
[
H^2(Q_k,mathbf F_p)^*cong R_k/R_k^p[R_k,F],
]
the dual of the cup-product map
[
H^1(Q_k,mathbf F_p)^{otimes2}longrightarrow H^2(Q_k,mathbf F_p)
]
is precisely the map induced by the degree-two initial-form map
[
R_k/R_k^p[R_k,F]longrightarrow D_2(F)/D_3(F).
]
This is the content of the standard cup/initial-relator compatibility: the value of a cup product on a relation is exactly the coefficient of that relation's degree-two commutator (and, for (p=2), power) initial form. For odd (p), only the alternating commutator part occurs. The general pairing is recorded in Mináč–Pasini–Quadrelli–Tân, Proposition 7.1 and the associated pairing diagram around Theorem 7.3. citeturn3search0turn2search3

Therefore the rank of the finite cup map equals the rank of its dual degree-two relation map. Since the latter has image exactly (mathbf F_p\cdotoperatorname{in}_2(r)),
[
oxed{dim_{mathbf F_p}C_k=1.}
]
This is the missing proof. It does **not** rely on injectivity of finite (H^2(Q_k)	o H^2(G)), and it does not confuse the finite (H^2) space with the global one-dimensional (H^2(G)).

The image is nonzero because the Demuškin relator has nonzero degree-two commutator form (equivalently, the global Demuškin cup pairing is nondegenerate). Thus the rank is exactly one, not merely at most one.

### Consequences

1. (C_k	o H^2(G,mathbf F_p)) is now injective: it is a nonzero map from a one-dimensional space.
2. Hence (C_k\cap\operatorname{im}(operatorname{tra}_k)=0), because the transgression image is killed by inflation to (G).
3. The D2 variation outputs (
u\cup\bar f) lie in (C_k), and D2's existential witness has nonzero global inflation, so every false candidate has a nonzero finite output in this one-dimensional line.
4. The finite recognition carrier is therefore genuinely one-dimensional and intrinsic to (Q_k), with no 45-dimensional computation required.
5. The stronger question of whether (E_k\to Q_k) alone canonically reconstructs the same functional on all of (O_k) remains a separate structural refinement, but it is not load-bearing.

### Final reclassification after the abstract proof

| Item | Status |
|---|---|
| (ker(C_k\to H^2(G))=0) | **PASS / CLOSED** |
| (dim C_k=1) | **PASS / CLOSED** |
| (C_k\hookrightarrow O_k) | **PASS / CLOSED** |
| 1D intrinsic finite selector carrier | **PASS / CLOSED** |
| Linear selector-carrier minimality = 1 | **PASS / CLOSED** |
| 45-dimensional computation | **DEFERRED / NOT REQUIRED** |
| Canonical (O_k\tomathbf F_p) reconstructed from (E_k\to Q_k) alone | **OPEN / NOT LOAD-BEARING** |

This supersedes the immediately preceding “kernel open” correction. The correction was useful: it identified exactly the missing proof obligation, which is now discharged by relation-module/cup duality.


## CRITICAL REVIEW — 2026-09-28 — RELATION/CUP RANK ARGUMENT AUDITED

The new closure is substantially stronger than the previous naturality-only argument, and the decisive idea is correct, but two points must remain explicit.

1. The quotient presentation must be written correctly. If G=F/R and Q_k=G/D_n(G), then the kernel of F -> Q_k is R_k=R D_n(F), because Zassenhaus filtration is functorial and D_n(G) is the image of D_n(F). Since n=p^{k-1}+1>=3 for odd p, D_n(F) subset D_3(F). Also R_k subset F^(2), so F -> Q_k remains a minimal pro-p presentation.

2. The phrase “standard relation-module/cup duality gives rank equality” needs the actual finite presentation map, not merely Theorem 7.3 quoted as a black box. Proposition 7.1 gives the commutative pairing diagram for a minimal pro-p presentation, and the rank of the cup map equals the rank of its dual relation-to-quadratic-initial-form map. For Q_k, that latter map has image exactly the one-dimensional span of in_2(r), because the added relators D_n(F) contribute nothing modulo D_3(F). Hence dim C_k=1. The published source explicitly states the pairing compatibility in Proposition 7.1 and identifies the quadratic initial-form map with cup products. citeturn0search2

This closes the earlier logical gap: the proof is NOT “global H^2 is one-dimensional, therefore finite C_k is one-dimensional.” It is “finite cup map and finite quadratic relation map are dual, and the latter has rank one.”

A further check: for the torsion-free odd-p Demushkin relation, the degree-two commutator form is nonzero; the q-term x_1^q has degree q>=p>=3 and therefore does not alter the quadratic initial form. Thus the rank-one conclusion applies throughout the declared odd-p Demushkin scope.

What must NOT be claimed: the cited theorem by itself does not prove any arbitrary pro-p group has one-dimensional cup image. The one-dimensionality here uses the specific one-relator Demushkin presentation together with the fact that the finite quotient adds only relators in D_3.

Final audited status:
- finite cup-line rank argument: PASS / CLOSED;
- kernel C_k -> H^2(G) = 0: PASS / CLOSED;
- C_k -> O_k injective: PASS / CLOSED;
- 1D finite selector carrier: PASS / CLOSED, conditional on already-closed D2 variation/separation;
- absolute selector-window minimality: OPEN;
- canonical O_k -> F_p from E_k -> Q_k alone: OPEN / not load-bearing;
- publication novelty: OPEN / CONDITIONAL.
