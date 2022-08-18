*Michael Craig 14 May 2020

Sets
		nonstorageegu(egu)
		;

alias(h,hh);

Parameters
*Commitment parameters
         pMinload(egu)                           "minimum load of EGU (GW)"
         pStartupfixedcost(egu)                  "start up cost of EGU (thousands$)"
         pMindowntime(egu)                       "MDT (hours)"
                 ;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load pMinload, pStartupfixedcost, pMindowntime
$gdxin

*DEFINE GENERATORS THAT ARE NOT STORAGE UNITS
nonstorageegu(egu) = not storageegu(egu);

Positive Variables
         vGenabovemin(egu,h)                     "power generation above minimum stable load (GW)"
         vTurnoff(egu,h)                         "indicates whether plant decides to turn off (1) or not (0) in hour h"
                 ;

Binary Variables
         vTurnon(egu,h)                          "indicates whether plant decides to turn on (1) or not (0) in hour h"
         vOnoroff(egu,h)                         "indicates whether plant is up (1) or down (0) in hour h"
                 ;

Equations
*Differentiate between generation and generation above min load
         definegenabovemin(egu,h)                "establish relationship between Gen (total gen) and Genabovemin (gen just above min stable load)"
         determineloadabovemin(egu,h)            "determine what each thermal unit's generation is above its minimum load. Constraints Genabovemin to be between max and min capacity"
*Cap reserve provision based on off status
         limitregupres(egu,h)                  "limit reg reserves provided by generator to multiple of ramp rate"
         limitcontres(egu,h)
         limitflexres(egu,h)                 "limit spin reserves provided by generator to multiple of ramp rate"
                  ;

******************GENERATION CONSTRAINTS******************
*Constrain plants to generate below their max capacity
definegenabovemin(egu,h).. vGen(egu,h) =e= vOnoroff(egu,h)*pMinload(egu)+vGenabovemin(egu,h);

*Establish relationship between gen above min load, gen output, and min load
determineloadabovemin(egu,h) .. vGenabovemin(egu,h) =l= (pCapac(egu)-pMinload(egu))*vOnoroff(egu,h);
**********************************************************

******************RESERVE PROVISION CONSTRAINTS******************
*Spin and reg reserves limited by ramp rate
limitregupres(nonstorageegu,h)$[pMaxregupoffer(nonstorageegu)>0] .. vRegup(nonstorageegu,h) =l= pMaxregupoffer(nonstorageegu)*vOnoroff(nonstorageegu,h);
limitflexres(nonstorageegu,h)$[pMaxflexoffer(nonstorageegu)>0] .. vFlex(nonstorageegu,h) =l= pMaxflexoffer(nonstorageegu)*vOnoroff(nonstorageegu,h);
limitcontres(nonstorageegu,h)$[pMaxcontoffer(nonstorageegu)>0] .. vCont(nonstorageegu,h) =l= pMaxcontoffer(nonstorageegu)*vOnoroff(nonstorageegu,h);
*****************************************************************
