# U1–U5 Proof Audit of `paper/main.tex` — 2026-09-25

## Scope

This audit checks the **actual publication manuscript** `paper/main.tex`, not the research log. The standard is: every load-bearing implication must be stated with hypotheses, coefficient conventions, and a proof sufficient for an external referee to reconstruct the argument.

Repository: `seocopy70/math_research`

Manuscript theorem under audit:
[
\mathsf K_k(Q_k,\rho)\Longleftrightarrow \rho=\chi_G\pmod{3^k},qquad k\ge2,
]
for the fixed rank-four (q=3) Demuškin group.

## Executive result

**The theorem appears mathematically salvageable, but the present `main.tex` is not yet publication-proof-complete.**

The most important finding is positive:

> For the frozen relator (r=x_1^3[x_1,x_2][x_3,x_4]), the twisted Fox calculation can be written directly for arbitrary (k\ge2). This is stronger and cleaner than the current manuscript's "reduce to level 2 + U5 induction" route.

Once U3 is stated with the required (3)-divisibility hypothesis and U4 is expanded, the selector theorem can be proved directly at every (k). U5 then becomes a useful independent cohomological uniqueness lemma, but is **not necessary for the main theorem**.

This is preferable for the paper because it removes the most delicate current induction bookkeeping from the load-bearing theorem proof.

---

# U1 — Semidirect-product filtration

### Manuscript claim

For
[
S_k=A_k\rtimes U_1,quad A_k=\mathbf Z/3^k,
]
and
[
T_j=3^{j-1}A_k\rtimes U_j,
]
the lower (3)-central filtration satisfies
[
P_j(S_k)=T_j,qquad P_{k+1}(S_k)=1.
]

### Audit

**STATUS: PASS, but proof is underwritten.**

The equality is correct for odd (p=3), but the manuscript currently states it without proving the two inclusions.

The proof should explicitly use
[
P_{j+1}(S_k)=P_j(S_k)^3[P_j(S_k),S_k]
]
and verify:
[
(3^{j-1}A_k)^3=3^jA_k,
]
in additive notation, together with
[
[3^{j-1}A_k,U_1]subseteq3^jA_k,
qquad
U_j^3subseteq U_{j+1},
qquad
[U_j,U_1]=1.
]

For the reverse inclusion, the (3)-power term supplies the full (3^jA_k), while (U_j^3=U_{j+1}) for (j<k) (using the odd-prime binomial calculation).

### Required manuscript repair

Add a short induction proving both inclusions, and explicitly state that this is an **odd-(p)** calculation. No (p=2) claim should be inferred.

---

# U2 — Factorization of crossed cocycles through (Q_k)

### Manuscript claim

For a candidate
[
\rho:G\to U_{1,k}
]
and (z\in Z^1(G,A_k(\rho))),
[
g\mapsto(z(g),\rho(g))
]
is a homomorphism (G\to S_k). Therefore (P_{k+1}(G)) is killed and the cocycle factors through
[
Q_k=G/P_{k+1}(G).
]

### Audit

**STATUS: PASS/CLOSED.**

This is the correct argument and is genuinely arbitrary-candidate: it does not assume (\rho=\chi).

Important logical boundary:

[
Z^1(G,A_k(\rho))\to Z^1(Q_k,A_k(\bar\rho))
]
is established.

This does **not** by itself establish
[
H^2(G,A_k(\rho))\cong H^2(Q_k,A_k(\rho)).
]

The manuscript does not currently make that forbidden (H^2)-factorization claim in the main theorem, which is correct. Keep that distinction explicit.

### Required manuscript repair

State that a candidate on (Q_k) is pulled back to (G) before applying the semidirect-product argument, and that only the relevant crossed cocycles are being factored.

---

# U3 — Finite Kummer/Fox criterion

### Manuscript claim

Surjectivity
[
H^1(G,A_k(\rho))\to H^1(G,\mathbf F_3)
]
is equivalent to the ability to lift every prescribed mod-(3) generator-value vector through
[
z(r)=\sum_i
\left.\frac{\partial r}{\partial x_i}\right|_\rho z(x_i)=0.
]

### Audit

**STATUS: PASS after a necessary correction.**

The equivalence itself is correct for a one-relator presentation, provided the coefficient convention is fixed and the principal-unit hypothesis is stated.

The current phrase

> "The proof is a finite Nakayama iteration over (A_k)"

is too compressed. It is only valid after observing that all twisted Fox coefficients are divisible by (3).

For the present relator and principal-unit candidate,
[
\rho(x_i)\equiv1\pmod3,
]
so every evaluated Fox coefficient is indeed (0pmod3).

A clean lemma should be inserted:

**Finite lifting lemma.** If (D=(D_1,\dots,D_n)\in(3A_k)^n), then
[
\ker(D:A_k^n\to A_k)\to(\mathbf F_3)^n
]
is surjective iff (D=0).

Proof: lift the standard basis vectors and successively divide the relation by (3,3^2,\ldots,3^{k-1}). At each stage the other coordinates are divisible by (3), so the chosen coefficient must vanish modulo the next power of (3).

This converts the Kummer predicate into the exact vanishing of the twisted Fox row.

### Important correction

Do **not** present this as a generic Nakayama argument for arbitrary relators without the (D_i\in3A_k) hypothesis.

---

# U4 — Standard-presentation twisted Fox calculation

### Current manuscript

The manuscript currently says:

> "the standard odd-(p) Demuškin calculation gives ..."
[
\rho(x_1)=\rho(x_3)=\rho(x_4)=1,qquad
\rho(x_2)=(1-3)^{-1}.
]

### Audit

**STATUS: CURRENTLY INCOMPLETE; DIRECT ALL-(k) REPAIR AVAILABLE.**

This is the most important proof-completeness gap in the present manuscript.

The calculation should not be cited merely as a "standard calculation", because this exact arbitrary-candidate selector is the load-bearing local step.

Let
[
a=\rho(x_1),quad b=\rho(x_2),quad
c=\rho(x_3),quad d=\rho(x_4).
]
Since (\rho(r)=1),
[
a^3=1.
]

With the stated Fox convention
[
[a,b]=a^{-1}b^{-1}ab,
]
the evaluated twisted Fox coefficients are
[
D_1=1+a+a^2b^{-1},
]
[
D_2=b^{-1}(a-1),
]
[
D_3=c^{-1}(d^{-1}-1),
]
[
D_4=d^{-1}(c-1).
]

All (D_i\in3A_k) because (a,b,c,d\equiv1pmod3).

By U3,
[
\mathsf K_k(Q_k,\rho)
\Longleftrightarrow
D_1=D_2=D_3=D_4=0.
]

Then:
[
D_2=0\Rightarrow a=1,
]
[
D_3=0\Rightarrow d=1,
]
[
D_4=0\Rightarrow c=1,
]
and therefore
[
D_1=2+b^{-1}=0.
]
Hence
[
b=-\frac12=(1-3)^{-1}\pmod{3^k}.
]

Thus the arbitrary candidate is uniquely
[
\rho=(1,(1-3)^{-1},1,1)=\chi_G\pmod{3^k}.
]

### Consequence

This is an **all-(k)** calculation. It removes the need to establish U4 only at (k=2) and then invoke U5 for the higher digits.

The numerical checks
[
4\pmod9,qquad13\pmod{27},qquad40\pmod{81}
]
are useful sanity checks but should be presented after the symbolic calculation, not as its proof.

---

# U5 — Variation formula and PD² uniqueness

## U5a — coefficient-extension variation

### Current manuscript claim

If
[
\rho_k'=\rho_k(1+3^{k-1}\nu),
]
then
[
\delta_{\rho_k'}-\delta_{\rho_k}
=
\iota\circ(\nu\smile-).
]

### Audit

**STATUS: MATHEMATICALLY PLAUSIBLE / PROOF INCOMPLETE IN CURRENT MANUSCRIPT.**

The formula is the right one, but the paper currently states it without fixing enough coefficient-map conventions.

The revised proof must specify:

1. the two coefficient modules;
2. the common kernel (A_{k-1}(\rho_{k-1}));
3. the embedding (\iota:A_{k-1}\hookrightarrow A_k);
4. the identification of the difference between the two coefficient actions with the (1)-cocycle (\nu);
5. the cochain-level calculation producing the cup product.

Without these conventions, the formula is not referee-complete.

---

# U5b — PD² socle injectivity

### Current manuscript claim

On the canonical branch,
[
H^2(G,\mathbf F_3)
\to
H^2(G,A_{k-1}(\chi))
]
is injective because its dual is the surjective reduction map on (H^0).

### Audit

**STATUS: CORRECT IDEA; NEEDS FULL COEFFICIENT-DUAL STATEMENT.**

For a Demuškin group with dualizing character (\chi), finite-coefficient PD² duality gives the relevant duality between (H^2(G,M)) and (H^0(G,M^*\otimes D)).

For
[
M=A_{k-1}(\chi),
]
the dual-twisted coefficient module reduces to the trivial (A_{k-1})-module. The induced map on (H^0) is
[
A_{k-1}\to\mathbf F_3,
]
which is surjective. Hence the dual (H^2)-map is injective.

The manuscript needs to state this coefficient convention explicitly rather than compressing it to "its dual is the surjective reduction map".

---

# U5c — Intrinsic uniqueness

### Audit

**STATUS: VALID conditional on U5a/U5b.**

If both connecting maps vanish, the variation identity gives
[
\iota(\nu\smile v)=0.
]
U5b then gives
[
\nu\smile v=0
]
for all (v\in H^1(G,\mathbf F_3)). Demuškin cup-product nondegeneracy gives
[
\nu=0.
]

The logic is sound once the preceding coefficient bookkeeping is supplied.

### But:

For the **current fixed rank-four (q=3) theorem**, U5 is no longer needed if U4 is upgraded to the direct all-(k) arbitrary-candidate calculation above.

That is a significant manuscript improvement: U5 can be retained as an independent cohomological uniqueness mechanism, but should not carry the main induction unless there is a separate reason to prefer it.

---

# Final proof architecture recommended after audit

The cleanest publication proof is:

1. **U1:** prove (P_{k+1}(S_k)=1).
2. **U2:** conclude arbitrary twisted cocycles factor through (Q_k).
3. **U3:** prove the finite lifting/Fox-row equivalence, including the (3A_k) lemma.
4. **U4:** compute the four twisted Fox coefficients for an arbitrary principal-unit candidate and solve them for every (k\ge2).
5. **Theorem:** conclude the finite-window recognition equivalence directly.
6. **U5:** retain as an independent intrinsic/cohomological uniqueness lemma or appendix-level strengthening, but do not make the main theorem depend on an unnecessary level-by-level induction.

This is logically shorter and stronger than the present "base (k=2) + U5 induction" route.

## Publication status after this audit

- U1: **PASS — needs proof expansion**
- U2: **PASS / CLOSED**
- U3: **PASS — needs precise lifting lemma**
- U4: **OPEN in manuscript / repair identified and apparently closes all (k\ge2) directly**
- U5a: **OPEN in manuscript — proof expansion required**
- U5b: **OPEN in manuscript — coefficient-duality expansion required**
- U5c: **PASS conditional on U5a/U5b**
- Main theorem: **not yet publication-proof-complete, but a shorter direct proof route is available**
- Novelty: remains **OPEN / CONDITIONAL** and is separate from this proof audit
- Minimality: remains **OPEN**

## Hard boundaries retained

- Fixed rank-four (q=3) theorem only.
- No claim of uniformity over all Demuškin parameters.
- (Q_k=G/P_{k+1}) is a sufficient finite window, not claimed minimal.
- No (H^2(G,A_k)\cong H^2(Q_k,A_k)) claim.
- Canonical orientation and global Kummerianity remain prior art.
- Publication novelty is not inferred from the proof audit.
