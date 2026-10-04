mkg:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if a=0 then return F/[F.1^(3^s)*Comm(F.2,F.3)^-1]; fi;   # r=[x,y]
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;
win:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn); return Image(nat); end;
count3:=function(W,n,ap)   # relation z^3 = r_{ap}(x,y)
  local J,Dm,T,Tl,Fr,fnat,A,vec,cubes,cnt,i,j,k,x,y,rv,pos;
  J:=JenningsSeries(W); Dm:=J[n-1];
  T:=RightTransversal(W,Dm); Tl:=List([1..Length(T)],i->T[i]);
  Fr:=FrattiniSubgroup(W); fnat:=NaturalHomomorphismByNormalSubgroup(W,Fr); A:=Image(fnat);
  vec:=List(Tl,t->Image(fnat,t)); cubes:=List(Tl,t->t^3); cnt:=0;
  for i in [1..Length(Tl)] do for j in [1..Length(Tl)] do
    if Size(Subgroup(A,[vec[i],vec[j]]))=9 then
      x:=Tl[i]; y:=Tl[j];
      if ap=0 then rv:=Comm(x,y); else rv:=x^(3^ap)*Comm(x,y); fi;
      for k in [1..Length(Tl)] do
        if cubes[k]=rv and Size(Subgroup(A,[vec[i],vec[j],vec[k]]))=27 then cnt:=cnt+1; fi;
      od;
    fi; od; od;
  return cnt; end;
n:=4;
for src in [[1,1],[1,2],[1,0]] do
  W:=win(mkg(src[1],src[2]),n,4);
  Print("source s=1 a=",src[2]," (0=inf) |W|=3^",Log(Size(W),3),": triples for z^3=r_{a'}:");
  for ap in [0,1,2] do Print(" a'=",ap,":",count3(W,n,ap)); od; Print("\n");
od;
QUIT;
