import numpy as np
from itertools import product

P = 3
D1 = 4
WORDS4 = list(product(range(1, 5), repeat=4))
INDEX4 = {w: i for i, w in enumerate(WORDS4)}
WORDS5 = list(product(range(1, 5), repeat=5))
INDEX5 = {w: i for i, w in enumerate(WORDS5)}


def add(A, B):
    C = dict(A)
    for w, c in B.items():
        C[w] = (C.get(w, 0) + c) % P
        if C[w] == 0:
            del C[w]
    return C


def neg(A):
    return {w: (-c) % P for w, c in A.items() if c % P}


def mul(A, B):
    C = {}
    for wa, ca in A.items():
        for wb, cb in B.items():
            w = wa + wb
            C[w] = (C.get(w, 0) + ca * cb) % P
            if C[w] == 0:
                del C[w]
    return C


def bracket(A, B):
    return add(mul(A, B), neg(mul(B, A)))


def rank3(A):
    A = np.array(A, dtype=np.int64, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
    m, n = A.shape
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i, c]), None)
        if q is None:
            continue
        A[[r, q]] = A[[q, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        for i in range(m):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == m:
            break
    return r


def vec4(A):
    v = np.zeros(256, dtype=np.int64)
    for w, c in A.items():
        v[INDEX4[w]] = c % P
    return v


def vec5(A):
    v = np.zeros(1024, dtype=np.int64)
    for w, c in A.items():
        v[INDEX5[w]] = c % P
    return v


def vec_to_dict4(v):
    return {WORDS4[i]: int(c) % P for i, c in enumerate(v) if int(c) % P}


def apply_linear_map(A, g):
    # Column convention: e_j maps to sum_i g[i,j] e_i.
    images = []
    for j in range(D1):
        image = {}
        for i in range(D1):
            c = int(g[i, j]) % P
            if c:
                image[(i + 1,)] = c
        images.append(image)
    out = {}
    for word, coeff in A.items():
        cur = {(): coeff}
        for letter in word:
            cur = mul(cur, images[letter - 1])
        out = add(out, cur)
    return out


def transvection(v):
    J = np.array([[0, 1, 0, 0], [-1, 0, 0, 0],
                  [0, 0, 0, 1], [0, 0, -1, 0]], dtype=np.int64) % P
    v = np.array(v, dtype=np.int64) % P
    return (np.eye(4, dtype=np.int64) + np.outer(v, (J @ v) % P)) % P


def basis_columns(M, target):
    B = np.empty((M.shape[0], 0), dtype=np.int64)
    r = 0
    for j in range(M.shape[1]):
        C = np.column_stack([B, M[:, j]])
        q = rank3(C)
        if q > r:
            B = C
            r = q
            if r == target:
                break
    assert r == target
    return B


def orbit_basis(seed, gens, target, modulo=None):
    basis = []
    combined = np.empty((256, 0), dtype=np.int64) if modulo is None else modulo.copy()
    queue = [seed]
    seen = set()
    while queue:
        a = queue.pop(0)
        key = tuple(vec4(a).tolist())
        if key in seen:
            continue
        seen.add(key)
        old_rank = rank3(combined)
        candidate = np.column_stack([combined, vec4(a)])
        new_rank = rank3(candidate)
        if new_rank > old_rank:
            basis.append(a)
            combined = candidate
            if len(basis) == target:
                # Continue no further: the target basis is already reached.
                # The queue is irrelevant to the basis itself.
                break
        for g in gens:
            queue.append(apply_linear_map(a, g))
    assert len(basis) == target
    return basis


# ---------- Independent construction of the ambient degree-4 data ----------
X = [{(1,): 1}, {(2,): 1}, {(3,): 1}, {(4,): 1}]
L2 = [bracket(X[i], X[j]) for i in range(4) for j in range(i + 1, 4)]
R = add(L2[0], L2[5])
R3 = [bracket(x, R) for x in X]
R4 = [bracket(x, r3) for x in X for r3 in R3]
R4_matrix = np.column_stack([vec4(a) for a in R4])
assert rank3(R4_matrix) == 15

J = np.array([[0, 1, 0, 0], [-1, 0, 0, 0],
              [0, 0, 0, 1], [0, 0, -1, 0]], dtype=np.int64) % P
generating_vectors = [(1, 0, 0, 0), (0, 1, 0, 0),
                      (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 1, 0)]
gens = [transvection(v) for v in generating_vectors]
assert len(gens) == 5
assert all(np.array_equal((g.T @ J @ g) % P, J) for g in gens)

T = bracket(bracket(bracket(X[2], X[3]), X[0]), X[0])
d = bracket({(1, 1, 1): 1}, {(2,): 1})

# W45 is the orbit span of T modulo (R)_4.
W_basis = orbit_basis(T, gens, 45, modulo=R4_matrix)
W = np.column_stack([vec4(a) for a in W_basis])
assert W.shape == (256, 45) and rank3(W) == 45
assert rank3(np.column_stack([R4_matrix, W])) == 60

# Wd is the orbit span of d; independently take 45 pivot columns.
queue = [d]
seen = {tuple(vec4(d).tolist())}
while queue:
    a = queue.pop(0)
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen:
            seen.add(key)
            queue.append(b)
Wd_all = np.column_stack([vec4(a) for a in [d]])
Wd_all = np.column_stack([vec4(a) for a in queue]) if False else None
# Rebuild the orbit list from the seen vectors in a deterministic order.
# A second BFS preserves the actual associative-word representatives.
orbit = [d]
seen2 = {tuple(vec4(d).tolist())}
for a in orbit:
    for g in gens:
        b = apply_linear_map(a, g)
        key = tuple(vec4(b).tolist())
        if key not in seen2:
            seen2.add(key)
            orbit.append(b)
assert len(orbit) == 360
Wd = basis_columns(np.column_stack([vec4(a) for a in orbit]), 45)
assert Wd.shape == (256, 45) and rank3(Wd) == 45

# ---------- Independent D1 / D4 / D5 actions ----------
def degree_action_matrix(g, degree, words, index):
    dim = len(words)
    G = np.zeros((dim, dim), dtype=np.int64)
    for j, w in enumerate(words):
        out = apply_linear_map({w: 1}, g)
        for ww, c in out.items():
            G[index[ww], j] = (G[index[ww], j] + int(c)) % P
    return G


def action1(g, h):
    # D1(g) X_h as an associative degree-1 vector.
    return apply_linear_map({(h,): 1}, g)


def bracket_col(v4, h):
    # Pure associative expansion [v, X_h] = v X_h - X_h v.
    out = np.zeros(1024, dtype=np.int64)
    for j, coeff in enumerate(v4):
        c = int(coeff) % P
        if not c:
            continue
        w = WORDS4[j]
        out[INDEX5[w + (h,)]] = (out[INDEX5[w + (h,)]] + c) % P
        out[INDEX5[(h,) + w]] = (out[INDEX5[(h,) + w]] - c) % P
    return out

print('A3-4-10 BRACKET PIPELINE SANITY CHECK (STANDALONE)')
print('No phase script is imported or executed.')
print('dim W45 =', rank3(W), 'dim Wd =', rank3(Wd))

# First isolate the three requested layers before testing the final identity.
for gi, g in enumerate(gens):
    D1g = degree_action_matrix(g, 1, list(product(range(1, 5), repeat=1)),
                               {w: i for i, w in enumerate(product(range(1, 5), repeat=1))})
    D4g = degree_action_matrix(g, 4, WORDS4, INDEX4)
    D5g = degree_action_matrix(g, 5, WORDS5, INDEX5)
    assert np.array_equal(D1g, g % P)
    # D4/D5 must agree with repeated application of the same D1 substitution.
    for j in (0, 1, 2, 3, 4, 15, 63, 127, 255):
        expected4 = vec4(apply_linear_map({WORDS4[j]: 1}, g))
        assert np.array_equal(D4g[:, j], expected4)
    for j in (0, 1, 7, 31, 127, 511, 1023):
        expected5 = vec5(apply_linear_map({WORDS5[j]: 1}, g))
        assert np.array_equal(D5g[:, j], expected5)
    print('GEN', gi, 'D1/D4/D5 action construction checks = PASS')

    for label, M in [('W45', W), ('Wd', Wd)]:
        for j in range(M.shape[1]):
            v = M[:, j] % P
            D4v = (D4g @ v) % P
            for h in range(1, 5):
                # Input-side isolation: verify D1(g)X_h independently.
                gh = action1(g, h)
                gh_vec = np.zeros(4, dtype=np.int64)
                for w, c in gh.items():
                    gh_vec[w[0] - 1] = c % P
                assert np.array_equal(gh_vec, D1g[:, h - 1])

                # Bracket isolation: compare the direct expansion with the
                # generic associative-map computation, before using D5.
                direct_bracket = bracket_col(v, h)
                generic_bracket = vec5(bracket(vec_to_dict4(v), {(h,): 1}))
                assert np.array_equal(direct_bracket, generic_bracket)

                lhs = (D5g @ direct_bracket) % P
                rhs = vec5(bracket(vec_to_dict4(D4v), gh))
                if not np.array_equal(lhs, rhs):
                    diff = (lhs - rhs) % P
                    nz = np.flatnonzero(diff)
                    print('FIRST_FAILURE')
                    print('generator =', gi, 'space =', label, 'basis =', j, 'h =', h)
                    print('D1(g)X_h =', gh)
                    print('D4(g)v nonzero count =', int(np.count_nonzero(D4v)))
                    print('bracket(v,X_h) nonzero count =', int(np.count_nonzero(direct_bracket)))
                    print('D5(g)[v,X_h] nonzero count =', int(np.count_nonzero(lhs)))
                    print('[D4(g)v,D1(g)X_h] nonzero count =', int(np.count_nonzero(rhs)))
                    print('difference nonzero count =', int(len(nz)))
                    print('first differing degree-5 word =', WORDS5[int(nz[0])] if len(nz) else None)
                    raise AssertionError((gi, label, j, h))
        print('GEN', gi, label, 'BRACKET_EQUIVARIANCE = PASS')

print('RESULT = PASS')
print('Ambient D1/D4/D5 construction and associative bracket equivariance are independently verified.')
print('This does not decide the separate A3-4-10 tau-compatibility question.')
