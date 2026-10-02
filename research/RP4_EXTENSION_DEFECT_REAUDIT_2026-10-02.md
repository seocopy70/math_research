# RP-4 Extension Defect Re-Audit — 2026-10-02

## Status

**RP-4 as formulated in the 2026-10-02 draft is NOT validly closed.**  
The draft contains two decisive mathematical errors:

1. the proposed equivalence
   [
   mathcal C	ext{ graph-sensitive}iff mathcal C	ext{ does not factor through abelianization}
   ]
   is too strong; non-factorization is necessary for separation of equal-abelianization objects, but not sufficient;

2. the claim that the extension commutator defect (kappa_n) factors through abelianization is false. In the rank-2 special-edge model, the first nonzero defect occurs at (n=q) and detects the nontrivial filtered commutator/power extension data.

The previously recorded local results in
`research/PAPER3_RAAG_2GEN_FILTERED_EXTENSION_DEFECT_AUDIT_2026-10-02.md`
and
`research/PAPER3_RAAG_3VERTEX_COMMON_SINK_AUDIT_2026-10-02.md`
remain controlling. The Grassmannian/special-plane carrier remains **FAIL / CLOSED**; that failure must not be conflated with failure of the extension-defect object itself.

## 1. Correction to Part I: graph-sensitive criterion

Let B denote the separation property:

[
existsGamma_1,Gamma_2,quad
G_{Gamma_1}^{ab}cong G_{Gamma_2}^{ab},
qquad
mathcal C(Gamma_1)
otcongmathcal C(Gamma_2).
]

Then B is the actual separation criterion.

If (mathcal C=Fcirc(-)^{ab}), B is impossible. Hence:

[
	ext{factorization through abelianization}Longrightarrow
eg B.
]

But the converse is not valid:

[

eg(	ext{factorization through abelianization})

otRightarrow B.
]

A non-abelian invariant may depend on the group beyond abelianization while nevertheless taking the same value on every pair in the restricted graph class having the same abelianization. Therefore the proposed iff is rejected.

For the present project, the safe working hierarchy is:

- A: intrinsic/functorial;
- B: existence of a same-abelianization separating pair;
- C: incidence reconstruction.

B, not non-factorization alone, is the graph-sensitivity test.

## 2. Correction to the extension calculation

For the Zassenhaus filtration,

[
A_n:=D_n/D_{n+1}
]

is central in

[
1	o A_n	o W_{n+1}	o W_n	o1.
]

When (W_n) is abelian, the commutator of lifts gives a well-defined alternating map

[
kappa_n:Lambda^2 W_n	o A_n.
]

The crucial point is that (kappa_n) is an invariant of the **extension multiplication**, not of (G^{ab}) alone.

### Rank-2 special-edge model

For

[
G=langle v,wmid wvw^{-1}=v^{1+q}angle,
qquad q=p^f, p	ext{ odd},
]

one has

[
G'=overline{langle v^qangle}subseteq D_q.
]

Consequently

[
operatorname{im}kappa_n=0quad(n<q),
]

while

[
operatorname{im}kappa_q
=
G'D_{q+1}/D_{q+1}
=
mathbf F_p,overline{v^q}
e0.
]

This is the first nonzero extension-defect degree. In particular, the statement that the defect first appears already in (K_2=D_2/D_3) is wrong for (qge3): since (v^qin D_qsubseteq D_3), its class in (D_2/D_3) is zero.

Thus the following calculation in the draft is invalid:

[
[	ilde x,	ilde s]=	ilde s^q
quadLongrightarrowquad
overline{[	ilde x,	ilde s]}=ar s^qin D_2/D_3.
]

For odd (p), the right conclusion is that the class vanishes in (D_2/D_3) and first becomes visible in (D_q/D_{q+1}).

## 3. Why “(kappa_n) is an abelianization factor” is false

The source of the error is a conflation of the **domain** and the **data defining the extension**.

Even when (W_n) is abelian, so that the domain can be written as an exterior square of an elementary/abelian quotient, the map (kappa_n) is determined by the multiplication law of (W_{n+1}). Two central extensions of the same abelian base by the same kernel can have different extension classes and different commutator pairings.

The elementary finite-group prototype is:

[
1	o C_p	o E	o C_p	imes C_p	o1,
]

where the split extension (C_p^3) and the exponent-(p) Heisenberg extension have the same base and kernel but different commutator structure. Hence the extension class is not determined by the abelianization data ((Q,A)).

Therefore:

[
oxed{kappa_n	ext{ is not an abelianization factor in general}.}
]

This does **not** by itself prove graph separation for the specially oriented RAAG class; it proves only that the proposed no-go argument is invalid.

## 4. What survives from the complete/common-sink calculations

The following local facts remain valid at the declared scopes:

- 2-generator special-edge model:
  [
  operatorname{im}kappa_q=mathbf F_poverline{v^q},
  qquad
  P_q^{-1}(operatorname{im}kappa_q)=mathbf F_par v.
  ]
  Classification: **PASS / LOCAL**.

- 3-vertex common-sink commuting-origin model:
  [
  operatorname{im}kappa_q
  =
  operatorname{span}{overline{v_1^q},overline{v_2^q}},
  ]
  and the restricted-power preimage recovers the ordinary/origin plane. Classification: **PASS / LOCAL**.

- complete 3-vertex graph with one sinkhole:
  the degree-(q) defect becomes an alternating form whose Grassmannian support admits accidental (q)-special planes. The proposed plane-intersection carrier fails. Classification: **FAIL / CLOSED** for that carrier.

Hence the correct conclusion is not

[
kappa_n	ext{ fails because it is abelianization-only},
]

but rather

[
oxed{
	ext{the raw commutator defect is genuine filtered extension data,
while the particular Grassmannian extraction from it fails globally.}
}
]

## 5. Correct next gate

RP-5 should **not** be started from the premise that RP-4 has been closed.

The next mathematically meaningful branch is:

[
oxed{	ext{full central extension class}
quad [E_n]in H^2(W_n,A_n)}
]

with the following pre-checks:

1. **Object:** the actual finite central extension
   (E_n=W_{n+1}	o W_n), not merely ((W_n,A_n));

2. **Input:** the declared finite-window input must be fixed precisely;

3. **Functoriality:** filtered group isomorphisms/morphisms must induce the extension class naturally;

4. **Gauge:** presentation/lift choices must disappear;

5. **Orientation bridge:** identify exactly what part, if any, of ([E_n]) maps to the canonical special/sinkhole structure;

6. **q-blindness:** define the construction for arbitrary (n), and detect (q) as a first-defect degree rather than inserting (q);

7. **Separation:** test whether the extension class distinguishes graphs with identical abelianization;

8. **Novelty:** avoid merely restating the known finite quotient extension class;

9. **Stop:** if the full extension class is already completely determined by the allowed finite-window input but yields no new separation, close only that carrier.

## 6. Classification after correction

| Claim | Correct status |
|---|---|
| Central extension (1	o D_n/D_{n+1}	o W_{n+1}	o W_n	o1) | PASS / CLOSED |
| (kappa_n) for abelian (W_n) | PASS / CLOSED |
| (kappa_q) first nonzero in rank-2 model | PASS / LOCAL |
| (kappa_q) detects origin direction via (P_q) in rank-2 | PASS / LOCAL |
| common-sink commuting-origin test | PASS / LOCAL |
| Grassmannian special-plane carrier | FAIL / CLOSED |
| “(kappa_n) factors through abelianization” | **FAIL / CLOSED — FALSE CLAIM** |
| “RP-4 extension-defect carrier is globally closed” | **FAIL / CLOSED — PREMATURE** |
| full extension class as a new carrier | **OPEN / LOAD-BEARING** |
| general graph-incidence recovery | **OPEN / LOAD-BEARING** |

## 7. Decision

The proposed RP-5 direction is mathematically legitimate, but the immediate action is a **corrected RP-4 → RP-5 gate**, not a wholesale jump to (H^2(W_1,K_1)).

In particular, computing (H^2(W_1,K_1)) first would be too early: it describes the degree-2 extension, whereas the special q-defect is a higher filtered extension phenomenon. For (q>2), the degree-2 class and the degree-(q) correction are distinct layers.

The first authorized RP-5 computation should therefore compare the **full extension classes across the first two informative layers**:

[
[E_1]in H^2(W_1,A_1)
quad	ext{and}quad
[E_q]in H^2(W_q,A_q),
]

with the rank-2 and complete/common-sink models as controls, and with the explicit requirement that the (q)-layer be reached intrinsically as the first nonzero defect.

**Current branch status:**
[
oxed{	ext{RP-4: OPEN / CORRECTED}}
]
[
oxed{	ext{RP-5: OPEN / AUTHORIZED AFTER PRE-CHECK}}
]

No large computation is authorized until the above object/input/functoriality/gauge/orientation/q-blindness checks are written down.
