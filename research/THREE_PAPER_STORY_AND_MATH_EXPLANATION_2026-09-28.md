# Three Papers as One Story: Infinite Maze → Finite Map → Direction Recognition
## 2026-09-28

## Purpose

This document records a two-layer explanation of the mathematical contribution of Paper 1, Paper 2, and Paper 3.

The first layer is a continuous story using the metaphor of an infinite maze, finite maps, and a genuine direction signpost. The second layer translates every major metaphor back into the mathematical objects and statements. The purpose is pedagogical: first understand the architecture without technical vocabulary, then learn the mathematics by translating the already-understood story.

This document is explanatory. The authoritative theorem, proof, audit, and publication-status records remain the dedicated research and manuscript files.

---

# Part I. The complete story, without requiring the mathematics

Imagine an infinite maze.

It never ends. New corridors and junctions keep appearing, and nobody can inspect the whole maze at once.

Somewhere in this maze there is a genuine direction signpost: a piece of information that tells us the real direction toward the treasure. But there are also many candidate signposts. Some are false.

The problem is therefore:

> Can we identify the genuine direction without exploring the entire infinite maze?

The explorers decide to cut out a finite map.

But immediately there is a problem. If the map is too shallow, important information may have been cut away. Different signposts may then look identical.

So the research naturally breaks into three questions.

## Paper 1 — Can a finite map recognize the genuine direction?

The first expedition discovers a remarkable principle:

> Even though the maze is infinite, an appropriately chosen finite map can contain enough information for a test that distinguishes the genuine direction from false candidates.

The crucial point is that the test does not begin by being handed the answer.

A candidate signpost can be presented to the test, and the test determines whether it survives.

Thus the first paper establishes the basic possibility:

> A finite piece of the infinite maze can support an intrinsic recognition mechanism for the global direction information.

## Paper 2 — How deep must the map be?

The second expedition asks a more precise question.

It is not enough to say “make the map sufficiently large.”

We want the exact depth at which all information needed by the relevant affine tests has been preserved.

Too shallow:

> some necessary information disappears.

Deep enough:

> every relevant affine crossed-cocycle test is already determined by the finite map.

The result is an exact depth threshold

\[
n_{\mathrm{aff}}(k)=p^{k-1}+1.
\]

So Paper 2 supplies the map-making rule.

It tells us how far into the infinite maze we have to cut before the relevant information is guaranteed to survive.

It also establishes sharpness in the declared affine crossed-cocycle category: in that category, a generally smaller depth cannot replace the stated bound.

## Paper 3 — Use that map to find the genuine signpost

Now the third expedition takes the finite map supplied by the previous work and actually runs the Kummer test on it.

We take an arbitrary candidate direction signpost \(\rho\).

The finite map carries enough information to perform the test, and the test is intrinsic: it does not need to be fed the original presentation as part of the selector.

False candidates fail.

The genuine candidate survives.

For the declared Demuškin scope, the result is

\[
\mathsf K_k(Q_k,\rho)
\iff
\rho=\chi_G\pmod{p^k},
\]

and in particular for the fixed rank-four \(p=3\) setting,

\[
Q_k=G/P_{3^{k-1}+1}(G).
\]

Thus the finite map is not itself the answer. The important object is:

> **finite map + a test on that map.**

Paper 3 then asks how much of the finite information is actually needed for the selector. At the declared linear selector-carrier level, the surviving first-order detector can be compressed to a one-dimensional finite cup-product line, and dimension zero cannot recognize a false candidate. This is a category-relative minimality statement, not an absolute claim about every imaginable nonlinear finite encoding.

The resulting story is therefore:

> Paper 1 shows that finite recognition is possible.  
> Paper 2 determines the sharp affine depth needed to preserve the relevant information.  
> Paper 3 uses that finite window to recognize the genuine orientation and studies how tightly the recognition information can be compressed.

---

# Part II. One-sentence memory aid

**Paper 1:** “A finite map can recognize the genuine direction of an infinite maze.”

**Paper 2:** “We found exactly how deep the map must be so that the relevant direction information is not lost.”

**Paper 3:** “Using that map and the Kummer test, we can uniquely select the genuine direction, and within the declared linear selector category compress the decisive first-order signal to one dimension.”

The overall arc is:

\[
\boxed{\text{Recognition}
\;\longrightarrow\;
\text{Sharp information depth}
\;\longrightarrow\;
\text{Recognition at the sharp window}}
\]

---

# Part III. Metaphor dictionary

| Maze story | Mathematical object |
|---|---|
| Infinite maze | Demuškin pro-\(p\) group \(G\) |
| Whole maze | The full infinite profinite group |
| Genuine direction signpost | Canonical orientation \(\chi_G\) |
| Candidate signpost | Candidate orientation \(\rho\) |
| Finite map | Finite quotient / Zassenhaus window \(Q_k\) |
| Map depth | Filtration depth |
| Information visible on the map | Data retained by the finite quotient |
| Signpost test | Kummer predicate \(\mathsf K_k\) |
| Any candidate can be tested | Arbitrary-candidate factorization |
| False signpost fails | Failure of the Kummer condition / nonzero obstruction |
| Only one signpost survives | Uniqueness of the canonical orientation |
| Map + test | Finite quotient + intrinsic Kummer recognition mechanism |
| Exact map depth | \(p^{k-1}+1\) |
| Proof carrier that removes transient finite obstruction | Transgression quotient \(\mathcal O_k\) |
| Final compressed first-order signal | Finite cup-product line \(C_k\) |
| One-dimensional decisive signal | \(\dim_{\mathbf F_p} C_k=1\) in the declared setting |
| “Can we make the map smaller?” | Selector-minimality question |

---

# Part IV. Small glossary before the mathematics

### Demuškin group

The mathematical version of the special infinite maze: a highly structured pro-\(p\) group with a nondegenerate duality/cup-product structure.

### Canonical orientation

The genuine direction information attached to the Demuškin group:

\[
\chi_G:G\to\mathbf Z_p^\times.
\]

### Candidate \(\rho\)

A possible orientation that we want to test.

### Finite quotient \(Q_k\)

A finite approximation of \(G\) obtained by discarding sufficiently deep filtration information.

For the main selector:

\[
Q_k=G/P_{p^{k-1}+1}(G),
\]

and in the fixed \(p=3\) case:

\[
Q_k=G/P_{3^{k-1}+1}(G).
\]

### Filtration

A hierarchy measuring how deep a group-theoretic phenomenon lies. Cutting at a given level produces a finite window.

### Factorization

The statement that the relevant test/representation on the infinite group is already determined by the finite quotient. In the maze metaphor: the necessary test does not need corridors beyond the chosen map.

### Kummer predicate

The finite cohomological test that asks whether a candidate orientation has the required lifting property.

### Uniqueness

Only the canonical candidate satisfies the finite Kummer condition.

### Transgression quotient \(\mathcal O_k\)

A corrected finite obstruction carrier used in the proof. It removes the part of finite \(H^2\) that is killed by the finite central extension

\[
E_k\to Q_k.
\]

### Cup-product line \(C_k\)

The intrinsic finite subspace generated by cup products:

\[
C_k=
\operatorname{im}
\left(
H^1(Q_k,\mathbf F_p)^{\otimes2}
\xrightarrow{\cup}
H^2(Q_k,\mathbf F_p)
\right).
\]

In the declared Demuškin setting, the audited relation/cup argument gives

\[
\dim_{\mathbf F_p}C_k=1.
\]

---

# Part V. The mathematical story, now in high-school-level language

## 1. Start with an infinite object

Let \(G\) be the Demuškin pro-\(p\) group under study.

It is too large to inspect directly if our goal is to recover its canonical orientation

\[
\chi_G:G\to\mathbf Z_p^\times.
\]

The research question is therefore an information question:

> How much finite information about \(G\) is enough to determine \(\chi_G\bmod p^k\)?

This is why the finite quotient is the central object.

---

## 2. Cut the infinite object at a finite depth

Use the filtration \(P_n(G)\) and define

\[
Q_k=G/P_{p^{k-1}+1}(G).
\]

This forgets all information lying deeper than the chosen level.

The important question is not whether the quotient remembers everything about \(G\). It obviously does not.

The question is narrower:

> Does it remember everything needed for the particular recognition problem?

That distinction is fundamental.

---

## 3. Paper 1: finite information can carry recognition

The recognition problem involves a candidate \(\rho\) and a twisted cohomological lifting condition.

At the full-group level, the canonical orientation is characterized by a Kummerian condition. The research turns this into a finite-window question:

\[
\mathsf K_k(Q_k,\rho).
\]

The point is that the candidate is not assumed in advance to be the canonical one.

The test is applied to arbitrary candidates.

When the finite condition is equivalent to

\[
\rho=\chi_G\pmod{p^k},
\]

we have a genuine recognition mechanism rather than merely a reconstruction after supplying the answer.

---

## 4. Paper 2: prove the finite window is really sufficient

The main technical issue is factorization.

Suppose we have the affine crossed-cocycle representation associated with a candidate \(\rho\).

Paper 2 proves that, at level \(k\), every such representation factors through the finite quotient once the filtration reaches

\[
n_{\mathrm{aff}}(k)=p^{k-1}+1.
\]

Schematically:

\[
G
\longrightarrow
Q_k
\longrightarrow
\text{relevant affine data}.
\]

This means that the affine test cannot distinguish two elements of \(G\) that become equal in \(Q_k\).

Therefore the finite quotient genuinely contains all the information required by this class of tests.

The result is sharp in the declared affine category: a generally smaller depth does not suffice uniformly there.

---

## 5. Paper 3: turn factorization into recognition

Once factorization is known, define the finite Kummer predicate directly on \(Q_k\).

The recognition theorem is:

\[
\boxed{
\mathsf K_k(Q_k,\rho)
\iff
\rho=\chi_G\pmod{p^k}.
}
\]

The proof has two conceptual directions.

### The genuine orientation passes

The canonical orientation is known to be Kummerian. Together with factorization, its lifting property descends to the finite window.

### A false orientation fails

Write a false lift at the next level as

\[
\rho_k'
=
\chi_k(1+p^{k-1}\nu),
\]

where \(\nu\neq0\) represents the first place where the candidate differs from the canonical orientation.

The variation of the connecting obstruction is controlled by

\[
\nu\smile \bar f.
\]

The Demuškin cup product is nondegenerate, so for nonzero \(\nu\) there is a suitable witness \(f\) for which this variation is nonzero.

The finite proof must be careful here: finite \(H^2\) does not automatically inject into global \(H^2\). The repaired argument therefore uses the finite central extension

\[
1\to K_k\to E_k\to Q_k\to1
\]

and the transgression quotient

\[
\mathcal O_k(G)
=
H^2(Q_k,\mathbf F_p)/
\operatorname{im}(\operatorname{tra}_k).
\]

This removes the transient finite classes that should not count as genuine global obstructions.

That is the crucial corrected proof architecture.

---

## 6. The final compression

After the obstruction survives the transient sector, the first-order difference between the canonical and false branches is governed by the cup product.

Define

\[
C_k=
\operatorname{im}
\left(
H^1(Q_k,\mathbf F_p)^{\otimes2}
\xrightarrow{\cup}
H^2(Q_k,\mathbf F_p)
\right).
\]

The degree-two initial relation of the Demuškin group gives

\[
\dim_{\mathbf F_p}C_k=1
\]

in the declared setting.

Thus the complicated finite obstruction can, for the recognition selector, be compressed to a one-dimensional linear carrier.

The logic is:

\[
\text{false candidate}
\Rightarrow
\nu\neq0
\Rightarrow
\exists f:
u\smile\bar f\neq0
\Rightarrow
\text{nonzero finite cup obstruction}
\Rightarrow
\text{candidate rejected}.
\]

Because a zero-dimensional carrier cannot detect any false candidate, dimension one is minimal **within this declared linear selector-carrier category**.

---

# Part VI. The three papers as one mathematical machine

\[
\boxed{
\begin{array}{c}
\text{Infinite Demuškin group }G\\
\downarrow\\
\text{finite window }Q_k\\
\downarrow\\
\textbf{Paper 1: recognition mechanism exists}\\
\downarrow\\
\textbf{Paper 2: exact affine depth }p^{k-1}+1\\
\downarrow\\
\textbf{Paper 3: finite Kummer recognition}\\
\downarrow\\
\rho=\chi_G\pmod{p^k}\text{ uniquely}\
\downarrow\\
\text{linear first-order signal compressed to }C_k,\ \dim C_k=1
\end{array}}
\]

The deepest conceptual point is therefore not a particular formula.

It is the separation of three ideas:

1. **Recognition:** Can finite information determine the global invariant?
2. **Factorization depth:** How much finite information must be retained for the relevant tests?
3. **Selector:** Once that window is available, what intrinsic finite test uniquely identifies the desired invariant?

This separation prevents three different claims from being accidentally conflated.

---

# Part VII. Final intuitive summary

The research is not saying:

> “We calculated a finite approximation and happened to find the answer.”

It is saying something stronger and more structural:

> **There is an infinite object with a distinguished global direction. A finite window can retain enough information to test candidate directions. The necessary depth of that window can be bounded sharply for the relevant affine tests. At that window, an intrinsic Kummer condition singles out exactly the canonical direction, and the decisive first-order information can be compressed to a one-dimensional linear signal in the declared selector category.**

That is the unified conceptual picture of Papers 1–3.

---

## Scope reminders

- The canonical Demuškin orientation itself is classical; the papers do not claim to have invented \(\chi_G\).
- The mathematical contribution concerns the finite-window/factorization/recognition package at the explicitly declared scopes.
- “Sharp” and “minimal” are always category-relative statements here: affine crossed-cocycle sharpness and linear selector-carrier minimality are different claims.
- Absolute minimality over arbitrary nonlinear finite encodings is not claimed.
- Publication novelty remains a conditional literature-audit question; no absolute priority claim is made.
