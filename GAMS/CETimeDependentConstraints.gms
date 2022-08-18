Sets
        block0h(h)
        block1h(h)
        blockpeaknet2h(h)
        blockpeaktotal3h(h)
        block4h(h)
        block5h(h)
        blockpeaknetramp6h(h)
        ;

Parameters
        pWeightblock0h
        pWeightblock1h
        pWeightblockpeaknet2h
        pWeightblockpeaktotal3h
        pWeightblock4h
        pWeightblock5h
        pWeightblockpeaknetramp6h
        pInitSOC(storageegu)
        pInitSOCtech(storagetech)
        pHourInitblock0h
        pHourFinalblock0h
        pHourInitblock1h
        pHourFinalblock1h
        pSOCScalarblock1h
        pHourInitblockpeaknet2h
        pHourFinalblockpeaknet2h
        pSOCScalarblockpeaknet2h
        pHourInitblockpeaktotal3h
        pHourFinalblockpeaktotal3h
        pSOCScalarblockpeaktotal3h
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
$load block0h,block1h,blockpeaknet2h,blockpeaktotal3h,block4h,block5h,blockpeaknetramp6h
$load pWeightblock0h,pWeightblock1h,pWeightblockpeaknet2h,pWeightblockpeaktotal3h,pWeightblock4h,pWeightblock5h,pWeightblockpeaknetramp6h
$load pSOCScalarblock1h,pSOCScalarblockpeaknet2h,pSOCScalarblockpeaktotal3h,pSOCScalarblock4h,pSOCScalarblock5h,pSOCScalarblockpeaknetramp6h
$load pInitSOC,pInitSOCtech
$gdxin

pHourInitblock0h = smin(h$block0h(h),ord(h));
pHourFinalblock0h = smax(h$block0h(h),ord(h));
pHourInitblock1h = smin(h$block1h(h),ord(h));
pHourFinalblock1h = smax(h$block1h(h),ord(h));
pHourInitblockpeaknet2h = smin(h$blockpeaknet2h(h),ord(h));
pHourFinalblockpeaknet2h = smax(h$blockpeaknet2h(h),ord(h));
pHourInitblockpeaktotal3h = smin(h$blockpeaktotal3h(h),ord(h));
pHourFinalblockpeaktotal3h = smax(h$blockpeaktotal3h(h),ord(h));
pHourInitblock4h = smin(h$block4h(h),ord(h));
pHourFinalblock4h = smax(h$block4h(h),ord(h));
pHourInitblock5h = smin(h$block5h(h),ord(h));
pHourFinalblock5h = smax(h$block5h(h),ord(h));
pHourInitblockpeaknetramp6h = smin(h$blockpeaknetramp6h(h),ord(h));
pHourFinalblockpeaknetramp6h = smax(h$blockpeaknetramp6h(h),ord(h));

nonInitH(h)= yes;
nonInitH(h)$[ord(h)=pHourInitblock0h] = no;
nonInitH(h)$[ord(h)=pHourInitblock1h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaknet2h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaktotal3h] = no;
nonInitH(h)$[ord(h)=pHourInitblock4h] = no;
nonInitH(h)$[ord(h)=pHourInitblock5h] = no;
nonInitH(h)$[ord(h)=pHourInitblockpeaknetramp6h] = no;

Variables
        vInitSOCblock1h(storageegu)
        vInitSOCblockpeaknet2h(storageegu)
        vInitSOCblockpeaktotal3h(storageegu)
        vInitSOCblock4h(storageegu)
        vInitSOCblock5h(storageegu)
        vInitSOCblockpeaknetramp6h(storageegu)
        vInitSOCblock1htech(storagetech)
        vInitSOCblockpeaknet2htech(storagetech)
        vInitSOCblockpeaktotal3htech(storagetech)
        vInitSOCblock4htech(storagetech)
        vInitSOCblock5htech(storagetech)
        vInitSOCblockpeaknetramp6htech(storagetech)
        vFinalSOCblock0h(storageegu)
        vFinalSOCblock1h(storageegu)
        vFinalSOCblockpeaknet2h(storageegu)
        vFinalSOCblockpeaktotal3h(storageegu)
        vFinalSOCblock4h(storageegu)
        vFinalSOCblock5h(storageegu)
        vFinalSOCblockpeaknetramp6h(storageegu)
        vFinalSOCblock0htech(storagetech)
        vFinalSOCblock1htech(storagetech)
        vFinalSOCblockpeaknet2htech(storagetech)
        vFinalSOCblockpeaktotal3htech(storagetech)
        vFinalSOCblock4htech(storagetech)
        vFinalSOCblock5htech(storagetech)
        vFinalSOCblockpeaknetramp6htech(storagetech)
        vChangeSOCblock0h(storageegu)
        vChangeSOCblock1h(storageegu)
        vChangeSOCblockpeaknet2h(storageegu)
        vChangeSOCblockpeaktotal3h(storageegu)
        vChangeSOCblock4h(storageegu)
        vChangeSOCblock5h(storageegu)
        vChangeSOCblockpeaknetramp6h(storageegu)
        vChangeSOCblock0htech(storagetech)
        vChangeSOCblock1htech(storagetech)
        vChangeSOCblockpeaknet2htech(storagetech)
        vChangeSOCblockpeaktotal3htech(storagetech)
        vChangeSOCblock4htech(storagetech)
        vChangeSOCblock5htech(storagetech)
        vChangeSOCblockpeaknetramp6htech(storagetech)
        ;

Equations
        varCost
        co2Ems
        defSOC(storageegu,h)
        genPlusUpResToSOC(storageegu,h)
setInitSOCblock1hltstorageegu(ltstorageegu)
setInitSOCblockpeaknet2hltstorageegu(ltstorageegu)
setInitSOCblockpeaktotal3hltstorageegu(ltstorageegu)
setInitSOCblock4hltstorageegu(ltstorageegu)
setInitSOCblock5hltstorageegu(ltstorageegu)
setInitSOCblockpeaknetramp6hltstorageegu(ltstorageegu)
        defFinalSOCblock0h(storageegu,h)
        defChangeSOCblock0h(storageegu)
        defFinalSOCblock1h(storageegu,h)
        defChangeSOCblock1h(storageegu)
        defFinalSOCblockpeaknet2h(storageegu,h)
        defChangeSOCblockpeaknet2h(storageegu)
        defFinalSOCblockpeaktotal3h(storageegu,h)
        defChangeSOCblockpeaktotal3h(storageegu)
        defFinalSOCblock4h(storageegu,h)
        defChangeSOCblock4h(storageegu)
        defFinalSOCblock5h(storageegu,h)
        defChangeSOCblock5h(storageegu)
        defFinalSOCblockpeaknetramp6h(storageegu,h)
        defChangeSOCblockpeaknetramp6h(storageegu)
setInitSOCblock1hststorageegu(ststorageegu)
setInitSOCblockpeaknet2hststorageegu(ststorageegu)
setInitSOCblockpeaktotal3hststorageegu(ststorageegu)
setInitSOCblock4hststorageegu(ststorageegu)
setInitSOCblock5hststorageegu(ststorageegu)
setInitSOCblockpeaknetramp6hststorageegu(ststorageegu)
        defSOCtech(storagetech,h)
        genPlusUpResToSOCtech(storagetech,h)
setInitSOCblock1hltstoragetech(ltstoragetech)
setInitSOCblockpeaknet2hltstoragetech(ltstoragetech)
setInitSOCblockpeaktotal3hltstoragetech(ltstoragetech)
setInitSOCblock4hltstoragetech(ltstoragetech)
setInitSOCblock5hltstoragetech(ltstoragetech)
setInitSOCblockpeaknetramp6hltstoragetech(ltstoragetech)
        defFinalSOCblock0htech(storagetech,h)
        defChangeSOCblock0htech(storagetech)
        defFinalSOCblock1htech(storagetech,h)
        defChangeSOCblock1htech(storagetech)
        defFinalSOCblockpeaknet2htech(storagetech,h)
        defChangeSOCblockpeaknet2htech(storagetech)
        defFinalSOCblockpeaktotal3htech(storagetech,h)
        defChangeSOCblockpeaktotal3htech(storagetech)
        defFinalSOCblock4htech(storagetech,h)
        defChangeSOCblock4htech(storagetech)
        defFinalSOCblock5htech(storagetech,h)
        defChangeSOCblock5htech(storagetech)
        defFinalSOCblockpeaknetramp6htech(storagetech,h)
        defChangeSOCblockpeaknetramp6htech(storagetech)
setInitSOCblock1hststoragetech(ststoragetech)
setInitSOCblockpeaknet2hststoragetech(ststoragetech)
setInitSOCblockpeaktotal3hststoragetech(ststoragetech)
setInitSOCblock4hststoragetech(ststoragetech)
setInitSOCblock5hststoragetech(ststoragetech)
setInitSOCblockpeaknetramp6hststoragetech(ststoragetech)
        rampUpblock0h(egu,block0h)
        rampUpblock1h(egu,block1h)
        rampUpblockpeaknet2h(egu,blockpeaknet2h)
        rampUpblockpeaktotal3h(egu,blockpeaktotal3h)
        rampUpblock4h(egu,block4h)
        rampUpblock5h(egu,block5h)
        rampUpblockpeaknetramp6h(egu,blockpeaknetramp6h)
        rampUpblock0htech(tech,block0h)
        rampUpblock1htech(tech,block1h)
        rampUpblockpeaknet2htech(tech,blockpeaknet2h)
        rampUpblockpeaktotal3htech(tech,blockpeaktotal3h)
        rampUpblock4htech(tech,block4h)
        rampUpblock5htech(tech,block5h)
        rampUpblockpeaknetramp6htech(tech,blockpeaknetramp6h)
        ;

defSOC(storageegu,h).. vStateofcharge(storageegu,h) =e= pInitSOC(storageegu)$[ord(h)=pHourInitblock0h] + vInitSOCblock1h(storageegu)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaknet2h(storageegu)$[ord(h)=pHourInitblockpeaknet2h] + vInitSOCblockpeaktotal3h(storageegu)$[ord(h)=pHourInitblockpeaktotal3h] + vInitSOCblock4h(storageegu)$[ord(h)=pHourInitblock4h] + vInitSOCblock5h(storageegu)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6h(storageegu)$[ord(h)=pHourInitblockpeaknetramp6h] +
        vStateofcharge(storageegu, h-1)$nonInitH(h) -
               1/sqrt(pEfficiency(storageegu)) * vGen(storageegu,h) +
               sqrt(pEfficiency(storageegu)) * vCharge(storageegu,h);
genPlusUpResToSOC(storageegu,h).. vGen(storageegu,h)+vRegup(storageegu,h)+vFlex(storageegu,h)+vCont(storageegu,h) =l= vStateofcharge(storageegu, h-1)$nonInitH(h)
                     + pInitSOC(storageegu)$[ord(h)=pHourInitblock0h] + vInitSOCblock1h(storageegu)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaknet2h(storageegu)$[ord(h)=pHourInitblockpeaknet2h] + vInitSOCblockpeaktotal3h(storageegu)$[ord(h)=pHourInitblockpeaktotal3h] + vInitSOCblock4h(storageegu)$[ord(h)=pHourInitblock4h] + vInitSOCblock5h(storageegu)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6h(storageegu)$[ord(h)=pHourInitblockpeaknetramp6h];
setInitSOCblock1hltstorageegu(ltstorageegu).. vInitSOCblock1h(ltstorageegu) =e= vFinalSOCblock0h(ltstorageegu) + vChangeSOCblock0h(ltstorageegu)*pSOCScalarblock1h
                        ;
setInitSOCblockpeaknet2hltstorageegu(ltstorageegu).. vInitSOCblockpeaknet2h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblockpeaknet2h
                        ;
setInitSOCblockpeaktotal3hltstorageegu(ltstorageegu).. vInitSOCblockpeaktotal3h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblockpeaktotal3h + vChangeSOCblockpeaknet2h(ltstorageegu)
                        ;
setInitSOCblock4hltstorageegu(ltstorageegu).. vInitSOCblock4h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu) + vChangeSOCblock1h(ltstorageegu)*pSOCScalarblock4h + vChangeSOCblockpeaknet2h(ltstorageegu)+ vChangeSOCblockpeaktotal3h(ltstorageegu)
                        ;
setInitSOCblock5hltstorageegu(ltstorageegu).. vInitSOCblock5h(ltstorageegu) =e= vFinalSOCblock4h(ltstorageegu) + vChangeSOCblock4h(ltstorageegu)*pSOCScalarblock5h
                        ;
setInitSOCblockpeaknetramp6hltstorageegu(ltstorageegu).. vInitSOCblockpeaknetramp6h(ltstorageegu) =e= vFinalSOCblock5h(ltstorageegu) + vChangeSOCblock5h(ltstorageegu)*pSOCScalarblockpeaknetramp6h
                        ;
defFinalSOCblock0h(ltstorageegu,h)$[ord(h)=pHourFinalblock0h].. vFinalSOCblock0h(ltstorageegu) =e=
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock0h(ltstorageegu).. vChangeSOCblock0h(ltstorageegu) =e= vFinalSOCblock0h(ltstorageegu)
                              - pInitSOC(ltstorageegu);
defFinalSOCblock1h(ltstorageegu,h)$[ord(h)=pHourFinalblock1h].. vFinalSOCblock1h(ltstorageegu) =e=
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblock1h(ltstorageegu).. vChangeSOCblock1h(ltstorageegu) =e= vFinalSOCblock1h(ltstorageegu)
                              - vInitSOCblock1h(ltstorageegu);
defFinalSOCblockpeaknet2h(ltstorageegu,h)$[ord(h)=pHourFinalblockpeaknet2h].. vFinalSOCblockpeaknet2h(ltstorageegu) =e=
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblockpeaknet2h(ltstorageegu).. vChangeSOCblockpeaknet2h(ltstorageegu) =e= vFinalSOCblockpeaknet2h(ltstorageegu)
                              - vInitSOCblockpeaknet2h(ltstorageegu);
defFinalSOCblockpeaktotal3h(ltstorageegu,h)$[ord(h)=pHourFinalblockpeaktotal3h].. vFinalSOCblockpeaktotal3h(ltstorageegu) =e=
                           vStateofcharge(ltstorageegu,h);
defChangeSOCblockpeaktotal3h(ltstorageegu).. vChangeSOCblockpeaktotal3h(ltstorageegu) =e= vFinalSOCblockpeaktotal3h(ltstorageegu)
                              - vInitSOCblockpeaktotal3h(ltstorageegu);
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
setInitSOCblock1hststorageegu(ststorageegu).. vInitSOCblock1h(ststorageegu) =l=
                                    pInitSOC(ststorageegu);
setInitSOCblockpeaknet2hststorageegu(ststorageegu).. vInitSOCblockpeaknet2h(ststorageegu) =l=
                                    pInitSOC(ststorageegu);
setInitSOCblockpeaktotal3hststorageegu(ststorageegu).. vInitSOCblockpeaktotal3h(ststorageegu) =l=
                                    pInitSOC(ststorageegu);
setInitSOCblock4hststorageegu(ststorageegu).. vInitSOCblock4h(ststorageegu) =l=
                                    pInitSOC(ststorageegu);
setInitSOCblock5hststorageegu(ststorageegu).. vInitSOCblock5h(ststorageegu) =l=
                                    pInitSOC(ststorageegu);
setInitSOCblockpeaknetramp6hststorageegu(ststorageegu).. vInitSOCblockpeaknetramp6h(ststorageegu) =l=
                                    pInitSOC(ststorageegu);

defSOCtech(storagetech,h).. vStateofchargetech(storagetech,h) =e= pInitSOCtech(storagetech)$[ord(h)=pHourInitblock0h]*vEneBuiltSto(storagetech) + vInitSOCblock1htech(storagetech)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaknet2htech(storagetech)$[ord(h)=pHourInitblockpeaknet2h] + vInitSOCblockpeaktotal3htech(storagetech)$[ord(h)=pHourInitblockpeaktotal3h] + vInitSOCblock4htech(storagetech)$[ord(h)=pHourInitblock4h] + vInitSOCblock5htech(storagetech)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6htech(storagetech)$[ord(h)=pHourInitblockpeaknetramp6h] +
        vStateofchargetech(storagetech, h-1)$nonInitH(h) -
               1/sqrt(pEfficiencytech(storagetech)) * vGentech(storagetech,h) +
               sqrt(pEfficiencytech(storagetech)) * vChargetech(storagetech,h);
genPlusUpResToSOCtech(storagetech,h).. vGentech(storagetech,h)+vReguptech(storagetech,h)+vFlextech(storagetech,h)+vConttech(storagetech,h) =l= vStateofchargetech(storagetech, h-1)$nonInitH(h)
                     + pInitSOCtech(storagetech)$[ord(h)=pHourInitblock0h]*vEneBuiltSto(storagetech) + vInitSOCblock1htech(storagetech)$[ord(h)=pHourInitblock1h] + vInitSOCblockpeaknet2htech(storagetech)$[ord(h)=pHourInitblockpeaknet2h] + vInitSOCblockpeaktotal3htech(storagetech)$[ord(h)=pHourInitblockpeaktotal3h] + vInitSOCblock4htech(storagetech)$[ord(h)=pHourInitblock4h] + vInitSOCblock5htech(storagetech)$[ord(h)=pHourInitblock5h] + vInitSOCblockpeaknetramp6htech(storagetech)$[ord(h)=pHourInitblockpeaknetramp6h];
setInitSOCblock1hltstoragetech(ltstoragetech).. vInitSOCblock1htech(ltstoragetech) =e= vFinalSOCblock0htech(ltstoragetech) + vChangeSOCblock0htech(ltstoragetech)*pSOCScalarblock1h
                        ;
setInitSOCblockpeaknet2hltstoragetech(ltstoragetech).. vInitSOCblockpeaknet2htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblockpeaknet2h
                        ;
setInitSOCblockpeaktotal3hltstoragetech(ltstoragetech).. vInitSOCblockpeaktotal3htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblockpeaktotal3h + vChangeSOCblockpeaknet2htech(ltstoragetech)
                        ;
setInitSOCblock4hltstoragetech(ltstoragetech).. vInitSOCblock4htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech) + vChangeSOCblock1htech(ltstoragetech)*pSOCScalarblock4h + vChangeSOCblockpeaknet2htech(ltstoragetech)+ vChangeSOCblockpeaktotal3htech(ltstoragetech)
                        ;
setInitSOCblock5hltstoragetech(ltstoragetech).. vInitSOCblock5htech(ltstoragetech) =e= vFinalSOCblock4htech(ltstoragetech) + vChangeSOCblock4htech(ltstoragetech)*pSOCScalarblock5h
                        ;
setInitSOCblockpeaknetramp6hltstoragetech(ltstoragetech).. vInitSOCblockpeaknetramp6htech(ltstoragetech) =e= vFinalSOCblock5htech(ltstoragetech) + vChangeSOCblock5htech(ltstoragetech)*pSOCScalarblockpeaknetramp6h
                        ;
defFinalSOCblock0htech(ltstoragetech,h)$[ord(h)=pHourFinalblock0h].. vFinalSOCblock0htech(ltstoragetech) =e=
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock0htech(ltstoragetech).. vChangeSOCblock0htech(ltstoragetech) =e= vFinalSOCblock0htech(ltstoragetech)
                              - pInitSOCtech(ltstoragetech)*vEneBuiltSto(ltstoragetech);
defFinalSOCblock1htech(ltstoragetech,h)$[ord(h)=pHourFinalblock1h].. vFinalSOCblock1htech(ltstoragetech) =e=
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblock1htech(ltstoragetech).. vChangeSOCblock1htech(ltstoragetech) =e= vFinalSOCblock1htech(ltstoragetech)
                              - vInitSOCblock1htech(ltstoragetech);
defFinalSOCblockpeaknet2htech(ltstoragetech,h)$[ord(h)=pHourFinalblockpeaknet2h].. vFinalSOCblockpeaknet2htech(ltstoragetech) =e=
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblockpeaknet2htech(ltstoragetech).. vChangeSOCblockpeaknet2htech(ltstoragetech) =e= vFinalSOCblockpeaknet2htech(ltstoragetech)
                              - vInitSOCblockpeaknet2htech(ltstoragetech);
defFinalSOCblockpeaktotal3htech(ltstoragetech,h)$[ord(h)=pHourFinalblockpeaktotal3h].. vFinalSOCblockpeaktotal3htech(ltstoragetech) =e=
                           vStateofchargetech(ltstoragetech,h);
defChangeSOCblockpeaktotal3htech(ltstoragetech).. vChangeSOCblockpeaktotal3htech(ltstoragetech) =e= vFinalSOCblockpeaktotal3htech(ltstoragetech)
                              - vInitSOCblockpeaktotal3htech(ltstoragetech);
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
setInitSOCblock1hststoragetech(ststoragetech).. vInitSOCblock1htech(ststoragetech) =l=
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblockpeaknet2hststoragetech(ststoragetech).. vInitSOCblockpeaknet2htech(ststoragetech) =l=
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblockpeaktotal3hststoragetech(ststoragetech).. vInitSOCblockpeaktotal3htech(ststoragetech) =l=
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblock4hststoragetech(ststoragetech).. vInitSOCblock4htech(ststoragetech) =l=
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblock5hststoragetech(ststoragetech).. vInitSOCblock5htech(ststoragetech) =l=
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);
setInitSOCblockpeaknetramp6hststoragetech(ststoragetech).. vInitSOCblockpeaknetramp6htech(ststoragetech) =l=
                                    pInitSOCtech(ststoragetech)*vEneBuiltSto(ststoragetech);

varCost.. vVarcostannual =e= pWeightblock0h*(sum((egu,block0h),vVarcost(egu,block0h))+sum((tech,block0h),vVarcosttech(tech,block0h)))
        + pWeightblock1h*(sum((egu,block1h),vVarcost(egu,block1h))+sum((tech,block1h),vVarcosttech(tech,block1h)))
        + pWeightblockpeaknet2h*(sum((egu,blockpeaknet2h),vVarcost(egu,blockpeaknet2h))+sum((tech,blockpeaknet2h),vVarcosttech(tech,blockpeaknet2h)))
        + pWeightblockpeaktotal3h*(sum((egu,blockpeaktotal3h),vVarcost(egu,blockpeaktotal3h))+sum((tech,blockpeaktotal3h),vVarcosttech(tech,blockpeaktotal3h)))
        + pWeightblock4h*(sum((egu,block4h),vVarcost(egu,block4h))+sum((tech,block4h),vVarcosttech(tech,block4h)))
        + pWeightblock5h*(sum((egu,block5h),vVarcost(egu,block5h))+sum((tech,block5h),vVarcosttech(tech,block5h)))
        + pWeightblockpeaknetramp6h*(sum((egu,blockpeaknetramp6h),vVarcost(egu,blockpeaknetramp6h))+sum((tech,blockpeaknetramp6h),vVarcosttech(tech,blockpeaknetramp6h)));
co2Ems.. vCO2emsannual =e= pWeightblock0h*(sum((egu,block0h),vCO2ems(egu,block0h))+sum((tech,block0h),vCO2emstech(tech,block0h)))
        + pWeightblock1h*(sum((egu,block1h),vCO2ems(egu,block1h))+sum((tech,block1h),vCO2emstech(tech,block1h)))
        + pWeightblockpeaknet2h*(sum((egu,blockpeaknet2h),vCO2ems(egu,blockpeaknet2h))+sum((tech,blockpeaknet2h),vCO2emstech(tech,blockpeaknet2h)))
        + pWeightblockpeaktotal3h*(sum((egu,blockpeaktotal3h),vCO2ems(egu,blockpeaktotal3h))+sum((tech,blockpeaktotal3h),vCO2emstech(tech,blockpeaktotal3h)))
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
rampUpblockpeaknet2h(egu,blockpeaknet2h)$[ORD(blockpeaknet2h)>1].. vGen(egu,blockpeaknet2h)+vRegup(egu,blockpeaknet2h)+vFlex(egu,blockpeaknet2h)+vCont(egu,blockpeaknet2h) - vGen(egu,blockpeaknet2h-1) =l=
                  pRamprate(egu);
rampUpblockpeaknet2htech(tech,blockpeaknet2h)$[ORD(blockpeaknet2h)>1].. vGentech(tech,blockpeaknet2h)+vReguptech(tech,blockpeaknet2h)+vFlextech(tech,blockpeaknet2h)+vConttech(tech,blockpeaknet2h) - vGentech(tech,blockpeaknet2h-1) =l=
                  pRampratetech(tech)*vN(tech);
rampUpblockpeaktotal3h(egu,blockpeaktotal3h)$[ORD(blockpeaktotal3h)>1].. vGen(egu,blockpeaktotal3h)+vRegup(egu,blockpeaktotal3h)+vFlex(egu,blockpeaktotal3h)+vCont(egu,blockpeaktotal3h) - vGen(egu,blockpeaktotal3h-1) =l=
                  pRamprate(egu);
rampUpblockpeaktotal3htech(tech,blockpeaktotal3h)$[ORD(blockpeaktotal3h)>1].. vGentech(tech,blockpeaktotal3h)+vReguptech(tech,blockpeaktotal3h)+vFlextech(tech,blockpeaktotal3h)+vConttech(tech,blockpeaktotal3h) - vGentech(tech,blockpeaktotal3h-1) =l=
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
