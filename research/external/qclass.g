mkD:=function(a) local F; F:=FreeGroup("x","y");
  if a=0 then return F/[Comm(F.1,F.2)]; fi;
  return F/[F.1^(3^a)*Comm(F.1,F.2)]; end;
winD:=function(a,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(mkD(a),3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn); return Image(nat); end;
for n in [4,10] do
  Q:=List([0,1,2,3],a->winD(a,n,8));
  Print("n=",n," |Q_a| (a=inf,1,2,3): ",List(Q,q->Log(Size(q),3)),"\n");
  for i in [1..4] do for j in [i+1..4] do
    Print("  a=",[0,1,2,3][i]," vs a=",[0,1,2,3][j]," isomorphic: ",IsomorphismGroups(Q[i],Q[j])<>fail,"\n");
  od; od;
od;
QUIT;
