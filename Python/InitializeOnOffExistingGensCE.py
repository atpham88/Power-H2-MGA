#Michael Craig
#Dec 2, 2016

#Initialize on/off commitment state of existing units for CE model for first
#hour in each time block (seasons + demand day + ramp day).

from operator import *
from AuxFuncs import *
from GAMSAuxFuncs import *
import copy, pandas as pd

#For first hour of each time block, gets gen stack, sorts gens by op cost, then
#meets demand and assigns dispatched gens to "on".
#Inputs: gen fleet, hours + hourly wind & solar gen + demand for CE model (1d list,
#slimmed to CE hours), dict mapping time block to hours in that time block
#Outputs: dict mapping block to dict mapping gen symbol to on/off in first hour of dict.
def initializeOnOffExistingGens(genFleetForCE,hoursForCE,netDemand):
    sortedSymbols,sortedCapacs,reGenSymbols = getGenStack(genFleetForCE)
    blockToOnOff = dict()
    for bl in hoursForCE.unique():
        firstHr = hoursForCE.loc[hoursForCE == bl].index[0]
        hrNetDemand = netDemand.loc[firstHr].values[0]
        genToOnOff = getGenOnOffForHour(sortedSymbols,sortedCapacs,reGenSymbols,hrNetDemand)
        blockToOnOff[bl] = genToOnOff
    return blockToOnOff

#Get gen stack for fleet, returning sorted gen symbols, capacities, and RE gen symbols.
#Sorted in order of least -> most costly.
def getGenStack(genFleetForCE):
    noRE = genFleetForCE.loc[~genFleetForCE['FuelType'].isin(['Wind','Solar'])]
    re = genFleetForCE.drop(noRE.index)
    noRE = noRE.loc[~noRE['FuelType'].isin(['Energy Storage'])]
    noRE.sort_values(by="OpCost($/MWh)",inplace=True)
    noRESymbs = (noRE['ORIS Plant Code'].astype(str) + "+" + noRE['Unit ID'].astype(str))
    return noRE['GAMS Symbol'],noRE['Capacity (MW)'],re['GAMS Symbol']

#For given net demand value in hour, determine which gens should be on by 
#dispatching them using gen stack.
def getGenOnOffForHour(sortedSymbols,sortedCapacs,reGenSymbols,hrNetDemand):
    cumulativeCap = sortedCapacs.cumsum()
    online = cumulativeCap<hrNetDemand
    if False in online.values: online[online[online==False].index[0]] = True #set marginal generator as online
    onGens = sortedSymbols[online[online==True].index]
    genToOnOff = {**pd.Series(1,index=onGens).to_dict(),**pd.Series(1,index=reGenSymbols).to_dict()}
    if False in online.values: 
        offGens = sortedSymbols[online[online==False].index]
        genToOnOff = {**genToOnOff,**pd.Series(0,index=offGens).to_dict()}
    return genToOnOff
    