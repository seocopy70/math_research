# Research Map — Rank-4 pro-3 Demuškin Group / Intrinsic Orientation Recovery

> **Purpose of this file:** This is the state/map document for the whole research. It is intentionally concise and different from the chronological research log. A new chat/session should read this file first to recover the global goal, frozen results, current gate, and next experiment without reconstructing the history from scratch.

## 0. One-sentence research question

\[
\boxed{\text{Can the canonical orientation character }\chi:G\to\mathbb Z_3^\times\text{ be recovered intrinsically from filtered/graded data?}}
\]

The present strategy is not to read the orientation directly from a single degree-4 object, but to determine whether intrinsic filtration information survives in a symmetry-compatible structure strongly enough to distinguish the relevant cases and eventually recover \(\chi\).

---

## 1. Mathematical setting

Group:
\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle.
\]

Quadratic initial relation:
\[
R=[X_1,X_2]+[X_3,X_4].
\]

Degree-4 probe:
\[
T=[[[X_3,X_4],X_1],X_1].
\]

The symplectic symmetry group used in the mod-3 degree-4 analysis is
\[
H=Sp_4(\mathbb F_3).
\]

---

## 2. Global research chain

\[
\boxed{\chi\text{ recovery}}
\rightarrow
\boxed{\text{intrinsic filtration information}}
\rightarrow
\boxed{q=3\text{ vs }q=\infty\text{ distinguishability}}
\rightarrow
\boxed{\text{degree-4/degree-5 bracket-filtration interaction}}.
\]

Operationally:

```text
Demuškin group
  ↓
Zassenhaus filtration / graded Lie structure
  ↓
quadratic relation R
  ↓
degree-4 probe T
  ↓
H-orbit module W (dim 45)
  ↓
internal H-module structure + filtration intersection
  ↓
I = W ∩ W_d = ker(N), dim 35
  ↓
canonical intertwiner τ
  ↓
bracket compatibility test
  ↓
obstruction rank 10
  ↓
CURRENT: interpret the rank-10 obstruction
  ↓
ask whether it gives intrinsic information distinguishing q=3 from q=∞
  ↓
connect any successful invariant back to χ
```

---

## 3. Frozen results — do not recompute without a contradiction

### Phase 1 — single probe

- The single degree-4 probe \(T\) is **not canonical** under the relevant symplectic action.
- Single-probe strategy: **REJECTED / FROZEN**.

### Phase 2 — orbit module

- \(W=\langle H\cdot T\rangle\) has dimension **45**.
- Earlier filtration/module structure:
  \[
  0\subset U_{10}\subset K_{35}\subset W_{45}.
  \]
- \(U\cong\operatorname{Sym}^2(V)\), and \(K/U\) has dimension 25.
- \(W\cong\Lambda^2(\operatorname{Sym}^2(V))\).
- \(E=W/U\) is the non-split extension
  \[
  0\to M_{25}\to E_{35}\to\operatorname{Sym}^2(V)_{10}\to0.
  \]
- Candidate \(E\cong\operatorname{Sym}^4(V)\): **REJECTED**.
- Track B A2:
  \[
  HP_4((uv)^{-3})=-T=2T\neq0.
  \]

### Phase 2-3 — endomorphism algebra

Authoritative historical script:
`research/phase2_3_endH_optimized_2026-09-15.py`

Frozen result:
\[
\dim\operatorname{End}_H(W)=2.
\]
There is a non-scalar nilpotent \(N\) with
\[
N^2=0,\qquad \operatorname{rank}N=10,\qquad \dim\ker N=35.
\]
Hence
\[
\operatorname{End}_H(W)\cong\mathbb F_3[\varepsilon]/(\varepsilon^2).
\]
This says the 45-dimensional module has nontrivial internal nilpotent structure; it is not a direct sum of irreducibles in the naive way.

### A3-4 — filtration intersection

\[
I=W\cap W_d,\qquad \dim I=35.
\]
Independent A3-4-8 verification established
\[
\boxed{I=\ker N}.
\]
This is frozen.

### A3-4 — intertwiner

A rank-45 intertwiner \(\tau\) was constructed between the relevant symmetry actions, with
\[
\tau(I)=I_d.
\]
The target bracket compatibility test is
\[
\boxed{\tau([v,X_h])=[\tau(v),X_h]}
\]
for the four fixed generators \(h\).

---

## 4. A3-4 audit/repair status — COMPLETE

A provenance audit compared the historical Phase 2-1 representation with the current A3-4 representation.

Audit branch:
`audit/a3-4-action-provenance`

Audit run:
`35242896521`

The audit established exact equality of:

- selected \(W\) basis in ambient degree-4 coordinates;
- all five generator action matrices \(A_1,\ldots,A_5\);
- \(B=A_2+A_3+A_4+A_5\);
- Krylov rank.

Reported values:
\[
\operatorname{rank}(B_{hist})=\operatorname{rank}(B_{curr})=44,
\]
\[
\operatorname{KrylovRank}_{hist}=\operatorname{KrylovRank}_{curr}=45.
\]

The earlier apparent Krylov rank 2 was traced to an implementation error in the old A3-4 `action_matrix()` extraction. It treated \(W\) as if it were an invariant ambient complement. The correct quotient action must work in
\[
(R_4\mid W),
\]
not in \(W\) alone, because ambient representatives can acquire an \((R)_4\) component.

Corrected commit:
`62886877f97e58e87d59b0075d45e38be6176410`

Corrected run:
`35245280405`

The repaired computation reproduced the frozen structural results:

- \(\dim W=45\)
- \(\dim W_d=45\)
- \(\dim I=35\)
- \(\dim\operatorname{End}_H(W)=2\)
- \(N^2=0\)
- \(\operatorname{rank}N=10\)
- \(\dim\ker N=35\)
- \(\ker N=I\)

Downstream independent bracket review also matched the primary result.

**Therefore the A3-4 computational/provenance audit is CLOSED.** Do not reopen it unless a new genuine mathematical contradiction appears.

---

## 5. Current mathematical gate — OPEN

### Verified input

The bracket-compatibility computation gives, for each of the four generators,

\[
\operatorname{DIRECT\_DISCREPANCY\_RANK}=10,
\]

and the stacked obstruction has rank

\[
\boxed{\operatorname{obstruction\ rank}=10}.
\]

The independent review reproduced the same result.

### Correct interpretation of the status

The computation is **verified**, but its mathematical meaning is **OPEN**.

The statement currently established is:

> The transported degree-4 structure fails the tested bracket-compatibility condition, and the resulting obstruction space has rank 10.

It is **not yet established** that this rank-10 obstruction distinguishes \(q=3\) from \(q=\infty\), nor that it directly determines the orientation character.

### Current research question

\[
\boxed{\text{What is the mathematical structure of this 10-dimensional obstruction?}}
\]

The first task is to identify its position relative to the already known 10-dimensional object
\[
U\cong\operatorname{Sym}^2(V),
\]
and relative to \(N\), \(I=\ker N\), and the filtration-derived subspaces.

Only after that should we test whether the obstruction is an intrinsic filtration invariant and whether it differs between \(q=3\) and \(q=\infty\).

---

## 6. Next research stage — obstruction analysis

### Goal

Determine whether the rank-10 obstruction is merely a defect of the chosen transport \(\tau\), or whether it carries a canonical/intrinsic piece of filtration information.

### Required order

1. **Consume the corrected A3-4 artifacts.** Prefer the verified objects from commit `62886877f97e58e87d59b0075d45e38be6176410` over rebuilding frozen objects.
2. Identify exactly which 10-dimensional subspace is the obstruction (image/kernel/cokernel, depending on the stored certificate).
3. Compare it with the known 10-dimensional \(U\cong\operatorname{Sym}^2(V)\).
4. Test its relationship with \(\ker N=I\), the quotient \(W/I\), and the relevant filtration-derived spaces.
5. Determine whether the obstruction is stable under the relevant symmetry and independent of arbitrary basis/transport choices.
6. Only then design the first explicit \(q=3\) versus \(q=\infty\) comparison.

### What would count as meaningful progress

A successful result would be something like:

\[
\boxed{\text{obstruction space = a canonical module/subquotient already determined by filtered data}}
\]

or a precise structural relation that forces a difference between the two \(q\)-cases.

A failure to find such structure is not a proof that no intrinsic invariant exists; it only rejects that particular obstruction route.

---

## 7. What is NOT the current task

- Do **not** redo the A3-4 provenance audit.
- Do **not** rebuild the historical Phase 2 representation merely to reconfirm it.
- Do **not** treat the rank-10 obstruction as already proving \(q=3\) versus \(q=\infty\).
- Do **not** claim orientation recovery yet.
- Do **not** change frozen mathematical objects unless a new contradiction is demonstrated.

---

## 8. New-chat / new-window protocol

When opening a new chat, the first message can simply be:

> **수학증명 프로젝트 이어가기. 먼저 `RESEARCH_MAP.md`를 기준으로 현재 상태를 복원해줘. A3-4 audit는 완료·동결되어 있고, 현재 본 연구 단계는 obstruction rank 10의 구조 분석이다. 새 계산 전에 global position / purpose / dependency / pass-fail consequence를 먼저 정리하고, 기존 artifact를 우선 사용해 설계하자.**

Then provide the relevant GitHub Actions run or artifact only if a concrete calculation needs to be inspected.

### Session safety rules

- **Map first:** recover global state from this file before relying on conversational memory.
- **Frozen means frozen:** do not recompute a frozen result just because a new chat cannot see the old calculation.
- **Artifact first:** downstream experiments should consume verified artifacts whenever possible.
- **Contradiction first:** only reopen provenance/audit if a genuinely incompatible result appears.
- **Experiment gate:** before code/execution, state purpose, dependency, expected interpretation, and pass/fail consequence.
- **Separate history from state:** `research/00_RESEARCH_LOG.md` preserves chronology; this file preserves the current map.

---

## 9. Research-record architecture

### History / process
`research/00_RESEARCH_LOG.md`

Preserves detailed chronology, including failed experiments, implementation mistakes, corrections, and provenance investigations.

### State / map
`RESEARCH_MAP.md` (this file)

Preserves only the current research state, frozen results, open questions, and next path.

The two documents serve different purposes and should not be merged into one giant record.

---

## 10. Status legend

- 🟢 **FROZEN / VERIFIED** — may be used downstream without routine recomputation.
- 🟡 **OPEN** — mathematically meaningful but not settled.
- 🔴 **REJECTED** — strategy/result ruled out for the stated purpose.
- ⚪ **BACKGROUND** — context, not a current research gate.

### Current state at last update

| Item | Status |
|---|---|
| Single probe \(T\) canonicality | 🔴 Rejected |
| \(W\) orbit module, dim 45 | 🟢 Frozen |
| \(\dim End_H(W)=2\) | 🟢 Frozen |
| \(N^2=0\), rank \(N=10\) | 🟢 Frozen |
| \(I=W\cap W_d\), dim 35 | 🟢 Frozen |
| \(I=\ker N\) | 🟢 Frozen |
| rank-45 intertwiner \(\tau\) | 🟢 Verified |
| A3-4 provenance audit | 🟢 Closed |
| bracket discrepancy rank 10 | 🟢 Computed + independently verified |
| meaning of rank-10 obstruction | 🟡 Open |
| q=3 vs q=∞ distinction via obstruction | 🟡 Open |
| intrinsic recovery of \(\chi\) | 🟡 Open |

---

## 11. Immediate next checkpoint

**Do not start by asking whether rank 10 is "good" or "bad".**

Start by asking:

\[
\boxed{\text{What exactly is the 10-dimensional obstruction as a mathematical subspace/module?}}
\]

Then ask:

\[
\boxed{\text{Is that object canonical under the relevant symmetry and filtration data?}}
\]

Then, and only then:

\[
\boxed{\text{Does it distinguish }q=3\text{ from }q=\infty\text{?}}
\]

Finally:

\[
\boxed{\text{Can that distinction contribute to intrinsic recovery of }\chi\text{?}}
\]
