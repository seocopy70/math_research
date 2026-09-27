# Paper 3 — M2 Post-Blumer–Quadrelli F1 Sharpness Literature Audit (2026-09-27)

## Status

**PASS / CLOSED — prior-art gate, with the normal limitation that literature searches establish an audited negative rather than an absolute proof of nonexistence.**

This audit closes the mandatory M2 gate for the F1 sharpness branch. The exact question was whether work after Blumer–Quadrelli, or the literature they rely on, already proves that the F1 bound n <= q is sharp, or gives an explicit F1 obstruction/failure for some n > q.

## 1. Blumer–Quadrelli baseline

The authoritative repository audit of arXiv:2603.15464v2 verifies Proposition (2.a): for G in F1, the strong n-fold Massey vanishing property holds when n <= q. The source does not prove the converse n > q => failure.

The F1 branch therefore remains a genuine sharpness question rather than a restatement of the published proposition.

## 2. New post-publication paper checked

Marina Palaisti, arXiv:2609.00253, submitted 31 August 2026, is explicitly about the two-relator family F2, obtained by adding the commuting relator [z1,z2]=1 to the Demuškin-type relation. Its introduction states this family and identifies Blumer–Quadrelli Question 5.13 as the motivating all-length question.

The paper develops support-block profiles and a one-relator reduction. Its five-fold theorem proves vanishing for the full-interior-support case and reduces the remaining five-fold support types; it does not study the F1 one-relator family or prove sharpness of the F1 bound n <= q.

## 3. Targeted web search

Searches on 2026-09-27 covered:
- arXiv for 2609.00253, F1/F2 Demuškin Massey sharpness, and post-Blumer–Quadrelli work;
- exact combinations involving F1, n > q, Massey, and Demuškin;
- the Blumer–Quadrelli paper and related Massey literature.

No source was found that states an F1 converse/sharpness theorem, or an explicit strong Massey-vanishing failure for an F1 group at n > q.

This is an audited negative result, not a claim that no unpublished or unindexed work can exist.

## 4. Structural transfer from F2

Palaisti's F2 paper is relevant methodologically, not as an F1 answer.

The added commuting relator supplies a second central defect in Dwyer's lifting problem. Once that defect is made exact, the paper's one-relator reduction removes the remaining Demuškin defect by an endpoint correction. The paper explicitly notes that the correction preserves the power term x1^q for every parameter allowed in F2.

This supports the following conditional structural interpretation:
- the F2 mechanism has an additional relation/defect that can be eliminated before treating the Demuškin defect;
- F1 lacks that extra relation;
- therefore one should not assume the F2 all-length reduction transfers to F1;
- the F1 breakpoint at n=q+1 in the elementary U_(n+1) centrality argument remains a genuine F1-specific candidate boundary.

This is evidence about mechanism, not a proof of F1 sharpness.

## 5. Interaction with the hand calculation

The separate hand audit established:
A^q is central in U_(n+1) for n <= q,
while for n=q+1, the standard Jordan block gives A^q=I+N^q with support on the q-th superdiagonal, which is not central in U_(q+2).

Thus:
- proof-mechanism breakpoint at n=q+1: PASS / CLOSED;
- actual F1 Massey-vanishing failure at n=q+1: OPEN.

The literature audit does not change that logical separation.

## 6. M2 classification and next gate

**M2 post-Blumer–Quadrelli prior-art audit: PASS / CLOSED.**

Consequently the continuity protocol now authorizes the smallest computational stress test:
(p,q,d,n)=(3,3,2,4), i.e. U_5(F_3).

The next gate is still M1, not M3:
- construct/characterize admissible (alpha_1,...,alpha_4) with all entries nonzero and the required adjacent cup-vanishing;
- determine whether there exists an admissible Dwyer lift with the required Demuškin relator condition;
- independently verify the result.

A single counterexample would establish local sharpness at (p,q,n)=(3,3,4), but would not by itself prove a uniform theorem in p,d,q,n.

## 7. No reopening

No closed Paper 1/2 branch is reopened. The F2 literature is imported only as a methodological comparison and a warning not to transfer a two-relator cancellation argument to the one-relator F1 family without proof.
