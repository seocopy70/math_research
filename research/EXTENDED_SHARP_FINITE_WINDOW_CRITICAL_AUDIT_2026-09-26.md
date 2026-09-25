# EXTENDED SHARP FINITE-WINDOW CRITICAL AUDIT — 2026-09-26

## Scope

Audit target: uploaded `sharp_finite_window.tex`, proposed as an expanded successor to the current finite-window Kummer-recognition manuscript.

Audit standard: publication-level mathematical attack, following the Research Continuity Protocol. The audit distinguishes theorem validity, proof validity, novelty, and algorithmic claims.

## Executive classification

- Core finite-window factorization mechanism through the corrected Zassenhaus quotient: **PASS / CONDITIONAL**
- Current main theorem as written: **FAIL / CLOSED**
- Current commutator cocycle formula: **FAIL / CLOSED**
- Current explicit selector (ho=(1,1+p^f,ldots)) for all (k): **FAIL / CLOSED**
- Canonical orientation value for the stated relator: must be ((1-p^f)^{-1}) in the second coordinate; current manuscript disagrees for (kge3): **FAIL / CLOSED**
- Sharpness/minimality of the recognition window: **OPEN**; current proof establishes only a representation-factorization threshold, not recognition minimality
- Complete q-collapse classification: **PASS / LOCAL** pending a fully written quotient-isomorphism proof and parameter conventions
- Newton algorithm: **OPEN / CONDITIONAL**; arithmetic lifting idea is plausible, but current input model and complexity claim are underspecified
- Publication novelty: **OPEN / CONDITIONAL**

## 1. Load-bearing fatal error: crossed-cocycle commutator formula

The manuscript defines left crossed homomorphisms by
(z(gh)=z(g)+ho(g)z(h)), and uses ([a,b]=a^{-1}b^{-1}ab).

With (A=ho(a)), (B=ho(b)), direct expansion gives
[
z([a,b])
=A^{-1}B^{-1}igl((1-B)z(a)+(A-1)z(b)igr).
]
The factor (A^{-1}B^{-1}) is missing from equation (49).

Thus equation (49) is false under the manuscript's own cocycle and commutator conventions.

This is not cosmetic: it changes the Fox obstruction equations at every precision beyond the first residue layer.

## 2. Consequence: the claimed all-k selector is wrong

For the stated relator
(r_f=x_1^{p^f}[x_1,x_2]cdots)
and after the forced condition (a_1=1), the correct first coefficient is
[
F_1=S_{p^f}(1)+a_2^{-1}-1
=p^f+a_2^{-1}-1.
]
Therefore (F_1=0) gives
[
a_2=(1-p^f)^{-1},
]
not (a_2=1+p^f).

The two coincide modulo (p^2), which explains why the old mod-9 (p=3,q=3) computation survives, but they differ from (p^3) onward. Example:
[
p=3,quad f=1,quad k=3:
qquad
(1-q)^{-1}=(-2)^{-1}equiv13pmod{27},
]
whereas
(1+q=4pmod{27}).

The external literature independently records the canonical value for this relator as ((1-q)^{-1}). See Labute's classification and later expositions. This means the current manuscript's Theorem 3/U4/Main Theorem are mathematically false as written for (kge3).

## 3. The 'sharp window' theorem overclaims what is proved

The current theorem says the window (p^{k-1}+1) is minimal for recognition. Its proof instead establishes a different statement:
[
P_n(G)subseteqkerpsi
quad	ext{for every affine representation }psi:G	o S_k.
]

Even if that factorization threshold is sharp, it does NOT imply that no smaller quotient could carry some other intrinsic predicate that recognizes the canonical orientation.

The research state explicitly kept Zassenhaus-window minimality **OPEN**. The expanded draft silently promotes this open issue to a theorem.

Correct publication wording should separate:

1. **representation-universal factorization threshold**: (p^{k-1}+1);
2. **recognition minimality among all intrinsic carriers/predicates**: still OPEN unless separately proved.

## 4. The sharpness proof contains a second direct error

Line 137 says the canonical
(chimod p^k) is surjective onto (U_{1,k}) because
(chi(x_2)-1=pcdot	ext{unit}).

For (fge k), the canonical value is
[
chi(x_2)=(1-p^f)^{-1}equiv1pmod{p^k},
]
so (chimod p^k) is trivial, not surjective.

Hence the displayed attainment proof does not establish sharpness for the claimed range 'all f'. A separate noncanonical affine representation would have to be constructed if the factorization-threshold sharpness statement is retained.

## 5. Newton section inherits the same wrong equations

The Newton iteration is based on the manuscript's (F_i). Once the commutator formula is corrected, the higher-level nonlinear system changes.

The Jacobian modulo (p) may still be invertible and the Henselian lifting strategy may survive, but this must be recomputed from the corrected (F_i). The current (O(kd)) theorem therefore cannot be retained without a fresh proof.

Also, (O(kd)) is only a scalar-arithmetic complexity statement for solving the displayed normal-form equations. It is not yet an intrinsic algorithmic complexity bound for taking an abstract finite group (Q_k) as input, computing its abelianization, finding a distinguished presentation, and producing the canonical character.

## 6. q-recovery claim needs sharper input conventions

For (f<k), the stated abelianization calculation plausibly recovers (f), hence (q=p^f), from the isomorphism type of (Q_k).

For (fge k), (Q_k^{(f)}cong Q_k^{(infty)}), so only the collapse class (fge k) is visible.

This is compatible with the intended information boundary, but the manuscript should say explicitly whether 'recoverable from (Q_k)' means:
- from the abstract isomorphism class,
- from a marked quotient with distinguished generators,
- or from the concrete normal-form presentation.

The algorithm section currently mixes these three input models.

## 7. U5 is currently redundant for the stated standard-family theorem

Once U3 is correctly established and the corrected explicit Fox coefficients are computed for the normal-form relator, the uniqueness of the candidate can be proved directly at every (k). The U5 intrinsic induction is therefore not load-bearing for this particular standard-family theorem.

This is potentially useful rather than harmful: the expanded paper can become cleaner by separating:
- a direct explicit-selector theorem for the normal-form family;
- the stronger intrinsic U5 mechanism as a separate structural theorem only if its hypotheses and naturality are independently stated.

If U5 is retained as the engine of the main theorem, the manuscript should explain why this stronger route is needed rather than simply importing a presentation-local calculation.

## 8. Literature boundary

The canonical Demushkin orientation and its uniqueness as the Kummerian orientation are established prior art, including Labute and later treatments. The modern literature also formulates Kummerianity directly through the same finite coefficient-extension maps.

Therefore novelty cannot be claimed for canonical-orientation recovery itself. The possible new contribution is narrower:
- factorization of the finite Kummer predicate through the specific Zassenhaus quotient;
- a q-blind selector formulated on that finite quotient;
- the exact information-loss/collapse boundary;
- possibly an effective finite-level reconstruction algorithm.

Each of these must be separated from the classical full-group Kummerian theorem.

## 9. Required repair order

Before any further broadening or submission:

1. Correct equation (49) from first principles under the chosen left/right cocycle convention.
2. Recompute all (F_i) exactly.
3. Reprove U3 with the corrected coefficients.
4. Verify the selector gives ((1-p^f)^{-1}) at every (k).
5. Recompute the Newton Jacobian and lifting recurrence.
6. Separate factorization-threshold sharpness from recognition minimality.
7. Either prove factorization sharpness for all (f), or restrict the theorem.
8. Rewrite the q-recovery and algorithm input model precisely.
9. Perform a literature comparison specifically against the finite-quotient selector formulation.
10. Only then decide whether this is a genuine successor paper or a corrected generalization of the existing manuscript.

## Final research classification

**The proposed extension contains a potentially strong and publishable direction, but the submitted draft is not currently mathematically sound. The central obstruction is localized and repairable: the crossed-cocycle commutator identity is wrong, and that error propagates directly into the all-k selector, q-recovery formula, and Newton system. The sharp-minimality claim is a separate overreach and should remain OPEN until a genuine recognition lower bound is proved.**

No closed research branch is reopened by this audit.
