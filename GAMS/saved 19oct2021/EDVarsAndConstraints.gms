*Michael Craig 14 May 2020

Equations
*Generation and reserve constraints
         limitflexres(egu,h)             limit spin reserves by existing plants by ramp rate
         limitcontres(egu,h)             limit cont reserves by existing plants by ramp rate
         limitregupres(egu,h)            limit reg reserves by existing plants by ramp rate
         ;

******************GENERATION AND RESERVE CONSTRAINTS******************
*Limit spining and regulation reserves each to ramp capability and time of reserve
limitflexres(egu,h)$[pMaxflexoffer(egu)>0] .. vFlex(egu,h) =l= pMaxflexoffer(egu);
limitcontres(egu,h)$[pMaxcontoffer(egu)>0] .. vCont(egu,h) =l= pMaxcontoffer(egu);
limitregupres(egu,h)$[pMaxregupoffer(egu)>0] .. vRegup(egu,h) =l= pMaxregupoffer(egu);
**********************************************************************
