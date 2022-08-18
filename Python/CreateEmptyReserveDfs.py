import pandas as pd
import numpy as np

def createEmptyReserveDfs(windGenRegion,newCfs=None):
    #Reserves
    regUp = pd.DataFrame(0,columns=windGenRegion.columns,index=windGenRegion.index)
    flex,cont,regDemand,regUpSolar,regUpWind,flexSolar,flexWind = regUp.copy(),regUp.copy(),regUp.copy(),regUp.copy(),regUp.copy(),regUp.copy(),regUp.copy()
    #Reserves for new plants - only run this for CE model
    if newCfs is not None: 
        windCfs = newCfs[[col for col in newCfs if 'wind' in col]]
        windRegUp = pd.DataFrame(np.zeros((windCfs.shape[0],windCfs.shape[1])),columns=windCfs.columns,index=windCfs.index)
        windFlex = pd.DataFrame(np.zeros((windCfs.shape[0],windCfs.shape[1])),columns=windCfs.columns,index=windCfs.index)
        solarCfs = newCfs[[col for col in newCfs if 'solar' in col]]
        solarRegUp = pd.DataFrame(np.zeros((solarCfs.shape[0],solarCfs.shape[1])),columns=solarCfs.columns,index=solarCfs.index)
        solarFlex = pd.DataFrame(np.zeros((solarCfs.shape[0],solarCfs.shape[1])),columns=solarCfs.columns,index=solarCfs.index)
        regUpInc,flexInc = pd.concat([windRegUp,solarRegUp],axis=1),pd.concat([windFlex,solarFlex],axis=1)
    else:
        regUpInc,flexInc = None,None
    return cont,regUp,flex,regDemand,regUpSolar,regUpWind,flexSolar,flexWind,regUpInc,flexInc
