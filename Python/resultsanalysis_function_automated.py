
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter as xw
import numpy as np


def results_summary(buildLimitsCase, emissionSystem, planNESystem, co2EmsCapInFinalYear,
                    yearIncDACS, electrifiedDemand, elecDemandScen,interconn):

    m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\"


    if buildLimitsCase == 1: case_name = "reference"
    elif buildLimitsCase == 2: case_name = "lNuclear"
    elif buildLimitsCase == 3: case_name = "lNuclearCCS"
    elif buildLimitsCase == 4: case_name = "lH2"
    elif buildLimitsCase == 5: case_name = "lTrans"

    pythonFolder = 'C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\'

    if emissionSystem == 'Negative':
        resultsDir = 'Results_' + interconn + '_' + emissionSystem + 'NEin' + str(planNESystem) + '_' + str(int(co2EmsCapInFinalYear/1e6)) \
                     + '_' + str(electrifiedDemand) + elecDemandScen + case_name
        resultsFolder = pythonFolder + 'Results_' + interconn + '_' + emissionSystem + str(int(co2EmsCapInFinalYear/1e6)) + '_' + 'DACS' + str(yearIncDACS) \
                        + 'NEin' + str(planNESystem) + '_' + case_name + '_' + str(electrifiedDemand) + elecDemandScen
    elif emissionSystem == 'NetZero':
        resultsDir = 'Results_' + interconn + '_' + emissionSystem + '_' + str(int(co2EmsCapInFinalYear/1e6)) \
                     + '_' + str(electrifiedDemand) + elecDemandScen + case_name
        resultsFolder = pythonFolder + 'Results_' + interconn + '_' + emissionSystem + '_' + 'DACS' + str(yearIncDACS) \
                        + '_' + case_name + '_' + str(electrifiedDemand) + elecDemandScen


    resultsFolder2050 = '\\2050' + 'CO2Cap' + str(int(co2EmsCapInFinalYear / 1e6)) + '\\CE\\'

    if planNESystem == 2030 and emissionSystem == 'Negative':
        resultsFolder2030 = '\\2030' + 'CO2Cap' + str(int(co2EmsCapInFinalYear/1e6)) + '\\CE\\'
    elif planNESystem == 2040 and emissionSystem == 'Negative':
        resultsFolder2040 = '\\2040' + 'CO2Cap' + str(int(co2EmsCapInFinalYear / 1e6)) + '\\CE\\'


    # Set up the excel file
    results_book = xw.Workbook(pythonFolder + 'Results Summary\\' + resultsDir + '.xlsx')
    result_sheet_cost = results_book.add_worksheet('Costs')
    result_sheet_CE = results_book.add_worksheet('CE')
    result_sheet_Generation = results_book.add_worksheet('Generation')
    result_sheet_Generation_new = results_book.add_worksheet('New Generation')

    # read in new capacity investment solution:
    genFleetAfter2050 = pd.read_csv(resultsFolder + resultsFolder2050 + 'genFleetAfterCE2050.csv')
    genFleetAfter2050 = genFleetAfter2050[genFleetAfter2050.YearAddedCE >= 2030]

    # Costs:
    if planNESystem == 2030 and emissionSystem == 'Negative':
        vZannual_2030 = pd.read_csv(resultsFolder + resultsFolder2030 + 'vZannualCE2030.csv', header=None)
        vVarcostannual_2030 = pd.read_csv(resultsFolder + resultsFolder2030 + 'vVarcostannualCE2030.csv', header=None)
        vZannual_2030 = vZannual_2030.iloc[0, 0] / 1000
        vVarcostannual_2030 = vVarcostannual_2030.iloc[0, 0] / 1000
        vFixedcostannual_2030 = vZannual_2030 - vVarcostannual_2030
        vZannual_2040 = 0
        vVarcostannual_2040 = 0
        vFixedcostannual_2040 = 0
    elif planNESystem == 2040 and emissionSystem == 'Negative':
        vZannual_2040 = pd.read_csv(resultsFolder + resultsFolder2040 + 'vZannualCE2040.csv', header=None)
        vVarcostannual_2040 = pd.read_csv(resultsFolder + resultsFolder2040 + 'vVarcostannualCE2040.csv', header=None)
        vZannual_2040 = vZannual_2040.iloc[0, 0] / 1000
        vVarcostannual_2040 = vVarcostannual_2040.iloc[0, 0] / 1000
        vFixedcostannual_2040 = vZannual_2040 - vVarcostannual_2040
        vZannual_2030 = 0
        vVarcostannual_2030 = 0
        vFixedcostannual_2030 = 0

    if planNESystem == 2020 or planNESystem == 2050 or emissionSystem == 'NetZero':
        vZannual_2030 = 0
        vVarcostannual_2030 = 0
        vFixedcostannual_2030 = 0

        vZannual_2040 = 0
        vVarcostannual_2040 = 0
        vFixedcostannual_2040 = 0

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
    if planNESystem == 2030 and emissionSystem == 'Negative':
        genFleetAfter2030 = genFleetAfter2050[genFleetAfter2050.YearAddedCE == 2030]
        genFleetAfter2030 = genFleetAfter2030[['PlantType', 'Capacity (MW)']]

        CoalCCS_2030 = genFleetAfter2030[genFleetAfter2030['PlantType'].str.contains('Coal Steam CCS')]
        CC_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'].str.contains('Combined Cycle')]
        CCCCS_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'].str.contains('Combined Cycle CCS')]
        Nuclear_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'].str.contains('Nuclear')]
        Hydrogen_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'].str.contains('Hydrogen')]
        Battery_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'].str.contains('Battery Storage')]
        DAC_2030 = genFleetAfter2030.loc[genFleetAfter2030['PlantType'].str.contains('DAC')]
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

        CoalCCS_2040 = 0
        CC_2040 = 0
        CCCCS_2040 = 0
        Nuclear_2040 = 0
        Hydrogen_2040 = 0
        Battery_2040 = 0
        DAC_2040 = 0
        Wind_2040 = 0
        Solar_2040 = 0

        # Existing Generation:
        # 2030:
        vGen_2030 = pd.read_csv(resultsFolder + resultsFolder2030 + 'vGenCE2030.csv')
        vGen_2030.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
        vGen_2030 = vGen_2030.T
        vGen_2030.columns = vGen_2030.iloc[0]
        vGen_2030 = vGen_2030.drop(vGen_2030.index[0])
        vGen_2030 = vGen_2030.reset_index()
        vGen_2030.rename(columns={'index': 'Unit'}, inplace=True)

        genforCE2030_existing = pd.read_csv(resultsFolder + resultsFolder2030 + 'genFleetForCE2030.csv')
        genforCE2030_existing = genforCE2030_existing[['PlantType']]

        vGen_2030['Total Gen'] = vGen_2030.iloc[:, 1:].sum(axis=1)
        vGen_2030 = vGen_2030[['Total Gen']]
        vGen_2030['PlantType'] = genforCE2030_existing

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

        # New generation:
        # 2030:
        vGen_new_2030 = pd.read_csv(resultsFolder + resultsFolder2030 + 'vGentechCE2030.csv')
        vGen_new_2030.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
        vGen_new_2030 = vGen_new_2030.T
        vGen_new_2030.columns = vGen_new_2030.iloc[0]
        vGen_new_2030 = vGen_new_2030.drop(vGen_new_2030.index[0])
        vGen_new_2030 = vGen_new_2030.reset_index()
        vGen_new_2030.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

        vGen_new_2030['Total Gen'] = vGen_new_2030.iloc[:, 1:].sum(axis=1)
        vGen_new_2030 = vGen_new_2030[['Total Gen', 'GAMS Symbol']]

        gen_CoalSteam_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('Coal Steam CCS')]
        gen_CC_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('Combined Cycle')]
        gen_CCCCS_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('Combined Cycle CCS')]
        gen_Bat_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('Battery Storage')]
        gen_H2_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('Hydrogen')]
        gen_Nuclear_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('Nuclear')]
        gen_DAC_new_2030 = vGen_new_2030.loc[vGen_new_2030['GAMS Symbol'].str.contains('DAC')]
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
        gen_CC_new_2030 = gen_CC_new_2030 - gen_CCCCS_new_2030

        gen_CoalSteam_new_2040 = 0
        gen_CC_new_2040 = 0
        gen_CCCCS_new_2040 = 0
        gen_Bat_new_2040 = 0
        gen_H2_new_2040 = 0
        gen_Nuclear_new_2040 = 0
        gen_Solar_new_2040 = 0
        gen_Wind_new_2040 = 0
        gen_DAC_new_2040 = 0
        gen_CC_new_2040 = 0

    elif planNESystem == 2040 and emissionSystem == 'Negative':
        genFleetAfter2040 = genFleetAfter2050[genFleetAfter2050.YearAddedCE == 2040]
        genFleetAfter2040 = genFleetAfter2040[['PlantType', 'Capacity (MW)']]

        CoalCCS_2040 = genFleetAfter2040[genFleetAfter2040['PlantType'].str.contains('Coal Steam CCS')]
        CC_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'].str.contains('Combined Cycle')]
        CCCCS_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'].str.contains('Combined Cycle CCS')]
        Nuclear_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'].str.contains('Nuclear')]
        Hydrogen_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'].str.contains('Hydrogen')]
        Battery_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'].str.contains('Battery Storage')]
        DAC_2040 = genFleetAfter2040.loc[genFleetAfter2040['PlantType'].str.contains('DAC')]
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

        CoalCCS_2030 = 0
        CC_2030 = 0
        CCCCS_2030 = 0
        Nuclear_2030 = 0
        Hydrogen_2030 = 0
        Battery_2030 = 0
        DAC_2030 = 0
        Wind_2030 = 0
        Solar_2030 = 0

        # Existing Generation:
        # 2040:
        vGen_2040 = pd.read_csv(resultsFolder + resultsFolder2040 + 'vGenCE2040.csv')
        vGen_2040.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
        vGen_2040 = vGen_2040.T
        vGen_2040.columns = vGen_2040.iloc[0]
        vGen_2040 = vGen_2040.drop(vGen_2040.index[0])
        vGen_2040 = vGen_2040.reset_index()
        vGen_2040.rename(columns={'index': 'Unit'}, inplace=True)

        genforCE2040_existing = pd.read_csv(resultsFolder + resultsFolder2040 + 'genFleetForCE2040.csv')
        genforCE2040_existing = genforCE2040_existing[['PlantType']]

        vGen_2040['Total Gen'] = vGen_2040.iloc[:, 1:].sum(axis=1)
        vGen_2040 = vGen_2040[['Total Gen']]
        vGen_2040['PlantType'] = genforCE2040_existing

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

        # New generation:
        # 2040:
        vGen_new_2040 = pd.read_csv(resultsFolder + resultsFolder2040 + 'vGentechCE2040.csv')
        vGen_new_2040.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
        vGen_new_2040 = vGen_new_2040.T
        vGen_new_2040.columns = vGen_new_2040.iloc[0]
        vGen_new_2040 = vGen_new_2040.drop(vGen_new_2040.index[0])
        vGen_new_2040 = vGen_new_2040.reset_index()
        vGen_new_2040.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

        vGen_new_2040['Total Gen'] = vGen_new_2040.iloc[:, 1:].sum(axis=1)
        vGen_new_2040 = vGen_new_2040[['Total Gen', 'GAMS Symbol']]

        gen_CoalSteam_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('Coal Steam CCS')]
        gen_CC_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('Combined Cycle')]
        gen_CCCCS_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('Combined Cycle CCS')]
        gen_Bat_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('Battery Storage')]
        gen_H2_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('Hydrogen')]
        gen_Nuclear_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('Nuclear')]
        gen_DAC_new_2040 = vGen_new_2040.loc[vGen_new_2040['GAMS Symbol'].str.contains('DAC')]
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
        gen_CC_new_2040 = gen_CC_new_2040 - gen_CCCCS_new_2040

        gen_CoalSteam_new_2030 = 0
        gen_CC_new_2030 = 0
        gen_CCCCS_new_2030 = 0
        gen_Bat_new_2030 = 0
        gen_H2_new_2030 = 0
        gen_Nuclear_new_2030 = 0
        gen_Solar_new_2030 = 0
        gen_Wind_new_2030 = 0
        gen_DAC_new_2030 = 0
        gen_CC_new_2030 = 0

    # Costs:
    vZannual_2050 = pd.read_csv(resultsFolder + resultsFolder2050 + 'vZannualCE2050.csv', header=None)
    vVarcostannual_2050 = pd.read_csv(resultsFolder + resultsFolder2050 + 'vVarcostannualCE2050.csv', header=None)

    vZannual_2050 = vZannual_2050.iloc[0,0]/1000
    vVarcostannual_2050 = vVarcostannual_2050.iloc[0, 0] / 1000
    vFixedcostannual_2050 = vZannual_2050 - vVarcostannual_2050

    if planNESystem == 2020 or planNESystem == 2050 or emissionSystem =='NetZero':
        vZannual_2030 = 0
        vVarcostannual_2030 = 0
        vFixedcostannual_2030 = 0

        vZannual_2040 = 0
        vVarcostannual_2040 = 0
        vFixedcostannual_2040 = 0

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
    vGen_2050 = pd.read_csv(resultsFolder + resultsFolder2050 + 'vGenCE2050.csv')
    vGen_2050.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    vGen_2050 = vGen_2050.T
    vGen_2050.columns = vGen_2050.iloc[0]
    vGen_2050 = vGen_2050.drop(vGen_2050.index[0])
    vGen_2050 = vGen_2050.reset_index()
    vGen_2050.rename(columns={'index': 'Unit'}, inplace=True)

    # read in plant type for existing generation:
    genforCE2050_existing = pd.read_csv(resultsFolder + resultsFolder2050 + 'genFleetForCE2050.csv')
    genforCE2050_existing = genforCE2050_existing[['PlantType']]

    # Generation:
    # 2050:
    vGen_2050['Total Gen'] = vGen_2050.iloc[:, 1:].sum(axis=1)
    vGen_2050 = vGen_2050[['Total Gen']]
    vGen_2050['PlantType'] = genforCE2050_existing

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
    vGen_new_2050 = pd.read_csv(resultsFolder + resultsFolder2050 + 'vGentechCE2050.csv')
    vGen_new_2050.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    vGen_new_2050 = vGen_new_2050.T
    vGen_new_2050.columns = vGen_new_2050.iloc[0]
    vGen_new_2050 = vGen_new_2050.drop(vGen_new_2050.index[0])
    vGen_new_2050 = vGen_new_2050.reset_index()
    vGen_new_2050.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    # 2050:
    vGen_new_2050['Total Gen'] = vGen_new_2050.iloc[:, 1:].sum(axis=1)
    vGen_new_2050 = vGen_new_2050[['Total Gen', 'GAMS Symbol']]

    gen_CoalSteam_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('Coal Steam CCS')]
    gen_CC_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('Combined Cycle')]
    gen_CCCCS_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    gen_Bat_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('Battery Storage')]
    gen_H2_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('Hydrogen')]
    gen_Nuclear_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('Nuclear')]
    gen_DAC_new_2050 = vGen_new_2050.loc[vGen_new_2050['GAMS Symbol'].str.contains('DAC')]
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
    gen_CC_new_2050 = gen_CC_new_2050 - gen_CCCCS_new_2050

    if planNESystem == 2020 or planNESystem == 2050 or emissionSystem == 'NetZero':
        gen_CoalSteam_new_2030 = 0
        gen_CC_new_2030 = 0
        gen_CCCCS_new_2030 = 0
        gen_Bat_new_2030 = 0
        gen_H2_new_2030 = 0
        gen_Nuclear_new_2030 = 0
        gen_Solar_new_2030 = 0
        gen_Wind_new_2030 = 0
        gen_DAC_new_2030 = 0
        gen_CC_new_2030 = 0

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

        CoalCCS_2030 = 0
        CC_2030 = 0
        CCCCS_2030 = 0
        Nuclear_2030 = 0
        Hydrogen_2030 = 0
        Battery_2030 = 0
        DAC_2030 = 0
        Wind_2030 = 0
        Solar_2030 = 0

        gen_CoalSteam_new_2040 = 0
        gen_CC_new_2040 = 0
        gen_CCCCS_new_2040 = 0
        gen_Bat_new_2040 = 0
        gen_H2_new_2040 = 0
        gen_Nuclear_new_2040 = 0
        gen_Solar_new_2040 = 0
        gen_Wind_new_2040 = 0
        gen_DAC_new_2040 = 0
        gen_CC_new_2040 = 0

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

        CoalCCS_2040 = 0
        CC_2040 = 0
        CCCCS_2040 = 0
        Nuclear_2040 = 0
        Hydrogen_2040 = 0
        Battery_2040 = 0
        DAC_2040 = 0
        Wind_2040 = 0
        Solar_2040 = 0

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
    result_sheet_CE.write("C10", DAC_2040)

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

    if planNESystem == 2050 and emissionSystem =='Negative':
        resultsFolder2060 = '\\2060' + 'CO2Cap' + str(int(co2EmsCapInFinalYear / 1e6)) + '\\CE\\'

        # read in new capacity investment solution:
        genFleetAfter2060 = pd.read_csv(resultsFolder + resultsFolder2060 + 'genFleetAfterCE2060.csv')
        genFleetAfter2060 = genFleetAfter2060[genFleetAfter2060.YearAddedCE > 2050]

        # Costs:
        vZannual_2060 = pd.read_csv(resultsFolder + resultsFolder2060 + 'vZannualCE2060.csv', header=None)
        vVarcostannual_2060 = pd.read_csv(resultsFolder + resultsFolder2060 + 'vVarcostannualCE2060.csv', header=None)
        vZannual_2060 = vZannual_2060.iloc[0, 0] / 1000
        vVarcostannual_2060 = vVarcostannual_2060.iloc[0, 0] / 1000
        vFixedcostannual_2060 = vZannual_2060 - vVarcostannual_2060

        result_sheet_cost.write("D1", "total Operating cost 2051 (million $)")
        result_sheet_cost.write("E1", vVarcostannual_2060)

        result_sheet_cost.write("D6", "total Fixed cost 2051 (million $)")
        result_sheet_cost.write("E6", vFixedcostannual_2060)

        result_sheet_cost.write("D12", "total cost 2051 (million $)")
        result_sheet_cost.write("E12", vZannual_2060)

        # CE:
        genFleetAfter2060 = genFleetAfter2060[genFleetAfter2060.YearAddedCE == 2060]
        genFleetAfter2060 = genFleetAfter2060[['PlantType', 'Capacity (MW)']]

        CoalCCS_2060 = genFleetAfter2060[genFleetAfter2060['PlantType'].str.contains('Coal Steam CCS')]
        CC_2060 = genFleetAfter2060.loc[genFleetAfter2060['PlantType'].str.contains('Combined Cycle')]
        CCCCS_2060 = genFleetAfter2060.loc[genFleetAfter2060['PlantType'].str.contains('Combined Cycle CCS')]
        Nuclear_2060 = genFleetAfter2060.loc[genFleetAfter2060['PlantType'].str.contains('Nuclear')]
        Hydrogen_2060 = genFleetAfter2060.loc[genFleetAfter2060['PlantType'].str.contains('Hydrogen')]
        Battery_2060 = genFleetAfter2060.loc[genFleetAfter2060['PlantType'].str.contains('Battery Storage')]
        DAC_2060 = genFleetAfter2060.loc[genFleetAfter2060['PlantType'].str.contains('DAC')]
        Wind_2060 = genFleetAfter2060[genFleetAfter2060['PlantType'].str.contains('wind')]
        Solar_2060 = genFleetAfter2060[genFleetAfter2060['PlantType'].str.contains('solar')]

        CoalCCS_2060 = CoalCCS_2060['Capacity (MW)'].sum()
        CC_2060 = CC_2060['Capacity (MW)'].sum()
        CCCCS_2060 = CCCCS_2060['Capacity (MW)'].sum()
        Nuclear_2060 = Nuclear_2060['Capacity (MW)'].sum()
        Hydrogen_2060 = Hydrogen_2060['Capacity (MW)'].sum()
        Battery_2060 = Battery_2060['Capacity (MW)'].sum()
        DAC_2060 = DAC_2060['Capacity (MW)'].sum()
        Wind_2060 = Wind_2060['Capacity (MW)'].sum()
        Solar_2060 = Solar_2060['Capacity (MW)'].sum()

        # Existing Generation:
        vGen_2060 = pd.read_csv(resultsFolder + resultsFolder2060 + 'vGenCE2060.csv')
        vGen_2060.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
        vGen_2060 = vGen_2060.T
        vGen_2060.columns = vGen_2060.iloc[0]
        vGen_2060 = vGen_2060.drop(vGen_2060.index[0])
        vGen_2060 = vGen_2060.reset_index()
        vGen_2060.rename(columns={'index': 'Unit'}, inplace=True)

        genforCE2060_existing = pd.read_csv(resultsFolder + resultsFolder2060 + 'genFleetForCE2060.csv')
        genforCE2060_existing = genforCE2060_existing[['PlantType']]

        vGen_2060['Total Gen'] = vGen_2060.iloc[:, 1:].sum(axis=1)
        vGen_2060 = vGen_2060[['Total Gen']]
        vGen_2060['PlantType'] = genforCE2060_existing

        gen_CoalSteam_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Coal Steam']
        gen_CC_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Combined Cycle']
        gen_CCCCS_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Combined Cycle CCS']
        gen_CT_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Combustion Turbine']
        gen_OG_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'O/G Steam']
        gen_Bio_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Biomass']
        gen_Bat_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Energy Storage']
        gen_H2_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Hydrogen']
        gen_Nuclear_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'Nuclear']
        gen_DAC_2060 = vGen_2060.loc[vGen_2060['PlantType'] == 'DAC']
        gen_Solar_2060 = vGen_2060[vGen_2060['PlantType'].str.contains('solar')]
        gen_Wind_2060 = vGen_2060[vGen_2060['PlantType'].str.contains('wind')]

        gen_CoalSteam_2060 = gen_CoalSteam_2060['Total Gen'].sum()
        gen_CC_2060 = gen_CC_2060['Total Gen'].sum()
        gen_CCCCS_2060 = gen_CCCCS_2060['Total Gen'].sum()
        gen_Bat_2060 = gen_Bat_2060['Total Gen'].sum()
        gen_H2_2060 = gen_H2_2060['Total Gen'].sum()
        gen_Nuclear_2060 = gen_Nuclear_2060['Total Gen'].sum()
        gen_Solar_2060 = gen_Solar_2060['Total Gen'].sum()
        gen_Wind_2060 = gen_Wind_2060['Total Gen'].sum()
        gen_DAC_2060 = gen_DAC_2060['Total Gen'].sum()
        gen_CT_2060 = gen_CT_2060['Total Gen'].sum()
        gen_OG_2060 = gen_OG_2060['Total Gen'].sum()
        gen_Bio_2060 = gen_Bio_2060['Total Gen'].sum()

        # New generation:
        vGen_new_2060 = pd.read_csv(resultsFolder + resultsFolder2060 + 'vGentechCE2060.csv')
        vGen_new_2060.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
        vGen_new_2060 = vGen_new_2060.T
        vGen_new_2060.columns = vGen_new_2060.iloc[0]
        vGen_new_2060 = vGen_new_2060.drop(vGen_new_2060.index[0])
        vGen_new_2060 = vGen_new_2060.reset_index()
        vGen_new_2060.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

        vGen_new_2060['Total Gen'] = vGen_new_2060.iloc[:, 1:].sum(axis=1)
        vGen_new_2060 = vGen_new_2060[['Total Gen', 'GAMS Symbol']]

        gen_CoalSteam_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('Coal Steam CCS')]
        gen_CC_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('Combined Cycle')]
        gen_CCCCS_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('Combined Cycle CCS')]
        gen_Bat_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('Battery Storage')]
        gen_H2_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('Hydrogen')]
        gen_Nuclear_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('Nuclear')]
        gen_DAC_new_2060 = vGen_new_2060.loc[vGen_new_2060['GAMS Symbol'].str.contains('DAC')]
        gen_Solar_new_2060 = vGen_new_2060[vGen_new_2060['GAMS Symbol'].str.contains('solar')]
        gen_Wind_new_2060 = vGen_new_2060[vGen_new_2060['GAMS Symbol'].str.contains('wind')]

        gen_CoalSteam_new_2060 = gen_CoalSteam_new_2060['Total Gen'].sum()
        gen_CC_new_2060 = gen_CC_new_2060['Total Gen'].sum()
        gen_CCCCS_new_2060 = gen_CCCCS_new_2060['Total Gen'].sum()
        gen_Bat_new_2060 = gen_Bat_new_2060['Total Gen'].sum()
        gen_H2_new_2060 = gen_H2_new_2060['Total Gen'].sum()
        gen_Nuclear_new_2060 = gen_Nuclear_new_2060['Total Gen'].sum()
        gen_Solar_new_2060 = gen_Solar_new_2060['Total Gen'].sum()
        gen_Wind_new_2060 = gen_Wind_new_2060['Total Gen'].sum()
        gen_DAC_new_2060 = gen_DAC_new_2060['Total Gen'].sum()
        gen_CC_new_2060 = gen_CC_new_2060 - gen_CCCCS_new_2060

        # Write in excel:
        result_sheet_CE.write("G1", "2051")
        result_sheet_CE.write("H1", "Total (including 2051)")

        result_sheet_CE.write("G2", CoalCCS_2060)
        result_sheet_CE.write("G3", CC_2060)
        result_sheet_CE.write("G4", CCCCS_2060)
        result_sheet_CE.write("G5", Nuclear_2060)
        result_sheet_CE.write("G6", Wind_2060)
        result_sheet_CE.write("G7", Solar_2060)
        result_sheet_CE.write("G8", Battery_2060)
        result_sheet_CE.write("G9", Hydrogen_2060)
        result_sheet_CE.write("G10", DAC_2060)

        result_sheet_CE.write("H2", CoalCCS_2030 + CoalCCS_2040 + CoalCCS_2050 + CoalCCS_2060)
        result_sheet_CE.write("H3", CC_2030 + CC_2040 + CC_2050 + CC_2060)
        result_sheet_CE.write("H4", CCCCS_2030 + CCCCS_2040 + CCCCS_2050 + CCCCS_2060)
        result_sheet_CE.write("H5", Nuclear_2030 + Nuclear_2040 + Nuclear_2050 + Nuclear_2060)
        result_sheet_CE.write("H6", Wind_2030 + Wind_2040 + Wind_2050 + Wind_2060)
        result_sheet_CE.write("H7", Solar_2030 + Solar_2040 + Solar_2050 + Solar_2060)
        result_sheet_CE.write("H8", Battery_2030 + Battery_2040 + Battery_2050 + Battery_2060)
        result_sheet_CE.write("H9", Hydrogen_2030 + Hydrogen_2040 + Hydrogen_2050 + Hydrogen_2060)
        result_sheet_CE.write("H10", DAC_2030 + DAC_2040 + DAC_2050 + DAC_2060)

        # Generation:
        result_sheet_Generation.write("G1", "2051")
        result_sheet_Generation.write("H1", "Total (including 2051")

        result_sheet_Generation.write("G2", gen_CoalSteam_2060)
        result_sheet_Generation.write("G3", gen_CC_2060)
        result_sheet_Generation.write("G4", gen_CCCCS_2060)
        result_sheet_Generation.write("G5", gen_Nuclear_2060)
        result_sheet_Generation.write("G6", gen_Wind_2060)
        result_sheet_Generation.write("G7", gen_Solar_2060)
        result_sheet_Generation.write("G8", gen_Bat_2060)
        result_sheet_Generation.write("G9", gen_H2_2060)
        result_sheet_Generation.write("G10", gen_DAC_2060)
        result_sheet_Generation.write("G11", gen_CT_2060)
        result_sheet_Generation.write("G12", gen_OG_2060)
        result_sheet_Generation.write("G13", gen_Bio_2060)

        # new Generation:
        result_sheet_Generation_new.write("G1", "2051")
        result_sheet_Generation_new.write("H1", "Total (including 2051)")

        result_sheet_Generation_new.write("G2", gen_CoalSteam_new_2060)
        result_sheet_Generation_new.write("G3", gen_CC_new_2060)
        result_sheet_Generation_new.write("G4", gen_CCCCS_new_2060)
        result_sheet_Generation_new.write("G5", gen_Nuclear_new_2060)
        result_sheet_Generation_new.write("G6", gen_Wind_new_2060)
        result_sheet_Generation_new.write("G7", gen_Solar_new_2060)
        result_sheet_Generation_new.write("G8", gen_Bat_new_2060)
        result_sheet_Generation_new.write("G9", gen_H2_new_2060)
        result_sheet_Generation_new.write("G10", gen_DAC_new_2060)

        result_sheet_Generation_new.write("H2", gen_CoalSteam_new_2030 + gen_CoalSteam_new_2040 + gen_CoalSteam_new_2050 + gen_CoalSteam_new_2060)
        result_sheet_Generation_new.write("H3", gen_CC_new_2030 + gen_CC_new_2040 + gen_CC_new_2050 + gen_CC_new_2060)
        result_sheet_Generation_new.write("H4", gen_CCCCS_new_2030 + gen_CCCCS_new_2040 + gen_CCCCS_new_2050 + gen_CCCCS_new_2060)
        result_sheet_Generation_new.write("H5", gen_Nuclear_new_2030 + gen_Nuclear_new_2040 + gen_Nuclear_new_2050 + gen_Nuclear_new_2060)
        result_sheet_Generation_new.write("H6", gen_Wind_new_2030 + gen_Wind_new_2040 + gen_Wind_new_2050 + gen_Wind_new_2060)
        result_sheet_Generation_new.write("H7", gen_Solar_new_2030 + gen_Solar_new_2040 + gen_Solar_new_2050 + gen_Solar_new_2060)
        result_sheet_Generation_new.write("H8", gen_Bat_new_2030 + gen_Bat_new_2040 + gen_Bat_new_2050 + gen_Bat_new_2060)
        result_sheet_Generation_new.write("H9", gen_H2_new_2030 + gen_H2_new_2040 + gen_H2_new_2050 + gen_H2_new_2060)
        result_sheet_Generation_new.write("H10", gen_DAC_new_2030 + gen_DAC_new_2040 + gen_DAC_new_2050 + gen_DAC_new_2060)

    results_book.close()