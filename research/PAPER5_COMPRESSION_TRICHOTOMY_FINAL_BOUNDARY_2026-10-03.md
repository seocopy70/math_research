# PAPER 5 — COMPRESSION TRICHOTOMY AND MINIMALITY BOUNDARY
## 2026-10-03

### Final structural question

After the characteristic-kernel no-go and the connected target-free realization groupoid theorem, what can “smaller/coarsest intrinsic realization” legitimately mean?

### Pre-check

**Object.** A compression object C(W) intended to replace the intrinsic realization groupoid R(W) while retaining specified information.

**Input.** The unmarked filtered source W and the intrinsically characterized target class C_{d,n}.

**Functoriality.** C must be invariant/functorial under filtered-group isomorphisms.

**Gauge.** Any marked quotient representative is forbidden unless it is explicitly retained as part of the object.

**Orientation bridge.** The only invariant currently certified at realization level is the relative split/non-split Boolean, constant on the connected realization groupoid.

**q-blindness.** The target class is q-blind at the finite-window level.

**Separation.** C2 supplies the moving-kernel obstruction to selecting one characteristic quotient.

**Stop.** No further computation is required until the information preserved by “compression” is fixed.

## 1. Three possible meanings of compression

### A. Preserve only the relative Boolean

Suppose the requirement is merely that there exist
R(W) -> C(W) -> {split,nonsplit}
with the Boolean factoring through C.

For a fixed source W_n, the Boolean is already constant on the connected admissible realization groupoid. Hence the terminal one-point object factors the Boolean.

Therefore no nontrivial minimality theorem can hold in this category: the coarsest Boolean carrier is the terminal object.

This is not a weakness of the realization groupoid. It shows that Boolean preservation alone is too weak to define the intended compression problem.

### B. Preserve the full admissible realization groupoid

Suppose a compression C is required to retain the complete admissible realization object, including morphisms/stabilizers, up to categorical equivalence.

Then any valid compression satisfies C ≃ R as a groupoid (or, for a structured functorial object, an equivalent categorical model).

Consequently “strictly smaller than R” is not an invariant notion. A skeleton may have fewer objects, but it is equivalent to R and retains exactly the same categorical information.

Thus the correct endpoint here is not a smallest representative but the equivalence class of R.

### C. Preserve a canonical characteristic quotient

If compression is required to be an internally selected quotient W/N(W) with N(W) characteristic and isomorphic to the target class, C2 already gives FAIL/CLOSED: no admissible target kernel is characteristic.

The intersection/generated-kernel audit strengthens this: the two universal characteristic kernel constructions give respectively a quotient strictly larger than Q_n and Q_n^{ab}.

## 2. Trichotomy

The three natural interpretations therefore give:

1. Boolean-only compression -> terminal object, hence trivial minimality.
2. Full-realization compression -> equivalence class of R, hence no strict smaller object in the same information category.
3. Characteristic-quotient compression -> impossible by C2.

Hence the original phrase

“the realization groupoid is the minimal characteristic invariant”

is not a well-posed theorem statement.

The mathematically defensible statement is the boundary:

> There is no nontrivial minimality theorem until the project specifies an admissible compression category and exactly which structure of the realization problem must be preserved.

Once such a category is fixed, a new minimality theorem may be meaningful, but it is a new research problem rather than a consequence of the current orbit theorem.

## 3. What is actually established

The strongest current Paper-5 chain is:

W_n
 -> intrinsic target class C_{d,n} = {Q_{d,n}} up to isomorphism
 -> intrinsic admissible realization groupoid R^{ad}_{d,n}(W_n)
 -> nonempty and connected for the declared critical source
 -> realization-independent relative split/non-split Boolean.

At the same time:

- canonical marked quotient/kernel: FAIL/CLOSED;
- first universal characteristic compressions: FAIL/CLOSED;
- absolute characteristic-compression no-go: not proved;
- orbit category as a minimal object: FAIL/CLOSED as formulated.

## 4. Novelty boundary

The nontrivial structural contribution is not a new minimality theorem.

It is the separation of three layers that were previously conflated:

(1) target isomorphism-class reconstruction is possible;
(2) marked quotient reconstruction is impossible because the admissible kernels move in an automorphism orbit;
(3) the resulting realization problem has a canonical target-free connected groupoid and an invariant relative Boolean.

This is a genuine logical-boundary result. It should not be inflated into an absolute minimality claim.

## 5. Final Paper-5 status

- intrinsic finite Demushkin-shadow target class: **PASS / CLOSED**;
- target isomorphism-class uniqueness: **PASS / CLOSED**;
- canonical marked quotient/kernel: **FAIL / CLOSED**;
- target-free admissible realization groupoid: **PASS / CLOSED** for the declared critical source/class;
- connectedness / one admissible realization orbit: **PASS / CLOSED** under the established orbit theorem;
- relative Boolean factorization: **PASS / CLOSED** under the declared admissibility/orbit hypotheses;
- intersection characteristic compression: **FAIL / CLOSED**;
- generated-kernel characteristic compression: **FAIL / CLOSED**;
- proposed orbit-category minimality: **FAIL / CLOSED** as formulated;
- absolute characteristic compression no-go: **OPEN**;
- coarsest intrinsic realization: **OPEN only after a nontrivial admissible compression category is explicitly declared**;
- absolute minimality: **OPEN only as a separately defined future problem**.

## Stop

Do not search for another carrier, another characteristic kernel, another orbit category, or another threshold.

The current Paper-5 structural program has reached its logical boundary. Any future continuation must begin by declaring a genuinely nontrivial compression category/order; otherwise “minimality” collapses either to the terminal Boolean object or to categorical equivalence with the realization groupoid.
