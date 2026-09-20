# HA61-B CORRECTION — SCOPE AUDIT AFTER CRITICAL REVIEW — 2026-09-20

## Verdict

**HA61-B is NOT yet PASS / LOCAL. It remains OPEN / LOAD-BEARING.**

The earlier HA61-B record overclaimed a structural cancellation. The q=3 and q=9 calculations establish that, for the audited frozen standard-family branches, no independently visible additive (B_{\rho_2}) term survives. They do **not** prove that every admissible (A_2)-valued lift / relation jet has no such term modulo the primary zero locus.

The correct status is therefore:

- HA61-A: **PASS / LOCAL**.
- HA61-B: **OPEN / LOAD-BEARING**.
- (B_{\rho_2}=0) for the two audited standard branches: **PASS / LOCAL**.
- General structural vanishing/absorption of (B_{\rho_2}): **OPEN**.
- Intrinsic (t_2): **OPEN / LOAD-BEARING**.
- All-(n) induction: **OPEN / DECISIVE**.

## Why the previous structural claim was too strong

The previous HA61-B argument said that because (\delta_2(f)=0), all old-(\rho_2) contributions belong to the already-satisfied first obstruction and therefore cannot define a new secondary invariant.

That implication is not automatic.

A secondary calculation may contain a term depending on the chosen (A_2)-lift (z), even after the primary obstruction vanishes. To eliminate it one must prove one of the following:

1. it is identically zero on the primary zero locus;
2. it is the coboundary/gauge variation of the chosen (A_2)-lift;
3. it is exactly a transported normalization already fixed at stage (n=2);
4. it can be canonically absorbed into the definition of (t_2).

None of these has yet been established in full generality.

## What the q=3 calculation actually proves

For the frozen standard relator
[
r_3=x_1^3[x_1,x_2][x_3,x_4]
]
with (\rho_2(x_2)=4), direct evaluation gives the same new-parameter slope as the q=9 branch.

This is a strong constraint: the old action does not create an additional visible constant in these branches.

But it is not a universal vanishing theorem for (B_{\rho_2}).

In particular, q=3 tests one specific relation jet and one specific coefficient action. It does not test:
- arbitrary degree-(ge3) relation jets;
- arbitrary (A_2)-lift gauges;
- arbitrary filtered presentations representing the same intrinsic group data;
- possible twisted terms that vanish on the chosen standard branch but survive elsewhere.

## Correct HA61-B target

We must now write the most general secondary obstruction schematically as
[
\delta_3(z)
=
\bigl[
f(t_2)
+
B_{\rho_2}(z)
+
(\mu\wedge f)(R)
+
E_{\ge4}(z)
\bigr]\omega,
]
where (E_{\ge4}) denotes terms whose vanishing/absorption must be justified by an explicit filtration estimate, not by notation.

The attack must then determine, in order:

### B1. Origin
Identify every source of a (\rho_2)-dependent term in the full crossed-word expansion.

### B2. Primary-zero reduction
Impose (\delta_2(f)=0) and determine exactly which old-action terms vanish and which remain.

### B3. Gauge test
Change the (A_2)-lift
[
z\mapsto z+d\phi
]
and compute the change of the candidate (B_{\rho_2}(z)).

### B4. Independence test
Determine whether the surviving expression can be written canonically as (f(s_2)) for some filtered residual (s_2). If yes, it belongs to the (t_2)-sector rather than being an independent (B_{\rho_2}).

### B5. Filtration cutoff
Prove which terms are zero modulo (27) after division by (9), using an explicit degree/filtration bound.

Only after B1-B5 may HA61-B be classified.

## Consequence for HA61-C

HA61-C must NOT yet begin as a theorem-producing step.

The correct order remains:

[
\boxed{
A\;\text{full expansion}
\to
B\;B_{\rho_2}\text{ audit}
\to
C\;t_2\text{ intrinsicity}
\to
D\;n\to n+1.
}
]

The q=3/q=9 agreement is a valuable local constraint inside B, not permission to skip B.

## Research-program consequence

The current project has not lost progress. The correction actually sharpens the load-bearing gate:

[
\text{HA61-B}
=
\text{“is the old coefficient action genuinely new secondary data,
or is it gauge/primary-normalization/t}_2\text{-data?”}
]

That is now the next attack.

## Decision

**HA61-B: OPEN / LOAD-BEARING.**

No all-(n) induction. No claim of intrinsic (t_2) until this gate is settled.
