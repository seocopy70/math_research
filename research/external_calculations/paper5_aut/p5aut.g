LoadPackage("autpgrp");
mkG:=function(p,s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(p^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(p^s)*(F.2^(p^a)*Comm(F.2,F.3))^-1]; end;
winW:=function(p,G,n,c) local qs,epi,H,J,Dn,nat; qs:=PQuotient(G,p,c,2000); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi); J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi; nat:=NaturalHomomorphismByNormalSubgroup(H,Dn); return Image(nat); end;
p:=5; n:=6; for t in [[0,1],[1,1],[2,1],[1,2],[0,2]] do tm:=Runtime(); W:=winW(p,mkG(p,t[1],t[2]),n,6); A:=AutomorphismGroupPGroup(W); Print("p=5 n=6 s=",t[1]," a=",t[2]," |W|=5^",Log(Size(W),5)," |Aut|=",Collected(Factors(A.size))," time ",(Runtime()-tm)/1000.0,"s\n"); od; QUIT;
