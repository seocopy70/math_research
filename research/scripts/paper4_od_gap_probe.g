LoadPackage("anupq");
Print("GAP=", GAPInfo.Version, "\n");
Print("ANUPQ loaded=", LoadPackage("anupq"), "\n");

WindowQuotient := function(p, n, rel)
  local F, H, qs, epi, P, J, N, nat, W;
  F := FreeGroup("z","x1","x2");
  H := F / [ rel ];
  qs := PQuotient(H, p, n-1);
  epi := EpimorphismQuotientSystem(qs);
  P := Image(epi);
  J := JenningsSeries(P);
  N := J[n];
  nat := NaturalHomomorphismByNormalSubgroup(P, N);
  W := Image(nat);
  return rec(W:=W, map:=epi*nat, F:=F);
end;

TestCase := function(name, p, s, rword, d)
  local n, t, F, z, x1, x2, rels, A, B, ws, wt, cA, cB, qB, QA;
  n := p^s + 1;
  t := s+1;
  F := FreeGroup("z","x1","x2"); z:=F.1; x1:=F.2; x2:=F.3;
  if d=2 then
    rword := rword(x1,x2);
  else
    rword := rword(x1);
  fi;
  A := WindowQuotient(p,n,z^(p^s)*rword^(-1));
  B := WindowQuotient(p,n,z^(p^t)*rword^(-1));
  ws := A.W; wt := B.W;
  cA := Image(A.map,z^(p^s));
  cB := Image(B.map,z^(p^s));
  qB := NormalClosure(wt,Subgroup(wt,[cB]));
  QA := FactorGroup(wt,qB);
  Print("\\nCASE ",name," p=",p," s=",s," n=",n," d=",d,"\\n");
  Print("|W_s|=",Size(ws)," |W_t|=",Size(wt)," ratio=",Size(wt)/Size(ws),"\\n");
  Print("ord(c in W_s)=",Order(cA)," ord(c in W_t)=",Order(cB)," |Q|=",Size(QA),"\\n");
end;

TestCase("S-x3",3,1,function(x1) return x1^3; end,1);
TestCase("N-x9",3,1,function(x1) return x1^9; end,1);
TestCase("S-comm",3,1,function(x1,x2) return Comm(x1,x2); end,2);
QUIT;
