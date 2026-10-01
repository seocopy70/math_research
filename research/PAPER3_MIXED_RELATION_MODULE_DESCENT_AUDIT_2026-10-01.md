# MIXED (3,I)-ADIC FOX — CATEGORICAL RELATION-MODULE DESCENT AUDIT — 2026-10-01

## Result

The weighted Magnus obstruction is now isolated from the remaining categorical issue. The correct descent statement is a stable Fox/Lyndon relation-module statement over the finite **extension window**, not merely a statement about the two underlying objects (Q_k) and (A_k).

Set
[
N_k=3^{k-1}+1,qquad
Q_k=G/D_{N_k},qquad
E_k=G/D_{N_k+1},qquad
A_k=D_{N_k}/D_{N_k+1}.
]

The weighted Magnus lemma already proves
[
D_{N_k}subset 1+(3,I)^{k+1},
]
so the mixed coefficient algebra through precision (k) factors through (Q_k), and the first possible relation contribution from (D_{N_k}) is exactly the boundary class in (A_k).

## 1. Categorical object required by the Fox descent

The natural finite input for the relation-module descent is the central extension window
[
1longrightarrow A_klongrightarrow E_klongrightarrow Q_klongrightarrow1,
]
with its extension class, not the pair of abstract groups (Q_k) and (A_k) considered separately.

This distinction is load-bearing: (A_k=D_{N_k}/D_{N_k+1}) is not a subgroup of (Q_k=G/D_{N_k}). Thus an isomorphism of the bare pair
[
(Q_k,A_k)
]
does not, by itself, identify the central extension (E_k). Any theorem written as
[
(Q_k,A_k)Rightarrow M_k
]
is therefore under-specified unless “pair” is explicitly defined to mean the extension window.

## 2. Stable relation-module mechanism

For a finite pro-3 quotient (E), choose a minimal free pro-3 presentation
[
1	o R	o F	o E	o1.
]
The completed Fox/Lyndon sequence identifies the relation module with the kernel of the canonical differential
[
Lambda_E^dlongrightarrow Lambda_E,qquad
e_imapsto x_i-1,
]
and the relation generators map by their Fox rows. The relation module is presentation-dependent only up to the standard stable free-module ambiguity; after projectivization, this ambiguity disappears.

This is the categorical reason that the projective Fox object is the correct descent target: it is the stable relation-module class of the finite extension window, rather than a chosen relator row.

The classical pro-p relation-module exact sequence gives the required Fox realization; see Mel'nikov's exact sequence and the standard completed Fox/Lyndon formulation. This supports the structural mechanism, but does not by itself identify the present mixed jet.

## 3. Weighted boundary identification

Let (uin D_{N_k}). The weighted Magnus estimate gives
[
u-1in(3,I)^{k+1}.
]
Applying the Fox differential lowers the weighted order by exactly one:
[
duin(3,I)^k,dX.
]
If (uin D_{N_k+1}), then the same estimate gives
[
duin(3,I)^{k+1},dX.
]
Hence the induced boundary map
[
partial_k:
A_k=D_{N_k}/D_{N_k+1}
longrightarrow
(3,I)^k/(3,I)^{k+1},dX
]
is well-defined.

The map is natural under morphisms of filtered extensions because Fox differentiation is the universal first-order differential and the weighted filtration is preserved. Relation-generator changes and Nielsen changes act by the already verified gauge/Jacobian transformations; projectivization removes the remaining free-coordinate ambiguity.

Thus the deep-kernel contribution to the mixed Fox jet is determined by the boundary extension data, not by an arbitrary characteristic-zero lift.

## 4. Descent statement

With the finite input defined as the extension window
[
mathsf W_k(G):=(E_k	o Q_k, A_k),
]
the natural candidate theorem is
[
mathsf W_k(G)congmathsf W_k(H)
quadLongrightarrowquad
mathcal M_k(G)congmathcal M_k(H),
]
where (mathcal M_k) is the projectivized mixed Fox relation jet.

The proof decomposes into:

1. (Q_k) determines the truncated mixed coefficient algebra below weighted order (k);
2. the extension (E_k	o Q_k) determines the finite relation-module class;
3. (A_k) supplies exactly the weighted-order-(k) boundary contribution;
4. stable relation-module equivalence becomes projective equivalence;
5. the construction is natural under extension-window isomorphisms.

No characteristic-zero information survives independently of this finite extension window at precision (k).

## 5. Important boundary

What has **not** been established is the stronger statement from the previously abbreviated notation
[
(Q_k,A_k)Longrightarrowmathcal M_k.
]
That implication is not justified unless the extension (E_k	o Q_k) is part of the finite input or is canonically reconstructible in the declared category.

Therefore the remaining gate is not “Zassenhaus versus characteristic zero.” That part is closed. The remaining gate is the precise categorical packaging of the finite extension window and the proof that the projective Fox jet is its natural stable relation-module image.

## 6. Independent literature control

Efrat's p-adic Magnus result supplies the coefficient divisibility and the coefficient/boundary pairing used in the weighted step. cite source in final response only; this file itself is repository-local.

Mel'nikov's pro-p relation-module exact sequence supplies the structural Fox realization of a relation module as the kernel of the Fox differential. Neither source states the present mixed ((3,I))-adic finite-window theorem.

## Classification

- weighted Magnus coefficient descent: **PASS / CLOSED**;
- naive deep-relator counterexample: **FAIL / CLOSED**;
- stable/projective Fox mechanism: **PASS / LOCAL**;
- descent from the **finite extension window** to the projective mixed Fox jet: **PASS / LOCAL — proof architecture complete, formal naturality statement still to be written**;
- descent from the bare ((Q_k,A_k)) pair: **OPEN / NOT WELL-TYPED until the input category is defined**;
- whole Mixed Fox branch: **OPEN / LOAD-BEARING**;
- next decisive action: formalize the extension-window category and write the natural transformation (mathsf W_k	omathcal M_k), then independently check it against the projective Fox covariance identities.
