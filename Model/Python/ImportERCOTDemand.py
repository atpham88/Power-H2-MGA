#Michael Craig
#October 6, 2014
#Import hourly ERCOT demand data from CSVs, return in 1d list w/out header

import os, csv, pandas as pd, numpy as np
from AuxFuncs import *

#Extract hourly ERCOT demand from given year, and return it in 1d list w/out headers
#Drop leap day (feb 29) from demand to align w/ MERRA data
def importHourlyERCOTDemand(demandYear):
    #Set filename and directory
    filename = 'Native_Load_' + str(demandYear) + '.csv'
    demandDir = os.path.join('Data','ERCOTDemand')
    #Read into pd
    rawDemand = pd.read_csv(os.path.join(demandDir,filename),delimiter=',',index_col='HourEnding')
    demand = rawDemand['ERCOT']
    leapDays=demand.index[demand.index.str.find("02/29",0,10) != -1]
    demand.drop(leapDays, inplace=True) 
    print(demand)
    print(demand.dtypes())
    demand.atpe(float)
    return demand

# #This is for importing cleaned BA data from Ruggles: https://zenodo.org/record/3690240
# def get_demand_data(demand_file_in, year_in, hrsShift=0):
#     demand_data = pd.read_csv(demand_file_in,delimiter=',',usecols=["date_time","cleaned demand (MW)"],index_col="date_time")

#     # Remove Leap Days
#     leap_days=demand_data.index[demand_data.index.str.find("-02-29",0,10) != -1]
#     demand_data.drop(leap_days, inplace=True) 
#         # two date_time formats from eia cleaned data
#     leap_days=demand_data.index[demand_data.index.str.find(str(year_in)+"0229",0,10) != -1]
#     demand_data.drop(leap_days, inplace=True)

#     # Find Given Year
#     hourly_load = np.array(demand_data["cleaned demand (MW)"][demand_data.index.str.find(str(year_in),0,10) != -1].values)

#     # Shift load
#     if hrsShift!=0:
#         newLoad = np.array([0]*abs(hrsShift))
#         if hrsShift>0:
#             hourly_load = np.concatenate([newLoad,hourly_load[:(hourly_load.shape[0]-hrsShift)]])
#         else:
#             hourly_load = np.concatenate([hourly_load[abs(hrsShift):],newLoad])

#     # Error Handling
#     if(hourly_load.size != 8760):
#         print("Demand Error. Expected array of size 8760. Found:",hourly_load.size)
#         return -1

#     return hourly_load
