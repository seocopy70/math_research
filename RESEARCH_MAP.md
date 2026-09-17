# Research Map — Rank-4 pro-3 Demuškin Group / Intrinsic Orientation Recovery

> **Purpose:** Current state/map document for the whole research. Read this first in a new session. Chronology belongs in `research/00_RESEARCH_LOG.md`.

## 0. One-sentence research question

\[
\boxed{\text{Can the canonical orientation character }\chi:G\to\mathbb Z_3^\times\text{ be recovered intrinsically from filtered/graded data?}}
\]

The strategy is to determine whether intrinsic filtration information survives in a symmetry-compatible structure strongly enough to distinguish the relevant cases and eventually recover \(\chi\).

---

## 1. Mathematical setting

\[
G=\langle x_1,x_2,x_3,x_4\mid x_1^3[x_1,x_2][x_3,x_4]=1\rangle,
\qquad
R=[X_1,X_2]+[X_3,X_4].
\]

Degree-4 probe:
\[
T=[[[X_3,X_4],X_1],X_1].
\]

Symmetry group:
\[
H=Sp_4(\mathbb F_3).
\]

---

## 2. Global research chain

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
O2: identify the mathematical structure of the rank-10 obstruction
  ↓
O2-3: compare obstruction module O with U = im(N)
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
- \(0\subset U_{10}\subset K_{35}\subset W_{45}\).
- \(U\cong\operatorname{Sym}^2(V)\), and \(K/U\) has dimension 25.
- \(W\cong\Lambda^2(\operatorname{Sym}^2(V))\).
- \(E=W/U\) is the non-split extension
  \[
  0\to M_{25}\to E_{35}\to\operatorname{Sym}^2(V)_{10}\to0.
  \]
- Candidate \(E\cong\operatorname{Sym}^4(V)\): **REJECTED**.
- Track B A2: \(HP_4((uv)^{-3})=-T=2T\ne0\).

### Phase 2-3 — endomorphism algebra

Authoritative script: `research/phase2_3_endH_optimized_2026-09-15.py`.

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

Thus
\[
0\subset U=\operatorname{im}N\subset K=\ker N\subset W,
\qquad \dim U=10,\dim K=35,\dim W=45.
\]

### A3-4 — filtration intersection

\[
I=W\cap W_d,\qquad \dim I=35,
\]
and independent A3-4-8 verification established
\[
\boxed{I=\ker N}.
\]
This is frozen.

### A3-4 — provenance/repair audit

Audit branch: `audit/a3-4-action-provenance`  
Audit run: `35242896521`  
Corrected commit: `62886877f97e58e87d59b0075d45e38be6176410`  
Corrected run: `35245280405`

The audit established exact equality of the selected \(W\) basis in ambient degree-4 coordinates, all five generator action matrices, \(B=A_2+A_3+A_4+A_5\), and Krylov rank. The earlier Krylov-rank-2 result came from an incorrect old `action_matrix()` extraction that treated \(W\) as an invariant ambient complement; the correct quotient action works in \((R)_4\mid W\).

The repaired computation reproduced:
- \(\dim W=45\)
- \(\dim W_d=45\)
- \(\dim I=35\)
- \(\dim\operatorname{End}_H(W)=2\)
- \(N^2=0\)
- \(\operatorname{rank}N=10\)
- \(\dim\ker N=35\)
- \(\ker N=I\)

**A3-4 computational/provenance audit is CLOSED.** Do not reopen without a genuine contradiction.

---

## 4. O2-2 — transported obstruction action: COMPLETE / VERIFIED

Verification record: `research/O2-2_RESULT_2026-09-18.md`  
GitHub Actions run: `35278644641`  
Job: `105395199074`  
Working verification commit: `5a447946e9bb7087078e22eccc9bd304a7170494`

### O2-2R/S/T

- **O2-2R — generator-level obstruction equivariance: PASS.**
- **O2-2S — group consistency of \(T_g\): PASS.**
- **O2-2T — exact identification: PASS.**

For all five generators, the independently solved 16-parameter action satisfies exactly
\[
\boxed{T_g=g^{-T}}\qquad(\text{over }\mathbb F_3).
\]
Generator-pair multiplicativity also passes.

Therefore
\[
D_{\rm stack}A_W(g)
=(T_g\otimes A_5(g))D_{\rm stack}
=(g^{-T}\otimes A_5(g))D_{\rm stack}
\]
for the generators and hence all \(g\in H\). Consequently
\[
\boxed{O=\operatorname{Im}D_{\rm stack}\text{ is an }H\text{-submodule}.}
\]

### Final pre-O2-3 identity check — PASS

The \(A_W(g)\) used in O2-2 is the same mathematical \(W\)-action used to define \(N\):

- `phase2_3_endH_optimized_2026-09-15.py` loads `action_matrices` from `phase2_1_invariant_space_verification_2026-09-15.py`.
- Phase 2-1 constructs these matrices from `apply_linear_map(a, g)` with the column convention
  \[
  e_j\mapsto\sum_i g_{ij}e_i.
  \]
- The corrected A3-4/O2 pipeline uses the same `apply_linear_map` definition and the same five `gens` construction.
- O2-2 constructs `A_W` from those corrected ambient actions.

Thus there is **no coordinate/convention mismatch between the \(A_W\) defining \(N\) and the \(A_W\) in O2-2**.

### Legacy convention archaeology

Status: **⚪ NOT YET DETERMINED**.

A hard-coded matrix numerically equal to \(g^{-T}\) was found historically, but it was a separate sanity-check object, not evidence that a legacy tuple-action implementation used that convention. The historical provenance question remains open.

This does **not** block O2-3: O2-2 solved \(T_g\) directly from current data and verified exact \(g^{-T}\), independent of any assumed legacy convention.

---

## 5. Current mathematical gate — OPEN

The bracket-compatibility computation is verified:

\[
\operatorname{DIRECT\_DISCREPANCY\_RANK}=10
\]
for each of the four tested generators, and
\[
\boxed{\operatorname{rank}D_{\rm stack}=10}.
\]

This establishes a rank-10 obstruction, but **does not yet establish** that the obstruction distinguishes \(q=3\) from \(q=\infty\), or that it directly determines \(\chi\).

Current question:
\[
\boxed{\text{What is the mathematical structure of the 10-dimensional obstruction }O?}
\]

---

## 6. O2-3 — CURRENT FRONTIER

### Goal

Determine whether
\[
U=\operatorname{im}N\cong W/\ker N=W/I
\]
is naturally identified with
\[
O=\operatorname{im}D_{\rm stack}.
\]

### Required order

1. **Trace/character precheck.** Compare the generator traces/characters of the known 10-dimensional \(U\) and the obstruction image \(O\).
2. **Kernel check:** verify
   \[
   \boxed{\ker D_{\rm stack}=I=\ker N}.
   \]
3. **Dimension check:** verify
   \[
   \boxed{\dim O=10}.
   \]
4. If 2–3 pass, form the induced map
   \[
   \bar D_{\rm stack}:W/I\to O
   \]
   and verify it is an isomorphism.
5. Use \(W/I\cong U\) to obtain the induced 10-dimensional comparison.
6. Verify \(H\)-equivariance of the induced map.
7. Only if the structural comparison is not already decisive, solve an explicit **10×10 intertwiner**.

### Dependency

O2-3 consumes the corrected A3-4 artifacts from commit `62886877f97e58e87d59b0075d45e38be6176410` and the verified O2-2 obstruction relation. It does **not** depend on resolving the legacy tuple-action archaeology.

### Pass/fail consequence

- **PASS:** \(\ker D=I\), \(\dim O=10\), and the induced map \(W/I\to O\) is an \(H\)-equivariant isomorphism. Then the obstruction is identified with the already-known 10-dimensional module \(U\) up to the induced canonical map, and the next task is to determine whether this identification is filtration-intrinsic.
- **FAIL:** any kernel/dimension/equivariance mismatch. Then do not claim \(O\cong U\); inspect the exact source of the mismatch before proceeding.

---

## 7. What is NOT the current task

- Do **not** redo the A3-4 provenance audit.
- Do **not** rebuild the historical Phase 2 representation merely to reconfirm it.
- Do **not** treat rank 10 as already proving \(q=3\) versus \(q=\infty\).
- Do **not** claim orientation recovery yet.
- Do **not** change frozen mathematical objects unless a new contradiction is demonstrated.
- Do **not** block O2-3 on the unresolved historical tuple-action question.

---

## 8. New-chat / new-window protocol

When opening a new chat:

> **수학증명 프로젝트 이어가기. 먼저 `RESEARCH_MAP.md`를 기준으로 현재 상태를 복원해줘. A3-4 audit는 완료·동결되어 있고, O2-2는 PASS이며, 현재 본 연구 단계는 O2-3: \(U=\operatorname{im}N\)과 rank-10 obstruction \(O=\operatorname{im}D_{\rm stack}\)의 구조 비교다. 새 계산 전에 global position / purpose / dependency / pass-fail consequence를 먼저 정리하고, corrected artifact를 우선 사용하자.**

### Session safety rules

- **Map first:** recover global state from this file.
- **Frozen means frozen:** do not recompute frozen results without contradiction.
- **Artifact first:** downstream experiments consume verified artifacts.
- **Contradiction first:** reopen provenance only for a genuine incompatible result.
- **Experiment gate:** before execution, state purpose, dependency, expected interpretation, and pass/fail consequence.
- **Separate history from state:** chronology stays in `research/00_RESEARCH_LOG.md`.

---

## 9. Research-record architecture

### History / process
`research/00_RESEARCH_LOG.md`

Preserves chronology, failed experiments, implementation mistakes, corrections, and provenance investigations.

### State / map
`RESEARCH_MAP.md`

Preserves current research state, frozen results, open questions, and next path.

---

## 10. Status legend

- 🟢 **FROZEN / VERIFIED** — may be used downstream without routine recomputation.
- 🟡 **OPEN** — mathematically meaningful but not settled.
- 🔴 **REJECTED** — strategy/result ruled out for the stated purpose.
- ⚪ **BACKGROUND / NOT YET DETERMINED** — contextual or unresolved historical issue, not a current mathematical gate.

### Current state

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
| O2-2R/S/T | 🟢 PASS |
| \(T_g=g^{-T}\) | 🟢 Exact / verified |
| \(O=\operatorname{Im}D_{\rm stack}\) is an \(H\)-submodule | 🟢 Verified |
| \(A_W\) identity with action defining \(N\) | 🟢 Verified |
| legacy tuple-action convention archaeology | ⚪ Not yet determined |
| O2-3 \(\ker D=I\) | 🟡 Open |
| O2-3 \(\dim O=10\) | 🟡 Open |
| O2-3 induced \(W/I\to O\) isomorphism | 🟡 Open |
| q=3 vs q=∞ distinction via obstruction | 🟡 Open |
| intrinsic recovery of \(\chi\) | 🟡 Open |

---

## 11. Immediate next checkpoint

Do not ask whether rank 10 is "good" or "bad". Ask first:

\[
\boxed{\ker D_{\rm stack}\stackrel{?}{=}I=\ker N}
\]

and

\[
\boxed{\dim\operatorname{Im}D_{\rm stack}\stackrel{?}{=}10.}
\]

If both pass, the decisive next object is
\[
\boxed{\bar D_{\rm stack}:W/I\longrightarrow O}
\]
and the question is whether it identifies \(O\) with the known module
\[
\boxed{U=\operatorname{im}N\cong W/I.}
\]
