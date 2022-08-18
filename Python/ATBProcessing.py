

import os, copy
import pandas as pd
import xlsxwriter as xw

from AuxFuncs import *

atbScenario = 'Advanced'            # Conservative, Moderate, Advanced
convert2019to2012Dollars = 0.8958
crpYearsSO = 20                     # CRP years for solar PV (20 or 30)
crpYearsWI = 30                     # CRP years for wind (20 or 30)
crpYearsES = 20                     # CRP years for energy storage (20 or 30)
crpYearsFO = 75                     # CRP years for coal (20 or 30 or 75)
crpYearsCC = 55                     # CRP years for natural gas (20 or 30 or 55)
crpYearsNU = 60                     # CRP years for nuclear (20 or 30 or 60)
coreMetricCase = "Market"           # Or R&D

plantType = ['Solar PV','Wind','Coal Steam','Coal Steam CCS','Combined Cycle',
             'Combined Cycle CCS','Combustion Turbine','Nuclear','Battery Storage']
params = ['Heat Rate (Btu/kWh)','CAPEX(2012$/MW)', 'FOM(2012$/MW/yr)', 'VOM(2012$/MWh)']
yearAvail = list(range(2020,2051))
T = list(range(31))

atbDir = "C:\\Users\\atpha\\Documents\\Research\\ATB\\2021\\"
abtDesDir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\NewPlantData\\"
atbOrig = pd.read_csv(atbDir+'ATBe.csv')
atbOrigXls_Coal = pd.read_excel(atbDir + '2021-ATB-Data_Master_new.xlsx', sheet_name='Coal_FE')
atbOrigXls_Gas = pd.read_excel(atbDir + '2021-ATB-Data_Master_new.xlsx', sheet_name='Natural Gas_FE')
atbOrigXls_Nuclear = pd.read_excel(atbDir + '2021-ATB-Data_Master_new.xlsx', sheet_name='Nuclear')
atbOrigXls_Bat = pd.read_excel(atbDir + '2021-ATB-Data_Master_new.xlsx', sheet_name='Utility-Scale Battery Storage')

# Set up the excel file
results_book = xw.Workbook(abtDesDir + 'atbProcessed_'+atbScenario+'.xlsx')
result_sheet_atb = results_book.add_worksheet('atbProcessed')

for item in T:
    result_sheet_atb.write(0, item + 2, yearAvail[item])

result_sheet_atb.write("A1", "PlantType")
result_sheet_atb.write("B1", "Parameter")

for item in list(range(3)):
    result_sheet_atb.write(item + 1, 0, plantType[0])
    result_sheet_atb.write(item + 4, 0, plantType[1])
    result_sheet_atb.write(item + 1, 1, params[item+1])
    result_sheet_atb.write(item + 4, 1, params[item+1])

for item in list(range(4)):
    result_sheet_atb.write(item + 7, 0, plantType[2])
    result_sheet_atb.write(item + 11, 0, plantType[3])
    result_sheet_atb.write(item + 15, 0, plantType[4])
    result_sheet_atb.write(item + 19, 0, plantType[5])
    result_sheet_atb.write(item + 23, 0, plantType[6])
    result_sheet_atb.write(item + 27, 0, plantType[7])
    result_sheet_atb.write(item + 31, 0, plantType[8])
    result_sheet_atb.write(item + 7, 1, params[item])
    result_sheet_atb.write(item + 11, 1, params[item])
    result_sheet_atb.write(item + 15, 1, params[item])
    result_sheet_atb.write(item + 19, 1, params[item])
    result_sheet_atb.write(item + 23, 1, params[item])
    result_sheet_atb.write(item + 27, 1, params[item])
    if item <3: item2 = item+1
    elif item ==3: item2 = 0
    result_sheet_atb.write(item + 31, 1, params[item2])
result_sheet_atb.write("B35", 'Efficiency')

# Solar:
solar_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'UtilityPV') & (atbOrig['techdetail'] == 'Class2')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsSO) & (atbOrig['crpyears'] == crpYearsSO) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
solar_CAPEX = solar_CAPEX.reset_index()
solar_CAPEX = solar_CAPEX.drop(['index'], axis=1)
solar_FOM = atbOrig.loc[((atbOrig['technology'] == 'UtilityPV') & (atbOrig['techdetail'] == 'Class2')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsSO) & (atbOrig['crpyears'] == crpYearsSO) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
solar_FOM = solar_FOM.reset_index()
solar_FOM = solar_FOM.drop(['index'], axis=1)
solar_VOM = atbOrig.loc[((atbOrig['technology'] == 'UtilityPV') & (atbOrig['techdetail'] == 'Class2')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsSO) & (atbOrig['crpyears'] == crpYearsSO) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
solar_VOM = solar_VOM.reset_index()
solar_VOM = solar_VOM.drop(['index'], axis=1)

# Wind:
wind_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'LandbasedWind') & (atbOrig['techdetail'] == 'Class2')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsWI) & (atbOrig['crpyears'] == crpYearsWI) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
wind_CAPEX = wind_CAPEX.reset_index()
wind_CAPEX = wind_CAPEX.drop(['index'], axis=1)
wind_FOM = atbOrig.loc[((atbOrig['technology'] == 'LandbasedWind') & (atbOrig['techdetail'] == 'Class2')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsWI) & (atbOrig['crpyears'] == crpYearsWI) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
wind_FOM = wind_FOM.reset_index()
wind_FOM = wind_FOM.drop(['index'], axis=1)
wind_VOM = atbOrig.loc[((atbOrig['technology'] == 'LandbasedWind') & (atbOrig['techdetail'] == 'Class2')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsWI) & (atbOrig['crpyears'] == crpYearsWI) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
wind_VOM = wind_VOM.reset_index()
wind_VOM = wind_VOM.drop(['index'], axis=1)

# Coal:
coal_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'Coal_FE') & (atbOrig['techdetail'] == 'newAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsFO) & (atbOrig['crpyears'] == crpYearsFO) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
coal_CAPEX = coal_CAPEX.reset_index()
coal_CAPEX = coal_CAPEX.drop(['index'], axis=1)
coal_FOM = atbOrig.loc[((atbOrig['technology'] == 'Coal_FE') & (atbOrig['techdetail'] == 'newAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsFO) & (atbOrig['crpyears'] == crpYearsFO) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
coal_FOM = coal_FOM.reset_index()
coal_FOM = coal_FOM.drop(['index'], axis=1)
coal_VOM = atbOrig.loc[((atbOrig['technology'] == 'Coal_FE') & (atbOrig['techdetail'] == 'newAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsFO) & (atbOrig['crpyears'] == crpYearsFO) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
coal_VOM = coal_VOM.reset_index()
coal_VOM = coal_VOM.drop(['index'], axis=1)

# Coal CCS:
coalCCS_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'Coal_FE') & (atbOrig['techdetail'] == 'CCS90AvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsFO) & (atbOrig['crpyears'] == crpYearsFO) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
coalCCS_CAPEX = coalCCS_CAPEX.reset_index()
coalCCS_CAPEX = coalCCS_CAPEX.drop(['index'], axis=1)
coalCCS_FOM = atbOrig.loc[((atbOrig['technology'] == 'Coal_FE') & (atbOrig['techdetail'] == 'CCS90AvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsFO) & (atbOrig['crpyears'] == crpYearsFO) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
coalCCS_FOM = coalCCS_FOM.reset_index()
coalCCS_FOM = coalCCS_FOM.drop(['index'], axis=1)
coalCCS_VOM = atbOrig.loc[((atbOrig['technology'] == 'Coal_FE') & (atbOrig['techdetail'] == 'CCS90AvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsFO) & (atbOrig['crpyears'] == crpYearsFO) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
coalCCS_VOM = coalCCS_VOM.reset_index()
coalCCS_VOM = coalCCS_VOM.drop(['index'], axis=1)

# NGCC:
NGCC_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CCAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
NGCC_CAPEX = NGCC_CAPEX.reset_index()
NGCC_CAPEX = NGCC_CAPEX.drop(['index'], axis=1)
NGCC_FOM = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CCAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
NGCC_FOM = NGCC_FOM.reset_index()
NGCC_FOM = NGCC_FOM.drop(['index'], axis=1)
NGCC_VOM = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CCAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
NGCC_VOM = NGCC_VOM.reset_index()
NGCC_VOM = NGCC_VOM.drop(['index'], axis=1)

# NGCC CCS:
NGCCCCS_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CCCCSAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
NGCCCCS_CAPEX = NGCCCCS_CAPEX.reset_index()
NGCCCCS_CAPEX = NGCCCCS_CAPEX.drop(['index'], axis=1)
NGCCCCS_FOM = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CCCCSAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
NGCCCCS_FOM = NGCCCCS_FOM.reset_index()
NGCCCCS_FOM = NGCCCCS_FOM.drop(['index'], axis=1)
NGCCCCS_VOM = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CCCCSAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
NGCCCCS_VOM = NGCCCCS_VOM.reset_index()
NGCCCCS_VOM = NGCCCCS_VOM.drop(['index'], axis=1)

# CT:
CT_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CTAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
CT_CAPEX = CT_CAPEX.reset_index()
CT_CAPEX = CT_CAPEX.drop(['index'], axis=1)
CT_FOM = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CTAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
CT_FOM = CT_FOM.reset_index()
CT_FOM = CT_FOM.drop(['index'], axis=1)
CT_VOM = atbOrig.loc[((atbOrig['technology'] == 'NaturalGas_FE') & (atbOrig['techdetail'] == 'CTAvgCF')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsCC) & (atbOrig['crpyears'] == crpYearsCC) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
CT_VOM = CT_VOM.reset_index()
CT_VOM = CT_VOM.drop(['index'], axis=1)

# Nuclear:
nuclear_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'Nuclear') & (atbOrig['techdetail'] == 'Nuclear')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsNU) & (atbOrig['crpyears'] == crpYearsNU) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
nuclear_CAPEX = nuclear_CAPEX.reset_index()
nuclear_CAPEX = nuclear_CAPEX.drop(['index'], axis=1)
nuclear_FOM = atbOrig.loc[((atbOrig['technology'] == 'Nuclear') & (atbOrig['techdetail'] == 'Nuclear')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsNU) & (atbOrig['crpyears'] == crpYearsNU) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
nuclear_FOM = nuclear_FOM.reset_index()
nuclear_FOM = nuclear_FOM.drop(['index'], axis=1)
nuclear_VOM = atbOrig.loc[((atbOrig['technology'] == 'Nuclear') & (atbOrig['techdetail'] == 'Nuclear')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsNU) & (atbOrig['crpyears'] == crpYearsNU) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
nuclear_VOM = nuclear_VOM.reset_index()
nuclear_VOM = nuclear_VOM.drop(['index'], axis=1)

# Battery:
battery_CAPEX = atbOrig.loc[((atbOrig['technology'] == 'Utility-Scale Battery Storage') & (atbOrig['techdetail'] == '4Hr Battery Storage')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsES) & (atbOrig['crpyears'] == crpYearsES) &
                (atbOrig['core_metric_parameter'] == 'CAPEX') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
battery_CAPEX = battery_CAPEX.reset_index()
battery_CAPEX = battery_CAPEX.drop(['index'], axis=1)
battery_FOM = atbOrig.loc[((atbOrig['technology'] == 'Utility-Scale Battery Storage') & (atbOrig['techdetail'] == '4Hr Battery Storage')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsES) & (atbOrig['crpyears'] == crpYearsES) &
                (atbOrig['core_metric_parameter'] == 'Fixed O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars*1000
battery_FOM = battery_FOM.reset_index()
battery_FOM = battery_FOM.drop(['index'], axis=1)
battery_VOM = atbOrig.loc[((atbOrig['technology'] == 'Utility-Scale Battery Storage') & (atbOrig['techdetail'] == '4Hr Battery Storage')) &
                ((atbOrig['scenario'] == atbScenario) & (atbOrig['core_metric_case'] == coreMetricCase)) &
                (atbOrig['crpyears'] == crpYearsES) & (atbOrig['crpyears'] == crpYearsES) &
                (atbOrig['core_metric_parameter'] == 'Variable O&M') & (atbOrig['core_metric_variable'] > 2019)]['value']*convert2019to2012Dollars
battery_VOM = battery_VOM.reset_index()
battery_VOM = battery_VOM.drop(['index'], axis=1)

# Heat rate:
if atbScenario == 'Moderate':
    coal_HR = atbOrigXls_Coal.iloc[100,12:43]*1000
    coalCCS_HR = atbOrigXls_Coal.iloc[116, 12:43]*1000
    NGCC_HR = atbOrigXls_Gas.iloc[95, 12:43]*1000
    CT_HR = atbOrigXls_Gas.iloc[89, 12:43]*1000
    NGCCCCS_HR = atbOrigXls_Gas.iloc[101, 12:43]*1000
elif atbScenario == 'Conservative':
    coal_HR = atbOrigXls_Coal.iloc[101, 12:43]*1000
    coalCCS_HR = atbOrigXls_Coal.iloc[117, 12:43]*1000
    NGCC_HR = atbOrigXls_Gas.iloc[96, 12:43]*1000
    CT_HR = atbOrigXls_Gas.iloc[90, 12:43]*1000
    NGCCCCS_HR = atbOrigXls_Gas.iloc[102, 12:43]*1000
elif atbScenario == 'Advanced':
    coal_HR = atbOrigXls_Coal.iloc[99, 12:43]*1000
    coalCCS_HR = atbOrigXls_Coal.iloc[115, 12:43]*1000
    NGCC_HR = atbOrigXls_Gas.iloc[94, 12:43]*1000
    CT_HR = atbOrigXls_Gas.iloc[88, 12:43]*1000
    NGCCCCS_HR = atbOrigXls_Gas.iloc[100, 12:43]*1000

nuclear_HR = atbOrigXls_Nuclear.iloc[109, 12:43]*1000
battery_HR = atbOrigXls_Bat.iloc[91, 6:37]

coal_HR = coal_HR.reset_index()
coal_HR = coal_HR.drop(['index'], axis=1)
coal_HR = coal_HR.astype(float)

coalCCS_HR = coalCCS_HR.reset_index()
coalCCS_HR = coalCCS_HR.drop(['index'], axis=1)
coalCCS_HR = coalCCS_HR.astype(float)

NGCC_HR = NGCC_HR.reset_index()
NGCC_HR = NGCC_HR.drop(['index'], axis=1)
NGCC_HR = NGCC_HR.astype(float)

NGCCCCS_HR = NGCCCCS_HR.reset_index()
NGCCCCS_HR = NGCCCCS_HR.drop(['index'], axis=1)
NGCCCCS_HR = NGCCCCS_HR.astype(float)

CT_HR = CT_HR.reset_index()
CT_HR = CT_HR.drop(['index'], axis=1)
CT_HR = CT_HR.astype(float)

nuclear_HR = nuclear_HR.reset_index()
nuclear_HR = nuclear_HR.drop(['index'], axis=1)
nuclear_HR = nuclear_HR.astype(float)

battery_HR = battery_HR.reset_index()
battery_HR = battery_HR.drop(['index'], axis=1)
battery_HR = battery_HR.astype(float)


for item in T:
    result_sheet_atb.write(1, item + 2, solar_CAPEX.iloc[item])
    result_sheet_atb.write(2, item + 2, solar_FOM.iloc[item])
    result_sheet_atb.write(3, item + 2, solar_VOM.iloc[item])
    result_sheet_atb.write(4, item + 2, wind_CAPEX.iloc[item])
    result_sheet_atb.write(5, item + 2, wind_FOM.iloc[item])
    result_sheet_atb.write(6, item + 2, wind_VOM.iloc[item])
    result_sheet_atb.write(8, item + 2, coal_CAPEX.iloc[item])
    result_sheet_atb.write(9, item + 2, coal_FOM.iloc[item])
    result_sheet_atb.write(10, item + 2, coal_VOM.iloc[item])
    result_sheet_atb.write(12, item + 2, coalCCS_CAPEX.iloc[item])
    result_sheet_atb.write(13, item + 2, coalCCS_FOM.iloc[item])
    result_sheet_atb.write(14, item + 2, coalCCS_VOM.iloc[item])
    result_sheet_atb.write(16, item + 2, NGCC_CAPEX.iloc[item])
    result_sheet_atb.write(17, item + 2, NGCC_FOM.iloc[item])
    result_sheet_atb.write(18, item + 2, NGCC_VOM.iloc[item])
    result_sheet_atb.write(20, item + 2, NGCCCCS_CAPEX.iloc[item])
    result_sheet_atb.write(21, item + 2, NGCCCCS_FOM.iloc[item])
    result_sheet_atb.write(22, item + 2, NGCCCCS_VOM.iloc[item])
    result_sheet_atb.write(24, item + 2, CT_CAPEX.iloc[item])
    result_sheet_atb.write(25, item + 2, CT_FOM.iloc[item])
    result_sheet_atb.write(26, item + 2, CT_VOM.iloc[item])
    result_sheet_atb.write(28, item + 2, nuclear_CAPEX.iloc[item])
    result_sheet_atb.write(29, item + 2, nuclear_FOM.iloc[item])
    result_sheet_atb.write(30, item + 2, nuclear_VOM.iloc[item])
    result_sheet_atb.write(31, item + 2, battery_CAPEX.iloc[item])
    result_sheet_atb.write(32, item + 2, battery_FOM.iloc[item])
    result_sheet_atb.write(33, item + 2, battery_VOM.iloc[item])

    result_sheet_atb.write(7, item + 2, coal_HR.iloc[item])
    result_sheet_atb.write(11, item + 2, coalCCS_HR.iloc[item])
    result_sheet_atb.write(15, item + 2, NGCC_HR.iloc[item])
    result_sheet_atb.write(19, item + 2, NGCCCCS_HR.iloc[item])
    result_sheet_atb.write(23, item + 2, CT_HR.iloc[item])
    result_sheet_atb.write(27, item + 2, nuclear_HR.iloc[item])
    result_sheet_atb.write(34, item + 2, battery_HR.iloc[item])




results_book.close()