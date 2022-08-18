#Michael Craig
#October 4, 2016
#Define several auxiliary functions that are used by a range of scripts.

import csv

################ READ AND WRITE CSV LISTS
#Read CSV to 2d list
#Input: full file name including dir (str)
#Output: 2d list
def readCSVto2dList(fileNameWithDir):
    with open(fileNameWithDir,'r') as f:
        f = csv.reader(f)
        f = list(f)
    return f

#Write 2d list to CSV
#Input: 2d list, full file name including dir & .csv (str)
def write2dListToCSV(list2d,fileNameWithDir):
    fullFileName=fileNameWithDir
    with open(fullFileName, 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(list2d)
################ 

################ CONVERT DOLLAR YEARS 
#Convert dollar years to 2012 dollars
#CPI from Minneapolis Fed, https://www.minneapolisfed.org/community/teaching-aids/
#cpi-calculator-information/consumer-price-index-and-inflation-rates-1913.
#Inputs: name of parameter of dollar year to convert, parameter value (cost)
#Outputs: cost in 2012 dollars
def convertCostToTgtYr(paramName,cost):    
    paramDollarYears = {'startup':2011,'vom':2012,'fom':2012,'occ':2012,'fuel':2019,'tgt':2012}
    targetDollarYear = 2012
    cpiValues = {2015:237,2014:236.7,2013:233,2012:229.6,2011:224.9,2010:218.1,
            2009:214.5,2008:215.3,2007:207.3,2006:201.6,2005:195.3,2019:255.657}
    return doConversion(paramName,cost,paramDollarYears,targetDollarYear,cpiValues)

#Convert dollar year
def doConversion(paramName,cost,paramDollarYears,targetDollarYear,cpiValues):
    paramDollarYear = paramDollarYears[paramName]
    (cpiTgtYear,cpiParamYear) = (cpiValues[targetDollarYear],cpiValues[paramDollarYear])
    return cost*cpiTgtYear/cpiParamYear
################ 

################ ROTATE 2D LIST FROM HORIZ TO VERT OR VICE VERSA
def rotate(list2d):
    list2drotated = list()
    for col in range(len(list2d[0])):
        list2drotated.append([row[col] for row in list2d])
    return list2drotated
###############