LoadPackage("autpgrp");
mkG:=function(p,s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(p^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(p^s)*(F.2^(p^a)*Comm(F.2,F.3))^-1]; end;
winW:=function(p,G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,p,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn); return Image(nat); end;
autord:=function(W) local A; A:=AutomorphismGroupPGroup(W); return Collected(Factors(A.size)); end;
Print("p=3, n=4 (s=0 means split-type r=1, a'=a):\n");
for t in [[1,1],[1,2],[2,1],[3,1],[2,2],[0,1],[0,2]] do
  W:=winW(3,mkG(3,t[1],t[2]),4,4);
  Print("  s=",t[1]," a=",t[2]," |W|=3^",Log(Size(W),3)," |Aut|=",autord(W),"\n");
od;
QUIT;
