Sets
       i   regions (or flows away from region)   / MISO, PJM /
       lp  physical line / mpLine /
fMap(i, lp) / ("MISO", "PJM").mpLine /;

Parameters
       a(i)  capacity of plant in regions
         /    MISO    200
              PJM     600  /
       b(i)  demand at regions
         /    MISO    100
              PJM     700  / ;

Scalar d  current transmission capacity  /10/;
Scalar c  cost of expanding 1 MW of line  /100/ ;
Scalar g  cost operation generation  /30/ ;

Variables
     x(i)  generation
     y(i)  flows
     l     new capacity built
     z     total transmission cost ;
Positive variables x,l;
Equations
     cost        objective function
     supply(i)   supply limit at plant i
     demand(i)   satisfy demand
     flow(i)     flow constrains
     flow_bal     flow balance   ;
cost ..        z  =e=  c*l+sum(i, g*x(i)) ;
supply(i) ..   x(i)  =l=  a(i) ;
*flow(i) ..  y(i)  =l=  d(i) + l(i-1)+ l(i)$(ord(i)>=2) ;
flow(i) ..  y(i)  =l=  sum(fMap(i,lp), d + l);
demand(i) ..   x(i) - y(i)  =e=  b(i) ;
flow_bal..  sum(i, y(i)) =e= 0;
Model toyMod /all/ ;
Solve toyMod using lp minimizing z ;


