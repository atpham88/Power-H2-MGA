*Michael Craig 14 May 2020

Equations
*Limit storage generation plus up reserves
		 limitstorageresup(storageegu,h)
		;
		
******************STORAGE CONSTRAINTS*********************************
*Limit up reserves to spare capacity while discharging & to charge amount while charging
limitstorageresup(storageegu,h) .. vRegup(storageegu,h) + vFlex(storageegu,h) + vCont(storageegu,h) =l= (pCapac(storageegu) - vGen(storageegu,h)) + vCharge(storageegu,h);
**********************************************************************