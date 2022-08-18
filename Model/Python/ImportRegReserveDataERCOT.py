#Michael Craig
#October 6, 2016
#Function provides 2016 reg up & down requirements from ERCOT, as well as
#incremental reg up & down values for each GW of wind added to system.
#Sources: ERCOT AS Requirements_2016 Effective 070116 & 
#ERCOT Methodologies for Determining Ancillary Service Requirements Effective 070116

import os
from AuxFuncs import *

def setKeyParameters(runLoc):
    if runLoc == 'pc': reserveDir = 'C:\\Users\\mtcraig\\Desktop\\EPP Research\\Databases\\ERCOTReserves\\ERCOTMethodsToDetermineASRequirements'
    else: reserveDir = 'Data\\ERCOTReserves'
    filenames = {'up':'ercotRegUp2016.csv','down':'ercotRegDown2016.csv',
                'upInc':'ercotRegUpIncWithWind2016.csv','downInc':'ercotRegDownIncWithWind2016.csv',
                'nonspin':'ercotNonspin2016.csv'}
    daysPerMonth = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,
                    'Sep':30,'Oct':31,'Nov':30,'Dec':31}
    return (reserveDir,filenames,daysPerMonth)

################################################################################
###### MASTER FUNCTION #########################################################
################################################################################
#Function imports 2016 reg up & down requirements from ERCOT (provided for each
#hour of the day for each month, e.g. 1-24 for Jan, 1-24 for Feb, etc.), and
#similarly-formatted incremental reg up & down per GW wind added to system.
#Outputs: hourly reg up & down requirements (1d list, no header), hourly
#incremental reg up & down requirements per GW wind added (1d list, no header)
def importRegReserveData(runLoc):
    (reserveDir,filenames,daysPerMonth) = setKeyParameters(runLoc)
    (hourlyRegUp,hourlyRegDown) = importHourlyReg(reserveDir,filenames,daysPerMonth)
    (hourlyRegUpIncWind,hourlyRegDownIncWind) = importHourlyIncReg(reserveDir,filenames,daysPerMonth)
    hourlyNonspin = importHourlyNonspin(reserveDir,filenames,daysPerMonth)
    return (hourlyRegUp,hourlyRegDown,hourlyRegUpIncWind,hourlyRegDownIncWind,hourlyNonspin)
################################################################################
################################################################################
################################################################################

################################################################################
###### IMPORT REG UP AND DOWN VALUES ###########################################
################################################################################
#Takes in CSV filenames and dir where reg req data is, and outputs
#1d lists of annual hourly reg reqs
def importHourlyReg(reserveDir,filenames,daysPerMonth):
    regUpData = readCSVto2dList(os.path.join(reserveDir,filenames['up']))
    regDownData = readCSVto2dList(os.path.join(reserveDir,filenames['down']))
    return (convertRegDataToHourly1dList(regUpData,daysPerMonth),
            convertRegDataToHourly1dList(regDownData,daysPerMonth))
    
#Converts reg req in form of hour-ending per month to hourly reg data for year
#by getting hourly req for a day, then multiplying that by # days that month.
#Inputs: reg req in hour-ending per month format (2d list, row = month & col = hr)
#Outputs: 1d list of hourly reg req for whole year
def convertRegDataToHourly1dList(rawRegData,daysPerMonth):
    (hrPerDay,firstDataCol) = (24,1)
    rowWithColHeads = [row[0] for row in rawRegData].index('HE')
    firstDataRow = rowWithColHeads + 1
    headerRow = rawRegData[rowWithColHeads]
    hourlyRegReq = []
    for idx in range(firstDataCol,len(headerRow)):
        currMonth = rawRegData[rowWithColHeads][idx].strip()
        hourEndReg = [float(row[idx]) for row in rawRegData[firstDataRow:firstDataRow+hrPerDay]]
        daysInMonth = daysPerMonth[currMonth]
        hourlyRegReq += hourEndReg*daysInMonth
    return hourlyRegReq
################################################################################
################################################################################
################################################################################

################################################################################
###### IMPORT INCREMENTAL REG UP AND DOWN VALUES PER GW WIND ADDED #############
################################################################################
#Takes in CSV filenames and dir where reg req per added GW wind is, and outputs
#1d lists of annual hourly reg incremental req per GW wind
def importHourlyIncReg(reserveDir,filenames,daysPerMonth):
    regUpIncData = readCSVto2dList(os.path.join(reserveDir,filenames['upInc']))
    regDownIncData = readCSVto2dList(os.path.join(reserveDir,filenames['downInc']))
    return (convertRegIncDataToHourly1dList(regUpIncData,daysPerMonth),
            convertRegIncDataToHourly1dList(regDownIncData,daysPerMonth))

#Converts reg req in form of hour-ending per month to hourly reg data for year
#by getting hourly req for a day, then multiplying that by # days that month.
#Inputs: reg req in hour-ending per month format (2d list, row = month & col = hr)
#Outputs: 1d list of hourly reg req for whole year
def convertRegIncDataToHourly1dList(rawRegData,daysPerMonth):
    (hrPerDay,firstDataCol,monthHeadCol) = (24,1,0)
    rowWithColHeads = [row[0] for row in rawRegData].index('Month')
    firstDataRow = rowWithColHeads + 1
    headerCol = rawRegData[monthHeadCol]
    hourlyRegReqInc = []
    for idx in range(firstDataRow,len(rawRegData)):
        currMonth = rawRegData[idx][monthHeadCol].strip() 
        if currMonth != '': #empty line @ end of array; skips that line
            if '.' in currMonth: currMonth = currMonth[:-1]
            hourEndReg = rawRegData[idx][firstDataCol:]
            hourEndReg = [float(val) for val in hourEndReg]
            daysInMonth = daysPerMonth[currMonth]
            hourlyRegReqInc += hourEndReg*daysInMonth
    return hourlyRegReqInc
################################################################################
################################################################################
################################################################################

################################################################################
###### IMPORT NONSPIN RESERVES #################################################
################################################################################
#Use same call as reg reserves, since in same data format
def importHourlyNonspin(reserveDir,filenames,daysPerMonth):
    nonspinData = readCSVto2dList(os.path.join(reserveDir,filenames['nonspin']))
    return convertRegDataToHourly1dList(nonspinData,daysPerMonth)
################################################################################
################################################################################
################################################################################

# importRegReserveData()