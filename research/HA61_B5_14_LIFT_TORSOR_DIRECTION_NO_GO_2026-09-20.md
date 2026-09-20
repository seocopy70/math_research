# HA61-B5-14 — LIFT-TORSOR DIRECTION ATTACK — 2026-09-20

## Verdict

**FAIL / CLOSED for a canonical one-dimensional lift direction constructed from the intrinsic pair (H^1(G,F_3), cup product, f) alone.**

The full coefficient-lift torsor has dimension 4 over F_3. Assuming the still-open variation identity
delta_{3,rho_3(1+9nu)}(f)-delta_{3,rho_3}(f)=±(nu cup f),
the zero set is an affine hyperplane parallel to f^perp, of dimension 3. Restricting to a one-dimensional direction can restore uniqueness only if that direction is canonically chosen transverse to f^perp.

The symplectic structure alone does not supply such a transverse line functorially.

## 1. Object

Let V=H^1(G,F_3), dim V=4, with nondegenerate alternating Demushkin cup pairing < , >:V×V→H^2(G,F_3)≅F_3 after the already-fixed common normalization.

For f≠0, define
K_f = {nu in V : nu cup f=0}=f^perp.
Then dim K_f=3.

Under the candidate variation formula, the obstruction function on the lift torsor is affine-linear with linear part nu↦nu cup f. Hence its kernel, when nonempty, is an affine translate of K_f.

## 2. Direction no-go from the symplectic data alone

A one-dimensional direction L=F_3·d yields a unique zero only if d cup f ≠ 0.

The data (V,<,>,f) canonically determine the line F_3 f, but
f cup f=0
because the pairing is alternating. Therefore the canonically obvious line is useless for selection: the obstruction is constant along it.

More generally, any transverse line to f^perp is a choice of symplectic dual to f. There is no canonical such line from (V,<,>,f) alone. The stabilizer of f in Sp(V) preserves f and f^perp but acts nontrivially on the set of transverse lines; a choice of one transverse line is extra structure.

Therefore:

**No canonical one-dimensional lift direction exists in the bare intrinsic symplectic data.**

This is a genuine symmetry obstruction, not a failure of computation.

## 3. Consequence for the current program

The surviving delta_3 family cannot be compressed to a unique rho_3 by:

- the full lift torsor alone;
- the cup pairing plus f;
- a canonically chosen line obtained only from f and the Demushkin symplectic structure.

Thus the question is sharpened.

A unique finite selector can still exist only if the declared filtered/relation input contributes additional intrinsic structure that canonically chooses a transverse direction (or an equivalent quotient) in the lift torsor.

## 4. Authorized next attack

Test the actual filtered input, not the abstract symplectic shadow.

Candidate extra data at the current depth include the intrinsic relation-jet pair (R,p) or its already-established coarsening. The required theorem is:

filtered input -> a functorial affine one-dimensional sub-torsor L_f subset L(rho_2)

such that the variation functional nu↦nu cup f is nonzero on its direction.

This must pass:

1. Object: exact one-dimensional sub-torsor/quotient.
2. Input: only the declared finite filtered/relation input.
3. Functoriality: invariance under presentation and relator gauge.
4. Gauge: no chosen H^2 generator or coefficient trivialization may be smuggled in.
5. Orientation bridge: the line must arise before selecting the zero.
6. q-blindness: no q or chi.
7. Separation: q=3, q=9, and power-free controls must remain distinguishable where required.
8. Novelty: it must be more than Serre's existing coefficient-lifting characterization in disguise.

If no such transverse line/quotient survives the gauge and symmetry audit, then the full delta_3 family is intrinsically higher-dimensional and there is a hard logical boundary against unique mod-27 recovery from this input.

## Classification

- B5-13 zero-selector uniqueness: **FAIL / CLOSED**.
- Variation identity: **OPEN / DECISIVE**.
- Canonical 1D direction from (V,cup,f) alone: **FAIL / CLOSED**.
- Filtered-input-induced transverse direction: **OPEN / DECISIVE**.
- HA61-C: **not opened**.
