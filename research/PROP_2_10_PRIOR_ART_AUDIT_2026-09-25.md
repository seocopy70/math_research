# PROP. 2.10 — PRIOR-ART AUDIT OF THE RESTRICTION-SURJECTIVITY NEGATIVE RESULT — 2026-09-25

## Target negative result

For the rank-4, p=3 Demushkin group and the specific choice N=P_3(G), the restriction map
H^1(G,F_3) -> H^1(P_3,F_3)^G
appearing as a hypothesis in Quadrelli (2024), Proposition 2.10, is not surjective.

The current proof uses:
1. P_3(G) subset Phi(G), so the dual inclusion P_3/P_3^3[P_3,G] -> G/Phi(G) is zero;
2. P_3/P_4 != 0, with dim_F3(P_3/P_4)=20;
3. P_3^3[P_3,G] subset P_4;
therefore the source P_3/P_3^3[P_3,G] is nonzero, so the dual map is not injective and restriction is not surjective.

Only the k=2 instance is claimed here.

## Primary prior-art source: Quadrelli 2024, Proposition 2.10

Quadrelli, *Chasing Maximal Pro-p Galois Groups via 1-Cyclotomicity*, Mediterr. J. Math. 21 (2024), Prop. 2.10, states that if (G,theta) is already Kummerian, N is normal with N subset Ker(theta), and
H^1(G,F_p) -> H^1(N,F_p)^G
is surjective, then (G/N,theta_/N) is Kummerian.

The proof explicitly identifies the dual condition as injectivity of
N/N^p[G,N] -> G/Phi(G), and then chooses generators adapted to N.

This source therefore confirms that the restriction-surjectivity hypothesis is a genuine additional hypothesis, not a formal consequence of N subset Ker(theta).

## Exact comparison

The present negative result is NOT a contradiction, correction, or counterexample to Proposition 2.10.

It shows that for N=P_3 in the present Demushkin setting, the sufficient hypothesis of Proposition 2.10 fails. Hence Prop. 2.10 cannot be invoked automatically to obtain the desired finite-window result by taking N=P_{k+1}.

The logical distinction is:

- Prop. 2.10: Kummerianity of (G,theta) + restriction-surjectivity => Kummerianity of the quotient.
- Present result: for N=P_3, restriction-surjectivity itself fails.
- Present finite-window theorem: factorization/recognition is proved directly for arbitrary finite candidate rho, without using Prop. 2.10.

## Prior art for the graded-dimension input

The nonvanishing P_3/P_4 is standard Zassenhaus-filtration information. Mináč–Rogelstad–Tân, *How fast do Zassenhaus filtrations of pro-p-groups descend?* (arXiv:1405.6980 / 2014), gives explicit graded dimensions for Demushkin groups. For rank d and p=3,
c_3=(d^3-4d)/3,
so d=4 gives c_3=20.

Thus the numerical fact dim_F3(P_3/P_4)=20 is not new.

The inclusions P_3 subset Phi(G) and P_3^3[P_3,G] subset P_4 are standard filtration/Frattini facts and are not claimed as new.

## Search result on the exact composite statement

Targeted searches for:
- H^1(G,F_3) -> H^1(P_3,F_3)^G for Demushkin groups;
- P_3/P_4 = 20 together with Demushkin/Kummerian restriction;
- P_{k+1} and Kummerian quotient inheritance;
- restriction-surjectivity for P_{k+1};
did not locate a source stating this exact application or identifying it as an existing obstruction.

Broader searches did locate the individual ingredients and the general quotient-inheritance theorem, but not the exact composite negative statement.

Therefore the correct novelty classification is NOT "new theorem" and NOT "known theorem". It is:

**PASS / CONDITIONAL as a prior-art separation lemma:** the exact composite application appears not to have been explicitly stated in the audited corpus, while all ingredients are classical/known.

## Logical role in the paper

This result should be used modestly:

> Proposition 2.10 does not automatically collapse our finite-window construction, because its restriction-surjectivity hypothesis fails already for N=P_3 in the rank-4 p=3 Demushkin case.

It should NOT be advertised as a new structural theorem about restriction maps in general.

Its value is prior-art separation: it closes one concrete route by which the finite-window factorization might have been an immediate corollary of known quotient inheritance.

## References checked

1. Quadrelli (2024), Proposition 2.10 and its proof.
2. Labute (1967), *Classification of Demushkin Groups*, for the Demushkin classification/canonical orientation background.
3. Mináč–Rogelstad–Tân (2014), Zassenhaus graded dimensions for Demushkin groups.
4. Quadrelli–Weigel (2022), Kummerian/Bogomolov–Positselski structural equivalences.
5. Efrat–Quadrelli (2019), Kummerian pro-p pairs and quotient/cohomological characterizations.
6. Blumer–Quadrelli (2026), arXiv:2603.15464v2: variations of Demushkin groups / 1-cyclotomic obstructions.
7. Pál–Quick (2026), arXiv:2601.07551v2 and arXiv:2607.01028v2: A_3-formality of Demushkin groups; no exact Prop. 2.10/P_3 restriction application found.

## Decision

- Exact negative statement already known verbatim: **NOT FOUND**
- Mathematical ingredients: **KNOWN**
- Proposition 2.10 applicability to N=P_3: **FAIL / CLOSED**
- Prior-art separation value: **PASS / CONDITIONAL**
- Independent novelty of this lemma alone: **DO NOT CLAIM**
