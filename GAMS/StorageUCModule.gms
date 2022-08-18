*Michael Craig 14 May 2020

Equations
*Limit rate of charging
		 limitcharging(storageegu,h)
*Limit reserve provision
		 limitregupstoragetoramp(storageegu,h)
		 limitflexstoragetoramp(storageegu,h)
		 limitcontstoragetoramp(storageegu,h)
*Limit storage generation plus up reserves
		 limitstorageresup(storageegu,h)
		;

*RATE OF CHARGE CONSTRAINT
*Limit rate of charging, and constrain charging to when storage unit is off (or not discharging)
limitcharging(storageegu,h) .. vCharge(storageegu,h) =l= pCapaccharge(storageegu) * (1 - vOnoroff(storageegu,h));

*RESERVE CONSTRAINTS
*Limit reg up and down and spin to ramp capabilities and market participation. Assume ramp rate is same for charging and generation
limitregupstoragetoramp(storageegu,h) .. vRegup(storageegu,h) =l= pMaxregupoffer(storageegu);
limitflexstoragetoramp(storageegu,h) .. vFlex(storageegu,h) =l= pMaxflexoffer(storageegu);
limitcontstoragetoramp(storageegu,h) .. vCont(storageegu,h) =l= pMaxcontoffer(storageegu);

*Limit reg up to spare capacity while discharging & to charge amount while charging
limitstorageresup(storageegu,h) .. vRegup(storageegu,h) + vFlex(storageegu,h) + vCont(storageegu,h) =l= (vOnoroff(storageegu,h)*pCapac(storageegu)
                                                                                                         - vGen(storageegu,h)) + vCharge(storageegu,h);