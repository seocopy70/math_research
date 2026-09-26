# Successor submission status — 2026-09-26

## Submission candidate

- Manuscript: `paper/successor_main.tex`
- Submission branch: `successor-submission-2026-09-26`
- Base: `successor-publication-candidate-2026-09-26`
- PR: #3
- Head commit: `481fb1659716fe5d6000c40f2701d3adb49415d0`

## Referee repairs completed

1. Formally defined (n_{\mathrm{aff}}(k;G)).
2. Corrected the main theorem's malformed quantifier sentence.
3. Made the factorization/coboundary statement precise.
4. Added an explicit abelianization argument for the (f<k) finite-depth distinction.
5. Recast the free-pro-(p) boundary at the correct finite-level cohomological statement; the unsupported claim that the lifting property automatically transfers to the finite quotient was removed.
6. Explicitly stated that the principal contribution is the exact sharp factorization window, while recognition is a boundary result.
7. Preserved the conditional novelty wording.

## Current mathematical classification

- Main affine finite-window theorem: **PASS / CLOSED**
- Category-relative sharpness: **PASS / CLOSED**
- Rank-two boundary: **PASS / CLOSED**
- Finite-depth (f)-collapse: **PASS / LOCAL**
- Factorization vs recognition: **PASS / CLOSED**
- Free-pro-(p) information-loss boundary: **PASS / CLOSED**
- Finite Demushkin free products: **PASS / CLOSED**
- Absolute carrier minimality: **OPEN / category-dependent**
- Broader elementary-type uniformity: **OPEN / not claimed**
- Exact novelty/priority: **OPEN / CONDITIONAL**

## CI gate

A GitHub Actions run for the submission commit was started:

- Workflow: Build successor manuscript
- Run: 22
- Run ID: `36211977926`
- At the time of this record: **IN PROGRESS**

The existing publication-candidate branch had already passed the exact successor build and PDF verification before this submission-repair branch. The final submission branch requires the new CI run to close before treating the package as technically release-ready.

## Release gate remaining

1. Close the new CI build/verification run.
2. Preserve the resulting PDF artifact.
3. Freeze the submission source at the verified commit.
4. Keep the independent referee audit and this status record alongside the source.
5. Only after the CI gate is green, prepare the final external-submission package.

No broader mathematical expansion is required before submission.
