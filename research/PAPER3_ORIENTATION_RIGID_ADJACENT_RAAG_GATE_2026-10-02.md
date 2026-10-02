# PAPER 3 — ORIENTATION-RIGID ADJACENT CLASS GATE: SPECIAL ORIENTED PRO-p RAAGs — 2026-10-02

## 0. Decision

The first serious adjacent-class candidate is the class of **special oriented right-angled Artin pro-p groups (oriented pro-p RAAGs)**.

This class passes the first structural screen better than free pro-p or locally-uniform/θ-abelian groups:

- it has a canonical orientation, and for a special digraph that orientation is the unique orientation satisfying the Kummerian lifting condition;
- the underlying class is substantially richer than the one-parameter Demuškin q-family because the defining finite digraph contributes independent combinatorial structure;
- the orientation is supported on sinkholes and takes value (1+q) there, (1) elsewhere;
- the finite-window problem therefore separates into a low-degree graph part and a higher-degree orientation/q part.

However, **finite-window identifiability is not yet closed**. The candidate is therefore **OPEN / LOAD-BEARING**, not PASS.

## 1. Literature-level admissibility

For a digraph Γ and p-power (q=p^f), the associated oriented pro-p RAAG has relations
[
[w,u]=u^q
]
on special directed edges and
[
[w,u]=1
]
on ordinary edges. For a special digraph, the canonical orientation is
[
	heta_Gamma(v)=
egin{cases}
1+q,&v	ext{ a sinkhole},\
1,&	ext{otherwise}.
end{cases}
]

The literature states that there exists an orientation making the natural Kummerian maps surjective at every level iff Γ is special, and in that case the orientation is unique and equals (	heta_Gamma). It also characterizes elementary-type special digraphs via 1-cyclotomicity / Frattini-resistance / Galois realizability. citeturn3search0turn5search0

Thus the target is not merely a presentation decoration: at the special-digraph scope it is canonically selected by an intrinsic group-theoretic/cohomological property.

## 2. Why this is genuinely adjacent rather than another Demuškin re-encoding

A Demuškin group is essentially controlled, in the relevant odd-p normal form, by rank and q. Hence q-compression inside that family was classified as re-encoding.

An oriented pro-p RAAG has additional independent finite combinatorial data Γ. In particular, the minimal generating set is indexed by vertices, while the degree-two relation structure records the underlying graph; the directed/special part contributes the (q)-power deformation. The literature gives (H^1(G,mathbf F_p)) from the vertex set and identifies the degree-two cohomological relation structure with graph data in the RAAG setting. citeturn5search1turn4search2

Therefore the target is schematically
[
(Gamma,q)longmapsto[	heta_Gammamod p^k],
]
not merely
[
qlongmapsto[chi_qmod p^k].
]

This is the first candidate where "orientation rigidity + non-q classification" is materially present.

## 3. Object / Input / Functoriality / Gauge / Orientation bridge / q-blindness / Separation / Novelty / Stop

### Object

A special oriented pro-p RAAG (G_{Gamma,q}), considered up to abstract pro-p group isomorphism.

### Input

[
W_k(G)=G/G_{(N_k+1)},qquad N_k=p^{k-1}+1.
]

### Functoriality

The canonical orientation is unique at the special-digraph level. Hence an abstract isomorphism between admissible groups transports the canonical orientation to the canonical orientation. This supplies the required target functoriality, subject to the scope of the uniqueness theorem. citeturn3search0

### Gauge

Do not use a chosen vertex labeling as the target. The target is the isomorphism class
[
[	heta_Gammamod p^k].
]

### Orientation bridge

The canonical orientation is characterized by the Kummerian lifting property, and for special digraphs is explicitly given by the sinkhole formula above. citeturn3search0

### q-blindness

The carrier/input construction must not insert (q), (	heta_Gamma), or sinkhole labels by definition. The finite-window object itself must reveal the relevant defect.

### Separation

This is the first genuine OPEN gate.

There are two layers:

1. **Graph layer:** degree-two data should recover the underlying undirected adjacency information.
2. **Orientation layer:** special directed edges are invisible at their initial degree-two commutator term, but the (u^q) correction appears at degree (q).

Hence the critical question is whether the first nontrivial q-dependent relation defect canonically identifies the sinkhole support and (qmod p^k), without choosing a presentation.

### Novelty

If successful, this is not merely a restatement of Demuškin q-recovery: the finite window would recover a canonical orientation on a class with independent graph/extension data. This is potentially a genuine extension theorem.

### Stop

If the separation argument reduces entirely to choosing the original digraph presentation and reading off its relators, classify as **FAIL/CLOSED — presentation-level re-encoding**. A successful theorem must identify the orientation support and q from intrinsic finite-window data.

## 4. Finite-window mechanism: the promising threshold

For a special directed relation,
[
[w,u]=u^q,
]
the commutator term has Zassenhaus degree 2, while (u^q) has degree (q=p^f).

Thus:

- the degree-2 initial relation records the underlying adjacency;
- the first q-dependent correction occurs at degree (q);
- if (q=p^f<p^k), then
[
qle p^{k-1}<p^{k-1}+1=N_k,
]
so the q-dependent defect lies inside the (W_k) window;
- if (qge p^k), then (q) is invisible at this depth and
[
1+qequiv1pmod{p^k},
]
so the canonical orientation itself is trivial modulo (p^k).

This gives a strong candidate for the same observability threshold:
[
N_k=p^{k-1}+1.
]

But this is **only a candidate mechanism**, not yet a theorem. The missing step is intrinsic extraction of the degree-q defect from the abstract finite quotient.

## 5. The key new obstruction

There is a subtle issue absent from the one-parameter Demuškin calculation.

In the Demuškin case, the q-defect was tied to a distinguished relation whose intrinsic defect could be classified globally.

For an oriented RAAG there may be many special edges/sinkholes. The finite window must recover not just "there exists a q-defect", but the **intrinsic subspace/support on which the canonical orientation is nontrivial**.

Schematically:
[
W_k
ightsquigarrow
	ext{degree-2 graph object}
ightsquigarrow
	ext{degree-q deformation module}
ightsquigarrow
(	ext{sinkhole support},q)
ightsquigarrow
[	heta_Gammamod p^k].
]

The deformation module is therefore the correct object to attack, not the entire associated graded direct sum.

## 6. Why this is preferable to locally-uniform / θ-abelian groups

Locally uniform pro-p groups also have canonical orientations and are 1-cyclotomic. However, their basic structure is already described by a semidirect form with a single p-power parameter:
[
mathbf Z_p^Itimesmathbf Z_p,
]
so they risk collapsing back into the same q-parameter phenomenon.

The RAAG class retains a finite combinatorial incidence structure in addition to q. The literature explicitly develops canonical orientations for oriented RAAGs and characterizes when they are 1-cyclotomic. citeturn1search0turn3search0

Therefore RAAGs are the better first adjacent-class test.

## 7. Current gate classification

| Gate | Status | Reason |
|---|---|---|
| Orientation rigidity | **PASS/LOCAL** | unique Kummerian orientation for special digraphs |
| Non-q structural data | **PASS/LOCAL** | finite defining digraph contributes independent data |
| Intrinsic target | **PASS/LOCAL** | canonical orientation is group-theoretically selected |
| Finite-window threshold (N_k) | **CONDITIONAL** | q-defect degree gives the mechanism, intrinsic descent not proved |
| Graph recovery from finite input | **PASS/LOCAL** | degree-two cohomological/RAAG data provides strong route |
| Directed/sinkhole recovery | **OPEN** | q-dependent deformation must be extracted intrinsically |
| Full (W_kRightarrow[	hetamod p^k]) theorem | **OPEN** | load-bearing separation step remains |
| Genuine novelty | **OPEN** | depends on intrinsic separation rather than presentation reading |

## 8. Exact next attack

Do **not** search for another carrier yet.

Attack the following proposition:

> **RAAG Orientation Separation Problem.**  
> Let (G_{Gamma,q}) and (G_{Delta,r}) be special oriented pro-p RAAGs of the declared finite type. If
> [
> W_k(G_{Gamma,q})cong W_k(G_{Delta,r}),
> ]
> must the induced canonical orientations satisfy
> [
> [	heta_{Gamma,q}mod p^k]
> =
> [	heta_{Delta,r}mod p^k]?
> ]

Break it into two subclaims:

### S1 — underlying graph

Show that the finite window determines the degree-two graph object intrinsically.

### S2 — orientation deformation

After S1 identifies the graph layer, show that the first q-dependent relation-module defect inside degree (<N_k) determines the sinkhole support and (qmod p^k).

Only if S2 survives without choosing the original presentation should the branch advance.

## 9. Stop condition

If S2 turns out to require an external choice of the defining digraph or relator basis, classify:

**FAIL/CLOSED — presentation-level re-encoding.**

If S2 can be expressed through an intrinsic relation-module/extension-class object of (W_k), classify:

**OPEN → candidate finite-window orientation theorem.**

That distinction is the decisive novelty test.

## 10. Final decision

The research question is now sharpened to:

[
oxed{
	ext{special oriented pro-p RAAG}
quadlongrightarrowquad
	ext{intrinsic finite-window orientation separation}
}
]

This is a materially better adjacent-class target than free pro-p or θ-abelian/local-uniform groups.

Current classification:

[
oxed{	ext{RAAG adjacent class = OPEN / LOAD-BEARING}}
]

No claim is made yet that the finite-window theorem holds. The next authorized calculation/proof is only S1 → S2, with special attention to intrinsic relation-module descent and avoidance of presentation-level re-encoding.
