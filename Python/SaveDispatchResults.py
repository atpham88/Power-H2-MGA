#Michael Craig

import os,time

#### SAVING RESULTS INTO DATAFRAMES WITH DATETIME INDEX; BUT NOT GETTING DATETIME OUT OF GAMS!
def saveDispatchResults(dispatchResults,sysResults,opsModel,yearDtIdx,dayDtIdx):
    t0 = time.time()
    #Save hourly plant operations
    for k in dispatchResults:
        if k in [r.name for r in opsModel.out_db]:
            for rec in opsModel.out_db[k]:  #out_db[k] returns dict of (gen,hour):value
                hr = int(rec.key(1)[1:]) #h1 -> 1
                dispatchResults[k].loc[yearDtIdx[hr],rec.key(0)] = float(rec.level)
    #Save system level results
    resultToEqn = {'mcGen':'meetdemand','mcRegup':'meetregupreserve',
        'mcFlex':'meetflexreserve','mcCont':'meetcontreserve'}
    for k in sysResults:
        modelName = resultToEqn[k] if 'mc' in k else k
        if modelName in [r.name for r in opsModel.out_db]:
            for rec in opsModel.out_db[modelName]:
                if k != 'vZ':
                    hr = int(rec.key(0)[1:]) #h1 -> 1
                    sysResults.loc[yearDtIdx[hr],k] = float(rec.marginal if 'mc' in k else rec.level)
                else:
                    sysResults.loc[dayDtIdx[0],k] = float(rec.level)
    return dispatchResults,sysResults

def writeDispatchResults(dispatchResults,sysResults,msAndSs,resultsDir,currYear):
    for r in dispatchResults:
        dispatchResults[r].to_csv(os.path.join(resultsDir,'dispatchResult'+r+str(currYear)+'.csv'))
    sysResults.to_csv(os.path.join(resultsDir,'dispatchResultSystem'+str(currYear)+'.csv'))
    msAndSs.to_csv(os.path.join(resultsDir,'dispatchResultsMsAndSs' + str(currYear) + '.csv'))
        
    