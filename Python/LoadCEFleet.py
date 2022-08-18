#Michael Craig
#Jan 25, 2017
#Loads CE fleet w/out retired units for given year for input to UC model

from AuxFuncs import *
import os,csv

################################################################################
####### LOAD CE FLEET FOR UC YEAR ##############################################
################################################################################
def loadCEFleet(year,resultsDir):
    fleetFileName = 'genFleetCEtoUC' + str(year) + '.csv'
    genFleetNoRetiredUnits = readCSVto2dList(os.path.join(resultsDir,'CEtoUC',fleetFileName))
    return genFleetNoRetiredUnits
################################################################################
################################################################################
################################################################################
