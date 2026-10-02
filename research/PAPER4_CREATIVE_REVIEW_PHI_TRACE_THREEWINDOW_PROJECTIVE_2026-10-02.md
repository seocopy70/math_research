# PAPER 4 — CREATIVE RE-EXAMINATION OF Φ / TRACE / THREE-WINDOW / PROJECTIVE ROUTES — 2026-10-02

## Decision

The proposed global-linear reformulation is useful, but its strongest hoped-for conclusions do not survive structural stress tests.

The outcome is mixed:

- Φ: **PASS / LOCAL as an intrinsic package**, but its rank-one atoms do not in general determine the orientation functional.
- rank-one atom extraction: **FAIL / CLOSED as a universal normalization mechanism**.
- trace/total-mass functional on Im Φ: **FAIL / CLOSED in the general specially oriented chordal class**.
- three-window upgrade: **OPEN / LOCAL**, but no evidence currently shows that it repairs the first-order obstruction; in the basic q=p^{k-1} regime the q^2 terms are already invisible modulo p^k.
- projective-class relaxation: **FAIL / CLOSED for exact χ mod p^k**, because scalar normalization changes the first q-coefficient.
- affine-hull route: **FAIL / CLOSED for the naive normalized-signature set**, by an explicit chordal multi-sink incidence model whose affine hull has codimension >1.

## 1. What survives

Writing
[
Phi:U	ooperatorname{Hom}(O,A),qquad
Phi(u)=B_q(u,-)
]
is a genuine change of viewpoint. It packages all origin tests simultaneously and avoids the false premise that each direction must be individually pure.

Likewise the intrinsic restricted-power map
[
P_E(ar x)=	ilde x^{,exp(W_q)}
]
is a legitimate q-blind local target in the audited window, subject to the previously recorded scope limitations.

Thus the linear-algebra package is worth retaining as a diagnostic language.

## 2. Fatal problem with "rank-one atoms"

The phrase "support is minimal" is not intrinsic in a bare vector space. It requires a decomposition/basis or an additional canonical support structure.

Rank-one tensor elements are intrinsic, but their preimages need not determine the desired orientation hyperplane. In particular, overlapping sinks can have identical rank-one images, while the orientation functional lives on a larger domain.

Therefore:
[
	ext{rank-one atoms of }operatorname{Im}Phi

otRightarrow
omega_q
]
without an additional theorem.

## 3. Decisive trace obstruction

Consider the specially oriented chordal tree with ordinary vertices (a,b) and special vertices (s,t,u), with special edges
[
a	o s,qquad b	o t,qquad a	o u,qquad b	o u.
]
The underlying graph is the path
[
s-a-u-b-t,
]
hence chordal. Every special edge terminates at a special vertex, so the graph is specially oriented.

At the first q-defect layer, after identifying the origin q-power targets (P_a,P_b), the pairing has the incidence form
[
Phi(ar s)=P_a,qquad
Phi(ar t)=P_b,qquad
Phi(ar u)=P_a+P_b.
]

Suppose a canonical total-mass functional
[
	au:operatorname{Im}Phi	omathbf F_p
]
were to satisfy
[
	au(Phi(ar s))=
	au(Phi(ar t))=
	au(Phi(ar u))=1.
]
Then linearity forces
[
1=	au(P_a+P_b)=	au(P_a)+	au(P_b)=2.
]
For odd (p), this is impossible.

Hence:

[
oxed{
	ext{No universal trace/total-mass functional on }operatorname{Im}Phi
	ext{ can normalize all special directions.}
}
]

This is a structural counterexample, not a computational accident.

The obstruction is exactly the non-uniform incidence relation
[
c_u=c_s+c_t
]
among sink columns. It shows that the proposed "sum of coefficients" is not a well-defined linear functional of the pairing image in general.

## 4. Consequence for affine-hull normalization

For the same tree, write
[
u=alphaar s+etaar t+gammaar u.
]
Then
[
B_q(u,ar a)=(alpha+gamma)P_a,qquad
B_q(u,ar b)=(eta+gamma)P_b.
]

If the normalized-signature condition asks for equality with the intrinsic q-power target on both origin sectors, then
[
alpha+gamma=1,qquad
eta+gamma=1.
]
Its solution set is the affine line
[
mathcal S_{m both}
=
{(1-gamma,1-gamma,gamma):gammainmathbf F_p}.
]

Its affine hull has dimension (1) inside
[
Usimeqmathbf F_p^3,
]
hence codimension (2), not codimension (1).

The set contains both the genuine sink direction (ar u) and the accidental direction
[
ar s+ar t.
]
Indeed both have the same two total incidence coefficients:
[
Phi(ar u)=Phi(ar s+ar t)=P_a+P_b.
]

Therefore the naive affine-hull theorem
[
operatorname{Aff}(mathcal S_E)=omega_q^{-1}(1)
]
is false for this natural global-pairing signature.

This does not prove that no more elaborate finite-window construction can recover (omega_q); it closes this particular signature-based realization.

## 5. Why this is different from the two-sink overlap

The earlier two-sink one-origin model
[
Phi(s)=Phi(t)=P_a
]
was misleadingly benign: the desired functional
[
omega(alpha s+eta t)=alpha+eta
]
still factors through the one-dimensional image.

The three-sink tree is the first decisive obstruction because it creates a nontrivial linear relation with nonzero coefficient sum:
[
Phi(u)-Phi(s)-Phi(t)=0.
]
That relation is incompatible with assigning value (1) to all three genuine sink directions.

Thus the correct invariant is not merely "rank-one image" or "total mass"; the incidence matrix itself carries relations that can destroy the putative trace.

## 6. Three-window proposal

Adding
[
W_{q-1}leftarrow W_qleftarrow W_{q+1}
quad	ext{or}quad
W_qleftarrow W_{q+1}leftarrow W_{q+2}
]
is logically legitimate only after the input is redefined.

However, in the target regime
[
q=p^{k-1},qquad kge2,
]
the first nonlinear correction satisfies
[
q^2=p^{2k-2}equiv0pmod{p^k}.
]
Thus in the basic special-edge relation
[
(1+q)^m=1+mq+inom m2q^2+cdots,
]
the quadratic q-term is already invisible at the precision relevant to (chimod p^k).

Therefore merely extending one or two filtration levels is not automatically expected to separate first-order incidence collisions. A genuine three-window theorem would have to exhibit a new degree-((q+1)) invariant not already determined by the first q-defect.

Status: **OPEN / LOCAL**, not a current lead.

## 7. Projective relaxation

The proposal to retain only the projective class of (omega_q) does not meet the original target.

The orientation has first correction
[
chi(g)equiv1+q,omega_q(ar g)pmod{p^k}.
]
Replacing (omega_q) by (comega_q), (cinmathbf F_p^	imes), changes the character by
[
q(c-1)omega_q(ar g),
]
which is generally nonzero modulo (p^k).

Thus projective recovery is strictly weaker than recovery of (chimod p^k), unless the theorem explicitly changes its target.

Classification:
**FAIL / CLOSED for the original exact-orientation target.**

## 8. Revised research boundary

The creative reframe therefore yields a useful negative theorem:

[
oxed{
	ext{The pairing image alone does not universally contain enough canonical linear structure
to normalize }omega_q.
}
]

The surviving chain is only
[
W_qleftarrow W_{q+1}
	o O_q
	o P_E
	o Phi,
]
where (Phi) is diagnostic data.

The arrows
[
Phi	o	ext{rank-one atoms}	oomega_q
]
and
[
Phi	ooperatorname{Tr}_Phi	oomega_q
]
are closed in the general class.

## 9. Relation to Gate D

This does not reopen the already closed Gate D for the unrestricted specially oriented RAAG class. That class still has the stronger same-underlying-group/different-orientation obstruction from isolated special vertices.

The present result concerns the only meaningful continuation: even after one removes that obvious object-level defect and attempts a restricted-class T1 realization, the global pairing/trace/affine-hull routes encounter independent structural obstructions.

## Classification

- Φ as global packaging: **PASS / LOCAL**.
- Rank-one atom extraction as universal carrier: **FAIL / CLOSED**.
- Trace/total-mass normalization: **FAIL / CLOSED**.
- Naive normalized affine-hull theorem: **FAIL / CLOSED**.
- Three-window extension: **OPEN / LOCAL**.
- Projective-only target: **FAIL / CLOSED**.
- T1 exact finite-window normalization: **OPEN**, but no longer supported by the tested global-linear constructions.

## Stop condition

Do not continue modifying the same rank-one/trace/affine-hull construction.

Any further positive attempt must introduce genuinely new information beyond the pairing image, or prove a structural theorem on a sharply restricted class that rules out the incidence relation above.

