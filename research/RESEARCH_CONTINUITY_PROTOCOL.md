# RESEARCH CONTINUITY PROTOCOL — 2026-09-19

## Purpose

This document is the operational contract for continuing the mathematics research across new chats/windows. It is subordinate to the mathematical content of RESEARCH_MAP.md, CURRENT_STATE.md, and 00_RESEARCH_LOG.md, and is intended to prevent loss of methodology, stage criteria, negative results, and decision boundaries.

## 1. Mandatory restoration order

At the beginning of every new research session:

1. Read `RESEARCH_MAP.md` first for the global mathematical map and authoritative current-status header.
2. Read `CURRENT_STATE.md` for the latest active gates, dependencies, and immediate next tasks.
3. Read `research/00_RESEARCH_LOG.md` for chronology, corrections, failed approaches, and evidence provenance.
4. Read the relevant stage/audit document before executing work in that branch.
5. Treat the latest authoritative header and explicit later corrections as controlling over stale historical labels.

Memory or conversational recollection is not an authoritative substitute for these files.

## 2. Fixed research decision procedure

Every substantive branch follows:

**pre-check → define object/input → prove legitimacy → execute only if authorized → independently verify → classify result → record immediately.**

No computation is authorized merely because a higher-order object exists.

## 3. Required pre-computation tests

Before substantial computation, answer:

1. **Object:** What exact mathematical object is being constructed?
2. **Input:** What information is allowed, and what is excluded?
3. **Functoriality:** What maps/isomorphisms induce maps of the object?
4. **Gauge:** Which presentation/lift/normalization changes are quotiented, and why?
5. **Orientation bridge:** Where is the precise map to the crossed-derivation/orientation data?
6. **q-blindness:** Is q absent from the definition?
7. **Separation:** Can relevant q=3 and q=∞ cases be distinguished without inserting q?
8. **Novelty:** Is the result stronger/different than an existing theorem or merely a reproof?
9. **Stop:** If any of 1–5 fails, stop computation and return to definitions.

## 4. Minimum theorem-quality thresholds

A result is not promoted to a principal mathematical contribution unless, as applicable, it establishes:

- non-tautological definition;
- intrinsic/presentation-independent meaning;
- precise factorization or reconstruction theorem;
- a genuine negative boundary or separation result;
- non-redundancy/minimality only relative to an explicitly defined admissible category;
- clear distinction between hand verification of known formulas and genuinely new information.

The following are validation evidence, not novelty by themselves:
- recovering (chi(x_2)=(1-q)^{-1}) from a known presentation;
- reproducing a known dimension/module calculation;
- a successful computation without an intrinsic interpretation.

## 5. Current stage hierarchy

The principal theorem program is:

**D0 definition → D1 intrinsicity → D2 orientation bridge → D3 carrier/coarseness → D4 independent literature comparison.**

Current target:
[
	ext{intrinsic filtered input}
	o
	ext{coarsest defensible carrier}
	o
	ext{natural coefficient functional}
	o
	ext{unique finite-level orientation}
	o
	ext{inverse limit}.
]

Current established boundaries:

- bare associated graded/quadratic shadow (
otRightarrowchimod9): CLOSED;
- projective degree-(2,3) enriched relation jet (Rightarrowchimod9): CLOSED at the stated standard hypotheses;
- coarsest quotient (overline J_3=[(R,p(P))]): CLOSED in the specified linear-evaluation quotient category;
- fixed q=3 exact filtered relation/evaluation carrier (Rightarrowchi): CLOSED;
- compatible full filtered relation-jet tower (Rightarrowchi): CLOSED;
- universal bounded-degree + finite-precision carrier (Rightarrow) full (chi): FAIL/CLOSED;
- naive Z_3 restricted-Lie scalar extension: FAIL/CLOSED;
- non-tautological concrete exact Z_3 compression analogous to (([R],p(P))): OPEN;
- absolute minimality among arbitrary invariant categories: ill-posed until the admissible category is fixed;
- M1 intrinsic carrier functor, M2 non-tautological orientation factorization, M3 independent comparison/obstruction remain the governing structural objectives where not already closed by the stated enriched-carrier formulation.

## 6. Literature as reusable methodology

Full-paper audits are not merely citations. Extract and preserve reusable proof methodology separately from claims:

- canonical object → functorial obstruction → explicit computation;
- presentation/lift independence before numerical interpretation;
- subgroup/cohomological tests as independent structural checks;
- explicit separation of what a paper proves from what it does not prove.

For every important paper, record:
1. object constructed;
2. input data;
3. invariance/naturality mechanism;
4. obstruction/evaluation mechanism;
5. verification method;
6. exact logical boundary;
7. possible map/factorization into the current project.

Never infer that a method transfers merely because the subject matter is similar.

## 7. Stage result classification

Every stage conclusion must be labeled one of:

- **PASS / CLOSED:** theorem-level target established under explicit hypotheses;
- **PASS / LOCAL:** a computation or lemma is verified but does not close the main structural gate;
- **FAIL / CLOSED:** candidate is ruled out or a no-go theorem is proved;
- **OPEN:** a precise unresolved theorem/definition remains;
- **CONDITIONAL:** valid only under named hypotheses;
- **HISTORICAL / SUPERSEDED:** retained for traceability but must not control current decisions.

A PASS must state exactly what it proves and what it does not prove.

## 8. Continuity rule for new chats

A new chat must reconstruct the state from repository artifacts, not from conversational memory. If a later document contradicts an earlier one, use the later authoritative correction and record the supersession explicitly. Do not silently revive closed approaches.

Before any new branch, state internally (and in the record when material) the active gate, its predecessor evidence, its failure conditions, and the consequence of PASS/FAIL.

## 9. Publication-discipline rule

Before calling the work a new theorem or discovery, perform a final audit:

- Is the statement genuinely stronger/different from known orientation formulas?
- Is the carrier defined without (chi) or q?
- Is intrinsicity proved?
- Is the reconstruction map explicit and natural?
- Is there a sharp negative boundary?
- Is any minimality claim relative to a declared category?
- Is the literature comparison complete enough to rule out immediate rephrasing?
- Can another mathematician reproduce the logical chain without the chat history?

If the last answer is no, the research is not yet continuity-complete.

## 10. Record-keeping rule

Important definitions, corrections, PASS/FAIL decisions, frozen boundaries, next tasks, and literature-method transfers must be recorded in the appropriate authoritative artifact immediately. The log records chronology; CURRENT_STATE records active state; RESEARCH_MAP records the global structure; this protocol records the method for maintaining continuity.
