LoadPackage("anupq");
Print("GAP=", GAPInfo.Version, "\n");
Print("ANUPQ loaded=", LoadPackage("anupq"), "\n");

WindowQuotient := function(p, n, relfun)
  local F, z, x1, x2, H, qs, epi, P, J, N, nat, W, rel;
  F := FreeGroup("z","x1","x2"); z:=F.1; x1:=F.2; x2:=F.3;
  rel := relfun(z,x1,x2);
  H := F / [ rel ];
  qs := PQuotient(H, p, n-1);
  epi := EpimorphismQuotientSystem(qs);
  P := Image(epi);
  J := JenningsSeries(P);
  N := J[n];
  nat := NaturalHomomorphismByNormalSubgroup(P, N);
  W := Image(nat);
  return rec(W:=W, map:=CompositionMapping(epi,nat), F:=F);
end;

TestCase := function(name, p, s, relfun)
  local n, t, A, B, ws, wt, z, cA, cB, qB, QA;
  n := p^s + 1; t := s+1;
  A := WindowQuotient(p,n,function(z,x1,x2) return z^(p^s)*relfun(x1,x2)^(-1); end);
  B := WindowQuotient(p,n,function(z,x1,x2) return z^(p^t)*relfun(x1,x2)^(-1); end);
  ws := A.W; wt := B.W; z := A.F.1;
  cA := Image(A.map,z^(p^s));
  z := B.F.1; cB := Image(B.map,z^(p^s));
  qB := NormalClosure(wt,Subgroup(wt,[cB]));
  QA := FactorGroup(wt,qB);
  Print("\nCASE ",name," p=",p," s=",s," n=",n,"\n");
  Print("|W_s|=",Size(ws)," |W_t|=",Size(wt)," ratio=",Size(wt)/Size(ws),"\n");
  Print("ord(c in W_s)=",Order(cA)," ord(c in W_t)=",Order(cB)," |Q|=",Size(QA),"\n");
end;

TestCase("S-x3",3,1,function(x1,x2) return x1^3; end);
TestCase("N-x9",3,1,function(x1,x2) return x1^9; end);
TestCase("S-comm",3,1,function(x1,x2) return Comm(x1,x2); end);
QUIT;
