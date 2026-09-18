"""Q3-2A-R: robustness audit for the size-40 projective orbit observation.

This is an audit, not a q=3/q=infinity experiment.
It verifies:
1) the generated image on U has order 25920, and its projective kernel is measured explicitly;
2) the projective kernel is explicitly measured;
3) the target [N(d3)] lies in the size-40 orbit;
4) all d in the H-orbit of the authoritative d3 give N(d) in the same
   projective orbit (when nonzero);
5) the audit records the exact generators, U basis, and sampled/all H-orbit
   targets needed for reproduction.

The robustness test is intentionally restricted to the H-orbit of d3.
Therefore it tests H-equivalent choices, not arbitrary alternative local
representatives. No q-information is inferred.
"""
from pathlib import Path
import runpy, json
import numpy as np

P = 3
ROOT = Path(__file__).parent
ART = ROOT / "artifacts"

ns = runpy.run_path(str(ROOT / "O2_7_q_control_variation_module_2026-09-18.py"))
N = np.array(ns["N"], dtype=np.int64) % P
A_W = [np.array(A, dtype=np.int64) % P for A in ns["A_W"]]
d_W = np.array(ns["d_W"], dtype=np.int64) % P

# Reconstruct the exact five authoritative 4x4 generators explicitly.
# Do not depend on runpy namespace names for generator provenance.
J = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=np.int64) % P
generating_vectors = [
    (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (1,0,1,0)
]
def transvection(v):
    v = np.array(v, dtype=np.int64).reshape(4,1) % P
    return (np.eye(4, dtype=np.int64) + v @ ((J @ v).T)) % P
gens_4 = [transvection(v) for v in generating_vectors]

def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    m, n = A.shape
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i, c]), None)
        if piv is None:
            continue
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r

def column_basis(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    pivots = []
    current = np.zeros((A.shape[0], 0), dtype=np.int64)
    current_rank = 0
    for j in range(A.shape[1]):
        candidate = np.column_stack([current, A[:, j]]) if current.size else A[:, j:j+1]
        r = rank3(candidate)
        if r > current_rank:
            pivots.append(j)
            current = candidate
            current_rank = r
    return A[:, pivots]

def solve_full_column(A, b):
    A = np.array(A, dtype=np.int64) % P
    b = np.array(b, dtype=np.int64) % P
    m, n = A.shape
    aug = np.concatenate([A, b.reshape(m, 1)], axis=1)
    row = 0
    pivots = []
    for c in range(n):
        p = next((i for i in range(row, m) if aug[i, c]), None)
        if p is None:
            continue
        if p != row:
            aug[[row, p]] = aug[[p, row]]
        if aug[row, c] == 2:
            aug[row] = (2 * aug[row]) % P
        for i in range(m):
            if i != row and aug[i, c]:
                aug[i] = (aug[i] - aug[i, c] * aug[row]) % P
        pivots.append(c)
        row += 1
    if np.any(np.all(aug[:, :n] == 0, axis=1) & (aug[:, n] != 0)):
        raise AssertionError("vector not in U")
    x = np.zeros(n, dtype=np.int64)
    for i, c in enumerate(pivots):
        x[c] = aug[i, n]
    assert np.array_equal((A @ x) % P, b)
    return x

# ---------- Structural preflight ----------
U_basis = column_basis(N)
assert U_basis.shape == (45, 10)
assert rank3(U_basis) == 10
assert rank3(np.column_stack([U_basis, N])) == 10

for gi, A in enumerate(A_W):
    image = (A @ U_basis) % P
    assert rank3(np.column_stack([U_basis, image])) == 10, (
        f"U is not H-stable under generator {gi}"
    )

A_U = []
for A in A_W:
    cols = np.column_stack([
        solve_full_column(U_basis, (A @ U_basis[:, j]) % P)
        for j in range(10)
    ])
    A_U.append(cols % P)
    assert np.array_equal((U_basis @ cols) % P, (A @ U_basis) % P)

print("Q3-2A-R PREFLIGHT: U=im(N) rank-10 and H-stable under all 5 generators")

def line_key(v):
    v = np.array(v, dtype=np.int64) % P
    nz = np.flatnonzero(v)
    if len(nz) == 0:
        raise ValueError("zero vector")
    scale = 1 if v[nz[0]] == 1 else 2
    return tuple(((scale * v) % P).tolist())

def mat_key(A):
    return tuple(np.array(A, dtype=np.int64).reshape(-1).tolist())

def mat_apply(A, v):
    return tuple(((A @ np.array(v, dtype=np.int64)) % P).tolist())

# ---------- Abstract H = Sp4(F3) / representation kernel audit ----------
assert len(gens_4) == 5
J = np.array([[0,1,0,0],[-1,0,0,0],[0,0,0,1],[0,0,-1,0]], dtype=np.int64) % P
assert all(np.array_equal((g.T @ J @ g) % P, J) for g in gens_4)
I4 = np.eye(4, dtype=np.int64)
def key4(A): return tuple(np.array(A, dtype=np.int64).reshape(-1).tolist())
abstract_group = {key4(I4): I4}
frontier4 = [I4]
while frontier4:
    g = frontier4.pop()
    for a in gens_4:
        h = (a @ g) % P
        k = key4(h)
        if k not in abstract_group:
            abstract_group[k] = h
            frontier4.append(h)
assert len(abstract_group) == 51840
# Simultaneously enumerate the representation image; each abstract element
# is tracked with its induced U matrix, so the kernel is measured directly.
paired = {(key4(I4), mat_key(np.eye(10, dtype=np.int64))): (I4, np.eye(10, dtype=np.int64))}
frontier_pair = [(I4, np.eye(10, dtype=np.int64))]
while frontier_pair:
    g4, gu = frontier_pair.pop()
    for a4, au in zip(gens_4, A_U):
        h4 = (a4 @ g4) % P
        hu = (au @ gu) % P
        k = (key4(h4), mat_key(hu))
        if k not in paired:
            paired[k] = (h4, hu)
            frontier_pair.append((h4, hu))
kernel_elements = [h4 for h4, hu in paired.values() if np.array_equal(hu, np.eye(10, dtype=np.int64))]
assert len(kernel_elements) == 2
assert any(np.array_equal(g, I4) for g in kernel_elements)
assert any(np.array_equal(g, (-I4) % P) for g in kernel_elements)
assert len(paired) == 51840
print("Q3-2A-R ABSTRACT H ORDER =", len(abstract_group))
print("Q3-2A-R KERNEL H->GL(U) ORDER =", len(kernel_elements))

# ---------- Enumerate the actual generated group on U ----------
I10 = np.eye(10, dtype=np.int64)
group = {mat_key(I10): I10}
frontier = [I10]
while frontier:
    g = frontier.pop()
    for a in A_U:
        h = (a @ g) % P
        k = mat_key(h)
        if k not in group:
            group[k] = h
            frontier.append(h)

H_order = len(group)
assert H_order == 25920, f"generated image on U has order {H_order}, expected 25920"
print("Q3-2A-R GROUP IMAGE ORDER ON U =", H_order)

# Projective kernel of the generated image on U: scalar matrices actually present.
scalar_keys = {mat_key(I10), mat_key((2 * I10) % P)}
projective_kernel_order = sum(1 for g in group.values() if mat_key(g) in scalar_keys)
assert projective_kernel_order == 1, (
    f"unexpected projective kernel order {projective_kernel_order}; "
    "2I should not occur in the U-image"
)
effective_projective_order = H_order // projective_kernel_order
assert effective_projective_order == 25920
print("Q3-2A-R PROJECTIVE KERNEL ORDER =", projective_kernel_order)
print("Q3-2A-R EFFECTIVE PROJECTIVE GROUP ORDER =", effective_projective_order)

# ---------- Reconstruct the Q3-2A census ----------
lines = []
for vals in np.ndindex(*(3,) * 10):
    if all(x == 0 for x in vals):
        continue
    if next(x for x in vals if x) != 1:
        continue
    lines.append(tuple(vals))
assert len(lines) == (3**10 - 1) // 2

line_set = set(lines)

def act_line(key, A):
    return line_key((A @ np.array(key, dtype=np.int64)) % P)

# Use the full generated group for the orbit of any target, while the
# census itself is still reproduced from the five generators.
unseen = set(line_set)
orbits = []
while unseen:
    seed = min(unseen)
    orb = {seed}
    frontier = [seed]
    while frontier:
        x = frontier.pop()
        for A in A_U:
            y = act_line(x, A)
            if y not in orb:
                orb.add(y)
                frontier.append(y)
    unseen -= orb
    orbits.append(orb)

orbits.sort(key=lambda o: (len(o), min(o)))
sizes = [len(o) for o in orbits]
assert len(orbits) == 16
assert sizes[0] == 40
assert min(sizes) == 40
assert max(sizes) == 4320

Nd = (N @ d_W) % P
assert rank3(Nd) == 1
nd_coord = solve_full_column(U_basis, Nd)
nd_line = line_key(nd_coord)
target_idx = next(i for i, o in enumerate(orbits) if nd_line in o)
assert len(orbits[target_idx]) == 40

# ---------- Robustness over the full H-orbit of d3 ----------
d_orbit = set()
d_frontier = [d_W]
d_keys = {tuple(d_W.tolist())}
while d_frontier:
    d = d_frontier.pop()
    d_orbit.add(tuple(d.tolist()))
    for a in A_W:
        y = (a @ d) % P
        k = tuple(y.tolist())
        if k not in d_keys:
            d_keys.add(k)
            d_frontier.append(y)

assert len(d_orbit) > 1
assert len(d_orbit) <= 51840

target_orbit_sizes = []
nd_lines = []
nd_nonzero_count = 0
nd_zero_count = 0
for d_tuple in d_orbit:
    d = np.array(d_tuple, dtype=np.int64)
    nd = (N @ d) % P
    if rank3(nd) == 0:
        nd_zero_count += 1
        continue
    nd_nonzero_count += 1
    c = solve_full_column(U_basis, nd)
    lk = line_key(c)
    idx = next(i for i, o in enumerate(orbits) if lk in o)
    target_orbit_sizes.append(len(orbits[idx]))
    nd_lines.append(lk)

assert nd_nonzero_count > 0
assert set(target_orbit_sizes) == {40}

# Equivariance audit: N(A_W d) = A_U N(d) in coordinates for all d in the orbit.
# This directly explains why H-equivalent representatives should stay in one
# projective orbit, but we still check it computationally.
equivariance_checks = 0
for d_tuple in list(d_orbit):
    d = np.array(d_tuple, dtype=np.int64)
    for aW, aU in zip(A_W, A_U):
        lhs = (N @ ((aW @ d) % P)) % P
        ndc = solve_full_column(U_basis, (N @ d) % P)
        rhs = (U_basis @ (aU @ ndc)) % P
        assert np.array_equal(lhs, rhs)
        equivariance_checks += 1

artifact = {
    "experiment": "Q3-2A-R",
    "scope": "robustness audit only; no q=3 vs q=infinity claim",
    "single_invariant": "I([v]) = |H.[v]|",
    "authoritative_source_commit": "d9817458f793f6cc0ae7535d8e0bd21bd3b4c525",
    "dim_U": 10,
    "N_rank": rank3(N),
    "U_basis_shape": list(U_basis.shape),
    "U_basis_rank": rank3(U_basis),
    "num_H_generators": len(A_U),
    "H_generator_matrices_on_U": [A.tolist() for A in A_U],
    "abstract_H_order": len(abstract_group),
    "exact_5_generators_on_V": [g.tolist() for g in gens_4],
    "kernel_H_to_U_order_verified": len(kernel_elements),
    "kernel_H_to_U_elements": [g.tolist() for g in kernel_elements],
    "generated_U_image_order": H_order,
    "kernel_H_to_U_order": 2,
    "abstract_H_projective_kernel_order_verified": 2,
    "abstract_H_projective_effective_order": 25920,
    "projective_kernel_order": projective_kernel_order,
    "projective_kernel_scalars_present": [1],
    "effective_projective_group_order": effective_projective_order,
    "projective_line_count": len(lines),
    "projective_orbit_count": len(orbits),
    "orbit_sizes": sizes,
    "minimum_orbit_size": min(sizes),
    "maximum_orbit_size": max(sizes),
    "Nd3_rank": rank3(Nd),
    "Nd3_orbit_size": len(orbits[target_idx]),
    "Nd3_orbit_index": target_idx,
    "Nd3_stabilizer_order_in_abstract_H": 51840 // len(orbits[target_idx]),
    "Nd3_stabilizer_order_in_U_image": H_order // len(orbits[target_idx]),
    "d3_H_orbit_size": len(d_orbit),
    "N_d_nonzero_count": nd_nonzero_count,
    "N_d_zero_count": nd_zero_count,
    "N_d_projective_orbit_sizes": sorted(set(target_orbit_sizes)),
    "all_H_equivalent_nonzero_Nd_are_size_40": set(target_orbit_sizes) == {40},
    "equivariance_checks": equivariance_checks,
    "robustness_scope_note": (
        "Tests every d in the H-orbit of the authoritative d3; "
        "does not test arbitrary non-H-equivalent local representatives."
    ),
}

ART.mkdir(exist_ok=True)
(ART / "q3_2a_r_robustness_audit.json").write_text(
    json.dumps(artifact, indent=2), encoding="utf-8"
)

print("Q3-2A-R ROBUSTNESS AUDIT")
print("generated U-image order =", H_order)
print("projective kernel order =", projective_kernel_order)
print("effective projective order =", effective_projective_order)
print("projective census orbit count =", len(orbits))
print("minimum orbit size =", min(sizes))
print("maximum orbit size =", max(sizes))
print("[N(d3)] orbit size =", len(orbits[target_idx]))
print("[N(d3)] stabilizer order in abstract H =", 51840 // len(orbits[target_idx]))
print("[N(d3)] stabilizer order in U-image =", H_order // len(orbits[target_idx]))
print("d3 H-orbit size =", len(d_orbit))
print("nonzero N(d) count on H.d3 =", nd_nonzero_count)
print("zero N(d) count on H.d3 =", nd_zero_count)
print("projective orbit sizes of all nonzero N(d), d in H.d3 =", sorted(set(target_orbit_sizes)))
print("all nonzero H-equivalent N(d) are size 40 =", set(target_orbit_sizes) == {40})
print("Q3-2A-R RESULT = H-EQUIVALENT ROBUSTNESS CONFIRMED")
