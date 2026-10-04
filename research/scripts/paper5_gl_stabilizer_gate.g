LoadPackage("autpgrp");

mkG:=function(s,a) local F;
  F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1];
end;

winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))];
end;

Coord:=function(v,b)
  local i,j,k;
  for i in [0..2] do for j in [0..2] do for k in [0..2] do
    if b[1]^i*b[2]^j*b[3]^k=v then return [i,j,k]; fi;
  od; od; od;
  Error("coordinate not found");
end;

ImageMatrix:=function(alpha,frnat,basis)
  local cols;
  cols:=List(basis,i->Coord(Image(frnat,Image(alpha,basis[i])),basis));
  return TransposedMat(Matrix(GF(3),cols));
end;

CandidateGroups:=function()
  local G,els,G02,G01,G12,G11,m,detA;
  G:=GL(3,3); els:=Elements(G);
  # (s,a)=(0,2): preserve the plane <x,y>.
  G02:=Group(Filtered(els,m->m[3][1]=0 and m[3][2]=0 and m[3][3]<>0));
  # (s,a)=(0,1): preserve <x> inside <x,y> and impose the mixed
  # x^[3] / [x,y] scaling condition, giving y-coefficient 1.
  G01:=Group(Filtered(els,m->m[2][1]=0 and m[3][1]=0 and
                           m[3][2]=0 and m[2][2]=1));
  # (s,a)=(1,2): preserve <x,y>, <z>, and impose z^[3]=[x,y]:
  # z-scalar equals determinant of the 2x2 block.
  G12:=Group(Filtered(els,function(m)
    detA:=DeterminantMat(Submatrix(m,[1,2],[1,2]));
    return m[3][1]=0 and m[3][2]=0 and m[1][3]=0 and
           m[2][3]=0 and m[3][3]=detA;
  end));
  # (s,a)=(1,1): impose the stronger root relation
  # x -> a x, y -> b x+y, z -> a z.
  G11:=Group(Filtered(els,m->m[2][1]=0 and m[3][1]=0 and
                           m[3][2]=0 and m[2][2]=1 and
                           m[1][3]=0 and m[2][3]=0 and
                           m[3][3]=m[1][1]));
  return [G01,G11,G02,G12];
end;

run:=function(s,a)
  local R,W,gens,A,frnat,basis,autGens,Mats,actual,Cands,expected,i,eq;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  # Work in the presentation basis (x,y,z), not an arbitrary PC basis.
  basis:=[Image(frnat,gens[2]),Image(frnat,gens[3]),Image(frnat,gens[1])];
  autGens:=Concatenation(A.glAutos,A.agAutos);
  Mats:=List(autGens,alpha->ImageMatrix(alpha,frnat,basis));
  actual:=Group(Mats);
  Cands:=CandidateGroups();
  expected:=[[0,1],[1,1],[0,2],[1,2]];
  i:=Position(expected,[s,a]); eq:=actual=Cands[i];
  Print("=== Paper5 GL stabilizer gate s=",s," a=",a," ===\n");
  Print("actual image order = ",Size(actual)," candidate order = ",Size(Cands[i]),"\n");
  Print("actual structure = ",StructureDescription(actual),"\n");
  Print("candidate structure = ",StructureDescription(Cands[i]),"\n");
  Print("embedded equality in basis (x,y,z) = ",eq,"\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;
