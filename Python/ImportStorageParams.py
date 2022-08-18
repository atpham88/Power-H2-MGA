#Michael Craig, 15 Apr 2020

import os
from AuxFuncs import *

########### IMPORT STORAGE PARAMETERS ##########################################
def importStorageParams(runLoc,scenario):
    if runLoc == 'pc': stoDir = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\StorageParameters'
    else: stoDir = 'Data'
    if scenario == 'highSto': stoFile = 'StorageParams18Jan17HighSto.csv'
    elif scenario == 'highStoEff': stoFile = 'StorageParams18Jan17HighStoEff.csv'
    else: stoFile = 'StorageParams18Jan17.csv'
    return readCSVto2dList(os.path.join(stoDir,stoFile)) 

########### ADD REG COST AND OFFER TO STO PARAMETERS ###########################
def addRegCostAndOfferEligToStoParams(regUpCostCoeffsUC,storageParams):
    storageParams[0].extend(['RegOfferCost($/MW)','RegOfferElig'])
    stoTypeCol = storageParams[0].index('StorageType')
    for row in storageParams[1:]: 
        if row[stoTypeCol] in regUpCostCoeffsUC: regOfferCost,regOfferElig = regUpCostCoeffsUC[row[stoTypeCol]],1
        else: regOfferCost,regOfferElig = 0,0
        row.extend([regOfferCost,regOfferElig])
