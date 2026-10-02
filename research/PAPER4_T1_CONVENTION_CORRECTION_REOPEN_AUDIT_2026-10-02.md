# PAPER 4 — T1 CONVENTION CORRECTION / AFFINE-HULL REOPENING — 2026-10-02

## Decision

The earlier T1 affine-hull counterexample based on the separated two-sink vector (s+t) is **HISTORICAL / SUPERSEDED**.

The decisive error is the claim that, in
[
G=langle a,b,s,tmid sas^{-1}=a^{1+q}, tbt^{-1}=b^{1+q}angle,
]
the vertex (t) commutes with (a). In the oriented pro-(p) RAAG convention, absence of an edge means no defining relation; it does **not** imply commutation. The literature explicitly defines relations only for joined pairs, with ordinary edges giving commutation and special edges giving the (1+q) conjugation law. citeturn15search0turn4search0

Thus
[
[st,a]
]
has a genuine lower-filtration contribution coming from (t) against (a). In particular the element (ar s+ar t) does not satisfy the full filtered condition
[
[st,a]in D_q
]
that is required before taking the (q)-layer defect. The earlier computation
[
(st)a(st)^{-1}=sas^{-1}
]
is therefore invalid.

## 1. What survives

The corrected nonabelian observable is:
[
[u,x]in D_q,qquad
[u,x]equiv c_x(u)P_E(x)pmod{D_{q+1}}.
]

The lower-filtration condition must be imposed **before** the (q)-layer projection. This is exactly the correction already recorded in the nonabelian filtered-profile gate.

Under this corrected definition:

- separated two-sink (s+t): **not a valid normalized local witness**; lower contamination blocks it;
- overlapping common-sink (s+t): remains a valid (q)-flat witness, but its defect is (2P_E(a)), not (P_E(a)), so it does not satisfy normalized defect (1);
- rank-two special edge: genuine normalized directions (w+c v) remain valid and have canonical orientation (1);
- the previous separated-model affine-collapse argument disappears.

The literature independently confirms the convention and the local two-generator structure: a special edge (v	o w) gives (wvw^{-1}=v^{1+q}), while an ordinary edge gives commutation; the associated two-generator special-edge group is locally uniform with canonical orientation taking (1+q) on the terminus. citeturn4search0turn15search0

## 2. Corrected T1 target

The reopened target is not the old existential signature (mathcal S_E). It is the **fully filtered normalized local-uniform locus**
[
mathcal S_E^{mathrm{flat}}
=
left{
ar u:
exists,ar xin O, 
[u,x]in D_q, 
[u,x]equiv P_E(x)pmod{D_{q+1}}
ight},
]
with the full lower-filtration condition retained.

This is q-blind at the object level when (P_E) is recovered intrinsically from the adjacent extension, and it does not insert (omega).

The candidate theorem becomes
[
operatorname{Aff}igl(mathcal S_E^{mathrm{flat}}igr)
stackrel{?}{=}
omega_q^{-1}(1)
]
on an orientation-rigid class (for example, excluding isolated special vertices).

This is a genuinely different statement from the closed T1 theorem. It has not yet been proved.

## 3. Immediate control audit

### Separated two-sink

For (s+t), the missing relation ([t,a]=1) is unavailable. The degree-2 commutator of (t) with (a) survives before the (q)-layer. Therefore (s+t
otinmathcal S_E^{mathrm{flat}}).

**Classification: PASS / LOCAL for the corrected obstruction.**

### Overlapping common-sink

If
[
sas^{-1}=a^{1+q},qquad tat^{-1}=a^{1+q},
]
then (st) acts on (a) with factor ((1+q)^2), hence the (q)-defect is (2P_E(a)). For odd (p), it is not normalized to (P_E(a)).

**Classification: PASS / LOCAL.**

### Rank-two special edge

The affine family (w+c v) has the same special conjugation action on (v), and its canonical orientation is (1). Thus the local normalized locus is naturally an affine set rather than a single vertex line.

**Classification: PASS / LOCAL.**

### Chordal tree

The previous coefficient-kernel obstruction does not automatically transfer to (mathcal S_E^{mathrm{flat}}), because the full action retains lower-order information discarded by (Phi). This remains the decisive open control.

**Classification: OPEN / LOAD-BEARING.**

## 4. Consequence for D3

The earlier conclusion that the nonlinear normal-closure object was the *only* surviving route is now too strong.

The corrected full-filtered local locus is a legitimate target-first candidate and must be tested before declaring the normal-closure realization necessary. The normal-closure object remains a valid object-level repair, but it is no longer the unique authorized next object.

The research order is therefore:

1. test the corrected (mathcal S_E^{mathrm{flat}}) on the chordal-tree model;
2. if its affine hull still has a nontrivial orientation kernel, use that kernel to design the smallest nonlinear extension datum;
3. only then return to the normal-closure action.

## 5. Literature boundary

Blumer–Quadrelli–Weigel prove that for a specially oriented graph the canonical orientation is the unique torsion-free Kummerian orientation. Their local 2-generator argument shows that special-edge subgroups are locally uniform and that their canonical orientation is determined by the group structure. This validates the corrected local mechanism, but does not itself prove finite-window affine reconstruction. citeturn4search0turn15search0

No novelty claim is made.

## Classification

- old separated (s+t) affine-hull no-go: **HISTORICAL / SUPERSEDED**;
- corrected full-filtered normalized local locus: **OPEN / LOAD-BEARING**;
- rank-two and overlapping controls: **PASS / LOCAL**;
- chordal-tree affine-hull theorem: **OPEN / LOAD-BEARING**;
- unrestricted finite-window recovery: still **FAIL / CLOSED** by the isolated-special same-window obstruction;
- normal-closure nonlinear action: **PASS / LOCAL object**, but not yet necessary.

## Stop condition

Do not revive the old affine-hull theorem. The next authorized calculation is singular: the chordal-tree test for (mathcal S_E^{mathrm{flat}}). If it fails, construct the exact surviving kernel. If it passes, prove the spanning/uniqueness statement on the restricted class before introducing any larger nonlinear carrier.

## 6. Chordal-tree computation and the mixed-ordinary obstruction

The authorized chordal-tree test gives a useful local result.

For the tree with ordinary origins (a,b) and special vertices (s,t,u), with special edges
[
a	o s,quad b	o t,quad a	o u,quad b	o u,
]
the corrected flatness condition eliminates the old shear direction. In (U=langle s,t,uangle):

- testing against (a) forces the (t)-coefficient to vanish because ([t,a]) has lower degree, while the normalized q-defect is (alpha+gamma=1);
- testing against (b) forces the (s)-coefficient to vanish, while the normalized q-defect is (eta+gamma=1).

Hence (s,u,t) are all in the corrected normalized locus, and their affine hull is
[
alpha+eta+gamma=1,
]
which is exactly the canonical orientation hyperplane on this model.

**Chordal-tree control: PASS / LOCAL.**

But the mixed ordinary control now gives the decisive global boundary. Add an ordinary vertex (z) which has no special incidence with the recovered origin sector. Then (z) has no normalized q-flat witness: against a free/nonincident origin its commutator has lower degree, while against an ordinary commuting neighbor its q-defect is zero. Consequently the corrected normalized locus contains no (z)-direction, and its affine hull cannot equal the full hyperplane
[
omega_q^{-1}(1)
]
inside (U), because that hyperplane permits arbitrary (z)-coefficient.

Thus the corrected affine-hull theorem is still **FAIL / CLOSED on the full orientation-rigid class OR**. The failure is no longer the erroneous separated (s+t) witness; it is the genuine invisibility of ordinary directions.

This is a stronger and cleaner boundary: the full filtered local signature can recover the normalization on the special-incidence sector, but by itself it does not determine the zero extension on ordinary directions.

## 7. Final T1 classification after correction

- old separated (s+t) counterexample: **HISTORICAL / SUPERSEDED**;
- corrected full-filtered local mechanism: **PASS / LOCAL** on separated/overlapping/rank-two/chordal-tree controls;
- corrected chordal-tree affine reconstruction: **PASS / LOCAL**;
- full affine equality on OR: **FAIL / CLOSED** because ordinary non-origin directions remain unconstrained;
- special-incidence-sector reconstruction: **OPEN / LOAD-BEARING**;
- full orientation recovery: **OPEN only through a richer nonlinear extension datum**.

The result reinforces, rather than weakens, the D3 conclusion: after the local nonlinear profile has extracted the special-incidence normalization, the remaining problem is precisely the nonlinear mechanism needed to distinguish the zero ordinary sector from mixed directions. The normal-closure extension-action remains the authorized next structural object.

No new blind carrier hunt is authorized.
