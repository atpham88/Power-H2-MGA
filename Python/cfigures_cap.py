import pandas as pd
import numpy as np

def cap_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2):
    # read in new capacity investment solution:
    resultsCE_NZ = pd.read_csv(m_dir2+resultsDir_other_NZ + 'genFleetAfterCE2050.csv')
    resultsCE_NE2020 = pd.read_csv(m_dir2+resultsDir_other_NE2020 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2030 = pd.read_csv(m_dir2+resultsDir_other_NE2030 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2040 = pd.read_csv(m_dir2+resultsDir_other_NE2040 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'genFleetAfterCE2060.csv')

    resultsCE_NZ = resultsCE_NZ[resultsCE_NZ.YearAddedCE >= 2030]
    resultsCE_NE2020 = resultsCE_NE2020[resultsCE_NE2020.YearAddedCE >= 2030]
    resultsCE_NE2030 = resultsCE_NE2030[resultsCE_NE2030.YearAddedCE >= 2030]
    resultsCE_NE2040 = resultsCE_NE2040[resultsCE_NE2040.YearAddedCE >= 2030]
    resultsCE_NE2050 = resultsCE_NE2050[resultsCE_NE2050.YearAddedCE >= 2030]

    resultsCE_NZ = resultsCE_NZ[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2020 = resultsCE_NE2020[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2030 = resultsCE_NE2030[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2040 = resultsCE_NE2040[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2050 = resultsCE_NE2050[['PlantType', 'Capacity (MW)', 'region']]

    CoalCCS_CE_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Coal Steam CCS')]['Capacity (MW)'].sum()
    Coal_CE_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Coal Steam')]['Capacity (MW)'].sum() - CoalCCS_CE_NZ
    CCCCS_CE_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Combined Cycle CCS')]['Capacity (MW)'].sum()
    CC_CE_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Combined Cycle')]['Capacity (MW)'].sum() - CCCCS_CE_NZ
    nuclear_CE_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Nuclear')]['Capacity (MW)'].sum()
    wind_CE_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Wind')]['Capacity (MW)'].sum() \
                 + resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('wind')]['Capacity (MW)'].sum()
    solar_CE_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Solar')]['Capacity (MW)'].sum() \
                  + resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('solar')]['Capacity (MW)'].sum()
    battery_CE_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Battery Storage')]['Capacity (MW)'].sum() \
                    + resultsCE_NZ.loc[resultsCE_NZ['PlantType'].str.contains('Batteries')]['Capacity (MW)'].sum()
    hydrogen_CE_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Hydrogen')]['Capacity (MW)'].sum()
    dac_CE_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('DAC')]['Capacity (MW)'].sum()

    CoalCCS_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Coal Steam CCS') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CCCCS_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CC_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    nuclear_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Nuclear') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    battery_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Batteries') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                         + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Battery Storage') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    hydrogen_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Hydrogen') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    dac_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'DAC') & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    wind_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Wind')) & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                      + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('wind')) & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()
    solar_CE_SERC_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Solar')) & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                       + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('solar')) & (resultsCE_NZ['region'] == 'SERC'))]['Capacity (MW)'].sum()

    CoalCCS_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Coal Steam CCS') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CCCCS_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CC_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    nuclear_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Nuclear') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    battery_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Batteries') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                         + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Battery Storage') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    hydrogen_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Hydrogen') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    dac_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'DAC') & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    wind_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Wind')) & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                      + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('wind')) & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()
    solar_CE_MISO_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Solar')) & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                       + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('solar')) & (resultsCE_NZ['region'] == 'MISO'))]['Capacity (MW)'].sum()

    CoalCCS_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Coal Steam CCS') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CCCCS_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CC_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    nuclear_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Nuclear') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    battery_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Batteries') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                        + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Battery Storage') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    hydrogen_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Hydrogen') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    dac_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'DAC') & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    wind_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Wind')) & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                     + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('wind')) & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()
    solar_CE_PJM_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Solar')) & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                      + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('solar')) & (resultsCE_NZ['region'] == 'PJM'))]['Capacity (MW)'].sum()

    CoalCCS_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Coal Steam CCS') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CCCCS_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CC_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    nuclear_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Nuclear') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    battery_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Batteries') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                        + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Battery Storage') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    hydrogen_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Hydrogen') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    dac_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'DAC') & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    wind_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Wind')) & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                     + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('wind')) & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()
    solar_CE_SPP_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Solar')) & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                      + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('solar')) & (resultsCE_NZ['region'] == 'SPP'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Coal Steam CCS') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    CCCCS_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    CC_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    nuclear_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Nuclear') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    battery_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Batteries') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum() \
                       + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Battery Storage') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    hydrogen_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Hydrogen') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    dac_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'DAC') & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    wind_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Wind')) & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum() \
                    + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('wind')) & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()
    solar_CE_NY_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Solar')) & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum() \
                     + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('solar')) & (resultsCE_NZ['region'] == 'NY'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Coal Steam CCS') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    CCCCS_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    CC_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Combined Cycle') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    nuclear_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Nuclear') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    battery_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Batteries') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum() \
                       + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Battery Storage') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    hydrogen_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'Hydrogen') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    dac_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'] == 'DAC') & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    wind_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Wind')) & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum() \
                    + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('wind')) & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()
    solar_CE_NE_NZ = resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('Solar')) & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum() \
                     + resultsCE_NZ.loc[((resultsCE_NZ['PlantType'].str.contains('solar')) & (resultsCE_NZ['region'] == 'NE'))]['Capacity (MW)'].sum()


    # NE2020:
    CoalCCS_CE_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Coal Steam CCS')]['Capacity (MW)'].sum()
    CCCCS_CE_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Combined Cycle CCS')]['Capacity (MW)'].sum()
    CC_CE_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Combined Cycle')]['Capacity (MW)'].sum() - CCCCS_CE_NE2020
    nuclear_CE_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Nuclear')]['Capacity (MW)'].sum()
    wind_CE_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Wind')]['Capacity (MW)'].sum() \
                     + resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('wind')]['Capacity (MW)'].sum()
    solar_CE_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Solar')]['Capacity (MW)'].sum() \
                      + resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('solar')]['Capacity (MW)'].sum()
    battery_CE_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Battery Storage')]['Capacity (MW)'].sum() \
                        + resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'].str.contains('Batteries')]['Capacity (MW)'].sum()
    hydrogen_CE_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Hydrogen')]['Capacity (MW)'].sum()
    dac_CE_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('DAC')]['Capacity (MW)'].sum()

    CoalCCS_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CCCCS_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CC_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    nuclear_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Nuclear') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    battery_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Batteries') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Battery Storage') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    hydrogen_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Hydrogen') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    dac_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'DAC') & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    wind_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Wind')) & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('wind')) & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()
    solar_CE_SERC_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Solar')) & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('solar')) & (resultsCE_NE2020['region'] == 'SERC'))]['Capacity (MW)'].sum()

    CoalCCS_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CCCCS_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CC_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    nuclear_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Nuclear') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    battery_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Batteries') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Battery Storage') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    hydrogen_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Hydrogen') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    dac_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'DAC') & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    wind_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Wind')) & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('wind')) & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()
    solar_CE_MISO_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Solar')) & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('solar')) & (resultsCE_NE2020['region'] == 'MISO'))]['Capacity (MW)'].sum()

    CoalCCS_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CCCCS_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CC_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    nuclear_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Nuclear') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    battery_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Batteries') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Battery Storage') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    hydrogen_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Hydrogen') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    dac_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'DAC') & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    wind_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Wind')) & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('wind')) & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()
    solar_CE_PJM_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Solar')) & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('solar')) & (resultsCE_NE2020['region'] == 'PJM'))]['Capacity (MW)'].sum()

    CoalCCS_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CCCCS_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CC_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    nuclear_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Nuclear') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    battery_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Batteries') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Battery Storage') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    hydrogen_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Hydrogen') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    dac_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'DAC') & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    wind_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Wind')) & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('wind')) & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()
    solar_CE_SPP_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Solar')) & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('solar')) & (resultsCE_NE2020['region'] == 'SPP'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    CCCCS_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    CC_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    nuclear_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Nuclear') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    battery_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Batteries') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Battery Storage') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    hydrogen_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Hydrogen') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    dac_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'DAC') & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    wind_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Wind')) & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('wind')) & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()
    solar_CE_NY_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Solar')) & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('solar')) & (resultsCE_NE2020['region'] == 'NY'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    CCCCS_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    CC_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Combined Cycle') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    nuclear_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Nuclear') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    battery_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Batteries') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Battery Storage') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    hydrogen_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'Hydrogen') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    dac_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'] == 'DAC') & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    wind_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Wind')) & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('wind')) & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()
    solar_CE_NE_NE2020 = resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('Solar')) & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2020.loc[((resultsCE_NE2020['PlantType'].str.contains('solar')) & (resultsCE_NE2020['region'] == 'NE'))]['Capacity (MW)'].sum()

    # NE2030:
    CoalCCS_CE_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Coal Steam CCS')]['Capacity (MW)'].sum()
    CCCCS_CE_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Combined Cycle CCS')]['Capacity (MW)'].sum()
    CC_CE_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Combined Cycle')]['Capacity (MW)'].sum() - CCCCS_CE_NE2030
    nuclear_CE_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Nuclear')]['Capacity (MW)'].sum()
    wind_CE_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Wind')]['Capacity (MW)'].sum() \
                     + resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('wind')]['Capacity (MW)'].sum()
    solar_CE_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Solar')]['Capacity (MW)'].sum() \
                      + resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('solar')]['Capacity (MW)'].sum()
    battery_CE_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Battery Storage')]['Capacity (MW)'].sum() \
                        + resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'].str.contains('Batteries')]['Capacity (MW)'].sum()
    hydrogen_CE_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Hydrogen')]['Capacity (MW)'].sum()
    dac_CE_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('DAC')]['Capacity (MW)'].sum()

    CoalCCS_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CCCCS_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CC_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    nuclear_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Nuclear') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    battery_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Batteries') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Battery Storage') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    hydrogen_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Hydrogen') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    dac_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'DAC') & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    wind_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Wind')) & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('wind')) & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()
    solar_CE_SERC_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Solar')) & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('solar')) & (resultsCE_NE2030['region'] == 'SERC'))]['Capacity (MW)'].sum()

    CoalCCS_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CCCCS_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CC_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    nuclear_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Nuclear') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    battery_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Batteries') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Battery Storage') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    hydrogen_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Hydrogen') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    dac_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'DAC') & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    wind_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Wind')) & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('wind')) & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()
    solar_CE_MISO_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Solar')) & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('solar')) & (resultsCE_NE2030['region'] == 'MISO'))]['Capacity (MW)'].sum()

    CoalCCS_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CCCCS_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CC_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    nuclear_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Nuclear') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    battery_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Batteries') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Battery Storage') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    hydrogen_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Hydrogen') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    dac_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'DAC') & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    wind_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Wind')) & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('wind')) & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()
    solar_CE_PJM_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Solar')) & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('solar')) & (resultsCE_NE2030['region'] == 'PJM'))]['Capacity (MW)'].sum()

    CoalCCS_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CCCCS_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CC_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    nuclear_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Nuclear') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    battery_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Batteries') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Battery Storage') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    hydrogen_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Hydrogen') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    dac_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'DAC') & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    wind_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Wind')) & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('wind')) & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()
    solar_CE_SPP_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Solar')) & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('solar')) & (resultsCE_NE2030['region'] == 'SPP'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    CCCCS_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    CC_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    nuclear_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Nuclear') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    battery_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Batteries') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Battery Storage') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    hydrogen_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Hydrogen') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    dac_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'DAC') & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    wind_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Wind')) & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('wind')) & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()
    solar_CE_NY_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Solar')) & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('solar')) & (resultsCE_NE2030['region'] == 'NY'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    CCCCS_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    CC_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Combined Cycle') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    nuclear_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Nuclear') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    battery_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Batteries') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Battery Storage') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    hydrogen_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'Hydrogen') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    dac_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'] == 'DAC') & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    wind_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Wind')) & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('wind')) & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()
    solar_CE_NE_NE2030 = resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('Solar')) & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2030.loc[((resultsCE_NE2030['PlantType'].str.contains('solar')) & (resultsCE_NE2030['region'] == 'NE'))]['Capacity (MW)'].sum()

    # NE 2040:
    CoalCCS_CE_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Coal Steam CCS')]['Capacity (MW)'].sum()
    CCCCS_CE_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Combined Cycle CCS')]['Capacity (MW)'].sum()
    CC_CE_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Combined Cycle')]['Capacity (MW)'].sum() - CCCCS_CE_NE2040
    nuclear_CE_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Nuclear')]['Capacity (MW)'].sum()
    wind_CE_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Wind')]['Capacity (MW)'].sum() \
                     + resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('wind')]['Capacity (MW)'].sum()
    solar_CE_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Solar')]['Capacity (MW)'].sum() \
                      + resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('solar')]['Capacity (MW)'].sum()
    battery_CE_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Battery Storage')]['Capacity (MW)'].sum() \
                        + resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'].str.contains('Batteries')]['Capacity (MW)'].sum()
    hydrogen_CE_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Hydrogen')]['Capacity (MW)'].sum()
    dac_CE_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('DAC')]['Capacity (MW)'].sum()

    CoalCCS_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CCCCS_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CC_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    nuclear_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Nuclear') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    battery_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Batteries') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Battery Storage') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    hydrogen_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Hydrogen') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    dac_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'DAC') & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    wind_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Wind')) & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('wind')) & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()
    solar_CE_SERC_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Solar')) & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('solar')) & (resultsCE_NE2040['region'] == 'SERC'))]['Capacity (MW)'].sum()

    CoalCCS_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CCCCS_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CC_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    nuclear_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Nuclear') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    battery_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Batteries') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Battery Storage') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    hydrogen_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Hydrogen') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    dac_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'DAC') & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    wind_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Wind')) & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('wind')) & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()
    solar_CE_MISO_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Solar')) & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('solar')) & (resultsCE_NE2040['region'] == 'MISO'))]['Capacity (MW)'].sum()

    CoalCCS_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CCCCS_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CC_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    nuclear_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Nuclear') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    battery_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Batteries') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Battery Storage') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    hydrogen_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Hydrogen') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    dac_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'DAC') & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    wind_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Wind')) & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('wind')) & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()
    solar_CE_PJM_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Solar')) & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('solar')) & (resultsCE_NE2040['region'] == 'PJM'))]['Capacity (MW)'].sum()

    CoalCCS_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CCCCS_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CC_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    nuclear_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Nuclear') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    battery_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Batteries') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Battery Storage') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    hydrogen_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Hydrogen') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    dac_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'DAC') & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    wind_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Wind')) & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('wind')) & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()
    solar_CE_SPP_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Solar')) & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('solar')) & (resultsCE_NE2040['region'] == 'SPP'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    CCCCS_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    CC_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    nuclear_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Nuclear') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    battery_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Batteries') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Battery Storage') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    hydrogen_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Hydrogen') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    dac_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'DAC') & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    wind_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Wind')) & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('wind')) & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()
    solar_CE_NY_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Solar')) & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('solar')) & (resultsCE_NE2040['region'] == 'NY'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    CCCCS_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    CC_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Combined Cycle') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    nuclear_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Nuclear') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    battery_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Batteries') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Battery Storage') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    hydrogen_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'Hydrogen') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    dac_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'] == 'DAC') & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    wind_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Wind')) & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('wind')) & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()
    solar_CE_NE_NE2040 = resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('Solar')) & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2040.loc[((resultsCE_NE2040['PlantType'].str.contains('solar')) & (resultsCE_NE2040['region'] == 'NE'))]['Capacity (MW)'].sum()

    # NE 2050:
    CoalCCS_CE_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Coal Steam CCS')]['Capacity (MW)'].sum()
    CCCCS_CE_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Combined Cycle CCS')]['Capacity (MW)'].sum()
    CC_CE_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Combined Cycle')]['Capacity (MW)'].sum() - CCCCS_CE_NE2050
    nuclear_CE_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Nuclear')]['Capacity (MW)'].sum()
    wind_CE_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Wind')]['Capacity (MW)'].sum() \
                     + resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('wind')]['Capacity (MW)'].sum()
    solar_CE_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Solar')]['Capacity (MW)'].sum() \
                      + resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('solar')]['Capacity (MW)'].sum()
    battery_CE_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Battery Storage')]['Capacity (MW)'].sum() \
                        + resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'].str.contains('Batteries')]['Capacity (MW)'].sum()
    hydrogen_CE_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Hydrogen')]['Capacity (MW)'].sum()
    dac_CE_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('DAC')]['Capacity (MW)'].sum()

    CoalCCS_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CCCCS_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    CC_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    nuclear_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Nuclear') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    battery_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Batteries') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Battery Storage') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    hydrogen_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Hydrogen') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    dac_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'DAC') & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    wind_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Wind')) & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('wind')) & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()
    solar_CE_SERC_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Solar')) & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('solar')) & (resultsCE_NE2050['region'] == 'SERC'))]['Capacity (MW)'].sum()

    CoalCCS_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CCCCS_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    CC_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    nuclear_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Nuclear') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    battery_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Batteries') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                             + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Battery Storage') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    hydrogen_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Hydrogen') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    dac_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'DAC') & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    wind_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Wind')) & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('wind')) & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()
    solar_CE_MISO_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Solar')) & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('solar')) & (resultsCE_NE2050['region'] == 'MISO'))]['Capacity (MW)'].sum()

    CoalCCS_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CCCCS_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    CC_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    nuclear_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Nuclear') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    battery_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Batteries') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Battery Storage') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    hydrogen_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Hydrogen') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    dac_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'DAC') & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    wind_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Wind')) & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('wind')) & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()
    solar_CE_PJM_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Solar')) & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('solar')) & (resultsCE_NE2050['region'] == 'PJM'))]['Capacity (MW)'].sum()

    CoalCCS_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CCCCS_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    CC_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    nuclear_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Nuclear') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    battery_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Batteries') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                            + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Battery Storage') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    hydrogen_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Hydrogen') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    dac_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'DAC') & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    wind_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Wind')) & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('wind')) & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()
    solar_CE_SPP_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Solar')) & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum() \
                          + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('solar')) & (resultsCE_NE2050['region'] == 'SPP'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    CCCCS_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    CC_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    nuclear_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Nuclear') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    battery_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Batteries') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Battery Storage') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    hydrogen_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Hydrogen') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    dac_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'DAC') & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    wind_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Wind')) & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('wind')) & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()
    solar_CE_NY_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Solar')) & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('solar')) & (resultsCE_NE2050['region'] == 'NY'))]['Capacity (MW)'].sum()

    CoalCCS_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Coal Steam CCS') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    CCCCS_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    CC_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Combined Cycle') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    nuclear_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Nuclear') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    battery_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Batteries') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum() \
                           + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Battery Storage') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    hydrogen_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'Hydrogen') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    dac_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'] == 'DAC') & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    wind_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Wind')) & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum() \
                        + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('wind')) & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()
    solar_CE_NE_NE2050 = resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('Solar')) & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum() \
                         + resultsCE_NE2050.loc[((resultsCE_NE2050['PlantType'].str.contains('solar')) & (resultsCE_NE2050['region'] == 'NE'))]['Capacity (MW)'].sum()

    CC_CE_all = np.around(np.divide([CC_CE_NZ, CC_CE_NE2050, CC_CE_NE2040,
                                        CC_CE_NE2030, CC_CE_NE2020], 1000), decimals=1)

    CCCCS_CE_all = np.around(np.divide([CCCCS_CE_NZ, CCCCS_CE_NE2050, CCCCS_CE_NE2040,
                                        CCCCS_CE_NE2030, CCCCS_CE_NE2020], 1000), decimals=1)

    nuclear_CE_all = np.around(np.divide([nuclear_CE_NZ, nuclear_CE_NE2050, nuclear_CE_NE2040,
                                            nuclear_CE_NE2030, nuclear_CE_NE2020], 1000), decimals=1)

    wind_CE_all = np.around(np.divide([wind_CE_NZ, wind_CE_NE2050, wind_CE_NE2040,
                                        wind_CE_NE2030, wind_CE_NE2020], 1000), decimals=1)

    solar_CE_all = np.around(np.divide([solar_CE_NZ, solar_CE_NE2050, solar_CE_NE2040,
                                        solar_CE_NE2030, solar_CE_NE2020], 1000), decimals=1)

    battery_CE_all = np.around(np.divide([battery_CE_NZ, battery_CE_NE2050, battery_CE_NE2040,
                                            battery_CE_NE2030, battery_CE_NE2020], 1000), decimals=1)

    hydrogen_CE_all = np.around(np.divide([hydrogen_CE_NZ, hydrogen_CE_NE2050, hydrogen_CE_NE2040,
                                            hydrogen_CE_NE2030, hydrogen_CE_NE2020], 1000), decimals=1)

    dac_CE_all = np.around(np.divide([dac_CE_NZ, dac_CE_NE2050, dac_CE_NE2040,
                                        dac_CE_NE2030, dac_CE_NE2020], 1000), decimals=1)

    # SERC:
    CC_CE_SERC = np.around(np.divide([CC_CE_SERC_NZ, CC_CE_SERC_NE2050, CC_CE_SERC_NE2040,
                                     CC_CE_SERC_NE2030, CC_CE_SERC_NE2020], 1000), decimals=1)

    CCCCS_CE_SERC = np.around(np.divide([CCCCS_CE_SERC_NZ, CCCCS_CE_SERC_NE2050, CCCCS_CE_SERC_NE2040,
                                        CCCCS_CE_SERC_NE2030, CCCCS_CE_SERC_NE2020], 1000), decimals=1)

    nuclear_CE_SERC = np.around(np.divide([nuclear_CE_SERC_NZ, nuclear_CE_SERC_NE2050, nuclear_CE_SERC_NE2040,
                                          nuclear_CE_SERC_NE2030, nuclear_CE_SERC_NE2020], 1000), decimals=1)

    wind_CE_SERC = np.around(np.divide([wind_CE_SERC_NZ, wind_CE_SERC_NE2050, wind_CE_SERC_NE2040,
                                       wind_CE_SERC_NE2030, wind_CE_SERC_NE2020], 1000), decimals=1)

    solar_CE_SERC = np.around(np.divide([solar_CE_SERC_NZ, solar_CE_SERC_NE2050, solar_CE_SERC_NE2040,
                                        solar_CE_SERC_NE2030, solar_CE_SERC_NE2020], 1000), decimals=1)

    battery_CE_SERC = np.around(np.divide([battery_CE_SERC_NZ, battery_CE_SERC_NE2050, battery_CE_SERC_NE2040,
                                          battery_CE_SERC_NE2030, battery_CE_SERC_NE2020], 1000), decimals=1)

    hydrogen_CE_SERC = np.around(np.divide([hydrogen_CE_SERC_NZ, hydrogen_CE_SERC_NE2050, hydrogen_CE_SERC_NE2040,
                                           hydrogen_CE_SERC_NE2030, hydrogen_CE_SERC_NE2020], 1000), decimals=1)

    dac_CE_SERC = np.around(np.divide([dac_CE_SERC_NZ, dac_CE_SERC_NE2050, dac_CE_SERC_NE2040,
                                      dac_CE_SERC_NE2030, dac_CE_SERC_NE2020], 1000), decimals=1)

    CC_CE_MISO = np.around(np.divide([CC_CE_MISO_NZ, CC_CE_MISO_NE2050, CC_CE_MISO_NE2040,
                                      CC_CE_MISO_NE2030, CC_CE_MISO_NE2020], 1000), decimals=1)

    # MISO:
    CCCCS_CE_MISO = np.around(np.divide([CCCCS_CE_MISO_NZ, CCCCS_CE_MISO_NE2050, CCCCS_CE_MISO_NE2040,
                                         CCCCS_CE_MISO_NE2030, CCCCS_CE_MISO_NE2020], 1000), decimals=1)

    nuclear_CE_MISO = np.around(np.divide([nuclear_CE_MISO_NZ, nuclear_CE_MISO_NE2050, nuclear_CE_MISO_NE2040,
                                           nuclear_CE_MISO_NE2030, nuclear_CE_MISO_NE2020], 1000), decimals=1)

    wind_CE_MISO = np.around(np.divide([wind_CE_MISO_NZ, wind_CE_MISO_NE2050, wind_CE_MISO_NE2040,
                                        wind_CE_MISO_NE2030, wind_CE_MISO_NE2020], 1000), decimals=1)

    solar_CE_MISO = np.around(np.divide([solar_CE_MISO_NZ, solar_CE_MISO_NE2050, solar_CE_MISO_NE2040,
                                         solar_CE_MISO_NE2030, solar_CE_MISO_NE2020], 1000), decimals=1)

    battery_CE_MISO = np.around(np.divide([battery_CE_MISO_NZ, battery_CE_MISO_NE2050, battery_CE_MISO_NE2040,
                                           battery_CE_MISO_NE2030, battery_CE_MISO_NE2020], 1000), decimals=1)

    hydrogen_CE_MISO = np.around(np.divide([hydrogen_CE_MISO_NZ, hydrogen_CE_MISO_NE2050, hydrogen_CE_MISO_NE2040,
                                            hydrogen_CE_MISO_NE2030, hydrogen_CE_MISO_NE2020], 1000), decimals=1)

    dac_CE_MISO = np.around(np.divide([dac_CE_MISO_NZ, dac_CE_MISO_NE2050, dac_CE_MISO_NE2040,
                                       dac_CE_MISO_NE2030, dac_CE_MISO_NE2020], 1000), decimals=1)

    # PJM:
    CC_CE_PJM = np.around(np.divide([CC_CE_PJM_NZ, CC_CE_PJM_NE2050, CC_CE_PJM_NE2040,
                                     CC_CE_PJM_NE2030, CC_CE_PJM_NE2020], 1000), decimals=1)

    CCCCS_CE_PJM = np.around(np.divide([CCCCS_CE_PJM_NZ, CCCCS_CE_PJM_NE2050, CCCCS_CE_PJM_NE2040,
                                        CCCCS_CE_PJM_NE2030, CCCCS_CE_PJM_NE2020], 1000), decimals=1)

    nuclear_CE_PJM = np.around(np.divide([nuclear_CE_PJM_NZ, nuclear_CE_PJM_NE2050, nuclear_CE_PJM_NE2040,
                                          nuclear_CE_PJM_NE2030, nuclear_CE_PJM_NE2020], 1000), decimals=1)

    wind_CE_PJM = np.around(np.divide([wind_CE_PJM_NZ, wind_CE_PJM_NE2050, wind_CE_PJM_NE2040,
                                       wind_CE_PJM_NE2030, wind_CE_PJM_NE2020], 1000), decimals=1)

    solar_CE_PJM = np.around(np.divide([solar_CE_PJM_NZ, solar_CE_PJM_NE2050, solar_CE_PJM_NE2040,
                                        solar_CE_PJM_NE2030, solar_CE_PJM_NE2020], 1000), decimals=1)

    battery_CE_PJM = np.around(np.divide([battery_CE_PJM_NZ, battery_CE_PJM_NE2050, battery_CE_PJM_NE2040,
                                          battery_CE_PJM_NE2030, battery_CE_PJM_NE2020], 1000), decimals=1)

    hydrogen_CE_PJM = np.around(np.divide([hydrogen_CE_PJM_NZ, hydrogen_CE_PJM_NE2050, hydrogen_CE_PJM_NE2040,
                                           hydrogen_CE_PJM_NE2030, hydrogen_CE_PJM_NE2020], 1000), decimals=1)

    dac_CE_PJM = np.around(np.divide([dac_CE_PJM_NZ, dac_CE_PJM_NE2050, dac_CE_PJM_NE2040,
                                      dac_CE_PJM_NE2030, dac_CE_PJM_NE2020], 1000), decimals=1)

    # SPP:
    CC_CE_SPP = np.around(np.divide([CC_CE_SPP_NZ, CC_CE_SPP_NE2050, CC_CE_SPP_NE2040,
                                     CC_CE_SPP_NE2030, CC_CE_SPP_NE2020], 1000), decimals=1)

    CCCCS_CE_SPP = np.around(np.divide([CCCCS_CE_SPP_NZ, CCCCS_CE_SPP_NE2050, CCCCS_CE_SPP_NE2040,
                                        CCCCS_CE_SPP_NE2030, CCCCS_CE_SPP_NE2020], 1000), decimals=1)

    nuclear_CE_SPP = np.around(np.divide([nuclear_CE_SPP_NZ, nuclear_CE_SPP_NE2050, nuclear_CE_SPP_NE2040,
                                          nuclear_CE_SPP_NE2030, nuclear_CE_SPP_NE2020], 1000), decimals=1)

    wind_CE_SPP = np.around(np.divide([wind_CE_SPP_NZ, wind_CE_SPP_NE2050, wind_CE_SPP_NE2040,
                                       wind_CE_SPP_NE2030, wind_CE_SPP_NE2020], 1000), decimals=1)

    solar_CE_SPP = np.around(np.divide([solar_CE_SPP_NZ, solar_CE_SPP_NE2050, solar_CE_SPP_NE2040,
                                        solar_CE_SPP_NE2030, solar_CE_SPP_NE2020], 1000), decimals=1)

    battery_CE_SPP = np.around(np.divide([battery_CE_SPP_NZ, battery_CE_SPP_NE2050, battery_CE_SPP_NE2040,
                                          battery_CE_SPP_NE2030, battery_CE_SPP_NE2020], 1000), decimals=1)

    hydrogen_CE_SPP = np.around(np.divide([hydrogen_CE_SPP_NZ, hydrogen_CE_SPP_NE2050, hydrogen_CE_SPP_NE2040,
                                           hydrogen_CE_SPP_NE2030, hydrogen_CE_SPP_NE2020], 1000), decimals=1)

    dac_CE_SPP = np.around(np.divide([dac_CE_SPP_NZ, dac_CE_SPP_NE2050, dac_CE_SPP_NE2040,
                                      dac_CE_SPP_NE2030, dac_CE_SPP_NE2020], 1000), decimals=1)

    # NY:
    CC_CE_NY = np.around(np.divide([CC_CE_NY_NZ, CC_CE_NY_NE2050, CC_CE_NY_NE2040,
                                    CC_CE_NY_NE2030, CC_CE_NY_NE2020], 1000), decimals=1)

    CCCCS_CE_NY = np.around(np.divide([CCCCS_CE_NY_NZ, CCCCS_CE_NY_NE2050, CCCCS_CE_NY_NE2040,
                                       CCCCS_CE_NY_NE2030, CCCCS_CE_NY_NE2020], 1000), decimals=1)

    nuclear_CE_NY = np.around(np.divide([nuclear_CE_NY_NZ, nuclear_CE_NY_NE2050, nuclear_CE_NY_NE2040,
                                         nuclear_CE_NY_NE2030, nuclear_CE_NY_NE2020], 1000), decimals=1)

    wind_CE_NY = np.around(np.divide([wind_CE_NY_NZ, wind_CE_NY_NE2050, wind_CE_NY_NE2040,
                                      wind_CE_NY_NE2030, wind_CE_NY_NE2020], 1000), decimals=1)

    solar_CE_NY = np.around(np.divide([solar_CE_NY_NZ, solar_CE_NY_NE2050, solar_CE_NY_NE2040,
                                       solar_CE_NY_NE2030, solar_CE_NY_NE2020], 1000), decimals=1)

    battery_CE_NY = np.around(np.divide([battery_CE_NY_NZ, battery_CE_NY_NE2050, battery_CE_NY_NE2040,
                                         battery_CE_NY_NE2030, battery_CE_NY_NE2020], 1000), decimals=1)

    hydrogen_CE_NY = np.around(np.divide([hydrogen_CE_NY_NZ, hydrogen_CE_NY_NE2050, hydrogen_CE_NY_NE2040,
                                          hydrogen_CE_NY_NE2030, hydrogen_CE_NY_NE2020], 1000), decimals=1)

    dac_CE_NY = np.around(np.divide([dac_CE_NY_NZ, dac_CE_NY_NE2050, dac_CE_NY_NE2040,
                                     dac_CE_NY_NE2030, dac_CE_NY_NE2020], 1000), decimals=1)

    # NE:
    CC_CE_NE = np.around(np.divide([CC_CE_NE_NZ, CC_CE_NE_NE2050, CC_CE_NE_NE2040,
                                    CC_CE_NE_NE2030, CC_CE_NE_NE2020], 1000), decimals=1)

    CCCCS_CE_NE = np.around(np.divide([CCCCS_CE_NE_NZ, CCCCS_CE_NE_NE2050, CCCCS_CE_NE_NE2040,
                                       CCCCS_CE_NE_NE2030, CCCCS_CE_NE_NE2020], 1000), decimals=1)

    nuclear_CE_NE = np.around(np.divide([nuclear_CE_NE_NZ, nuclear_CE_NE_NE2050, nuclear_CE_NE_NE2040,
                                         nuclear_CE_NE_NE2030, nuclear_CE_NE_NE2020], 1000), decimals=1)

    wind_CE_NE = np.around(np.divide([wind_CE_NE_NZ, wind_CE_NE_NE2050, wind_CE_NE_NE2040,
                                      wind_CE_NE_NE2030, wind_CE_NE_NE2020], 1000), decimals=1)

    solar_CE_NE = np.around(np.divide([solar_CE_NE_NZ, solar_CE_NE_NE2050, solar_CE_NE_NE2040,
                                       solar_CE_NE_NE2030, solar_CE_NE_NE2020], 1000), decimals=1)

    battery_CE_NE = np.around(np.divide([battery_CE_NE_NZ, battery_CE_NE_NE2050, battery_CE_NE_NE2040,
                                         battery_CE_NE_NE2030, battery_CE_NE_NE2020], 1000), decimals=1)

    hydrogen_CE_NE = np.around(np.divide([hydrogen_CE_NE_NZ, hydrogen_CE_NE_NE2050, hydrogen_CE_NE_NE2040,
                                          hydrogen_CE_NE_NE2030, hydrogen_CE_NE_NE2020], 1000), decimals=1)

    dac_CE_NE = np.around(np.divide([dac_CE_NE_NZ, dac_CE_NE_NE2050, dac_CE_NE_NE2040,
                                     dac_CE_NE_NE2030, dac_CE_NE_NE2020], 1000), decimals=1)

    return (CC_CE_all, CCCCS_CE_all, nuclear_CE_all, wind_CE_all, solar_CE_all, battery_CE_all, hydrogen_CE_all, dac_CE_all,
            CC_CE_SERC, CCCCS_CE_SERC, nuclear_CE_SERC, wind_CE_SERC, solar_CE_SERC, battery_CE_SERC, hydrogen_CE_SERC, dac_CE_SERC,
            CC_CE_MISO, CCCCS_CE_MISO, nuclear_CE_MISO, wind_CE_MISO, solar_CE_MISO, battery_CE_MISO, hydrogen_CE_MISO, dac_CE_MISO,
            CC_CE_PJM, CCCCS_CE_PJM, nuclear_CE_PJM, wind_CE_PJM, solar_CE_PJM, battery_CE_PJM, hydrogen_CE_PJM, dac_CE_PJM,
            CC_CE_SPP, CCCCS_CE_SPP, nuclear_CE_SPP, wind_CE_SPP, solar_CE_SPP, battery_CE_SPP, hydrogen_CE_SPP, dac_CE_SPP,
            CC_CE_NY, CCCCS_CE_NY, nuclear_CE_NY, wind_CE_NY, solar_CE_NY, battery_CE_NY, hydrogen_CE_NY, dac_CE_NY,
            CC_CE_NE, CCCCS_CE_NE, nuclear_CE_NE, wind_CE_NE, solar_CE_NE, battery_CE_NE, hydrogen_CE_NE, dac_CE_NE)
