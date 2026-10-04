LoadPackage("autpgrp");
mkG:=function(s,a) local F; F:=FreeGroup("z","x","y");
  if s=0 then return F/[(F.2^(3^a)*Comm(F.2,F.3))]; fi;
  return F/[F.1^(3^s)*(F.2^(3^a)*Comm(F.2,F.3))^-1]; end;
mkD:=function(a) local F; F:=FreeGroup("x","y"); return F/[F.1^(3^a)*Comm(F.1,F.2)]; end;
winW:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat),List(GeneratorsOfGroup(G),g->Image(nat,Image(epi,g)))]; end;
# set of epimorphisms W(s,a) -> Q_a(4) as triples (pi z, pi x, pi y)
epis:=function(s,a,Q)
  local els,Fr,fn,A,vec,res,b,c,rv,i,j,k,pw;
  els:=AsList(Q); Fr:=FrattiniSubgroup(Q); fn:=NaturalHomomorphismByNormalSubgroup(Q,Fr); A:=Image(fn);
  res:=[];
  pw:=List(els,e->e^(3^s));
  for j in [1..Length(els)] do for k in [1..Length(els)] do
    b:=els[j]; c:=els[k];
    if Size(Subgroup(A,[Image(fn,b),Image(fn,c)]))=Size(A) then
      rv:=b^(3^a)*Comm(b,c);
      if s=0 then for i in [1..Length(els)] do Add(res,[els[i],b,c]); od;
      else for i in [1..Length(els)] do if pw[i]=rv then Add(res,[els[i],b,c]); fi; od; fi;
    fi;
  od; od; return res; end;
Print("loaded\n");
