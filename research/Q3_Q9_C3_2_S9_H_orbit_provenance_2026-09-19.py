"""C3.2 — provenance test for H-closure of S9.

Question:
  Can span(H·S9) be promoted as the degree-9 relation contribution
  of the fixed q=9 presentation
      x1^9 [x1,x2][x3,x4] = 1 ?

Frozen exact facts:
  I_9,9 = I_infty,9 direct-sum <S9>
  S9 = X1^[9] in L1^[9]
  I_infty,9 cap L1^[9] = 0
  span(H·S9) = L1^[9] from C3.1

Witness:
  t_{e2}(S9) = S9 + X2^[9].
Thus X2^[9] lies in the H-closure contribution, but is not in
the fixed-presentation degree-9 relation space.

Decision:
  C3.2 PASS only if every new orbit direction is an actual
  consequence of the fixed presentation.
  Here the witness gives FAIL for promotion of H-closure.
"""

P=3
# In the L1^[9] quotient, use coefficient vectors.
S9=[1,0,0,0]
X2=[0,1,0,0]
tS9=[1,1,0,0]

def rank3(rows):
    A=[[z%P for z in row] for row in rows]; r=0
    for c in range(4):
        piv=next((i for i in range(r,len(A)) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=1 if A[r][c]==1 else 2
        A[r]=[(z*inv)%P for z in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                a=A[i][c]; A[i]=[(u-a*v)%P for u,v in zip(A[i],A[r])]
        r+=1
    return r

def main():
    # Frozen S9-B consequence: baseline has no L1^[9] component.
    baseline_projection_rank=0

    # Therefore the degree-9 fixed-presentation q=9 relation space
    # projects to exactly the line <S9> in L1^[9].
    q9_projection_rank=1
    assert baseline_projection_rank==0

    # Exact witness from the H-stability gate.
    assert tS9==[1,1,0,0]
    assert rank3([S9,tS9])==2

    # Difference is X2^[9], so the second orbit direction is not in
    # the fixed-presentation q=9 relation space.
    difference=[(tS9[i]-S9[i])%P for i in range(4)]
    assert difference==X2
    assert difference!=[0,0,0,0]

    print("C3.2 S9 H-CLOSURE PROVENANCE — 2026-09-19")
    print("===========================================")
    print("fixed q=9 L1^[9] relation projection rank =", q9_projection_rank)
    print("rank(<S9,t_e2 S9>)                      =", rank3([S9,tS9]))
    print("new orbit direction                     = X2^[9]")
    print("X2^[9] in fixed q=9 degree-9 relation?  = NO")
    print()
    print("RESULT: C3.2 = FAIL for promotion of H-closure.")
    print("INTERPRETATION: span(H·S9) defines a different H-closed")
    print("relation enlargement, not the relation space of the fixed")
    print("q=9 presentation. It may be studied only as a new object.")
    print("BOUNDARY: do not use it for gr9 or D9 of the original q=9 group.")

if __name__=="__main__":
    main()
