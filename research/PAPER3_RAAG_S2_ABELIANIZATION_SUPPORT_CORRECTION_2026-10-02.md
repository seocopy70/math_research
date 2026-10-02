# PAPER 3 — CORRECTION: FINITE-WINDOW ABELIANIZATION DOES NOT CLOSE S2 — 2026-10-02

## Decision

A critical correction is required to the preceding exploratory note. The proposed claim that finite-window abelianization directly recovers the sinkhole/special support is incorrect.

For the standard special-edge model

    G=<v,w | w v w^{-1}=v^{1+q}>

the canonical orientation is nontrivial on the conjugating sinkhole w and trivial on the acted-on generator v. Abelianization gives v^q=1, so its q-sensitive torsion support is source/base-side information, not the sinkhole support.

Therefore the previous abelianization-only closure of S2 is withdrawn.

## 1. Correct two-vertex model

For the basic special edge,

    w v w^{-1}=v^{1+q},
    theta(v)=1, theta(w)=1+q.

Abelianization gives

    v^q=1,

but no corresponding torsion relation on w. Thus the torsion-bearing direction and the orientation-bearing direction are different.

## 2. What abelianization does give

For q=p^f<p^k, the finite-window abelianization can contain a canonical q-sensitive torsion subgroup such as A_k[p^{k-1}]. This is a useful intrinsic control invariant and can recover q in the visible regime.

Status: PASS / LOCAL — q-sensitive torsion/source-side control.

## 3. Why abelianization cannot define the orientation

The canonical orientation is a homomorphism to an abelian target, but it is not obtained by sending the abelianization torsion subgroup to 1+q. In the two-generator model the torsion relation is on v while theta is nontrivial on w.

Therefore the implication

    torsion support = sinkhole support

is false.

## 4. Correct S2 factorization

The more accurate route is

    W_k
      -> q-sensitive torsion/source-side relation support
      -> intrinsic conjugation/action defect
      -> sinkhole support
      -> [theta mod p^k].

The full group, not merely its abelianization, must encode the asymmetric conjugating direction.

## 5. Relation-module target

With a minimal filtered presentation 1 -> R -> F -> W_k -> 1, the special relation has the asymmetric form

    [w,v] v^{-q}=1.

The q-power component identifies the acted-on/base direction; the conjugating variable w carries the canonical orientation. Hence S2 requires an intrinsic support construction for the conjugating side of the relation defect.

The natural candidates remain a filtered relation module, an extension-class/action module, or an equivalent central/Frattini quotient.

## 6. Cohomological target

The minimal-presentation transgression identifies the relation module modulo p-powers and commutators with H^2. The special relation contributes an asymmetric class. The required sinkhole support must be extracted from that asymmetry, not from the torsion component alone.

## 7. Literature check

The oriented pro-p RAAG literature gives the special relation and canonical orientation in the two-generator model, and the minimal-presentation/transgression description of H^2. These support the distinction above.

## 8. Corrected gate table

| Item | Status |
|---|---|
| Zassenhaus degree q=p^f | PASS / CLOSED |
| Special relation wvw^{-1}=v^{1+q} | PASS / CLOSED |
| Candidate N_k=p^{k-1}+1 | CONDITIONAL |
| q-sensitive torsion in finite-window abelianization | PASS / LOCAL |
| Abelianization alone recovers sinkhole support | FAIL / CLOSED |
| Abelianization as q/source-side control | PASS / LOCAL |
| Intrinsic conjugation/action defect | OPEN / LOAD-BEARING |
| Sinkhole-support reconstruction | OPEN / LOAD-BEARING |
| W_k => [theta mod p^k] | OPEN |
| Presentation-level sinkhole reading | FAIL / CLOSED |

## 9. Immediate next attack

Attack the two-vertex special-edge model first:

    G_q=<v,w | wvw^{-1}=v^{1+q}>.

Determine whether W_k contains an abstract, isomorphism-invariant object that distinguishes the conjugator w from the torsion-bearing base direction v. Then test stability under ordinary edges, multiple sinkholes, and free-product/elementary-type constructions.

If an abstract finite-window automorphism exchanges the two roles while preserving W_k, S2 has a no-go. If not, the induced conjugation/extension module is the likely carrier.

## 10. Final decision

The current user conclusion that abelianization is a control invariant but does not finish S2 is correct. The abelianization shortcut to sinkhole support is rejected.

Current frontier:

    q-sensitive torsion support -> intrinsic conjugating/sinkhole support

Status: OPEN / LOAD-BEARING.