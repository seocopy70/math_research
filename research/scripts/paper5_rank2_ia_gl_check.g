LoadPackage("autpgrp");

# Minimal Paper 5 IA/GL check: p=3, rank 2, r=x^3, n=4.
# Compare split/s=0,a=1 against non-split/s=1,a=1.
mkG:=function(s)
  local F;
  F:=FreeGroup("z","x");
  if s=0 then return F/[F.2^3]; fi;
  return F/[F.1^3*F.2^-3];
end;

winW:=function(G,n)
  local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,4); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=J[n];
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return Image(nat);
end;

valuation:=function(N,p) local v; v:=0; while N mod p=0 do N:=N/p; v:=v+1; od; return v; end;

run:=function(s)
  local W,A,fr,V,d,L,IA,glperms,elsV,alpha,imgs,Autorder,report;
  W:=winW(mkG(s),4);
  A:=AutomorphismGroupPGroup(W);
  fr:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W));
  V:=Image(fr); elsV:=AsSortedList(V); d:=LogInt(Size(V),3);
  glperms:=[];
  for alpha in A.glAutos do
    imgs:=List(elsV,v->Image(fr,Image(alpha,PreImagesRepresentative(fr,v))));
    Add(glperms,PermList(List(imgs,v->Position(elsV,v))));
  od;
  if Length(glperms)=0 then L:=TrivialSubgroup(SymmetricGroup(Length(elsV))); else L:=Group(glperms); fi;
  IA:=Group(A.agAutos); Autorder:=A.size;
  report:=rec(s:=s, SizeW:=Size(W), dimV:=d, GLorder:=Size(L), IAorder:=Size(IA),
    AutOrder:=Autorder, v3GL:=valuation(Size(L),3), v3IA:=valuation(Size(IA),3),
    v3Aut:=valuation(Autorder,3), factorization:=(Size(L)*Size(IA)=Autorder),
    agTrivialOnV:=ForAll(A.agAutos,a->ForAll(GeneratorsOfGroup(W),g->Image(fr,Image(a,g))=Image(fr,g))),
    glOrderRecord:=(Size(L)=A.glOrder));
  Print(report,"\n");
end;
run(0); run(1); QUIT;
