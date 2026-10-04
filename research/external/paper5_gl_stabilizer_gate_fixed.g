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

ImageMatrix:=function(alpha,frnat,pre)
  local cols,vb;
  vb:=List(pre,w->Image(frnat,w));
  cols:=List(pre,w->Coord(Image(frnat,Image(alpha,w)),vb));
  return TransposedMat(cols*Z(3)^0);
end;

CandidateGroups:=function()
  local G,els,G02,G01,G12,G11,z,o,detA;
  G:=GL(3,3); els:=Elements(G); z:=Zero(GF(3)); o:=One(GF(3));
  G02:=Group(Filtered(els,m->m[3][1]=z and m[3][2]=z and m[3][3]<>z));
  G01:=Group(Filtered(els,m->m[2][1]=z and m[3][1]=z and
                           m[3][2]=z and m[2][2]=o));
  G12:=Group(Filtered(els,function(m)
    detA:=DeterminantMat(m{[1,2]}{[1,2]});
    return m[3][1]=z and m[3][2]=z and m[1][3]=z and
           m[2][3]=z and m[3][3]=detA;
  end));
  G11:=Group(Filtered(els,m->m[2][1]=z and m[3][1]=z and
                           m[3][2]=z and m[2][2]=o and
                           m[1][3]=z and m[2][3]=z and
                           m[3][3]=m[1][1]));
  return [G01,G11,G02,G12];
end;

run:=function(s,a)
  local R,W,gens,A,frnat,basis,autGens,Mats,actual,Cands,expected,i,eq;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  # Work in the presentation basis (x,y,z), not an arbitrary PC basis.
  basis:=[gens[2],gens[3],gens[1]];
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
