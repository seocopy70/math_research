# Research Map — Rank-4 pro-3 Demuškin Group / Intrinsic Orientation Recovery

> **Purpose:** Current state/map document. Read this first in a new session. Chronology belongs in `research/00_RESEARCH_LOG.md`.

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
R=[X_1,X_2]+[X_3,X_4],
\]

with degree-4 probe
\[
T=[[[X_3,X_4],X_1],X_1],
\]
and \(H=Sp_4(\mathbb F_3)\).

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
rank-10 stacked obstruction O
  ↓
O2-3: O ≅ W/I ≅ U = im(N)
  ↓
CURRENT: determine whether this 10-dim module is filtration-intrinsic
  ↓
then test q=3 vs q=∞
  ↓
connect any successful invariant back to χ
```

---

## 3. Frozen structural results

### Phase 1 — single probe

- Single degree-4 probe \(T\) is not canonical under the relevant symplectic action.
- Single-probe strategy: **REJECTED / FROZEN**.

### Phase 2 — orbit/module structure

\[
\dim W=45,
\qquad
0\subset U_{10}\subset K_{35}\subset W_{45}.
\]

\[
U\cong\operatorname{Sym}^2(V),
\qquad
\dim(K/U)=25,
\qquad
W\cong\Lambda^2(\operatorname{Sym}^2(V)).
\]

\[
0\to M_{25}\to E_{35}=W/U\to\operatorname{Sym}^2(V)_{10}\to0
\]
is the non-split extension; the candidate \(E\cong\operatorname{Sym}^4(V)\) was rejected.

Track B A2:
\[
HP_4((uv)^{-3})=-T=2T\ne0.
\]

### Phase 2-3 — endomorphism algebra

Authoritative script: `research/phase2_3_endH_optimized_2026-09-15.py`.

\[
\dim\operatorname{End}_H(W)=2,
\quad
N^2=0,
\quad
\operatorname{rank}N=10,
\quad
\dim\ker N=35.
\]

Hence
\[
\operatorname{End}_H(W)\cong\mathbb F_3[\varepsilon]/(\varepsilon^2).
\]

### A3-4 — filtration intersection

\[
I=W\cap W_d,
\qquad
\dim I=35,
\qquad
\boxed{I=\ker N}.
\]
This is frozen.

### A3-4 provenance/repair audit

Audit run `35242896521`; corrected commit `62886877f97e58e87d59b0075d45e38be6176410`; corrected run `35245280405`.

The audit established exact equality of the selected \(W\) basis, all five generator action matrices, \(B=A_2+A_3+A_4+A_5\), and Krylov rank. The earlier apparent Krylov-rank-2 result came from an incorrect old quotient-action extraction. The repaired computation reproduced all frozen structural results.

**A3-4 computational/provenance audit is CLOSED.**

---

## 4. O2-2 — transported obstruction action: COMPLETE / VERIFIED

Record: `research/O2-2_RESULT_2026-09-18.md`  
Run `35278644641`, job `105395199074`.

- O2-2R: **PASS**
- O2-2S: **PASS**
- O2-2T: **PASS**

For all five generators, the independently solved 16-parameter action satisfies exactly
\[
\boxed{T_g=g^{-T}}
\]
over \(\mathbb F_3\), with generator-pair multiplicativity also verified.

Therefore
\[
D_{\rm stack}A_W(g)
=(g^{-T}\otimes A_5(g))D_{\rm stack},
\]
so
\[
\boxed{O=\operatorname{im}D_{\rm stack}\text{ is an }H\text{-submodule}.}
\]

### Final pre-O2-3 action identity check

**PASS:** the \(A_W(g)\) used in O2-2 is the same mathematical action used to define \(N\). The authoritative Phase 2-3 script loads `action_matrices` from Phase 2-1; Phase 2-1 and the corrected A3-4 pipeline use the same `apply_linear_map` and the same five `gens` construction, with column convention
\[
e_j\mapsto\sum_i g_{ij}e_i.
\]
Thus there is no coordinate/convention mismatch between the representation defining \(N\) and the \(A_W\) used in O2-2.

### Legacy convention archaeology

**⚪ NOT YET DETERMINED.** A historical hard-coded matrix numerically equal to \(g^{-T}\) was found, but it was a separate sanity-check object, not evidence that a legacy tuple-action implementation used that convention. This does not block the mathematical pipeline.

---

## 5. O2-3 — rank-10 obstruction identified: PASS / COMPLETE

Record: `research/O2-3_RESULT_2026-09-18.md`  
Run `35279936962`, job `105399291836`  
Final code commit: `3cf1608e26f0ef15ee6610ab8ae25a7f9237b951`

### Verified facts

\[
D_{\rm stack}\in\operatorname{Hom}(W,\mathbb F_3^{4096}),
\qquad
\operatorname{rank}D_{\rm stack}=10,
\qquad
\dim\ker D_{\rm stack}=35.
\]

Directly verified:
\[
D_{\rm stack}|_I=0,
\qquad
\boxed{\ker D_{\rm stack}=I=\ker N}.
\]

Therefore
\[
\bar D_{\rm stack}:W/I\xrightarrow{\sim}O
\]
is an isomorphism.

The nilpotent map gives
\[
N:W/I\xrightarrow{\sim}U=\operatorname{im}N.
\]
Combining them yields
\[
\boxed{U\xrightarrow{\sim}O}
\]
with rank 10.

The generator traces are identical:
\[
\operatorname{tr}(U)=[1,1,1,1,1],
\qquad
\operatorname{tr}(O)=[1,1,1,1,1],
\]
and the induced \(U\to O\) map was directly verified to be \(H\)-equivariant for all five generators. No independent 10x10 solve was needed.

### Mathematical interpretation

The rank-10 obstruction is **not merely a dimension coincidence** within the verified pipeline:
\[
\boxed{O\cong W/I\cong U=\operatorname{im}N}
\]
as an \(H\)-module via the induced map coming from \(D_{\rm stack}\) and \(N\).

This does **not yet** prove that the module is filtration-intrinsic, does not distinguish \(q=3\) from \(q=\infty\), and does not recover \(\chi\).

### Important distinction

The older A3-4-11 `OBSTRUCTION_MODULE` calculation concerns a different obstruction in `Hom(V,L_5/(R)_5)` and has a 45-dimensional image. It must not be conflated with the present O2-2/O2-3 stacked obstruction, whose image is the 10-dimensional \(O\).

---

## 6. CURRENT MATHEMATICAL GATE — OPEN

The next question is no longer whether the rank-10 obstruction is a 10-dimensional \(H\)-module. That has been settled.

The current question is:

\[
\boxed{\text{Is }U\cong O\text{ canonically determined by the filtration data, independently of the chosen transport }\tau?}
\]

Only after this is addressed should the project design the explicit \(q=3\) versus \(q=\infty\) comparison.

### Dependency

The next stage consumes the corrected A3-4 artifacts from commit `62886877f97e58e87d59b0075d45e38be6176410` and the verified O2-2/O2-3 records. It does not depend on resolving legacy tuple-action archaeology.

### Pass/fail consequence

- **PASS:** show that the identified 10-dimensional module/map is forced by filtered data or by a canonical construction, not by the arbitrary choice of \(\tau\).
- **FAIL:** if the identification changes under admissible choices of transport or basis, then the current obstruction route does not yet provide an intrinsic invariant; do not infer a \(q\)-distinction.

---


---

## 6A. O2-4 — absolute transport-independence: FAIL / COMPLETE

Record: `research/O2-4_RESULT_2026-09-18.md`  
Run `35281594800`.

For the exact B1-admissible normalized family
[
	au_b=	au(I+bN),qquad b=0,1,2,
]
each obstruction image has rank 10, but the three images are distinct. Their pairwise join ranks are 20:
[
operatorname{rank}(O_b+O_c)=20quad(b
e c).
]
Hence
[
oxed{O_0,O_1,O_2	ext{ are not equal}.}
]

**Interpretation:** the absolute obstruction image (O_	au=operatorname{Im}D_	au) is transport-dependent. This is a localized failure of canonicality, not a failure of the fixed-(	au) O2-3 module calculation.

The earlier scalar rescaling idea (a	au) is **not an admissible transport freedom** under the B1 pointwise condition (	au|_I=I_{W_d}); it must not be used as an O2-4/O2-5 test.

---

## 6B. O2-5 — affine transport variation: PASS / COMPLETE

Record: `research/O2-5_RESULT_2026-09-18.md`  
Run `35283099072`, job `105409292646`  
Final code commit: `5ab1e41befeb2c425ec0ad478de9665e78e3af9f`.

The corrected implementation first resolved a coordinate-system issue: the 256-dimensional vectors are degree-4 ambient coordinates, not 45-dimensional (W)-coordinates. The final B1 audit compares both sides in the same 256-dimensional ambient coordinate system via
[
I_{W,mathrm{coeff}}=Q_{W45}^{-1}I_{mathrm{coord}},
qquad
T_b^{mathrm{amb}}=W_d	au_bQ_{W45}^{-1}.
]

All final workflow assertions passed.

### Verified checkpoints

- B1 admissibility of the exact (b=0,1,2) family: **PASS**.
- Affine obstruction identity
[
D_b=D_0+bDelta D,qquad Delta D=D_1-D_0
]
: **PASS**.
- Variation rank:
[
oxed{operatorname{rank}Delta D=10}
]
: **PASS**.
- H-stability of
[
Delta O=operatorname{Im}Delta D
]
under the same transported target action used in O2-2: **PASS**.

Therefore
[
oxed{dimDelta O=10,qquad Delta O	ext{ is an }H	ext{-submodule}.}
]

### O2-6 — basepoint-independence: PASS / COMPLETE

Record: research/O2-6_RESULT_2026-09-18.md  
Run 35284130822, job 105412565419.

The complete frozen B1 family was tested by comparing the actual finite-difference maps:
\\[
D_1-D_0,\\qquad D_2-D_1,\\qquad D_0-D_2.
\\]
All three maps have rank 10 and are exactly equal. Hence the affine variation direction, and therefore \\(\\Delta O=\\operatorname{Im}\\Delta D\\), is independent of the basepoint within the complete verified B1 admissible family.

This closes the basepoint-dependence loophole left by O2-5. It still does not provide a transport-free formula solely in filtered/graded terms, nor does it establish \\(\\Delta O\\cong U\\) canonically, q=3 versus q=infinity, or recovery of \\(\\chi\\).

### Critical logical boundary

O2-5 does **not** prove that (Delta O) is canonical under a change of base transport, nor that it is determined by filtration data alone. It establishes a 10-dimensional H-stable **transport-variation module** within the fixed B1 affine family.

It also does not prove a canonical isomorphism (Delta Ocong U), distinguish (q=3) from (q=infty), or recover (chi).

The next gate is therefore:
[
oxed{	ext{Is the variation module }Delta O	ext{ itself independent of the remaining admissible choices?}}
]

Only after this gate should the project move to the explicit (q=3) versus (q=infty) comparison.


## 6C. O2-7 — q-control of transport variation: INFORMATIVE FAIL / COMPLETE

Record: `research/O2-7_RESULT_2026-09-18.md`  
Run: `35284838948`, final code commit `988f61c04f3c659db2b4bff285f8f0809d4e7f4f`.

The first proposed identification
[
langle Hcdot [X_1^{[3]},X_2]angle = U
]
is false.

Verified:
- (dimlangle Hcdot dangle=45), so the q=3 p-power class (d=[X_1^{[3]},X_2]) generates all of (W).
- (dim N(d)=1).
- (dimlangle Hcdot N(d)angle=9).
- (dim U=10), with (langle Hcdot N(d)anglesubset U).
- (operatorname{im}(	au N)=	au(U)) at the tested subspace level.
- The q=(infty) p-power control has (d_infty=0).

Thus O2-7 is an **informative FAIL of the naive identification**, not a failure of the O2-3/O2-6 results. The q-sensitive class has a nontrivial 9-dimensional shadow inside (U), but (U) contains one additional dimension.

### Next gate

Characterize the exact extension
[
0	o langle Hcdot N(d)angle	o U	o U/langle Hcdot N(d)angle	o0
]
and determine whether the remaining 1-dimensional quotient/direction is related to (Delta D) or carries the q=3-specific information.

The q=(infty) control used in O2-7 is local: it suppresses the p-power contribution and does not yet constitute a full recomputation of the q=(infty) filtered structure.


## 7. What is NOT the current task

- Do **not** redo the A3-4 provenance audit.
- Do **not** rebuild the historical Phase 2 representation without contradiction.
- Do **not** treat \(O\cong U\) as already proving \(q=3\) versus \(q=\infty\).
- Do **not** claim orientation recovery yet.
- Do **not** block progress on unresolved historical tuple-action archaeology.

---

## 8. New-chat / new-window protocol

> **수학증명 프로젝트 이어가기. 먼저 `RESEARCH_MAP.md`를 기준으로 현재 상태를 복원해줘. A3-4 audit는 완료·동결, O2-2는 PASS, O2-3도 PASS이며 현재 본 연구 단계는 `U = im(N) ≅ O = im(D_stack)`라는 식별이 transport-독립적이고 filtration-intrinsic인지 확인하는 것이다. 새 계산 전에 global position / purpose / dependency / pass-fail consequence를 먼저 정리하고 corrected artifact를 우선 사용하자.**

### Session safety rules

- **Map first.**
- **Frozen means frozen.**
- **Artifact first.**
- **Contradiction first.**
- **Experiment gate:** before execution state purpose, dependency, expected interpretation, and pass/fail consequence.
- **History/state separation:** chronology in `research/00_RESEARCH_LOG.md`; current state here.

---

## 9. Research-record architecture

- History/process: `research/00_RESEARCH_LOG.md`
- State/map: `RESEARCH_MAP.md`
- O2-2 record: `research/O2-2_RESULT_2026-09-18.md`
- O2-3 record: `research/O2-3_RESULT_2026-09-18.md`

---

## 10. Status legend

- 🟢 **FROZEN / VERIFIED** — safe downstream input.
- 🟡 **OPEN** — mathematically meaningful but unsettled.
- 🔴 **REJECTED** — ruled out for the stated purpose.
- ⚪ **BACKGROUND / NOT YET DETERMINED** — unresolved historical/contextual issue, not a current mathematical gate.

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
| bracket discrepancy rank 10 | 🟢 Verified |
| O2-2R/S/T | 🟢 PASS |
| \(T_g=g^{-T}\) | 🟢 Exact / verified |
| \(O=\operatorname{im}D_{\rm stack}\) is an \(H\)-submodule | 🟢 Verified |
| \(A_W\) identity with action defining \(N\) | 🟢 Verified |
| \(\ker D_{\rm stack}=I\) | 🟢 PASS |
| \(\dim O=10\) | 🟢 PASS |
| \(U\cong O\) as \(H\)-modules | 🟢 PASS |
| absolute transport-independence of O_tau | 🔴 Failed in O2-4 |\n| variation-module basepoint independence within B1 family | 🟢 O2-6 PASS |\n| O2-7 raw p-power orbit = U | 🔴 False (orbit dimension 45) |
| O2-7 H.N(d) inside U, dim 9 | 🟢 Verified |
| full filtration-intrinsic characterization of Delta O | 🟡 Open |
| legacy tuple-action archaeology | ⚪ Not yet determined |
| q=3 vs q=∞ distinction | 🟡 Open |
| intrinsic recovery of \(\chi\) | 🟡 Open |

---

## 11. Immediate next checkpoint

Do not ask whether O2-3 is "good" or "bad". It has passed.

Ask instead:

\[
\boxed{\text{What makes the 10-dimensional module }U\cong O\text{ canonical?}}
\]

The critical issue is **transport dependence**: the current \(O\) was produced from the specific canonical intertwiner \(\tau\) already fixed by the A3-4 construction. We must determine whether the resulting 10-dimensional module/map is forced by the filtered structure, or merely an artifact of that transport choice.

Only after this gate:
\[
\boxed{q=3\;\text{vs}\;q=\infty}
\]
and eventually
\[
\boxed{\chi\text{ recovery}}.
\]
