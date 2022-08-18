#Michael Craig
#October 6, 2016
#Add storage units to fleet, as well as some extra columsn for storage parameters

import copy, random

#Inputs: fleet (2d list), storage params (2d list), storage type to model, num 
#storage units to add
#Outputs: fleet w/ storage units added and storage parameters added as columns
def addStorageToGenFleet(fleetUC,storageParams,stoType,numStoToAdd,ocAdderMin,ocAdderMax,
                        regUpCostCoeffs):
    addStoParamColsToFleet(fleetUC,storageParams)
    fleetUC = addStorageUnitsToFleet(fleetUC,storageParams,stoType,numStoToAdd,ocAdderMin,
                                ocAdderMax,regUpCostCoeffs)
    return fleetUC

#Adds storage parameters as columsn to end of fleet, and fills in fleet so even 2d list
def addStoParamColsToFleet(fleetUC,storageParams):
    stoHeads = storageParams[0]
    fleetHeads = fleetUC[0]
    addedCols = 0
    #Add headers
    for stoHead in stoHeads:
        if stoHead not in fleetHeads:
            fleetHeads.append(stoHead)
            addedCols += 1
    #Add empty columns
    emptyCols = ['']*addedCols
    for idx in range(1,len(fleetUC)): fleetUC[idx] += emptyCols

#Adds storage units to bottom of fleet
def addStorageUnitsToFleet(fleetUC,storageParams,stoType,numStoToAdd,ocAdderMin,
                        ocAdderMax,regUpCostCoeffs):
    stoHeadsWithStrData = ['StorageType','PlantType','Modeled Fuels'] #vals that should be strings
    (stoHeads,fleetHeads) = (storageParams[0],fleetUC[0])
    stoTypeCol = stoHeads.index('StorageType')
    stoRow = [row for row in storageParams if row[stoTypeCol]==stoType][0]
    #Fill in values in new storage row
    stoFleetRow = [''] * len(fleetHeads)
    for head in stoHeads:
        if head in fleetHeads:
            if head in stoHeadsWithStrData: val = stoRow[stoHeads.index(head)]
            else: val = float(stoRow[stoHeads.index(head)])
            stoFleetRow[fleetHeads.index(head)] = val
    randAdderCol = fleetUC[0].index('RandOpCostAdder($/MWh)')
    stoFleetRow[randAdderCol] = random.uniform(ocAdderMin,ocAdderMax)
    #Add row to fleet after adding ORIS & unit ID
    (orisCol,unitIdCol) = (fleetHeads.index('ORIS Plant Code'),fleetHeads.index('Unit ID'))
    maxOrisId = max([int(row[orisCol]) for row in fleetUC[1:]])
    stoOris = maxOrisId+1
    for i in range(numStoToAdd): 
        rowToAdd = copy.copy(stoFleetRow)
        rowToAdd[orisCol] = stoOris
        rowToAdd[unitIdCol] = '1'
        fleetUC.append(rowToAdd)
        stoOris += 1
    return copy.deepcopy(fleetUC)

####################### TEST SCRIPT ############################################
# def testScript():
#     fleetUC = [['hey','no','good'],[1,2,3]]
#     sto = [['StorageType','hey','no','x','y'],['b',5,6,7,27]]
#     stoType = 'b'
#     x = addStorageToGenFleet(fleetUC,sto,stoType,1)
#     print('hey',x)

# testScript()