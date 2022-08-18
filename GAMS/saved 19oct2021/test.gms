Set i /i1*i10/;
Alias (i,ii);

Variable z, g(i);

Equation dummy, e(i);

dummy.. z =e= 1;
e(i)$(mod(ord(i),2)=1).. sum(ii$((ord(ii)>=ord(i) and (ord(ii)<=ord(i)+2))), g(ii)) =e= 0;

option LimRow = 10;
model m /all/;
solve m min z use lp;