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

MatKey:=function(m) return JoinStringsWithSeparator(List(Flat(m),String),","); end;

W:=winW(mkG(0,1)); W:=W[1];
A:=AutomorphismGroupPGroup(W);
frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
gens:=GeneratorsOfGroup(W);
basis:=[gens[2],gens[3],gens[1]];
autGens:=Concatenation(A.glAutos,A.agAutos);
Mats:=List(autGens,alpha->ImageMatrix(alpha,frnat,basis));

Print("=== p=5 n=6 (s,a)=(0,1) MATRIX DIAGNOSTIC ===\n");
Print("W order=",Size(W)," Aut order=",Size(A)," Frattini quotient order=",Size(Image(frnat)),"\n");
Print("basis order (x,y,z) via gens[2],gens[3],gens[1]\n");
Print("number of aut generators=",Length(Mats),"\n");

for i in [1..Length(Mats)] do
  Print("M[",i,"]=",Mats[i]," det=",DeterminantMat(Mats[i]),"\n");
od;

G01:=Group(D(1,2),EMat(1,2,1),EMat(1,3,1),EMat(2,3,1),D(3,2));
Print("candidate order=",Size(G01)," generators=",GeneratorsOfGroup(G01),"\n");

actual:=Group(List(Mats,m->Matrix(Fld,m)));
Print("actual matrix group order=",Size(actual)," equal candidate=",actual=G01,"\n");

# Compare generated subgroup after all elementary convention transforms.
Variants:=[
  actual,
  Group(List(Mats,m->TransposedMat(m))),
  Group(List(Mats,m->m^-1)),
  Group(List(Mats,m->TransposedMat(m^-1)))
];
Names:=["M","transpose","inverse","transpose-inverse"];
for i in [1..4] do
  Print("variant ",Names[i]," order=",Size(Variants[i])," equals candidate=",Variants[i]=G01,"\n");
od;

Print("candidate generator matrices:\n");
for g in GeneratorsOfGroup(G01) do Print(g,"\n"); od;

# Test the old coordinate permutation convention directly on all vectors.
Vecs:=Elements(Fld^3);
MatPerm:=function(m) return PermList(List(Vecs,v->Position(Vecs,v*m))); end;
Lact:=Group(List(Mats,MatPerm)); Cact:=Group(List(GeneratorsOfGroup(G01),MatPerm));
Print("direct permutation orders actual=",Size(Lact)," candidate=",Size(Cact)," equal=",Lact=Cact,"\n");

QUIT;
