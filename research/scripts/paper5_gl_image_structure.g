LoadPackage("autpgrp");

mkG:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;

winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))]; end;

permOnV:=function(alpha,frnat,elsV)
  local imgs;
  imgs:=List(elsV,v->Image(frnat,Image(alpha,PreImagesRepresentative(frnat,v))));
  return PermList(List(imgs,v->Position(elsV,v)));
end;

run:=function(s,a)
  local R,W,gens,A,frnat,V,elsV,autGens,autImages,L,orb,nonzero,
        nonzeroOrbits,rep,stab,DS;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat); elsV:=AsSortedList(V);
  autGens:=Concatenation(A.glAutos,A.agAutos);
  autImages:=List(autGens,alpha->permOnV(alpha,frnat,elsV));
  L:=Group(autImages);
  orb:=Orbits(L,[1..Length(elsV)]);
  nonzero:=Filtered([1..Length(elsV)],i->elsV[i]<>One(V));
  nonzeroOrbits:=Orbits(L,nonzero);
  Print("=== GL image structure s=",s," a=",a," ===\n");
  Print("order=",Size(L)," structure=",StructureDescription(L)," id=",IdGroup(L),"\n");
  Print("centerOrder=",Size(Centre(L))," derivedOrder=",Size(DerivedSubgroup(L))," exponent=",Exponent(L),"\n");
  Print("allOrbitSizes=",List(orb,Length)," nonzeroOrbitSizes=",List(nonzeroOrbits,Length),"\n");
  for rep in List(nonzeroOrbits,o->o[1]) do
    stab:=Stabilizer(L,rep);
    Print("repIndex=",rep," stabilizerOrder=",Size(stab),"\n");
  od;
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;
