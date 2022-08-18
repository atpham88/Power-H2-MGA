#Michael Craig
#Sets values for initial condition parameters for UC run, either for first
#run of entire year using assumed values or based on last values in prior run.

import pandas as pd

########### SET INITIAL CONDITION PARAMETERS FOR FIRST UC RUN ##################
#For first UC run of year. Assume all plants initially off w/ no carried MDT
#Inputs: gen fleet
#Outputs: 1d list of initial on/off, gen above min (MWh), & carried MDT values
def setInitCondsFirstDay(genFleet,initSOCFraction):
    onOffInitial = pd.Series(0,index=genFleet['GAMS Symbol'])
    genAboveMinInitial = pd.Series(0,index=genFleet['GAMS Symbol'])
    mdtCarriedInitial = pd.Series(0,index=genFleet['GAMS Symbol'])
    stoRows = genFleet.loc[genFleet['FuelType']=='Energy Storage']
    socInitial = pd.Series(initSOCFraction*stoRows['Nameplate Energy Capacity (MWh)'].astype(float).values,index=stoRows['GAMS Symbol'])
    return (onOffInitial,genAboveMinInitial,mdtCarriedInitial,socInitial)
            
########### SET INITIAL CONDITION PARAMETERS PER PRIOR UC RUN ##################
#Set values for init cond params based on prior UC run
#Inputs: prior UC run results as GAMS object, gen fleet, hours for curr UC run, 
#num days for optim horiz (i.e., keep those results), num days look ahead (need to skip these).
#Outputs: 1d lists of initial on/off & gen above min (MWh) & carried MDT vals
def setInitConds(idx,genFleet,dispatchResults):
    lastHr = idx[0] - pd.Timedelta(hours=1)
    stoRows = genFleet.loc[genFleet['FuelType']=='Energy Storage']
    socInitial = (dispatchResults['vStateofcharge'].loc[lastHr,stoRows['GAMS Symbol']]*1000)
    onOffInitial = dispatchResults['vOnoroff'].loc[lastHr]
    minLoads = genFleet['MinLoad(MWh)']
    minLoads.index = genFleet['GAMS Symbol']
    genAboveMinInitial = (dispatchResults['vGen'].loc[lastHr]*1000-minLoads)
    genAboveMinInitial.loc[genAboveMinInitial<0] = 0
    mdtCarriedInitial = getMdtCarriedInitial(dispatchResults['vTurnoff'].loc[:lastHr],genFleet,lastHr)
    return (onOffInitial,genAboveMinInitial,mdtCarriedInitial,socInitial)

def getMdtCarriedInitial(turnOff,genFleet,lastHr):
    mdtCarriedInitial = pd.Series()
    for g in turnOff:
        mdt = genFleet.loc[genFleet['GAMS Symbol']==g,'MinDownTime(hrs)'].values[0]
        genOff = turnOff[g]
        priorOffs = genOff[genOff == 1]
        if priorOffs.shape[0]==0: #has never turned off
            mdtCarried = 0
        else: #has turned off
            hrsOff = (lastHr - priorOffs.index[-1])/pd.Timedelta(hours=1)
            mdtCarried = max(0,mdt - hrsOff)
        mdtCarriedInitial.loc[g] = mdtCarried
    return mdtCarriedInitial
