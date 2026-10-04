LoadPackage("autpgrp");
mkG:=function(s) local F; F:=FreeGroup("z","x"); if s=0 then return F/[F.2^3]; fi; return F/[F.1^3*F.2^-3]; end;
winW:=function(G) local qs,epi,H,J,Dn,nat; qs:=PQuotient(G,3,4); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi); J:=JenningsSeries(H); Dn:=J[4]; nat:=NaturalHomomorphismByNormalSubgroup(H,Dn); return Image(nat); end;
valuation:=function(N,p) local v; v:=0; while N mod p=0 do N:=N/p; v:=v+1; od; return v; end;
run:=function(s) local W,A,B,fr,V,elsV,d,autgens,perms,L,act,IA,alpha,imgs;
 W:=winW(mkG(s)); A:=AutomorphismGroupPGroup(W); B:=ConvertHybridAutGroup(A); fr:=NaturalHomomorphismByNormalSubgroup(W,FrattiniSubgroup(W)); V:=Image(fr); elsV:=AsSortedList(V); d:=LogInt(Size(V),3); autgens:=GeneratorsOfGroup(B); perms:=List(autgens,alpha->PermList(List(elsV,v->Position(elsV,Image(fr,Image(alpha,PreImagesRepresentative(fr,v))))))); L:=Group(perms); act:=GroupHomomorphismByImages(B,L,autgens,perms); IA:=Kernel(act); Print(rec(s:=s,SizeW:=Size(W),dimV:=d,GLorder:=Size(L),IAorder:=Size(IA),AutOrder:=Size(B),v3GL:=valuation(Size(L),3),v3IA:=valuation(Size(IA),3),v3Aut:=valuation(Size(B),3),factorization:=(Size(L)*Size(IA)=Size(B)),glOrderRecord:=A.glOrder,solublePartOrder:=Product(A.agOrder)),"\n"); end;
run(0); run(1); QUIT;
