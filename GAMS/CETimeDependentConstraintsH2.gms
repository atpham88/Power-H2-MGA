Sets
	block0h(h)
	block1h(h)
	blockpeaktotal2h(h)
	blockpeaknet3h(h)
	block4h(h)
	blockpeaknetramp5h(h)
	block6h(h)
	;

Parameters
	pWeightblock0h
	pWeightblock1h
	pWeightblockpeaktotal2h
	pWeightblockpeaknet3h
	pWeightblock4h
	pWeightblockpeaknetramp5h
	pWeightblock6h
	pInitSOC(storageegu)
	pInitSOCtech(storagetech)
	pHourInitblock0h
	pHourFinalblock0h
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
	pHourInitblockpeaknetramp5h
	pHourFinalblockpeaknetramp5h
	pSOCScalarblockpeaknetramp5h
	pHourInitblock6h
	pHourFinalblock6h
	pSOCScalarblock6h
	pMaxgenhydroblock0h(z)
	pMaxgenhydroblock1h(z)
	pMaxgenhydroblockpeaktotal2h(z)
	pMaxgenhydroblockpeaknet3h(z)
	pMaxgenhydroblock4h(z)
	pMaxgenhydroblockpeaknetramp5h(z)
	pMaxgenhydroblock6h(z)
	;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load block0h,block1h,blockpeaktotal2h,blockpeaknet3h,block4h,blockpeaknetramp5h,block6h
$load pWeightblock0h,pWeightblock1h,pWeightblockpeaktotal2h,pWeightblockpeaknet3h,pWeightblock4h,pWeightblockpeaknetramp5h,pWeightblock6h
$load pSOCScalarblock1h,pSOCScalarblockpeaktotal2h,pSOCScalarblockpeaknet3h,pSOCScalarblock4h,pSOCScalarblockpeaknetramp5h,pSOCScalarblock6h
$load pInitSOC,pInitSOCtech
$load pMaxgenhydroblock0h,pMaxgenhydroblock1h,pMaxgenhydroblockpeaktotal2h,pMaxgenhydroblockpeaknet3h,pMaxgenhydroblock4h,pMaxgenhydroblockpeaknetramp5h,pMaxgenhydroblock6h
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
pHourInitblockpeaknetramp5h = smin(h$blockpeaknetramp5h(h),ord(h));
pHourFinalblockpeaknetramp5h = smax(h$blockpeaknetramp5h(h),ord(h));
pHourInitblock6h = smin(h$block6h(h),ord(h));
pHourFinalblock6h = smax(h$block6h(h),ord(h));

nonInitH(h)= yes;
nonInitH(h)$[ord(h)=pHourInitblock0h] = no;
nonInitH(h)$[ord(h)=pHourInitblock1h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaktotal2h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaknet3h] = no;
nonInitH(h)$[ord(h)=pHourInitblock4h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaknetramp5h] = no;
nonInitH(h)$[ord(h)=pHourInitblock6h] = no;

Variables
	vInitSOCblock1h(storageegu)
	vInitSOCblockpeaktotal2h(storageegu)
	vInitSOCblockpeaknet3h(storageegu)
	vInitSOCblock4h(storageegu)
	vInitSOCblockpeaknetramp5h(storageegu)
	vInitSOCblock6h(storageegu)
	vInitSOCblock1htech(storagetech)
	vInitSOCblockpeaktotal2htech(storagetech)
	vInitSOCblockpeaknet3htech(storagetech)
	vInitSOCblock4htech(storagetech)
	vInitSOCblockpeaknetramp5htech(storagetech)
	vInitSOCblock6htech(storagetech)
	vFinalSOCblock0h(storageegu)
	vFinalSOCblock1h(storageegu)
	vFinalSOCblockpeaktotal2h(storageegu)
	vFinalSOCblockpeaknet3h(storageegu)
	vFinalSOCblock4h(storageegu)
	vFinalSOCblockpeaknetramp5h(storageegu)
	vFinalSOCblock6h(storageegu)
	vFinalSOCblock0htech(storagetech)
	vFinalSOCblock1htech(storagetech)
	vFinalSOCblockpeaktotal2htech(storagetech)
	vFinalSOCblockpeaknet3htech(storagetech)
	vFinalSOCblock4htech(storagetech)
	vFinalSOCblockpeaknetramp5htech(storagetech)
	vFinalSOCblock6htech(storagetech)
	vChangeSOCblock0h(storageegu)
	vChangeSOCblock1h(storageegu)
	vChangeSOCblockpeaktotal2h(storageegu)
	vChangeSOCblockpeaknet3h(storageegu)
	vChangeSOCblock4h(storageegu)
	vChangeSOCblockpeaknetramp5h(storageegu)
	vChangeSOCblock6h(storageegu)
	vChangeSOCblock0htech(storagetech)
	vChangeSOCblock1htech(storagetech)
	vChangeSOCblockpeaktotal2htech(storagetech)
	vChangeSOCblockpeaknet3htech(storagetech)
	vChangeSOCblock4htech(storagetech)
	vChangeSOCblockpeaknetramp5htech(storagetech)
	vChangeSOCblock6htech(storagetech)
	;

Equations
	varCost
	co2Ems
	defSOC(storageegu,h)
	genPlusUpResToSOC(storageegu,h)
	setInitSOCblock1hltstorageegu(ltstorageegu)
	setInitSOCblockpeaktotal2hltstorageegu(ltstorageegu)
	setInitSOCblockpeaknet3hltstorageegu(ltstorageegu)
	setInitSOCblock4hltstorageegu(ltstorageegu)
	setInitSOCblockpeaknetramp5hltstorageegu(ltstorageegu)
	setInitSOCblock6hltstorageegu(ltstorageegu)
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
	defFinalSOCblockpeaknetramp5h(storageegu,h)
	defChangeSOCblockpeaknetramp5h(storageegu)
	defFinalSOCblock6h(storageegu,h)
	defChangeSOCblock6h(storageegu)
	setInitSOCblock1hststorageegu(ststorageegu)
	setInitSOCblockpeaktotal2hststorageegu(ststorageegu)
	setInitSOCblockpeaknet3hststorageegu(ststorageegu)
	setInitSOCblock4hststorageegu(ststorageegu)
	setInitSOCblockpeaknetramp5hststorageegu(ststorageegu)
	setInitSOCblock6hststorageegu(ststorageegu)
	defSOCtech(storagetech,h)
	genPlusUpResToSOCtech(storagetech,h)
	setInitSOCblock1hltstoragetech(ltstoragetech)
	setInitSOCblockpeaktotal2hltstoragetech(ltstoragetech)
	setInitSOCblockpeaknet3hltstoragetech(ltstoragetech)
	setInitSOCblock4hltstoragetech(ltstoragetech)
	setInitSOCblockpeaknetramp5hltstoragetech(ltstoragetech)
	setInitSOCblock6hltstoragetech(ltstoragetech)
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
	defFinalSOCblockpeaknetramp5htech(storagetech,h)
	defChangeSOCblockpeaknetramp5htech(storagetech)
	defFinalSOCblock6htech(storagetech,h)
	defChangeSOCblock6htech(storagetech)
	setInitSOCblock1hststoragetech(ststoragetech)
	setInitSOCblockpeaktotal2hststoragetech(ststoragetech)
	setInitSOCblockpeaknet3hststoragetech(ststoragetech)
	setInitSOCblock4hststoragetech(ststoragetech)
	setInitSOCblockpeaknetramp5hststoragetech(ststoragetech)
	setInitSOCblock6hststoragetech(ststoragetech)
	rampUpblock0h(egu,block0h)
	rampUpblock1h(egu,block1h)
	rampUpblockpeaktotal2h(egu,blockpeaktotal2h)
	rampUpblockpeaknet3h(egu,blockpeaknet3h)
	rampUpblock4h(egu,block4h)
	rampUpblockpeaknetramp5h(egu,blockpeaknetramp5h)
	rampUpblock6h(egu,block6h)
	rampUpblock0htech(tech,block0h)
	rampUpblock1htech(tech,block1h)
	rampUpblockpeaktotal2htech(tech,blockpeaktotal2h)
	rampUpblockpeaknet3htech(tech,blockpeaknet3h)
	rampUpblock4htech(tech,block4h)
	rampUpblockpeaknetramp5htech(tech,blockpeaknetramp5h)
	rampUpblock6htech(tech,block6h)
	limitHydroGenblock0h(z)
	limitHydroGenblock1h(z)
	limitHydroGenblockpeaktotal2h(z)
	limitHydroGenblockpeaknet3h(z)
	limitHydroGenblock4h(z)
	limitHydroGenblockpeaknetramp5h(z)
	limitHydroGenblock6h(z)
	;

defSOC(storageegu,h).. vStateofcharge(storageegu,h) =e= pInitSOC(storageegu)$[ord(h)=pHourInitblock0h] + vInitSOCblock1h(storageegu)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2h(storageegu)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3h(storageegu)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4h(storageegu)$[ord(h)=pHourInitblock4h] + vInitSOCblockpeaknetramp5h(storageegu)$[ord(h)=pHourInitblockpeaknetramp5h] + vInitSOCblock6h(storageegu)$[ord(h)=pHourInitblock6h] +
	vStateofcharge(storageegu, h-1)$nonInitH(h) - 
               1/sqrt(pEfficiency(storageegu)) * vGen(storageegu,h) + 
               sqrt(pEfficiency(storageegu)) * vCharge(storageegu,h);
genPlusUpResToSOC(storageegu,h).. vGen(storageegu,h)+vRegup(storageegu,h)+vFlex(storageegu,h)+vCont(storageegu,h) =l= vStateofcharge(storageegu, h-1)$nonInitH(h)
                     + pInitSOC(storageegu)$[ord(h)=pHourInitblock0h] + vInitSOCblock1h(storageegu)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2h(storageegu)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3h(storageegu)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4h(storageegu)$[ord(h)=pHourInitblock4h] + vInitSOCblockpeaknetramp5h(storageegu)$[ord(h)=pHourInitblockpeaknetramp5h] + vInitSOCblock6h(storageegu)$[ord(h)=pHourInitblock6h];
setInitSOCblock1hltstorageegu(ltstorageegu).. vInitSOCblock1h(ltstorageegu) =e= vFinalSOCblock0h(ltstorageegu) + vChangeSOCblock0h(ltstorageegu)*pSOCScalarblock1h 
                        ;
setInitSOCblockpeaktotal2hltstorageegu(ltstorageegu).. vInitSOCblockpeaktotal2h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblockpeaktotal2h 
                        ;
setInitSOCblockpeaknet3hltstorageegu(ltstorageegu).. vInitSOCblockpeaknet3h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblockpeaknet3h + vChangeSOCblockpeaktotal2h(ltstorageegu)
                        ;
setInitSOCblock4hltstorageegu(ltstorageegu).. vInitSOCblock4h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblock4h + vChangeSOCblockpeaktotal2h(ltstorageegu)+ vChangeSOCblockpeaknet3h(ltstorageegu)
                        ;
setInitSOCblockpeaknetramp5hltstorageegu(ltstorageegu).. vInitSOCblockpeaknetramp5h(ltstorageegu) =e= vFinalSOCblock4h(ltstorageegu) + vChangeSOCblock4h(ltstorageegu)*pSOCScalarblockpeaknetramp5h 
                        ;
setInitSOCblock6hltstorageegu(ltstorageegu).. vInitSOCblock6h(ltstorageegu) =e= vFinalSOCblock4h(ltstorageegu) + vChangeSOCblock4h(ltstorageegu)*pSOCScalarblock6h + vChangeSOCblockpeaknetramp5h(ltstorageegu)
                        ;
defFinalSOCblock0h(ltstorageegu,h)$[ord(h)=pHourFinalblock0h].. vFinalSOCblock0h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock0h(ltstorageegu).. vChangeSOCblock0h(ltstorageegu) =e= vFinalSOCblock0h(ltstorageegu) 
                              - pInitSOC(ltstorageegu);
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
defFinalSOCblockpeaknetramp5h(ltstorageegu,h)$[ord(h)=pHourFinalblockpeaknetramp5h].. vFinalSOCblockpeaknetramp5h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblockpeaknetramp5h(ltstorageegu).. vChangeSOCblockpeaknetramp5h(ltstorageegu) =e= vFinalSOCblockpeaknetramp5h(ltstorageegu) 
                              - vInitSOCblockpeaknetramp5h(ltstorageegu);
defFinalSOCblock6h(ltstorageegu,h)$[ord(h)=pHourFinalblock6h].. vFinalSOCblock6h(ltstorageegu) =e= 
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock6h(ltstorageegu).. vChangeSOCblock6h(ltstorageegu) =e= vFinalSOCblock6h(ltstorageegu) 
                              - vInitSOCblock6h(ltstorageegu);
setInitSOCblock1hststorageegu(ststorageegu).. vInitSOCblock1h(ststorageegu) =e= 
                                    pInitSOC(ststorageegu);
setInitSOCblockpeaktotal2hststorageegu(ststorageegu).. vInitSOCblockpeaktotal2h(ststorageegu) =e= 
                                    pInitSOC(ststorageegu);
setInitSOCblockpeaknet3hststorageegu(ststorageegu).. vInitSOCblockpeaknet3h(ststorageegu) =e= 
                                    pInitSOC(ststorageegu);
setInitSOCblock4hststorageegu(ststorageegu).. vInitSOCblock4h(ststorageegu) =e= 
                                    pInitSOC(ststorageegu);
setInitSOCblockpeaknetramp5hststorageegu(ststorageegu).. vInitSOCblockpeaknetramp5h(ststorageegu) =e= 
                                    pInitSOC(ststorageegu);
setInitSOCblock6hststorageegu(ststorageegu).. vInitSOCblock6h(ststorageegu) =e= 
                                    pInitSOC(ststorageegu);

defSOCtech(storagetech,h).. vStateofchargetech(storagetech,h) =e= pInitSOCtech(storagetech)$[ord(h)=pHourInitblock0h]*vEneBuiltSto(storagetech) + vInitSOCblock1htech(storagetech)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2htech(storagetech)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3htech(storagetech)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4htech(storagetech)$[ord(h)=pHourInitblock4h] + vInitSOCblockpeaknetramp5htech(storagetech)$[ord(h)=pHourInitblockpeaknetramp5h] + vInitSOCblock6htech(storagetech)$[ord(h)=pHourInitblock6h] +
	vStateofchargetech(storagetech, h-1)$nonInitH(h) - 
               1/sqrt(pEfficiencytech(storagetech)) * vGentech(storagetech,h) + 
               sqrt(pEfficiencytech(storagetech)) * vChargetech(storagetech,h);
genPlusUpResToSOCtech(storagetech,h).. vGentech(storagetech,h)+vReguptech(storagetech,h)+vFlextech(storagetech,h)+vConttech(storagetech,h) =l= vStateofchargetech(storagetech, h-1)$nonInitH(h)
                     + pInitSOCtech(storagetech)$[ord(h)=pHourInitblock0h]*vEneBuiltSto(storagetech) + vInitSOCblock1htech(storagetech)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaktotal2htech(storagetech)$[ord(h)=pHourInitblockpeaktotal2h] + vInitSOCblockpeaknet3htech(storagetech)$[ord(h)=pHourInitblockpeaknet3h] + vInitSOCblock4htech(storagetech)$[ord(h)=pHourInitblock4h] + vInitSOCblockpeaknetramp5htech(storagetech)$[ord(h)=pHourInitblockpeaknetramp5h] + vInitSOCblock6htech(storagetech)$[ord(h)=pHourInitblock6h];
setInitSOCblock1hltstoragetech(ltstoragetech).. vInitSOCblock1htech(ltstoragetech) =e= vFinalSOCblock0htech(ltstoragetech) + vChangeSOCblock0htech(ltstoragetech)*pSOCScalarblock1h 
                        ;
setInitSOCblockpeaktotal2hltstoragetech(ltstoragetech).. vInitSOCblockpeaktotal2htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblockpeaktotal2h 
                        ;
setInitSOCblockpeaknet3hltstoragetech(ltstoragetech).. vInitSOCblockpeaknet3htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblockpeaknet3h + vChangeSOCblockpeaktotal2htech(ltstoragetech)
                        ;
setInitSOCblock4hltstoragetech(ltstoragetech).. vInitSOCblock4htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblock4h + vChangeSOCblockpeaktotal2htech(ltstoragetech)+ vChangeSOCblockpeaknet3htech(ltstoragetech)
                        ;
setInitSOCblockpeaknetramp5hltstoragetech(ltstoragetech).. vInitSOCblockpeaknetramp5htech(ltstoragetech) =e= vFinalSOCblock4htech(ltstoragetech) + vChangeSOCblock4htech(ltstoragetech)*pSOCScalarblockpeaknetramp5h 
                        ;
setInitSOCblock6hltstoragetech(ltstoragetech).. vInitSOCblock6htech(ltstoragetech) =e= vFinalSOCblock4htech(ltstoragetech) + vChangeSOCblock4htech(ltstoragetech)*pSOCScalarblock6h + vChangeSOCblockpeaknetramp5htech(ltstoragetech)
                        ;
defFinalSOCblock0htech(ltstoragetech,h)$[ord(h)=pHourFinalblock0h].. vFinalSOCblock0htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock0htech(ltstoragetech).. vChangeSOCblock0htech(ltstoragetech) =e= vFinalSOCblock0htech(ltstoragetech) 
                              - pInitSOCtech(ltstoragetech)*vEneBuiltSto(ltstoragetech);
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
defFinalSOCblockpeaknetramp5htech(ltstoragetech,h)$[ord(h)=pHourFinalblockpeaknetramp5h].. vFinalSOCblockpeaknetramp5htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblockpeaknetramp5htech(ltstoragetech).. vChangeSOCblockpeaknetramp5htech(ltstoragetech) =e= vFinalSOCblockpeaknetramp5htech(ltstoragetech) 
                              - vInitSOCblockpeaknetramp5htech(ltstoragetech);
defFinalSOCblock6htech(ltstoragetech,h)$[ord(h)=pHourFinalblock6h].. vFinalSOCblock6htech(ltstoragetech) =e= 
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock6htech(ltstoragetech).. vChangeSOCblock6htech(ltstoragetech) =e= vFinalSOCblock6htech(ltstoragetech) 
                              - vInitSOCblock6htech(ltstoragetech);
setInitSOCblock1hststoragetech(ststoragetech).. vInitSOCblock1htech(ststoragetech) =e= 
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblockpeaktotal2hststoragetech(ststoragetech).. vInitSOCblockpeaktotal2htech(ststoragetech) =e= 
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblockpeaknet3hststoragetech(ststoragetech).. vInitSOCblockpeaknet3htech(ststoragetech) =e= 
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblock4hststoragetech(ststoragetech).. vInitSOCblock4htech(ststoragetech) =e= 
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblockpeaknetramp5hststoragetech(ststoragetech).. vInitSOCblockpeaknetramp5htech(ststoragetech) =e= 
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblock6hststoragetech(ststoragetech).. vInitSOCblock6htech(ststoragetech) =e= 
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);

varCost.. vVarcostannual =e= pWeightblock0h*(sum((egu,block0h),vVarcost(egu,block0h))+sum((tech,block0h),vVarcosttech(tech,block0h)))
	+ pWeightblock1h*(sum((egu,block1h),vVarcost(egu,block1h))+sum((tech,block1h),vVarcosttech(tech,block1h)))
	+ pWeightblockpeaktotal2h*(sum((egu,blockpeaktotal2h),vVarcost(egu,blockpeaktotal2h))+sum((tech,blockpeaktotal2h),vVarcosttech(tech,blockpeaktotal2h)))
	+ pWeightblockpeaknet3h*(sum((egu,blockpeaknet3h),vVarcost(egu,blockpeaknet3h))+sum((tech,blockpeaknet3h),vVarcosttech(tech,blockpeaknet3h)))
	+ pWeightblock4h*(sum((egu,block4h),vVarcost(egu,block4h))+sum((tech,block4h),vVarcosttech(tech,block4h)))
	+ pWeightblockpeaknetramp5h*(sum((egu,blockpeaknetramp5h),vVarcost(egu,blockpeaknetramp5h))+sum((tech,blockpeaknetramp5h),vVarcosttech(tech,blockpeaknetramp5h)))
	+ pWeightblock6h*(sum((egu,block6h),vVarcost(egu,block6h))+sum((tech,block6h),vVarcosttech(tech,block6h)));
co2Ems.. vCO2emsannual =e= pWeightblock0h*(sum((egu,block0h),vCO2ems(egu,block0h))+sum((tech,block0h),vCO2emstech(tech,block0h)))
	+ pWeightblock1h*(sum((egu,block1h),vCO2ems(egu,block1h))+sum((tech,block1h),vCO2emstech(tech,block1h)))
	+ pWeightblockpeaktotal2h*(sum((egu,blockpeaktotal2h),vCO2ems(egu,blockpeaktotal2h))+sum((tech,blockpeaktotal2h),vCO2emstech(tech,blockpeaktotal2h)))
	+ pWeightblockpeaknet3h*(sum((egu,blockpeaknet3h),vCO2ems(egu,blockpeaknet3h))+sum((tech,blockpeaknet3h),vCO2emstech(tech,blockpeaknet3h)))
	+ pWeightblock4h*(sum((egu,block4h),vCO2ems(egu,block4h))+sum((tech,block4h),vCO2emstech(tech,block4h)))
	+ pWeightblockpeaknetramp5h*(sum((egu,blockpeaknetramp5h),vCO2ems(egu,blockpeaknetramp5h))+sum((tech,blockpeaknetramp5h),vCO2emstech(tech,blockpeaknetramp5h)))
	+ pWeightblock6h*(sum((egu,block6h),vCO2ems(egu,block6h))+sum((tech,block6h),vCO2emstech(tech,block6h)));

limitHydroGenblock0h(z)..sum((hydroegu,block0h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,block0h)) =l= pMaxgenhydroblock0h(z);
limitHydroGenblock1h(z)..sum((hydroegu,block1h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,block1h)) =l= pMaxgenhydroblock1h(z);
limitHydroGenblockpeaktotal2h(z)..sum((hydroegu,blockpeaktotal2h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,blockpeaktotal2h)) =l= pMaxgenhydroblockpeaktotal2h(z);
limitHydroGenblockpeaknet3h(z)..sum((hydroegu,blockpeaknet3h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,blockpeaknet3h)) =l= pMaxgenhydroblockpeaknet3h(z);
limitHydroGenblock4h(z)..sum((hydroegu,block4h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,block4h)) =l= pMaxgenhydroblock4h(z);
limitHydroGenblockpeaknetramp5h(z)..sum((hydroegu,blockpeaknetramp5h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,blockpeaknetramp5h)) =l= pMaxgenhydroblockpeaknetramp5h(z);
limitHydroGenblock6h(z)..sum((hydroegu,block6h)$[pGenzone(hydroegu)=ORD(z)],vGen(hydroegu,block6h)) =l= pMaxgenhydroblock6h(z);

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
rampUpblockpeaknetramp5h(egu,blockpeaknetramp5h)$[ORD(blockpeaknetramp5h)>1].. vGen(egu,blockpeaknetramp5h)+vRegup(egu,blockpeaknetramp5h)+vFlex(egu,blockpeaknetramp5h)+vCont(egu,blockpeaknetramp5h) - vGen(egu,blockpeaknetramp5h-1) =l= 
                  pRamprate(egu);
rampUpblockpeaknetramp5htech(tech,blockpeaknetramp5h)$[ORD(blockpeaknetramp5h)>1].. vGentech(tech,blockpeaknetramp5h)+vReguptech(tech,blockpeaknetramp5h)+vFlextech(tech,blockpeaknetramp5h)+vConttech(tech,blockpeaknetramp5h) - vGentech(tech,blockpeaknetramp5h-1) =l= 
                  pRampratetech(tech)*vN(tech);
rampUpblock6h(egu,block6h)$[ORD(block6h)>1].. vGen(egu,block6h)+vRegup(egu,block6h)+vFlex(egu,block6h)+vCont(egu,block6h) - vGen(egu,block6h-1) =l= 
                  pRamprate(egu);
rampUpblock6htech(tech,block6h)$[ORD(block6h)>1].. vGentech(tech,block6h)+vReguptech(tech,block6h)+vFlextech(tech,block6h)+vConttech(tech,block6h) - vGentech(tech,block6h-1) =l= 
                  pRampratetech(tech)*vN(tech);
