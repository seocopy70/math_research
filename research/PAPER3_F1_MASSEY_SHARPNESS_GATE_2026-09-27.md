# Paper 3 — F1 Massey Sharpness Gate (2026-09-27)

## Status

**ACTIVE / LOAD-BEARING BRANCH — M-GATE**

This record supersedes the earlier informal proposal that treated “Demuškin triple-Massey vanishing” itself as a useful target. The fixed Demuškin category is not an adequate nontrivial target category for that formulation.

The new target is the Blumer–Quadrelli family F1 and the sharpness of their explicit sufficient bound for strong Massey vanishing.

## 1. Source verification

The local source archive arXiv-2603.15464v2 (Blumer–Quadrelli, Variations of Demushkin Groups that are not Absolute Galois Groups) was independently unpacked and inspected.

The source states Proposition (2.a):

If G is in F1 and n <= q, then G satisfies a strong variant of the n-fold Massey vanishing property.

The same source separately states, in Example 2(a), that an ordinary Demuškin group satisfies strong n-fold Massey vanishing for every n >= 3, citing Pál–Szabó, Theorem 3.5.

Citation correction: the earlier attribution of this strong all-n Demuškin vanishing statement to Mináč–Tân was incorrect. Blumer–Quadrelli cite A. Pál and E. Szabó, The strong Massey vanishing conjecture for fields with virtual cohomological dimension at most 1, arXiv:1811.06192 (2020), Theorem 3.5.

## 2. Verified structural data of F1

For G in F1, the associated graded restricted Lie algebra is explicitly presented as

gr G = <X1,Y1,...,Xd,Yd | [X2,Y2]+...+[Xd,Yd]=0>.

Thus the leading graded relation omits X1,Y1; the x1^q contribution occurs at a later Zassenhaus depth. This is directly compatible with the Paper 1/2 toolkit: Zassenhaus filtration, initial forms, Magnus/Fox expansions, and mildness.

## 3. Logical boundary

The earlier target “triple Massey vanishing” inside the ordinary fixed-rank Demuškin category is INVALID / CLOSED as a recognition target, because all Demuškin groups satisfy the relevant strong Massey vanishing for every n >= 3. There is no target separation inside that category.

By contrast, Blumer–Quadrelli’s F1 contains non-1-cyclotomic Demuškin-like variations for which Proposition (2.a) gives a parameter-dependent sufficient bound:

n <= q  ==>  strong n-fold Massey vanishing.

The paper does NOT prove the converse:

n > q  ==>  strong n-fold Massey vanishing fails.

Therefore sharpness of the bound is an unresolved question in the source, subject to the mandatory post-publication literature audit.

## 4. Paper 3 translation

Candidate target:

T_n(G) = the strong n-fold Massey-vanishing property,

on an explicitly declared category containing F1.

The first load-bearing question is:

Is the bound n <= q sharp for F1?

Only after that should the finite-window recognition threshold be formulated precisely:

r_Tn(C;D) = min{m : W_m(G) isomorphic to W_m(H) implies T_n(G) isomorphic to T_n(H) for all G,H in C}.

This must not be confused with the already-known sufficient bound n <= q.

## 5. Required M-Gate

M0 — Category:
Fix the exact category. First candidate C = F1, or a minimally enlarged class if separation requires it.
Status: OPEN.

M1 — Target nontriviality / sharpness:
Determine whether the strong n-fold Massey property actually changes across n=q. The smallest stress test is d=2, q=p, n=p+1.
Status: OPEN / LOAD-BEARING.

M2 — Prior-art depth audit:
Search post-Blumer–Quadrelli literature and the relevant Pál–Szabó / Pál–Quick / Massey literature for an existing converse, sharpness theorem, or explicit n>q obstruction.
Status: OPEN / MANDATORY BEFORE COMPUTATION.

M3 — Finite-window recognition:
If M1 passes, determine the smallest Zassenhaus window at which the target is recognized/separated.
Status: NOT AUTHORIZED YET.

M4 — Generalization:
Test whether the resulting formula depends uniformly on p,d,q,n and whether the mechanism extends to F2, free products, or a wider mild multi-relator class.
Status: DEFERRED.

## 6. Generalization test

The branch is promoted only if the eventual answer is more than a one-off calculation. Ideally it should yield a theorem of the form threshold = F(p,d,q,n), or an equally clean structural criterion, with a mechanism that survives at least one enlargement of the category.

A single computation at (d,q,n)=(2,p,p+1) is evidence only; it is not by itself a Paper 3 theorem.

## 7. Relationship to the ultimate Paper 3 program

This branch is potentially relevant to the broader goal of finite filtered information recognizing a global cohomological/structural target.

No claim is yet made that it realizes the full unified-detector program. That remains OPEN / CONDITIONAL.

Safe current statement: Blumer–Quadrelli supplies a published, parameter-dependent sufficient Massey-vanishing bound in a Demuškin-like non-1-cyclotomic family. Determining whether that bound is sharp, and then identifying the finite Zassenhaus information required to recognize the corresponding Massey target, is a concrete candidate for the Paper 3 recognition-threshold program.

## 8. Mandatory pre-computation audit

Before substantial computation:

1. Object — exact strong Massey target.
2. Input — exact Zassenhaus window and allowed data.
3. Functoriality — target/window invariant under declared isomorphisms.
4. Gauge — presentation choices and defining-system ambiguity controlled.
5. Orientation bridge — exact map from finite filtered data to the Massey obstruction.
6. q-blindness — do not insert q by hand if q-independent recognition is claimed.
7. Separation — produce an actual pair/family with different target values.
8. Novelty — compare against the source proposition and later citations.
9. Stop — if any of 1–5 is unjustified, do not compute.

## 9. Classification

- Fixed Demuškin triple-Massey target: FAIL / CLOSED.
- F1 sufficient bound n <= q: PASS / CLOSED as a verified literature fact.
- Sharpness of n <= q: OPEN / LOAD-BEARING.
- Post-Blumer–Quadrelli converse/prior-art audit: OPEN / MANDATORY.
- Finite Zassenhaus recognition threshold: OPEN / NOT YET AUTHORIZED.
- General (p,d,q,n) threshold theorem: OPEN / CONDITIONAL.
- Broader Paper 3 ultimate generalization: OPEN / CONDITIONAL.

## 10. Immediate next action

Do not start the d=2, q=p, n=p+1 Massey calculation yet.

First perform M2. The exact question is:

Has any work after Blumer–Quadrelli, or any cited/related work they rely on, already proved that the bound n <= q in Proposition (2.a) is sharp, or exhibited strong n-fold Massey vanishing/failure for n > q in F1?

Only if the answer is negative should the small-case computation be authorized.
