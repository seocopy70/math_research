# PAPER 3 TOP-DOWN T−1/T0 CLOSURE — INTRINSIC DEMUŠKIN ORIENTATION AND FINITE-WINDOW OBSERVABILITY — 2026-10-02

## 0. Decision

The previously open target-identification gate T−1 is now closed for the declared active scope:

- odd prime p;
- infinite finite-rank Demuškin groups;
- fixed rank d (active instance p=3, d=4);
- standard Demuškin orientation valued in (1+p\mathbf Z_p);
- finite target (chi_k=chi_G\bmod p^k);
- finite input (W_k=(G/D_{N_k},D_{N_k}/D_{N_k+1})), (N_k=p^{k-1}+1).

The crucial correction is that Labute's crossed-derivation character is not merely a presentation-local scalar. Labute's Theorem 4 constructs a unique continuous homomorphism
[
\chi_G:G\to U_p
]
characterized by the Kummerian derivation property, and in the standard odd-p normal form gives
[
\chi_G(x_2)=(1-q)^{-1},qquad \chi_G(x_i)=1 (i\ne2).
]
Modern sources identify this as the canonical Demuškin orientation and state that it is the unique orientation making the Demuškin group Kummerian/1-cyclotomic.

Therefore the previous T0 objection—"theta=(1-q)^{-1} is only a presentation-level twist"—is resolved at the declared standard Demuškin scope: the relevant Labute character is precisely the canonical intrinsic orientation.

## 1. Exact target: basis-free formulation

The target is not a generator-coordinate tuple.

For an infinite odd-p Demuškin group (G), let
[
\chi_G:G\to1+p\mathbf Z_p
]
be the unique canonical orientation characterized by Labute's Kummerian crossed-derivation property (equivalently, the canonical orientation/dualizing orientation in the modern formulation).

For a group isomorphism (arphi:G\to H), the transported character
[
\chi_H\circ\varphi
]
is again a Kummerian orientation on (G). By uniqueness,
[
\boxed{\chi_H\circ\varphi=\chi_G.}
]
Hence the canonical orientation is functorial under group isomorphisms.

At finite level, define
[
[\chi_k(G)]
]
as the transported-isomorphism class of the reduction
[
\chi_G\bmod p^k.
]
This removes presentation/basis dependence. It is the correct target for the top-down identifiability question.

## 2. Literature control: three notions are now separated correctly

### 2.1 Abstract Demuškin orientation

Labute proves existence and uniqueness of the continuous character with the required crossed-derivation/Kummerian property. Modern treatments call it the canonical orientation of the Demuškin group.

### 2.2 Cyclotomic orientation

A pro-p Galois group of a field containing the p-th roots of unity carries its p-cyclotomic character. For a realizable Demuškin group, the canonical orientation coincides with the cyclotomic character because the dualizing module is the p-power roots-of-unity module. This is an arithmetic specialization, not the definition of the abstract target.

Thus "cyclotomic character" is not the primary target of the present abstract theorem; it is a realization of the same canonical orientation when the Galois hypotheses apply.

### 2.3 Labute coefficient/crossed-derivation formula

For the standard odd-p presentation
[
G=\langle x_1,\ldots,x_dmid x_1^q[x_1,x_2][x_3,x_4]\cdots=1\rangle,
]
Labute's Theorem 4 gives
[
\chi_G(x_2)=(1-q)^{-1},qquad \chi_G(x_i)=1 (i\ne2).
]
Therefore this formula is now legitimately usable as a coordinate expression for the intrinsic canonical orientation, after the theorem-level identification above.

## 3. T−1 result

The target-identification gate is therefore:

[
\boxed{\text{T−1 target identification = PASS/CLOSED}}
]

under the declared standard odd-p Demuškin hypotheses.

What is proved:
1. the target is an intrinsic canonical orientation;
2. it is unique;
3. it is invariant under abstract group isomorphism;
4. Labute's explicit normal-form formula computes that target;
5. in realizable arithmetic cases it agrees with the p-cyclotomic orientation.

What is not claimed:
- that every Demuškin group is realizable as an absolute Galois group;
- that the cyclotomic interpretation is available outside an arithmetic realization;
- that finite-window factorization has yet been proved.

## 4. T0 finite-window identifiability

Now return to
[
N_k=p^{k-1}+1.
]

For the standard odd-p fixed-rank family,
[
q\in\{p,p^2,p^3,\ldots\}\cup\{0\}.
]

There are exactly two relevant finite-precision regimes.

### Regime A: (q<p^k)

Then (q=p^s) with (s<k), and hence
[
q<N_k.
]
The q-power term in the Demuškin relator first appears at Zassenhaus degree q. The intrinsic graded dimensions below (N_k) therefore detect the first q-dependent defect. The established Demuškin reconstruction audit gives
[
W_k(G)\cong W_k(H)
\Longrightarrow q(G)=q(H)
]
in this regime.

### Regime B: (q\ge p^k) or (q=0)

Since
[
p^k>p^{k-1}+1=N_k
]
for (p\ge3), these q-values lie beyond the finite window. The q-power term is invisible through the declared truncation, and the finite-window reconstruction collapses these values to one q-regime.

But the canonical orientation formula gives
[
\chi_G(x_2)=(1-q)^{-1}.
]
If (q\equiv0\pmod{p^k}), then in (mathbf Z_p)
[
(1-q)^{-1}\equiv1\pmod{p^k}.
]
For (q=0), the same formula gives exactly (1).

All other standard-form generator values are already (1). Therefore
[
q\ge p^k 	ext{or }q=0
\Longrightarrow
[\chi_k(G)]
]
is the same trivial finite-level orientation class.

### No boundary case (q=N_k)

This case is impossible:
[
N_k=p^{k-1}+1
]
is not a p-power, while standard odd-p Demuškin q is a p-power or 0.

It must not appear in the proof.

## 5. T0 theorem

Combining the intrinsic target identification with the finite-window q reconstruction:

[
\boxed{
W_k(G)\cong W_k(H)
\Longrightarrow
[\chi_k(G)]=[\chi_k(H)]
}
]

for the standard odd-p fixed-rank Demuškin family.

### Proof

If the common window lies in Regime A, the window determines q exactly; the canonical orientation is the unique orientation attached to the Demuškin group and has the standard coordinate value ((1-q)^{-1}), so the finite-level target is determined.

If the common window lies in Regime B, all admissible q-values are congruent to 0 modulo (p^k), or q=0, and the canonical orientation reduces to the trivial character modulo (p^k).

Thus the target is constant on every finite-window isomorphism class.

## 6. Status

- Top-down carrier-independent no-go lemma: **PASS/CLOSED**.
- (I_k(w)) identifiability criterion: **PASS/CLOSED**.
- T−1 intrinsic target identification: **PASS/CLOSED** at standard odd-p Demuškin scope.
- Demuškin finite-window T0: **PASS/CLOSED** at standard odd-p fixed-rank scope.
- Broad extension reconstruction: **FAIL/CLOSED**.
- Broad orientation non-identifiability: **OPEN / NOT PROVED**.
- Observability-depth monotonicity: **OPEN**.
- New carrier construction before T0: **NO LONGER BLOCKED**, but novelty must still be tested.

## 7. Important logical boundary

This closure does not establish a new carrier.

Indeed, T0 says the target already descends through the finite window. It does not say that a particular intrinsic algebraic object is the coarsest realization of that descent.

Therefore the research question now changes again:

[
\boxed{
\text{finite-window orientation factorization is established}
\quad\Longrightarrow\quad
\text{find the coarsest/non-tautological intrinsic realization, if any.}
}
]

The Mixed Fox branch remains closed as a new recognition theorem because its current bridge is classification repackaging. The next carrier search is therefore authorized only for a genuinely different realization of the already-proved finite target factorization.

## 8. Evidence

Primary/near-primary controls:
- Labute, *Classification of Demushkin groups*, Theorem 4: unique character with the crossed-derivation property and the standard value ((1-q)^{-1}).
- Quadrelli, *Chasing Maximal Pro-p Galois Groups via 1-Cyclotomicity*, Example 2.6: canonical Demuškin orientation, uniqueness, and the standard odd-p formula.
- Quadrelli–Weigel / related cyclotomic-pair literature: canonical orientation is the 1-cyclotomic orientation for infinite Demuškin groups.
- Modern cohomological classification sources: canonical orientation and q are intrinsic classification data.

These sources establish the target identification; they do not by themselves establish the project's finite-window factorization. The latter uses the project-specific Demuškin Zassenhaus reconstruction already independently audited.

## 9. Research consequence

The first top-down T0 attempt was correctly superseded because it lacked the target-identification theorem. That defect is now repaired.

The active problem is no longer "does the finite window determine the canonical orientation?" within the standard odd-p fixed-rank family. It does.

The nontrivial remaining top-down question is:

> What is the intrinsic, q-blind, non-redundant finite realization of the already-forced map (W_k\mapsto[\chi_k]), and is there a genuinely smaller/coarser observable object than the existing selector?

This is the next authorized gate.
