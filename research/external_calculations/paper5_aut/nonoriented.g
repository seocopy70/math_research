# Does the window detect the amalgam index s when D has NO orientation (non-PD one-relator group)?
# D1 = <x,y|x^q[x,y]> (Demuskin, control)   D2 = <x,y,w | x^q [y,w]> (rank 3, not Demuskin)
mkG:=function(s,which,a)
  local F,z,x,y,w,r;
  if which=1 then F:=FreeGroup("z","x","y"); z:=F.1;x:=F.2;y:=F.3; r:=x^(3^a)*Comm(x,y);
  else F:=FreeGroup("z","x","y","w"); z:=F.1;x:=F.2;y:=F.3;w:=F.4; r:=x^(3^a)*Comm(y,w); fi;
  return F/[z^(3^s)*r^-1]; end;
mkD:=function(which,a)
  local F,x,y,w,r;
  if which=1 then F:=FreeGroup("x","y"); x:=F.1;y:=F.2; r:=x^(3^a)*Comm(x,y);
  else F:=FreeGroup("x","y","w"); x:=F.1;y:=F.2;w:=F.3; r:=x^(3^a)*Comm(y,w); fi;
  return F/[r]; end;
winOf:=function(G,n,c) local qs,epi,H,J,Dn,nat;
  qs:=PQuotient(G,3,c); epi:=EpimorphismQuotientSystem(qs); H:=Image(epi);
  J:=JenningsSeries(H); Dn:=TrivialSubgroup(H); if Length(J)>=n then Dn:=J[n]; fi;
  nat:=NaturalHomomorphismByNormalSubgroup(H,Dn);
  return [Image(nat), Image(nat,Image(epi,G.1))]; end;
test:=function(s,which,a,n,c)
  local G,R,W,zz,K,KK,N,nat2,E,KE,iso,comp,Dw,Q;
  G:=mkG(s,which,a); R:=winOf(G,n,c); W:=R[1]; zz:=R[2];
  K:=NormalClosure(W,Subgroup(W,[zz])); KK:=DerivedSubgroup(K);
  nat2:=NaturalHomomorphismByNormalSubgroup(W,KK); E:=Image(nat2); KE:=Image(nat2,K);
  iso:=IsomorphismPcGroup(E); E:=Image(iso); KE:=Image(iso,KE);
  Dw:=winOf(mkD(which,a),n,c+3)[1];
  comp:=ComplementClassesRepresentatives(E,KE);
  Print("rank ",which," s=",s," a=",a," n=",n," pclass=",c," |W|=3^",Log(Size(W),3),
        " |Q|=3^",Log(Size(W)/Size(K),3)," (indep 3^",Log(Size(Dw),3),")",
        " K^ab=",AbelianInvariants(KE)," complements=",Length(comp),"\n");
end;
test(1,1,1,4,3);   # control: Demuskin rank 2, s=1, n=4 : expected nonsplit
test(1,2,1,4,3);   # rank 3 non-Demuskin, s=1, n=4
test(1,2,1,3,3);   # rank 3, n=3 <= p^s : expected split
QUIT;
