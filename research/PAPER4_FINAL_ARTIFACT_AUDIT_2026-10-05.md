# Paper 4 — final artifact audit addendum — 2026-10-05

## Classification

**PASS / CLOSED — final local manuscript/PDF build audited.**

The repository's `paper4-tex-2026-10-04/paper4/main.tex` was re-read against the authoritative 2026-10-05 Paper 4 state. One stale sentence remained in its abstract: it referred to a direct same-window order-jump separation for 1<=a<s<t. That route is superseded and is not used in the clean final artifact.

The regenerated artifact removes that stale claim and contains the current theorem package:

- arbitrary-pro-p subgroup-depth comparison D_n(G) cap K subseteq D_{ceil(n/p^s)}(K);
- weighted-normal-form proof, not the rejected augmentation-ideal equality route;
- uniform optimality of the p^s compression factor in the free-pro-p class;
- lower-window blindness through p^s;
- intrinsic transfer obstruction epsilon_s;
- exact unmarked separation W_{p^s+1}(G_{s,s}) notcong W_{p^s+1}(G_{s,infinity});
- exact threshold n_sep(s)=p^s+1;
- complete critical-window a-classification;
- the r=z^p boundary against the arbitrary-relator degree-only claim.

## Local artifact

- TeX: `/mnt/data/Paper4_final_2026-10-05.tex`
- PDF: `/mnt/data/Paper4_final_2026-10-05.pdf`
- PDF pages: 6
- Build: pdflatex, two passes
- PDF SHA-256: `94523f44050b343bd788e6c6e451e779a4e5a8455b9ee94d1cf58aa5cf7e1b81`
- TeX SHA-256: `071580ca2ea6c355af5f524ed20067bb5f29795cd2a26d46ee816f6b722f68df`

## Artifact checks

PASS: LaTeX compilation.

PASS: PDF text extraction.

PASS: no stale 1<=a<s<t order-jump claim in the regenerated artifact.

PASS: no arbitrary-r degree-only theorem.

PASS: no arbitrary-pro-p sharpness claim.

PASS: final PDF visually checked on first and last pages; no clipping or page-boundary corruption observed.

The previously recorded 10-page PDF SHA in `PAPER4_REVISED_MANUSCRIPT_AUDIT_2026-10-05.md` refers to an earlier local binary that is not present in the current runtime. It must not be reused as the checksum of this final local PDF.

## Mathematical scope

Odd p, s>=2, even d, nondegenerate alternating quadratic initial relation. Degenerate quadratic intrinsic separation, s=1, arbitrary-relator degree-only visibility, arbitrary-pro-p sharpness, and unrestricted absolute minimality remain unpromoted.

## 2026-10-05 — CI publication freeze

The repository manuscript was reconciled with the authoritative Paper 4 state and the superseded abstract order-jump sentence was removed. The manuscript parameter scope is (age1); the critical-window (a)-classification is explicitly included. Bibliography entries were audited against publisher records and DOI metadata.

Final CI build:
- branch: `paper4-tex-2026-10-04`
- commit: `b3e0e3cd85f17ab038815030b2643e6be002c4fd`
- workflow: `paper4-tex-build`
- run: `37291334999`
- result: **PASS**
- artifact: `paper4-pdf`, id `11337135583`
- PDF: 17 pages, 423897 bytes
- PDF SHA-256: `85d5bd7793a8ba271c6a883ed4e0f7ca1849fc283c821a6cf92c84d56a4601ad`
- source blob SHA: `13f50f4ff38f528d17f1cbaaa737bf12af2c5084`
- source SHA-256: `b5169596ab6a84d693e66fb0138ceecbd10eda925cf341ef44a4a677674b65ab`
- artifact ZIP digest: `sha256:13d97ff0e3a9cbf762906a610e51cb9068d03a4d9b07dfc827448b792b0d5885`

CI audit passed:
- LaTeX compilation;
- PDF text extraction;
- title/author presence;
- reference section presence;
- absence of the superseded direct order-jump wording;
- PDF artifact existence;
- source/PDF checksum manifest generation.

The earlier local 6-page artifact and its SHA are **HISTORICAL / SUPERSEDED** and must not be cited as the final publication PDF.

**Final classification: PASS / CLOSED — publication artifact frozen.**
