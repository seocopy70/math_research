# PAPER 3 RESEARCH PROGRAM — FINITE-WINDOW RECOGNITION THRESHOLDS

Date: 2026-09-27
Status: ACTIVE / NEW RESEARCH PROGRAM
Publication status of former Paper 3 corpus: CLOSED as an independent paper; absorbed into Paper 2.

## 0. Research-program decision

Paper 1 and Paper 2 are now treated as **closed/frozen research stages** for purposes of this program. Their publication manuscripts and completed results remain preserved and are not to be reopened merely to generate further variants.

The next active research program is **Paper 3** in the new sense: a genuinely new paper built around finite-window recognition thresholds.

Important naming rule:
- "former Paper 3" = the 2026-09-26 free-product/application manuscript, already absorbed into Paper 2.
- "Paper 3" from this document onward = the new finite-window recognition-threshold research program.

## 1. Why Paper 3 exists

The first two papers established two different pieces of the same phenomenon.

- Paper 1 established that finite filtered/relation information can, in suitable settings, recover a global invariant.
- Paper 2 established a sharp finite-window factorization depth in the affine/Kummer setting:
  n_aff(k) = p^(k-1)+1,
  together with sharpness and the relevant information-loss boundaries.

The natural next question is not another application of those theorems. It is:

> Can the amount of finite filtered information required to recognize a global target itself be made into a mathematical invariant, and can its behavior be studied systematically across targets, categories, and filtrations?

This is the conceptual reason for Paper 3.

## 2. Ultimate research goal

The long-term goal is to move from the present family-specific results to a general theory of **finite filtered observation and global invariant recognition**.

The ultimate object is a framework of the form

    finite filtered observation
            |
            v
       information loss
            |
            v
       factorization
            |
            v
       recognition of T
            |
            v
     sharp recognition depth

The eventual ambition is a general theorem (or a sharp obstruction/counterexample theory) describing when a global invariant T of a filtered pro-p object is determined by a finite window, how much information is necessary, and which structural features of T, the category, and the filtration control that threshold.

Paper 3 is explicitly recorded as the **most natural first step toward that ultimate goal**, not as the ultimate general theorem itself.

## 3. Core definitions

Let C be an admissible category/class of filtered pro-p groups and D_bullet a natural filtration.

Define the n-window observation by

    W_n(G) := (G/D_n(G), D_1/D_n, ..., D_{n-1}/D_n)

and

    G ~_n H  iff  W_n(G) is isomorphic to W_n(H)

with the precise morphism/marking structure fixed by the declared category.

For a global target T, define the category-relative recognition threshold

    r_T(C;D_bullet)
      := min { n : G ~_n H => T(G) isomorphic to T(H)
                for all G,H in C },

with r_T = infinity when no such n exists.

This definition is deliberately category-level. A threshold attached to one fixed G is not meaningful because T(G) is then already fixed.

## 4. Factorization threshold versus recognition threshold

Keep two notions separate.

Factorization threshold:

    f_O(k) := minimum n such that the observation O_k
              factors through G/P_n(G).

Paper 2 already proves, in the stated affine crossed-cocycle category,

    f_aff(k) = p^(k-1)+1.

Recognition threshold:

    r_T(C;D_bullet)

asks whether the n-window itself determines the target T across the whole admissible class.

Do NOT identify f_O with r_T without a separate proof.

A central early question is whether there are examples with

    f_O > r_T

or

    f_O = r_T

for structural reasons.

## 5. First research gates

### N0 — Definition
Freeze the category-level definition of r_T and the exact window object W_n.

Target: PASS/CLOSED.

### N1 — Basic threshold theory
Prove the basic structural facts:
1. well-definedness;
2. monotonicity in n;
3. separation lower bound;
4. target-factorization monotonicity;
5. joint-target behavior, with the exact hypotheses stated.

Target: PASS/CLOSED.

### N2 — Paper 2 bridge
Re-express the known affine result as a benchmark:
    f_aff(k)=p^(k-1)+1.

Determine exactly what it implies, and does not imply, about
    r_{chi mod p^k}(C;D_bullet).

Do not claim a new theorem merely by changing notation.

### N3 — First genuinely new target
Select the smallest target for which existing Paper 1/2 results do not already settle r_T.

Priority order:
1. a cohomological/extension target naturally visible from the finite filtered object;
2. a secondary orientation/obstruction datum not equivalent to the already-closed affine target;
3. only then broader target families.

The selection must pass a prior-art/non-redundancy check before large computation.

### N4 — Separation examples
Search for pairs G,H with identical n-windows but different T, giving rigorous lower bounds for r_T.

The lower-bound construction is part of the theorem, not an afterthought.

### N5 — Category and filtration comparison
Only after a nontrivial target is established:
- vary the admissible category C;
- compare Zassenhaus with lower p-central filtration;
- record exactly which conclusions are category-relative.

## 6. Candidate first targets

Potential targets include:
- chi mod p^k, only as a benchmark and bridge to Paper 2;
- selected cup-product/cohomological data;
- selected central extension classes;
- higher/Bockstein-type obstruction data;
- affine structure versus a strictly weaker/stronger target.

The first target must be chosen by novelty and tractability, not by convenience alone.

## 7. Non-negotiable logical boundaries

- Do not claim discovery of the canonical Demushkin orientation; that is classical/closed.
- Do not claim absolute carrier minimality without an admissible category.
- Do not confuse abstract quotient isomorphism with marked/functorial finite-window data.
- Do not turn a factorization statement into a recognition theorem without proving the bridge.
- Do not infer a general threshold law from the existing affine formula alone.
- Do not reopen closed Fox/t2/Q3/Q9 branches unless a new result requires a genuinely different question.
- Computation is validation/evidence; it is not itself a theorem.
- Every new target must undergo prior-art and redundancy audit before being promoted to a paper claim.

## 8. Execution order

1. Freeze N0/N1 definitions and proofs.
2. Use Paper 2 only as the benchmark/bridge, not as the novelty claim.
3. Perform a candidate-target novelty screen.
4. Select one first target.
5. Prove the first upper/lower threshold bounds.
6. Build the first nontrivial recognition example.
7. Only then generalize across categories or filtrations.

## 9. Ultimate-goal statement

The program should preserve this exact conceptual hierarchy:

Paper 1:
    finite-window information can recover a global invariant.

Paper 2:
    in a concrete affine/Kummer setting, the necessary factorization depth can be made sharp.

Paper 3:
    turn "how much finite information is needed to recognize T?" into a category-relative mathematical object and begin its general theory.

Ultimate goal:
    develop a general theory of finite-window recognition thresholds for filtered algebraic objects, identifying structural conditions for finite recognizability, sharp thresholds, and information-theoretic obstructions.

Paper 3 is therefore recorded as the **natural first step toward the ultimate generalization**, not as an arbitrary new branch.
