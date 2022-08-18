#Michael Craig
#October 6, 2016
#Function extracts wind built by CE and scales reg up & down based on added wind.

from operator import *

#Changes reg up & down based on wind built in CE model
#Inputs: annual hourly reg up & down req & hourly change in regup & down per 1000 MW 
#wind added (1d lists w/out headers), new gens added by capac exp (list of (tech,num built) tuples),
#new techs data (2d list)
#Outputs: new annual hourly reg up & down req (1d list, no header)
def scaleRegResForAddedWind(hourlyRegUp,hourlyRegDown,hourlyRegUpIncWind,hourlyRegDownIncWind,
                            newGenerators,newTechsCE):
    mwToGw = 1000
    (numWindBuilt,windName) = (0,'Wind')
    for (tech,newBuilds) in newGenerators:
        if tech==windName: numWindBuilt = newBuilds 
    addedWindCapac = numWindBuilt * getWindTechCapac(newTechsCE,windName)
    regUpChange = [inc*addedWindCapac/mwToGw for inc in hourlyRegUpIncWind]
    regDownChange = [inc*addedWindCapac/mwToGw for inc in hourlyRegDownIncWind]
    newRegUp = list(map(add,regUpChange,hourlyRegUp))
    newRegDown = list(map(add,regUpChange,hourlyRegDown))
    return (newRegUp,newRegDown)

def getWindTechCapac(newTechsCE,windName):
    techCol = newTechsCE[0].index('TechnologyType')
    capacCol = newTechsCE[0].index('Capacity(MW)')
    windRow = [row for row in newTechsCE[1:] if row[techCol]==windName][0]
    return int(windRow[capacCol])

############# TEST SCRIPT ######################################################
# from AuxFuncs import *
# import os
# def testScript():
#     hourlyRegUp=[1,2,3,4,5,6]
#     hourlyRegDown=[10,11,12,13,14,15]
#     hourlyRegUpIncWind=[2,2,2,4,4,4]
#     hourlyRegDownIncWind=[3,3,3,1,1,1]
#     newGenerators = [('coal',5),('solar',10),('Wind',0)]
#     techDir = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\NewPlantData'
#     techFile = 'CandidateTechsCapacExp.csv'
#     newTechsCE = readCSVto2dList(os.path.join(techDir,techFile))
#     (newUp,newDown) = scaleRegResForAddedWind(hourlyRegUp,hourlyRegDown,
#                     hourlyRegUpIncWind,hourlyRegDownIncWind,newGenerators,newTechsCE)

# testScript()