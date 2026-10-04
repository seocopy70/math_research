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
  local R,W,gens,A,frnat,V,elsV,autGens,autImages,L,fixed,
        projReps,projPos,projPerms,p,im,j,k,PP,porb;
  R:=winW(mkG(s,a),4,4); W:=R[1]; gens:=R[2];
  A:=AutomorphismGroupPGroup(W);
  frnat:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(frnat); elsV:=AsSortedList(V);
  autGens:=Concatenation(A.glAutos,A.agAutos);
  autImages:=List(autGens,alpha->permOnV(alpha,frnat,elsV));
  L:=Group(autImages);
  fixed:=Filtered([1..Length(elsV)],i->elsV[i]<>One(V) and ForAll(GeneratorsOfGroup(L),p->i^p=i));

  projReps:=Filtered([1..Length(elsV)],i->elsV[i]<>One(V) and i<=Position(elsV,elsV[i]^-1));
  projPos:=function(i) return Position(projReps,i); end;
  projPerms:=[];
  for p in autImages do
    Add(projPerms,PermList(List(projReps,i->
      j:=Position(elsV,Image(p,elsV[i]));
      k:=Position(elsV,elsV[j]^-1);
      projPos(if j<k then j else k fi)
    )));
  od;
  PP:=Group(projPerms);
  porb:=Orbits(PP,[1..Length(projReps)]);

  Print("=== projective GL audit s=",s," a=",a," ===\n");
  Print("|L|=",Size(L)," fixedNonzeroVectors=",Length(fixed),
        " projectiveOrbits=",List(porb,Length),
        " fixedProjectiveLines=",Length(Filtered(porb,o->Length(o)=1)),"\\n");
end;

for t in [[0,1],[1,1],[0,2],[1,2]] do run(t[1],t[2]); od;
QUIT;

# trigger projective audit
