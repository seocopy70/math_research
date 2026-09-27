# Literature archive

This directory stores primary-source literature used for theorem-level verification.

## Directory policy

- `originals/` — immutable copies of primary-source PDFs or source archives obtained for research verification.
- `audits/` — project-specific theorem-by-theorem audits and reusable methodological extractions.
- `index.md` — catalog of sources, versions, identifiers, and the research questions for which each source is authoritative.

## Recommended workflow

1. Put the original paper/source archive in `originals/`.
2. Record the exact arXiv identifier, version, title, authors, and date in `index.md`.
3. When a theorem is used, create or update an audit under `audits/` with the exact theorem/proposition and its logical boundary.
4. Do not treat an AI summary as a primary source; verify important claims against the stored original.

## Naming

Prefer names such as:

`arXiv-1103.1508v1.tar.gz`
`arXiv-1103.1508v1.pdf`

Keep the original version number. If a later version is relevant, store it separately rather than silently replacing the earlier source.

## Copyright / repository visibility

Before committing full-text papers, check that the repository's visibility and the paper's license/redistribution terms permit storing the full text. If not, keep only bibliographic metadata, links, and project-authored audit notes in the repository.