# PAPER 4 — CRITICAL REVIEW OF q>0 BOUNDARY / NEXT-GATE DISCIPLINE — 2026-10-02

## Verdict

The submitted critical review is **substantively correct**, but one phrase must be weakened:

> “integral, gauge-invariant, nonabelian relation data” is the **only remaining candidate**

is too strong if read mathematically exhaustively. It is the **only remaining primary route currently authorized by the research program** after the untwisted E2 and ordinary mod-p graded routes were closed. Twisted/dualizing-coefficient constructions, higher cohomological operations, or other integral nonlinear objects are logically possible, but each is a *new branch* requiring a fresh Object/Input/Gauge/q-blindness pre-check.

## 1. q>0 H_2 correction

For an infinite odd-p Demushkin group with q=p^a>0 and standard relation
r_D=x_1^{p^a}[x_1,x_2]...[x_{d-1},x_d],
the trivial-coefficient one-relator cellular/Fox boundary has exponent-sum vector
(p^a,0,...,0). Hence the relevant map Z_p -> Z_p is multiplication by p^a and is injective, giving H_2(D,Z_p)=0.

For q=0 the exponent-sum vector is zero and H_2(D,Z_p)≅Z_p.

Therefore the q=0 E2 transgression
H_2(D,Z_p) -> (N^{ab})_D
has no nonzero source in the q>0 case. The classification
**untwisted E2 continuation: FAIL / CLOSED**
is justified.

This is a structural closure, not merely a failed computation.

## 2. Untwisted H_1-extension saturation

For the stress presentation
G_{s,a}=<z,x_1,...,x_d | z^{p^s}=r_D>,
abelianization gives p^s z=p^a x_1. In the five-term sequence, because H_2(D,Z_p)=0, the coinvariant module identifies with the H_1-kernel in this stress model. The resulting extension class on the torsion summand lies in
Ext^1_{Z_p}(Z/p^a,Z_p)≅Z/p^a
and is represented by p^s modulo p^a, up to sign/unit convention.

Hence for s>=a the *stress-model untwisted H_1/coinvariant layer* saturates.

Important scope correction:
this is not a theorem that every free-by-Demushkin extension with q=p^a has the same extension class. The proposed G_{s,a} family has not been independently certified as a free-by-Demushkin family for arbitrary s>a. The PASS/LOCAL label must remain local to the stated stress presentation.

## 3. Ordinary mod-p Zassenhaus graded

For the same stress presentation, with odd p and a,s>=1, the initial relation is the degree-2 Demushkin commutator form and is independent of s. The Schmidt/Gärtner mildness criterion can be used at the candidate level to control the associated graded.

Thus:
- initial-form blindness to s: **PASS / CLOSED**;
- ordinary mod-p associated-graded recovery of s: **FAIL / CLOSED** *for the candidate stress model*.

The scope must remain explicit: this is not a certified theorem about an arbitrary free-by-Demushkin family, and it does not imply blindness of the full finite quotient.

The distinction
associated graded blind  !=  finite-window blind
is mandatory and remains intact.

## 4. The strongest correction to the submitted table

The following row should read:

| Item | Classification | Exact scope |
|---|---|---|
| q>0 untwisted E2 source | **FAIL / CLOSED** | H_2(D,Z_p)=0 for standard q=p^a>0 |
| q>0 untwisted H_1-extension | **FAIL / CLOSED** | stress model; saturated for s>=a |
| ordinary mod-p Zassenhaus graded | **FAIL / CLOSED** | stress-model candidate; blind to s |
| integral gauge-invariant nonabelian relation data | **OPEN / LOAD-BEARING** | primary authorized successor |
| twisted/dualizing-coefficient replacement | **OPEN** | separate branch; not E2 continuation |
| full finite-window factorization | **OPEN / LOAD-BEARING** | no theorem yet |
| universal impossibility for q>0 deep tails | **OPEN** | no claim permitted |

## 5. The next gate is definition, not computation

Before computing any Magnus coefficient, define a candidate I_m(G) in one sentence.

Minimum acceptable form:

> I_m(G) is a presentation-independent quotient/truncation of an integral p-adic relation object, with all presentation-basis, relator-generator, lift/section, conjugacy, and unit-scaling gauges explicitly quotiented.

Then specify:

### Object
Exactly which module/ring/filtered relation object is used?

### Input
Does I_m use only G as an abstract/profinite group (or only the declared finite window), or does it secretly use a chosen presentation, D, q, orientation, or lift?

### Functoriality
Which filtered-group isomorphisms induce maps of I_m?

### Gauge
At minimum test:
- free-basis/Nielsen changes;
- relator multiplication by a unit;
- conjugating the relator;
- lift/section changes;
- automorphisms of the quotient D;
- automorphisms of the kernel presentation;
- any BBG-type boundary automorphism relevant to the construction.

### Orientation bridge
There must be a natural map from I_m to the actual target information. Merely recovering p^s is not an orientation theorem.

### q-blindness
The definition may not insert a or q=p^a.

### Separation
It must distinguish the relevant q=0 and q>0 stress regimes without using q as an input label.

### Non-reencoding
A presentation coefficient is not acceptable merely because it numerically equals the desired answer. The same intrinsic finite object must force the value.

## 6. Important methodological boundary

The phrase “integral Magnus/relation data is the only remaining candidate” must therefore be replaced by:

> **The only remaining primary route currently authorized is an intrinsic, gauge-invariant, nonabelian integral relation object strictly richer than the ordinary mod-p associated graded.**

This preserves the research direction without pretending that all other mathematics has been exhausted.

## 7. Novelty boundary

The object itself is standard technology. Any eventual Paper-4 contribution would have to be one of:
1. a new intrinsic quotient/truncation;
2. a proof that it factors through a finite Zassenhaus window;
3. a sharp obstruction showing that no such factorization exists in a declared admissible category;
4. a reconstruction theorem to the target orientation/cohomological datum.

A successful calculation of a Magnus coefficient alone is not a Paper-4 theorem.

## 8. Current Gate

**Gate P4-Q+ / INTEGRAL-NONABELIAN-DEFINITION**

Status: **OPEN / LOAD-BEARING**.

No carrier search, no arbitrary Magnus computation, and no RAAG return are authorized before the exact object and gauge quotient pass pre-check.

