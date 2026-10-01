# THREE PAPER PUBLICATION-STYLE FINALIZATION — 2026-10-01

## Scope
A publication-style cleanup was applied to the three already-audited manuscript sources. This revision is **editorial/style-only**: no theorem, proof, hypothesis, mathematical scope, or novelty classification was intentionally changed.

## Changes applied
- Removed the explicit Companion papers / placeholder-arXiv boilerplate.
- Removed repeated defensive novelty disclaimers and kept the literature boundary concise.
- Replaced informal "kills P_n" language with factorization/annihilation language.
- Made the Paper 2 identification \(p=q=3,\ f=1\) explicit.
- Standardized finite coefficient notation around \(A_k=\mathbb Z/3^k\mathbb Z\) and \(U_{1,k}=1+3A_k\), with multiplication understood.
- Tightened the introductions so the finite-information question is stated before the technical machinery.
- Tightened Paper 1 title to match its actual theorem scope.
- Tightened Paper 3 abstract to state the actual contribution directly rather than listing defensive non-claims.

## Authoritative style-final branches
- Paper 1: paper1-style-final-2026-10-01
  - source: paper/successor_main.tex
  - final CI run: 36796538885
  - PDF: 8 pages
  - PDF SHA-256: b4806dc7ed111ffeb3b93d5ef9066d958252fff132506a5d95f25dad76afe960
- Paper 2: paper2-style-final-2026-10-01
  - source: paper/main.tex
  - final CI run: 36797038430
  - PDF: 13 pages
  - PDF SHA-256: 97504d2bc5db7f668f2287d62bca902cde0b285b1a4b7ef11ffe58c0c8928e32
- Paper 3: paper3-style-final-2026-10-01
  - source: paper/main.tex
  - source-correct style build: 36797042460
  - PDF: 17 pages
  - PDF SHA-256: 3518e5f966401d48eae9c8b76b80fe7a9ba4e53f76bc4255edb66862082bf7ff

## Verification
- Paper 1 CI build/verification/package: PASS / CLOSED.
- Paper 2 CI build/verification/package: PASS / CLOSED.
- Paper 3 source-correct style-final build/verification/package: PASS / CLOSED.
- PDF text extraction and first-page visual inspection: PASS / CLOSED.
- No known "Put Put", "qq u a d a", "3j" source/rendering corruption, companion placeholders, or similar artifact contamination was found in the final PDFs.
- Mathematical research status is unchanged. Publication novelty remains OPEN / CONDITIONAL.

## Important workflow correction
The legacy Paper 3 workflow .github/workflows/paper3-build.yml targets the older paper3/main.tex application manuscript. The style-final branch therefore uses the dedicated source-correct workflow .github/workflows/paper3-style-final-build.yml to compile the authoritative paper/main.tex.

Classification: PASS / CLOSED — publication-style artifact finalization.
