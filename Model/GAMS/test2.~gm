Set i /NYBOS, NYDC, BOSNY, DCNY/;
Alias (i,ii);

Parameter
h(i)
o(i)     origin of trip
/NYBOS 1, NYDC 1, BOSNY 2, DCNY 3/
e(i)     destination of trip
/NYBOS 2, NYDC 3, BOSNY 1, DCNY 1/;


Display i,o,e;

Variable z, g(i);

Equation dummy, k(i,ii);

dummy.. z =e= 1;
k(i,ii)$(o(i)=e(ii) and o(ii)=e(i)).. g(i) =e= g(ii);
*k(i).. g(i)$(ORD(i)=1) - g(i)$(ORD(i)=3) =e= 0;
*k(i).. g(i)$(ord(i)>=3) =e= g(i-2)
*k(i).. sum((i,ii)$[o(i)=e(ii) and o(ii)=e(i)],g(ii)) =e= 0
*k(i).. sum((i,ii),g(ii)) =e= 0
*k(i).. g(i)$(ord(i)>=3) + g(i-2) =e= 0
*k(i).. g(i) + g(i-2) =e= 0
option LimRow = 10;
model m /all/;
solve m min z use lp;
