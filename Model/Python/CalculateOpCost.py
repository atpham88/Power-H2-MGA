#Michael Craig
#Calculate operational costs of fleet

from operator import *
from AuxFuncs import *

#Returns 1d list of fleet's op costs ($/MWh) w/ or w/out co2 price ($/ton)
#Op cost = HR * FC + VOM [ + Co2EmsRate * CO2Price]
def calcOpCosts(genFleet,scaleLbToShortTon,*co2Price):
    fuelPriceCol = genFleet[0].index('FuelPrice($/MMBtu)')
    print('IN CALCULATEOPCOST')
    AAAA
    hrCol = genFleet[0].index('Heat Rate (Btu/kWh)')
    vomCol = genFleet[0].index('VOM($/MWh)')
    (baseOpCosts,hrs) = calcBaseOpCost(fuelPriceCol,hrCol,vomCol,genFleet)
    randAdderCol = genFleet[0].index('RandOpCostAdder($/MWh)')
    randAdders = [float(row[randAdderCol]) for row in genFleet[1:]] #$/mwh
    opCosts = list(map(add,baseOpCosts,randAdders))
    if len(co2Price) > 0:
        co2Col = genFleet[0].index('CO2EmRate(lb/MMBtu)')
        genCo2EmsRatePerMMbtu = [float(row[co2Col])/scaleLbToShortTon for row in genFleet[1:]] #ton/MMBtu
        genCo2EmsPerMWh = list(map(mul,genCo2EmsRatePerMMbtu,hrs)) #ton/MWh
        opCosts = list(map(add,opCosts,[val*co2Price[0] for val in genCo2EmsPerMWh]))
    return (opCosts,hrs)

#Calculate base op cost: hr*fp + vom
def calcBaseOpCost(fpCol,hrCol,vomCol,fleetOrTechs):
    fuelPrices = [convertCostToTgtYr('fuel',float(row[fpCol])) for row in fleetOrTechs[1:]] #$/mmbtu
    hrs = [float(row[hrCol])/1000 for row in fleetOrTechs[1:]] #mmbtu/mwh
    voms = [float(row[vomCol]) for row in fleetOrTechs[1:]] #$/mwh
    return (list(map(add,voms,map(mul,hrs,fuelPrices))),hrs) #$/mwh

#Calculate op costs for new techs
def calcOpCostsTech(newTechs):
    fuelPriceCol = newTechs[0].index('FuelCost($/MMBtu)')
    hrCol = newTechs[0].index('HR(Btu/kWh)')
    vomCol = newTechs[0].index('VOM(2012$/MWh)')
    baseOpCosts = calcBaseOpCost(fuelPriceCol,hrCol,vomCol,newTechs)[0] #just op costs
    return [val+.05 for val in baseOpCosts]