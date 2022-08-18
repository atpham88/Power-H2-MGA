##### ISOLATE DATA FOR USE IN CE
#Inputs: , any # of dfs
#Outputs: any # of dfs w/ just hours used in CE
def isolateDataInCEHours(hoursForCE,*args):
    return [df.loc[hoursForCE.index] for df in args]
