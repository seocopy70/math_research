"""Phase 2-8: identify M=ker(N)/im(N) with L(2,1).

Independent model: ATLAS 25-dimensional GF(3) representation of U4(2)
~= PSp4(3). The same five Sp4(F3) transvections are mapped through
Sp4/Z -> U4(2), then into the ATLAS 25D module. Finally solve
P A_i^M = A_i^L P over F3 and require rank(P)=25.

Memory-safe revision: GAP is started with an explicit multi-gigabyte
workspace (-m 4g). The previous run stopped at GAP's pre-set memory limit
before the actual intertwiner calculation; this revision changes only the
GAP workspace allocation, not the mathematical computation.
"""
from pathlib import Path
import runpy, subprocess, ast
import numpy as np

P=3
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts'/'phase2_8_B_L21'; OUT.mkdir(parents=True,exist_ok=True)

# Phase 2-7 exports the exact quotient matrices MA when executed with runpy.
ns=runpy.run_path(str(ROOT/'research/phase2_7_M_quotient_2026-09-15.py'))
MA=[np.array(x,dtype=np.int64)%P for x in ns['MA']]
assert len(MA)==5 and all(x.shape==(25,25) for x in MA)

def rank3(M):
    M=np.array(M,dtype=np.int64,copy=True)%P
    m,n=M.shape; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if M[i,c]),None)
        if q is None: continue
        M[[r,q]]=M[[q,r]]
        if M[r,c]==2: M[r]=(2*M[r])%P
        for i in range(m):
            if i!=r and M[i,c]: M[i]=(M[i]-M[i,c]*M[r])%P
        r+=1
        if r==m: break
    return r

def null3(M):
    M=np.array(M,dtype=np.int64,copy=True)%P
    m,n=M.shape; piv=[]; r=0
    for c in range(n):
        q=next((i for i in range(r,m) if M[i,c]),None)
        if q is None: continue
        M[[r,q]]=M[[q,r]]
        if M[r,c]==2: M[r]=(2*M[r])%P
        for i in range(m):
            if i!=r and M[i,c]: M[i]=(M[i]-M[i,c]*M[r])%P
        piv.append(c); r+=1
        if r==m: break
    out=[]
    for f in [j for j in range(n) if j not in piv]:
        x=np.zeros(n,dtype=np.int64); x[f]=1
        for rr,c in enumerate(piv): x[c]=(-M[rr,f])%P
        out.append(x)
    return out

# Exactly the same five transvections used in Phase 2-1/2-6.
gens4=[
[[1,2,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
[[1,0,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]],
[[1,0,0,0],[0,1,0,0],[0,0,1,2],[0,0,0,1]],
[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,1]],
[[1,2,0,2],[0,1,0,0],[0,2,1,2],[0,0,0,1]],]

gapout=OUT/'L21_generators.pydata'
gap=OUT/'build_L21.g'
gens='['+','.join('Matrix(F,%s)'%repr(x) for x in gens4)+']'
gap.write_text(f'''LoadPackage("atlasrep");;
F:=GF(3);; g4:={gens};; H:=Group(g4);;
Z:=Subgroup(H,[-One(g4[1])]);; nat:=NaturalHomomorphismByNormalSubgroup(H,Z);; Pbar:=Image(nat);;
G0:=AtlasGroup("U4(2)");; iso:=IsomorphismGroups(Pbar,G0);;
info:=OneAtlasGeneratingSetInfo("U4(2)",Characteristic,3,Dimension,25);;
a25:=AtlasGenerators(info.identifier);; G25:=Group(a25.generators);;
phi:=GroupHomomorphismByImages(G0,G25,GeneratorsOfGroup(G0),a25.generators);;
Print("SIZE_H=",Size(H)," SIZE_PBAR=",Size(Pbar)," SIZE_G0=",Size(G0),"\\n");;
Print("ISO_EXISTS=",iso<>fail," ATLAS25_EXISTS=",info<>fail," SIZE_G25=",Size(G25),"\\n");;
out:=OutputTextFile("{gapout}",false);;
PrintTo(out,"L21gens=[");;
for i in [1..5] do t:=Image(iso,Image(nat,g4[i]));; m:=Image(phi,t);; PrintTo(out,String(List(m,x->List(x,y->IntFFE(y)))),",");; od;;
PrintTo(out,"]");; CloseStream(out);; QUIT;
''',encoding='utf-8')

# The previous run hit GAP's pre-set workspace limit. 4 GiB is comfortably
# below the GitHub runner's available RAM and leaves the mathematical code
# unchanged. GAP documents -m as the startup workspace allocation option.
proc=subprocess.run(['gap','-q','-m','4g',str(gap)],capture_output=True,text=True)
print(proc.stdout,end=''); print(proc.stderr,end='')
if proc.returncode: raise SystemExit(proc.returncode)

raw=gapout.read_text(encoding='utf-8')
L21=np.array(ast.literal_eval(raw.split('=',1)[1]),dtype=np.int64)%P
assert L21.shape==(5,25,25)

# Solve P A_i^M = A_i^L P simultaneously over F3.
blocks=[]; I=np.eye(25,dtype=np.int64)
for am,al in zip(MA,L21):
    blocks.append((np.kron(am.T,I)-np.kron(I,al))%P)
Sys=np.vstack(blocks)%P
ker=null3(Sys)
homdim=len(ker); full=False; witness=None
for v in ker:
    Q=v.reshape(25,25)%P
    if rank3(Q)==25:
        full=True; witness=Q; break

print('PHASE 2-8 / M versus ATLAS L(2,1)')
print('dim M = 25')
print('ATLAS model dimension =',L21.shape[1])
print('intertwiner system shape =',Sys.shape)
print('dim Hom_H(M,L(2,1)) =',homdim)
print('full-rank intertwiner found =',full)
print('rank(P) =',rank3(witness) if witness is not None else 0)
print('CONCLUSION:', 'M ~= L(2,1) PROVED' if full else 'identification remains open')

(OUT/'result.txt').write_text('\n'.join([
'Phase 2-8 B certification',
f'INTERTWINER_DIM={homdim}',
f'FULL_RANK={full}',
f'RANK_P={rank3(witness) if witness is not None else 0}',
'M ~= L(2,1) PROVED' if full else 'M ~= L(2,1) NOT PROVED'])+'\n',encoding='utf-8')
