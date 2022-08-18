Sets
	block0h(h)
	block1h(h)
	blockpeaktotal2h(h)
	blockpeaknet3h(h)
	block4h(h)
	block5h(h)
	blockpeaknetramp6h(h)
	;

Parameters
	pWeightblock0h
	pWeightblock1h
	pWeightblockpeaktotal2h
	pWeightblockpeaknet3h
	pWeightblock4h
	pWeightblock5h
	pWeightblockpeaknetramp6h
	pHourInitblock0h
	pHourFinalblock0h
	pInitSOCblock0h(storageegu)
	pInitSOCblock0htech(storagetech)
	pHourInitblock1h
	pHourFinalblock1h
	pSOCScalarblock1h
	pHourInitblockpeaktotal2h
	pHourFinalblockpeaktotal2h
	pSOCScalarblockpeaktotal2h
	pHourInitblockpeaknet3h
	pHourFinalblockpeaknet3h
	pSOCScalarblockpeaknet3h
	pHourInitblock4h
	pHourFinalblock4h
	pSOCScalarblock4h
	pHourInitblock5h
	pHourFinalblock5h
	pSOCScalarblock5h
	pHourInitblockpeaknetramp6h
	pHourFinalblockpeaknetramp6h
	pSOCScalarblockpeaknetramp6h
	;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load block0h,block1h,blockpeaktotal2h,blockpeaknet3h,block4h,block5h,blockpeaknetramp6h
$load pWeightblock0h,pWeightblock1h,pWeightblockpeaktotal2h,pWeightblockpeaknet3h,pWeightblock4h,pWeightblock5h,pWeightblockpeaknetramp6h
$load pSOCScalarblock1h,pSOCScalarblockpeaktotal2h,pSOCScalarblockpeaknet3h,pSOCScalarblock4h,pSOCScalarblock5h,pSOCScalarblockpeaknetramp6h
$load pInitSOCblock0h,pInitSOCblock0htech
$gdxin

pHourInitblock0h = smin(h$block0h(h),ord(h));
pHourFinalblock0h = smax(h$block0h(h),ord(h));
pHourInitblock1h = smin(h$block1h(h),ord(h));
pHourFinalblock1h = smax(h$block1h(h),ord(h));
pHourInitblockpeaktotal2h = smin(h$blockpeaktotal2h(h),ord(h));
pHourFinalblockpeaktotal2h = smax(h$blockpeaktotal2h(h),ord(h));
pHourInitblockpeaknet3h = smin(h$blockpeaknet3h(h),ord(h));
pHourFinalblockpeaknet3h = smax(h$blockpeaknet3h(h),ord(h));
pHourInitblock4h = smin(h$block4h(h),ord(h));
pHourFinalblock4h = smax(h$block4h(h),ord(h));
pHourInitblock5h = smin(h$block5h(h),ord(h));
pHourFinalblock5h = smax(h$block5h(h),ord(h));
pHourInitblockpeaknetramp6h = smin(h$blockpeaknetramp6h(h),ord(h));
pHourFinalblockpeaknetramp6h = smax(h$blockpeaknetramp6h(h),ord(h));

nonInitH(h)= yes;
nonInitH(h)$[ord(h)=pHourInitblock0h] = no;
nonInitH(h)$[ord(h)=pHourInitblock1h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaktotal2h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaknet3h] = no;
nonInitH(h)$[ord(h)=pHourInitblock4h] = no;
nonInitH(h)$[ord(h)=pHourInitblock5h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaknetramp6h] = no;

Variables
	vInitSOCblock1h(storageegu)
	vInitSOCblockpeaktotal2h(storageegu)
	vInitSOCblockpeaknet3h(storageegu)
	vInitSOCblock4h(storageegu)
	vInitSOCblock5h(storageegu)
	vInitSOCblockpeaknetramp6h(storageegu)
	vInitSOCblock1htech(storagetech)
	vInitSOCblockpeaktotal2htech(storagetech)
	vInitSOCblockpeaknet3htech(storagetech)
	vInitSOCblock4htech(storagetech)
	vInitSOCblock5htech(storagetech)
	vInitSOCblockpeaknetramp6htech(storagetech)
	vFinalSOCblock0h(storageegu)
	vFinalSOCblock1h(storageegu)
	vFinalSOCblockpeaktotal2h(storageegu)
	vFinalSOCblockpeaknet3h(storageegu)
	vFinalSOCblock4h(storageegu)
	vFinalSOCblock5h(storageegu)
	vFinalSOCblockpeaknetramp6h(storageegu)
	vFinalSOCblock0htech(storagetech)
	vFinalSOCblock1htech(storagetech)
	vFinalSOCblockpeaktotal2htech(storagetech)
	vFinalSOCblockpeaknet3htech(storagetech)
	vFinalSOCblock4htech(storagetech)
	vFinalSOCblock5htech(storagetech)
	vFinalSOCblockpeaknetramp6htech(storagetech)
	vChangeSOCblock0h(storageegu)
	vChangeSOCblock1h(storageegu)
	vChangeSOCblockpeaktotal2h(storageegu)
	vChangeSOCblockpeaknet3h(storageegu)
	vChangeSOCblock4h(storageegu)
	vChangeSOCblock5h(storageegu)
	vChangeSOCblockpeaknetramp6h(storageegu)
	vChangeSOCblock0htech(storagetech)
	vChangeSOCblock1htech(storagetech)
	vChangeSOCblockpeaktotal2htech(storagetech)
	vChangeSOCblockpeaknet3htech(storagetech)
	vChangeSOCblock4htech(storagetech)
	vChangeSOCblock5htech(storagetech)
	vChangeSOCblockpeaknetramp6htech(storagetech)
	;

Equations
	varCost
	co2Ems
	defSOC(storageegu,h)
	genPlusUpResToSOC(storageegu,h)
	setInitSOCblock1h(storageegu)
	setInitSOCblockpeaktotal2h(storageegu)
	setInitSOCblockpeaknet3h(storageegu)
	setInitSOCblock4h(storageegu)
	setInitSOCblock5h(storageegu)
	setInitSOCblockpeaknetramp6h(storageegu)
	defFinalSOCblock0h(storageegu,h)
	defChangeSOCblock0h(storageegu)
	defFinalSOCblock1h(storageegu,h)
	defChangeSOCblock1h(storageegu)
	defFinalSOCblockpeaktotal2h(storageegu,h)
	defChangeSOCblockpeaktotal2h(storageegu)
	defFinalSOCblockpeaknet3h(storageegu,h)
	defChangeSOCblockpeaknet3h(storageegu)
	defFinalSOCblock4h(storageegu,h)
	defChangeSOCblock4h(storageegu)
	defFinalSOCblock5h(storageegu,h)
	defChangeSOCblock5h(storageegu)
	defFinalSOCblockpeaknetramp6h(storageegu,h)
	defChangeSOCblockpeaknetramp6h(storageegu)
	defSOCtech(storagetech,h)
	genPlusUpResToSOCtech(storagetech,h)
	setInitSOCblock1htech(storagetech)
	setInitSOCblockpeaktotal2htech(storagetech)
	setInitSOCblockpeaknet3htech(storagetech)
	setInitSOCblock4htech(storagetech)
	setInitSOCblock5htech(storagetech)
	setInitSOCblockpeaknetramp6htech(storagetech)
	defFinalSOCblock0htech(storagetech,h)
	defChangeSOCblock0htech(storagetech)
	defFinalSOCblock1htech(storagetech,h)
	defChangeSOCblock1htech(storagetech)
	defFinalSOCblockpeaktotal2htech(storagetech,h)
	defChangeSOCblockpeaktotal2htech(storagetech)
	defFinalSOCblockpeaknet3htech(storagetech,h)
	defChangeSOCblockpeaknet3htech(storagetech)
	defFinalSOCblock4htech(storagetech,h)
	defChangeSOCblock4htech(storagetech)
	defFinalSOCblock5htech(storagetech,h)
	defChangeSOCblock5htech(storagetech)
	defFinalSOCblockpeaknetramp6htech(storagetech,h)
	defChangeSOCblockpeaknetramp6htech(storagetech)
	rampUpblock0h(egu,block0h)
	rampUpblock1h(egu,block1h)
	rampUpblockpeaktotal2h(egu,blockpeaktotal2h)
	rampUpblockpeaknet3h(egu,blockpeaknet3h)
	rampUpblock4h(egu,block4h)
	rampUpblock5h(egu,block5h)
	rampUpblockpeaknetramp6h(egu,blockpeaknetramp6h)
	rampUpblock0htech(tech,block0h)
	rampUpblock1htech(tech,block1h)
	rampUpblockpeaktotal2htech(tech,blockpeaktotal2h)
	rampUpblockpeaknet3htech(tech,blockpeaknet3h)
	rampUpblock4htech(tech,block4h)
	rampUpblock5htech(tech,block5h)
	rampUpblockpeaknetramp6htech(tech,blockpeaknetramp6h)
	;

defSOC(storageegu,h).. vStateofcharge(storageegu,h) =e= pInitSOCblock0h(storageegu)$[ord(h)=pHourInitblock0h] + vInitSOCblock1h(storageegu)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2h(storageegu)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3h(storageegu)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4h(storageegu)$[ord(h)=pHourInitblock4h] + vInitSOCblock5h(storageegu)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6h(storageegu)$[ord(h)=pHourInitblockpeaknetramp6h] +
	vStateofcharge(storageegu, h-1)$nonInitH(h) - 
               1/sqrt(pEfficiency(storageegu)) * vGen(storageegu,h) + 
               sqrt(pEfficiency(storageegu)) * vCharge(storageegu,h);
genPlusUpResToSOC(storageegu,h).. vGen(storageegu,h)+vRegup(storageegu,h)+vFlex(storageegu,h)+vCont(storageegu,h) =l= vStateofcharge(storageegu, h-1)$nonInitH(h)
                     + pInitSOCblock0h(storageegu)$[ord(h)=pHourInitblock0h] + vInitSOCblock1h(storageegu)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2h(storageegu)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3h(storageegu)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4h(storageegu)$[ord(h)=pHourInitblock4h] + vInitSOCblock5h(storageegu)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6h(storageegu)$[ord(h)=pHourInitblockpeaknetramp6h];
setInitSOCblock1h(ltstorageegu).. vInitSOCblock1h(ltstorageegu) =e= vFinalSOCblock0h(ltstorageegu) + vChangeSOCblock0h(ltstorageegu)*pSOCScalarblock1h 
                        ;
setInitSOCblockpeaktotal2h(ltstorageegu).. vInitSOCblockpeaktotal2h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblockpeaktotal2h 
                        ;
setInitSOCblockpeaknet3h(ltstorageegu).. vInitSOCblockpeaknet3h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblockpeaknet3h + vChangeSOCblockpeaktotal2h(ltstorageegu)
                        ;
setInitSOCblock4h(ltstorageegu).. vInitSOCblock4h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblock4h + vChangeSOCblockpeaktotal2h(ltstorageegu)+ vChangeSOCblockpeaknet3h(ltstorageegu)
                        ;
setInitSOCblock5h(ltstorageegu).. vInitSOCblock5h(ltstorageegu) =e= vFinalSOCblock4h(ltstorageegu) + vChangeSOCblock4h(ltstorageegu)*pSOCScalarblock5h 
                        ;
setInitSOCblockpeaknetramp6h(ltstorageegu).. vInitSOCblockpeaknetramp6h(ltstorageegu) =e= vFinalSOCblock5h(ltstorageegu) + vChangeSOCblock5h(ltstorageegu)*pSOCScalarblockpeaknetramp6h 
                        ;
defFinalSOCblock0h(ltstorageegu,h)$[ord(h)=pHourFinalblock0h].. vFinalSOCblock0h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock0h(ltstorageegu).. vChangeSOCblock0h(ltstorageegu) =e= vFinalSOCblock0h(ltstorageegu) 
                              - pInitSOCblock0h(ltstorageegu);
defFinalSOCblock1h(ltstorageegu,h)$[ord(h)=pHourFinalblock1h].. vFinalSOCblock1h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock1h(ltstorageegu).. vChangeSOCblock1h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) 
                              - vInitSOCblock1h(ltstorageegu);
defFinalSOCblockpeaktotal2h(ltstorageegu,h)$[ord(h)=pHourFinalblockpeaktotal2h].. vFinalSOCblockpeaktotal2h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblockpeaktotal2h(ltstorageegu).. vChangeSOCblockpeaktotal2h(ltstorageegu) =e= vFinalSOCblockpeaktotal2h(ltstorageegu) 
                              - vInitSOCblockpeaktotal2h(ltstorageegu);
defFinalSOCblockpeaknet3h(ltstorageegu,h)$[ord(h)=pHourFinalblockpeaknet3h].. vFinalSOCblockpeaknet3h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblockpeaknet3h(ltstorageegu).. vChangeSOCblockpeaknet3h(ltstorageegu) =e= vFinalSOCblockpeaknet3h(ltstorageegu) 
                              - vInitSOCblockpeaknet3h(ltstorageegu);
defFinalSOCblock4h(ltstorageegu,h)$[ord(h)=pHourFinalblock4h].. vFinalSOCblock4h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock4h(ltstorageegu).. vChangeSOCblock4h(ltstorageegu) =e= vFinalSOCblock4h(ltstorageegu) 
                              - vInitSOCblock4h(ltstorageegu);
defFinalSOCblock5h(ltstorageegu,h)$[ord(h)=pHourFinalblock5h].. vFinalSOCblock5h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock5h(ltstorageegu).. vChangeSOCblock5h(ltstorageegu) =e= vFinalSOCblock5h(ltstorageegu) 
                              - vInitSOCblock5h(ltstorageegu);
defFinalSOCblockpeaknetramp6h(ltstorageegu,h)$[ord(h)=pHourFinalblockpeaknetramp6h].. vFinalSOCblockpeaknetramp6h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblockpeaknetramp6h(ltstorageegu).. vChangeSOCblockpeaknetramp6h(ltstorageegu) =e= vFinalSOCblockpeaknetramp6h(ltstorageegu) 
                              - vInitSOCblockpeaknetramp6h(ltstorageegu);

defSOCtech(storagetech,h).. vStateofchargetech(storagetech,h) =e= pInitSOCblock0htech(storagetech)$[ord(h)=pHourInitblock0h]*vN(storagetech) + vInitSOCblock1htech(storagetech)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2htech(storagetech)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3htech(storagetech)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4htech(storagetech)$[ord(h)=pHourInitblock4h] + vInitSOCblock5htech(storagetech)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6htech(storagetech)$[ord(h)=pHourInitblockpeaknetramp6h] +
	vStateofchargetech(storagetech, h-1)$nonInitH(h) - 
               1/sqrt(pEfficiencytech(storagetech)) * vGentech(storagetech,h) + 
               sqrt(pEfficiencytech(storagetech)) * vChargetech(storagetech,h);
genPlusUpResToSOCtech(storagetech,h).. vGentech(storagetech,h)+vReguptech(storagetech,h)+vFlextech(storagetech,h)+vConttech(storagetech,h) =l= vStateofchargetech(storagetech, h-1)$nonInitH(h)
                     + pInitSOCblock0htech(storagetech)$[ord(h)=pHourInitblock0h]*vN(storagetech) + vInitSOCblock1htech(storagetech)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2htech(storagetech)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3htech(storagetech)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4htech(storagetech)$[ord(h)=pHourInitblock4h] + vInitSOCblock5htech(storagetech)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6htech(storagetech)$[ord(h)=pHourInitblockpeaknetramp6h];
setInitSOCblock1htech(ltstoragetech).. vInitSOCblock1htech(ltstoragetech) =e= vFinalSOCblock0htech(ltstoragetech) + vChangeSOCblock0htech(ltstoragetech)*pSOCScalarblock1h 
                        ;
setInitSOCblockpeaktotal2htech(ltstoragetech).. vInitSOCblockpeaktotal2htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblockpeaktotal2h 
                        ;
setInitSOCblockpeaknet3htech(ltstoragetech).. vInitSOCblockpeaknet3htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblockpeaknet3h + vChangeSOCblockpeaktotal2htech(ltstoragetech)
                        ;
setInitSOCblock4htech(ltstoragetech).. vInitSOCblock4htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblock4h + vChangeSOCblockpeaktotal2htech(ltstoragetech)+ vChangeSOCblockpeaknet3htech(ltstoragetech)
                        ;
setInitSOCblock5htech(ltstoragetech).. vInitSOCblock5htech(ltstoragetech) =e= vFinalSOCblock4htech(ltstoragetech) + vChangeSOCblock4htech(ltstoragetech)*pSOCScalarblock5h 
                        ;
setInitSOCblockpeaknetramp6htech(ltstoragetech).. vInitSOCblockpeaknetramp6htech(ltstoragetech) =e= vFinalSOCblock5htech(ltstoragetech) + vChangeSOCblock5htech(ltstoragetech)*pSOCScalarblockpeaknetramp6h 
                        ;
defFinalSOCblock0htech(ltstoragetech,h)$[ord(h)=pHourFinalblock0h].. vFinalSOCblock0htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock0htech(ltstoragetech).. vChangeSOCblock0htech(ltstoragetech) =e= vFinalSOCblock0htech(ltstoragetech) 
                              - pInitSOCblock0htech(ltstoragetech)*vN(ltstoragetech);
defFinalSOCblock1htech(ltstoragetech,h)$[ord(h)=pHourFinalblock1h].. vFinalSOCblock1htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock1htech(ltstoragetech).. vChangeSOCblock1htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) 
                              - vInitSOCblock1htech(ltstoragetech);
defFinalSOCblockpeaktotal2htech(ltstoragetech,h)$[ord(h)=pHourFinalblockpeaktotal2h].. vFinalSOCblockpeaktotal2htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblockpeaktotal2htech(ltstoragetech).. vChangeSOCblockpeaktotal2htech(ltstoragetech) =e= vFinalSOCblockpeaktotal2htech(ltstoragetech) 
                              - vInitSOCblockpeaktotal2htech(ltstoragetech);
defFinalSOCblockpeaknet3htech(ltstoragetech,h)$[ord(h)=pHourFinalblockpeaknet3h].. vFinalSOCblockpeaknet3htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblockpeaknet3htech(ltstoragetech).. vChangeSOCblockpeaknet3htech(ltstoragetech) =e= vFinalSOCblockpeaknet3htech(ltstoragetech) 
                              - vInitSOCblockpeaknet3htech(ltstoragetech);
defFinalSOCblock4htech(ltstoragetech,h)$[ord(h)=pHourFinalblock4h].. vFinalSOCblock4htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock4htech(ltstoragetech).. vChangeSOCblock4htech(ltstoragetech) =e= vFinalSOCblock4htech(ltstoragetech) 
                              - vInitSOCblock4htech(ltstoragetech);
defFinalSOCblock5htech(ltstoragetech,h)$[ord(h)=pHourFinalblock5h].. vFinalSOCblock5htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock5htech(ltstoragetech).. vChangeSOCblock5htech(ltstoragetech) =e= vFinalSOCblock5htech(ltstoragetech) 
                              - vInitSOCblock5htech(ltstoragetech);
defFinalSOCblockpeaknetramp6htech(ltstoragetech,h)$[ord(h)=pHourFinalblockpeaknetramp6h].. vFinalSOCblockpeaknetramp6htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblockpeaknetramp6htech(ltstoragetech).. vChangeSOCblockpeaknetramp6htech(ltstoragetech) =e= vFinalSOCblockpeaknetramp6htech(ltstoragetech) 
                              - vInitSOCblockpeaknetramp6htech(ltstoragetech);

varCost.. vVarcostannual =e= pWeightblock0h*(sum((egu,block0h),vVarcost(egu,block0h))+sum((tech,block0h),vVarcosttech(tech,block0h)))
	+ pWeightblock1h*(sum((egu,block1h),vVarcost(egu,block1h))+sum((tech,block1h),vVarcosttech(tech,block1h)))
	+ pWeightblockpeaktotal2h*(sum((egu,blockpeaktotal2h),vVarcost(egu,blockpeaktotal2h))+sum((tech,blockpeaktotal2h),vVarcosttech(tech,blockpeaktotal2h)))
	+ pWeightblockpeaknet3h*(sum((egu,blockpeaknet3h),vVarcost(egu,blockpeaknet3h))+sum((tech,blockpeaknet3h),vVarcosttech(tech,blockpeaknet3h)))
	+ pWeightblock4h*(sum((egu,block4h),vVarcost(egu,block4h))+sum((tech,block4h),vVarcosttech(tech,block4h)))
	+ pWeightblock5h*(sum((egu,block5h),vVarcost(egu,block5h))+sum((tech,block5h),vVarcosttech(tech,block5h)))
	+ pWeightblockpeaknetramp6h*(sum((egu,blockpeaknetramp6h),vVarcost(egu,blockpeaknetramp6h))+sum((tech,blockpeaknetramp6h),vVarcosttech(tech,blockpeaknetramp6h)));
co2Ems.. vCO2emsannual =e= pWeightblock0h*(sum((egu,block0h),vCO2ems(egu,block0h))+sum((tech,block0h),vCO2emstech(tech,block0h)))
	+ pWeightblock1h*(sum((egu,block1h),vCO2ems(egu,block1h))+sum((tech,block1h),vCO2emstech(tech,block1h)))
	+ pWeightblockpeaktotal2h*(sum((egu,blockpeaktotal2h),vCO2ems(egu,blockpeaktotal2h))+sum((tech,blockpeaktotal2h),vCO2emstech(tech,blockpeaktotal2h)))
	+ pWeightblockpeaknet3h*(sum((egu,blockpeaknet3h),vCO2ems(egu,blockpeaknet3h))+sum((tech,blockpeaknet3h),vCO2emstech(tech,blockpeaknet3h)))
	+ pWeightblock4h*(sum((egu,block4h),vCO2ems(egu,block4h))+sum((tech,block4h),vCO2emstech(tech,block4h)))
	+ pWeightblock5h*(sum((egu,block5h),vCO2ems(egu,block5h))+sum((tech,block5h),vCO2emstech(tech,block5h)))
	+ pWeightblockpeaknetramp6h*(sum((egu,blockpeaknetramp6h),vCO2ems(egu,blockpeaknetramp6h))+sum((tech,blockpeaknetramp6h),vCO2emstech(tech,blockpeaknetramp6h)));

rampUpblock0h(egu,block0h)$[ORD(block0h)>1].. vGen(egu,block0h)+vRegup(egu,block0h)+vFlex(egu,block0h)+vCont(egu,block0h) - vGen(egu,block0h-1) =l= 
                  pRamprate(egu);
rampUpblock0htech(tech,block0h)$[ORD(block0h)>1].. vGentech(tech,block0h)+vReguptech(tech,block0h)+vFlextech(tech,block0h)+vConttech(tech,block0h) - vGentech(tech,block0h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblock1h(egu,block1h)$[ORD(block1h)>1].. vGen(egu,block1h)+vRegup(egu,block1h)+vFlex(egu,block1h)+vCont(egu,block1h) - vGen(egu,block1h-1) =l= 
                  pRamprate(egu);
rampUpblock1htech(tech,block1h)$[ORD(block1h)>1].. vGentech(tech,block1h)+vReguptech(tech,block1h)+vFlextech(tech,block1h)+vConttech(tech,block1h) - vGentech(tech,block1h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblockpeaktotal2h(egu,blockpeaktotal2h)$[ORD(blockpeaktotal2h)>1].. vGen(egu,blockpeaktotal2h)+vRegup(egu,blockpeaktotal2h)+vFlex(egu,blockpeaktotal2h)+vCont(egu,blockpeaktotal2h) - vGen(egu,blockpeaktotal2h-1) =l= 
                  pRamprate(egu);
rampUpblockpeaktotal2htech(tech,blockpeaktotal2h)$[ORD(blockpeaktotal2h)>1].. vGentech(tech,blockpeaktotal2h)+vReguptech(tech,blockpeaktotal2h)+vFlextech(tech,blockpeaktotal2h)+vConttech(tech,blockpeaktotal2h) - vGentech(tech,blockpeaktotal2h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblockpeaknet3h(egu,blockpeaknet3h)$[ORD(blockpeaknet3h)>1].. vGen(egu,blockpeaknet3h)+vRegup(egu,blockpeaknet3h)+vFlex(egu,blockpeaknet3h)+vCont(egu,blockpeaknet3h) - vGen(egu,blockpeaknet3h-1) =l= 
                  pRamprate(egu);
rampUpblockpeaknet3htech(tech,blockpeaknet3h)$[ORD(blockpeaknet3h)>1].. vGentech(tech,blockpeaknet3h)+vReguptech(tech,blockpeaknet3h)+vFlextech(tech,blockpeaknet3h)+vConttech(tech,blockpeaknet3h) - vGentech(tech,blockpeaknet3h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblock4h(egu,block4h)$[ORD(block4h)>1].. vGen(egu,block4h)+vRegup(egu,block4h)+vFlex(egu,block4h)+vCont(egu,block4h) - vGen(egu,block4h-1) =l= 
                  pRamprate(egu);
rampUpblock4htech(tech,block4h)$[ORD(block4h)>1].. vGentech(tech,block4h)+vReguptech(tech,block4h)+vFlextech(tech,block4h)+vConttech(tech,block4h) - vGentech(tech,block4h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblock5h(egu,block5h)$[ORD(block5h)>1].. vGen(egu,block5h)+vRegup(egu,block5h)+vFlex(egu,block5h)+vCont(egu,block5h) - vGen(egu,block5h-1) =l= 
                  pRamprate(egu);
rampUpblock5htech(tech,block5h)$[ORD(block5h)>1].. vGentech(tech,block5h)+vReguptech(tech,block5h)+vFlextech(tech,block5h)+vConttech(tech,block5h) - vGentech(tech,block5h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblockpeaknetramp6h(egu,blockpeaknetramp6h)$[ORD(blockpeaknetramp6h)>1].. vGen(egu,blockpeaknetramp6h)+vRegup(egu,blockpeaknetramp6h)+vFlex(egu,blockpeaknetramp6h)+vCont(egu,blockpeaknetramp6h) - vGen(egu,blockpeaknetramp6h-1) =l= 
                  pRamprate(egu);
rampUpblockpeaknetramp6htech(tech,blockpeaknetramp6h)$[ORD(blockpeaknetramp6h)>1].. vGentech(tech,blockpeaknetramp6h)+vReguptech(tech,blockpeaknetramp6h)+vFlextech(tech,blockpeaknetramp6h)+vConttech(tech,blockpeaknetramp6h) - vGentech(tech,blockpeaknetramp6h-1) =l= 
                  pRampratetech(tech)*vN(tech);
