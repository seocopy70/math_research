"""Q3/Q9 S9 degree-9 H-stability audit — 2026-09-19.

Decision question:
  Is I_9,9 = I_infty,9 + <S9> stable under the fixed H=Sp_4(F_3) action?

Frozen inputs:
  dim I_infty,9 = 13524
  I_infty,9 cap L1^[9] = 0
  S9 = X1^[9] != 0

Because the baseline is H-stable, stability of I_9,9 would require
the line <S9> to be H-stable modulo the baseline. The L1^[9]
projection makes this an exact 4-dimensional natural-module test.

The script checks this with the authoritative symplectic convention
J and the fixed first generator t_{e2}. Under column action:
  t_{e2}(e1) = e1 + e2.
Since S9 is the restricted 9th power of e1 and coefficients are in F3,
the induced p-layer action is identical on coefficient vectors:
  S9 -> S9 + X2^[9].
This is not in <S9>, hence I_9,9 is not H-stable.
"""

P=3

J=[
    [0,1,0,0],
    [2,0,0,0],
    [0,0,0,1],
    [0,0,2,0],
]

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(4))%P for i in range(4)]

def transvection(v):
    # t_v = I + v (Jv)^T
    Jv=matvec(J,v)
    return [[(1 if i==j else 0) + v[i]*Jv[j] for j in range(4)] for i in range(4)]

def rank3(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%P),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=1 if A[r][c]%P==1 else 2
        A[r]=[(z*inv)%P for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%P:
                a=A[i][c]%P
                A[i]=[(u-a*v)%P for u,v in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def main():
    e1=[1,0,0,0]
    e2=[0,1,0,0]
    t=transvection(e2)

    # Symplectic sanity.
    JT=[[J[j][i]%P for j in range(4)] for i in range(4)]
    TJ=[[sum(t[i][k]*J[k][j] for k in range(4))%P for j in range(4)] for i in range(4)]
    TJT=[[sum(TJ[i][k]*t[j][k] for k in range(4))%P for j in range(4)] for i in range(4)]
    assert TJT==J

    image=matvec(t,e1)
    assert image==[1,1,0,0]

    # In L1^[9], restricted 9th power is coefficient-linear over F3.
    # Thus the p-layer coordinate changes from e1 to e1+2e2.
    baseline_projection=[[0,0,0,0]]  # structural lemma: zero L1^[9] projection
    s9=[1,0,0,0]
    s9_image=image

    # The new degree-9 space has L1^[9] projection exactly <e1>.
    # Its transformed generator has a nonzero e2 component.
    span_before=[s9]
    span_after=[s9_image]
    assert rank3(span_before)==1
    assert rank3(span_after)==1
    assert rank3([s9,s9_image])==2

    # Therefore transformed S9 is not in the degree-9 q=9 relation space.
    # The baseline cannot absorb the difference because its L1^[9]
    # projection is zero.
    difference=[(s9_image[i]-s9[i])%P for i in range(4)]
    assert difference==[0,1,0,0]
    assert difference != [0,0,0,0]

    print("Q3/Q9 S9 H-STABILITY DEGREE-9 AUDIT — 2026-09-19")
    print("====================================================")
    print("generator: t_e2")
    print("t_e2(e1) =", image)
    print("S9 image in L1^[9] coordinates =", s9_image)
    print("baseline L1^[9] projection rank =", rank3(baseline_projection))
    print("rank(<S9>) =", rank3(span_before))
    print("rank(<S9>, h.S9>) =", rank3([s9,s9_image]))
    print()
    print("RESULT: h.S9 = S9 + X2^[9], with nonzero X2^[9] component.")
    print("RESULT: h.S9 is not in I_9,9.")
    print("RESULT: I_9,9 is NOT H-stable.")
    print("DECISION: H-STABILITY = FAIL (mathematical failure, validated computation).")
    print("SCOPE: this does not invalidate the q=9 degree-9 relation-space construction.")
    print("SCOPE: gr9 quotient identification and D9 remain blocked.")

if __name__=="__main__":
    main()
