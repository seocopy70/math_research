# CONVENTION CORRECTION AUDIT — 2026-10-02

## Controlling literature convention

Blumer–Quadrelli–Weigel define an edge e=(v,w) with origin v and terminus w. A special edge is an edge whose inverse is absent. The origin of every edge is ordinary; a vertex is special precisely when it is the terminus of a special edge. For a special edge (v,w), the defining relation is
[
w v w^{-1}=v^{1+q}.
]
Hence, in abelianization,
[
v=v^{1+q}Longrightarrow v^q=1.
]
Therefore the ordinary origin v is the q-torsion direction, while the special terminus w is not made torsion by this relation. The source explicitly distinguishes the special vertex (terminus) from the ordinary origin. citeturn1search0turn1search1

## Project-wide correction

Every RP-3 statement that identified the torsion/annihilator sector with the special/sinkhole set is reversed under the literature convention.

Use:
[
O={	ext{ordinary origins of special edges}},qquad
S={	ext{special termini/sinkholes}}.
]

Then
[
G^{ab}cong (mathbf Z/q)^{O}oplusmathbf Z_p^{Vsetminus O}.
]

At the adjacent jump,
[
W_q^{ab}cong(mathbf Z/q)^V,
qquad
W_{q+1}^{ab}cong(mathbf Z/pq)^{Vsetminus O}oplus(mathbf Z/q)^O.
]
Consequently the q-blind exponent-jump carrier satisfies
[
mathcal L(W_q,W_{q+1})
={chiin H^1(G,mathbf F_p):chi|_{langle Oangle}=0},
]
and therefore
[
mathcal L(W_q,W_{q+1})^perp
=operatorname{span}{ar v:vin O}subseteq L_1.
]

Thus the RP-3 carrier architecture survives, but its recovered subspace is the origin plane, not the sinkhole plane.

## Status

- Literature convention: VERIFIED.
- RP-3 torsion-sector label: CORRECTED / SUPERSEDES EARLIER SINKHOLE LABEL.
- RP-3 q-blind adjacent-window construction: PASS / LOCAL after correction, for the origin/torsion sector.
- Any claim that this carrier directly recovers the special/sinkhole sector: REJECTED unless an additional intrinsic bridge O↔S is proved.
- RP-5 same-abelianization extension separation: unaffected in substance; its O/S notation already follows the corrected convention.
- Grassmannian branch: FAIL / CLOSED and not reopened.

Detailed source: Blumer–Quadrelli–Weigel, Oriented right-angled Artin pro-ℓ groups and maximal pro-ℓ Galois groups, and Directed graphs, Frattini-resistance, and maximal pro-p Galois groups. citeturn1search0turn1search1
