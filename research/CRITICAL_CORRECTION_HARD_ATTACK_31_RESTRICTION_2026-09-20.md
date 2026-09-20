# CRITICAL CORRECTION — HARD ATTACK 31 TOP-CLASS RESTRICTION CLAIM

## 2026-09-20

### 1. The load-bearing error

Hard Attack 31 asserted that for the canonical PD^2 coefficient A=A_k(chi), the top/fundamental class restricts nontrivially to the open subgroup N=P_{k+1}(G), and used this to conclude that the quotient-inflation image is zero.

This is not justified and is contradicted already at k=1 by the standard PD^2/Demuškin behavior: for a proper open subgroup of p-power index, restriction of the mod-p degree-two fundamental class can be zero. A concrete surface/Demuškin source records precisely that for an open subgroup L of index divisible by p, Res:H^2(G,F_p)->H^2(L,F_p) is zero. The underlying top-dimensional pullback is multiplication by the covering degree, hence vanishes mod p.

For the present branch, k=1 has A_1(chi)=F_3 because chi mod 3 is trivial. Therefore the asserted nonzero restriction fails at the first level. The Hard Attack 31 argument
“canonical top class restricts nontrivially => inflation image is zero”
is invalid.

### 2. Consequence

The following previous classifications must be REOPENED:

- coker(delta) as an orientation selector: NOT CLOSED by Hard Attack 31;
- Fitting/annihilator invariants depending on coker(delta): NOT CLOSED by that argument;
- the statement that the canonical class necessarily lies in the E_infty^{0,2} top row: FALSE/UNJUSTIFIED;
- the claim E_infty^{1,1}(G,chi)=0 derived from that row placement: UNJUSTIFIED.

What remains valid is only the exact spectral-sequence identity
coker(delta) ≅ im(inflation H^2(Q,A)->H^2(G,A)).
That identity itself is standard and remains PASS.

### 3. Stronger structural correction

For a proper open subgroup N of a PD^2/Demuškin group, the restriction of degree-two mod-p classes may vanish. Therefore the canonical class can lie in the lower part of the LHS filtration rather than the top q=2 row.

This changes the research geometry substantially:

q=0 inflation is no longer automatically “too shallow”; it may carry the global fundamental class after restriction kills it.

The earlier dichotomy
“q=0 is quotient-only, q=2 is orientation”
was too crude. The extension filtration can place the orientation class in F^1/F^2 or F^2.

### 4. New binding task

The next attack must compute, for the canonical coefficient action, the actual LHS filtration of H^2(G,A_k(chi)):

- determine the inflation image;
- determine E_infty^{1,1};
- determine whether the canonical class is represented by quotient inflation, middle-row data, or a nontrivial extension of filtration pieces;
- then test whether the resulting finite defect is a genuine selector.

No numerical scan is authorized until this filtration placement is proved.

### 5. Literature sanity check

The LHS spectral sequence has
E_2^{p,q}=H^p(Q,H^q(N,A)) => H^{p+q}(G,A), and the five-term sequence identifies the relevant transgression/inflation edge. Standard references also emphasize that the differentials and extension problems are the non-automatic part of the spectral sequence.

The PD^2/Demuškin literature confirms that the canonical orientation is the action on the dualizing module, but this does not imply nonzero restriction of a mod-p top class to a proper p-power-index open subgroup.

### 6. Revised status

- Hard Attack 31 exact coker identity: PASS / LOCAL.
- Hard Attack 31 selector closure: **HISTORICAL / SUPERSEDED**.
- coker-based orientation selector: **OPEN**.
- Fitting/annihilator of coker: **OPEN**.
- middle-row E_infty^{1,1}: **OPEN**.
- raw top-row d_3 with imported H^2(N,A): still non-tautological FAIL/CLOSED.
- universal orientation reconstruction: **OPEN**.

This correction takes precedence over the previous Hard Attack 31 closure.
