#Michael Craig
#October 4, 2016
#Helper functions for Python-GAMS interaction

def createHourSymbol(hour):
    return 'h' + str(hour)

def extract0dVarResultsFromGAMSModel(gamsModel,varName):
    for rec in gamsModel.out_db[varName]: varValue = rec.level
    return varValue

def extract1dVarResultsFromGAMSModel(modelResults,varName):
    varResults = dict()
    for rec in modelResults.out_db[varName]: varResults[rec.key(0)] = rec.level
    return varResults

def extract2dVarResultsIntoDict(modelResults,varName):
    varResultsDict = dict()
    for rec in modelResults.out_db[varName]:
        varResultsDict[(rec.key(0),rec.key(1))] = rec.level
    return varResultsDict

def extract2dVarResultsIntoDictNoLA(modelResults,varName,hoursOpt):
    varResultsDict = dict()
    hoursOptSet = set(hoursOpt)
    for rec in modelResults.out_db[varName]:
        (gen,hour) = (rec.key(0),rec.key(1)) #Vars are indexed as egu,h
        if hour in hoursOptSet: varResultsDict[(gen,hour)] = rec.level
    return varResultsDict
