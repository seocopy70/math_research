# Paper 5 Gate B — Q-layer / p-adic refinement audit (2026-10-09)

## Classification

**Gate B: OPEN / LOAD-BEARING.**

This audit records the correction that separates the valid restricted-Lie quotient work from the invalid attempt to extract p-adic/Teichmuller information from the mod-p quotients (Q_{p^k}).

## 1. General commutator-power lemma

Let (A=\mathbf F_p\langle X,Y\rangle) and (C=[A,A]) be the vector subspace spanned by associative commutators.

For arbitrary (a,b\in A),
[
(ab)^p-(ba)^p
=a(ba)^{p-1}b-(ba)^{p-1}ba
=[a,(ba)^{p-1}b]\in C.
]
Thus ((ab)^p\equiv(ba)^p\pmod C).

For odd prime (p), the noncommutative binomial expansion modulo the additive commutator subspace gives
[
(a+b)^p\equiv a^p+b^p\pmod C,
]
because mixed words occur in cyclic orbits of size (p). Hence
[
(ab-ba)^p
\equiv (ab)^p+(-ba)^p
=(ab)^p-(ba)^p
\equiv0\pmod C.
]
Therefore
[
\boxed{[a,b]^p\in C\qquad(a,b\in A).}
]

The quotient (A/C) is being used only as a vector space of cyclic words; no multiplication on (A/C) is assumed.

**Classification: PASS / LOCAL.** The argument is elementary and uniform in (a,b), but it is a lemma inside the present filtered-Lie construction, not yet an independently packaged theorem.

## 2. Intersection (C\cap L=[L,L])

Let (L=L_{\rm res}(X,Y)\hookrightarrow A). The restricted abelianization (L/[L,L]) has the independent generators
[
X^{[p^k]},quad Y^{[p^k]}qquad(k\ge0).
]
Their images in (A/C) are the distinct cyclic words (X^{p^k}) and (Y^{p^k}), hence are linearly independent. Therefore
[
L/[L,L]\hookrightarrow A/C
]
and
[
\ker(L\to A/C)=C\cap L=[L,L].
]

Combining this with the preceding lemma gives
[
[L,L]^{[p]}\subseteq C\cap L=[L,L],
]
so the ordinary derived ideal is already restricted:
[
\boxed{[L,L]_{\rm res}=[L,L].}
]

The further identification
[
I_n=[L_{n-1},L_1]=J_n
]
is valid only after the degree convention for (L_n) and the ordinary-Lie Hall-word decomposition are stated explicitly. In particular, restricted (p)-powers must not be treated as independent bracket generators before the equality ( [L,L]_{\rm res}=[L,L]) has been used.

**Classification: PASS / LOCAL**, with the Hall-word/degree bookkeeping to be formalized in the manuscript.

## 3. The (Q_{p^k}) obstruction is mod-p only

For
[
Q_{p^k}
=
L_{p^k}/[L_{p^k-1},L_1]
\cong
\mathbf F_pX^{[p^k]}\oplus\mathbf F_pY^{[p^k]},
]
the coefficients are already reduced modulo (p).

Consequently, for any (\tilde\alpha\in\mathbf Z_p),
[
\overline{\tilde\alpha^{p^k}}
=
\overline{\tilde\alpha}
\in\mathbf F_p,
]
and therefore
[
(\tilde\alpha^{p^k}-\tilde\alpha)X^{[p^k]}=0
quad\text{in }Q_{p^k}.
]

Thus (Q_{p^k}) cannot distinguish a general (p)-adic lift from its Teichmuller representative. Vanishing of the (Q_{p^k})-class is only a graded mod-(p) statement and does **not** imply
[
E_{p^k}\in D_{p^k+1}.
]

In particular the implication
[
\tilde\alpha^{p^k}=\tilde\alpha
\Longrightarrow
\text{all graded obstructions vanish}
\Longrightarrow
\text{exact lift}
]
fails at its second arrow unless an additional filtered lifting theorem is supplied.

**Classification: FAIL / CLOSED as stated.**

## 4. Hall–Petresco perturbation lemma survives

For (u=x^{\tilde\alpha}\delta), with (\delta\in D_2), the first (p)-power layer calculation can be made with Hall–Petresco:
[
u^p\equiv (x^{\tilde\alpha})^p\pmod{D_{p+1}},
]
because the cross commutator terms have sufficiently high Zassenhaus weight and (\delta^p\in D_{2p}\subseteq D_{p+1}).

This proves only the disappearance of the (D_2)-perturbation in the first (p)-power layer. It does not provide the all-(k) relation-preservation theorem.

**Classification: PASS / LOCAL.**

## 5. Important correction to the proposed Witt-coordinate argument

Writing
[
\tilde\alpha=[a_0]+p[a_1]+p^2[a_2]+\cdots
]
is a legitimate way to expose (p)-adic coefficient data, but expressions such as
[
(x^{\tilde\alpha})^p
=
x^{p[a_0]^p}x^{p^2[a_1]^p}\cdots
]
cannot be used as a group identity without an independent collection/commutator calculation. The factors do not commute in the pro-(p) group.

More importantly, the proposed map
[
D_{p^k}\cap p^rA\longrightarrow L_{p^k+r}
]
is not yet a well-typed filtered statement: (A=\mathbf F_p\langle X,Y\rangle) has no (p)-adic scalar filtration. The integral object must first be specified, e.g. an appropriate completed (\mathbf Z_p)-Magnus/group-algebra or enveloping-algebra filtration, and the map to the Zassenhaus graded pieces must be proved well-defined and independent of choices.

Therefore the phrase “Witt-coordinate filtered lifting lemma” is currently a **research target**, not an available lemma.

## 6. Correct load-bearing target

The needed theorem is an integral filtered comparison of the form:

- define an integral (p)-adic/Magnus filtration (F^{r}_{\rm int}) on a completed (\mathbf Z_p)-object attached functorially to the free pro-(p) group;
- prove a precise comparison between (D_n)-membership and the joint (p)-adic/augmentation filtration;
- identify the first nonzero integral coefficient of the relation-preservation residual;
- show that vanishing at every restricted (p^k)-layer forces the residual into
[
\bigcap_{k\ge1}D_{p^k+1}=1
]
by pro-(p) completeness.

The theorem must retain the coefficient information lost by (Q_{p^k}). It cannot be obtained by merely iterating the mod-(p) quotients.

## 7. Current Gate B classification

| Claim | Classification |
|---|---|
| degree-2 / degree-(p) separation | PASS / CLOSED |
| ( [a,b]^p\in C) for all (a,b\in A) | PASS / LOCAL |
| (C\cap L=[L,L]) | PASS / LOCAL |
| (I=[L,L]_{\rm res}=[L,L]) | PASS / LOCAL |
| (I_n=J_n) after explicit degree bookkeeping | PASS / LOCAL |
| Hall–Petresco (D_2)-perturbation at first (p)-layer | PASS / LOCAL |
| (Q_{p^k}) detects Teichmuller precision | **FAIL / CLOSED** |
| all-(k) restricted-power formula | OPEN / LOAD-BEARING |
| integral/p-adic filtered lifting lemma | OPEN / LOAD-BEARING |
| exact pro-(p) lift | OPEN / LOAD-BEARING |
| Gate B | **OPEN / LOAD-BEARING** |

## 8. Authorized next action

Do **not** return to BCH, and do **not** continue blind (D_5/D_6/D_{p^k}) computation.

The next mathematical task is to formulate the integral filtered object correctly and prove the smallest comparison lemma that actually retains one (p)-adic coefficient beyond the mod-(p) Zassenhaus quotient. Only after that lemma is independently verified should an all-(k) restricted-power argument be attempted.
