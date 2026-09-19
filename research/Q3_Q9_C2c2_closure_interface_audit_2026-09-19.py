"""C-2c-2 closure-interface audit — 2026-09-19.

Purpose:
  Verify that the proposed graded restricted-ideal recursion agrees with
  the repository's already audited ordinary relation recursion through
  degree 5, and identify the first genuinely new restricted contribution
  at degree 6.

Method:
  - Free Lie bases are the standard Lyndon bracketing basis, embedded in
    the degree-wise tensor algebra over F_3.
  - The project restricted ambient convention is
      L_n^res = L_n plus p-power layers L_{n/3^k}^{[3^k]}.
  - The restricted ideal recursion is
      I_n = span_i [L_i^res, I_{n-i}]
            + (I_{n/3})^[3] when 3 | n.
  - All ranks are exact over F_3.

This audit does NOT insert S9, does NOT define gr_9(G), and does NOT
test H-stability.
"""

from itertools import product
from functools import lru_cache
import numpy as np

P = 3
K = 4


def add(A, B):
    C = dict(A)
    for w, c in B.items():
        C[w] = (C.get(w, 0) + c) % P
        if C[w] == 0:
            del C[w]
    return C


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
    return add(mul(A, B), {
        w: (-c) % P for w, c in mul(B, A).items()
    })


def power(A, n):
    out = {(): 1}
    for _ in range(n):
        out = mul(out, A)
    return out


def encode(word):
    idx = 0
    for x in word:
        idx = idx * K + (x - 1)
    return idx


def vector(A, degree):
    v = np.zeros(K ** degree, dtype=np.int16)
    for w, c in A.items():
        if len(w) != degree:
            raise AssertionError(
                f"wrong degree: expected {degree}, got {len(w)}"
            )
        v[encode(w)] = c % P
    return v


def rank_and_pivots(M):
    """Exact F_3 column rank and pivot-column indices."""
    A = np.array(M, dtype=np.int16, copy=True) % P
    if A.ndim == 1:
        A = A[:, None]
    rows, cols = A.shape
    r = 0
    pivots = []
    for c in range(cols):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        p = r + int(nz[0])
        if p != r:
            A[[r, p]] = A[[p, r]]
        if A[r, c] == 2:
            A[r] = (2 * A[r]) % P
        rows_to_clear = np.flatnonzero(A[:, c])
        rows_to_clear = rows_to_clear[rows_to_clear != r]
        if rows_to_clear.size:
            coeff = A[rows_to_clear, c].copy()
            A[rows_to_clear] = (
                A[rows_to_clear] - coeff[:, None] * A[r]
            ) % P
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return r, pivots


def basis_from_candidates(candidates, degree):
    if not candidates:
        return [], 0
    M = np.column_stack([vector(a, degree) for a in candidates])
    rank, pivots = rank_and_pivots(M)
    return [candidates[j] for j in pivots], rank


def is_lyndon(word):
    return all(word < word[i:] for i in range(1, len(word)))


def lyndon_words(degree):
    return [
        w for w in product(range(1, K + 1), repeat=degree)
        if is_lyndon(w)
    ]


@lru_cache(None)
def lyndon_bracket(word):
    if len(word) == 1:
        return {(word[0],): 1}

    # Standard Lyndon factorization: longest proper Lyndon suffix.
    split = None
    for i in range(1, len(word)):
        if is_lyndon(word[i:]):
            split = i
            break
    if split is None:
        raise AssertionError(f"no Lyndon factorization for {word}")
    return bracket(
        lyndon_bracket(word[:split]),
        lyndon_bracket(word[split:]),
    )


def make_lie_basis(max_degree):
    return {
        n: [lyndon_bracket(w) for w in lyndon_words(n)]
        for n in range(1, max_degree + 1)
    }


def bracket_candidates(A, B):
    return [bracket(a, b) for a in A for b in B]


def span_rank(candidates, degree):
    if not candidates:
        return 0
    return rank_and_pivots(
        np.column_stack([vector(a, degree) for a in candidates])
    )[0]


def assert_same_span(A, B, degree):
    ra = span_rank(A, degree)
    rb = span_rank(B, degree)
    rab = span_rank(A + B, degree)
    assert ra == rb == rab, (ra, rb, rab)


def main():
    L = make_lie_basis(6)

    expected = {1: 4, 2: 6, 3: 20, 4: 60, 5: 204, 6: 670}
    for n, dim in expected.items():
        assert len(L[n]) == dim
        assert span_rank(L[n], n) == dim

    # Project restricted ambient through degree 6.
    Lres = {n: list(L[n]) for n in L}
    Lres[3] += [power(x, 3) for x in L[1]]
    Lres[6] += [power(a, 3) for a in L[2]]
    assert span_rank(Lres[3], 3) == 24
    assert span_rank(Lres[6], 6) == 676

    X = [{(i,): 1} for i in range(1, 5)]
    L2 = L[2]
    R = add(L2[0], L2[5])

    # The audited ordinary relation recursion.
    I = {2: [R]}

    R3 = bracket_candidates(L[1], I[2])
    I[3], r3 = basis_from_candidates(R3, 3)
    assert r3 == 4

    R4 = bracket_candidates(L[1], I[3])
    I[4], r4 = basis_from_candidates(R4, 4)
    assert r4 == 15

    R5 = bracket_candidates(L[1], I[4])
    I[5], r5 = basis_from_candidates(R5, 5)
    assert r5 == 60

    # Proposed restricted recursion. Through degree 5 it must give
    # exactly the same spaces as the ordinary relation recursion.
    for n, expected_dim in [(3, 4), (4, 15), (5, 60)]:
        candidates = []
        for i in range(1, n):
            j = n - i
            if j in I:
                candidates += bracket_candidates(Lres[i], I[j])
        if n % 3 == 0 and n // 3 in I:
            candidates += [power(a, 3) for a in I[n // 3]]
        assert span_rank(candidates, n) == expected_dim
        assert_same_span(candidates, I[n], n)

    # The only extra ambient generators in L_3^res are x^[3].
    # Their brackets with R are not a new relation layer:
    # [x^[3],R] = ad(x)^3(R) in the associative realization.
    for x in X:
        lhs = bracket(power(x, 3), R)
        rhs = bracket(x, bracket(x, bracket(x, R)))
        assert lhs == rhs

    # Degree 6: restricted recursion has the same ordinary bracket closure
    # but adds the first genuinely new p-power contribution I_2^[3].
    ordinary6 = []
    restricted6 = []
    for i in range(1, 6):
        j = 6 - i
        if j not in I:
            continue
        ordinary6 += bracket_candidates(L[i], I[j])
        restricted6 += bracket_candidates(Lres[i], I[j])

    rank_ordinary6 = span_rank(ordinary6, 6)
    rank_restricted_brackets6 = span_rank(restricted6, 6)
    pI2 = [power(a, 3) for a in I[2]]
    rank_pI2 = span_rank(pI2, 6)
    rank_with_p = span_rank(restricted6 + pI2, 6)

    assert rank_ordinary6 == 230
    assert rank_restricted_brackets6 == 230
    assert rank_pI2 == 1
    assert rank_with_p == 231

    # Thus p-closure is first visible at degree 6 and is not redundant.
    assert rank_with_p > rank_restricted_brackets6

    print("C-2c-2 CLOSURE-INTERFACE AUDIT — 2026-09-19")
    print("==============================================")
    print("ordinary Lie dimensions:")
    for n in range(1, 7):
        print(f"  dim L_{n} = {len(L[n])}")
    print("restricted ambient:")
    print("  dim L_3^res =", span_rank(Lres[3], 3))
    print("  dim L_6^res =", span_rank(Lres[6], 6))
    print("relation recursion:")
    print("  dim I_2 =", 1)
    print("  dim I_3 =", r3)
    print("  dim I_4 =", r4)
    print("  dim I_5 =", r5)
    print("degree-6 audit:")
    print("  ordinary bracket closure rank =", rank_ordinary6)
    print("  restricted bracket closure rank =", rank_restricted_brackets6)
    print("  rank(I_2^[3]) =", rank_pI2)
    print("  rank(restricted bracket closure + I_2^[3]) =", rank_with_p)
    print("RESULT: ordinary recursion is reproduced exactly through degree 5.")
    print("RESULT: restricted ambient additions at degree 3 do not alter I_3-I_5.")
    print("RESULT: p-closure first contributes a genuinely new dimension at degree 6.")
    print("RESULT: C-2c-2 closure-interface audit = PASS")
    print("SCOPE: no S9 insertion, no degree-9 relation rank, no H-stability.")


if __name__ == "__main__":
    main()
