##### ISOLATE DATA FOR USE IN CE
#Inputs: , any # of dfs
#Outputs: any # of dfs w/ just hours used in CE
def isolateDataInCEHours(hoursForCE,*args):
    return [df.loc[hoursForCE.index] for df in args]

def isolateDataInCEBlocks(hoursForCE,*args):
    blockDataAll = list()
    for df in args:
        dfInCE = df.loc[hoursForCE.index]
        dfInCE['block'] = hoursForCE
        blockData = dfInCE.groupby(['block']).sum()
        assert((dfInCE.sum().sum() - blockData.sum().sum())<dfInCE.sum().sum()*.0001)
        blockDataAll.append(blockData)
    return blockDataAll