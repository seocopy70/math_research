LoadPackage("autpgrp");

P:=5; N:=6; C:=5; Fld:=GF(P);

mkG:=function(s,a) local F;
  F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(P^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^P*(F.2^(P^a)*Comm(F.2,F.3))^-1];
end;

winW:=function(G) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,P,C); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
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
  local G,G02,G01,G12,G11;
  G:=GL(3,P);
  G02:=Group(EMat(1,2,1),EMat(2,1,1),D(1,2),EMat(1,3,1),EMat(2,3,1),D(3,2));
  G01:=Group(D(1,2),EMat(1,2,1),EMat(1,3,1),EMat(2,3,1),D(3,2));
  G12:=Group(EMat(1,2,1),EMat(2,1,1),D(1,2),D(3,2));
  G11:=Group(D(1,2),EMat(1,2,1));
  return [G01,G11,G02,G12];
end;

run:=function(s,a)
  local R,W,gens,A,frnat,basis,autGens,Mats,actual,Cands,expected,i,eq,nontriv;
  R:=winW(mkG(s,a)); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  basis:=[gens[2],gens[3],gens[1]];
  autGens:=Concatenation(A.glAutos,A.agAutos);
  Mats:=List(autGens,alpha->ImageMatrix(alpha,frnat,basis));
  if ForAny(Mats,m->DeterminantMat(m)=0) then
    Error("non-invertible Frattini action matrix");
  fi;
  nontriv:=Filtered(Mats,m->m<>IdentityMat(3,Fld));
  actual:=CallFuncList(Group,nontriv);
  Cands:=CandidateGroups();
  expected:=[[0,1],[1,1],[0,2],[1,2]];
  i:=Position(expected,[s,a]); eq:=actual=Cands[i];
  Print("=== Paper5 p=5,n=6 GL stabilizer gate s=",s," a=",a," ===\n");
  Print("actual image order = ",Size(actual)," candidate order = ",Size(Cands[i]),"\n");
  Print("embedded equality in basis (x,y,z) = ",eq,"\n");
  if not eq then Error("STABILIZER equality failure"); fi;
  Print("STABILIZER p=5 s=",s," a=",a," PASS\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
Print("STABILIZER_P5_CERTIFICATE=PASS\n");
QUIT;
