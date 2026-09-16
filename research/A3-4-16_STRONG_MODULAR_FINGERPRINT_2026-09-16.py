import runpy
import numpy as np
from collections import deque
from sympy import Matrix, symbols

P=3; ROOT='research/'
ns=runpy.run_path(ROOT+'A3-4-14_BA_MODULE_FINGERPRINT_2026-09-16.py')
rank3=ns['rank3']; Mgens=[np.array(x,dtype=np.int64)%P for x in ns['Mgens']]
BA_gens=[np.array(x,dtype=np.int64)%P for x in ns['BA']]; K_gens=[np.array(x,dtype=np.int64)%P for x in ns['K']]
I4=np.eye(4,dtype=np.int64); I35=np.eye(35,dtype=np.int64)
def mm(A,B): return (A@B)%P
def key(M): return tuple(int(x) for x in M.reshape(-1))
def inv4(M):
    R=np.column_stack([M.copy()%P,I4]); r=0
    for c in range(4):
        q=next(i for i in range(r,4) if R[i,c]); R[[r,q]]=R[[q,r]]
        if R[r,c]==2:R[r]=(2*R[r])%P
        for i in range(4):
            if i!=r and R[i,c]:R[i]=(R[i]-R[i,c]*R[r])%P
        r+=1
    return R[:,4:]%P
Ginv=[inv4(G) for G in Mgens]
Gmap={key(I4):0}; group=[I4]; parent=[-1]; parent_gen=[-1]; q=deque([0])
while q:
    i=q.popleft(); A=group[i]
    for gi,G in enumerate(Mgens):
        H=mm(A,G); k=key(H)
        if k not in Gmap:
            Gmap[k]=len(group); group.append(H); parent.append(i); parent_gen.append(gi); q.append(len(group)-1)
assert len(group)==51840
adj=[[] for _ in group]
for i,A in enumerate(group):
    for G,Gi in zip(Mgens,Ginv):
        adj[i].append(Gmap[key(mm(mm(G,A),Gi))]); adj[i].append(Gmap[key(mm(mm(Gi,A),G))])
seen=np.zeros(len(group),bool); classes=[]; class_of=np.full(len(group),-1,np.int32)
for s in range(len(group)):
    if seen[s]: continue
    st=[s]; seen[s]=1; cls=[]
    while st:
        i=st.pop(); cls.append(i)
        for j in adj[i]:
            if not seen[j]: seen[j]=1; st.append(j)
    ci=len(classes)
    for i in cls: class_of[i]=ci
    classes.append(cls)
assert len(classes)==34

def word_for(idx):
    w=[]
    while parent[idx]!=-1: w.append(parent_gen[idx]); idx=parent[idx]
    return list(reversed(w))
def rep_word(w,mats):
    R=I35.copy()
    for gi in w:R=(R@mats[gi])%P
    return R

def order4(T,max_order=5000):
    R=I4.copy()
    for k in range(1,max_order+1):
        R=(R@T)%P
        if np.array_equal(R,I4): return k
    return None

def order35(T,max_order=5000):
    R=I35.copy()
    for k in range(1,max_order+1):
        R=(R@T)%P
        if np.array_equal(R,I35): return k
    return None
x=symbols('x')
def charpoly_F3(T):
    return tuple(int(c)%P for c in Matrix(T.tolist()).charpoly(x).all_coeffs())
def rank_profile(T):
    D=(T-I35)%P; R=D.copy(); out=[]
    for _ in range(35):
        r=rank3(R); out.append(r)
        if r==0: break
        R=(R@D)%P
    return tuple(out)
def jordan1(T):
    rp=rank_profile(T); null=[35]+[35-r for r in rp]
    ge=[null[k]-null[k-1] for k in range(1,len(null))]
    return tuple(ge[k]-(ge[k+1] if k+1<len(ge) else 0) for k in range(len(ge)))

def fp(T): return {'order':order35(T),'charpoly':charpoly_F3(T),'rank_profile':rank_profile(T),'jordan1':jordan1(T)}

rows=[]
for ci,cls in enumerate(classes,1):
    idx=min(cls); w=word_for(idx); Tb=rep_word(w,BA_gens); Tk=rep_word(w,K_gens)
    fb,fk=fp(Tb),fp(Tk); rows.append((ci,len(cls),order4(group[idx]),fb,fk))

char_diff=[r[0] for r in rows if r[3]['charpoly']!=r[4]['charpoly']]
rank_diff=[r[0] for r in rows if r[3]['rank_profile']!=r[4]['rank_profile']]
jordan_diff=[r[0] for r in rows if r[3]['jordan1']!=r[4]['jordan1']]
strong=[r[0] for r in rows if r[3]!=r[4]]
regular=[r for r in rows if r[2]%3!=0]; singular=[r for r in rows if r[2]%3==0]
print('A3-4-16 / STRONG MODULAR FINGERPRINT')
print('group_size =',len(group)); print('conjugacy_classes =',len(classes)); print('module_dimension = 35')
print('3_REGULAR_CLASS_COUNT =',len(regular)); print('3_SINGULAR_CLASS_COUNT =',len(singular))
print('CHARPOLY_DISTINGUISHING_CLASS_COUNT =',len(char_diff))
print('RANK_PROFILE_DISTINGUISHING_CLASS_COUNT =',len(rank_diff))
print('JORDAN_1_DISTINGUISHING_CLASS_COUNT =',len(jordan_diff))
print('STRONG_FINGERPRINT_DISTINGUISHING_CLASS_COUNT =',len(strong))
print('3_REGULAR_CHARPOLY_DISTINGUISHING_CLASSES =',[r[0] for r in regular if r[3]['charpoly']!=r[4]['charpoly']])
print('3_SINGULAR_RANK_PROFILE_DISTINGUISHING_CLASSES =',[r[0] for r in singular if r[3]['rank_profile']!=r[4]['rank_profile']])
print('3_SINGULAR_JORDAN_1_DISTINGUISHING_CLASSES =',[r[0] for r in singular if r[3]['jordan1']!=r[4]['jordan1']])
for r in rows:
    ci,size,go,fb,fk=r
    if fb!=fk:
        print('DISTINGUISHING CLASS',ci,'size=',size,'group_order=',go)
        print('  BA=',fb); print('  K =',fk)
print('NOTE: characteristic polynomials are computed exactly, then reduced mod 3.')
print('NOTE: Jordan-1 data describes the generalized eigenspace for eigenvalue 1; no ordinary-character claim is made in defining characteristic.')
print('ALL A3-4-16 CHECKS COMPLETED')
