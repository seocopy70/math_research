# FOLLOW-UP REPAIR STAGE — 2026-09-26

## Purpose

This is the next publication-preparation stage after the authoritative 2026-09-26 successor audit. The frozen publication manuscript `paper/main.tex` was not modified.

## Work completed

1. **Sharpness proof repaired conceptually and checked locally.**
   - The false claim that the canonical ((1-p^f)^{-1}) orientation must generate (U_{1,k}) was removed.
   - For (f<k), the canonical orientation together with (z(x_1)=1) gives the lower-bound witness:
     [
     z(x_1^{p^{k-1}})=p^{k-1}
otequiv0pmod {p^k}.
     ]
   - For (fge k), the independent witness
     [
     ho(x_1)=1,quad ho(x_2)=1+p,quad z(x_1)=0,quad z(x_2)=1
     ]
     gives the same lower bound, using
     [
     v_p((1+p)^{p^{k-1}}-1)=k.
     ]
   - Therefore the affine-category statement
     [
     n_{m aff}(k)=p^{k-1}+1
     ]
     is the controlling sharpness theorem for all (dge2, fge1).

2. **The obsolete (d=2,f>1) failure branch is superseded.**
   It must not appear in the successor manuscript.

3. **The mixed-commutator gate is treated as closed.**
   For (T_n(G)=G/P_n(G)), truncation is the reflector onto the class (P_n=1). Hence it preserves pro-(p) coproducts after reflection:
   [
   T_n(G_1*_pG_2)
   cong
   T_n(G_1)*_pT_n(G_2)ig/P_n(T_n(G_1)*_pT_n(G_2)).
   ]
   Thus mixed commutators lie in the reflected (P_n)-kernel and are killed at the same finite window.

4. **The positive uniformity claim is narrowed.**
   The theorem is supported for finite free pro-(p) products of Demushkin blocks with their canonical orientations. The broader recursively defined (mathcal{ET}_p^{rig}) class remains OPEN until its closure operations are explicitly defined and verified.

5. **The bare-quotient impossibility is narrowed.**
   The negative statement concerns only an isomorphism-natural/functorial selector whose input is the bare abstract quotient (Q_k). It does not exclude selectors using quotient maps, markings, distinguished subgroups, coefficient actions, or extension data.

6. **Newton/Jacobian algorithmic claims are removed from the structural theorem.**
   They require an explicit input model and a separate lifting/convergence proof.

7. **Bibliography is now a publication-critical task.**
   The successor source must use actual citation commands and a verified bibliography rather than prose-only references.

## Local build

A clean three-pass LaTeX build of a newly assembled structural working draft was completed locally:
- pages: 5
- exit status: 0
- no LaTeX Error/Warning/undefined-reference matches in the final pass.

This PDF is a **working reconstruction**, not a byte-for-byte repair of the uploaded `followup_merged.tex`. The uploaded source is not currently present in the GitHub repository, so overwriting it would risk silently changing un-audited text.

## Current classification

- affine sharpness theorem: **PASS / CLOSED**
- (d=2) boundary: **PASS / CLOSED**
- mixed-commutator factorization: **PASS / CLOSED**
- finite Demushkin free-product uniformity: **PASS / CLOSED**
- broad (mathcal{ET}_p^{rig}) uniformity: **OPEN**
- bare abstract-(Q_k) impossibility: **PASS / LOCAL**
- Newton algorithmic claim: **OPEN / separated**
- original uploaded `followup_merged.tex` repair: **OPEN / source-recovery dependent**
- successor publication novelty: **OPEN / CONDITIONAL**

## Next authorized step

Recover the exact uploaded `followup_merged.tex` source (or place it in the repository as the authoritative successor source), then apply the above repairs **without reconstructing unverified passages from memory**. After that:
1. compile three passes;
2. run an independent mathematical audit against the repaired source;
3. add verified bibliography/citations;
4. run CI from the exact successor commit;
5. only then promote the successor manuscript from working draft to publication candidate.
