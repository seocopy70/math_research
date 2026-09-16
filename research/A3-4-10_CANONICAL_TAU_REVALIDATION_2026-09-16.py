import runpy
import numpy as np
from itertools import product

P=3; ROOT='research/'
ns=runpy.run_path(ROOT+'A3-4-REVALIDATION_I_AND_K_TRUE_Wd_2026-09-16.py')
rank3=ns['rank3']; W=np.array(ns['W45'],dtype=np.int64)%P; Wd=np.array(ns['Wd'],dtype=np.int64)%P
I=np.array(ns['I_coord'],dtype=np.int64)%P

# Reconstruct the canonical quotient-induced tau exactly as in the TRUE-Wd revalidation.
ns1=runpy.run_path(ROOT+'phase2_1_invariant_space_verification_2026-09-15.py')
words4=list(ns1['index4'].keys()); index4=ns1['index4']
gens=ns1['gens']; apply_linear_map=ns1['apply_linear_map']

def basis_columns(M,target):
    B=np.empty((M.shape[0],0),dtype=np.int64); r=0
    for j in range(M.shape[1]):
        C=np.column_stack([B,M[:,j]]); q=rank3(C)
        if q>r: B=C; r=q
        if r==target: break
    assert r==target; return B

def left_inverse(B):
    k=B.shape[1]; R=np.empty((0,k),dtype=np.int64); rows=[]; r=0
    for i in range(B.shape[0]):
        C=np.vstack([R,B[i:i+1]]); q=rank3(C)
        if q>r: rows.append(i); R=C; r=q
        if r==k: break
    E=np.column_stack([R,np.eye(k,dtype=np.int64)])%P
    for c in range(k):
        q=next(i for i in range(c,k) if E[i,c]); E[[c,q]]=E[[q,c]]
        if E[c,c]==2:E[c]=(2*E[c])%P
        for i in range(k):
            if i!=c and E[i,c]:E[i]=(E[i]-E[i,c]*E[c])%P
    return rows,E[:,k:]

def inv3(A):
    A=np.array(A,dtype=np.int64)%P;n=A.shape[0]
    E=np.column_stack([A,np.eye(n,dtype=np.int64)])%P
    for c in range(n):
        q=next(i for i in range(c,n) if E[i,c]);E[[c,q]]=E[[q,c]]
        if E[c,c]==2:E[c]=(2*E[c])%P
        for i in range(n):
            if i!=c and E[i,c]:E[i]=(E[i]-E[i,c]*E[c])%P
    return E[:,n:]

def coords(B,V):
    rows,L=left_inverse(B);return (L@V[rows])%P

R3=[ns1['bracket']({(i,):1},{(1,2):1,(2,1):2,(3,4):1,(4,3):2}) for i in range(1,5)]
R4_raw=[ns1['bracket']({(i,):1},r) for i in range(1,5) for r in R3]
R4=basis_columns(np.column_stack([ns1['vec4'](a) for a in R4_raw]),15)
ambient_basis=basis_columns(np.column_stack([R4,np.eye(256,dtype=np.int64)]),60)
rows,L60=left_inverse(ambient_basis)
QW=(L60@W[rows])%P; QWd=(L60@Wd[rows])%P
QW=QW[15:,:]; QWd=QWd[15:,:]
assert rank3(QW)==45 and rank3(QWd)==45
tau_coord=(inv3(QWd)@QW)%P
# tau: W45 coordinates -> Wd coordinates
T_ambient=(Wd@tau_coord)%P
# tau-id as an ambient map W45 -> L4
E=(T_ambient-W)%P
# Verify canonical tau fixes the actual 35-dimensional intersection I.
assert rank3(E)<=10
assert rank3((E@I)%P)==0

# Degree-5 bracket discrepancy for the canonical tau.
words5=list(product((1,2,3,4),repeat=5)); index5={w:i for i,w in enumerate(words5)}
def br(v,g):
    out=np.zeros(1024,dtype=np.int64)
    for j,c in enumerate(v):
        c=int(c)%P
        if c:
            w=words4[j];out[index5[w+(g,)]]=(out[index5[w+(g,)]]+c)%P
            out[index5[(g,)+w]]=(out[index5[(g,)+w]]-c)%P
    return out
D=np.vstack([np.column_stack([br(E[:,j],g) for j in range(45)]) for g in range(1,5)])%P
print('A3-4-10 / CANONICAL QUOTIENT TAU REVALIDATION')
print('dim W45 =',rank3(W)); print('dim Wd =',rank3(Wd)); print('dim I =',rank3(W@I))
print('rank(tau-id) =',rank3(E)); print('nullity(tau-id) on W45 =',45-rank3(E))
print('rank((tau-id)|I) =',rank3(E@I)); print('tau fixes I exactly =',rank3(E@I)==0)
print('canonical tau is H-equivariant =', all(np.array_equal((A@tau_coord)%P,(tau_coord@A)%P) for A in ns['A_W']))
print('canonical bracket obstruction rank =',rank3(D))
print('canonical obstruction shape =',D.shape)
assert rank3(E)<=10 and rank3(E@I)==0
assert all(np.array_equal((A@tau_coord)%P,(tau_coord@A)%P) for A in ns['A_W'])
print('RESULT: canonical quotient-induced tau has displacement rank <=10; this is distinct from the old A3-4-10 affine intertwiner X.')
print('ALL CANONICAL TAU REVALIDATION CHECKS PASSED')
