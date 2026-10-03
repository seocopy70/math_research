# Documentation Architecture — source-of-truth policy
Last reviewed: 2026-10-04

## Purpose
Keep the complete research record without forcing current research to carry the weight of its entire history.

## Canonical roles
| File/area | One question | Role |
| CURRENT_STATE.md | What is true/current now? | LIVE |
| RESEARCH_MAP.md | How do pieces depend on one another? | LIVE MAP |
| research/02_EVIDENCE_INDEX.md | What evidence supports each claim? | LIVE EVIDENCE INDEX |
| research/00_RESEARCH_LOG.md | What changed, when, and why? | HISTORICAL LEDGER |
| research/03_CONVENTIONS_AND_IMPLEMENTATION.md | What computational conventions bind? | LIVE RULES |
| research/DOCUMENTATION_ARCHITECTURE.md | Where does a new record go? | LIVE META-RULE |
| research/archive/ | What was important but is not current? | ARCHIVE |
| plans/ | What is proposed but not established? | PLANNING |

## Archive rule
Archive means preserve, not delete. A superseded document remains searchable with its original content. The archive index records what it contains, why it was preserved, whether it was superseded, and which current document replaced its role. The archive is not an alternate source of truth.

## Status vocabulary
CLOSED = settled for stated scope.
OPEN = unresolved.
FAILED = proposed claim/route is false or tested construction failed.
HISTORICAL = provenance only.

Evidence quality is separate: PASS, LOCAL, NONE.
LOAD-BEARING is a priority flag, not a research state.

## Anti-duplication
Put the authoritative statement in CURRENT_STATE or the relevant evidence record; dependencies in RESEARCH_MAP; evidence pointers in EVIDENCE_INDEX; historical evolution in LOG/archive. Do not duplicate live claims across overview files.

## Update rule
When current truth changes:
1. update CURRENT_STATE;
2. update EVIDENCE_INDEX if evidence changes;
3. update RESEARCH_MAP only if dependencies change;
4. append one concise correction/supersession entry to 00_RESEARCH_LOG;
5. archive a dated old overview only when its orientation materially changes.

## Safety
No historical document is destroyed during documentation refactoring. Replaced live documents are copied to the dated archive and linked from ARCHIVE_INDEX.

## Retrieval
If you remember a topic but not its filename:
1. search ARCHIVE_INDEX;
2. follow its topic/path pointer;
3. search 00_RESEARCH_LOG for the transition date;
4. inspect the archived audit/result.

This prevents the “record exists but nobody remembers where” failure mode.