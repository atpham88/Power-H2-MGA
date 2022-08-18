*Michael Craig 16 Apr 2020

Sets
         storageegu(egu)                 storage units
                 ;

Parameters
         pStoinenergymarket              whether storage can provide energy (1) or not (0)
         pEfficiency(storageegu)         round trip storage efficiency
         pCapaccharge(storageegu)        max charging capacity (GW)
         pMaxsoc(storageegu)             max stored energy (GWh)
         pMinsoc(storageegu)             min stored energy (GWh)
                ;

$if not set gdxincname $abort 'no include file name for data file provided'
$gdxin %gdxincname%
$load storageegu, pStoinenergymarket,pEfficiency,pMaxsoc,pMinsoc,pCapaccharge
$gdxin

Positive Variables
         vStateofcharge(storageegu,h)            "energy stored in storage unit at end of hour h (GWh)"
         vCharge(storageegu,h)                   "charged energy by storage unit in hour h (GWh)"
                 ;

*LIMIT GENERATION AND RESERVES
*Bound generation to capacity and ability to participate in energy market
vGen.up(storageegu,h) = pStoinenergymarket * pCapac(storageegu);

*CHARGE CONSTRAINTS
*Place upper bound on charging
vCharge.up(storageegu,h) = pCapaccharge(storageegu);

*STATE OF CHARGE BOUNDS
vStateofcharge.lo(storageegu,h) = pMinsoc(storageegu);
vStateofcharge.up(storageegu,h) = pMaxsoc(storageegu);
