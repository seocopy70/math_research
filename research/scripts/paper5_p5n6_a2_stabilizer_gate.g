LoadPackage("autpgrp");

P:=5; N:=6; C:=6; Fld:=GF(P);

mkG:=function(s,a) local F;
  F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(P^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^P*(F.2^(P^a)*Comm(F.2,F.3))^-1];
end;

winW:=function(G) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,P,C,2000); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=N then Dn:=J[N]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))];
end;

Coord:=function(v,b)
  local i,j,k;
  for i in [0..P-1] do for j in [0..P-1] do for k in [0..P-1] do
    if b[1]^i*b[2]^j*b[3]^k=v then return [i,j,k]; fi;
  od; od; od;
  Error("coordinate not found");
end;

ImageMatrix:=function(alpha,frnat,basis)
  local cols,j,M;
  cols:=List([1..Length(basis)],j->
    Coord(Image(frnat,Image(alpha,basis[j])),
          List(basis,k->Image(frnat,k))));
  M:=TransposedMat(Matrix(Fld,cols));
  return List([1..3],i->List([1..3],j->M[i][j]));
end;

EMat:=function(i,j,a)
  local m;
  m:=IdentityMat(3,Fld); m[i][j]:=a*One(Fld); return m;
end;

D:=function(i,a)
  local m;
  m:=IdentityMat(3,Fld); m[i][i]:=a*One(Fld); return m;
end;

CandidateGroups:=function()
  local G,G02,G12;
  G:=GL(3,P);
  G02:=Group(EMat(1,2,1),EMat(2,1,1),D(1,2),EMat(1,3,1),EMat(2,3,1),D(3,2));
  G12:=Group(EMat(1,2,1),EMat(2,1,1),[[2*One(Fld),0*One(Fld),0*One(Fld)],[0*One(Fld),One(Fld),0*One(Fld)],[0*One(Fld),0*One(Fld),2*One(Fld)]]);
  return [G02,G12];
end;

MulM:=function(A,B) local C,i,j,k,t;
  C:=List([1..3],i->List([1..3],j->0*One(Fld)));
  for i in [1..3] do for j in [1..3] do
    t:=0*One(Fld);
    for k in [1..3] do t:=t+A[i][k]*B[k][j]; od;
    C[i][j]:=t;
  od; od;
  return C;
end;

KeyM:=function(A)
  return JoinStringsWithSeparator(List(Flat(A),x->String(Int(x))),",");
end;

ClosureKeys:=function(gens)
  local one,seen,queue,A,B,C,key,q;
  one:=IdentityMat(3,Fld); seen:=rec(); key:=ReplacedString(KeyM(one),",","_");
  seen.(key):=true; queue:=[one]; q:=1;
  while q<=Length(queue) do
    A:=queue[q]; q:=q+1;
    for B in gens do
      C:=MulM(A,B); key:=ReplacedString(KeyM(C),",","_");
      if not IsBound(seen.(key)) then seen.(key):=true; Add(queue,C); fi;
    od;
  od;
  return Set(RecNames(seen));
end;

run:=function(s,a)
  local R,W,gens,A,frnat,basis,autGens,Mats,Cands,expected,i,actualKeys,candKeys;
  Print("BUILD W for s=",s," a=",a," ...\n");
  R:=winW(mkG(s,a)); W:=R[1]; gens:=R[2];
  Print("|W|=",Size(W),"\n");
  A:=AutomorphismGroupPGroup(W);
  Print("|Aut(W)|=",A.size," glOrder=",A.glOrder,"\n");
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  basis:=[gens[2],gens[3],gens[1]];
  autGens:=Concatenation(A.glAutos,A.agAutos);
  Mats:=List(autGens,alpha->ImageMatrix(alpha,frnat,basis));
  Cands:=CandidateGroups(); expected:=[[0,2],[1,2]];
  i:=Position(expected,[s,a]);
  actualKeys:=ClosureKeys(Mats);
  candKeys:=Set(List(Elements(Cands[i]),m->ReplacedString(KeyM(m),",","_")));
  Print("candidate order=",Size(Cands[i])," actual GL image=",Length(actualKeys),"\n");
  Print("entrywise equality=",actualKeys=candKeys,"\n");
  if actualKeys<>candKeys then Error("A2 STABILIZER FAILURE"); fi;
  Print("A2_STABILIZER s=",s," a=",a," PASS\n");
end;

for t in [[0,2],[1,2]] do run(t[1],t[2]); od;
Print("P5_A2_STABILIZER_CERTIFICATE=PASS\n");
QUIT;
