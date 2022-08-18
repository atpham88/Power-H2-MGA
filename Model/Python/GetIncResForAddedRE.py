#Michael Craig
#Jan 4, 2017

#Script determines new reserve requirements per unit of RE added by
#capacity expansion model.

from ReservesWWSIS import *
import pandas as pd

#Takes in CFs for hypothetical new wind and solar plants, determines reserve
#requirements for that installed capacity of wind and solar, then normalizes
#reserve requirements to per MW added wind or solar by dividing by hypothetical
#amount of wind and solar added to obtain new CFs.
#Inputs: windIdsAndCapacs (2d list w/ NREL wind IDs used to load gen files),
#solarFilenamesAndCapacs (2d list w/ NREL solar filenames used to load gen files),
#hourly demand, fraction of load included in reg & cont reserves, percentile error
#of wind and solar forecasts included in reg & flex reserves, windCfsDtHr (2d list w/ hourly 
#wind CFs for each wind generator in fleet, col 1 = dt, subsequent cols = gen),
#same formatted 2d lists subhourly wind CFs & solar hourly & subhourly CFs, 
#MW of wind and solar added to fleet in order to get new wind & solar CFs.
#Outputs: dfs for entire year of incremental MW res requirements per MW
#wind or solar added.
def getIncResForAddedRE(newCfs,regErrorPercentile,flexErrorPercentile):
    #Calculate wind reg + flex increase
    windCfs = newCfs[[col for col in newCfs if 'wind' in col]]
    reg = windCfs.apply(calcWindReserves,axis=0,args=(regErrorPercentile,))
    windRegUp = pd.DataFrame(abs(np.array([r[0] for r in reg])).T,columns=reg.index,index=windCfs.index)
    flex = windCfs.apply(calcWindReserves,axis=0,args=(flexErrorPercentile,))
    windFlex = pd.DataFrame(abs(np.array([r[0] for r in flex])).T,columns=flex.index,index=windCfs.index)
    #Calculate solar reg + flex increase
    solarCfs = newCfs[[col for col in newCfs if 'solar' in col]]
    reg = solarCfs.apply(calcSolarReserves,axis=0,args=(regErrorPercentile,))
    solarRegUp = pd.DataFrame(abs(np.array([r[0] for r in reg])).T,columns=reg.index,index=solarCfs.index)
    flex = solarCfs.apply(calcSolarReserves,axis=0,args=(flexErrorPercentile,))
    solarFlex = pd.DataFrame(abs(np.array([r[0] for r in flex])).T,columns=flex.index,index=solarCfs.index)
    return pd.concat([windRegUp,solarRegUp],axis=1),pd.concat([windFlex,solarFlex],axis=1)
