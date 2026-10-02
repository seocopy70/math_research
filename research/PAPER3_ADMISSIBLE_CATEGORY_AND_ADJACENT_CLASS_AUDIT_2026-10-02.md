# PAPER 3 POST-EXPLORATION — ADMISSIBLE CATEGORY / ADJACENT-CLASS AUDIT — 2026-10-02

## 0. Decision

The proposed A–D "admissible finite realization category" is a useful design sketch, but it is **not yet a valid minimality category**. Two defects are decisive:

1. A functor (F:mathrm{Dem}	omathrm{Fin}) plus finiteness/intrinsicity does not prevent target-reencoding. The category must specify not only objects but also morphisms, observation maps, and what counts as an admissible realization.
2. The proposed (X_{ab}=igoplus gr_n(G)) is not an abelianization. It is the associated graded object of the Zassenhaus filtration (with restricted-Lie structure if retained). If the degree labels and operations are discarded, the proposed carrier can lose exactly the structure used to read the defect degree.

More importantly, the same-family compression problem is already closed by the sharp (k)-class information bound plus the defect-index realization: within the standard odd-p fixed-rank Demuškin family, any further "compression" that still recovers the full ([chi_k]) is classification-level unless it yields a structural theorem not reducible to the q-regime.

The authorized next branch is therefore an adjacent-class test, not another same-family compression.

## 1. Critique of the proposed admissible category

### 1.1 A–D are necessary-style constraints, not a category

A functor (F:mathrm{Dem}	omathrm{Fin}) is too permissive. One can define functors whose values are arbitrary finite encodings of isomorphism classes. Thus "functorial + finite + intrinsic" does not by itself exclude the tautological target.

Condition C ("non-constant") is also not sufficient: it is a property of one chosen map on one family, not a structural restriction on the realization category.

Condition D (closure under quotients) is insufficient as well. To state a coarsest object, one needs at least:
- a category of admissible carriers;
- a specified observation/factorization relation;
- an equivalence notion for carriers;
- closure under the relevant quotients/refinements;
- a non-tautological restriction excluding carriers defined from the target itself.

Therefore the earlier statement "the first task is to define A–D" is too strong. The first task is to define a **non-reencoding admissible realization problem**.

### 1.2 The statistical analogy is only methodological

Minimal sufficiency is genuinely a factorization/coarsening concept, but its classical definition uses a statistical model and sufficiency relative to a parameter. The literature states minimal sufficiency as recoverability from every sufficient statistic. citeturn2search0turn2search8

For this project there is no probability model. The useful import is only the order-theoretic idea:
[
Xpreceq Y iff X 	ext{ factors through }Y.
]
The research object should therefore be a **factorization preorder on admissible realizations**, not a claim that Bahadur/Fisher theory transfers.

### 1.3 Critical correction: vector-space cardinality lower bound

The statement
[
p^{dim V}ge k
]
is valid only if the carrier observation is the underlying set (or otherwise retains (p^{dim V}) distinguishable states).

If (V) is regarded merely as an (mathbf F_p)-vector-space object up to isomorphism, then for each fixed dimension there is only one isomorphism class. Thus dimension alone does **not** imply (p^{dim V}) target classes.

The correct lower-bound statement is:
[
|mathrm{Iso}(C_k)|ge k.
]
A dimension bound requires an additional convention, e.g. that the observation is a distinguished element/subspace/functional or a graded vector-space with the relevant labeled data retained. This correction does not affect the (k)-class lower bound itself.

## 2. Critical correction to (X_{ab})

The object
[
igoplus_{nle N_k}gr_n(G)
]
is the **associated graded Zassenhaus object**, not the abelianization of (W_k).

If only the direct-sum vector space is retained, the degree labels must be part of the object; otherwise the "first defect degree" is not even a well-defined observable.

If the restricted-Lie bracket and p-operation are retained, the object is substantially richer than a plain finite set/vector space. That may be mathematically useful, but then the compression claim must compare it against the original filtered group using a declared morphism class.

Within the standard Demuškin family, the defect degree (q=p^s) already gives the exact k-class partition needed for ([chi_k]). Therefore the associated graded construction is presently best classified as another realization of the same q-information, not as a genuinely new carrier.

## 3. Cohomological candidate: the proposed (X_{cohom}) is circular

The expression
[
H^1(W_k,mathbf Z/p^k)^{chi	ext{-twisted}}
]
uses (chi) in the definition of the carrier. This violates the project's q-blind/target-blind requirement.

A legitimate cohomological candidate would have to be defined from an untwisted canonical module or extension class already present in the finite input, and only afterwards admit a natural map to ([chi_k]). Merely moving (chi) into the phrase "twisted part" is not compression.

## 4. Adjacent-class test: free pro-p groups

The cleanest adjacent-class stress test is the class of finitely generated free pro-p groups with orientation as the target structure.

Literature gives the decisive boundary:

- For a free pro-p group (F), ((F,	heta)) is 1-cyclotomic for **every** orientation (	heta:F	o1+pmathbf Z_p). citeturn1search0turn1search6
- By contrast, an infinite Demuškin group has a unique orientation completing it to a 1-cyclotomic pair, and in standard normal form that orientation has (chi(x_2)=(1-p^f)^{-1}), (chi(x_i)=1) for (i
e2). citeturn1search0turn1search8

Hence, once the class is enlarged from Demuškin groups to free pro-p groups **while the input remains the underlying un-oriented finite window (W_k(G))**, the orientation target ceases to be a function of the input object at all: the same (G), hence the same (W_k(G)), supports multiple distinct 1-cyclotomic orientations.

Therefore:

[
oxed{	ext{underlying }W_k(G)
otRightarrow	ext{ a unique orientation on the free-pro-p adjacent class}.}
]

This is stronger than a finite-window counterexample: it is an **object-level non-identifiability** obstruction. No carrier constructed solely from the un-oriented finite window can recover an orientation that is not intrinsic to the underlying group.

Classification:
- adjacent-class un-oriented orientation identifiability for free pro-p groups: **FAIL / CLOSED**;
- reason: the target is not single-valued on the underlying object;
- this does not contradict Demuškin T0, because Demuškin uniqueness is precisely the missing rigidity.

## 5. What this tells us about the right general theorem

The useful generalization is not "all 1-cyclotomic pro-p groups". The correct prerequisite is:

> **orientation rigidity:** the admissible underlying group (G) carries a unique target orientation in the declared orientation class.

Only after orientation rigidity is established does finite-window observability become a meaningful inverse problem.

Thus the natural hierarchy is:

[
	ext{orientation rigidity}
;Longrightarrow;
	ext{finite-window identifiability}
;Longrightarrow;
	ext{admissible realization/coarseness}.
]

Demuškin groups pass the first gate; free pro-p groups fail it.

This is a genuine boundary theorem for the broader program, because it identifies the precise hypothesis that was silently supplied by the Demuškin classification.

## 6. Result classification

- A–D as a complete admissible-category definition: **FAIL / CLOSED — insufficient to exclude re-encoding**.
- Minimal-sufficiency analogy: **PASS / LOCAL — factorization preorder only**.
- (X_{ab}) terminology: **FAIL / CLOSED — misnamed; use associated graded object**.
- (X_{ab}) as a same-family new carrier: **FAIL / CLOSED — presently q-classification re-encoding**.
- (X_{cohom}) with explicit (chi)-twist: **FAIL / CLOSED — target-circular**.
- Free-pro-p adjacent-class orientation identifiability from un-oriented (W_k): **FAIL / CLOSED — object-level non-identifiability**.
- General orientation-rigidity prerequisite: **PASS / LOCAL** as the correct next structural axiom, not yet a full theorem for a broad class.

## 7. Next authorized branch

The next branch is **not** another carrier inside the standard Demuškin family.

Authorized target:
[
	ext{find an adjacent class } mathcal C'
	ext{ with orientation rigidity but without q-classification,}
]
then test whether a finite window determines the rigid orientation.

Candidate classes should be screened in this order:
1. a class with a canonical/unique orientation;
2. a class not classified solely by the Demuškin q-parameter;
3. an intrinsic finite filtration with a meaningful extension/deformation layer;
4. a target whose finite observability is not an immediate restatement of classification.

No large computation is authorized until such a class passes Object/Input/Functoriality/Gauge/Orientation bridge/q-blindness/Separation/Novelty/Stop.

## 8. Final boundary

The current research has established a clean three-way separation:

[
oxed{
egin{array}{c}
	ext{standard Demuškin:}\
W_kRightarrow[chi_k],quad k	ext{-class lower bound sharp,}\
	ext{but same-family coarsest realization is classification-equivalent;}
\[2mm]
	ext{free pro-p adjacent class:}\
	ext{orientation is not intrinsic to }G,	ext{ so }W_k	ext{-only recovery is impossible;}
\[2mm]
	ext{remaining genuine problem:}\
	ext{find an orientation-rigid adjacent class where finite observability is nontrivial.}
end{array}}
]

This is the current stopping boundary for the branch.
