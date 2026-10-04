mk:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;
win:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn); return Image(nat); end;
# exhaustive: r(x',y') depends only on x',y' mod D_{n-1} (since [D_{n-1},G] in D_n=1, (D_{n-1})^3 in D_n)
count:=function(W,n,ap)
  local J,Dm,T,Fr,fnat,A,vec,cnt,x,y,rel,i,j,Tl;
  J:=JenningsSeries(W); Dm:=J[n-1];
  T:=RightTransversal(W,Dm); Tl:=List([1..Length(T)],i->T[i]);
  Fr:=FrattiniSubgroup(W); fnat:=NaturalHomomorphismByNormalSubgroup(W,Fr); A:=Image(fnat);
  vec:=List(Tl,t->Image(fnat,t)); cnt:=0;
  for i in [1..Length(Tl)] do for j in [1..Length(Tl)] do
    if Size(Subgroup(A,[vec[i],vec[j]]))=9 then
      x:=Tl[i]; y:=Tl[j];
      if ap=0 then rel:=Comm(x,y); else rel:=x^(3^ap)*Comm(x,y); fi;
      if IsOne(rel) then cnt:=cnt+1; fi;
    fi; od; od;
  return cnt; end;
n:=4;
for src in [[1,1],[1,2],[2,1],[3,1],[2,2],[0,1]] do
  W:=win(mk(src[1],src[2]),n,4);
  Print("source s=",src[1],"(0=inf) a=",src[2]," |W|=3^",Log(Size(W),3),"  hom-count of W'_{a'}->W (gen pairs, r_{a'}=1):");
  for ap in [0,1,2] do Print("  a'=",ap,":",count(W,n,ap)); od; Print("\n");
od;
QUIT;
