# POST-PAPER-3 RESEARCH — Gate D three-attack intrinsic-carrier triage — 2026-10-01

## Scope correction

**Paper 3 본체는 완성·고정되어 있다.** 이 문서는 Paper 3 본체의 정리·증명·완성도를 재검증하는 문서가 아니다.

이 문서가 다루는 것은 Paper 3가 제시한 **후속 일반화 연구 프로그램**이다:
[
W_nlongrightarrow	ext{intrinsic carrier}longrightarrow	ext{global orientation}.
]

따라서 여기서 (t_2), full (delta)-family, intrinsic carrier 또는 Gate D가 실패해도 그 결과는 **Paper 3 본체의 FAIL이 아니다.** 실패하면 해당 후속 연구 branch만 닫는다.

## Frozen inputs

Paper 3 본체와 Paper 2 selector 결과는 이 branch의 **완료된 선행 입력**이다. 이를 다시 증명하거나 publication-completeness gate로 되돌리지 않는다.

## Purpose

The three attacks are applied to the **post-Paper-3 generalization branch**:
1. **Object attack** — exact finite-input object legitimacy.
2. **Intrinsicity attack** — presentation, relator, basis/Nielsen, coefficient-lift, and gauge independence; this is the first decisive battleground.
3. **Orientation-bridge attack** — a non-redundant map from a surviving carrier to finite orientation data.

The structural stop rule remains unchanged: if intrinsicity fails, close only this carrier branch; do not reopen Paper 3 or Paper 2.

## Current classification

- Paper 3 본체: **FROZEN / COMPLETE**.
- Paper 2 selector: **FROZEN / COMPLETE; no reproof authorized**.
- F2 operational branch: **CLOSED**.
- F1 pairwise finite-window threshold (q+1): **PASS / CLOSED** at declared two-object scope.
- (W_{10}	odelta)-family: **PASS / CLOSED** at audited fixed scope as a pre-existing input.
- single-vector (t_2) carrier: **FAIL / CLOSED**.
- genuinely new intrinsic/coarser post-Paper-3 carrier: **OPEN / LOAD-BEARING**.
- Paper 2 selector reproof: **NOT AUTHORIZED**.

## Immediate decision boundary

The first real battleground is **not whether Paper 3 is correct**. It is whether a genuinely new carrier extracted from the surviving finite-window/cohomological data exists and remains intrinsic.

The second battleground is whether such a carrier yields a non-redundant orientation bridge.

No (W_{11}/W_{12}) or new Fox computation is authorized merely to re-establish the frozen Paper 2/3 selector chain.

---

# PAPER 3 — Gate D three-attack intrinsic-carrier triage — 2026-10-01

## Purpose

This record fixes the immediate research sequence after the F2 operational closure and before any new large computation.

The three attacks are:

1. **Object attack** — is the proposed carrier an exact mathematical object determined by the declared finite input, or is it only a presentation-level construction?
2. **Intrinsicity attack (first decisive battleground)** — does the carrier survive presentation changes, relator changes, basis/Nielsen changes, coefficient-lift reparametrization, and orientation-choice changes as a genuine functorial object?
3. **Orientation-bridge attack** — if the carrier survives, is there a natural map from the carrier to the finite orientation datum, rather than a disguised insertion/reconstruction of the known orientation?

The stop rule is structural: if attack 2 shows essential presentation/orientation dependence, the carrier branch is FAIL/CLOSED and no deeper computation is authorized. If attack 2 survives but attack 3 is unresolved, status remains OPEN. If both survive, only then is further recognition/separation work authorized.

## Authoritative baseline checked

The current repository state was restored from:
- RESEARCH_MAP.md
- CURRENT_STATE.md
- research/00_RESEARCH_LOG.md
- research/RESEARCH_CONTINUITY_PROTOCOL.md
- research/PAPER3_GATE_D_FINITE_WINDOW_RECOGNITION_PRECHECK_2026-10-01.md
- research/INTRINSIC_CARRIER_FORMAL_GATE_PRE_MOD27_2026-09-20.md
- research/PAPER3_HA58_P4_D10_FULL_INTRINSICITY_AUDIT_2026-09-27.md
- research/PAPER3_GATE_A_W10_TO_LRHO2_2026-09-28.md
- research/PAPER3_GATE_B_W10_TO_DELTA3_FAMILY_RESULT_2026-09-28.md
- research/PAPER3_GATE_C_DELTA3_TO_CHI27_RESULT_2026-09-28.md

## Attack 1 — Object

The currently surviving fixed-scope chain is

W_10 -> L(rho_2) -> {delta_{3,rho_3}} -> chi mod 27.

At the audited scope:
- W_10 is a precise marked filtered finite object.
- L(rho_2) is a finite lift domain once the already-audited rho_2 is supplied/recovered.
- The delta family is a genuine cohomological connecting-map family.
- Gate B has a finite quotient construction of the delta family at the declared scope.
- The earlier single-vector t_2 compression is not an admissible replacement: it has a presentation-conjugation counterexample.

**Classification: PASS / CLOSED for object legitimacy at the audited fixed-scope chain.**

This does NOT establish that the chain is a new Paper 3 contribution; that redundancy boundary is already CLOSED against merely restating Paper 2.

## Attack 2 — Intrinsicity / presentation and orientation dependence

### Presentation/gauge test

The dangerous candidate is any compression of the delta family to a coordinate residual such as t_2.

The existing HA61-B5-12 witness is decisive:
r -> v r v^{-1} leaves the abstract group and the intrinsic connecting-obstruction family unchanged, while the proposed coordinate vector transforms as

t_2 -> t_2 + p

for suitable v in the frozen rank-four q=3 branch.

Therefore:
- a single canonical t_2 is **FAIL / CLOSED**;
- t_2/<p> is also insufficient;
- the diagonal (t_2,mu) quotient is not an admissible orientation carrier.

This is not merely a missing proof. It is an explicit gauge counterexample.

### Surviving carrier test

The full family rho_3 -> delta_{3,rho_3} is different. Each delta is defined cohomologically from a short exact coefficient sequence, and the family is natural under admissible group/coefficient-data isomorphisms once rho_2 is fixed.

Gate B further constructs the family from finite quotient cohomology at the audited W_10 scope, without a presentation or relator representative.

Therefore the currently surviving **full delta-family is not shown to be a presentation artifact**.

However, this does not yet prove that every proposed coarser carrier extracted from it is intrinsic. Any compression must itself be subjected to the same gauge test.

### Orientation-choice test

The indexing parameter rho_3 is allowed to vary over the full lift domain L(rho_2); it is not fixed to chi mod 27 in the definition of the delta family.

Thus the family itself does not insert the target orientation rho_3=chi.

But rho_2 is a previously recovered mod-9 orientation datum. Therefore the chain is intrinsically seeded by an already closed lower-level orientation carrier. This is legitimate for the audited recursive construction, but it means that a claim of an entirely orientation-free new carrier would be stronger and is NOT established by the current chain.

**Attack-2 classification: PASS / LOCAL for the full cohomological delta-family; FAIL / CLOSED for single-vector/compressed t_2 carriers; OPEN for any genuinely coarser new recognition carrier.**

This is the key boundary: the presentation-dependence attack does not kill the full delta family, but it kills the tempting coordinate compression. No further computation should be spent on t_2-style compression.

## Attack 3 — Orientation bridge

For the fixed Demushkin scope, the zero-connecting-map selector identifies the canonical mod-27 orientation, using the established Kummerian/Demushkin existence and the variation/cup-product uniqueness mechanism.

But as a Paper 3 novelty claim, this bridge is not sufficient by itself: the same selector mechanism is already part of the completed Paper 2 theorem assembly.

Therefore the bridge is mathematically available at the audited scope but is **not a new Paper 3 theorem** unless it is coupled to a genuinely new category-relative recognition statement or a strictly new intrinsic carrier.

**Classification: PASS / CLOSED as an existing fixed-scope selector bridge; FAIL / CLOSED as a standalone new Paper 3 novelty route; broader recognition bridge remains OPEN.**

## Immediate consequence

The three attacks do not justify another W_11/W_12 computation.

The surviving research question is now sharply narrowed:

> Is there a genuinely new intrinsic carrier, coarser than the already-completed Paper 2 selector chain but richer than the killed single-vector t_2 compression, that yields a category-relative finite-window recognition statement?

The first real battleground is therefore not existence of a presentation-independent delta family — that has survived — but whether a **non-redundant carrier extracted from it** survives all gauge/functoriality requirements.

## Stop rule

- If the proposed new carrier reduces to t_2 or an equivalent presentation coordinate: **FAIL / CLOSED**.
- If it depends on choosing chi mod 27 as input: **FAIL / CLOSED**.
- If it is only the full delta-family selector already proved in Paper 2: **FAIL / CLOSED on novelty/redundancy**.
- If it survives both gauge and redundancy tests but its orientation bridge is unresolved: **OPEN**.
- Only a surviving non-redundant carrier authorizes the next separation/threshold attack.

## Current research classification

- F2 operational branch: **CLOSED**.
- F1 pairwise finite-window threshold q+1: **PASS / CLOSED** at declared two-object scope.
- W_10 -> delta family: **PASS / CLOSED** at audited fixed scope.
- single-vector t_2 carrier: **FAIL / CLOSED**.
- new intrinsic/coarser Paper 3 carrier: **OPEN / LOAD-BEARING**.
- Paper 2 selector reproof: **FORBIDDEN / NOT AUTHORIZED**.
