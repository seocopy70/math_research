# GATE T — GENERALIZATION CLAIM / INDEPENDENT REVIEW REQUIRED — 2026-10-03

## Reported new result

A new hand proof is reported for the relative relation-window threshold in the stress family, extending to general odd prime p, a>=1, and even rank d>=2:
n_sep^rel(s)=p^s+1.

The reported proof replaces the earlier generator-by-generator survival argument with an explicit test group E'. In E', z has order p^(s+1), y acts on z by u=1-q with q=p^a, and the defining relation is realized as z^(p^s)=r. The claimed consequences are:
1. no choice of lift can make r trivial, hence the pushed-out finite extension is nonsplit;
2. z^(p^s) has exact Zassenhaus depth p^s, so it survives at depth p^s+1;
3. nonsplitting descends back to the original marked extension by quotient/pushout naturality;
4. higher even rank is reduced by sending extra Demushkin generators to 1.

GAP cross-checks are reported for 10 cases with p=3,5,7 and s<=4, including the previously unresolved s=3,n=28 boundary, and agree with earlier direct W computations.

## Correction from critical review (2026-10-03)

The following points are now explicitly corrected in this audit.

1. The suggestion that exact depth of z^(p^s) can be proved by a cyclic quotient is **withdrawn**. In the proposed E', the relation [z,y]=z^(-q) puts z^q in the commutator subgroup; when a<=s, z^(p^s) dies in the abelianization. Hence there need not be a cyclic quotient in which z has order p^(s+1). The exact-depth step must instead be established by the filtered-algebra calculation used in the proof, with its coefficient ring and filtration stated precisely.
2. The proof's use of F_p[[E']] must not be conflated with the Z_p[[G]] I-adic filtration. The relevant standard identification is the mod-p completed group-algebra augmentation filtration for the p-Zassenhaus series; the proof should name the exact theorem rather than saying vaguely “I-adic = normal-word degree.”
3. The concrete E' construction and the calculation phi(r)=z^(p^s) are reported to be present in the proof note. They still need line-by-line verification, but their absence is no longer an identified gap.
4. A Q-equivariance requirement is unnecessary. It is enough to exhibit the stated surjective homomorphism Psi and the commutative diagram with D, and then prove the extension/nonsplitting implication.
5. The lift-independence calculation is reported complete: since ker(E' -> D)=<z>, lifts differ by z-powers (z^i x, z^j y), so the section obstruction must be checked against exactly those changes.
6. The d>=4 reduction is not justified by the false general slogan “a split extension remains split under every quotient.” The actual proof uses the fact that the extra generators map into the abelian kernel <z>, so their mutual commutators become trivial. That specific argument is the one to audit.

## Current classification before independent proof audit

- Reported general relative threshold: CONDITIONAL / pending independent proof audit.
- Computational cross-checks: PASS / LOCAL.
- Orientation recovery: OPEN; the result separates s with a fixed a and does not by itself recover a or chi.
- p=2, q=0, s=0: OUT OF SCOPE.
- Unmarked/abstract-group realization: OPEN.
- Novelty: OPEN / literature audit required.

## Load-bearing proof point

The critical hand-proof step is the assertion that the relevant I-adic filtration agrees with the required normal/Zassenhaus word depth. This must be stated with the exact coefficient ring and filtration theorem used. No promotion to PASS/CLOSED is authorized until this identification, the construction of E', and the quotient/pushout implication are independently checked.

## Governance

Do not replace the older a=1 correction by this report merely because the claim is stronger. The older a=1 OPEN status remains authoritative until the new proof survives independent audit. If the proof closes the gap, supersede the older correction explicitly with a dated correction and preserve the historical record.

## Immediate next checks

1. Verify the exact definition and presentation of E'.
2. Verify the Q-equivariant quotient/pushout map from the original finite extension to E'.
3. Verify nonsplitting in E' by a lift-independent argument.
4. Verify exact Zassenhaus depth of z^(p^s), including the coefficient/filtration theorem.
5. Verify the d>=4 reduction.
6. Independently compare GAP cases, including p=3,s=3,a=1,n=28.
7. Perform novelty/literature search only after the theorem statement is fixed.
