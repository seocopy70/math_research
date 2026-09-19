# HARD ATTACK 6 — LOGICAL AUDIT OF THE FOX CARRIER — 2026-09-19

## Verdict

The universal Fox object is a legitimate and useful exact characteristic-zero **linearized obstruction object**, but the previous wording “J_r=0 is the exact orientation locus” is too strong unless an additional theorem identifies canonical orientation with vanishing of the entire evaluated Fox row.

This is the most important remaining audit. The Fox calculus itself is standard: evaluated Fox rows control the linearized relator defect of crossed-homomorphism/lift problems, and the chain rule controls basis changes. However, that fact alone does not identify the character with the zero of the row.

## 1. Correct logical statement

For a candidate character (ho), the evaluated Fox row
[
J_r(ho)
]
defines a linear map on generator-variation vectors:
[
J_r(ho):M^d	o M
]
in the crossed-module/semidirect-product linearization.

A crossed derivation with generator values (a=(a_i)) satisfies
[
J_r(ho)a=0.
]

Therefore the intrinsic object supplied directly by Fox calculus is the pair
[
(ho,ker J_r(ho)),
]
or equivalently the universal family of linear obstruction maps.

It is **not automatic** that the orientation condition is
[
J_r(ho)=0
]
as a row.

That stronger condition was true in the frozen normal-form calculation because the chosen canonical derivation vector made all row coefficients vanish at the resulting (ho), but this coincidence needs an independent argument before it can define the general orientation locus.

## 2. Three logically distinct conditions

They must be kept separate:

(A) existence of a nonzero crossed derivation:
[
ker J_r(ho)
eq0;
]

(B) existence of the specific canonical/Demuškin orientation derivation:
[
a_{mathrm{can}}inker J_r(ho);
]

(C) vanishing of the whole row:
[
J_r(ho)=0.
]

The implications
[
(C)Rightarrow(B)Rightarrow(A)
]
hold when the canonical vector is defined.

The reverse implications do not follow from Fox calculus alone.

## 3. Immediate danger: C may be too restrictive

A basis change multiplies the row by an invertible matrix on the right, so the condition “row = 0” is actually stable under basis change. This is good.

But it remains a stronger condition than “there exists a canonical kernel vector”. Thus the carrier may accidentally recover the correct point in this one normal form while failing to be the right invariant in another equivalent presentation.

The next decisive experiment is therefore not another representation scan. It is to construct several Nielsen-equivalent minimal presentations of the same group and compare:

1. the universal Fox row;
2. its zero locus;
3. the kernel locus;
4. the transported canonical derivation vector.

If zero-row and canonical-kernel loci diverge under a presentation change, the current carrier claim must be weakened.

## 4. Second danger: the coefficient torus is character-theoretic, not obviously filtration-theoretic

The map
[
x_imapsto T_i
]
is universal for abelian multiplicative coefficients. Hence it naturally sees characters factoring through the abelianization.

That is appropriate for a (mathbf Z_3^	imes)-valued orientation, but it does **not** by itself make the object an intrinsic Zassenhaus/Jennings–Lazard filtered carrier.

Therefore the research chain is currently:

filtered group data -> (still missing) canonical character-theoretic identification -> universal Fox scheme -> exact character.

The Fox scheme does not replace the missing filtered bridge.

## 5. Third danger: “intrinsic” must be weakened

What has been established is presentation covariance of the Fox construction under the tested moves, not yet a theorem that the resulting scheme is canonically attached to the abstract pro-3 group independently of all choices and completions.

In particular, the completed coefficient ring and the chosen character neighborhood (1+3mathbf Z_3) are part of the construction. They are natural for the target (mathbf Z_3^	imes), but this is character-theoretic naturality, not the same as an intrinsic filtered construction.

## 6. Corrected research position

The Fox branch is **not a detour**. It has exposed a potentially useful exact endpoint:

[
oxed{
	ext{presentation-independent universal linearized Fox obstruction family}
}
]

But it should not yet be advertised as the desired intrinsic filtered degree-(2,3) carrier.

The genuine target remains:

[
oxed{
	ext{intrinsic filtered data}
Longrightarrow
	ext{canonical character obstruction/evaluation}
}
]

The Fox scheme can serve as an exact comparison object against which any proposed filtered carrier must reproduce the same character locus.

## 7. Next gate

Perform the Nielsen-equivalent presentation stress test before doing any further compression.

Required outputs:

- at least two nontrivial Nielsen transforms of the rank-4 presentation;
- symbolic universal Fox rows in both presentations;
- explicit coordinate substitution between their character tori;
- comparison of row-zero loci;
- comparison of kernel loci;
- explicit transport of the canonical derivation vector.

Decision rule:

If row-zero locus is invariant and agrees with the canonical-kernel locus in all tests, the carrier claim strengthens.

If not, downgrade the carrier to an exact auxiliary obstruction family and return to the filtered-to-character bridge.

No representation-theoretic scan should be performed before this gate closes.
