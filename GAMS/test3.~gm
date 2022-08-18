Sets
       i   regions   / MISO, PJM /
Parameters
       a(i)  capacity of plant in regions
         /    MISO    200
              PJM     600  /
       b(i)  demand at regions
         /    MISO    300
              PJM     500  /;
Alias (i,ii);
Table  d(i,ii)  transmission capacity
                  MISO       PJM
    MISO           0         50
    PJM           50         0        ;
Scalar f  cost of expanding 1 MW of line  /100/ ;
Scalar g  cost operation generation  /30/ ;
Parameter
       c(i,ii)  transmission cost ;
c(i,ii) = f * d(i,ii);
Variables
     x(i)     generation
     y(i,ii)  flows
     l(i,ii)  new capacity built
     z        total transmission cost ;
Positive variables x,y;
Equations
     cost        objective function
     supply(i)   supply limit at plant i
     demand(i)   satisfy demand
     flow(i,ii)   flow constrains;
cost ..        z  =e=  sum((i,ii), f*l(i,ii))+sum(i, g*x(i)) ;
supply(i) ..   x(i)  =l=  a(i) ;
flow(i,ii) ..  y(i,ii)  =l=  d(i,ii) + l(i,ii) ;
demand(i) ..   x(i) + sum(ii,y(i,ii))  =g=  b(i) ;
Model toyMod /all/ ;
Solve toyMod using lp minimizing z ;