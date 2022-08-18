
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter as xw

case_to_run = 1
zeroSys = True
planningDACs = 3
elect_demand = 1

m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\Python\\"

resultCase = 'ResultsC1'
if zeroSys: sysCase = 'zeroSys'
elif not zeroSys: sysCase = 'negSys'

if planningDACs == 1: planningCase = 'noDAC'
elif planningDACs == 2: planningCase = 'lateDAC'
elif planningDACs == 3: planningCase = "earlyDAC"

if case_to_run == 1: case_name = "reference"
elif case_to_run == 2: case_name = "lNuclear"
elif case_to_run == 3: case_name = "lNuclearCCS"
elif case_to_run == 4: case_name = "lH2"

if elect_demand == 1: high_elect = "highElectrification"
elif elect_demand == 0: high_elect = ""

resultsDir = resultCase + '_' + sysCase + '_' + planningCase + '_' + case_name + '_' + high_elect
pythonFolder = 'C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\Python\\'
resultsFolder = pythonFolder + resultsDir + '\\CE\\'

# Set up the excel file
results_book = xw.Workbook(pythonFolder + 'Results\\' + sysCase + '_' + planningCase + '_' + case_name + '_' + high_elect + '.xlsx')
result_sheet_cost = results_book.add_worksheet('Costs')
result_sheet_CE = results_book.add_worksheet('CE')
result_sheet_Generation = results_book.add_worksheet('Generation')
result_sheet_Generation_new = results_book.add_worksheet('New Generation')

# read in new capacity investment solution:
genFleetAfter2050 = pd.read_csv(resultsFolder + 'genFleetAfterCE2050.csv')
genFleetAfter2050 = genFleetAfter2050[genFleetAfter2050.YearAddedCE >= 2030]




if planningDACs != 3:
    # Costs:
    vZannual_2030 = pd.read_csv(resultsFolder + 'vZannualCE2030.csv', header=None)
    vZannual_2040 = pd.read_csv(resultsFolder + 'vZannualCE2040.csv', header=None)
    vVarcostannual_2030 = pd.read_csv(resultsFolder + 'vVarcostannualCE2030.csv', header=None)
    vVarcostannual_2040 = pd.read_csv(resultsFolder + 'vVarcostannualCE2040.csv', header=None)

    vZannual_2030 = vZannual_2030.iloc[0,0]/1000
    vZannual_2040 = vZannual_2040.iloc[0,0]/1000

    vVarcostannual_2030 = vVarcostannual_2030.iloc[0, 0] / 1000
    vVarcostannual_2040 = vVarcostannual_2040.iloc[0, 0] / 1000

    vFixedcostannual_2030 = vZannual_2030 - vVarcostannual_2030
    vFixedcostannual_2040 = vZannual_2040 - vVarcostannual_2040

    result_sheet_cost.write("A1", "total Operating cost 2030 (million $)")
    result_sheet_cost.write("B1", vVarcostannual_2030)
    result_sheet_cost.write("A2", "total Operating cost 2040 (million $)")
    result_sheet_cost.write("B2", vVarcostannual_2040)

    result_sheet_cost.write("A6", "total Fixed cost 2030 (million $)")
    result_sheet_cost.write("B6", vFixedcostannual_2030)
    result_sheet_cost.write("A7", "total Fixed cost 2040 (million $)")
    result_sheet_cost.write("B7", vFixedcostannual_2040)

    result_sheet_cost.write("A12", "total cost 2030 (million $)")
    result_sheet_cost.write("B12", vZannual_2030)
    result_sheet_cost.write("A13", "total cost 2040 (million $)")
    result_sheet_cost.write("B13", vZannual_2040)

    # CE:
    genFleetAfter2030 = genFleetAfter2050[genFleetAfter2050.YearAddedCE == 2030]
    genFleetAfter2040 = genFleetAfter2050[genFleetAfter2050.YearAddedCE == 2040]

    genFleetAfter2030 = genFleetAfter2030[['PlantType', 'Capacity (MW)']]
    genFleetAfter2040 = genFleetAfter2040[['PlantType', 'Capacity (MW)']]

    CoalCCS_2030 = genFleetAfter2030[genFleetAfter2030['PlantType'].str.contains('Coal Steam CCS')]
    CC_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'] == 'Combined Cycle']
    CCCCS_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'] == 'Combined Cycle CCS']
    Nuclear_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'] == 'Nuclear']
    Hydrogen_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'] == 'Hydrogen']
    Battery_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'] == 'Battery Storage']
    DAC_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'] == 'DAC']
    Wind_2030 = genFleetAfter2030[genFleetAfter2030['PlantType'].str.contains('wind')]
    Solar_2030 = genFleetAfter2030[genFleetAfter2030['PlantType'].str.contains('solar')]

    CoalCCS_2030 = CoalCCS_2030['Capacity (MW)'].sum()
    CC_2030 = CC_2030['Capacity (MW)'].sum()
    CCCCS_2030 = CCCCS_2030['Capacity (MW)'].sum()
    Nuclear_2030 = Nuclear_2030['Capacity (MW)'].sum()
    Hydrogen_2030 = Hydrogen_2030['Capacity (MW)'].sum()
    Battery_2030 = Battery_2030['Capacity (MW)'].sum()
    DAC_2030 = DAC_2030['Capacity (MW)'].sum()
    Wind_2030 = Wind_2030['Capacity (MW)'].sum()
    Solar_2030 = Solar_2030['Capacity (MW)'].sum()

    CoalCCS_2040 = genFleetAfter2040[genFleetAfter2040['PlantType'].str.contains('Coal Steam CCS')]
    CC_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'] == 'Combined Cycle']
    CCCCS_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'] == 'Combined Cycle CCS']
    Nuclear_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'] == 'Nuclear']
    Hydrogen_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'] == 'Hydrogen']
    Battery_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'] == 'Battery Storage']
    DAC_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'] == 'DAC']
    Wind_2040 = genFleetAfter2040[genFleetAfter2040['PlantType'].str.contains('wind')]
    Solar_2040 = genFleetAfter2040[genFleetAfter2040['PlantType'].str.contains('solar')]

    CoalCCS_2040 = CoalCCS_2040['Capacity (MW)'].sum()
    CC_2040 = CC_2040['Capacity (MW)'].sum()
    CCCCS_2040 = CCCCS_2040['Capacity (MW)'].sum()
    Nuclear_2040 = Nuclear_2040['Capacity (MW)'].sum()
    Hydrogen_2040 = Hydrogen_2040['Capacity (MW)'].sum()
    Battery_2040 = Battery_2040['Capacity (MW)'].sum()
    DAC_2040 = DAC_2040['Capacity (MW)'].sum()
    Wind_2040 = Wind_2040['Capacity (MW)'].sum()
    Solar_2040 = Solar_2040['Capacity (MW)'].sum()

    # Existing Generation:
    # 2030:
    vGen_2030 = pd.read_csv(resultsFolder + 'vGenCE2030.csv')
    genforCE2030_existing = pd.read_csv(resultsFolder + 'genFleetForCE2030.csv')
    genforCE2030_existing = genforCE2030_existing[['PlantType']]

    vGen_2030['Total Gen'] = vGen_2030.iloc[:, 1:].sum(axis=1)
    vGen_2030_temp = vGen_2030[['Total Gen']]
    vGen_2030_temp['PlantType'] = genforCE2030_existing
    vGen_2030 = vGen_2030_temp
    gen_CoalSteam_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Coal Steam']
    gen_CC_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Combined Cycle']
    gen_CCCCS_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Combined Cycle CCS']
    gen_CT_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Combustion Turbine']
    gen_OG_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'O/G Steam']
    gen_Bio_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Biomass']
    gen_Bat_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Energy Storage']
    gen_H2_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Hydrogen']
    gen_Nuclear_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'Nuclear']
    gen_DAC_2030 = vGen_2030.loc[vGen_2030['PlantType'] == 'DAC']
    gen_Solar_2030 = vGen_2030[vGen_2030['PlantType'].str.contains('solar')]
    gen_Wind_2030 = vGen_2030[vGen_2030['PlantType'].str.contains('wind')]

    gen_CoalSteam_2030 = gen_CoalSteam_2030['Total Gen'].sum()
    gen_CC_2030 = gen_CC_2030['Total Gen'].sum()
    gen_CCCCS_2030 = gen_CCCCS_2030['Total Gen'].sum()
    gen_Bat_2030 = gen_Bat_2030['Total Gen'].sum()
    gen_H2_2030 = gen_H2_2030['Total Gen'].sum()
    gen_Nuclear_2030 = gen_Nuclear_2030['Total Gen'].sum()
    gen_Solar_2030 = gen_Solar_2030['Total Gen'].sum()
    gen_Wind_2030 = gen_Wind_2030['Total Gen'].sum()
    gen_DAC_2030 = gen_DAC_2030['Total Gen'].sum()
    gen_CT_2030 = gen_CT_2030['Total Gen'].sum()
    gen_OG_2030 = gen_OG_2030['Total Gen'].sum()
    gen_Bio_2030 = gen_Bio_2030['Total Gen'].sum()

    # 2040:
    vGen_2040 = pd.read_csv(resultsFolder + 'vGenCE2040.csv')
    genforCE2040_existing = pd.read_csv(resultsFolder + 'genFleetForCE2040.csv')
    genforCE2040_existing = genforCE2040_existing[['PlantType']]

    vGen_2040['Total Gen'] = vGen_2040.iloc[:, 1:].sum(axis=1)
    vGen_2040_temp = vGen_2040[['Total Gen']]
    vGen_2040_temp['PlantType'] = genforCE2040_existing
    vGen_2040 = vGen_2040_temp
    gen_CoalSteam_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Coal Steam']
    gen_CC_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Combined Cycle']
    gen_CCCCS_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Combined Cycle CCS']
    gen_CT_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Combustion Turbine']
    gen_OG_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'O/G Steam']
    gen_Bio_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Biomass']
    gen_Bat_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Energy Storage']
    gen_H2_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Hydrogen']
    gen_Nuclear_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'Nuclear']
    gen_DAC_2040 = vGen_2040.loc[vGen_2040['PlantType'] == 'DAC']
    gen_Solar_2040 = vGen_2040[vGen_2040['PlantType'].str.contains('solar')]
    gen_Wind_2040 = vGen_2040[vGen_2040['PlantType'].str.contains('wind')]

    gen_CoalSteam_2040 = gen_CoalSteam_2040['Total Gen'].sum()
    gen_CC_2040 = gen_CC_2040['Total Gen'].sum()
    gen_CCCCS_2040 = gen_CCCCS_2040['Total Gen'].sum()
    gen_Bat_2040 = gen_Bat_2040['Total Gen'].sum()
    gen_H2_2040 = gen_H2_2040['Total Gen'].sum()
    gen_Nuclear_2040 = gen_Nuclear_2040['Total Gen'].sum()
    gen_Solar_2040 = gen_Solar_2040['Total Gen'].sum()
    gen_Wind_2040 = gen_Wind_2040['Total Gen'].sum()
    gen_DAC_2040 = gen_DAC_2040['Total Gen'].sum()
    gen_CT_2040 = gen_CT_2040['Total Gen'].sum()
    gen_OG_2040 = gen_OG_2040['Total Gen'].sum()
    gen_Bio_2040 = gen_Bio_2040['Total Gen'].sum()

    # New generation:
    # 2030:
    vGen_new_2030 = pd.read_csv(resultsFolder + 'vGentechCE2030.csv')
    vGen_new_2030['Total Gen'] = vGen_new_2030.iloc[:, 1:].sum(axis=1)
    vGen_new_2030_temp = vGen_new_2030[['Total Gen', 'GAMS Symbol']]
    vGen_new_2030 = vGen_new_2030_temp
    gen_CoalSteam_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'Coal Steam CCS']
    gen_CC_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'Combined Cycle']
    gen_CCCCS_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'Combined Cycle CCS']
    gen_Bat_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'Battery Storage']
    gen_H2_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'Hydrogen']
    gen_Nuclear_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'Nuclear']
    gen_DAC_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'] == 'DAC']
    gen_Solar_new_2030 = vGen_new_2030[vGen_new_2030['GAMS Symbol'].str.contains('solar')]
    gen_Wind_new_2030 = vGen_new_2030[vGen_new_2030['GAMS Symbol'].str.contains('wind')]

    gen_CoalSteam_new_2030 = gen_CoalSteam_new_2030['Total Gen'].sum()
    gen_CC_new_2030 = gen_CC_new_2030['Total Gen'].sum()
    gen_CCCCS_new_2030 = gen_CCCCS_new_2030['Total Gen'].sum()
    gen_Bat_new_2030 = gen_Bat_new_2030['Total Gen'].sum()
    gen_H2_new_2030 = gen_H2_new_2030['Total Gen'].sum()
    gen_Nuclear_new_2030 = gen_Nuclear_new_2030['Total Gen'].sum()
    gen_Solar_new_2030 = gen_Solar_new_2030['Total Gen'].sum()
    gen_Wind_new_2030 = gen_Wind_new_2030['Total Gen'].sum()
    gen_DAC_new_2030 = gen_DAC_new_2030['Total Gen'].sum()

    # 2040:
    vGen_new_2040 = pd.read_csv(resultsFolder + 'vGentechCE2040.csv')
    vGen_new_2040['Total Gen'] = vGen_new_2040.iloc[:, 1:].sum(axis=1)
    vGen_new_2040_temp = vGen_new_2040[['Total Gen', 'GAMS Symbol']]
    vGen_new_2040 = vGen_new_2040_temp
    gen_CoalSteam_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'Coal Steam CCS']
    gen_CC_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'Combined Cycle']
    gen_CCCCS_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'Combined Cycle CCS']
    gen_Bat_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'Battery Storage']
    gen_H2_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'Hydrogen']
    gen_Nuclear_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'Nuclear']
    gen_DAC_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'] == 'DAC']
    gen_Solar_new_2040 = vGen_new_2040[vGen_new_2040['GAMS Symbol'].str.contains('solar')]
    gen_Wind_new_2040 = vGen_new_2040[vGen_new_2040['GAMS Symbol'].str.contains('wind')]

    gen_CoalSteam_new_2040 = gen_CoalSteam_new_2040['Total Gen'].sum()
    gen_CC_new_2040 = gen_CC_new_2040['Total Gen'].sum()
    gen_CCCCS_new_2040 = gen_CCCCS_new_2040['Total Gen'].sum()
    gen_Bat_new_2040 = gen_Bat_new_2040['Total Gen'].sum()
    gen_H2_new_2040 = gen_H2_new_2040['Total Gen'].sum()
    gen_Nuclear_new_2040 = gen_Nuclear_new_2040['Total Gen'].sum()
    gen_Solar_new_2040 = gen_Solar_new_2040['Total Gen'].sum()
    gen_Wind_new_2040 = gen_Wind_new_2040['Total Gen'].sum()
    gen_DAC_new_2040 = gen_DAC_new_2040['Total Gen'].sum()

else:
    vZannual_2030 = 0
    vZannual_2040 = 0
    vVarcostannual_2030 = 0
    vVarcostannual_2040 = 0
    vFixedcostannual_2030 = 0
    vFixedcostannual_2040 = 0

    CoalCCS_2030 = 0
    CC_2030 = 0
    CCCCS_2030 = 0
    Nuclear_2030 = 0
    Hydrogen_2030 = 0
    Battery_2030 = 0
    DAC_2030 = 0
    Wind_2030 = 0
    Solar_2030 = 0

    CoalCCS_2040 = 0
    CC_2040 = 0
    CCCCS_2040 = 0
    Nuclear_2040 = 0
    Hydrogen_2040 = 0
    Battery_2040 = 0
    DAC_2040 = 0
    Wind_2040 = 0
    Solar_2040 = 0

    gen_CoalSteam_2030 = 0
    gen_CC_2030 = 0
    gen_CCCCS_2030 = 0
    gen_Bat_2030 = 0
    gen_H2_2030 = 0
    gen_Nuclear_2030 = 0
    gen_Solar_2030 = 0
    gen_Wind_2030 = 0
    gen_DAC_2030 = 0
    gen_CT_2030 = 0
    gen_OG_2030 = 0
    gen_Bio_2030 = 0

    gen_CoalSteam_2040 = 0
    gen_CC_2040 = 0
    gen_CCCCS_2040 = 0
    gen_Bat_2040 = 0
    gen_H2_2040 = 0
    gen_Nuclear_2040 = 0
    gen_Solar_2040 = 0
    gen_Wind_2040 = 0
    gen_DAC_2040 = 0
    gen_CT_2040 = 0
    gen_OG_2040 = 0
    gen_Bio_2040 = 0

    gen_CoalSteam_new_2030 = 0
    gen_CC_new_2030 = 0
    gen_CCCCS_new_2030 = 0
    gen_Bat_new_2030 = 0
    gen_H2_new_2030 = 0
    gen_Nuclear_new_2030 = 0
    gen_Solar_new_2030 = 0
    gen_Wind_new_2030 = 0
    gen_DAC_new_2030 = 0

    gen_CoalSteam_new_2040 = 0
    gen_CC_new_2040 = 0
    gen_CCCCS_new_2040 = 0
    gen_Bat_new_2040 = 0
    gen_H2_new_2040 = 0
    gen_Nuclear_new_2040 = 0
    gen_Solar_new_2040 = 0
    gen_Wind_new_2040 = 0
    gen_DAC_new_2040 = 0


# Costs:
vZannual_2050 = pd.read_csv(resultsFolder + 'vZannualCE2050.csv', header=None)
vVarcostannual_2050 = pd.read_csv(resultsFolder + 'vVarcostannualCE2050.csv', header=None)

vZannual_2050 = vZannual_2050.iloc[0,0]/1000
vVarcostannual_2050 = vVarcostannual_2050.iloc[0, 0] / 1000
vFixedcostannual_2050 = vZannual_2050 - vVarcostannual_2050

result_sheet_cost.write("A3", "total Operating cost 2050 (million $)")
result_sheet_cost.write("B3", vVarcostannual_2050)
result_sheet_cost.write("A8", "total Fixed cost 2050 (million $)")
result_sheet_cost.write("B8", vFixedcostannual_2050)

result_sheet_cost.write("A4", "total Operating cost (million $)")
result_sheet_cost.write("B4", vVarcostannual_2030 + vVarcostannual_2040 + vVarcostannual_2050)

result_sheet_cost.write("A9", "total Fixed cost (million $)")
result_sheet_cost.write("B9", vFixedcostannual_2030 + vFixedcostannual_2040 + vFixedcostannual_2050)

result_sheet_cost.write("A14", "total cost 2050 (million $)")
result_sheet_cost.write("B14", vZannual_2050)

result_sheet_cost.write("A16", "total cost (million $)")
result_sheet_cost.write("B16", vZannual_2030 + vZannual_2040 + vZannual_2050)

# CE:
genFleetAfter2050 = genFleetAfter2050[genFleetAfter2050.YearAddedCE == 2050]
genFleetAfter2050 = genFleetAfter2050[['PlantType', 'Capacity (MW)']]

CoalCCS_2050 = genFleetAfter2050[genFleetAfter2050['PlantType'].str.contains('Coal Steam CCS')]
CC_2050 = genFleetAfter2050.loc[genFleetAfter2050['PlantType'] == 'Combined Cycle']
CCCCS_2050 = genFleetAfter2050.loc[genFleetAfter2050['PlantType'] == 'Combined Cycle CCS']
Nuclear_2050 = genFleetAfter2050.loc[genFleetAfter2050['PlantType'] == 'Nuclear']
Hydrogen_2050 = genFleetAfter2050.loc[genFleetAfter2050['PlantType'] == 'Hydrogen']
Battery_2050 = genFleetAfter2050.loc[genFleetAfter2050['PlantType'] == 'Battery Storage']
DAC_2050 = genFleetAfter2050.loc[genFleetAfter2050['PlantType'] == 'DAC']
Wind_2050 = genFleetAfter2050[genFleetAfter2050['PlantType'].str.contains('wind')]
Solar_2050 = genFleetAfter2050[genFleetAfter2050['PlantType'].str.contains('solar')]

CoalCCS_2050 = CoalCCS_2050['Capacity (MW)'].sum()
CC_2050 = CC_2050['Capacity (MW)'].sum()
CCCCS_2050 = CCCCS_2050['Capacity (MW)'].sum()
Nuclear_2050 = Nuclear_2050['Capacity (MW)'].sum()
Hydrogen_2050 = Hydrogen_2050['Capacity (MW)'].sum()
Battery_2050 = Battery_2050['Capacity (MW)'].sum()
DAC_2050 = DAC_2050['Capacity (MW)'].sum()
Wind_2050 = Wind_2050['Capacity (MW)'].sum()
Solar_2050 = Solar_2050['Capacity (MW)'].sum()

# Generation:
# read in existing plant type solution:
vGen_2050 = pd.read_csv(resultsFolder + 'vGenCE2050.csv')

# read in plant type for existing generation:
genforCE2050_existing = pd.read_csv(resultsFolder + 'genFleetForCE2050.csv')
genforCE2050_existing = genforCE2050_existing[['PlantType']]

# Generation:
# 2050:
vGen_2050['Total Gen'] = vGen_2050.iloc[:, 1:].sum(axis=1)
vGen_2050_temp = vGen_2050[['Total Gen']]
vGen_2050_temp['PlantType'] = genforCE2050_existing
vGen_2050 = vGen_2050_temp
gen_CoalSteam_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Coal Steam']
gen_CC_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Combined Cycle']
gen_CCCCS_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Combined Cycle CCS']
gen_CT_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Combustion Turbine']
gen_OG_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'O/G Steam']
gen_Bio_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Biomass']
gen_Bat_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Energy Storage']
gen_H2_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Hydrogen']
gen_Nuclear_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'Nuclear']
gen_DAC_2050 = vGen_2050.loc[vGen_2050['PlantType'] == 'DAC']
gen_Solar_2050 = vGen_2050[vGen_2050['PlantType'].str.contains('solar')]
gen_Wind_2050 = vGen_2050[vGen_2050['PlantType'].str.contains('wind')]

gen_CoalSteam_2050 = gen_CoalSteam_2050['Total Gen'].sum()
gen_CC_2050 = gen_CC_2050['Total Gen'].sum()
gen_CCCCS_2050 = gen_CCCCS_2050['Total Gen'].sum()
gen_Bat_2050 = gen_Bat_2050['Total Gen'].sum()
gen_H2_2050 = gen_H2_2050['Total Gen'].sum()
gen_Nuclear_2050 = gen_Nuclear_2050['Total Gen'].sum()
gen_Solar_2050 = gen_Solar_2050['Total Gen'].sum()
gen_Wind_2050 = gen_Wind_2050['Total Gen'].sum()
gen_DAC_2050 = gen_DAC_2050['Total Gen'].sum()
gen_CT_2050 = gen_CT_2050['Total Gen'].sum()
gen_OG_2050 = gen_OG_2050['Total Gen'].sum()
gen_Bio_2050 = gen_Bio_2050['Total Gen'].sum()

# New generation:
# read in new plant type generation:
vGen_new_2050 = pd.read_csv(resultsFolder + 'vGentechCE2050.csv')

# 2050:
vGen_new_2050['Total Gen'] = vGen_new_2050.iloc[:, 1:].sum(axis=1)
vGen_new_2050_temp = vGen_new_2050[['Total Gen', 'GAMS Symbol']]
vGen_new_2050 = vGen_new_2050_temp
gen_CoalSteam_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'Coal Steam CCS']
gen_CC_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'Combined Cycle']
gen_CCCCS_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'Combined Cycle CCS']
gen_Bat_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'Battery Storage']
gen_H2_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'Hydrogen']
gen_Nuclear_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'Nuclear']
gen_DAC_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'] == 'DAC']
gen_Solar_new_2050 = vGen_new_2050[vGen_new_2050['GAMS Symbol'].str.contains('solar')]
gen_Wind_new_2050 = vGen_new_2050[vGen_new_2050['GAMS Symbol'].str.contains('wind')]

gen_CoalSteam_new_2050 = gen_CoalSteam_new_2050['Total Gen'].sum()
gen_CC_new_2050 = gen_CC_new_2050['Total Gen'].sum()
gen_CCCCS_new_2050 = gen_CCCCS_new_2050['Total Gen'].sum()
gen_Bat_new_2050 = gen_Bat_new_2050['Total Gen'].sum()
gen_H2_new_2050 = gen_H2_new_2050['Total Gen'].sum()
gen_Nuclear_new_2050 = gen_Nuclear_new_2050['Total Gen'].sum()
gen_Solar_new_2050 = gen_Solar_new_2050['Total Gen'].sum()
gen_Wind_new_2050 = gen_Wind_new_2050['Total Gen'].sum()
gen_DAC_new_2050 = gen_DAC_new_2050['Total Gen'].sum()

# Write in excel:
result_sheet_CE.write("A2", "Coal Steam CCS")
result_sheet_CE.write("A3", "Combined Cycle")
result_sheet_CE.write("A4", "Combined Cycle CCS")
result_sheet_CE.write("A5", "Nuclear")
result_sheet_CE.write("A6", "Wind")
result_sheet_CE.write("A7", "Solar PV")
result_sheet_CE.write("A8", "Battery Storage")
result_sheet_CE.write("A9", "Hydrogen")
result_sheet_CE.write("A10", "DAC")

result_sheet_CE.write("B1", "2030")
result_sheet_CE.write("C1", "2040")
result_sheet_CE.write("D1", "2050")
result_sheet_CE.write("E1", "Total")

result_sheet_CE.write("B2", CoalCCS_2030)
result_sheet_CE.write("B3", CC_2030)
result_sheet_CE.write("B4", CCCCS_2030)
result_sheet_CE.write("B5", Nuclear_2030)
result_sheet_CE.write("B6", Wind_2030)
result_sheet_CE.write("B7", Solar_2030)
result_sheet_CE.write("B8", Battery_2030)
result_sheet_CE.write("B9", Hydrogen_2030)
result_sheet_CE.write("B10", DAC_2030)

result_sheet_CE.write("C2", CoalCCS_2040)
result_sheet_CE.write("C3", CC_2040)
result_sheet_CE.write("C4", CCCCS_2040)
result_sheet_CE.write("C5", Nuclear_2040)
result_sheet_CE.write("C6", Wind_2040)
result_sheet_CE.write("C7", Solar_2040)
result_sheet_CE.write("C8", Battery_2040)
result_sheet_CE.write("C9", Hydrogen_2040)
result_sheet_CE.write("C10", DAC_2030)

result_sheet_CE.write("D2", CoalCCS_2050)
result_sheet_CE.write("D3", CC_2050)
result_sheet_CE.write("D4", CCCCS_2050)
result_sheet_CE.write("D5", Nuclear_2050)
result_sheet_CE.write("D6", Wind_2050)
result_sheet_CE.write("D7", Solar_2050)
result_sheet_CE.write("D8", Battery_2050)
result_sheet_CE.write("D9", Hydrogen_2050)
result_sheet_CE.write("D10", DAC_2050)

result_sheet_CE.write("E2", CoalCCS_2030 + CoalCCS_2040 + CoalCCS_2050)
result_sheet_CE.write("E3", CC_2030 + CC_2040 + CC_2050)
result_sheet_CE.write("E4", CCCCS_2030 + CCCCS_2040 + CCCCS_2050)
result_sheet_CE.write("E5", Nuclear_2030 + Nuclear_2040 + Nuclear_2050)
result_sheet_CE.write("E6", Wind_2030 + Wind_2040 + Wind_2050)
result_sheet_CE.write("E7", Solar_2030 + Solar_2040 + Solar_2050)
result_sheet_CE.write("E8", Battery_2030 + Battery_2040 + Battery_2050)
result_sheet_CE.write("E9", Hydrogen_2030 + Hydrogen_2040 + Hydrogen_2050)
result_sheet_CE.write("E10", DAC_2030 + DAC_2040 + DAC_2050)

# Generation:
result_sheet_Generation.write("A2", "Coal Steam")
result_sheet_Generation.write("A3", "Combined Cycle")
result_sheet_Generation.write("A4", "Combined Cycle CCS")
result_sheet_Generation.write("A5", "Nuclear")
result_sheet_Generation.write("A6", "Wind")
result_sheet_Generation.write("A7", "Solar PV")
result_sheet_Generation.write("A8", "Battery Storage")
result_sheet_Generation.write("A9", "Hydrogen")
result_sheet_Generation.write("A10", "DAC")
result_sheet_Generation.write("A11", "Combustion Turbine")
result_sheet_Generation.write("A12", "O/G Steam")
result_sheet_Generation.write("A13", "Biomass")

result_sheet_Generation.write("B1", "2030")
result_sheet_Generation.write("C1", "2040")
result_sheet_Generation.write("D1", "2050")
result_sheet_Generation.write("E1", "Total")

result_sheet_Generation.write("B2", gen_CoalSteam_2030)
result_sheet_Generation.write("B3", gen_CC_2030)
result_sheet_Generation.write("B4", gen_CCCCS_2030)
result_sheet_Generation.write("B5", gen_Nuclear_2030)
result_sheet_Generation.write("B6", gen_Wind_2030)
result_sheet_Generation.write("B7", gen_Solar_2030)
result_sheet_Generation.write("B8", gen_Bat_2030)
result_sheet_Generation.write("B9", gen_H2_2030)
result_sheet_Generation.write("B10", gen_DAC_2030)
result_sheet_Generation.write("B11", gen_CT_2030)
result_sheet_Generation.write("B12", gen_OG_2030)
result_sheet_Generation.write("B13", gen_Bio_2030)

result_sheet_Generation.write("C2", gen_CoalSteam_2040)
result_sheet_Generation.write("C3", gen_CC_2040)
result_sheet_Generation.write("C4", gen_CCCCS_2040)
result_sheet_Generation.write("C5", gen_Nuclear_2040)
result_sheet_Generation.write("C6", gen_Wind_2040)
result_sheet_Generation.write("C7", gen_Solar_2040)
result_sheet_Generation.write("C8", gen_Bat_2040)
result_sheet_Generation.write("C9", gen_H2_2040)
result_sheet_Generation.write("C10", gen_DAC_2040)
result_sheet_Generation.write("C11", gen_CT_2040)
result_sheet_Generation.write("C12", gen_OG_2040)
result_sheet_Generation.write("C13", gen_Bio_2040)

result_sheet_Generation.write("D2", gen_CoalSteam_2050)
result_sheet_Generation.write("D3", gen_CC_2050)
result_sheet_Generation.write("D4", gen_CCCCS_2050)
result_sheet_Generation.write("D5", gen_Nuclear_2050)
result_sheet_Generation.write("D6", gen_Wind_2050)
result_sheet_Generation.write("D7", gen_Solar_2050)
result_sheet_Generation.write("D8", gen_Bat_2050)
result_sheet_Generation.write("D9", gen_H2_2050)
result_sheet_Generation.write("D10", gen_DAC_2050)
result_sheet_Generation.write("D11", gen_CT_2050)
result_sheet_Generation.write("D12", gen_OG_2050)
result_sheet_Generation.write("D13", gen_Bio_2050)

result_sheet_Generation.write("E2", gen_CoalSteam_2030 + gen_CoalSteam_2040 + gen_CoalSteam_2050)
result_sheet_Generation.write("E3", gen_CC_2030 + gen_CC_2040 + gen_CC_2050)
result_sheet_Generation.write("E4", gen_CCCCS_2030 + gen_CCCCS_2040 + gen_CCCCS_2050)
result_sheet_Generation.write("E5", gen_Nuclear_2030 + gen_Nuclear_2040 + gen_Nuclear_2050)
result_sheet_Generation.write("E6", gen_Wind_2030 + gen_Wind_2040 + gen_Wind_2050)
result_sheet_Generation.write("E7", gen_Solar_2030 + gen_Solar_2040 + gen_Solar_2050)
result_sheet_Generation.write("E8", gen_Bat_2030 + gen_Bat_2040 + gen_Bat_2050)
result_sheet_Generation.write("E9", gen_H2_2030 + gen_H2_2040 + gen_H2_2050)
result_sheet_Generation.write("E10", gen_DAC_2030 + gen_DAC_2040 + gen_DAC_2050)
result_sheet_Generation.write("E11", gen_CT_2030 + gen_CT_2040 + gen_CT_2050)
result_sheet_Generation.write("E12", gen_OG_2030 + gen_OG_2040 + gen_OG_2050)
result_sheet_Generation.write("E13", gen_Bio_2030 + gen_Bio_2040 + gen_Bio_2050)

# new Generation:
result_sheet_Generation_new.write("A2", "Coal Steam CCS")
result_sheet_Generation_new.write("A3", "Combined Cycle")
result_sheet_Generation_new.write("A4", "Combined Cycle CCS")
result_sheet_Generation_new.write("A5", "Nuclear")
result_sheet_Generation_new.write("A6", "Wind")
result_sheet_Generation_new.write("A7", "Solar PV")
result_sheet_Generation_new.write("A8", "Battery Storage")
result_sheet_Generation_new.write("A9", "Hydrogen")
result_sheet_Generation_new.write("A10", "DAC")

result_sheet_Generation_new.write("B1", "2030")
result_sheet_Generation_new.write("C1", "2040")
result_sheet_Generation_new.write("D1", "2050")
result_sheet_Generation_new.write("E1", "Total")

result_sheet_Generation_new.write("B2", gen_CoalSteam_new_2030)
result_sheet_Generation_new.write("B3", gen_CC_new_2030)
result_sheet_Generation_new.write("B4", gen_CCCCS_new_2030)
result_sheet_Generation_new.write("B5", gen_Nuclear_new_2030)
result_sheet_Generation_new.write("B6", gen_Wind_new_2030)
result_sheet_Generation_new.write("B7", gen_Solar_new_2030)
result_sheet_Generation_new.write("B8", gen_Bat_new_2030)
result_sheet_Generation_new.write("B9", gen_H2_new_2030)
result_sheet_Generation_new.write("B10", gen_DAC_new_2030)

result_sheet_Generation_new.write("C2", gen_CoalSteam_new_2040)
result_sheet_Generation_new.write("C3", gen_CC_new_2040)
result_sheet_Generation_new.write("C4", gen_CCCCS_new_2040)
result_sheet_Generation_new.write("C5", gen_Nuclear_new_2040)
result_sheet_Generation_new.write("C6", gen_Wind_new_2040)
result_sheet_Generation_new.write("C7", gen_Solar_new_2040)
result_sheet_Generation_new.write("C8", gen_Bat_new_2040)
result_sheet_Generation_new.write("C9", gen_H2_new_2040)
result_sheet_Generation_new.write("C10", gen_DAC_new_2040)

result_sheet_Generation_new.write("D2", gen_CoalSteam_new_2050)
result_sheet_Generation_new.write("D3", gen_CC_new_2050)
result_sheet_Generation_new.write("D4", gen_CCCCS_new_2050)
result_sheet_Generation_new.write("D5", gen_Nuclear_new_2050)
result_sheet_Generation_new.write("D6", gen_Wind_new_2050)
result_sheet_Generation_new.write("D7", gen_Solar_new_2050)
result_sheet_Generation_new.write("D8", gen_Bat_new_2050)
result_sheet_Generation_new.write("D9", gen_H2_new_2050)
result_sheet_Generation_new.write("D10", gen_DAC_new_2050)

result_sheet_Generation_new.write("E2", gen_CoalSteam_new_2030 + gen_CoalSteam_new_2040 + gen_CoalSteam_new_2050)
result_sheet_Generation_new.write("E3", gen_CC_new_2030 + gen_CC_new_2040 + gen_CC_new_2050)
result_sheet_Generation_new.write("E4", gen_CCCCS_new_2030 + gen_CCCCS_new_2040 + gen_CCCCS_new_2050)
result_sheet_Generation_new.write("E5", gen_Nuclear_new_2030 + gen_Nuclear_new_2040 + gen_Nuclear_new_2050)
result_sheet_Generation_new.write("E6", gen_Wind_new_2030 + gen_Wind_new_2040 + gen_Wind_new_2050)
result_sheet_Generation_new.write("E7", gen_Solar_new_2030 + gen_Solar_new_2040 + gen_Solar_new_2050)
result_sheet_Generation_new.write("E8", gen_Bat_new_2030 + gen_Bat_new_2040 + gen_Bat_new_2050)
result_sheet_Generation_new.write("E9", gen_H2_new_2030 + gen_H2_new_2040 + gen_H2_new_2050)
result_sheet_Generation_new.write("E10", gen_DAC_new_2030 + gen_DAC_new_2040 + gen_DAC_new_2050)

results_book.close()