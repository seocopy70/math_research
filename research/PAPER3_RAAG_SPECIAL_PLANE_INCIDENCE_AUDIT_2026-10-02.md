# PAPER 3 FOLLOW-UP — SPECIAL-PLANE INCIDENCE / NON-ABELIAN (W_q) GATE — 2026-10-02

## Decision

The statement “(W_q) is non-abelian, therefore the intrinsic extension carrier is unavailable” is **too strong**.

The full bilinear pairing
[
kappa_q:W_q	imes W_q	o A_q
]
is indeed unavailable when (W_q) is non-abelian. But the finite window still contains a canonical **2-dimensional incidence test** that does not require (W_q) to be abelian.

The replacement is not to force a bilinear (kappa_q), but to inspect, for each 2-plane (Ule L_1=D_1/D_2), the first Zassenhaus degree at which an independent pair in (U) has a nonzero commutator defect.

This yields a new candidate intrinsic carrier:
[
mathscr S_n(G)
=
left{
Uin operatorname{Gr}(2,L_1):
egin{array}{l}
	ext{some independent }x,yin U	ext{ commute in }W_n,\
[	ilde x,	ilde y]
otin D_{n+1}
end{array}
ight}.
]
Equivalently, define
[
ho(U)=min{n:exists	ext{ independent }x,yin U, 
[	ilde x,	ilde y]in D_nsetminus D_{n+1}}.
]
Then (mathscr S_n={U:ho(U)=n}).

The definition uses only the filtered group (G) through its finite windows, not a presentation, generator labels, relator, or (q).

## 1. Why the previous “non-abelian wall” is not the final obstruction

For (W_n=G/D_n), the commutator of two arbitrary elements need not lie in (A_n=D_n/D_{n+1}). This prevents a global bilinear (kappa_n).

However, if (ar x,ar yin W_n) commute, then
[
[	ilde x,	ilde y]in D_n.
]
If the lifts are changed by (D_n), the commutator changes by an element of
[
[D_n,D_1]subseteq D_{n+1}.
]
Hence the class
[
[	ilde x,	ilde y]mod D_{n+1}in A_n
]
is well-defined for **commuting pairs**.

Thus the correct object is a partially defined commutator defect on the intrinsic commuting-pair locus, not a bilinear form on all of (W_n).

The Zassenhaus identities
[
[D_i,D_j]subseteq D_{i+j},qquad D_i^psubseteq D_{pi}
]
justify the lift-independence mechanism.

## 2. Why the 2-plane formulation is necessary

A naive set of all commuting-pair defects is too large.

Even inside a free pro-(p) origin subgroup, one can manufacture pairs whose degree-one parts are dependent while their first nonzero commutator occurs at a high filtration level. Those pairs are not the special-edge phenomenon.

Therefore impose the intrinsic condition:
[
dimlangle ar x,ar yangle=2
quad	ext{in }L_1.
]

This removes the “same degree-one direction plus deep correction” contamination.

The resulting object is projective/Grassmannian rather than bilinear:
[
U=langle ar x,ar yangleinoperatorname{Gr}(2,L_1).
]

This is still intrinsic under filtered-group isomorphisms.

## 3. Local test: the non-commuting-origin special line

Consider the first genuinely non-abelian-origin model
[
G=
langle x,y,zmid
xyx^{-1}=y^{1+q},;
xzx^{-1}=z^{1+q}
angle
=
langle y,zangletimeslangle xangle,
]
where (langle y,zangle) is free pro-(p).

This is the special line-digraph model studied in the oriented pro-(p) RAAG literature. The literature independently identifies (langle y,zangle) as a free pro-(p) group.

### 3.1 Degree-2 ordinary sector

The origin subgroup is free, so
[
[ar y,ar z]
e0in L_2.
]
Thus every 2-plane contained in
[
V_1:=operatorname{span}{ar y,ar z}
]
has ordinary degree-2 commutator defect.

Hence
[
ho(U)=2
qquad(Usubseteq V_1, dim U=2).
]

### 3.2 Special planes

For every nonzero (uin V_1), the pair (x,u) has no degree-2 commutator because (x) is joined by a special edge to both origin vertices. Its first nonzero commutator occurs at degree (q):
[
[x,u]equiv u^{q}pmod{D_{q+1}}
]
at the associated first-survival level.

Therefore
[
ho(operatorname{span}{ar x,u})=q.
]

If instead
[
U=operatorname{span}{ar x+v,u},
qquad v,uin V_1,quad v
otinmathbf F_pu,
]
then
[
[ar x+v,u]_2=[v,u]_2
e0,
]
because (V_1) is free at degree two. Hence
[
ho(U)=2.
]

Consequently the (q)-special 2-planes are exactly
[
oxed{
mathscr S_q
=
{
operatorname{span}(ar x,u):
0
e uin V_1
}.
}
]

This is the first important result beyond the commuting-origin model.

### 3.3 Intrinsic recovery of the sinkhole

If (dim V_1ge2), then
[
igcap_{Uinmathscr S_q}U
=
mathbf F_par x.
]

Thus the sinkhole line is recovered **intrinsically as the intersection of the q-special 2-planes**.

At the same time,
[
operatorname{span}igl(igcup_{Uinmathscr S_q}Uigr)
=
mathbf F_par xoplus V_1
]
recovers the whole common-sink sector.

This removes the previous obstacle caused by the non-abelian (W_q).

## 4. Boundary case: one special edge

If the sinkhole has only one special neighbor, (mathscr S_q) contains only one relevant 2-plane, so the intersection construction does not isolate the sinkhole line.

But this is exactly the already solved rank-2 local problem:
[
P_q^{-1}(operatorname{im}kappa_q)
=
mathbf F_par v.
]

Therefore the two mechanisms fit:

- **degree-(q) special-plane incidence** when a sinkhole has at least two independent special neighbors;
- **restricted-power origin-line recognition** for a single special edge.

This is not a new ad hoc case split: the first mechanism detects the sinkhole by incidence, while the second detects the origin by the (q)-power image.

## 5. General specially oriented graph: proposed intrinsic object

For an arbitrary specially oriented graph, define for every finite window level (n):

[
mathscr S_n(G)
=
{Uinoperatorname{Gr}(2,L_1):
ho(U)=n}.
]

Then define the first nontrivial level
[
q_{mathrm{inc}}
=
min{n:mathscr S_n(G)
earnothing, n>2}.
]

The definition is (q)-blind: (q) is not supplied. The level is discovered from the first nonzero filtered commutator defect.

The expected structure for a genuine special graph is:

[
mathscr S_q
=
igcup_{win V^s}
{
operatorname{span}(w,u):
0
e uin S_w
},
]
where (S_wle L_1) is the span of ordinary vertices joined to the sinkhole (w) by special edges.

This would turn the finite window into an intrinsic incidence geometry:
[
	ext{q-special 2-planes}
longrightarrow
	ext{sinkhole lines}
longrightarrow
	ext{special-source subspaces}.
]

## 6. Critical unresolved point

The displayed formula for (mathscr S_q) is **not yet proved for every specially oriented graph**.

The possible obstruction is cancellation in degree 2 for arbitrary linear combinations of vertices. A general proof must establish:

> If an independent 2-plane (Ule L_1) has no degree-2 commutator and has a nonzero first commutator defect at degree (q), then (U) is generated by a sinkhole direction and a vector in its special-neighbor span.

Equivalently, no “accidental” q-special 2-planes may arise from linear combinations crossing different graph neighborhoods.

This is now the precise load-bearing theorem.

## 7. Literature control

Blumer–Quadrelli–Weigel define specially oriented graphs by requiring every special edge to terminate at a special vertex, and identify the canonical orientation as (1+q) on the special/sinkhole vertices and (1) on ordinary vertices. Their two-generator special-edge model gives the local semidirect structure used above, and their Proposition 4.11 gives the embedding of clique subgroups. citeturn5search0turn12search2

Quadrelli's later Frattini-resistance paper explicitly treats the three-vertex special line model
[
langle x,y,zmid xy=y^{1+q}, xz=z^{1+q}angle
]
as (Vtimeslangle xangle) with (V=langle y,zangle) a free pro-(p) group. This independently supports the non-commuting-origin local model used here. citeturn10search12turn12search0

The literature does **not** appear, from the audited material, to supply the finite-window Grassmannian defect carrier or the claimed factorization from (mathscr S_q) to sinkhole lines. That remains the project's own open question.

## 8. Object / Input / Functoriality / Gauge / Orientation / q-blindness / Separation / Novelty / Stop

- **Object:** (mathscr S_nsubseteqoperatorname{Gr}(2,L_1)), defined from filtered commutator survival.
- **Input:** finite filtered windows (W_n) only.
- **Functoriality:** filtered isomorphisms transport (L_1), 2-planes, and commutator survival.
- **Gauge:** presentation/lift choices disappear; lift-independence follows from ([D_n,D_1]subseteq D_{n+1}).
- **Orientation bridge:** once sinkhole/source incidence is recovered, the known canonical formula gives (1+q) on sinkholes and (1) elsewhere; this remains classification-relative, not yet a new orientation theorem.
- **q-blindness:** yes; (q) is discovered as the first nonzero incidence level.
- **Separation:** q=3 and q=(infty) separate by finite first-survival level versus no special defect.
- **Novelty:** potentially non-redundant because the carrier is an incidence geometry of finite filtered commutator survival, not the frozen q-selector; however novelty is **not established**.
- **Stop:** no large computation is needed until the accidental-plane theorem is proved or refuted.

## 9. Current classification

| Claim | Status |
|---|---|
| Full bilinear (kappa_q) on non-abelian (W_q) | FAIL / CLOSED — wrong domain |
| Lift-independent defect on commuting pairs | PASS / LOCAL |
| 2-plane first-survival invariant (ho(U)) | PASS / LOCAL |
| q-special-plane carrier in commuting-origin model | PASS / LOCAL |
| q-special-plane carrier in noncommuting-origin special-line model | PASS / LOCAL |
| Sinkhole recovery by intersection when (dim S_wge2) | PASS / LOCAL |
| Single-edge rank-2 fallback | PASS / LOCAL |
| General special-graph (mathscr S_q) formula | OPEN / LOAD-BEARING |
| Accidental q-special-plane exclusion | OPEN / LOAD-BEARING |
| General directed/sinkhole separation | OPEN / LOAD-BEARING |
| New finite-window orientation theorem | OPEN |
| Naive (operatorname{gr}(R)) route | FAIL / CLOSED — WRONG OBJECT |
| Gauge obstruction | FAIL / CLOSED |
| Paper 3 main result | FROZEN / COMPLETE |

## 10. Decision

The previous statement

> “non-abelian (W_q) blocks the intrinsic extension approach”

is **superseded**.

The correct statement is:

> **Non-abelian (W_q) blocks the global bilinear commutator pairing, but not the finite-window 2-plane first-survival geometry.**

The active Gate D is therefore narrowed to a single theorem:

[
oxed{
	ext{No accidental q-special 2-planes}
}
]

for specially oriented pro-(p) RAAGs.

If this theorem passes, the next step is intrinsic reconstruction of the sinkhole/source incidence graph from (mathscr S_q). If it fails, the explicit counterexample should be retained as the new categorical obstruction.

No large computation, Mixed Fox, (O_k), (W_{11}/W_{12}), Paper 2, or frozen Paper 3 branch is reopened.


## 11. Gate D resolution: explicit accidental-plane counterexample

The load-bearing theorem is **refuted** on the full class of specially oriented graphs.

Take the complete underlying graph on three vertices ({s,a,b}), with (s) the unique special/sinkhole vertex, special edges
[
a	o s,qquad b	o s,
]
and the ordinary edge (aleftrightarrow b). Thus
[
G=langle s,a,bmid asa^{-1}=s^{1+q},;bsb^{-1}=s^{1+q},;[a,b]=1angle.
]
This is an admissible complete specially oriented graph: the literature explicitly states that a complete special graph has at most one special vertex, and if present every other vertex is joined to it by a special edge. citeturn0search0

Here the degree-2 commutator sector is zero for every pair of degree-one generators, so (W_q) is abelian and the original (kappa_q) is actually available.

Let
[
L_1=mathbf F_par soplusmathbf F_par aoplusmathbf F_par b.
]
Modulo (D_{q+1}), the special relations give
[
B_q(ar a,ar s)=ar s^{,q},qquad
B_q(ar b,ar s)=ar s^{,q},qquad
B_q(ar a,ar b)=0,
]
up to the harmless global sign convention for the commutator. Thus (B_q) is a nonzero alternating form with radical
[
R=mathbf F_p(ar a-ar b).
]

For a (2)-plane (Ule L_1), the first-survival degree is (q) exactly when (B_q|_U
e0), equivalently when (R
otsubset U). Consequently
[
mathscr S_q
=
{Uinoperatorname{Gr}(2,L_1):R
otsubset U}.
]

This immediately destroys the proposed sinkhole-intersection rule. For example,
[
U_1=operatorname{span}(ar s,ar a),
qquad
U_2=operatorname{span}(ar s+ar a,ar b)
]
both lie in (mathscr S_q), but
[
U_1cap U_2=0.
]
Hence
[
igcap_{Uinmathscr S_q}U=0,
]
not (mathbf F_par s).

The failure is not a presentation artifact. The entire calculation is in the intrinsic finite-window extension defect because the complete graph makes (W_q) abelian. In particular, the accidental plane
[
U_2=operatorname{span}(ar s+ar a,ar b)
]
is a genuine intrinsic q-special plane, not a lift or coordinate illusion.

The mechanism is transparent: when the ordinary vertices (a,b) commute, a tilted plane can retain the same degree-(q) special defect. The previous “free origin sector forces (v,u) independent (Rightarrow) degree-2 obstruction” argument is therefore only valid when the relevant origin directions have nontrivial degree-2 commutator.

### 11.1 Consequence

The proposed theorem

> every (q)-special independent (2)-plane is generated by a sinkhole direction and a special-neighbor direction

is **FAIL / CLOSED** for arbitrary specially oriented RAAGs.

The stronger statement that the (q)-special Grassmannian itself canonically recovers the sinkhole/source incidence is also **FAIL / CLOSED** in this category.

What survives is a conditional/local theorem for graphs in which the ordinary-neighbor sector has sufficient degree-2 noncommutativity. The complete-graph counterexample is the sharp small obstruction and must be retained.

### 11.2 What the counterexample teaches

The failure is structural, not accidental:

- If the ordinary-neighbor sector has a nonzero degree-2 bracket, tilted planes are often rejected already at degree 2.
- If that sector is abelian, degree-2 separation disappears.
- Then the degree-(q) defect descends to an alternating form on a larger degree-one space.
- Its Grassmannian support records the form's radical, not the distinguished sinkhole line.
- Therefore **first-survival 2-plane incidence is too coarse to distinguish the sinkhole from ordinary directions in complete special graphs.**

This closes the current carrier, but does **not** establish a general impossibility theorem for every intrinsic finite-window carrier.

## 12. Final Gate D classification

- non-abelian (W_q) as a global bilinear-pairing obstruction: **FAIL / CLOSED — superseded**;
- special-plane first-survival carrier: **FAIL / CLOSED — explicit counterexample**;
- accidental q-special-plane exclusion: **FAIL / CLOSED**;
- sinkhole recovery by (mathscr S_q)-intersection: **FAIL / CLOSED**;
- conditional special-plane theorem under noncommuting-origin hypotheses: **PASS / LOCAL**;
- general directed/sinkhole separation by this carrier: **FAIL / CLOSED**;
- existence of some other intrinsic finite-window carrier: **OPEN**.

The research frontier therefore moves one level upward: the obstruction is no longer “non-abelian (W_q)” but **coarseness of the first-survival Grassmannian carrier even when (W_q) is abelian**.

No further computation of this carrier is authorized.
