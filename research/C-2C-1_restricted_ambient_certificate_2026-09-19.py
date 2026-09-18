"""C-2c-1: restricted ambient certificate (small rank-2 control).

Purpose:
  Verify directly in the tensor algebra over F_3 that, for two generators
  in degree 9, the free Lie component L_9 and the restricted p-power
  contributions L_3^[3] and L_1^[9] are linearly independent.

This is an ambient-space certificate only. It does not construct R_9,
gr_9(G), H-stability, or any q-invariant.

The implementation uses exact F_3 arithmetic and a custom rank routine;
no floating-point linear algebra is used.
"""

P = 3
K = 2


def rank3(rows):
    A = [list(map(lambda x: x % P, row)) for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = 1 if A[r][c] == 1 else 2
        A[r] = [(x * inv) % P for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                a = A[i][c]
                A[i] = [(x - a * y) % P for x, y in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r


def independent(rows):
    out = []
    r = 0
    for row in rows:
        rr = rank3(out + [row])
        if rr > r:
            out.append(row)
            r = rr
    return out


def encode(word):
    idx = 0
    for x in word:
        idx = idx * K + x
    return idx


def vector_from_dict(d, degree):
    v = [0] * (K ** degree)
    for word, coeff in d.items():
        v[encode(word)] = coeff % P
    return v


def dict_from_vector(v, degree):
    out = {}
    for idx, coeff in enumerate(v):
        if coeff % P == 0:
            continue
        x = idx
        word = [0] * degree
        for j in range(degree - 1, -1, -1):
            word[j] = x % K
            x //= K
        out[tuple(word)] = coeff % P
    return out


def bracket(u, v):
    out = {}
    for wu, cu in u.items():
        for wv, cv in v.items():
            uv = wu + wv
            vu = wv + wu
            out[uv] = (out.get(uv, 0) + cu * cv) % P
            out[vu] = (out.get(vu, 0) - cu * cv) % P
    return {w: c for w, c in out.items() if c % P}


def build_free_lie_bases(max_degree):
    L = {
        1: [
            vector_from_dict({(0,): 1}, 1),
            vector_from_dict({(1,): 1}, 1),
        ]
    }
    for n in range(2, max_degree + 1):
        candidates = []
        for i in range(1, n):
            j = n - i
            for u in L[i]:
                for v in L[j]:
                    candidates.append(
                        vector_from_dict(
                            bracket(dict_from_vector(u, i), dict_from_vector(v, j)),
                            n,
                        )
                    )
        L[n] = independent(candidates)
    return L


def associative_power(v, degree, exponent):
    base = dict_from_vector(v, degree)
    result = {(): 1}
    for _ in range(exponent):
        nxt = {}
        for a, ca in result.items():
            for b, cb in base.items():
                w = a + b
                nxt[w] = (nxt.get(w, 0) + ca * cb) % P
        result = {w: c for w, c in nxt.items() if c % P}
    return vector_from_dict(result, degree * exponent)


def main():
    L = build_free_lie_bases(9)

    l3 = L[3]
    l9 = L[9]
    p3 = [associative_power(v, 3, 3) for v in l3]
    p9 = [associative_power(v, 1, 9) for v in L[1]]

    r_l9 = rank3(l9)
    r_p3 = rank3(p3)
    r_p9 = rank3(p9)
    r_all = rank3(l9 + p3 + p9)

    expected_l9 = (2 ** 9 - 2 ** 3) // 9
    expected_l3 = (2 ** 3 - 2) // 3

    assert r_l9 == expected_l9 == 56
    assert r_p3 == expected_l3 == 2
    assert r_p9 == 2
    assert r_all == 60
    assert r_all == r_l9 + r_p3 + r_p9

    print("C-2c-1 PASS")
    print(f"L_9 rank = {r_l9}")
    print(f"L_3^[3] rank = {r_p3}")
    print(f"L_1^[9] rank = {r_p9}")
    print(f"restricted degree-9 span rank = {r_all}")
    print("rank-2 restricted ambient dimension = 60")
    print("four-generator formal dimension check: L_9 + L_3^[3] + L_1^[9] = 29120 + 20 + 4 = 29144")


if __name__ == "__main__":
    main()
