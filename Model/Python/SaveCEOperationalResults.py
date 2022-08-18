#Michael Craig

from AuxFuncs import *
from GAMSAuxFuncs import *
import copy, csv, pandas as pd,os,numpy as np

def saveCapacExpOperationalData(ceModel,genFleet,newTechsCE,hoursForCE,transRegions,lineLimits,resultsDir,modelName,year):
    saveGeneratorResults(ceModel,genFleet,hoursForCE,resultsDir,modelName,year)
    saveGeneratorResults(ceModel,newTechsCE,hoursForCE,resultsDir,modelName,year,True)
    saveZonalSystemResults(ceModel,transRegions,hoursForCE,resultsDir,modelName,year)
    saveLineFlows(ceModel,lineLimits,hoursForCE,resultsDir,modelName,year)
    for n in ['vCO2emsannual','vZannual', 'vVarcostannual','vFixedcostannual']:
        write2dListToCSV([[extract0dVarResultsFromGAMSModel(ceModel,n)]],os.path.join(resultsDir,n + modelName + str(year) + '.csv'))

def saveGeneratorResults(ceModel,gens,hoursForCE,resultsDir,modelName,year,newTechs=False):
    for v in ['vGen','vRegup','vFlex','vCont','vTurnon','vTurnoff','vOnoroff','vCharge','vStateofcharge']:
        v += 'tech' if newTechs else ''
        if v in [i.name for i in ceModel.out_db]:
            df = pd.DataFrame(columns=gens['GAMS Symbol'],index=hoursForCE.index)
            for rec in ceModel.out_db[v]: df.loc[rec.key(1),rec.key(0)] = rec.level
            df.to_csv(os.path.join(resultsDir,v + modelName + str(year) + '.csv'))

def saveLineFlows(ceModel,lineLimits,hoursForCE,resultsDir,modelName,year,varName = 'vLineflow'):
    if varName in [i.name for i in ceModel.out_db]:
        df = pd.DataFrame(columns=lineLimits['GAMS Symbol'].values,index=hoursForCE.index)
        for rec in ceModel.out_db[varName]: df.loc[rec.key(1),rec.key(0)] = rec.level
        df.to_csv(os.path.join(resultsDir,varName + modelName + str(year) + '.csv'))

def saveZonalSystemResults(ceModel,transRegions,hoursForCE,resultsDir,modelName,year):
    resultLabelToEqnName = {'mcGen':'meetdemand','mcRegup':'meetregupreserve',
        'mcFlex':'meetflexreserve','mcCont':'meetcontreserve','vFlex':'vFlexreserve',
        'vRegup':'vRegupreserve'}
    for result,varName in resultLabelToEqnName.items():
        if varName in [i.name for i in ceModel.out_db]:
            df = pd.DataFrame(columns=[r for r in transRegions],index=hoursForCE.index)
            for rec in ceModel.out_db[varName]:
                value = rec.marginal if 'mc' in result else rec.level
                df.loc[rec.key(1),rec.key(0)] = value
                df.to_csv(os.path.join(resultsDir,result + modelName + str(year) + '.csv'))