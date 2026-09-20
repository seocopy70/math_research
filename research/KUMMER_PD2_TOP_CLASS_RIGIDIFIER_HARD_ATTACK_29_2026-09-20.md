# KUMMER PD2 TOP-CLASS RIGIDIFIER HARD ATTACK 29 — 2026-09-20

## 1. The obvious missing rigidifier

Hard Attack 28 isolated the missing datum as a distinguished 2-cell evaluation. A natural next idea is to use the top cohomology of the open subgroup N=P_{k+1}(G).

For a Demushkin/PD^2 pro-3 group, an open subgroup is again PD^2. Its top cohomology with F_3 coefficients is one-dimensional, and conjugation by G/N acts through the restricted orientation character. Thus the Q_k-module H^2(N,F_3) is already an orientation-bearing object.

## 2. Hard attack: this does not solve the filtered-carrier problem

If one adds H^2(N,F_3) as a Q_k-module to the finite carrier, the desired orientation mod 3 is recovered directly from the Q_k-action.

But this is not a new q-blind extension-theoretic reconstruction. It imports precisely the duality/top-class representation whose Q-action is the orientation character.

At higher precision the same issue persists: replacing F_3 by Z/3^k gives a top-class module whose Q-action is the desired character modulo 3^k. Adding it as input is therefore equivalent in information content to adding the target orientation itself.

Hence:

finite filtered extension data + top-class action
is an orientation-bearing carrier, not an independently derived orientation bridge.

## 3. Why this attack matters

This closes the most obvious escape from Hard Attacks 27–28:

- adding more kernel abelianization does not give the 2-cell evaluation automatically;
- adding the top cohomology module gives the evaluation, but only because it already contains the orientation action.

So the missing structure is now sharply localized:

[
oxed{
	ext{filtered extension data}
;
otsupseteq;
	ext{known top-class action by any automatic formal implication}.
}
]

A successful non-circular construction must manufacture the top-class/2-cell action from a lower-level filtered relation invariant rather than append it.

## 4. Remaining legitimate possibility

There is still one mathematically meaningful route:

construct a finite chain-level/extension-level object T_k from (Q_k,M_k,E_k) whose canonical cohomological evaluation, after proving an independent PD^2 identity, is identified with the top-class action.

The identity must be proved from the filtered object itself. It may not use the known formula for chi, the dualizing module action, or the Demushkin classification as an intermediate reconstruction.

This is stronger than merely computing H^2 after the fact.

## 5. Decision

- top-class module as an intrinsic group object: PASS / LOCAL;
- using its Q-action to recover orientation: PASS / LOCAL but tautological for the present carrier objective;
- top-class module as a new non-tautological filtered carrier: FAIL / CLOSED;
- chain-level T_k producing the top-class action independently: OPEN / decisive;
- universal impossibility of such T_k: OPEN (not proved).

## 6. Current research boundary

The project has now exhausted the obvious hierarchy

Q_k
 -> finite kernel extension M_k
 -> canonical extension class e_k
 -> top cohomology of the deep kernel.

At each step either the desired 2-cell information is absent, or adding it directly imports orientation.

The next attack must therefore be genuinely constructive: derive a finite 2-cell invariant from the extension itself, or prove a separation/counterexample showing that no such invariant can exist in the declared admissible category.

No further enlargement by already-oriented cohomology objects is authorized.
