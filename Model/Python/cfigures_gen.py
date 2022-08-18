import pandas as pd
import numpy as np

def gen_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2):
    # read in gen solution:
    resultsGenE_NZ = pd.read_csv(m_dir2 + resultsDir_other_NZ + 'vGenCE2050.csv')
    resultsGenE_NE2020 = pd.read_csv(m_dir2 + resultsDir_other_NE2020 + 'vGenCE2050.csv')
    resultsGenE_NE2030 = pd.read_csv(m_dir2 + resultsDir_other_NE2030 + 'vGenCE2050.csv')
    resultsGenE_NE2040 = pd.read_csv(m_dir2 + resultsDir_other_NE2040 + 'vGenCE2050.csv')
    resultsGenE_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'vGenCE2060.csv')

    resultsLoad_NZ = pd.read_csv(m_dir2 + resultsDir_other_NZ + 'demandCE2050.csv')
    resultsLoad_NE2020 = pd.read_csv(m_dir2 + resultsDir_other_NE2020 + 'demandCE2050.csv')
    resultsLoad_NE2030 = pd.read_csv(m_dir2 + resultsDir_other_NE2030 + 'demandCE2050.csv')
    resultsLoad_NE2040 = pd.read_csv(m_dir2 + resultsDir_other_NE2040 + 'demandCE2050.csv')
    resultsLoad_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'demandCE2060.csv')

    resultsGenE_NZ.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenE_NZ = resultsGenE_NZ.T
    resultsGenE_NZ.columns = resultsGenE_NZ.iloc[0]
    resultsGenE_NZ = resultsGenE_NZ.drop(resultsGenE_NZ.index[0])
    resultsGenE_NZ = resultsGenE_NZ.reset_index()
    resultsGenE_NZ.rename(columns={'index': 'Unit'}, inplace=True)

    resultsGenE_NE2020.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenE_NE2020 = resultsGenE_NE2020.T
    resultsGenE_NE2020.columns = resultsGenE_NE2020.iloc[0]
    resultsGenE_NE2020 = resultsGenE_NE2020.drop(resultsGenE_NE2020.index[0])
    resultsGenE_NE2020 = resultsGenE_NE2020.reset_index()
    resultsGenE_NE2020.rename(columns={'index': 'Unit'}, inplace=True)

    resultsGenE_NE2030.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenE_NE2030 = resultsGenE_NE2030.T
    resultsGenE_NE2030.columns = resultsGenE_NE2030.iloc[0]
    resultsGenE_NE2030 = resultsGenE_NE2030.drop(resultsGenE_NE2030.index[0])
    resultsGenE_NE2030 = resultsGenE_NE2030.reset_index()
    resultsGenE_NE2030.rename(columns={'index': 'Unit'}, inplace=True)

    resultsGenE_NE2040.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenE_NE2040 = resultsGenE_NE2040.T
    resultsGenE_NE2040.columns = resultsGenE_NE2040.iloc[0]
    resultsGenE_NE2040 = resultsGenE_NE2040.drop(resultsGenE_NE2040.index[0])
    resultsGenE_NE2040 = resultsGenE_NE2040.reset_index()
    resultsGenE_NE2040.rename(columns={'index': 'Unit'}, inplace=True)

    resultsGenE_NE2050.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenE_NE2050 = resultsGenE_NE2050.T
    resultsGenE_NE2050.columns = resultsGenE_NE2050.iloc[0]
    resultsGenE_NE2050 = resultsGenE_NE2050.drop(resultsGenE_NE2050.index[0])
    resultsGenE_NE2050 = resultsGenE_NE2050.reset_index()
    resultsGenE_NE2050.rename(columns={'index': 'Unit'}, inplace=True)

    # read in plant type for existing generation:
    planttypeE_NZ = pd.read_csv(m_dir2 + resultsDir_other_NZ + 'genFleetForCE2050.csv')
    planttypeE_NZ = planttypeE_NZ[['PlantType', 'region']]
    resultsGenE_NZ['Total Gen'] = resultsGenE_NZ.iloc[:, 1:].sum(axis=1)
    resultsGenE_NZ = resultsGenE_NZ[['Total Gen']]
    resultsGenE_NZ['PlantType'] = planttypeE_NZ['PlantType']
    resultsGenE_NZ['region'] = planttypeE_NZ['region']

    planttypeE_NE2020 = pd.read_csv(m_dir2 + resultsDir_other_NE2020 + 'genFleetForCE2050.csv')
    planttypeE_NE2020 = planttypeE_NE2020[['PlantType', 'region']]
    resultsGenE_NE2020['Total Gen'] = resultsGenE_NE2020.iloc[:, 1:].sum(axis=1)
    resultsGenE_NE2020 = resultsGenE_NE2020[['Total Gen']]
    resultsGenE_NE2020['PlantType'] = planttypeE_NE2020['PlantType']
    resultsGenE_NE2020['region'] = planttypeE_NE2020['region']

    planttypeE_NE2030 = pd.read_csv(m_dir2 + resultsDir_other_NE2030 + 'genFleetForCE2050.csv')
    planttypeE_NE2030 = planttypeE_NE2030[['PlantType', 'region']]
    resultsGenE_NE2030['Total Gen'] = resultsGenE_NE2030.iloc[:, 1:].sum(axis=1)
    resultsGenE_NE2030 = resultsGenE_NE2030[['Total Gen']]
    resultsGenE_NE2030['PlantType'] = planttypeE_NE2030['PlantType']
    resultsGenE_NE2030['region'] = planttypeE_NE2030['region']

    planttypeE_NE2040 = pd.read_csv(m_dir2 + resultsDir_other_NE2040 + 'genFleetForCE2050.csv')
    planttypeE_NE2040 = planttypeE_NE2040[['PlantType', 'region']]
    resultsGenE_NE2040['Total Gen'] = resultsGenE_NE2040.iloc[:, 1:].sum(axis=1)
    resultsGenE_NE2040 = resultsGenE_NE2040[['Total Gen']]
    resultsGenE_NE2040['PlantType'] = planttypeE_NE2040['PlantType']
    resultsGenE_NE2040['region'] = planttypeE_NE2040['region']

    planttypeE_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'genFleetForCE2060.csv')
    planttypeE_NE2050 = planttypeE_NE2050[['PlantType', 'region']]
    resultsGenE_NE2050['Total Gen'] = resultsGenE_NE2050.iloc[:, 1:].sum(axis=1)
    resultsGenE_NE2050 = resultsGenE_NE2050[['Total Gen']]
    resultsGenE_NE2050['PlantType'] = planttypeE_NE2050['PlantType']
    resultsGenE_NE2050['region'] = planttypeE_NE2050['region']

    Coal_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Coal Steam']
    CC_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Combined Cycle CCS']
    CT_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Combustion Turbine']
    OG_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'O/G Steam']
    bio_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Biomass']
    battery_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Hydrogen']
    nuclear_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Nuclear']
    dac_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'DAC']
    solarN_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('solar')]
    solarE_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Solar PV']
    windN_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('wind')]
    windE_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Onshore Wind']
    pump_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Pumped Storage']
    Other1_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Flywheels')]
    Other2_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Fossil Waste')]
    Other3_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Fuel Cell')]
    Other4_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('IGCC')]
    Other5_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Landfill Gas')]
    Other6_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Tires')]

    Coal_GenE_NZ_SERC = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'SERC']
    Coal_GenE_NZ_MISO = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'MISO']
    Coal_GenE_NZ_NE = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'NE']
    Coal_GenE_NZ_NY = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'NY']
    Coal_GenE_NZ_PJM = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'PJM']
    Coal_GenE_NZ_SPP = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'SPP']
    CC_GenE_NZ_SERC = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'SERC']
    CC_GenE_NZ_MISO = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'MISO']
    CC_GenE_NZ_NE = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'NE']
    CC_GenE_NZ_NY = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'NY']
    CC_GenE_NZ_PJM = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'PJM']
    CC_GenE_NZ_SPP = Coal_GenE_NZ.loc[Coal_GenE_NZ['region'] == 'SPP']
    CCCCS_GenE_NZ_SERC = CCCCS_GenE_NZ.loc[CCCCS_GenE_NZ['region'] == 'SERC']
    CCCCS_GenE_NZ_MISO = CCCCS_GenE_NZ.loc[CCCCS_GenE_NZ['region'] == 'MISO']
    CCCCS_GenE_NZ_NE = CCCCS_GenE_NZ.loc[CCCCS_GenE_NZ['region'] == 'NE']
    CCCCS_GenE_NZ_NY = CCCCS_GenE_NZ.loc[CCCCS_GenE_NZ['region'] == 'NY']
    CCCCS_GenE_NZ_PJM = CCCCS_GenE_NZ.loc[CCCCS_GenE_NZ['region'] == 'PJM']
    CCCCS_GenE_NZ_SPP = CCCCS_GenE_NZ.loc[CCCCS_GenE_NZ['region'] == 'SPP']
    CT_GenE_NZ_SERC = CT_GenE_NZ.loc[CT_GenE_NZ['region'] == 'SERC']
    CT_GenE_NZ_MISO = CT_GenE_NZ.loc[CT_GenE_NZ['region'] == 'MISO']
    CT_GenE_NZ_NE = CT_GenE_NZ.loc[CT_GenE_NZ['region'] == 'NE']
    CT_GenE_NZ_NY = CT_GenE_NZ.loc[CT_GenE_NZ['region'] == 'NY']
    CT_GenE_NZ_PJM = CT_GenE_NZ.loc[CT_GenE_NZ['region'] == 'PJM']
    CT_GenE_NZ_SPP = CT_GenE_NZ.loc[CT_GenE_NZ['region'] == 'SPP']
    OG_GenE_NZ_SERC = OG_GenE_NZ.loc[OG_GenE_NZ['region'] == 'SERC']
    OG_GenE_NZ_MISO = OG_GenE_NZ.loc[OG_GenE_NZ['region'] == 'MISO']
    OG_GenE_NZ_NE = OG_GenE_NZ.loc[OG_GenE_NZ['region'] == 'NE']
    OG_GenE_NZ_NY = OG_GenE_NZ.loc[OG_GenE_NZ['region'] == 'NY']
    OG_GenE_NZ_PJM = OG_GenE_NZ.loc[OG_GenE_NZ['region'] == 'PJM']
    OG_GenE_NZ_SPP = OG_GenE_NZ.loc[OG_GenE_NZ['region'] == 'SPP']
    bio_GenE_NZ_SERC = bio_GenE_NZ.loc[bio_GenE_NZ['region'] == 'SERC']
    bio_GenE_NZ_MISO = bio_GenE_NZ.loc[bio_GenE_NZ['region'] == 'MISO']
    bio_GenE_NZ_NE = bio_GenE_NZ.loc[bio_GenE_NZ['region'] == 'NE']
    bio_GenE_NZ_NY = bio_GenE_NZ.loc[bio_GenE_NZ['region'] == 'NY']
    bio_GenE_NZ_PJM = bio_GenE_NZ.loc[bio_GenE_NZ['region'] == 'PJM']
    bio_GenE_NZ_SPP = bio_GenE_NZ.loc[bio_GenE_NZ['region'] == 'SPP']
    battery_GenE_NZ_SERC = battery_GenE_NZ.loc[battery_GenE_NZ['region'] == 'SERC']
    battery_GenE_NZ_MISO = battery_GenE_NZ.loc[battery_GenE_NZ['region'] == 'MISO']
    battery_GenE_NZ_NE = battery_GenE_NZ.loc[battery_GenE_NZ['region'] == 'NE']
    battery_GenE_NZ_NY = battery_GenE_NZ.loc[battery_GenE_NZ['region'] == 'NY']
    battery_GenE_NZ_PJM = battery_GenE_NZ.loc[battery_GenE_NZ['region'] == 'PJM']
    battery_GenE_NZ_SPP = battery_GenE_NZ.loc[battery_GenE_NZ['region'] == 'SPP']
    hydrogen_GenE_NZ_SERC = hydrogen_GenE_NZ.loc[hydrogen_GenE_NZ['region'] == 'SERC']
    hydrogen_GenE_NZ_MISO = hydrogen_GenE_NZ.loc[hydrogen_GenE_NZ['region'] == 'MISO']
    hydrogen_GenE_NZ_NE = hydrogen_GenE_NZ.loc[hydrogen_GenE_NZ['region'] == 'NE']
    hydrogen_GenE_NZ_NY = hydrogen_GenE_NZ.loc[hydrogen_GenE_NZ['region'] == 'NY']
    hydrogen_GenE_NZ_PJM = hydrogen_GenE_NZ.loc[hydrogen_GenE_NZ['region'] == 'PJM']
    hydrogen_GenE_NZ_SPP = hydrogen_GenE_NZ.loc[hydrogen_GenE_NZ['region'] == 'SPP']
    nuclear_GenE_NZ_SERC = nuclear_GenE_NZ.loc[nuclear_GenE_NZ['region'] == 'SERC']
    nuclear_GenE_NZ_MISO = nuclear_GenE_NZ.loc[nuclear_GenE_NZ['region'] == 'MISO']
    nuclear_GenE_NZ_NE = nuclear_GenE_NZ.loc[nuclear_GenE_NZ['region'] == 'NE']
    nuclear_GenE_NZ_NY = nuclear_GenE_NZ.loc[nuclear_GenE_NZ['region'] == 'NY']
    nuclear_GenE_NZ_PJM = nuclear_GenE_NZ.loc[nuclear_GenE_NZ['region'] == 'PJM']
    nuclear_GenE_NZ_SPP = nuclear_GenE_NZ.loc[nuclear_GenE_NZ['region'] == 'SPP']
    dac_GenE_NZ_SERC = dac_GenE_NZ.loc[dac_GenE_NZ['region'] == 'SERC']
    dac_GenE_NZ_MISO = dac_GenE_NZ.loc[dac_GenE_NZ['region'] == 'MISO']
    dac_GenE_NZ_NE = dac_GenE_NZ.loc[dac_GenE_NZ['region'] == 'NE']
    dac_GenE_NZ_NY = dac_GenE_NZ.loc[dac_GenE_NZ['region'] == 'NY']
    dac_GenE_NZ_PJM = dac_GenE_NZ.loc[dac_GenE_NZ['region'] == 'PJM']
    dac_GenE_NZ_SPP = dac_GenE_NZ.loc[dac_GenE_NZ['region'] == 'SPP']
    solarN_GenE_NZ_SERC = solarN_GenE_NZ.loc[solarN_GenE_NZ['region'] == 'SERC']
    solarN_GenE_NZ_MISO = solarN_GenE_NZ.loc[solarN_GenE_NZ['region'] == 'MISO']
    solarN_GenE_NZ_NE = solarN_GenE_NZ.loc[solarN_GenE_NZ['region'] == 'NE']
    solarN_GenE_NZ_NY = solarN_GenE_NZ.loc[solarN_GenE_NZ['region'] == 'NY']
    solarN_GenE_NZ_PJM = solarN_GenE_NZ.loc[solarN_GenE_NZ['region'] == 'PJM']
    solarN_GenE_NZ_SPP = solarN_GenE_NZ.loc[solarN_GenE_NZ['region'] == 'SPP']
    solarE_GenE_NZ_SERC = solarE_GenE_NZ.loc[solarE_GenE_NZ['region'] == 'SERC']
    solarE_GenE_NZ_MISO = solarE_GenE_NZ.loc[solarE_GenE_NZ['region'] == 'MISO']
    solarE_GenE_NZ_NE = solarE_GenE_NZ.loc[solarE_GenE_NZ['region'] == 'NE']
    solarE_GenE_NZ_NY = solarE_GenE_NZ.loc[solarE_GenE_NZ['region'] == 'NY']
    solarE_GenE_NZ_PJM = solarE_GenE_NZ.loc[solarE_GenE_NZ['region'] == 'PJM']
    solarE_GenE_NZ_SPP = solarE_GenE_NZ.loc[solarE_GenE_NZ['region'] == 'SPP']
    windN_GenE_NZ_SERC = windN_GenE_NZ.loc[windN_GenE_NZ['region'] == 'SERC']
    windN_GenE_NZ_MISO = windN_GenE_NZ.loc[windN_GenE_NZ['region'] == 'MISO']
    windN_GenE_NZ_NE = windN_GenE_NZ.loc[windN_GenE_NZ['region'] == 'NE']
    windN_GenE_NZ_NY = windN_GenE_NZ.loc[windN_GenE_NZ['region'] == 'NY']
    windN_GenE_NZ_PJM = windN_GenE_NZ.loc[windN_GenE_NZ['region'] == 'PJM']
    windN_GenE_NZ_SPP = windN_GenE_NZ.loc[windN_GenE_NZ['region'] == 'SPP']
    windE_GenE_NZ_SERC = windE_GenE_NZ.loc[windE_GenE_NZ['region'] == 'SERC']
    windE_GenE_NZ_MISO = windE_GenE_NZ.loc[windE_GenE_NZ['region'] == 'MISO']
    windE_GenE_NZ_NE = windE_GenE_NZ.loc[windE_GenE_NZ['region'] == 'NE']
    windE_GenE_NZ_NY = windE_GenE_NZ.loc[windE_GenE_NZ['region'] == 'NY']
    windE_GenE_NZ_PJM = windE_GenE_NZ.loc[windE_GenE_NZ['region'] == 'PJM']
    windE_GenE_NZ_SPP = windE_GenE_NZ.loc[windE_GenE_NZ['region'] == 'SPP']
    pump_GenE_NZ_SERC = pump_GenE_NZ.loc[pump_GenE_NZ['region'] == 'SERC']
    pump_GenE_NZ_MISO = pump_GenE_NZ.loc[pump_GenE_NZ['region'] == 'MISO']
    pump_GenE_NZ_NE = pump_GenE_NZ.loc[pump_GenE_NZ['region'] == 'NE']
    pump_GenE_NZ_NY = pump_GenE_NZ.loc[pump_GenE_NZ['region'] == 'NY']
    pump_GenE_NZ_PJM = pump_GenE_NZ.loc[pump_GenE_NZ['region'] == 'PJM']
    pump_GenE_NZ_SPP = pump_GenE_NZ.loc[pump_GenE_NZ['region'] == 'SPP']
    Other1_GenE_NZ_SERC = Other1_GenE_NZ.loc[Other1_GenE_NZ['region'] == 'SERC']
    Other1_GenE_NZ_MISO = Other1_GenE_NZ.loc[Other1_GenE_NZ['region'] == 'MISO']
    Other1_GenE_NZ_NE = Other1_GenE_NZ.loc[Other1_GenE_NZ['region'] == 'NE']
    Other1_GenE_NZ_NY = Other1_GenE_NZ.loc[Other1_GenE_NZ['region'] == 'NY']
    Other1_GenE_NZ_PJM = Other1_GenE_NZ.loc[Other1_GenE_NZ['region'] == 'PJM']
    Other1_GenE_NZ_SPP = Other1_GenE_NZ.loc[Other1_GenE_NZ['region'] == 'SPP']
    Other2_GenE_NZ_SERC = Other2_GenE_NZ.loc[Other2_GenE_NZ['region'] == 'SERC']
    Other2_GenE_NZ_MISO = Other2_GenE_NZ.loc[Other2_GenE_NZ['region'] == 'MISO']
    Other2_GenE_NZ_NE = Other2_GenE_NZ.loc[Other2_GenE_NZ['region'] == 'NE']
    Other2_GenE_NZ_NY = Other2_GenE_NZ.loc[Other2_GenE_NZ['region'] == 'NY']
    Other2_GenE_NZ_PJM = Other2_GenE_NZ.loc[Other2_GenE_NZ['region'] == 'PJM']
    Other2_GenE_NZ_SPP = Other2_GenE_NZ.loc[Other2_GenE_NZ['region'] == 'SPP']
    Other3_GenE_NZ_SERC = Other3_GenE_NZ.loc[Other3_GenE_NZ['region'] == 'SERC']
    Other3_GenE_NZ_MISO = Other3_GenE_NZ.loc[Other3_GenE_NZ['region'] == 'MISO']
    Other3_GenE_NZ_NE = Other3_GenE_NZ.loc[Other3_GenE_NZ['region'] == 'NE']
    Other3_GenE_NZ_NY = Other3_GenE_NZ.loc[Other3_GenE_NZ['region'] == 'NY']
    Other3_GenE_NZ_PJM = Other3_GenE_NZ.loc[Other3_GenE_NZ['region'] == 'PJM']
    Other3_GenE_NZ_SPP = Other3_GenE_NZ.loc[Other3_GenE_NZ['region'] == 'SPP']
    Other4_GenE_NZ_SERC = Other4_GenE_NZ.loc[Other4_GenE_NZ['region'] == 'SERC']
    Other4_GenE_NZ_MISO = Other4_GenE_NZ.loc[Other4_GenE_NZ['region'] == 'MISO']
    Other4_GenE_NZ_NE = Other4_GenE_NZ.loc[Other4_GenE_NZ['region'] == 'NE']
    Other4_GenE_NZ_NY = Other4_GenE_NZ.loc[Other4_GenE_NZ['region'] == 'NY']
    Other4_GenE_NZ_PJM = Other4_GenE_NZ.loc[Other4_GenE_NZ['region'] == 'PJM']
    Other4_GenE_NZ_SPP = Other4_GenE_NZ.loc[Other4_GenE_NZ['region'] == 'SPP']
    Other5_GenE_NZ_SERC = Other5_GenE_NZ.loc[Other5_GenE_NZ['region'] == 'SERC']
    Other5_GenE_NZ_MISO = Other5_GenE_NZ.loc[Other5_GenE_NZ['region'] == 'MISO']
    Other5_GenE_NZ_NE = Other5_GenE_NZ.loc[Other5_GenE_NZ['region'] == 'NE']
    Other5_GenE_NZ_NY = Other5_GenE_NZ.loc[Other5_GenE_NZ['region'] == 'NY']
    Other5_GenE_NZ_PJM = Other5_GenE_NZ.loc[Other5_GenE_NZ['region'] == 'PJM']
    Other5_GenE_NZ_SPP = Other5_GenE_NZ.loc[Other5_GenE_NZ['region'] == 'SPP']
    Other6_GenE_NZ_SERC = Other6_GenE_NZ.loc[Other6_GenE_NZ['region'] == 'SERC']
    Other6_GenE_NZ_MISO = Other6_GenE_NZ.loc[Other6_GenE_NZ['region'] == 'MISO']
    Other6_GenE_NZ_NE = Other6_GenE_NZ.loc[Other6_GenE_NZ['region'] == 'NE']
    Other6_GenE_NZ_NY = Other6_GenE_NZ.loc[Other6_GenE_NZ['region'] == 'NY']
    Other6_GenE_NZ_PJM = Other6_GenE_NZ.loc[Other6_GenE_NZ['region'] == 'PJM']
    Other6_GenE_NZ_SPP = Other6_GenE_NZ.loc[Other6_GenE_NZ['region'] == 'SPP']
    Other7_GenE_NZ_SERC = Other7_GenE_NZ.loc[Other7_GenE_NZ['region'] == 'SERC']
    Other7_GenE_NZ_MISO = Other7_GenE_NZ.loc[Other7_GenE_NZ['region'] == 'MISO']
    Other7_GenE_NZ_NE = Other7_GenE_NZ.loc[Other7_GenE_NZ['region'] == 'NE']
    Other7_GenE_NZ_NY = Other7_GenE_NZ.loc[Other7_GenE_NZ['region'] == 'NY']
    Other7_GenE_NZ_PJM = Other7_GenE_NZ.loc[Other7_GenE_NZ['region'] == 'PJM']
    Other7_GenE_NZ_SPP = Other7_GenE_NZ.loc[Other7_GenE_NZ['region'] == 'SPP']
    Other8_GenE_NZ_SERC = Other8_GenE_NZ.loc[Other8_GenE_NZ['region'] == 'SERC']
    Other8_GenE_NZ_MISO = Other8_GenE_NZ.loc[Other8_GenE_NZ['region'] == 'MISO']
    Other8_GenE_NZ_NE = Other8_GenE_NZ.loc[Other8_GenE_NZ['region'] == 'NE']
    Other8_GenE_NZ_NY = Other8_GenE_NZ.loc[Other8_GenE_NZ['region'] == 'NY']
    Other8_GenE_NZ_PJM = Other8_GenE_NZ.loc[Other8_GenE_NZ['region'] == 'PJM']
    Other8_GenE_NZ_SPP = Other8_GenE_NZ.loc[Other8_GenE_NZ['region'] == 'SPP']

    Coal_GenE_NZ = Coal_GenE_NZ['Total Gen'].sum()
    CCCCS_GenE_NZ = CCCCS_GenE_NZ['Total Gen'].sum()
    CC_GenE_NZ = CC_GenE_NZ['Total Gen'].sum()
    CT_GenE_NZ = CT_GenE_NZ['Total Gen'].sum()
    OG_GenE_NZ = OG_GenE_NZ['Total Gen'].sum()
    bio_GenE_NZ = bio_GenE_NZ['Total Gen'].sum()
    battery_GenE_NZ = battery_GenE_NZ['Total Gen'].sum()
    hydrogen_GenE_NZ = hydrogen_GenE_NZ['Total Gen'].sum()
    nuclear_GenE_NZ = nuclear_GenE_NZ['Total Gen'].sum()
    pump_GenE_NZ = pump_GenE_NZ['Total Gen'].sum()
    solar_GenE_NZ = solarN_GenE_NZ['Total Gen'].sum() + solarE_GenE_NZ['Total Gen'].sum()
    wind_GenE_NZ = windN_GenE_NZ['Total Gen'].sum() + windE_GenE_NZ['Total Gen'].sum()
    dac_GenE_NZ = dac_GenE_NZ['Total Gen'].sum()
    Others_GenE_NZ = Other1_GenE_NZ['Total Gen'].sum() + Other2_GenE_NZ['Total Gen'].sum() \
                     + Other3_GenE_NZ['Total Gen'].sum() + Other4_GenE_NZ['Total Gen'].sum() \
                     + Other5_GenE_NZ['Total Gen'].sum() + Other6_GenE_NZ['Total Gen'].sum() \
                     + Other7_GenE_NZ['Total Gen'].sum() + Other8_GenE_NZ['Total Gen'].sum()

    Coal_GenE_NZ_SERC = Coal_GenE_NZ_SERC['Total Gen'].sum()
    CCCCS_GenE_NZ_SERC = CCCCS_GenE_NZ_SERC['Total Gen'].sum()
    CC_GenE_NZ_SERC = CC_GenE_NZ_SERC['Total Gen'].sum()
    CT_GenE_NZ_SERC = CT_GenE_NZ_SERC['Total Gen'].sum()
    OG_GenE_NZ_SERC = OG_GenE_NZ_SERC['Total Gen'].sum()
    bio_GenE_NZ_SERC = bio_GenE_NZ_SERC['Total Gen'].sum()
    battery_GenE_NZ_SERC = battery_GenE_NZ_SERC['Total Gen'].sum()
    hydrogen_GenE_NZ_SERC = hydrogen_GenE_NZ_SERC['Total Gen'].sum()
    nuclear_GenE_NZ_SERC = nuclear_GenE_NZ_SERC['Total Gen'].sum()
    pump_GenE_NZ_SERC = pump_GenE_NZ_SERC['Total Gen'].sum()
    solar_GenE_NZ_SERC = solarN_GenE_NZ_SERC['Total Gen'].sum() + solarE_GenE_NZ_SERC['Total Gen'].sum()
    wind_GenE_NZ_SERC = windN_GenE_NZ_SERC['Total Gen'].sum() + windE_GenE_NZ_SERC['Total Gen'].sum()
    dac_GenE_NZ_SERC = dac_GenE_NZ_SERC['Total Gen'].sum()
    Others_GenE_NZ_SERC = Other1_GenE_NZ_SERC['Total Gen'].sum() + Other2_GenE_NZ_SERC['Total Gen'].sum() \
                          + Other3_GenE_NZ_SERC['Total Gen'].sum() + Other4_GenE_NZ_SERC['Total Gen'].sum() \
                          + Other5_GenE_NZ_SERC['Total Gen'].sum() + Other6_GenE_NZ_SERC['Total Gen'].sum() \
                          + Other7_GenE_NZ_SERC['Total Gen'].sum() + Other8_GenE_NZ_SERC['Total Gen'].sum()
    Coal_GenE_NZ_MISO = Coal_GenE_NZ_MISO['Total Gen'].sum()
    CCCCS_GenE_NZ_MISO = CCCCS_GenE_NZ_MISO['Total Gen'].sum()
    CC_GenE_NZ_MISO = CC_GenE_NZ_MISO['Total Gen'].sum()
    CT_GenE_NZ_MISO = CT_GenE_NZ_MISO['Total Gen'].sum()
    OG_GenE_NZ_MISO = OG_GenE_NZ_MISO['Total Gen'].sum()
    bio_GenE_NZ_MISO = bio_GenE_NZ_MISO['Total Gen'].sum()
    battery_GenE_NZ_MISO = battery_GenE_NZ_MISO['Total Gen'].sum()
    hydrogen_GenE_NZ_MISO = hydrogen_GenE_NZ_MISO['Total Gen'].sum()
    nuclear_GenE_NZ_MISO = nuclear_GenE_NZ_MISO['Total Gen'].sum()
    pump_GenE_NZ_MISO = pump_GenE_NZ_MISO['Total Gen'].sum()
    solar_GenE_NZ_MISO = solarN_GenE_NZ_MISO['Total Gen'].sum() + solarE_GenE_NZ_MISO['Total Gen'].sum()
    wind_GenE_NZ_MISO = windN_GenE_NZ_MISO['Total Gen'].sum() + windE_GenE_NZ_MISO['Total Gen'].sum()
    dac_GenE_NZ_MISO = dac_GenE_NZ_MISO['Total Gen'].sum()
    Others_GenE_NZ_MISO = Other1_GenE_NZ_MISO['Total Gen'].sum() + Other2_GenE_NZ_MISO['Total Gen'].sum() \
                          + Other3_GenE_NZ_MISO['Total Gen'].sum() + Other4_GenE_NZ_MISO['Total Gen'].sum() \
                          + Other5_GenE_NZ_MISO['Total Gen'].sum() + Other6_GenE_NZ_MISO['Total Gen'].sum() \
                          + Other7_GenE_NZ_MISO['Total Gen'].sum() + Other8_GenE_NZ_MISO['Total Gen'].sum()
    Coal_GenE_NZ_NE = Coal_GenE_NZ_NE['Total Gen'].sum()
    CCCCS_GenE_NZ_NE = CCCCS_GenE_NZ_NE['Total Gen'].sum()
    CC_GenE_NZ_NE = CC_GenE_NZ_NE['Total Gen'].sum()
    CT_GenE_NZ_NE = CT_GenE_NZ_NE['Total Gen'].sum()
    OG_GenE_NZ_NE = OG_GenE_NZ_NE['Total Gen'].sum()
    bio_GenE_NZ_NE = bio_GenE_NZ_NE['Total Gen'].sum()
    battery_GenE_NZ_NE = battery_GenE_NZ_NE['Total Gen'].sum()
    hydrogen_GenE_NZ_NE = hydrogen_GenE_NZ_NE['Total Gen'].sum()
    nuclear_GenE_NZ_NE = nuclear_GenE_NZ_NE['Total Gen'].sum()
    pump_GenE_NZ_NE = pump_GenE_NZ_NE['Total Gen'].sum()
    solar_GenE_NZ_NE = solarN_GenE_NZ_NE['Total Gen'].sum() + solarE_GenE_NZ_NE['Total Gen'].sum()
    wind_GenE_NZ_NE = windN_GenE_NZ_NE['Total Gen'].sum() + windE_GenE_NZ_NE['Total Gen'].sum()
    dac_GenE_NZ_NE = dac_GenE_NZ_NE['Total Gen'].sum()
    Others_GenE_NZ_NE = Other1_GenE_NZ_NE['Total Gen'].sum() + Other2_GenE_NZ_NE['Total Gen'].sum() \
                        + Other3_GenE_NZ_NE['Total Gen'].sum() + Other4_GenE_NZ_NE['Total Gen'].sum() \
                        + Other5_GenE_NZ_NE['Total Gen'].sum() + Other6_GenE_NZ_NE['Total Gen'].sum() \
                        + Other7_GenE_NZ_NE['Total Gen'].sum() + Other8_GenE_NZ_NE['Total Gen'].sum()
    Coal_GenE_NZ_NY = Coal_GenE_NZ_NY['Total Gen'].sum()
    CCCCS_GenE_NZ_NY = CCCCS_GenE_NZ_NY['Total Gen'].sum()
    CC_GenE_NZ_NY = CC_GenE_NZ_NY['Total Gen'].sum()
    CT_GenE_NZ_NY = CT_GenE_NZ_NY['Total Gen'].sum()
    OG_GenE_NZ_NY = OG_GenE_NZ_NY['Total Gen'].sum()
    bio_GenE_NZ_NY = bio_GenE_NZ_NY['Total Gen'].sum()
    battery_GenE_NZ_NY = battery_GenE_NZ_NY['Total Gen'].sum()
    hydrogen_GenE_NZ_NY = hydrogen_GenE_NZ_NY['Total Gen'].sum()
    nuclear_GenE_NZ_NY = nuclear_GenE_NZ_NY['Total Gen'].sum()
    pump_GenE_NZ_NY = pump_GenE_NZ_NY['Total Gen'].sum()
    solar_GenE_NZ_NY = solarN_GenE_NZ_NY['Total Gen'].sum() + solarE_GenE_NZ_NY['Total Gen'].sum()
    wind_GenE_NZ_NY = windN_GenE_NZ_NY['Total Gen'].sum() + windE_GenE_NZ_NY['Total Gen'].sum()
    dac_GenE_NZ_NY = dac_GenE_NZ_NY['Total Gen'].sum()
    Others_GenE_NZ_NY = Other1_GenE_NZ_NY['Total Gen'].sum() + Other2_GenE_NZ_NY['Total Gen'].sum() \
                        + Other3_GenE_NZ_NY['Total Gen'].sum() + Other4_GenE_NZ_NY['Total Gen'].sum() \
                        + Other5_GenE_NZ_NY['Total Gen'].sum() + Other6_GenE_NZ_NY['Total Gen'].sum() \
                        + Other7_GenE_NZ_NY['Total Gen'].sum() + Other8_GenE_NZ_NY['Total Gen'].sum()
    Coal_GenE_NZ_PJM = Coal_GenE_NZ_PJM['Total Gen'].sum()
    CCCCS_GenE_NZ_PJM = CCCCS_GenE_NZ_PJM['Total Gen'].sum()
    CC_GenE_NZ_PJM = CC_GenE_NZ_PJM['Total Gen'].sum()
    CT_GenE_NZ_PJM = CT_GenE_NZ_PJM['Total Gen'].sum()
    OG_GenE_NZ_PJM = OG_GenE_NZ_PJM['Total Gen'].sum()
    bio_GenE_NZ_PJM = bio_GenE_NZ_PJM['Total Gen'].sum()
    battery_GenE_NZ_PJM = battery_GenE_NZ_PJM['Total Gen'].sum()
    hydrogen_GenE_NZ_PJM = hydrogen_GenE_NZ_PJM['Total Gen'].sum()
    nuclear_GenE_NZ_PJM = nuclear_GenE_NZ_PJM['Total Gen'].sum()
    pump_GenE_NZ_PJM = pump_GenE_NZ_PJM['Total Gen'].sum()
    solar_GenE_NZ_PJM = solarN_GenE_NZ_PJM['Total Gen'].sum() + solarE_GenE_NZ_PJM['Total Gen'].sum()
    wind_GenE_NZ_PJM = windN_GenE_NZ_PJM['Total Gen'].sum() + windE_GenE_NZ_PJM['Total Gen'].sum()
    dac_GenE_NZ_PJM = dac_GenE_NZ_PJM['Total Gen'].sum()
    Others_GenE_NZ_PJM = Other1_GenE_NZ_PJM['Total Gen'].sum() + Other2_GenE_NZ_PJM['Total Gen'].sum() \
                         + Other3_GenE_NZ_PJM['Total Gen'].sum() + Other4_GenE_NZ_PJM['Total Gen'].sum() \
                         + Other5_GenE_NZ_PJM['Total Gen'].sum() + Other6_GenE_NZ_PJM['Total Gen'].sum() \
                         + Other7_GenE_NZ_PJM['Total Gen'].sum() + Other8_GenE_NZ_PJM['Total Gen'].sum()
    Coal_GenE_NZ_SPP = Coal_GenE_NZ_SPP['Total Gen'].sum()
    CCCCS_GenE_NZ_SPP = CCCCS_GenE_NZ_SPP['Total Gen'].sum()
    CC_GenE_NZ_SPP = CC_GenE_NZ_SPP['Total Gen'].sum()
    CT_GenE_NZ_SPP = CT_GenE_NZ_SPP['Total Gen'].sum()
    OG_GenE_NZ_SPP = OG_GenE_NZ_SPP['Total Gen'].sum()
    bio_GenE_NZ_SPP = bio_GenE_NZ_SPP['Total Gen'].sum()
    battery_GenE_NZ_SPP = battery_GenE_NZ_SPP['Total Gen'].sum()
    hydrogen_GenE_NZ_SPP = hydrogen_GenE_NZ_SPP['Total Gen'].sum()
    nuclear_GenE_NZ_SPP = nuclear_GenE_NZ_SPP['Total Gen'].sum()
    pump_GenE_NZ_SPP = pump_GenE_NZ_SPP['Total Gen'].sum()
    solar_GenE_NZ_SPP = solarN_GenE_NZ_SPP['Total Gen'].sum() + solarE_GenE_NZ_SPP['Total Gen'].sum()
    wind_GenE_NZ_SPP = windN_GenE_NZ_SPP['Total Gen'].sum() + windE_GenE_NZ_SPP['Total Gen'].sum()
    dac_GenE_NZ_SPP = dac_GenE_NZ_SPP['Total Gen'].sum()
    Others_GenE_NZ_SPP = Other1_GenE_NZ_SPP['Total Gen'].sum() + Other2_GenE_NZ_SPP['Total Gen'].sum() \
                         + Other3_GenE_NZ_SPP['Total Gen'].sum() + Other4_GenE_NZ_SPP['Total Gen'].sum() \
                         + Other5_GenE_NZ_SPP['Total Gen'].sum() + Other6_GenE_NZ_SPP['Total Gen'].sum() \
                         + Other7_GenE_NZ_SPP['Total Gen'].sum() + Other8_GenE_NZ_SPP['Total Gen'].sum()

    Coal_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Coal Steam']
    CC_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Combined Cycle CCS']
    CT_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Combustion Turbine']
    OG_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'O/G Steam']
    bio_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Biomass']
    battery_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Hydrogen']
    nuclear_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Nuclear']
    dac_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'DAC']
    solarN_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('solar')]
    solarE_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Solar PV']
    windN_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('wind')]
    windE_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Onshore Wind']
    pump_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Pumped Storage']
    Other1_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Flywheels')]
    Other2_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Fossil Waste')]
    Other3_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Fuel Cell')]
    Other4_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('IGCC')]
    Other5_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Landfill Gas')]
    Other6_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Tires')]

    Coal_GenE_NE2020_SERC = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'SERC']
    Coal_GenE_NE2020_MISO = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'MISO']
    Coal_GenE_NE2020_NE = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'NE']
    Coal_GenE_NE2020_NY = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'NY']
    Coal_GenE_NE2020_PJM = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'PJM']
    Coal_GenE_NE2020_SPP = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'SPP']
    CC_GenE_NE2020_SERC = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'SERC']
    CC_GenE_NE2020_MISO = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'MISO']
    CC_GenE_NE2020_NE = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'NE']
    CC_GenE_NE2020_NY = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'NY']
    CC_GenE_NE2020_PJM = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'PJM']
    CC_GenE_NE2020_SPP = Coal_GenE_NE2020.loc[Coal_GenE_NE2020['region'] == 'SPP']
    CCCCS_GenE_NE2020_SERC = CCCCS_GenE_NE2020.loc[CCCCS_GenE_NE2020['region'] == 'SERC']
    CCCCS_GenE_NE2020_MISO = CCCCS_GenE_NE2020.loc[CCCCS_GenE_NE2020['region'] == 'MISO']
    CCCCS_GenE_NE2020_NE = CCCCS_GenE_NE2020.loc[CCCCS_GenE_NE2020['region'] == 'NE']
    CCCCS_GenE_NE2020_NY = CCCCS_GenE_NE2020.loc[CCCCS_GenE_NE2020['region'] == 'NY']
    CCCCS_GenE_NE2020_PJM = CCCCS_GenE_NE2020.loc[CCCCS_GenE_NE2020['region'] == 'PJM']
    CCCCS_GenE_NE2020_SPP = CCCCS_GenE_NE2020.loc[CCCCS_GenE_NE2020['region'] == 'SPP']
    CT_GenE_NE2020_SERC = CT_GenE_NE2020.loc[CT_GenE_NE2020['region'] == 'SERC']
    CT_GenE_NE2020_MISO = CT_GenE_NE2020.loc[CT_GenE_NE2020['region'] == 'MISO']
    CT_GenE_NE2020_NE = CT_GenE_NE2020.loc[CT_GenE_NE2020['region'] == 'NE']
    CT_GenE_NE2020_NY = CT_GenE_NE2020.loc[CT_GenE_NE2020['region'] == 'NY']
    CT_GenE_NE2020_PJM = CT_GenE_NE2020.loc[CT_GenE_NE2020['region'] == 'PJM']
    CT_GenE_NE2020_SPP = CT_GenE_NE2020.loc[CT_GenE_NE2020['region'] == 'SPP']
    OG_GenE_NE2020_SERC = OG_GenE_NE2020.loc[OG_GenE_NE2020['region'] == 'SERC']
    OG_GenE_NE2020_MISO = OG_GenE_NE2020.loc[OG_GenE_NE2020['region'] == 'MISO']
    OG_GenE_NE2020_NE = OG_GenE_NE2020.loc[OG_GenE_NE2020['region'] == 'NE']
    OG_GenE_NE2020_NY = OG_GenE_NE2020.loc[OG_GenE_NE2020['region'] == 'NY']
    OG_GenE_NE2020_PJM = OG_GenE_NE2020.loc[OG_GenE_NE2020['region'] == 'PJM']
    OG_GenE_NE2020_SPP = OG_GenE_NE2020.loc[OG_GenE_NE2020['region'] == 'SPP']
    bio_GenE_NE2020_SERC = bio_GenE_NE2020.loc[bio_GenE_NE2020['region'] == 'SERC']
    bio_GenE_NE2020_MISO = bio_GenE_NE2020.loc[bio_GenE_NE2020['region'] == 'MISO']
    bio_GenE_NE2020_NE = bio_GenE_NE2020.loc[bio_GenE_NE2020['region'] == 'NE']
    bio_GenE_NE2020_NY = bio_GenE_NE2020.loc[bio_GenE_NE2020['region'] == 'NY']
    bio_GenE_NE2020_PJM = bio_GenE_NE2020.loc[bio_GenE_NE2020['region'] == 'PJM']
    bio_GenE_NE2020_SPP = bio_GenE_NE2020.loc[bio_GenE_NE2020['region'] == 'SPP']
    battery_GenE_NE2020_SERC = battery_GenE_NE2020.loc[battery_GenE_NE2020['region'] == 'SERC']
    battery_GenE_NE2020_MISO = battery_GenE_NE2020.loc[battery_GenE_NE2020['region'] == 'MISO']
    battery_GenE_NE2020_NE = battery_GenE_NE2020.loc[battery_GenE_NE2020['region'] == 'NE']
    battery_GenE_NE2020_NY = battery_GenE_NE2020.loc[battery_GenE_NE2020['region'] == 'NY']
    battery_GenE_NE2020_PJM = battery_GenE_NE2020.loc[battery_GenE_NE2020['region'] == 'PJM']
    battery_GenE_NE2020_SPP = battery_GenE_NE2020.loc[battery_GenE_NE2020['region'] == 'SPP']
    hydrogen_GenE_NE2020_SERC = hydrogen_GenE_NE2020.loc[hydrogen_GenE_NE2020['region'] == 'SERC']
    hydrogen_GenE_NE2020_MISO = hydrogen_GenE_NE2020.loc[hydrogen_GenE_NE2020['region'] == 'MISO']
    hydrogen_GenE_NE2020_NE = hydrogen_GenE_NE2020.loc[hydrogen_GenE_NE2020['region'] == 'NE']
    hydrogen_GenE_NE2020_NY = hydrogen_GenE_NE2020.loc[hydrogen_GenE_NE2020['region'] == 'NY']
    hydrogen_GenE_NE2020_PJM = hydrogen_GenE_NE2020.loc[hydrogen_GenE_NE2020['region'] == 'PJM']
    hydrogen_GenE_NE2020_SPP = hydrogen_GenE_NE2020.loc[hydrogen_GenE_NE2020['region'] == 'SPP']
    nuclear_GenE_NE2020_SERC = nuclear_GenE_NE2020.loc[nuclear_GenE_NE2020['region'] == 'SERC']
    nuclear_GenE_NE2020_MISO = nuclear_GenE_NE2020.loc[nuclear_GenE_NE2020['region'] == 'MISO']
    nuclear_GenE_NE2020_NE = nuclear_GenE_NE2020.loc[nuclear_GenE_NE2020['region'] == 'NE']
    nuclear_GenE_NE2020_NY = nuclear_GenE_NE2020.loc[nuclear_GenE_NE2020['region'] == 'NY']
    nuclear_GenE_NE2020_PJM = nuclear_GenE_NE2020.loc[nuclear_GenE_NE2020['region'] == 'PJM']
    nuclear_GenE_NE2020_SPP = nuclear_GenE_NE2020.loc[nuclear_GenE_NE2020['region'] == 'SPP']
    dac_GenE_NE2020_SERC = dac_GenE_NE2020.loc[dac_GenE_NE2020['region'] == 'SERC']
    dac_GenE_NE2020_MISO = dac_GenE_NE2020.loc[dac_GenE_NE2020['region'] == 'MISO']
    dac_GenE_NE2020_NE = dac_GenE_NE2020.loc[dac_GenE_NE2020['region'] == 'NE']
    dac_GenE_NE2020_NY = dac_GenE_NE2020.loc[dac_GenE_NE2020['region'] == 'NY']
    dac_GenE_NE2020_PJM = dac_GenE_NE2020.loc[dac_GenE_NE2020['region'] == 'PJM']
    dac_GenE_NE2020_SPP = dac_GenE_NE2020.loc[dac_GenE_NE2020['region'] == 'SPP']
    solarN_GenE_NE2020_SERC = solarN_GenE_NE2020.loc[solarN_GenE_NE2020['region'] == 'SERC']
    solarN_GenE_NE2020_MISO = solarN_GenE_NE2020.loc[solarN_GenE_NE2020['region'] == 'MISO']
    solarN_GenE_NE2020_NE = solarN_GenE_NE2020.loc[solarN_GenE_NE2020['region'] == 'NE']
    solarN_GenE_NE2020_NY = solarN_GenE_NE2020.loc[solarN_GenE_NE2020['region'] == 'NY']
    solarN_GenE_NE2020_PJM = solarN_GenE_NE2020.loc[solarN_GenE_NE2020['region'] == 'PJM']
    solarN_GenE_NE2020_SPP = solarN_GenE_NE2020.loc[solarN_GenE_NE2020['region'] == 'SPP']
    solarE_GenE_NE2020_SERC = solarE_GenE_NE2020.loc[solarE_GenE_NE2020['region'] == 'SERC']
    solarE_GenE_NE2020_MISO = solarE_GenE_NE2020.loc[solarE_GenE_NE2020['region'] == 'MISO']
    solarE_GenE_NE2020_NE = solarE_GenE_NE2020.loc[solarE_GenE_NE2020['region'] == 'NE']
    solarE_GenE_NE2020_NY = solarE_GenE_NE2020.loc[solarE_GenE_NE2020['region'] == 'NY']
    solarE_GenE_NE2020_PJM = solarE_GenE_NE2020.loc[solarE_GenE_NE2020['region'] == 'PJM']
    solarE_GenE_NE2020_SPP = solarE_GenE_NE2020.loc[solarE_GenE_NE2020['region'] == 'SPP']
    windN_GenE_NE2020_SERC = windN_GenE_NE2020.loc[windN_GenE_NE2020['region'] == 'SERC']
    windN_GenE_NE2020_MISO = windN_GenE_NE2020.loc[windN_GenE_NE2020['region'] == 'MISO']
    windN_GenE_NE2020_NE = windN_GenE_NE2020.loc[windN_GenE_NE2020['region'] == 'NE']
    windN_GenE_NE2020_NY = windN_GenE_NE2020.loc[windN_GenE_NE2020['region'] == 'NY']
    windN_GenE_NE2020_PJM = windN_GenE_NE2020.loc[windN_GenE_NE2020['region'] == 'PJM']
    windN_GenE_NE2020_SPP = windN_GenE_NE2020.loc[windN_GenE_NE2020['region'] == 'SPP']
    windE_GenE_NE2020_SERC = windE_GenE_NE2020.loc[windE_GenE_NE2020['region'] == 'SERC']
    windE_GenE_NE2020_MISO = windE_GenE_NE2020.loc[windE_GenE_NE2020['region'] == 'MISO']
    windE_GenE_NE2020_NE = windE_GenE_NE2020.loc[windE_GenE_NE2020['region'] == 'NE']
    windE_GenE_NE2020_NY = windE_GenE_NE2020.loc[windE_GenE_NE2020['region'] == 'NY']
    windE_GenE_NE2020_PJM = windE_GenE_NE2020.loc[windE_GenE_NE2020['region'] == 'PJM']
    windE_GenE_NE2020_SPP = windE_GenE_NE2020.loc[windE_GenE_NE2020['region'] == 'SPP']
    pump_GenE_NE2020_SERC = pump_GenE_NE2020.loc[pump_GenE_NE2020['region'] == 'SERC']
    pump_GenE_NE2020_MISO = pump_GenE_NE2020.loc[pump_GenE_NE2020['region'] == 'MISO']
    pump_GenE_NE2020_NE = pump_GenE_NE2020.loc[pump_GenE_NE2020['region'] == 'NE']
    pump_GenE_NE2020_NY = pump_GenE_NE2020.loc[pump_GenE_NE2020['region'] == 'NY']
    pump_GenE_NE2020_PJM = pump_GenE_NE2020.loc[pump_GenE_NE2020['region'] == 'PJM']
    pump_GenE_NE2020_SPP = pump_GenE_NE2020.loc[pump_GenE_NE2020['region'] == 'SPP']
    Other1_GenE_NE2020_SERC = Other1_GenE_NE2020.loc[Other1_GenE_NE2020['region'] == 'SERC']
    Other1_GenE_NE2020_MISO = Other1_GenE_NE2020.loc[Other1_GenE_NE2020['region'] == 'MISO']
    Other1_GenE_NE2020_NE = Other1_GenE_NE2020.loc[Other1_GenE_NE2020['region'] == 'NE']
    Other1_GenE_NE2020_NY = Other1_GenE_NE2020.loc[Other1_GenE_NE2020['region'] == 'NY']
    Other1_GenE_NE2020_PJM = Other1_GenE_NE2020.loc[Other1_GenE_NE2020['region'] == 'PJM']
    Other1_GenE_NE2020_SPP = Other1_GenE_NE2020.loc[Other1_GenE_NE2020['region'] == 'SPP']
    Other2_GenE_NE2020_SERC = Other2_GenE_NE2020.loc[Other2_GenE_NE2020['region'] == 'SERC']
    Other2_GenE_NE2020_MISO = Other2_GenE_NE2020.loc[Other2_GenE_NE2020['region'] == 'MISO']
    Other2_GenE_NE2020_NE = Other2_GenE_NE2020.loc[Other2_GenE_NE2020['region'] == 'NE']
    Other2_GenE_NE2020_NY = Other2_GenE_NE2020.loc[Other2_GenE_NE2020['region'] == 'NY']
    Other2_GenE_NE2020_PJM = Other2_GenE_NE2020.loc[Other2_GenE_NE2020['region'] == 'PJM']
    Other2_GenE_NE2020_SPP = Other2_GenE_NE2020.loc[Other2_GenE_NE2020['region'] == 'SPP']
    Other3_GenE_NE2020_SERC = Other3_GenE_NE2020.loc[Other3_GenE_NE2020['region'] == 'SERC']
    Other3_GenE_NE2020_MISO = Other3_GenE_NE2020.loc[Other3_GenE_NE2020['region'] == 'MISO']
    Other3_GenE_NE2020_NE = Other3_GenE_NE2020.loc[Other3_GenE_NE2020['region'] == 'NE']
    Other3_GenE_NE2020_NY = Other3_GenE_NE2020.loc[Other3_GenE_NE2020['region'] == 'NY']
    Other3_GenE_NE2020_PJM = Other3_GenE_NE2020.loc[Other3_GenE_NE2020['region'] == 'PJM']
    Other3_GenE_NE2020_SPP = Other3_GenE_NE2020.loc[Other3_GenE_NE2020['region'] == 'SPP']
    Other4_GenE_NE2020_SERC = Other4_GenE_NE2020.loc[Other4_GenE_NE2020['region'] == 'SERC']
    Other4_GenE_NE2020_MISO = Other4_GenE_NE2020.loc[Other4_GenE_NE2020['region'] == 'MISO']
    Other4_GenE_NE2020_NE = Other4_GenE_NE2020.loc[Other4_GenE_NE2020['region'] == 'NE']
    Other4_GenE_NE2020_NY = Other4_GenE_NE2020.loc[Other4_GenE_NE2020['region'] == 'NY']
    Other4_GenE_NE2020_PJM = Other4_GenE_NE2020.loc[Other4_GenE_NE2020['region'] == 'PJM']
    Other4_GenE_NE2020_SPP = Other4_GenE_NE2020.loc[Other4_GenE_NE2020['region'] == 'SPP']
    Other5_GenE_NE2020_SERC = Other5_GenE_NE2020.loc[Other5_GenE_NE2020['region'] == 'SERC']
    Other5_GenE_NE2020_MISO = Other5_GenE_NE2020.loc[Other5_GenE_NE2020['region'] == 'MISO']
    Other5_GenE_NE2020_NE = Other5_GenE_NE2020.loc[Other5_GenE_NE2020['region'] == 'NE']
    Other5_GenE_NE2020_NY = Other5_GenE_NE2020.loc[Other5_GenE_NE2020['region'] == 'NY']
    Other5_GenE_NE2020_PJM = Other5_GenE_NE2020.loc[Other5_GenE_NE2020['region'] == 'PJM']
    Other5_GenE_NE2020_SPP = Other5_GenE_NE2020.loc[Other5_GenE_NE2020['region'] == 'SPP']
    Other6_GenE_NE2020_SERC = Other6_GenE_NE2020.loc[Other6_GenE_NE2020['region'] == 'SERC']
    Other6_GenE_NE2020_MISO = Other6_GenE_NE2020.loc[Other6_GenE_NE2020['region'] == 'MISO']
    Other6_GenE_NE2020_NE = Other6_GenE_NE2020.loc[Other6_GenE_NE2020['region'] == 'NE']
    Other6_GenE_NE2020_NY = Other6_GenE_NE2020.loc[Other6_GenE_NE2020['region'] == 'NY']
    Other6_GenE_NE2020_PJM = Other6_GenE_NE2020.loc[Other6_GenE_NE2020['region'] == 'PJM']
    Other6_GenE_NE2020_SPP = Other6_GenE_NE2020.loc[Other6_GenE_NE2020['region'] == 'SPP']
    Other7_GenE_NE2020_SERC = Other7_GenE_NE2020.loc[Other7_GenE_NE2020['region'] == 'SERC']
    Other7_GenE_NE2020_MISO = Other7_GenE_NE2020.loc[Other7_GenE_NE2020['region'] == 'MISO']
    Other7_GenE_NE2020_NE = Other7_GenE_NE2020.loc[Other7_GenE_NE2020['region'] == 'NE']
    Other7_GenE_NE2020_NY = Other7_GenE_NE2020.loc[Other7_GenE_NE2020['region'] == 'NY']
    Other7_GenE_NE2020_PJM = Other7_GenE_NE2020.loc[Other7_GenE_NE2020['region'] == 'PJM']
    Other7_GenE_NE2020_SPP = Other7_GenE_NE2020.loc[Other7_GenE_NE2020['region'] == 'SPP']
    Other8_GenE_NE2020_SERC = Other8_GenE_NE2020.loc[Other8_GenE_NE2020['region'] == 'SERC']
    Other8_GenE_NE2020_MISO = Other8_GenE_NE2020.loc[Other8_GenE_NE2020['region'] == 'MISO']
    Other8_GenE_NE2020_NE = Other8_GenE_NE2020.loc[Other8_GenE_NE2020['region'] == 'NE']
    Other8_GenE_NE2020_NY = Other8_GenE_NE2020.loc[Other8_GenE_NE2020['region'] == 'NY']
    Other8_GenE_NE2020_PJM = Other8_GenE_NE2020.loc[Other8_GenE_NE2020['region'] == 'PJM']
    Other8_GenE_NE2020_SPP = Other8_GenE_NE2020.loc[Other8_GenE_NE2020['region'] == 'SPP']

    Coal_GenE_NE2020 = Coal_GenE_NE2020['Total Gen'].sum()
    CCCCS_GenE_NE2020 = CCCCS_GenE_NE2020['Total Gen'].sum()
    CC_GenE_NE2020 = CC_GenE_NE2020['Total Gen'].sum()
    CT_GenE_NE2020 = CT_GenE_NE2020['Total Gen'].sum()
    OG_GenE_NE2020 = OG_GenE_NE2020['Total Gen'].sum()
    bio_GenE_NE2020 = bio_GenE_NE2020['Total Gen'].sum()
    battery_GenE_NE2020 = battery_GenE_NE2020['Total Gen'].sum()
    hydrogen_GenE_NE2020 = hydrogen_GenE_NE2020['Total Gen'].sum()
    nuclear_GenE_NE2020 = nuclear_GenE_NE2020['Total Gen'].sum()
    pump_GenE_NE2020 = pump_GenE_NE2020['Total Gen'].sum()
    solar_GenE_NE2020 = solarN_GenE_NE2020['Total Gen'].sum() + solarE_GenE_NE2020['Total Gen'].sum()
    wind_GenE_NE2020 = windN_GenE_NE2020['Total Gen'].sum() + windE_GenE_NE2020['Total Gen'].sum()
    dac_GenE_NE2020 = dac_GenE_NE2020['Total Gen'].sum()
    Others_GenE_NE2020 = Other1_GenE_NE2020['Total Gen'].sum() + Other2_GenE_NE2020['Total Gen'].sum() \
                         + Other3_GenE_NE2020['Total Gen'].sum() + Other4_GenE_NE2020['Total Gen'].sum() \
                         + Other5_GenE_NE2020['Total Gen'].sum() + Other6_GenE_NE2020['Total Gen'].sum() \
                         + Other7_GenE_NE2020['Total Gen'].sum() + Other8_GenE_NE2020['Total Gen'].sum()

    Coal_GenE_NE2020_SERC = Coal_GenE_NE2020_SERC['Total Gen'].sum()
    CCCCS_GenE_NE2020_SERC = CCCCS_GenE_NE2020_SERC['Total Gen'].sum()
    CC_GenE_NE2020_SERC = CC_GenE_NE2020_SERC['Total Gen'].sum()
    CT_GenE_NE2020_SERC = CT_GenE_NE2020_SERC['Total Gen'].sum()
    OG_GenE_NE2020_SERC = OG_GenE_NE2020_SERC['Total Gen'].sum()
    bio_GenE_NE2020_SERC = bio_GenE_NE2020_SERC['Total Gen'].sum()
    battery_GenE_NE2020_SERC = battery_GenE_NE2020_SERC['Total Gen'].sum()
    hydrogen_GenE_NE2020_SERC = hydrogen_GenE_NE2020_SERC['Total Gen'].sum()
    nuclear_GenE_NE2020_SERC = nuclear_GenE_NE2020_SERC['Total Gen'].sum()
    pump_GenE_NE2020_SERC = pump_GenE_NE2020_SERC['Total Gen'].sum()
    solar_GenE_NE2020_SERC = solarN_GenE_NE2020_SERC['Total Gen'].sum() + solarE_GenE_NE2020_SERC['Total Gen'].sum()
    wind_GenE_NE2020_SERC = windN_GenE_NE2020_SERC['Total Gen'].sum() + windE_GenE_NE2020_SERC['Total Gen'].sum()
    dac_GenE_NE2020_SERC = dac_GenE_NE2020_SERC['Total Gen'].sum()
    Others_GenE_NE2020_SERC = Other1_GenE_NE2020_SERC['Total Gen'].sum() + Other2_GenE_NE2020_SERC['Total Gen'].sum() \
                              + Other3_GenE_NE2020_SERC['Total Gen'].sum() + Other4_GenE_NE2020_SERC['Total Gen'].sum() \
                              + Other5_GenE_NE2020_SERC['Total Gen'].sum() + Other6_GenE_NE2020_SERC['Total Gen'].sum() \
                              + Other7_GenE_NE2020_SERC['Total Gen'].sum() + Other8_GenE_NE2020_SERC['Total Gen'].sum()
    Coal_GenE_NE2020_MISO = Coal_GenE_NE2020_MISO['Total Gen'].sum()
    CCCCS_GenE_NE2020_MISO = CCCCS_GenE_NE2020_MISO['Total Gen'].sum()
    CC_GenE_NE2020_MISO = CC_GenE_NE2020_MISO['Total Gen'].sum()
    CT_GenE_NE2020_MISO = CT_GenE_NE2020_MISO['Total Gen'].sum()
    OG_GenE_NE2020_MISO = OG_GenE_NE2020_MISO['Total Gen'].sum()
    bio_GenE_NE2020_MISO = bio_GenE_NE2020_MISO['Total Gen'].sum()
    battery_GenE_NE2020_MISO = battery_GenE_NE2020_MISO['Total Gen'].sum()
    hydrogen_GenE_NE2020_MISO = hydrogen_GenE_NE2020_MISO['Total Gen'].sum()
    nuclear_GenE_NE2020_MISO = nuclear_GenE_NE2020_MISO['Total Gen'].sum()
    pump_GenE_NE2020_MISO = pump_GenE_NE2020_MISO['Total Gen'].sum()
    solar_GenE_NE2020_MISO = solarN_GenE_NE2020_MISO['Total Gen'].sum() + solarE_GenE_NE2020_MISO['Total Gen'].sum()
    wind_GenE_NE2020_MISO = windN_GenE_NE2020_MISO['Total Gen'].sum() + windE_GenE_NE2020_MISO['Total Gen'].sum()
    dac_GenE_NE2020_MISO = dac_GenE_NE2020_MISO['Total Gen'].sum()
    Others_GenE_NE2020_MISO = Other1_GenE_NE2020_MISO['Total Gen'].sum() + Other2_GenE_NE2020_MISO['Total Gen'].sum() \
                              + Other3_GenE_NE2020_MISO['Total Gen'].sum() + Other4_GenE_NE2020_MISO['Total Gen'].sum() \
                              + Other5_GenE_NE2020_MISO['Total Gen'].sum() + Other6_GenE_NE2020_MISO['Total Gen'].sum() \
                              + Other7_GenE_NE2020_MISO['Total Gen'].sum() + Other8_GenE_NE2020_MISO['Total Gen'].sum()
    Coal_GenE_NE2020_NE = Coal_GenE_NE2020_NE['Total Gen'].sum()
    CCCCS_GenE_NE2020_NE = CCCCS_GenE_NE2020_NE['Total Gen'].sum()
    CC_GenE_NE2020_NE = CC_GenE_NE2020_NE['Total Gen'].sum()
    CT_GenE_NE2020_NE = CT_GenE_NE2020_NE['Total Gen'].sum()
    OG_GenE_NE2020_NE = OG_GenE_NE2020_NE['Total Gen'].sum()
    bio_GenE_NE2020_NE = bio_GenE_NE2020_NE['Total Gen'].sum()
    battery_GenE_NE2020_NE = battery_GenE_NE2020_NE['Total Gen'].sum()
    hydrogen_GenE_NE2020_NE = hydrogen_GenE_NE2020_NE['Total Gen'].sum()
    nuclear_GenE_NE2020_NE = nuclear_GenE_NE2020_NE['Total Gen'].sum()
    pump_GenE_NE2020_NE = pump_GenE_NE2020_NE['Total Gen'].sum()
    solar_GenE_NE2020_NE = solarN_GenE_NE2020_NE['Total Gen'].sum() + solarE_GenE_NE2020_NE['Total Gen'].sum()
    wind_GenE_NE2020_NE = windN_GenE_NE2020_NE['Total Gen'].sum() + windE_GenE_NE2020_NE['Total Gen'].sum()
    dac_GenE_NE2020_NE = dac_GenE_NE2020_NE['Total Gen'].sum()
    Others_GenE_NE2020_NE = Other1_GenE_NE2020_NE['Total Gen'].sum() + Other2_GenE_NE2020_NE['Total Gen'].sum() \
                            + Other3_GenE_NE2020_NE['Total Gen'].sum() + Other4_GenE_NE2020_NE['Total Gen'].sum() \
                            + Other5_GenE_NE2020_NE['Total Gen'].sum() + Other6_GenE_NE2020_NE['Total Gen'].sum() \
                            + Other7_GenE_NE2020_NE['Total Gen'].sum() + Other8_GenE_NE2020_NE['Total Gen'].sum()
    Coal_GenE_NE2020_NY = Coal_GenE_NE2020_NY['Total Gen'].sum()
    CCCCS_GenE_NE2020_NY = CCCCS_GenE_NE2020_NY['Total Gen'].sum()
    CC_GenE_NE2020_NY = CC_GenE_NE2020_NY['Total Gen'].sum()
    CT_GenE_NE2020_NY = CT_GenE_NE2020_NY['Total Gen'].sum()
    OG_GenE_NE2020_NY = OG_GenE_NE2020_NY['Total Gen'].sum()
    bio_GenE_NE2020_NY = bio_GenE_NE2020_NY['Total Gen'].sum()
    battery_GenE_NE2020_NY = battery_GenE_NE2020_NY['Total Gen'].sum()
    hydrogen_GenE_NE2020_NY = hydrogen_GenE_NE2020_NY['Total Gen'].sum()
    nuclear_GenE_NE2020_NY = nuclear_GenE_NE2020_NY['Total Gen'].sum()
    pump_GenE_NE2020_NY = pump_GenE_NE2020_NY['Total Gen'].sum()
    solar_GenE_NE2020_NY = solarN_GenE_NE2020_NY['Total Gen'].sum() + solarE_GenE_NE2020_NY['Total Gen'].sum()
    wind_GenE_NE2020_NY = windN_GenE_NE2020_NY['Total Gen'].sum() + windE_GenE_NE2020_NY['Total Gen'].sum()
    dac_GenE_NE2020_NY = dac_GenE_NE2020_NY['Total Gen'].sum()
    Others_GenE_NE2020_NY = Other1_GenE_NE2020_NY['Total Gen'].sum() + Other2_GenE_NE2020_NY['Total Gen'].sum() \
                            + Other3_GenE_NE2020_NY['Total Gen'].sum() + Other4_GenE_NE2020_NY['Total Gen'].sum() \
                            + Other5_GenE_NE2020_NY['Total Gen'].sum() + Other6_GenE_NE2020_NY['Total Gen'].sum() \
                            + Other7_GenE_NE2020_NY['Total Gen'].sum() + Other8_GenE_NE2020_NY['Total Gen'].sum()
    Coal_GenE_NE2020_PJM = Coal_GenE_NE2020_PJM['Total Gen'].sum()
    CCCCS_GenE_NE2020_PJM = CCCCS_GenE_NE2020_PJM['Total Gen'].sum()
    CC_GenE_NE2020_PJM = CC_GenE_NE2020_PJM['Total Gen'].sum()
    CT_GenE_NE2020_PJM = CT_GenE_NE2020_PJM['Total Gen'].sum()
    OG_GenE_NE2020_PJM = OG_GenE_NE2020_PJM['Total Gen'].sum()
    bio_GenE_NE2020_PJM = bio_GenE_NE2020_PJM['Total Gen'].sum()
    battery_GenE_NE2020_PJM = battery_GenE_NE2020_PJM['Total Gen'].sum()
    hydrogen_GenE_NE2020_PJM = hydrogen_GenE_NE2020_PJM['Total Gen'].sum()
    nuclear_GenE_NE2020_PJM = nuclear_GenE_NE2020_PJM['Total Gen'].sum()
    pump_GenE_NE2020_PJM = pump_GenE_NE2020_PJM['Total Gen'].sum()
    solar_GenE_NE2020_PJM = solarN_GenE_NE2020_PJM['Total Gen'].sum() + solarE_GenE_NE2020_PJM['Total Gen'].sum()
    wind_GenE_NE2020_PJM = windN_GenE_NE2020_PJM['Total Gen'].sum() + windE_GenE_NE2020_PJM['Total Gen'].sum()
    dac_GenE_NE2020_PJM = dac_GenE_NE2020_PJM['Total Gen'].sum()
    Others_GenE_NE2020_PJM = Other1_GenE_NE2020_PJM['Total Gen'].sum() + Other2_GenE_NE2020_PJM['Total Gen'].sum() \
                             + Other3_GenE_NE2020_PJM['Total Gen'].sum() + Other4_GenE_NE2020_PJM['Total Gen'].sum() \
                             + Other5_GenE_NE2020_PJM['Total Gen'].sum() + Other6_GenE_NE2020_PJM['Total Gen'].sum() \
                             + Other7_GenE_NE2020_PJM['Total Gen'].sum() + Other8_GenE_NE2020_PJM['Total Gen'].sum()
    Coal_GenE_NE2020_SPP = Coal_GenE_NE2020_SPP['Total Gen'].sum()
    CCCCS_GenE_NE2020_SPP = CCCCS_GenE_NE2020_SPP['Total Gen'].sum()
    CC_GenE_NE2020_SPP = CC_GenE_NE2020_SPP['Total Gen'].sum()
    CT_GenE_NE2020_SPP = CT_GenE_NE2020_SPP['Total Gen'].sum()
    OG_GenE_NE2020_SPP = OG_GenE_NE2020_SPP['Total Gen'].sum()
    bio_GenE_NE2020_SPP = bio_GenE_NE2020_SPP['Total Gen'].sum()
    battery_GenE_NE2020_SPP = battery_GenE_NE2020_SPP['Total Gen'].sum()
    hydrogen_GenE_NE2020_SPP = hydrogen_GenE_NE2020_SPP['Total Gen'].sum()
    nuclear_GenE_NE2020_SPP = nuclear_GenE_NE2020_SPP['Total Gen'].sum()
    pump_GenE_NE2020_SPP = pump_GenE_NE2020_SPP['Total Gen'].sum()
    solar_GenE_NE2020_SPP = solarN_GenE_NE2020_SPP['Total Gen'].sum() + solarE_GenE_NE2020_SPP['Total Gen'].sum()
    wind_GenE_NE2020_SPP = windN_GenE_NE2020_SPP['Total Gen'].sum() + windE_GenE_NE2020_SPP['Total Gen'].sum()
    dac_GenE_NE2020_SPP = dac_GenE_NE2020_SPP['Total Gen'].sum()
    Others_GenE_NE2020_SPP = Other1_GenE_NE2020_SPP['Total Gen'].sum() + Other2_GenE_NE2020_SPP['Total Gen'].sum() \
                             + Other3_GenE_NE2020_SPP['Total Gen'].sum() + Other4_GenE_NE2020_SPP['Total Gen'].sum() \
                             + Other5_GenE_NE2020_SPP['Total Gen'].sum() + Other6_GenE_NE2020_SPP['Total Gen'].sum() \
                             + Other7_GenE_NE2020_SPP['Total Gen'].sum() + Other8_GenE_NE2020_SPP['Total Gen'].sum()

    Coal_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Coal Steam']
    CC_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Combined Cycle CCS']
    CT_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Combustion Turbine']
    OG_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'O/G Steam']
    bio_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Biomass']
    battery_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Hydrogen']
    nuclear_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Nuclear']
    dac_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'DAC']
    solarN_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('solar')]
    solarE_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Solar PV']
    windN_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('wind')]
    windE_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Onshore Wind']
    pump_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Pumped Storage']
    Other1_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Flywheels')]
    Other2_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Fossil Waste')]
    Other3_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Fuel Cell')]
    Other4_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('IGCC')]
    Other5_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Landfill Gas')]
    Other6_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Tires')]

    Coal_GenE_NE2030_SERC = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'SERC']
    Coal_GenE_NE2030_MISO = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'MISO']
    Coal_GenE_NE2030_NE = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'NE']
    Coal_GenE_NE2030_NY = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'NY']
    Coal_GenE_NE2030_PJM = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'PJM']
    Coal_GenE_NE2030_SPP = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'SPP']
    CC_GenE_NE2030_SERC = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'SERC']
    CC_GenE_NE2030_MISO = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'MISO']
    CC_GenE_NE2030_NE = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'NE']
    CC_GenE_NE2030_NY = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'NY']
    CC_GenE_NE2030_PJM = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'PJM']
    CC_GenE_NE2030_SPP = Coal_GenE_NE2030.loc[Coal_GenE_NE2030['region'] == 'SPP']
    CCCCS_GenE_NE2030_SERC = CCCCS_GenE_NE2030.loc[CCCCS_GenE_NE2030['region'] == 'SERC']
    CCCCS_GenE_NE2030_MISO = CCCCS_GenE_NE2030.loc[CCCCS_GenE_NE2030['region'] == 'MISO']
    CCCCS_GenE_NE2030_NE = CCCCS_GenE_NE2030.loc[CCCCS_GenE_NE2030['region'] == 'NE']
    CCCCS_GenE_NE2030_NY = CCCCS_GenE_NE2030.loc[CCCCS_GenE_NE2030['region'] == 'NY']
    CCCCS_GenE_NE2030_PJM = CCCCS_GenE_NE2030.loc[CCCCS_GenE_NE2030['region'] == 'PJM']
    CCCCS_GenE_NE2030_SPP = CCCCS_GenE_NE2030.loc[CCCCS_GenE_NE2030['region'] == 'SPP']
    CT_GenE_NE2030_SERC = CT_GenE_NE2030.loc[CT_GenE_NE2030['region'] == 'SERC']
    CT_GenE_NE2030_MISO = CT_GenE_NE2030.loc[CT_GenE_NE2030['region'] == 'MISO']
    CT_GenE_NE2030_NE = CT_GenE_NE2030.loc[CT_GenE_NE2030['region'] == 'NE']
    CT_GenE_NE2030_NY = CT_GenE_NE2030.loc[CT_GenE_NE2030['region'] == 'NY']
    CT_GenE_NE2030_PJM = CT_GenE_NE2030.loc[CT_GenE_NE2030['region'] == 'PJM']
    CT_GenE_NE2030_SPP = CT_GenE_NE2030.loc[CT_GenE_NE2030['region'] == 'SPP']
    OG_GenE_NE2030_SERC = OG_GenE_NE2030.loc[OG_GenE_NE2030['region'] == 'SERC']
    OG_GenE_NE2030_MISO = OG_GenE_NE2030.loc[OG_GenE_NE2030['region'] == 'MISO']
    OG_GenE_NE2030_NE = OG_GenE_NE2030.loc[OG_GenE_NE2030['region'] == 'NE']
    OG_GenE_NE2030_NY = OG_GenE_NE2030.loc[OG_GenE_NE2030['region'] == 'NY']
    OG_GenE_NE2030_PJM = OG_GenE_NE2030.loc[OG_GenE_NE2030['region'] == 'PJM']
    OG_GenE_NE2030_SPP = OG_GenE_NE2030.loc[OG_GenE_NE2030['region'] == 'SPP']
    bio_GenE_NE2030_SERC = bio_GenE_NE2030.loc[bio_GenE_NE2030['region'] == 'SERC']
    bio_GenE_NE2030_MISO = bio_GenE_NE2030.loc[bio_GenE_NE2030['region'] == 'MISO']
    bio_GenE_NE2030_NE = bio_GenE_NE2030.loc[bio_GenE_NE2030['region'] == 'NE']
    bio_GenE_NE2030_NY = bio_GenE_NE2030.loc[bio_GenE_NE2030['region'] == 'NY']
    bio_GenE_NE2030_PJM = bio_GenE_NE2030.loc[bio_GenE_NE2030['region'] == 'PJM']
    bio_GenE_NE2030_SPP = bio_GenE_NE2030.loc[bio_GenE_NE2030['region'] == 'SPP']
    battery_GenE_NE2030_SERC = battery_GenE_NE2030.loc[battery_GenE_NE2030['region'] == 'SERC']
    battery_GenE_NE2030_MISO = battery_GenE_NE2030.loc[battery_GenE_NE2030['region'] == 'MISO']
    battery_GenE_NE2030_NE = battery_GenE_NE2030.loc[battery_GenE_NE2030['region'] == 'NE']
    battery_GenE_NE2030_NY = battery_GenE_NE2030.loc[battery_GenE_NE2030['region'] == 'NY']
    battery_GenE_NE2030_PJM = battery_GenE_NE2030.loc[battery_GenE_NE2030['region'] == 'PJM']
    battery_GenE_NE2030_SPP = battery_GenE_NE2030.loc[battery_GenE_NE2030['region'] == 'SPP']
    hydrogen_GenE_NE2030_SERC = hydrogen_GenE_NE2030.loc[hydrogen_GenE_NE2030['region'] == 'SERC']
    hydrogen_GenE_NE2030_MISO = hydrogen_GenE_NE2030.loc[hydrogen_GenE_NE2030['region'] == 'MISO']
    hydrogen_GenE_NE2030_NE = hydrogen_GenE_NE2030.loc[hydrogen_GenE_NE2030['region'] == 'NE']
    hydrogen_GenE_NE2030_NY = hydrogen_GenE_NE2030.loc[hydrogen_GenE_NE2030['region'] == 'NY']
    hydrogen_GenE_NE2030_PJM = hydrogen_GenE_NE2030.loc[hydrogen_GenE_NE2030['region'] == 'PJM']
    hydrogen_GenE_NE2030_SPP = hydrogen_GenE_NE2030.loc[hydrogen_GenE_NE2030['region'] == 'SPP']
    nuclear_GenE_NE2030_SERC = nuclear_GenE_NE2030.loc[nuclear_GenE_NE2030['region'] == 'SERC']
    nuclear_GenE_NE2030_MISO = nuclear_GenE_NE2030.loc[nuclear_GenE_NE2030['region'] == 'MISO']
    nuclear_GenE_NE2030_NE = nuclear_GenE_NE2030.loc[nuclear_GenE_NE2030['region'] == 'NE']
    nuclear_GenE_NE2030_NY = nuclear_GenE_NE2030.loc[nuclear_GenE_NE2030['region'] == 'NY']
    nuclear_GenE_NE2030_PJM = nuclear_GenE_NE2030.loc[nuclear_GenE_NE2030['region'] == 'PJM']
    nuclear_GenE_NE2030_SPP = nuclear_GenE_NE2030.loc[nuclear_GenE_NE2030['region'] == 'SPP']
    dac_GenE_NE2030_SERC = dac_GenE_NE2030.loc[dac_GenE_NE2030['region'] == 'SERC']
    dac_GenE_NE2030_MISO = dac_GenE_NE2030.loc[dac_GenE_NE2030['region'] == 'MISO']
    dac_GenE_NE2030_NE = dac_GenE_NE2030.loc[dac_GenE_NE2030['region'] == 'NE']
    dac_GenE_NE2030_NY = dac_GenE_NE2030.loc[dac_GenE_NE2030['region'] == 'NY']
    dac_GenE_NE2030_PJM = dac_GenE_NE2030.loc[dac_GenE_NE2030['region'] == 'PJM']
    dac_GenE_NE2030_SPP = dac_GenE_NE2030.loc[dac_GenE_NE2030['region'] == 'SPP']
    solarN_GenE_NE2030_SERC = solarN_GenE_NE2030.loc[solarN_GenE_NE2030['region'] == 'SERC']
    solarN_GenE_NE2030_MISO = solarN_GenE_NE2030.loc[solarN_GenE_NE2030['region'] == 'MISO']
    solarN_GenE_NE2030_NE = solarN_GenE_NE2030.loc[solarN_GenE_NE2030['region'] == 'NE']
    solarN_GenE_NE2030_NY = solarN_GenE_NE2030.loc[solarN_GenE_NE2030['region'] == 'NY']
    solarN_GenE_NE2030_PJM = solarN_GenE_NE2030.loc[solarN_GenE_NE2030['region'] == 'PJM']
    solarN_GenE_NE2030_SPP = solarN_GenE_NE2030.loc[solarN_GenE_NE2030['region'] == 'SPP']
    solarE_GenE_NE2030_SERC = solarE_GenE_NE2030.loc[solarE_GenE_NE2030['region'] == 'SERC']
    solarE_GenE_NE2030_MISO = solarE_GenE_NE2030.loc[solarE_GenE_NE2030['region'] == 'MISO']
    solarE_GenE_NE2030_NE = solarE_GenE_NE2030.loc[solarE_GenE_NE2030['region'] == 'NE']
    solarE_GenE_NE2030_NY = solarE_GenE_NE2030.loc[solarE_GenE_NE2030['region'] == 'NY']
    solarE_GenE_NE2030_PJM = solarE_GenE_NE2030.loc[solarE_GenE_NE2030['region'] == 'PJM']
    solarE_GenE_NE2030_SPP = solarE_GenE_NE2030.loc[solarE_GenE_NE2030['region'] == 'SPP']
    windN_GenE_NE2030_SERC = windN_GenE_NE2030.loc[windN_GenE_NE2030['region'] == 'SERC']
    windN_GenE_NE2030_MISO = windN_GenE_NE2030.loc[windN_GenE_NE2030['region'] == 'MISO']
    windN_GenE_NE2030_NE = windN_GenE_NE2030.loc[windN_GenE_NE2030['region'] == 'NE']
    windN_GenE_NE2030_NY = windN_GenE_NE2030.loc[windN_GenE_NE2030['region'] == 'NY']
    windN_GenE_NE2030_PJM = windN_GenE_NE2030.loc[windN_GenE_NE2030['region'] == 'PJM']
    windN_GenE_NE2030_SPP = windN_GenE_NE2030.loc[windN_GenE_NE2030['region'] == 'SPP']
    windE_GenE_NE2030_SERC = windE_GenE_NE2030.loc[windE_GenE_NE2030['region'] == 'SERC']
    windE_GenE_NE2030_MISO = windE_GenE_NE2030.loc[windE_GenE_NE2030['region'] == 'MISO']
    windE_GenE_NE2030_NE = windE_GenE_NE2030.loc[windE_GenE_NE2030['region'] == 'NE']
    windE_GenE_NE2030_NY = windE_GenE_NE2030.loc[windE_GenE_NE2030['region'] == 'NY']
    windE_GenE_NE2030_PJM = windE_GenE_NE2030.loc[windE_GenE_NE2030['region'] == 'PJM']
    windE_GenE_NE2030_SPP = windE_GenE_NE2030.loc[windE_GenE_NE2030['region'] == 'SPP']
    pump_GenE_NE2030_SERC = pump_GenE_NE2030.loc[pump_GenE_NE2030['region'] == 'SERC']
    pump_GenE_NE2030_MISO = pump_GenE_NE2030.loc[pump_GenE_NE2030['region'] == 'MISO']
    pump_GenE_NE2030_NE = pump_GenE_NE2030.loc[pump_GenE_NE2030['region'] == 'NE']
    pump_GenE_NE2030_NY = pump_GenE_NE2030.loc[pump_GenE_NE2030['region'] == 'NY']
    pump_GenE_NE2030_PJM = pump_GenE_NE2030.loc[pump_GenE_NE2030['region'] == 'PJM']
    pump_GenE_NE2030_SPP = pump_GenE_NE2030.loc[pump_GenE_NE2030['region'] == 'SPP']
    Other1_GenE_NE2030_SERC = Other1_GenE_NE2030.loc[Other1_GenE_NE2030['region'] == 'SERC']
    Other1_GenE_NE2030_MISO = Other1_GenE_NE2030.loc[Other1_GenE_NE2030['region'] == 'MISO']
    Other1_GenE_NE2030_NE = Other1_GenE_NE2030.loc[Other1_GenE_NE2030['region'] == 'NE']
    Other1_GenE_NE2030_NY = Other1_GenE_NE2030.loc[Other1_GenE_NE2030['region'] == 'NY']
    Other1_GenE_NE2030_PJM = Other1_GenE_NE2030.loc[Other1_GenE_NE2030['region'] == 'PJM']
    Other1_GenE_NE2030_SPP = Other1_GenE_NE2030.loc[Other1_GenE_NE2030['region'] == 'SPP']
    Other2_GenE_NE2030_SERC = Other2_GenE_NE2030.loc[Other2_GenE_NE2030['region'] == 'SERC']
    Other2_GenE_NE2030_MISO = Other2_GenE_NE2030.loc[Other2_GenE_NE2030['region'] == 'MISO']
    Other2_GenE_NE2030_NE = Other2_GenE_NE2030.loc[Other2_GenE_NE2030['region'] == 'NE']
    Other2_GenE_NE2030_NY = Other2_GenE_NE2030.loc[Other2_GenE_NE2030['region'] == 'NY']
    Other2_GenE_NE2030_PJM = Other2_GenE_NE2030.loc[Other2_GenE_NE2030['region'] == 'PJM']
    Other2_GenE_NE2030_SPP = Other2_GenE_NE2030.loc[Other2_GenE_NE2030['region'] == 'SPP']
    Other3_GenE_NE2030_SERC = Other3_GenE_NE2030.loc[Other3_GenE_NE2030['region'] == 'SERC']
    Other3_GenE_NE2030_MISO = Other3_GenE_NE2030.loc[Other3_GenE_NE2030['region'] == 'MISO']
    Other3_GenE_NE2030_NE = Other3_GenE_NE2030.loc[Other3_GenE_NE2030['region'] == 'NE']
    Other3_GenE_NE2030_NY = Other3_GenE_NE2030.loc[Other3_GenE_NE2030['region'] == 'NY']
    Other3_GenE_NE2030_PJM = Other3_GenE_NE2030.loc[Other3_GenE_NE2030['region'] == 'PJM']
    Other3_GenE_NE2030_SPP = Other3_GenE_NE2030.loc[Other3_GenE_NE2030['region'] == 'SPP']
    Other4_GenE_NE2030_SERC = Other4_GenE_NE2030.loc[Other4_GenE_NE2030['region'] == 'SERC']
    Other4_GenE_NE2030_MISO = Other4_GenE_NE2030.loc[Other4_GenE_NE2030['region'] == 'MISO']
    Other4_GenE_NE2030_NE = Other4_GenE_NE2030.loc[Other4_GenE_NE2030['region'] == 'NE']
    Other4_GenE_NE2030_NY = Other4_GenE_NE2030.loc[Other4_GenE_NE2030['region'] == 'NY']
    Other4_GenE_NE2030_PJM = Other4_GenE_NE2030.loc[Other4_GenE_NE2030['region'] == 'PJM']
    Other4_GenE_NE2030_SPP = Other4_GenE_NE2030.loc[Other4_GenE_NE2030['region'] == 'SPP']
    Other5_GenE_NE2030_SERC = Other5_GenE_NE2030.loc[Other5_GenE_NE2030['region'] == 'SERC']
    Other5_GenE_NE2030_MISO = Other5_GenE_NE2030.loc[Other5_GenE_NE2030['region'] == 'MISO']
    Other5_GenE_NE2030_NE = Other5_GenE_NE2030.loc[Other5_GenE_NE2030['region'] == 'NE']
    Other5_GenE_NE2030_NY = Other5_GenE_NE2030.loc[Other5_GenE_NE2030['region'] == 'NY']
    Other5_GenE_NE2030_PJM = Other5_GenE_NE2030.loc[Other5_GenE_NE2030['region'] == 'PJM']
    Other5_GenE_NE2030_SPP = Other5_GenE_NE2030.loc[Other5_GenE_NE2030['region'] == 'SPP']
    Other6_GenE_NE2030_SERC = Other6_GenE_NE2030.loc[Other6_GenE_NE2030['region'] == 'SERC']
    Other6_GenE_NE2030_MISO = Other6_GenE_NE2030.loc[Other6_GenE_NE2030['region'] == 'MISO']
    Other6_GenE_NE2030_NE = Other6_GenE_NE2030.loc[Other6_GenE_NE2030['region'] == 'NE']
    Other6_GenE_NE2030_NY = Other6_GenE_NE2030.loc[Other6_GenE_NE2030['region'] == 'NY']
    Other6_GenE_NE2030_PJM = Other6_GenE_NE2030.loc[Other6_GenE_NE2030['region'] == 'PJM']
    Other6_GenE_NE2030_SPP = Other6_GenE_NE2030.loc[Other6_GenE_NE2030['region'] == 'SPP']
    Other7_GenE_NE2030_SERC = Other7_GenE_NE2030.loc[Other7_GenE_NE2030['region'] == 'SERC']
    Other7_GenE_NE2030_MISO = Other7_GenE_NE2030.loc[Other7_GenE_NE2030['region'] == 'MISO']
    Other7_GenE_NE2030_NE = Other7_GenE_NE2030.loc[Other7_GenE_NE2030['region'] == 'NE']
    Other7_GenE_NE2030_NY = Other7_GenE_NE2030.loc[Other7_GenE_NE2030['region'] == 'NY']
    Other7_GenE_NE2030_PJM = Other7_GenE_NE2030.loc[Other7_GenE_NE2030['region'] == 'PJM']
    Other7_GenE_NE2030_SPP = Other7_GenE_NE2030.loc[Other7_GenE_NE2030['region'] == 'SPP']
    Other8_GenE_NE2030_SERC = Other8_GenE_NE2030.loc[Other8_GenE_NE2030['region'] == 'SERC']
    Other8_GenE_NE2030_MISO = Other8_GenE_NE2030.loc[Other8_GenE_NE2030['region'] == 'MISO']
    Other8_GenE_NE2030_NE = Other8_GenE_NE2030.loc[Other8_GenE_NE2030['region'] == 'NE']
    Other8_GenE_NE2030_NY = Other8_GenE_NE2030.loc[Other8_GenE_NE2030['region'] == 'NY']
    Other8_GenE_NE2030_PJM = Other8_GenE_NE2030.loc[Other8_GenE_NE2030['region'] == 'PJM']
    Other8_GenE_NE2030_SPP = Other8_GenE_NE2030.loc[Other8_GenE_NE2030['region'] == 'SPP']

    Coal_GenE_NE2030 = Coal_GenE_NE2030['Total Gen'].sum()
    CCCCS_GenE_NE2030 = CCCCS_GenE_NE2030['Total Gen'].sum()
    CC_GenE_NE2030 = CC_GenE_NE2030['Total Gen'].sum()
    CT_GenE_NE2030 = CT_GenE_NE2030['Total Gen'].sum()
    OG_GenE_NE2030 = OG_GenE_NE2030['Total Gen'].sum()
    bio_GenE_NE2030 = bio_GenE_NE2030['Total Gen'].sum()
    battery_GenE_NE2030 = battery_GenE_NE2030['Total Gen'].sum()
    hydrogen_GenE_NE2030 = hydrogen_GenE_NE2030['Total Gen'].sum()
    nuclear_GenE_NE2030 = nuclear_GenE_NE2030['Total Gen'].sum()
    pump_GenE_NE2030 = pump_GenE_NE2030['Total Gen'].sum()
    solar_GenE_NE2030 = solarN_GenE_NE2030['Total Gen'].sum() + solarE_GenE_NE2030['Total Gen'].sum()
    wind_GenE_NE2030 = windN_GenE_NE2030['Total Gen'].sum() + windE_GenE_NE2030['Total Gen'].sum()
    dac_GenE_NE2030 = dac_GenE_NE2030['Total Gen'].sum()
    Others_GenE_NE2030 = Other1_GenE_NE2030['Total Gen'].sum() + Other2_GenE_NE2030['Total Gen'].sum() \
                         + Other3_GenE_NE2030['Total Gen'].sum() + Other4_GenE_NE2030['Total Gen'].sum() \
                         + Other5_GenE_NE2030['Total Gen'].sum() + Other6_GenE_NE2030['Total Gen'].sum() \
                         + Other7_GenE_NE2030['Total Gen'].sum() + Other8_GenE_NE2030['Total Gen'].sum()

    Coal_GenE_NE2030_SERC = Coal_GenE_NE2030_SERC['Total Gen'].sum()
    CCCCS_GenE_NE2030_SERC = CCCCS_GenE_NE2030_SERC['Total Gen'].sum()
    CC_GenE_NE2030_SERC = CC_GenE_NE2030_SERC['Total Gen'].sum()
    CT_GenE_NE2030_SERC = CT_GenE_NE2030_SERC['Total Gen'].sum()
    OG_GenE_NE2030_SERC = OG_GenE_NE2030_SERC['Total Gen'].sum()
    bio_GenE_NE2030_SERC = bio_GenE_NE2030_SERC['Total Gen'].sum()
    battery_GenE_NE2030_SERC = battery_GenE_NE2030_SERC['Total Gen'].sum()
    hydrogen_GenE_NE2030_SERC = hydrogen_GenE_NE2030_SERC['Total Gen'].sum()
    nuclear_GenE_NE2030_SERC = nuclear_GenE_NE2030_SERC['Total Gen'].sum()
    pump_GenE_NE2030_SERC = pump_GenE_NE2030_SERC['Total Gen'].sum()
    solar_GenE_NE2030_SERC = solarN_GenE_NE2030_SERC['Total Gen'].sum() + solarE_GenE_NE2030_SERC['Total Gen'].sum()
    wind_GenE_NE2030_SERC = windN_GenE_NE2030_SERC['Total Gen'].sum() + windE_GenE_NE2030_SERC['Total Gen'].sum()
    dac_GenE_NE2030_SERC = dac_GenE_NE2030_SERC['Total Gen'].sum()
    Others_GenE_NE2030_SERC = Other1_GenE_NE2030_SERC['Total Gen'].sum() + Other2_GenE_NE2030_SERC['Total Gen'].sum() \
                              + Other3_GenE_NE2030_SERC['Total Gen'].sum() + Other4_GenE_NE2030_SERC['Total Gen'].sum() \
                              + Other5_GenE_NE2030_SERC['Total Gen'].sum() + Other6_GenE_NE2030_SERC['Total Gen'].sum() \
                              + Other7_GenE_NE2030_SERC['Total Gen'].sum() + Other8_GenE_NE2030_SERC['Total Gen'].sum()
    Coal_GenE_NE2030_MISO = Coal_GenE_NE2030_MISO['Total Gen'].sum()
    CCCCS_GenE_NE2030_MISO = CCCCS_GenE_NE2030_MISO['Total Gen'].sum()
    CC_GenE_NE2030_MISO = CC_GenE_NE2030_MISO['Total Gen'].sum()
    CT_GenE_NE2030_MISO = CT_GenE_NE2030_MISO['Total Gen'].sum()
    OG_GenE_NE2030_MISO = OG_GenE_NE2030_MISO['Total Gen'].sum()
    bio_GenE_NE2030_MISO = bio_GenE_NE2030_MISO['Total Gen'].sum()
    battery_GenE_NE2030_MISO = battery_GenE_NE2030_MISO['Total Gen'].sum()
    hydrogen_GenE_NE2030_MISO = hydrogen_GenE_NE2030_MISO['Total Gen'].sum()
    nuclear_GenE_NE2030_MISO = nuclear_GenE_NE2030_MISO['Total Gen'].sum()
    pump_GenE_NE2030_MISO = pump_GenE_NE2030_MISO['Total Gen'].sum()
    solar_GenE_NE2030_MISO = solarN_GenE_NE2030_MISO['Total Gen'].sum() + solarE_GenE_NE2030_MISO['Total Gen'].sum()
    wind_GenE_NE2030_MISO = windN_GenE_NE2030_MISO['Total Gen'].sum() + windE_GenE_NE2030_MISO['Total Gen'].sum()
    dac_GenE_NE2030_MISO = dac_GenE_NE2030_MISO['Total Gen'].sum()
    Others_GenE_NE2030_MISO = Other1_GenE_NE2030_MISO['Total Gen'].sum() + Other2_GenE_NE2030_MISO['Total Gen'].sum() \
                              + Other3_GenE_NE2030_MISO['Total Gen'].sum() + Other4_GenE_NE2030_MISO['Total Gen'].sum() \
                              + Other5_GenE_NE2030_MISO['Total Gen'].sum() + Other6_GenE_NE2030_MISO['Total Gen'].sum() \
                              + Other7_GenE_NE2030_MISO['Total Gen'].sum() + Other8_GenE_NE2030_MISO['Total Gen'].sum()
    Coal_GenE_NE2030_NE = Coal_GenE_NE2030_NE['Total Gen'].sum()
    CCCCS_GenE_NE2030_NE = CCCCS_GenE_NE2030_NE['Total Gen'].sum()
    CC_GenE_NE2030_NE = CC_GenE_NE2030_NE['Total Gen'].sum()
    CT_GenE_NE2030_NE = CT_GenE_NE2030_NE['Total Gen'].sum()
    OG_GenE_NE2030_NE = OG_GenE_NE2030_NE['Total Gen'].sum()
    bio_GenE_NE2030_NE = bio_GenE_NE2030_NE['Total Gen'].sum()
    battery_GenE_NE2030_NE = battery_GenE_NE2030_NE['Total Gen'].sum()
    hydrogen_GenE_NE2030_NE = hydrogen_GenE_NE2030_NE['Total Gen'].sum()
    nuclear_GenE_NE2030_NE = nuclear_GenE_NE2030_NE['Total Gen'].sum()
    pump_GenE_NE2030_NE = pump_GenE_NE2030_NE['Total Gen'].sum()
    solar_GenE_NE2030_NE = solarN_GenE_NE2030_NE['Total Gen'].sum() + solarE_GenE_NE2030_NE['Total Gen'].sum()
    wind_GenE_NE2030_NE = windN_GenE_NE2030_NE['Total Gen'].sum() + windE_GenE_NE2030_NE['Total Gen'].sum()
    dac_GenE_NE2030_NE = dac_GenE_NE2030_NE['Total Gen'].sum()
    Others_GenE_NE2030_NE = Other1_GenE_NE2030_NE['Total Gen'].sum() + Other2_GenE_NE2030_NE['Total Gen'].sum() \
                            + Other3_GenE_NE2030_NE['Total Gen'].sum() + Other4_GenE_NE2030_NE['Total Gen'].sum() \
                            + Other5_GenE_NE2030_NE['Total Gen'].sum() + Other6_GenE_NE2030_NE['Total Gen'].sum() \
                            + Other7_GenE_NE2030_NE['Total Gen'].sum() + Other8_GenE_NE2030_NE['Total Gen'].sum()
    Coal_GenE_NE2030_NY = Coal_GenE_NE2030_NY['Total Gen'].sum()
    CCCCS_GenE_NE2030_NY = CCCCS_GenE_NE2030_NY['Total Gen'].sum()
    CC_GenE_NE2030_NY = CC_GenE_NE2030_NY['Total Gen'].sum()
    CT_GenE_NE2030_NY = CT_GenE_NE2030_NY['Total Gen'].sum()
    OG_GenE_NE2030_NY = OG_GenE_NE2030_NY['Total Gen'].sum()
    bio_GenE_NE2030_NY = bio_GenE_NE2030_NY['Total Gen'].sum()
    battery_GenE_NE2030_NY = battery_GenE_NE2030_NY['Total Gen'].sum()
    hydrogen_GenE_NE2030_NY = hydrogen_GenE_NE2030_NY['Total Gen'].sum()
    nuclear_GenE_NE2030_NY = nuclear_GenE_NE2030_NY['Total Gen'].sum()
    pump_GenE_NE2030_NY = pump_GenE_NE2030_NY['Total Gen'].sum()
    solar_GenE_NE2030_NY = solarN_GenE_NE2030_NY['Total Gen'].sum() + solarE_GenE_NE2030_NY['Total Gen'].sum()
    wind_GenE_NE2030_NY = windN_GenE_NE2030_NY['Total Gen'].sum() + windE_GenE_NE2030_NY['Total Gen'].sum()
    dac_GenE_NE2030_NY = dac_GenE_NE2030_NY['Total Gen'].sum()
    Others_GenE_NE2030_NY = Other1_GenE_NE2030_NY['Total Gen'].sum() + Other2_GenE_NE2030_NY['Total Gen'].sum() \
                            + Other3_GenE_NE2030_NY['Total Gen'].sum() + Other4_GenE_NE2030_NY['Total Gen'].sum() \
                            + Other5_GenE_NE2030_NY['Total Gen'].sum() + Other6_GenE_NE2030_NY['Total Gen'].sum() \
                            + Other7_GenE_NE2030_NY['Total Gen'].sum() + Other8_GenE_NE2030_NY['Total Gen'].sum()
    Coal_GenE_NE2030_PJM = Coal_GenE_NE2030_PJM['Total Gen'].sum()
    CCCCS_GenE_NE2030_PJM = CCCCS_GenE_NE2030_PJM['Total Gen'].sum()
    CC_GenE_NE2030_PJM = CC_GenE_NE2030_PJM['Total Gen'].sum()
    CT_GenE_NE2030_PJM = CT_GenE_NE2030_PJM['Total Gen'].sum()
    OG_GenE_NE2030_PJM = OG_GenE_NE2030_PJM['Total Gen'].sum()
    bio_GenE_NE2030_PJM = bio_GenE_NE2030_PJM['Total Gen'].sum()
    battery_GenE_NE2030_PJM = battery_GenE_NE2030_PJM['Total Gen'].sum()
    hydrogen_GenE_NE2030_PJM = hydrogen_GenE_NE2030_PJM['Total Gen'].sum()
    nuclear_GenE_NE2030_PJM = nuclear_GenE_NE2030_PJM['Total Gen'].sum()
    pump_GenE_NE2030_PJM = pump_GenE_NE2030_PJM['Total Gen'].sum()
    solar_GenE_NE2030_PJM = solarN_GenE_NE2030_PJM['Total Gen'].sum() + solarE_GenE_NE2030_PJM['Total Gen'].sum()
    wind_GenE_NE2030_PJM = windN_GenE_NE2030_PJM['Total Gen'].sum() + windE_GenE_NE2030_PJM['Total Gen'].sum()
    dac_GenE_NE2030_PJM = dac_GenE_NE2030_PJM['Total Gen'].sum()
    Others_GenE_NE2030_PJM = Other1_GenE_NE2030_PJM['Total Gen'].sum() + Other2_GenE_NE2030_PJM['Total Gen'].sum() \
                             + Other3_GenE_NE2030_PJM['Total Gen'].sum() + Other4_GenE_NE2030_PJM['Total Gen'].sum() \
                             + Other5_GenE_NE2030_PJM['Total Gen'].sum() + Other6_GenE_NE2030_PJM['Total Gen'].sum() \
                             + Other7_GenE_NE2030_PJM['Total Gen'].sum() + Other8_GenE_NE2030_PJM['Total Gen'].sum()
    Coal_GenE_NE2030_SPP = Coal_GenE_NE2030_SPP['Total Gen'].sum()
    CCCCS_GenE_NE2030_SPP = CCCCS_GenE_NE2030_SPP['Total Gen'].sum()
    CC_GenE_NE2030_SPP = CC_GenE_NE2030_SPP['Total Gen'].sum()
    CT_GenE_NE2030_SPP = CT_GenE_NE2030_SPP['Total Gen'].sum()
    OG_GenE_NE2030_SPP = OG_GenE_NE2030_SPP['Total Gen'].sum()
    bio_GenE_NE2030_SPP = bio_GenE_NE2030_SPP['Total Gen'].sum()
    battery_GenE_NE2030_SPP = battery_GenE_NE2030_SPP['Total Gen'].sum()
    hydrogen_GenE_NE2030_SPP = hydrogen_GenE_NE2030_SPP['Total Gen'].sum()
    nuclear_GenE_NE2030_SPP = nuclear_GenE_NE2030_SPP['Total Gen'].sum()
    pump_GenE_NE2030_SPP = pump_GenE_NE2030_SPP['Total Gen'].sum()
    solar_GenE_NE2030_SPP = solarN_GenE_NE2030_SPP['Total Gen'].sum() + solarE_GenE_NE2030_SPP['Total Gen'].sum()
    wind_GenE_NE2030_SPP = windN_GenE_NE2030_SPP['Total Gen'].sum() + windE_GenE_NE2030_SPP['Total Gen'].sum()
    dac_GenE_NE2030_SPP = dac_GenE_NE2030_SPP['Total Gen'].sum()
    Others_GenE_NE2030_SPP = Other1_GenE_NE2030_SPP['Total Gen'].sum() + Other2_GenE_NE2030_SPP['Total Gen'].sum() \
                             + Other3_GenE_NE2030_SPP['Total Gen'].sum() + Other4_GenE_NE2030_SPP['Total Gen'].sum() \
                             + Other5_GenE_NE2030_SPP['Total Gen'].sum() + Other6_GenE_NE2030_SPP['Total Gen'].sum() \
                             + Other7_GenE_NE2030_SPP['Total Gen'].sum() + Other8_GenE_NE2030_SPP['Total Gen'].sum()

    Coal_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Coal Steam']
    CC_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Combined Cycle CCS']
    CT_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Combustion Turbine']
    OG_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'O/G Steam']
    bio_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Biomass']
    battery_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Hydrogen']
    nuclear_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Nuclear']
    dac_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'DAC']
    solarN_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('solar')]
    solarE_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Solar PV']
    windN_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('wind')]
    windE_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Onshore Wind']
    pump_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Pumped Storage']
    Other1_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Flywheels')]
    Other2_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Fossil Waste')]
    Other3_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Fuel Cell')]
    Other4_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('IGCC')]
    Other5_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Landfill Gas')]
    Other6_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Tires')]

    Coal_GenE_NE2040_SERC = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'SERC']
    Coal_GenE_NE2040_MISO = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'MISO']
    Coal_GenE_NE2040_NE = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'NE']
    Coal_GenE_NE2040_NY = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'NY']
    Coal_GenE_NE2040_PJM = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'PJM']
    Coal_GenE_NE2040_SPP = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'SPP']
    CC_GenE_NE2040_SERC = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'SERC']
    CC_GenE_NE2040_MISO = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'MISO']
    CC_GenE_NE2040_NE = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'NE']
    CC_GenE_NE2040_NY = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'NY']
    CC_GenE_NE2040_PJM = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'PJM']
    CC_GenE_NE2040_SPP = Coal_GenE_NE2040.loc[Coal_GenE_NE2040['region'] == 'SPP']
    CCCCS_GenE_NE2040_SERC = CCCCS_GenE_NE2040.loc[CCCCS_GenE_NE2040['region'] == 'SERC']
    CCCCS_GenE_NE2040_MISO = CCCCS_GenE_NE2040.loc[CCCCS_GenE_NE2040['region'] == 'MISO']
    CCCCS_GenE_NE2040_NE = CCCCS_GenE_NE2040.loc[CCCCS_GenE_NE2040['region'] == 'NE']
    CCCCS_GenE_NE2040_NY = CCCCS_GenE_NE2040.loc[CCCCS_GenE_NE2040['region'] == 'NY']
    CCCCS_GenE_NE2040_PJM = CCCCS_GenE_NE2040.loc[CCCCS_GenE_NE2040['region'] == 'PJM']
    CCCCS_GenE_NE2040_SPP = CCCCS_GenE_NE2040.loc[CCCCS_GenE_NE2040['region'] == 'SPP']
    CT_GenE_NE2040_SERC = CT_GenE_NE2040.loc[CT_GenE_NE2040['region'] == 'SERC']
    CT_GenE_NE2040_MISO = CT_GenE_NE2040.loc[CT_GenE_NE2040['region'] == 'MISO']
    CT_GenE_NE2040_NE = CT_GenE_NE2040.loc[CT_GenE_NE2040['region'] == 'NE']
    CT_GenE_NE2040_NY = CT_GenE_NE2040.loc[CT_GenE_NE2040['region'] == 'NY']
    CT_GenE_NE2040_PJM = CT_GenE_NE2040.loc[CT_GenE_NE2040['region'] == 'PJM']
    CT_GenE_NE2040_SPP = CT_GenE_NE2040.loc[CT_GenE_NE2040['region'] == 'SPP']
    OG_GenE_NE2040_SERC = OG_GenE_NE2040.loc[OG_GenE_NE2040['region'] == 'SERC']
    OG_GenE_NE2040_MISO = OG_GenE_NE2040.loc[OG_GenE_NE2040['region'] == 'MISO']
    OG_GenE_NE2040_NE = OG_GenE_NE2040.loc[OG_GenE_NE2040['region'] == 'NE']
    OG_GenE_NE2040_NY = OG_GenE_NE2040.loc[OG_GenE_NE2040['region'] == 'NY']
    OG_GenE_NE2040_PJM = OG_GenE_NE2040.loc[OG_GenE_NE2040['region'] == 'PJM']
    OG_GenE_NE2040_SPP = OG_GenE_NE2040.loc[OG_GenE_NE2040['region'] == 'SPP']
    bio_GenE_NE2040_SERC = bio_GenE_NE2040.loc[bio_GenE_NE2040['region'] == 'SERC']
    bio_GenE_NE2040_MISO = bio_GenE_NE2040.loc[bio_GenE_NE2040['region'] == 'MISO']
    bio_GenE_NE2040_NE = bio_GenE_NE2040.loc[bio_GenE_NE2040['region'] == 'NE']
    bio_GenE_NE2040_NY = bio_GenE_NE2040.loc[bio_GenE_NE2040['region'] == 'NY']
    bio_GenE_NE2040_PJM = bio_GenE_NE2040.loc[bio_GenE_NE2040['region'] == 'PJM']
    bio_GenE_NE2040_SPP = bio_GenE_NE2040.loc[bio_GenE_NE2040['region'] == 'SPP']
    battery_GenE_NE2040_SERC = battery_GenE_NE2040.loc[battery_GenE_NE2040['region'] == 'SERC']
    battery_GenE_NE2040_MISO = battery_GenE_NE2040.loc[battery_GenE_NE2040['region'] == 'MISO']
    battery_GenE_NE2040_NE = battery_GenE_NE2040.loc[battery_GenE_NE2040['region'] == 'NE']
    battery_GenE_NE2040_NY = battery_GenE_NE2040.loc[battery_GenE_NE2040['region'] == 'NY']
    battery_GenE_NE2040_PJM = battery_GenE_NE2040.loc[battery_GenE_NE2040['region'] == 'PJM']
    battery_GenE_NE2040_SPP = battery_GenE_NE2040.loc[battery_GenE_NE2040['region'] == 'SPP']
    hydrogen_GenE_NE2040_SERC = hydrogen_GenE_NE2040.loc[hydrogen_GenE_NE2040['region'] == 'SERC']
    hydrogen_GenE_NE2040_MISO = hydrogen_GenE_NE2040.loc[hydrogen_GenE_NE2040['region'] == 'MISO']
    hydrogen_GenE_NE2040_NE = hydrogen_GenE_NE2040.loc[hydrogen_GenE_NE2040['region'] == 'NE']
    hydrogen_GenE_NE2040_NY = hydrogen_GenE_NE2040.loc[hydrogen_GenE_NE2040['region'] == 'NY']
    hydrogen_GenE_NE2040_PJM = hydrogen_GenE_NE2040.loc[hydrogen_GenE_NE2040['region'] == 'PJM']
    hydrogen_GenE_NE2040_SPP = hydrogen_GenE_NE2040.loc[hydrogen_GenE_NE2040['region'] == 'SPP']
    nuclear_GenE_NE2040_SERC = nuclear_GenE_NE2040.loc[nuclear_GenE_NE2040['region'] == 'SERC']
    nuclear_GenE_NE2040_MISO = nuclear_GenE_NE2040.loc[nuclear_GenE_NE2040['region'] == 'MISO']
    nuclear_GenE_NE2040_NE = nuclear_GenE_NE2040.loc[nuclear_GenE_NE2040['region'] == 'NE']
    nuclear_GenE_NE2040_NY = nuclear_GenE_NE2040.loc[nuclear_GenE_NE2040['region'] == 'NY']
    nuclear_GenE_NE2040_PJM = nuclear_GenE_NE2040.loc[nuclear_GenE_NE2040['region'] == 'PJM']
    nuclear_GenE_NE2040_SPP = nuclear_GenE_NE2040.loc[nuclear_GenE_NE2040['region'] == 'SPP']
    dac_GenE_NE2040_SERC = dac_GenE_NE2040.loc[dac_GenE_NE2040['region'] == 'SERC']
    dac_GenE_NE2040_MISO = dac_GenE_NE2040.loc[dac_GenE_NE2040['region'] == 'MISO']
    dac_GenE_NE2040_NE = dac_GenE_NE2040.loc[dac_GenE_NE2040['region'] == 'NE']
    dac_GenE_NE2040_NY = dac_GenE_NE2040.loc[dac_GenE_NE2040['region'] == 'NY']
    dac_GenE_NE2040_PJM = dac_GenE_NE2040.loc[dac_GenE_NE2040['region'] == 'PJM']
    dac_GenE_NE2040_SPP = dac_GenE_NE2040.loc[dac_GenE_NE2040['region'] == 'SPP']
    solarN_GenE_NE2040_SERC = solarN_GenE_NE2040.loc[solarN_GenE_NE2040['region'] == 'SERC']
    solarN_GenE_NE2040_MISO = solarN_GenE_NE2040.loc[solarN_GenE_NE2040['region'] == 'MISO']
    solarN_GenE_NE2040_NE = solarN_GenE_NE2040.loc[solarN_GenE_NE2040['region'] == 'NE']
    solarN_GenE_NE2040_NY = solarN_GenE_NE2040.loc[solarN_GenE_NE2040['region'] == 'NY']
    solarN_GenE_NE2040_PJM = solarN_GenE_NE2040.loc[solarN_GenE_NE2040['region'] == 'PJM']
    solarN_GenE_NE2040_SPP = solarN_GenE_NE2040.loc[solarN_GenE_NE2040['region'] == 'SPP']
    solarE_GenE_NE2040_SERC = solarE_GenE_NE2040.loc[solarE_GenE_NE2040['region'] == 'SERC']
    solarE_GenE_NE2040_MISO = solarE_GenE_NE2040.loc[solarE_GenE_NE2040['region'] == 'MISO']
    solarE_GenE_NE2040_NE = solarE_GenE_NE2040.loc[solarE_GenE_NE2040['region'] == 'NE']
    solarE_GenE_NE2040_NY = solarE_GenE_NE2040.loc[solarE_GenE_NE2040['region'] == 'NY']
    solarE_GenE_NE2040_PJM = solarE_GenE_NE2040.loc[solarE_GenE_NE2040['region'] == 'PJM']
    solarE_GenE_NE2040_SPP = solarE_GenE_NE2040.loc[solarE_GenE_NE2040['region'] == 'SPP']
    windN_GenE_NE2040_SERC = windN_GenE_NE2040.loc[windN_GenE_NE2040['region'] == 'SERC']
    windN_GenE_NE2040_MISO = windN_GenE_NE2040.loc[windN_GenE_NE2040['region'] == 'MISO']
    windN_GenE_NE2040_NE = windN_GenE_NE2040.loc[windN_GenE_NE2040['region'] == 'NE']
    windN_GenE_NE2040_NY = windN_GenE_NE2040.loc[windN_GenE_NE2040['region'] == 'NY']
    windN_GenE_NE2040_PJM = windN_GenE_NE2040.loc[windN_GenE_NE2040['region'] == 'PJM']
    windN_GenE_NE2040_SPP = windN_GenE_NE2040.loc[windN_GenE_NE2040['region'] == 'SPP']
    windE_GenE_NE2040_SERC = windE_GenE_NE2040.loc[windE_GenE_NE2040['region'] == 'SERC']
    windE_GenE_NE2040_MISO = windE_GenE_NE2040.loc[windE_GenE_NE2040['region'] == 'MISO']
    windE_GenE_NE2040_NE = windE_GenE_NE2040.loc[windE_GenE_NE2040['region'] == 'NE']
    windE_GenE_NE2040_NY = windE_GenE_NE2040.loc[windE_GenE_NE2040['region'] == 'NY']
    windE_GenE_NE2040_PJM = windE_GenE_NE2040.loc[windE_GenE_NE2040['region'] == 'PJM']
    windE_GenE_NE2040_SPP = windE_GenE_NE2040.loc[windE_GenE_NE2040['region'] == 'SPP']
    pump_GenE_NE2040_SERC = pump_GenE_NE2040.loc[pump_GenE_NE2040['region'] == 'SERC']
    pump_GenE_NE2040_MISO = pump_GenE_NE2040.loc[pump_GenE_NE2040['region'] == 'MISO']
    pump_GenE_NE2040_NE = pump_GenE_NE2040.loc[pump_GenE_NE2040['region'] == 'NE']
    pump_GenE_NE2040_NY = pump_GenE_NE2040.loc[pump_GenE_NE2040['region'] == 'NY']
    pump_GenE_NE2040_PJM = pump_GenE_NE2040.loc[pump_GenE_NE2040['region'] == 'PJM']
    pump_GenE_NE2040_SPP = pump_GenE_NE2040.loc[pump_GenE_NE2040['region'] == 'SPP']
    Other1_GenE_NE2040_SERC = Other1_GenE_NE2040.loc[Other1_GenE_NE2040['region'] == 'SERC']
    Other1_GenE_NE2040_MISO = Other1_GenE_NE2040.loc[Other1_GenE_NE2040['region'] == 'MISO']
    Other1_GenE_NE2040_NE = Other1_GenE_NE2040.loc[Other1_GenE_NE2040['region'] == 'NE']
    Other1_GenE_NE2040_NY = Other1_GenE_NE2040.loc[Other1_GenE_NE2040['region'] == 'NY']
    Other1_GenE_NE2040_PJM = Other1_GenE_NE2040.loc[Other1_GenE_NE2040['region'] == 'PJM']
    Other1_GenE_NE2040_SPP = Other1_GenE_NE2040.loc[Other1_GenE_NE2040['region'] == 'SPP']
    Other2_GenE_NE2040_SERC = Other2_GenE_NE2040.loc[Other2_GenE_NE2040['region'] == 'SERC']
    Other2_GenE_NE2040_MISO = Other2_GenE_NE2040.loc[Other2_GenE_NE2040['region'] == 'MISO']
    Other2_GenE_NE2040_NE = Other2_GenE_NE2040.loc[Other2_GenE_NE2040['region'] == 'NE']
    Other2_GenE_NE2040_NY = Other2_GenE_NE2040.loc[Other2_GenE_NE2040['region'] == 'NY']
    Other2_GenE_NE2040_PJM = Other2_GenE_NE2040.loc[Other2_GenE_NE2040['region'] == 'PJM']
    Other2_GenE_NE2040_SPP = Other2_GenE_NE2040.loc[Other2_GenE_NE2040['region'] == 'SPP']
    Other3_GenE_NE2040_SERC = Other3_GenE_NE2040.loc[Other3_GenE_NE2040['region'] == 'SERC']
    Other3_GenE_NE2040_MISO = Other3_GenE_NE2040.loc[Other3_GenE_NE2040['region'] == 'MISO']
    Other3_GenE_NE2040_NE = Other3_GenE_NE2040.loc[Other3_GenE_NE2040['region'] == 'NE']
    Other3_GenE_NE2040_NY = Other3_GenE_NE2040.loc[Other3_GenE_NE2040['region'] == 'NY']
    Other3_GenE_NE2040_PJM = Other3_GenE_NE2040.loc[Other3_GenE_NE2040['region'] == 'PJM']
    Other3_GenE_NE2040_SPP = Other3_GenE_NE2040.loc[Other3_GenE_NE2040['region'] == 'SPP']
    Other4_GenE_NE2040_SERC = Other4_GenE_NE2040.loc[Other4_GenE_NE2040['region'] == 'SERC']
    Other4_GenE_NE2040_MISO = Other4_GenE_NE2040.loc[Other4_GenE_NE2040['region'] == 'MISO']
    Other4_GenE_NE2040_NE = Other4_GenE_NE2040.loc[Other4_GenE_NE2040['region'] == 'NE']
    Other4_GenE_NE2040_NY = Other4_GenE_NE2040.loc[Other4_GenE_NE2040['region'] == 'NY']
    Other4_GenE_NE2040_PJM = Other4_GenE_NE2040.loc[Other4_GenE_NE2040['region'] == 'PJM']
    Other4_GenE_NE2040_SPP = Other4_GenE_NE2040.loc[Other4_GenE_NE2040['region'] == 'SPP']
    Other5_GenE_NE2040_SERC = Other5_GenE_NE2040.loc[Other5_GenE_NE2040['region'] == 'SERC']
    Other5_GenE_NE2040_MISO = Other5_GenE_NE2040.loc[Other5_GenE_NE2040['region'] == 'MISO']
    Other5_GenE_NE2040_NE = Other5_GenE_NE2040.loc[Other5_GenE_NE2040['region'] == 'NE']
    Other5_GenE_NE2040_NY = Other5_GenE_NE2040.loc[Other5_GenE_NE2040['region'] == 'NY']
    Other5_GenE_NE2040_PJM = Other5_GenE_NE2040.loc[Other5_GenE_NE2040['region'] == 'PJM']
    Other5_GenE_NE2040_SPP = Other5_GenE_NE2040.loc[Other5_GenE_NE2040['region'] == 'SPP']
    Other6_GenE_NE2040_SERC = Other6_GenE_NE2040.loc[Other6_GenE_NE2040['region'] == 'SERC']
    Other6_GenE_NE2040_MISO = Other6_GenE_NE2040.loc[Other6_GenE_NE2040['region'] == 'MISO']
    Other6_GenE_NE2040_NE = Other6_GenE_NE2040.loc[Other6_GenE_NE2040['region'] == 'NE']
    Other6_GenE_NE2040_NY = Other6_GenE_NE2040.loc[Other6_GenE_NE2040['region'] == 'NY']
    Other6_GenE_NE2040_PJM = Other6_GenE_NE2040.loc[Other6_GenE_NE2040['region'] == 'PJM']
    Other6_GenE_NE2040_SPP = Other6_GenE_NE2040.loc[Other6_GenE_NE2040['region'] == 'SPP']
    Other7_GenE_NE2040_SERC = Other7_GenE_NE2040.loc[Other7_GenE_NE2040['region'] == 'SERC']
    Other7_GenE_NE2040_MISO = Other7_GenE_NE2040.loc[Other7_GenE_NE2040['region'] == 'MISO']
    Other7_GenE_NE2040_NE = Other7_GenE_NE2040.loc[Other7_GenE_NE2040['region'] == 'NE']
    Other7_GenE_NE2040_NY = Other7_GenE_NE2040.loc[Other7_GenE_NE2040['region'] == 'NY']
    Other7_GenE_NE2040_PJM = Other7_GenE_NE2040.loc[Other7_GenE_NE2040['region'] == 'PJM']
    Other7_GenE_NE2040_SPP = Other7_GenE_NE2040.loc[Other7_GenE_NE2040['region'] == 'SPP']
    Other8_GenE_NE2040_SERC = Other8_GenE_NE2040.loc[Other8_GenE_NE2040['region'] == 'SERC']
    Other8_GenE_NE2040_MISO = Other8_GenE_NE2040.loc[Other8_GenE_NE2040['region'] == 'MISO']
    Other8_GenE_NE2040_NE = Other8_GenE_NE2040.loc[Other8_GenE_NE2040['region'] == 'NE']
    Other8_GenE_NE2040_NY = Other8_GenE_NE2040.loc[Other8_GenE_NE2040['region'] == 'NY']
    Other8_GenE_NE2040_PJM = Other8_GenE_NE2040.loc[Other8_GenE_NE2040['region'] == 'PJM']
    Other8_GenE_NE2040_SPP = Other8_GenE_NE2040.loc[Other8_GenE_NE2040['region'] == 'SPP']

    Coal_GenE_NE2040 = Coal_GenE_NE2040['Total Gen'].sum()
    CCCCS_GenE_NE2040 = CCCCS_GenE_NE2040['Total Gen'].sum()
    CC_GenE_NE2040 = CC_GenE_NE2040['Total Gen'].sum()
    CT_GenE_NE2040 = CT_GenE_NE2040['Total Gen'].sum()
    OG_GenE_NE2040 = OG_GenE_NE2040['Total Gen'].sum()
    bio_GenE_NE2040 = bio_GenE_NE2040['Total Gen'].sum()
    battery_GenE_NE2040 = battery_GenE_NE2040['Total Gen'].sum()
    hydrogen_GenE_NE2040 = hydrogen_GenE_NE2040['Total Gen'].sum()
    nuclear_GenE_NE2040 = nuclear_GenE_NE2040['Total Gen'].sum()
    pump_GenE_NE2040 = pump_GenE_NE2040['Total Gen'].sum()
    solar_GenE_NE2040 = solarN_GenE_NE2040['Total Gen'].sum() + solarE_GenE_NE2040['Total Gen'].sum()
    wind_GenE_NE2040 = windN_GenE_NE2040['Total Gen'].sum() + windE_GenE_NE2040['Total Gen'].sum()
    dac_GenE_NE2040 = dac_GenE_NE2040['Total Gen'].sum()
    Others_GenE_NE2040 = Other1_GenE_NE2040['Total Gen'].sum() + Other2_GenE_NE2040['Total Gen'].sum() \
                         + Other3_GenE_NE2040['Total Gen'].sum() + Other4_GenE_NE2040['Total Gen'].sum() \
                         + Other5_GenE_NE2040['Total Gen'].sum() + Other6_GenE_NE2040['Total Gen'].sum() \
                         + Other7_GenE_NE2040['Total Gen'].sum() + Other8_GenE_NE2040['Total Gen'].sum()

    Coal_GenE_NE2040_SERC = Coal_GenE_NE2040_SERC['Total Gen'].sum()
    CCCCS_GenE_NE2040_SERC = CCCCS_GenE_NE2040_SERC['Total Gen'].sum()
    CC_GenE_NE2040_SERC = CC_GenE_NE2040_SERC['Total Gen'].sum()
    CT_GenE_NE2040_SERC = CT_GenE_NE2040_SERC['Total Gen'].sum()
    OG_GenE_NE2040_SERC = OG_GenE_NE2040_SERC['Total Gen'].sum()
    bio_GenE_NE2040_SERC = bio_GenE_NE2040_SERC['Total Gen'].sum()
    battery_GenE_NE2040_SERC = battery_GenE_NE2040_SERC['Total Gen'].sum()
    hydrogen_GenE_NE2040_SERC = hydrogen_GenE_NE2040_SERC['Total Gen'].sum()
    nuclear_GenE_NE2040_SERC = nuclear_GenE_NE2040_SERC['Total Gen'].sum()
    pump_GenE_NE2040_SERC = pump_GenE_NE2040_SERC['Total Gen'].sum()
    solar_GenE_NE2040_SERC = solarN_GenE_NE2040_SERC['Total Gen'].sum() + solarE_GenE_NE2040_SERC['Total Gen'].sum()
    wind_GenE_NE2040_SERC = windN_GenE_NE2040_SERC['Total Gen'].sum() + windE_GenE_NE2040_SERC['Total Gen'].sum()
    dac_GenE_NE2040_SERC = dac_GenE_NE2040_SERC['Total Gen'].sum()
    Others_GenE_NE2040_SERC = Other1_GenE_NE2040_SERC['Total Gen'].sum() + Other2_GenE_NE2040_SERC['Total Gen'].sum() \
                              + Other3_GenE_NE2040_SERC['Total Gen'].sum() + Other4_GenE_NE2040_SERC['Total Gen'].sum() \
                              + Other5_GenE_NE2040_SERC['Total Gen'].sum() + Other6_GenE_NE2040_SERC['Total Gen'].sum() \
                              + Other7_GenE_NE2040_SERC['Total Gen'].sum() + Other8_GenE_NE2040_SERC['Total Gen'].sum()
    Coal_GenE_NE2040_MISO = Coal_GenE_NE2040_MISO['Total Gen'].sum()
    CCCCS_GenE_NE2040_MISO = CCCCS_GenE_NE2040_MISO['Total Gen'].sum()
    CC_GenE_NE2040_MISO = CC_GenE_NE2040_MISO['Total Gen'].sum()
    CT_GenE_NE2040_MISO = CT_GenE_NE2040_MISO['Total Gen'].sum()
    OG_GenE_NE2040_MISO = OG_GenE_NE2040_MISO['Total Gen'].sum()
    bio_GenE_NE2040_MISO = bio_GenE_NE2040_MISO['Total Gen'].sum()
    battery_GenE_NE2040_MISO = battery_GenE_NE2040_MISO['Total Gen'].sum()
    hydrogen_GenE_NE2040_MISO = hydrogen_GenE_NE2040_MISO['Total Gen'].sum()
    nuclear_GenE_NE2040_MISO = nuclear_GenE_NE2040_MISO['Total Gen'].sum()
    pump_GenE_NE2040_MISO = pump_GenE_NE2040_MISO['Total Gen'].sum()
    solar_GenE_NE2040_MISO = solarN_GenE_NE2040_MISO['Total Gen'].sum() + solarE_GenE_NE2040_MISO['Total Gen'].sum()
    wind_GenE_NE2040_MISO = windN_GenE_NE2040_MISO['Total Gen'].sum() + windE_GenE_NE2040_MISO['Total Gen'].sum()
    dac_GenE_NE2040_MISO = dac_GenE_NE2040_MISO['Total Gen'].sum()
    Others_GenE_NE2040_MISO = Other1_GenE_NE2040_MISO['Total Gen'].sum() + Other2_GenE_NE2040_MISO['Total Gen'].sum() \
                              + Other3_GenE_NE2040_MISO['Total Gen'].sum() + Other4_GenE_NE2040_MISO['Total Gen'].sum() \
                              + Other5_GenE_NE2040_MISO['Total Gen'].sum() + Other6_GenE_NE2040_MISO['Total Gen'].sum() \
                              + Other7_GenE_NE2040_MISO['Total Gen'].sum() + Other8_GenE_NE2040_MISO['Total Gen'].sum()
    Coal_GenE_NE2040_NE = Coal_GenE_NE2040_NE['Total Gen'].sum()
    CCCCS_GenE_NE2040_NE = CCCCS_GenE_NE2040_NE['Total Gen'].sum()
    CC_GenE_NE2040_NE = CC_GenE_NE2040_NE['Total Gen'].sum()
    CT_GenE_NE2040_NE = CT_GenE_NE2040_NE['Total Gen'].sum()
    OG_GenE_NE2040_NE = OG_GenE_NE2040_NE['Total Gen'].sum()
    bio_GenE_NE2040_NE = bio_GenE_NE2040_NE['Total Gen'].sum()
    battery_GenE_NE2040_NE = battery_GenE_NE2040_NE['Total Gen'].sum()
    hydrogen_GenE_NE2040_NE = hydrogen_GenE_NE2040_NE['Total Gen'].sum()
    nuclear_GenE_NE2040_NE = nuclear_GenE_NE2040_NE['Total Gen'].sum()
    pump_GenE_NE2040_NE = pump_GenE_NE2040_NE['Total Gen'].sum()
    solar_GenE_NE2040_NE = solarN_GenE_NE2040_NE['Total Gen'].sum() + solarE_GenE_NE2040_NE['Total Gen'].sum()
    wind_GenE_NE2040_NE = windN_GenE_NE2040_NE['Total Gen'].sum() + windE_GenE_NE2040_NE['Total Gen'].sum()
    dac_GenE_NE2040_NE = dac_GenE_NE2040_NE['Total Gen'].sum()
    Others_GenE_NE2040_NE = Other1_GenE_NE2040_NE['Total Gen'].sum() + Other2_GenE_NE2040_NE['Total Gen'].sum() \
                            + Other3_GenE_NE2040_NE['Total Gen'].sum() + Other4_GenE_NE2040_NE['Total Gen'].sum() \
                            + Other5_GenE_NE2040_NE['Total Gen'].sum() + Other6_GenE_NE2040_NE['Total Gen'].sum() \
                            + Other7_GenE_NE2040_NE['Total Gen'].sum() + Other8_GenE_NE2040_NE['Total Gen'].sum()
    Coal_GenE_NE2040_NY = Coal_GenE_NE2040_NY['Total Gen'].sum()
    CCCCS_GenE_NE2040_NY = CCCCS_GenE_NE2040_NY['Total Gen'].sum()
    CC_GenE_NE2040_NY = CC_GenE_NE2040_NY['Total Gen'].sum()
    CT_GenE_NE2040_NY = CT_GenE_NE2040_NY['Total Gen'].sum()
    OG_GenE_NE2040_NY = OG_GenE_NE2040_NY['Total Gen'].sum()
    bio_GenE_NE2040_NY = bio_GenE_NE2040_NY['Total Gen'].sum()
    battery_GenE_NE2040_NY = battery_GenE_NE2040_NY['Total Gen'].sum()
    hydrogen_GenE_NE2040_NY = hydrogen_GenE_NE2040_NY['Total Gen'].sum()
    nuclear_GenE_NE2040_NY = nuclear_GenE_NE2040_NY['Total Gen'].sum()
    pump_GenE_NE2040_NY = pump_GenE_NE2040_NY['Total Gen'].sum()
    solar_GenE_NE2040_NY = solarN_GenE_NE2040_NY['Total Gen'].sum() + solarE_GenE_NE2040_NY['Total Gen'].sum()
    wind_GenE_NE2040_NY = windN_GenE_NE2040_NY['Total Gen'].sum() + windE_GenE_NE2040_NY['Total Gen'].sum()
    dac_GenE_NE2040_NY = dac_GenE_NE2040_NY['Total Gen'].sum()
    Others_GenE_NE2040_NY = Other1_GenE_NE2040_NY['Total Gen'].sum() + Other2_GenE_NE2040_NY['Total Gen'].sum() \
                            + Other3_GenE_NE2040_NY['Total Gen'].sum() + Other4_GenE_NE2040_NY['Total Gen'].sum() \
                            + Other5_GenE_NE2040_NY['Total Gen'].sum() + Other6_GenE_NE2040_NY['Total Gen'].sum() \
                            + Other7_GenE_NE2040_NY['Total Gen'].sum() + Other8_GenE_NE2040_NY['Total Gen'].sum()
    Coal_GenE_NE2040_PJM = Coal_GenE_NE2040_PJM['Total Gen'].sum()
    CCCCS_GenE_NE2040_PJM = CCCCS_GenE_NE2040_PJM['Total Gen'].sum()
    CC_GenE_NE2040_PJM = CC_GenE_NE2040_PJM['Total Gen'].sum()
    CT_GenE_NE2040_PJM = CT_GenE_NE2040_PJM['Total Gen'].sum()
    OG_GenE_NE2040_PJM = OG_GenE_NE2040_PJM['Total Gen'].sum()
    bio_GenE_NE2040_PJM = bio_GenE_NE2040_PJM['Total Gen'].sum()
    battery_GenE_NE2040_PJM = battery_GenE_NE2040_PJM['Total Gen'].sum()
    hydrogen_GenE_NE2040_PJM = hydrogen_GenE_NE2040_PJM['Total Gen'].sum()
    nuclear_GenE_NE2040_PJM = nuclear_GenE_NE2040_PJM['Total Gen'].sum()
    pump_GenE_NE2040_PJM = pump_GenE_NE2040_PJM['Total Gen'].sum()
    solar_GenE_NE2040_PJM = solarN_GenE_NE2040_PJM['Total Gen'].sum() + solarE_GenE_NE2040_PJM['Total Gen'].sum()
    wind_GenE_NE2040_PJM = windN_GenE_NE2040_PJM['Total Gen'].sum() + windE_GenE_NE2040_PJM['Total Gen'].sum()
    dac_GenE_NE2040_PJM = dac_GenE_NE2040_PJM['Total Gen'].sum()
    Others_GenE_NE2040_PJM = Other1_GenE_NE2040_PJM['Total Gen'].sum() + Other2_GenE_NE2040_PJM['Total Gen'].sum() \
                             + Other3_GenE_NE2040_PJM['Total Gen'].sum() + Other4_GenE_NE2040_PJM['Total Gen'].sum() \
                             + Other5_GenE_NE2040_PJM['Total Gen'].sum() + Other6_GenE_NE2040_PJM['Total Gen'].sum() \
                             + Other7_GenE_NE2040_PJM['Total Gen'].sum() + Other8_GenE_NE2040_PJM['Total Gen'].sum()
    Coal_GenE_NE2040_SPP = Coal_GenE_NE2040_SPP['Total Gen'].sum()
    CCCCS_GenE_NE2040_SPP = CCCCS_GenE_NE2040_SPP['Total Gen'].sum()
    CC_GenE_NE2040_SPP = CC_GenE_NE2040_SPP['Total Gen'].sum()
    CT_GenE_NE2040_SPP = CT_GenE_NE2040_SPP['Total Gen'].sum()
    OG_GenE_NE2040_SPP = OG_GenE_NE2040_SPP['Total Gen'].sum()
    bio_GenE_NE2040_SPP = bio_GenE_NE2040_SPP['Total Gen'].sum()
    battery_GenE_NE2040_SPP = battery_GenE_NE2040_SPP['Total Gen'].sum()
    hydrogen_GenE_NE2040_SPP = hydrogen_GenE_NE2040_SPP['Total Gen'].sum()
    nuclear_GenE_NE2040_SPP = nuclear_GenE_NE2040_SPP['Total Gen'].sum()
    pump_GenE_NE2040_SPP = pump_GenE_NE2040_SPP['Total Gen'].sum()
    solar_GenE_NE2040_SPP = solarN_GenE_NE2040_SPP['Total Gen'].sum() + solarE_GenE_NE2040_SPP['Total Gen'].sum()
    wind_GenE_NE2040_SPP = windN_GenE_NE2040_SPP['Total Gen'].sum() + windE_GenE_NE2040_SPP['Total Gen'].sum()
    dac_GenE_NE2040_SPP = dac_GenE_NE2040_SPP['Total Gen'].sum()
    Others_GenE_NE2040_SPP = Other1_GenE_NE2040_SPP['Total Gen'].sum() + Other2_GenE_NE2040_SPP['Total Gen'].sum() \
                             + Other3_GenE_NE2040_SPP['Total Gen'].sum() + Other4_GenE_NE2040_SPP['Total Gen'].sum() \
                             + Other5_GenE_NE2040_SPP['Total Gen'].sum() + Other6_GenE_NE2040_SPP['Total Gen'].sum() \
                             + Other7_GenE_NE2040_SPP['Total Gen'].sum() + Other8_GenE_NE2040_SPP['Total Gen'].sum()

    Coal_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Coal Steam']
    CC_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Combined Cycle CCS']
    CT_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Combustion Turbine']
    OG_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'O/G Steam']
    bio_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Biomass']
    battery_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Hydrogen']
    nuclear_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Nuclear']
    dac_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'DAC']
    solarN_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('solar')]
    solarE_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Solar PV']
    windN_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('wind')]
    windE_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Onshore Wind']
    pump_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Pumped Storage']
    Other1_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Flywheels')]
    Other2_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Fossil Waste')]
    Other3_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Fuel Cell')]
    Other4_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('IGCC')]
    Other5_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Landfill Gas')]
    Other6_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Tires')]

    Coal_GenE_NE2050_SERC = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'SERC']
    Coal_GenE_NE2050_MISO = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'MISO']
    Coal_GenE_NE2050_NE = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'NE']
    Coal_GenE_NE2050_NY = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'NY']
    Coal_GenE_NE2050_PJM = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'PJM']
    Coal_GenE_NE2050_SPP = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'SPP']
    CC_GenE_NE2050_SERC = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'SERC']
    CC_GenE_NE2050_MISO = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'MISO']
    CC_GenE_NE2050_NE = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'NE']
    CC_GenE_NE2050_NY = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'NY']
    CC_GenE_NE2050_PJM = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'PJM']
    CC_GenE_NE2050_SPP = Coal_GenE_NE2050.loc[Coal_GenE_NE2050['region'] == 'SPP']
    CCCCS_GenE_NE2050_SERC = CCCCS_GenE_NE2050.loc[CCCCS_GenE_NE2050['region'] == 'SERC']
    CCCCS_GenE_NE2050_MISO = CCCCS_GenE_NE2050.loc[CCCCS_GenE_NE2050['region'] == 'MISO']
    CCCCS_GenE_NE2050_NE = CCCCS_GenE_NE2050.loc[CCCCS_GenE_NE2050['region'] == 'NE']
    CCCCS_GenE_NE2050_NY = CCCCS_GenE_NE2050.loc[CCCCS_GenE_NE2050['region'] == 'NY']
    CCCCS_GenE_NE2050_PJM = CCCCS_GenE_NE2050.loc[CCCCS_GenE_NE2050['region'] == 'PJM']
    CCCCS_GenE_NE2050_SPP = CCCCS_GenE_NE2050.loc[CCCCS_GenE_NE2050['region'] == 'SPP']
    CT_GenE_NE2050_SERC = CT_GenE_NE2050.loc[CT_GenE_NE2050['region'] == 'SERC']
    CT_GenE_NE2050_MISO = CT_GenE_NE2050.loc[CT_GenE_NE2050['region'] == 'MISO']
    CT_GenE_NE2050_NE = CT_GenE_NE2050.loc[CT_GenE_NE2050['region'] == 'NE']
    CT_GenE_NE2050_NY = CT_GenE_NE2050.loc[CT_GenE_NE2050['region'] == 'NY']
    CT_GenE_NE2050_PJM = CT_GenE_NE2050.loc[CT_GenE_NE2050['region'] == 'PJM']
    CT_GenE_NE2050_SPP = CT_GenE_NE2050.loc[CT_GenE_NE2050['region'] == 'SPP']
    OG_GenE_NE2050_SERC = OG_GenE_NE2050.loc[OG_GenE_NE2050['region'] == 'SERC']
    OG_GenE_NE2050_MISO = OG_GenE_NE2050.loc[OG_GenE_NE2050['region'] == 'MISO']
    OG_GenE_NE2050_NE = OG_GenE_NE2050.loc[OG_GenE_NE2050['region'] == 'NE']
    OG_GenE_NE2050_NY = OG_GenE_NE2050.loc[OG_GenE_NE2050['region'] == 'NY']
    OG_GenE_NE2050_PJM = OG_GenE_NE2050.loc[OG_GenE_NE2050['region'] == 'PJM']
    OG_GenE_NE2050_SPP = OG_GenE_NE2050.loc[OG_GenE_NE2050['region'] == 'SPP']
    bio_GenE_NE2050_SERC = bio_GenE_NE2050.loc[bio_GenE_NE2050['region'] == 'SERC']
    bio_GenE_NE2050_MISO = bio_GenE_NE2050.loc[bio_GenE_NE2050['region'] == 'MISO']
    bio_GenE_NE2050_NE = bio_GenE_NE2050.loc[bio_GenE_NE2050['region'] == 'NE']
    bio_GenE_NE2050_NY = bio_GenE_NE2050.loc[bio_GenE_NE2050['region'] == 'NY']
    bio_GenE_NE2050_PJM = bio_GenE_NE2050.loc[bio_GenE_NE2050['region'] == 'PJM']
    bio_GenE_NE2050_SPP = bio_GenE_NE2050.loc[bio_GenE_NE2050['region'] == 'SPP']
    battery_GenE_NE2050_SERC = battery_GenE_NE2050.loc[battery_GenE_NE2050['region'] == 'SERC']
    battery_GenE_NE2050_MISO = battery_GenE_NE2050.loc[battery_GenE_NE2050['region'] == 'MISO']
    battery_GenE_NE2050_NE = battery_GenE_NE2050.loc[battery_GenE_NE2050['region'] == 'NE']
    battery_GenE_NE2050_NY = battery_GenE_NE2050.loc[battery_GenE_NE2050['region'] == 'NY']
    battery_GenE_NE2050_PJM = battery_GenE_NE2050.loc[battery_GenE_NE2050['region'] == 'PJM']
    battery_GenE_NE2050_SPP = battery_GenE_NE2050.loc[battery_GenE_NE2050['region'] == 'SPP']
    hydrogen_GenE_NE2050_SERC = hydrogen_GenE_NE2050.loc[hydrogen_GenE_NE2050['region'] == 'SERC']
    hydrogen_GenE_NE2050_MISO = hydrogen_GenE_NE2050.loc[hydrogen_GenE_NE2050['region'] == 'MISO']
    hydrogen_GenE_NE2050_NE = hydrogen_GenE_NE2050.loc[hydrogen_GenE_NE2050['region'] == 'NE']
    hydrogen_GenE_NE2050_NY = hydrogen_GenE_NE2050.loc[hydrogen_GenE_NE2050['region'] == 'NY']
    hydrogen_GenE_NE2050_PJM = hydrogen_GenE_NE2050.loc[hydrogen_GenE_NE2050['region'] == 'PJM']
    hydrogen_GenE_NE2050_SPP = hydrogen_GenE_NE2050.loc[hydrogen_GenE_NE2050['region'] == 'SPP']
    nuclear_GenE_NE2050_SERC = nuclear_GenE_NE2050.loc[nuclear_GenE_NE2050['region'] == 'SERC']
    nuclear_GenE_NE2050_MISO = nuclear_GenE_NE2050.loc[nuclear_GenE_NE2050['region'] == 'MISO']
    nuclear_GenE_NE2050_NE = nuclear_GenE_NE2050.loc[nuclear_GenE_NE2050['region'] == 'NE']
    nuclear_GenE_NE2050_NY = nuclear_GenE_NE2050.loc[nuclear_GenE_NE2050['region'] == 'NY']
    nuclear_GenE_NE2050_PJM = nuclear_GenE_NE2050.loc[nuclear_GenE_NE2050['region'] == 'PJM']
    nuclear_GenE_NE2050_SPP = nuclear_GenE_NE2050.loc[nuclear_GenE_NE2050['region'] == 'SPP']
    dac_GenE_NE2050_SERC = dac_GenE_NE2050.loc[dac_GenE_NE2050['region'] == 'SERC']
    dac_GenE_NE2050_MISO = dac_GenE_NE2050.loc[dac_GenE_NE2050['region'] == 'MISO']
    dac_GenE_NE2050_NE = dac_GenE_NE2050.loc[dac_GenE_NE2050['region'] == 'NE']
    dac_GenE_NE2050_NY = dac_GenE_NE2050.loc[dac_GenE_NE2050['region'] == 'NY']
    dac_GenE_NE2050_PJM = dac_GenE_NE2050.loc[dac_GenE_NE2050['region'] == 'PJM']
    dac_GenE_NE2050_SPP = dac_GenE_NE2050.loc[dac_GenE_NE2050['region'] == 'SPP']
    solarN_GenE_NE2050_SERC = solarN_GenE_NE2050.loc[solarN_GenE_NE2050['region'] == 'SERC']
    solarN_GenE_NE2050_MISO = solarN_GenE_NE2050.loc[solarN_GenE_NE2050['region'] == 'MISO']
    solarN_GenE_NE2050_NE = solarN_GenE_NE2050.loc[solarN_GenE_NE2050['region'] == 'NE']
    solarN_GenE_NE2050_NY = solarN_GenE_NE2050.loc[solarN_GenE_NE2050['region'] == 'NY']
    solarN_GenE_NE2050_PJM = solarN_GenE_NE2050.loc[solarN_GenE_NE2050['region'] == 'PJM']
    solarN_GenE_NE2050_SPP = solarN_GenE_NE2050.loc[solarN_GenE_NE2050['region'] == 'SPP']
    solarE_GenE_NE2050_SERC = solarE_GenE_NE2050.loc[solarE_GenE_NE2050['region'] == 'SERC']
    solarE_GenE_NE2050_MISO = solarE_GenE_NE2050.loc[solarE_GenE_NE2050['region'] == 'MISO']
    solarE_GenE_NE2050_NE = solarE_GenE_NE2050.loc[solarE_GenE_NE2050['region'] == 'NE']
    solarE_GenE_NE2050_NY = solarE_GenE_NE2050.loc[solarE_GenE_NE2050['region'] == 'NY']
    solarE_GenE_NE2050_PJM = solarE_GenE_NE2050.loc[solarE_GenE_NE2050['region'] == 'PJM']
    solarE_GenE_NE2050_SPP = solarE_GenE_NE2050.loc[solarE_GenE_NE2050['region'] == 'SPP']
    windN_GenE_NE2050_SERC = windN_GenE_NE2050.loc[windN_GenE_NE2050['region'] == 'SERC']
    windN_GenE_NE2050_MISO = windN_GenE_NE2050.loc[windN_GenE_NE2050['region'] == 'MISO']
    windN_GenE_NE2050_NE = windN_GenE_NE2050.loc[windN_GenE_NE2050['region'] == 'NE']
    windN_GenE_NE2050_NY = windN_GenE_NE2050.loc[windN_GenE_NE2050['region'] == 'NY']
    windN_GenE_NE2050_PJM = windN_GenE_NE2050.loc[windN_GenE_NE2050['region'] == 'PJM']
    windN_GenE_NE2050_SPP = windN_GenE_NE2050.loc[windN_GenE_NE2050['region'] == 'SPP']
    windE_GenE_NE2050_SERC = windE_GenE_NE2050.loc[windE_GenE_NE2050['region'] == 'SERC']
    windE_GenE_NE2050_MISO = windE_GenE_NE2050.loc[windE_GenE_NE2050['region'] == 'MISO']
    windE_GenE_NE2050_NE = windE_GenE_NE2050.loc[windE_GenE_NE2050['region'] == 'NE']
    windE_GenE_NE2050_NY = windE_GenE_NE2050.loc[windE_GenE_NE2050['region'] == 'NY']
    windE_GenE_NE2050_PJM = windE_GenE_NE2050.loc[windE_GenE_NE2050['region'] == 'PJM']
    windE_GenE_NE2050_SPP = windE_GenE_NE2050.loc[windE_GenE_NE2050['region'] == 'SPP']
    pump_GenE_NE2050_SERC = pump_GenE_NE2050.loc[pump_GenE_NE2050['region'] == 'SERC']
    pump_GenE_NE2050_MISO = pump_GenE_NE2050.loc[pump_GenE_NE2050['region'] == 'MISO']
    pump_GenE_NE2050_NE = pump_GenE_NE2050.loc[pump_GenE_NE2050['region'] == 'NE']
    pump_GenE_NE2050_NY = pump_GenE_NE2050.loc[pump_GenE_NE2050['region'] == 'NY']
    pump_GenE_NE2050_PJM = pump_GenE_NE2050.loc[pump_GenE_NE2050['region'] == 'PJM']
    pump_GenE_NE2050_SPP = pump_GenE_NE2050.loc[pump_GenE_NE2050['region'] == 'SPP']
    Other1_GenE_NE2050_SERC = Other1_GenE_NE2050.loc[Other1_GenE_NE2050['region'] == 'SERC']
    Other1_GenE_NE2050_MISO = Other1_GenE_NE2050.loc[Other1_GenE_NE2050['region'] == 'MISO']
    Other1_GenE_NE2050_NE = Other1_GenE_NE2050.loc[Other1_GenE_NE2050['region'] == 'NE']
    Other1_GenE_NE2050_NY = Other1_GenE_NE2050.loc[Other1_GenE_NE2050['region'] == 'NY']
    Other1_GenE_NE2050_PJM = Other1_GenE_NE2050.loc[Other1_GenE_NE2050['region'] == 'PJM']
    Other1_GenE_NE2050_SPP = Other1_GenE_NE2050.loc[Other1_GenE_NE2050['region'] == 'SPP']
    Other2_GenE_NE2050_SERC = Other2_GenE_NE2050.loc[Other2_GenE_NE2050['region'] == 'SERC']
    Other2_GenE_NE2050_MISO = Other2_GenE_NE2050.loc[Other2_GenE_NE2050['region'] == 'MISO']
    Other2_GenE_NE2050_NE = Other2_GenE_NE2050.loc[Other2_GenE_NE2050['region'] == 'NE']
    Other2_GenE_NE2050_NY = Other2_GenE_NE2050.loc[Other2_GenE_NE2050['region'] == 'NY']
    Other2_GenE_NE2050_PJM = Other2_GenE_NE2050.loc[Other2_GenE_NE2050['region'] == 'PJM']
    Other2_GenE_NE2050_SPP = Other2_GenE_NE2050.loc[Other2_GenE_NE2050['region'] == 'SPP']
    Other3_GenE_NE2050_SERC = Other3_GenE_NE2050.loc[Other3_GenE_NE2050['region'] == 'SERC']
    Other3_GenE_NE2050_MISO = Other3_GenE_NE2050.loc[Other3_GenE_NE2050['region'] == 'MISO']
    Other3_GenE_NE2050_NE = Other3_GenE_NE2050.loc[Other3_GenE_NE2050['region'] == 'NE']
    Other3_GenE_NE2050_NY = Other3_GenE_NE2050.loc[Other3_GenE_NE2050['region'] == 'NY']
    Other3_GenE_NE2050_PJM = Other3_GenE_NE2050.loc[Other3_GenE_NE2050['region'] == 'PJM']
    Other3_GenE_NE2050_SPP = Other3_GenE_NE2050.loc[Other3_GenE_NE2050['region'] == 'SPP']
    Other4_GenE_NE2050_SERC = Other4_GenE_NE2050.loc[Other4_GenE_NE2050['region'] == 'SERC']
    Other4_GenE_NE2050_MISO = Other4_GenE_NE2050.loc[Other4_GenE_NE2050['region'] == 'MISO']
    Other4_GenE_NE2050_NE = Other4_GenE_NE2050.loc[Other4_GenE_NE2050['region'] == 'NE']
    Other4_GenE_NE2050_NY = Other4_GenE_NE2050.loc[Other4_GenE_NE2050['region'] == 'NY']
    Other4_GenE_NE2050_PJM = Other4_GenE_NE2050.loc[Other4_GenE_NE2050['region'] == 'PJM']
    Other4_GenE_NE2050_SPP = Other4_GenE_NE2050.loc[Other4_GenE_NE2050['region'] == 'SPP']
    Other5_GenE_NE2050_SERC = Other5_GenE_NE2050.loc[Other5_GenE_NE2050['region'] == 'SERC']
    Other5_GenE_NE2050_MISO = Other5_GenE_NE2050.loc[Other5_GenE_NE2050['region'] == 'MISO']
    Other5_GenE_NE2050_NE = Other5_GenE_NE2050.loc[Other5_GenE_NE2050['region'] == 'NE']
    Other5_GenE_NE2050_NY = Other5_GenE_NE2050.loc[Other5_GenE_NE2050['region'] == 'NY']
    Other5_GenE_NE2050_PJM = Other5_GenE_NE2050.loc[Other5_GenE_NE2050['region'] == 'PJM']
    Other5_GenE_NE2050_SPP = Other5_GenE_NE2050.loc[Other5_GenE_NE2050['region'] == 'SPP']
    Other6_GenE_NE2050_SERC = Other6_GenE_NE2050.loc[Other6_GenE_NE2050['region'] == 'SERC']
    Other6_GenE_NE2050_MISO = Other6_GenE_NE2050.loc[Other6_GenE_NE2050['region'] == 'MISO']
    Other6_GenE_NE2050_NE = Other6_GenE_NE2050.loc[Other6_GenE_NE2050['region'] == 'NE']
    Other6_GenE_NE2050_NY = Other6_GenE_NE2050.loc[Other6_GenE_NE2050['region'] == 'NY']
    Other6_GenE_NE2050_PJM = Other6_GenE_NE2050.loc[Other6_GenE_NE2050['region'] == 'PJM']
    Other6_GenE_NE2050_SPP = Other6_GenE_NE2050.loc[Other6_GenE_NE2050['region'] == 'SPP']
    Other7_GenE_NE2050_SERC = Other7_GenE_NE2050.loc[Other7_GenE_NE2050['region'] == 'SERC']
    Other7_GenE_NE2050_MISO = Other7_GenE_NE2050.loc[Other7_GenE_NE2050['region'] == 'MISO']
    Other7_GenE_NE2050_NE = Other7_GenE_NE2050.loc[Other7_GenE_NE2050['region'] == 'NE']
    Other7_GenE_NE2050_NY = Other7_GenE_NE2050.loc[Other7_GenE_NE2050['region'] == 'NY']
    Other7_GenE_NE2050_PJM = Other7_GenE_NE2050.loc[Other7_GenE_NE2050['region'] == 'PJM']
    Other7_GenE_NE2050_SPP = Other7_GenE_NE2050.loc[Other7_GenE_NE2050['region'] == 'SPP']
    Other8_GenE_NE2050_SERC = Other8_GenE_NE2050.loc[Other8_GenE_NE2050['region'] == 'SERC']
    Other8_GenE_NE2050_MISO = Other8_GenE_NE2050.loc[Other8_GenE_NE2050['region'] == 'MISO']
    Other8_GenE_NE2050_NE = Other8_GenE_NE2050.loc[Other8_GenE_NE2050['region'] == 'NE']
    Other8_GenE_NE2050_NY = Other8_GenE_NE2050.loc[Other8_GenE_NE2050['region'] == 'NY']
    Other8_GenE_NE2050_PJM = Other8_GenE_NE2050.loc[Other8_GenE_NE2050['region'] == 'PJM']
    Other8_GenE_NE2050_SPP = Other8_GenE_NE2050.loc[Other8_GenE_NE2050['region'] == 'SPP']

    Coal_GenE_NE2050 = Coal_GenE_NE2050['Total Gen'].sum()
    CCCCS_GenE_NE2050 = CCCCS_GenE_NE2050['Total Gen'].sum()
    CC_GenE_NE2050 = CC_GenE_NE2050['Total Gen'].sum()
    CT_GenE_NE2050 = CT_GenE_NE2050['Total Gen'].sum()
    OG_GenE_NE2050 = OG_GenE_NE2050['Total Gen'].sum()
    bio_GenE_NE2050 = bio_GenE_NE2050['Total Gen'].sum()
    battery_GenE_NE2050 = battery_GenE_NE2050['Total Gen'].sum()
    hydrogen_GenE_NE2050 = hydrogen_GenE_NE2050['Total Gen'].sum()
    nuclear_GenE_NE2050 = nuclear_GenE_NE2050['Total Gen'].sum()
    pump_GenE_NE2050 = pump_GenE_NE2050['Total Gen'].sum()
    solar_GenE_NE2050 = solarN_GenE_NE2050['Total Gen'].sum() + solarE_GenE_NE2050['Total Gen'].sum()
    wind_GenE_NE2050 = windN_GenE_NE2050['Total Gen'].sum() + windE_GenE_NE2050['Total Gen'].sum()
    dac_GenE_NE2050 = dac_GenE_NE2050['Total Gen'].sum()
    Others_GenE_NE2050 = Other3_GenE_NE2050['Total Gen'].sum() + Other4_GenE_NE2050['Total Gen'].sum() \
                         + Other5_GenE_NE2050['Total Gen'].sum() + Other6_GenE_NE2050['Total Gen'].sum() \
                         + Other7_GenE_NE2050['Total Gen'].sum() + Other8_GenE_NE2050['Total Gen'].sum()

    Coal_GenE_NE2050_SERC = Coal_GenE_NE2050_SERC['Total Gen'].sum()
    CCCCS_GenE_NE2050_SERC = CCCCS_GenE_NE2050_SERC['Total Gen'].sum()
    CC_GenE_NE2050_SERC = CC_GenE_NE2050_SERC['Total Gen'].sum()
    CT_GenE_NE2050_SERC = CT_GenE_NE2050_SERC['Total Gen'].sum()
    OG_GenE_NE2050_SERC = OG_GenE_NE2050_SERC['Total Gen'].sum()
    bio_GenE_NE2050_SERC = bio_GenE_NE2050_SERC['Total Gen'].sum()
    battery_GenE_NE2050_SERC = battery_GenE_NE2050_SERC['Total Gen'].sum()
    hydrogen_GenE_NE2050_SERC = hydrogen_GenE_NE2050_SERC['Total Gen'].sum()
    nuclear_GenE_NE2050_SERC = nuclear_GenE_NE2050_SERC['Total Gen'].sum()
    pump_GenE_NE2050_SERC = pump_GenE_NE2050_SERC['Total Gen'].sum()
    solar_GenE_NE2050_SERC = solarN_GenE_NE2050_SERC['Total Gen'].sum() + solarE_GenE_NE2050_SERC['Total Gen'].sum()
    wind_GenE_NE2050_SERC = windN_GenE_NE2050_SERC['Total Gen'].sum() + windE_GenE_NE2050_SERC['Total Gen'].sum()
    dac_GenE_NE2050_SERC = dac_GenE_NE2050_SERC['Total Gen'].sum()
    Others_GenE_NE2050_SERC = Other1_GenE_NE2050_SERC['Total Gen'].sum() + Other2_GenE_NE2050_SERC['Total Gen'].sum() \
                              + Other3_GenE_NE2050_SERC['Total Gen'].sum() + Other4_GenE_NE2050_SERC['Total Gen'].sum() \
                              + Other5_GenE_NE2050_SERC['Total Gen'].sum() + Other6_GenE_NE2050_SERC['Total Gen'].sum() \
                              + Other7_GenE_NE2050_SERC['Total Gen'].sum() + Other8_GenE_NE2050_SERC['Total Gen'].sum()
    Coal_GenE_NE2050_MISO = Coal_GenE_NE2050_MISO['Total Gen'].sum()
    CCCCS_GenE_NE2050_MISO = CCCCS_GenE_NE2050_MISO['Total Gen'].sum()
    CC_GenE_NE2050_MISO = CC_GenE_NE2050_MISO['Total Gen'].sum()
    CT_GenE_NE2050_MISO = CT_GenE_NE2050_MISO['Total Gen'].sum()
    OG_GenE_NE2050_MISO = OG_GenE_NE2050_MISO['Total Gen'].sum()
    bio_GenE_NE2050_MISO = bio_GenE_NE2050_MISO['Total Gen'].sum()
    battery_GenE_NE2050_MISO = battery_GenE_NE2050_MISO['Total Gen'].sum()
    hydrogen_GenE_NE2050_MISO = hydrogen_GenE_NE2050_MISO['Total Gen'].sum()
    nuclear_GenE_NE2050_MISO = nuclear_GenE_NE2050_MISO['Total Gen'].sum()
    pump_GenE_NE2050_MISO = pump_GenE_NE2050_MISO['Total Gen'].sum()
    solar_GenE_NE2050_MISO = solarN_GenE_NE2050_MISO['Total Gen'].sum() + solarE_GenE_NE2050_MISO['Total Gen'].sum()
    wind_GenE_NE2050_MISO = windN_GenE_NE2050_MISO['Total Gen'].sum() + windE_GenE_NE2050_MISO['Total Gen'].sum()
    dac_GenE_NE2050_MISO = dac_GenE_NE2050_MISO['Total Gen'].sum()
    Others_GenE_NE2050_MISO = Other1_GenE_NE2050_MISO['Total Gen'].sum() + Other2_GenE_NE2050_MISO['Total Gen'].sum() \
                              + Other3_GenE_NE2050_MISO['Total Gen'].sum() + Other4_GenE_NE2050_MISO['Total Gen'].sum() \
                              + Other5_GenE_NE2050_MISO['Total Gen'].sum() + Other6_GenE_NE2050_MISO['Total Gen'].sum() \
                              + Other7_GenE_NE2050_MISO['Total Gen'].sum() + Other8_GenE_NE2050_MISO['Total Gen'].sum()
    Coal_GenE_NE2050_NE = Coal_GenE_NE2050_NE['Total Gen'].sum()
    CCCCS_GenE_NE2050_NE = CCCCS_GenE_NE2050_NE['Total Gen'].sum()
    CC_GenE_NE2050_NE = CC_GenE_NE2050_NE['Total Gen'].sum()
    CT_GenE_NE2050_NE = CT_GenE_NE2050_NE['Total Gen'].sum()
    OG_GenE_NE2050_NE = OG_GenE_NE2050_NE['Total Gen'].sum()
    bio_GenE_NE2050_NE = bio_GenE_NE2050_NE['Total Gen'].sum()
    battery_GenE_NE2050_NE = battery_GenE_NE2050_NE['Total Gen'].sum()
    hydrogen_GenE_NE2050_NE = hydrogen_GenE_NE2050_NE['Total Gen'].sum()
    nuclear_GenE_NE2050_NE = nuclear_GenE_NE2050_NE['Total Gen'].sum()
    pump_GenE_NE2050_NE = pump_GenE_NE2050_NE['Total Gen'].sum()
    solar_GenE_NE2050_NE = solarN_GenE_NE2050_NE['Total Gen'].sum() + solarE_GenE_NE2050_NE['Total Gen'].sum()
    wind_GenE_NE2050_NE = windN_GenE_NE2050_NE['Total Gen'].sum() + windE_GenE_NE2050_NE['Total Gen'].sum()
    dac_GenE_NE2050_NE = dac_GenE_NE2050_NE['Total Gen'].sum()
    Others_GenE_NE2050_NE = Other1_GenE_NE2050_NE['Total Gen'].sum() + Other2_GenE_NE2050_NE['Total Gen'].sum() \
                            + Other3_GenE_NE2050_NE['Total Gen'].sum() + Other4_GenE_NE2050_NE['Total Gen'].sum() \
                            + Other5_GenE_NE2050_NE['Total Gen'].sum() + Other6_GenE_NE2050_NE['Total Gen'].sum() \
                            + Other7_GenE_NE2050_NE['Total Gen'].sum() + Other8_GenE_NE2050_NE['Total Gen'].sum()
    Coal_GenE_NE2050_NY = Coal_GenE_NE2050_NY['Total Gen'].sum()
    CCCCS_GenE_NE2050_NY = CCCCS_GenE_NE2050_NY['Total Gen'].sum()
    CC_GenE_NE2050_NY = CC_GenE_NE2050_NY['Total Gen'].sum()
    CT_GenE_NE2050_NY = CT_GenE_NE2050_NY['Total Gen'].sum()
    OG_GenE_NE2050_NY = OG_GenE_NE2050_NY['Total Gen'].sum()
    bio_GenE_NE2050_NY = bio_GenE_NE2050_NY['Total Gen'].sum()
    battery_GenE_NE2050_NY = battery_GenE_NE2050_NY['Total Gen'].sum()
    hydrogen_GenE_NE2050_NY = hydrogen_GenE_NE2050_NY['Total Gen'].sum()
    nuclear_GenE_NE2050_NY = nuclear_GenE_NE2050_NY['Total Gen'].sum()
    pump_GenE_NE2050_NY = pump_GenE_NE2050_NY['Total Gen'].sum()
    solar_GenE_NE2050_NY = solarN_GenE_NE2050_NY['Total Gen'].sum() + solarE_GenE_NE2050_NY['Total Gen'].sum()
    wind_GenE_NE2050_NY = windN_GenE_NE2050_NY['Total Gen'].sum() + windE_GenE_NE2050_NY['Total Gen'].sum()
    dac_GenE_NE2050_NY = dac_GenE_NE2050_NY['Total Gen'].sum()
    Others_GenE_NE2050_NY = Other1_GenE_NE2050_NY['Total Gen'].sum() + Other2_GenE_NE2050_NY['Total Gen'].sum() \
                            + Other3_GenE_NE2050_NY['Total Gen'].sum() + Other4_GenE_NE2050_NY['Total Gen'].sum() \
                            + Other5_GenE_NE2050_NY['Total Gen'].sum() + Other6_GenE_NE2050_NY['Total Gen'].sum() \
                            + Other7_GenE_NE2050_NY['Total Gen'].sum() + Other8_GenE_NE2050_NY['Total Gen'].sum()
    Coal_GenE_NE2050_PJM = Coal_GenE_NE2050_PJM['Total Gen'].sum()
    CCCCS_GenE_NE2050_PJM = CCCCS_GenE_NE2050_PJM['Total Gen'].sum()
    CC_GenE_NE2050_PJM = CC_GenE_NE2050_PJM['Total Gen'].sum()
    CT_GenE_NE2050_PJM = CT_GenE_NE2050_PJM['Total Gen'].sum()
    OG_GenE_NE2050_PJM = OG_GenE_NE2050_PJM['Total Gen'].sum()
    bio_GenE_NE2050_PJM = bio_GenE_NE2050_PJM['Total Gen'].sum()
    battery_GenE_NE2050_PJM = battery_GenE_NE2050_PJM['Total Gen'].sum()
    hydrogen_GenE_NE2050_PJM = hydrogen_GenE_NE2050_PJM['Total Gen'].sum()
    nuclear_GenE_NE2050_PJM = nuclear_GenE_NE2050_PJM['Total Gen'].sum()
    pump_GenE_NE2050_PJM = pump_GenE_NE2050_PJM['Total Gen'].sum()
    solar_GenE_NE2050_PJM = solarN_GenE_NE2050_PJM['Total Gen'].sum() + solarE_GenE_NE2050_PJM['Total Gen'].sum()
    wind_GenE_NE2050_PJM = windN_GenE_NE2050_PJM['Total Gen'].sum() + windE_GenE_NE2050_PJM['Total Gen'].sum()
    dac_GenE_NE2050_PJM = dac_GenE_NE2050_PJM['Total Gen'].sum()
    Others_GenE_NE2050_PJM = Other1_GenE_NE2050_PJM['Total Gen'].sum() + Other2_GenE_NE2050_PJM['Total Gen'].sum() \
                             + Other3_GenE_NE2050_PJM['Total Gen'].sum() + Other4_GenE_NE2050_PJM['Total Gen'].sum() \
                             + Other5_GenE_NE2050_PJM['Total Gen'].sum() + Other6_GenE_NE2050_PJM['Total Gen'].sum() \
                             + Other7_GenE_NE2050_PJM['Total Gen'].sum() + Other8_GenE_NE2050_PJM['Total Gen'].sum()
    Coal_GenE_NE2050_SPP = Coal_GenE_NE2050_SPP['Total Gen'].sum()
    CCCCS_GenE_NE2050_SPP = CCCCS_GenE_NE2050_SPP['Total Gen'].sum()
    CC_GenE_NE2050_SPP = CC_GenE_NE2050_SPP['Total Gen'].sum()
    CT_GenE_NE2050_SPP = CT_GenE_NE2050_SPP['Total Gen'].sum()
    OG_GenE_NE2050_SPP = OG_GenE_NE2050_SPP['Total Gen'].sum()
    bio_GenE_NE2050_SPP = bio_GenE_NE2050_SPP['Total Gen'].sum()
    battery_GenE_NE2050_SPP = battery_GenE_NE2050_SPP['Total Gen'].sum()
    hydrogen_GenE_NE2050_SPP = hydrogen_GenE_NE2050_SPP['Total Gen'].sum()
    nuclear_GenE_NE2050_SPP = nuclear_GenE_NE2050_SPP['Total Gen'].sum()
    pump_GenE_NE2050_SPP = pump_GenE_NE2050_SPP['Total Gen'].sum()
    solar_GenE_NE2050_SPP = solarN_GenE_NE2050_SPP['Total Gen'].sum() + solarE_GenE_NE2050_SPP['Total Gen'].sum()
    wind_GenE_NE2050_SPP = windN_GenE_NE2050_SPP['Total Gen'].sum() + windE_GenE_NE2050_SPP['Total Gen'].sum()
    dac_GenE_NE2050_SPP = dac_GenE_NE2050_SPP['Total Gen'].sum()
    Others_GenE_NE2050_SPP = Other1_GenE_NE2050_SPP['Total Gen'].sum() + Other2_GenE_NE2050_SPP['Total Gen'].sum() \
                             + Other3_GenE_NE2050_SPP['Total Gen'].sum() + Other4_GenE_NE2050_SPP['Total Gen'].sum() \
                             + Other5_GenE_NE2050_SPP['Total Gen'].sum() + Other6_GenE_NE2050_SPP['Total Gen'].sum() \
                             + Other7_GenE_NE2050_SPP['Total Gen'].sum() + Other8_GenE_NE2050_SPP['Total Gen'].sum()

    # New:
    resultsGenN_NZ = pd.read_csv(m_dir2 + resultsDir_other_NZ + 'vGentechCE2050.csv')
    resultsGenN_NE2020 = pd.read_csv(m_dir2 + resultsDir_other_NE2020 + 'vGentechCE2050.csv')
    resultsGenN_NE2030 = pd.read_csv(m_dir2 + resultsDir_other_NE2030 + 'vGentechCE2050.csv')
    resultsGenN_NE2040 = pd.read_csv(m_dir2 + resultsDir_other_NE2040 + 'vGentechCE2050.csv')
    resultsGenN_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'vGentechCE2060.csv')

    resultsGenN_NZ.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NZ = resultsGenN_NZ.T
    resultsGenN_NZ.columns = resultsGenN_NZ.iloc[0]
    resultsGenN_NZ = resultsGenN_NZ.drop(resultsGenN_NZ.index[0])
    resultsGenN_NZ = resultsGenN_NZ.reset_index()
    resultsGenN_NZ.rename(columns={'index': 'GAMS Symbol'}, inplace=True)
    resultsGenN_NZ['Total Gen'] = resultsGenN_NZ.iloc[:, 1:].sum(axis=1)
    resultsGenN_NZ = resultsGenN_NZ[['Total Gen', 'GAMS Symbol']]

    resultsGenN_NE2020.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2020 = resultsGenN_NE2020.T
    resultsGenN_NE2020.columns = resultsGenN_NE2020.iloc[0]
    resultsGenN_NE2020 = resultsGenN_NE2020.drop(resultsGenN_NE2020.index[0])
    resultsGenN_NE2020 = resultsGenN_NE2020.reset_index()
    resultsGenN_NE2020.rename(columns={'index': 'GAMS Symbol'}, inplace=True)
    resultsGenN_NE2020['Total Gen'] = resultsGenN_NE2020.iloc[:, 1:].sum(axis=1)
    resultsGenN_NE2020 = resultsGenN_NE2020[['Total Gen', 'GAMS Symbol']]

    resultsGenN_NE2030.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2030 = resultsGenN_NE2030.T
    resultsGenN_NE2030.columns = resultsGenN_NE2030.iloc[0]
    resultsGenN_NE2030 = resultsGenN_NE2030.drop(resultsGenN_NE2030.index[0])
    resultsGenN_NE2030 = resultsGenN_NE2030.reset_index()
    resultsGenN_NE2030.rename(columns={'index': 'GAMS Symbol'}, inplace=True)
    resultsGenN_NE2030['Total Gen'] = resultsGenN_NE2030.iloc[:, 1:].sum(axis=1)
    resultsGenN_NE2030 = resultsGenN_NE2030[['Total Gen', 'GAMS Symbol']]

    resultsGenN_NE2040.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2040 = resultsGenN_NE2040.T
    resultsGenN_NE2040.columns = resultsGenN_NE2040.iloc[0]
    resultsGenN_NE2040 = resultsGenN_NE2040.drop(resultsGenN_NE2040.index[0])
    resultsGenN_NE2040 = resultsGenN_NE2040.reset_index()
    resultsGenN_NE2040.rename(columns={'index': 'GAMS Symbol'}, inplace=True)
    resultsGenN_NE2040['Total Gen'] = resultsGenN_NE2040.iloc[:, 1:].sum(axis=1)
    resultsGenN_NE2040 = resultsGenN_NE2040[['Total Gen', 'GAMS Symbol']]

    resultsGenN_NE2050.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2050 = resultsGenN_NE2050.T
    resultsGenN_NE2050.columns = resultsGenN_NE2050.iloc[0]
    resultsGenN_NE2050 = resultsGenN_NE2050.drop(resultsGenN_NE2050.index[0])
    resultsGenN_NE2050 = resultsGenN_NE2050.reset_index()
    resultsGenN_NE2050.rename(columns={'index': 'GAMS Symbol'}, inplace=True)
    resultsGenN_NE2050['Total Gen'] = resultsGenN_NE2050.iloc[:, 1:].sum(axis=1)
    resultsGenN_NE2050 = resultsGenN_NE2050[['Total Gen', 'GAMS Symbol']]

    CoalCCS_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CC_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Combined Cycle')]
    CCCCS_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    battery_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Hydrogen')]
    nuclear_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Nuclear')]
    dac_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NZ = resultsGenN_NZ[resultsGenN_NZ['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NZ = resultsGenN_NZ[resultsGenN_NZ['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NZ_MISO = CoalCCS_GenN_NZ.loc[CoalCCS_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    battery_GenN_NZ_MISO = battery_GenN_NZ.loc[battery_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    hydrogen_GenN_NZ_MISO = hydrogen_GenN_NZ.loc[hydrogen_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    CoalCCS_GenN_NZ_SERC = CoalCCS_GenN_NZ.loc[CoalCCS_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    battery_GenN_NZ_SERC = battery_GenN_NZ.loc[battery_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    hydrogen_GenN_NZ_SERC = hydrogen_GenN_NZ.loc[hydrogen_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    CoalCCS_GenN_NZ_NE = CoalCCS_GenN_NZ.loc[CoalCCS_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    battery_GenN_NZ_NE = battery_GenN_NZ.loc[battery_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    hydrogen_GenN_NZ_NE = hydrogen_GenN_NZ.loc[hydrogen_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    CoalCCS_GenN_NZ_NY = CoalCCS_GenN_NZ.loc[CoalCCS_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    battery_GenN_NZ_NY = battery_GenN_NZ.loc[battery_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    hydrogen_GenN_NZ_NY = hydrogen_GenN_NZ.loc[hydrogen_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    CoalCCS_GenN_NZ_PJM = CoalCCS_GenN_NZ.loc[CoalCCS_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    battery_GenN_NZ_PJM = battery_GenN_NZ.loc[battery_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    hydrogen_GenN_NZ_PJM = hydrogen_GenN_NZ.loc[hydrogen_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    CoalCCS_GenN_NZ_SPP = CoalCCS_GenN_NZ.loc[CoalCCS_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    battery_GenN_NZ_SPP = battery_GenN_NZ.loc[battery_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    hydrogen_GenN_NZ_SPP = hydrogen_GenN_NZ.loc[hydrogen_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    CoalCCS_GenN_NZ = CoalCCS_GenN_NZ['Total Gen'].sum()
    battery_GenN_NZ = battery_GenN_NZ['Total Gen'].sum()
    hydrogen_GenN_NZ = hydrogen_GenN_NZ['Total Gen'].sum()

    CC_GenN_NZ_MISO = CC_GenN_NZ.loc[CC_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    CC_GenN_NZ_NE = CC_GenN_NZ.loc[CC_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    CC_GenN_NZ_NY = CC_GenN_NZ.loc[CC_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    CC_GenN_NZ_PJM = CC_GenN_NZ.loc[CC_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    CC_GenN_NZ_SERC = CC_GenN_NZ.loc[CC_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    CC_GenN_NZ_SPP = CC_GenN_NZ.loc[CC_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    CCCCS_GenN_NZ_MISO = CCCCS_GenN_NZ.loc[CCCCS_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    CCCCS_GenN_NZ_NE = CCCCS_GenN_NZ.loc[CCCCS_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    CCCCS_GenN_NZ_NY = CCCCS_GenN_NZ.loc[CCCCS_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    CCCCS_GenN_NZ_PJM = CCCCS_GenN_NZ.loc[CCCCS_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    CCCCS_GenN_NZ_SERC = CCCCS_GenN_NZ.loc[CCCCS_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    CCCCS_GenN_NZ_SPP = CCCCS_GenN_NZ.loc[CCCCS_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    nuclear_GenN_NZ_MISO = nuclear_GenN_NZ.loc[nuclear_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    nuclear_GenN_NZ_NE = nuclear_GenN_NZ.loc[nuclear_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    nuclear_GenN_NZ_NY = nuclear_GenN_NZ.loc[nuclear_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    nuclear_GenN_NZ_PJM = nuclear_GenN_NZ.loc[nuclear_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    nuclear_GenN_NZ_SERC = nuclear_GenN_NZ.loc[nuclear_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    nuclear_GenN_NZ_SPP = nuclear_GenN_NZ.loc[nuclear_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    solar_GenN_NZ_MISO = solar_GenN_NZ.loc[solar_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    solar_GenN_NZ_NE = solar_GenN_NZ.loc[solar_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    solar_GenN_NZ_NY = solar_GenN_NZ.loc[solar_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    solar_GenN_NZ_PJM = solar_GenN_NZ.loc[solar_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    solar_GenN_NZ_SERC = solar_GenN_NZ.loc[solar_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    solar_GenN_NZ_SPP = solar_GenN_NZ.loc[solar_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    wind_GenN_NZ_MISO = wind_GenN_NZ.loc[wind_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    wind_GenN_NZ_NE = wind_GenN_NZ.loc[wind_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    wind_GenN_NZ_NY = wind_GenN_NZ.loc[wind_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    wind_GenN_NZ_PJM = wind_GenN_NZ.loc[wind_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    wind_GenN_NZ_SERC = wind_GenN_NZ.loc[wind_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    wind_GenN_NZ_SPP = wind_GenN_NZ.loc[wind_GenN_NZ['GAMS Symbol'].str.contains('SPP')]
    dac_GenN_NZ_MISO = dac_GenN_NZ.loc[dac_GenN_NZ['GAMS Symbol'].str.contains('MISO')]
    dac_GenN_NZ_NE = dac_GenN_NZ.loc[dac_GenN_NZ['GAMS Symbol'].str.contains('NE')]
    dac_GenN_NZ_NY = dac_GenN_NZ.loc[dac_GenN_NZ['GAMS Symbol'].str.contains('NY')]
    dac_GenN_NZ_PJM = dac_GenN_NZ.loc[dac_GenN_NZ['GAMS Symbol'].str.contains('PJM')]
    dac_GenN_NZ_SERC = dac_GenN_NZ.loc[dac_GenN_NZ['GAMS Symbol'].str.contains('SERC')]
    dac_GenN_NZ_SPP = dac_GenN_NZ.loc[dac_GenN_NZ['GAMS Symbol'].str.contains('SPP')]

    CoalCCS_GenN_NZ_SERC = CoalCCS_GenN_NZ_SERC['Total Gen'].sum()
    battery_GenN_NZ_SERC = battery_GenN_NZ_SERC['Total Gen'].sum()
    hydrogen_GenN_NZ_SERC = hydrogen_GenN_NZ_SERC['Total Gen'].sum()
    CoalCCS_GenN_NZ_NY = CoalCCS_GenN_NZ_NY['Total Gen'].sum()
    battery_GenN_NZ_NY = battery_GenN_NZ_NY['Total Gen'].sum()
    hydrogen_GenN_NZ_NY = hydrogen_GenN_NZ_NY['Total Gen'].sum()
    CoalCCS_GenN_NZ_MISO = CoalCCS_GenN_NZ_MISO['Total Gen'].sum()
    battery_GenN_NZ_MISO = battery_GenN_NZ_MISO['Total Gen'].sum()
    hydrogen_GenN_NZ_MISO = hydrogen_GenN_NZ_MISO['Total Gen'].sum()
    CoalCCS_GenN_NZ_PJM = CoalCCS_GenN_NZ_PJM['Total Gen'].sum()
    battery_GenN_NZ_PJM = battery_GenN_NZ_PJM['Total Gen'].sum()
    hydrogen_GenN_NZ_PJM = hydrogen_GenN_NZ_PJM['Total Gen'].sum()
    CoalCCS_GenN_NZ_SPP = CoalCCS_GenN_NZ_SPP['Total Gen'].sum()
    battery_GenN_NZ_SPP = battery_GenN_NZ_SPP['Total Gen'].sum()
    hydrogen_GenN_NZ_SPP = hydrogen_GenN_NZ_SPP['Total Gen'].sum()
    CoalCCS_GenN_NZ_NE = CoalCCS_GenN_NZ_NE['Total Gen'].sum()
    battery_GenN_NZ_NE = battery_GenN_NZ_NE['Total Gen'].sum()
    hydrogen_GenN_NZ_NE = hydrogen_GenN_NZ_NE['Total Gen'].sum()

    CCCCS_GenN_NZ_MISO = CCCCS_GenN_NZ_MISO['Total Gen'].sum()
    CCCCS_GenN_NZ_NE = CCCCS_GenN_NZ_NE['Total Gen'].sum()
    CCCCS_GenN_NZ_NY = CCCCS_GenN_NZ_NY['Total Gen'].sum()
    CCCCS_GenN_NZ_PJM = CCCCS_GenN_NZ_PJM['Total Gen'].sum()
    CCCCS_GenN_NZ_SERC = CCCCS_GenN_NZ_SERC['Total Gen'].sum()
    CCCCS_GenN_NZ_SPP = CCCCS_GenN_NZ_SPP['Total Gen'].sum()
    CC_GenN_NZ_MISO = CC_GenN_NZ_MISO['Total Gen'].sum() - CCCCS_GenN_NZ_MISO
    CC_GenN_NZ_NE = CC_GenN_NZ_NE['Total Gen'].sum() - CCCCS_GenN_NZ_NE
    CC_GenN_NZ_NY = CC_GenN_NZ_NY['Total Gen'].sum() - CCCCS_GenN_NZ_NY
    CC_GenN_NZ_PJM = CC_GenN_NZ_PJM['Total Gen'].sum() - CCCCS_GenN_NZ_PJM
    CC_GenN_NZ_SERC = CC_GenN_NZ_SERC['Total Gen'].sum() - CCCCS_GenN_NZ_SERC
    CC_GenN_NZ_SPP = CC_GenN_NZ_SPP['Total Gen'].sum() - CCCCS_GenN_NZ_SPP
    nuclear_GenN_NZ_MISO = nuclear_GenN_NZ_MISO['Total Gen'].sum()
    nuclear_GenN_NZ_NE = nuclear_GenN_NZ_NE['Total Gen'].sum()
    nuclear_GenN_NZ_NY = nuclear_GenN_NZ_NY['Total Gen'].sum()
    nuclear_GenN_NZ_PJM = nuclear_GenN_NZ_PJM['Total Gen'].sum()
    nuclear_GenN_NZ_SERC = nuclear_GenN_NZ_SERC['Total Gen'].sum()
    nuclear_GenN_NZ_SPP = nuclear_GenN_NZ_SPP['Total Gen'].sum()
    solar_GenN_NZ_MISO = solar_GenN_NZ_MISO['Total Gen'].sum()
    solar_GenN_NZ_NE = solar_GenN_NZ_NE['Total Gen'].sum()
    solar_GenN_NZ_NY = solar_GenN_NZ_NY['Total Gen'].sum()
    solar_GenN_NZ_PJM = solar_GenN_NZ_PJM['Total Gen'].sum()
    solar_GenN_NZ_SERC = solar_GenN_NZ_SERC['Total Gen'].sum()
    solar_GenN_NZ_SPP = solar_GenN_NZ_SPP['Total Gen'].sum()
    wind_GenN_NZ_MISO = wind_GenN_NZ_MISO['Total Gen'].sum()
    wind_GenN_NZ_NE = wind_GenN_NZ_NE['Total Gen'].sum()
    wind_GenN_NZ_NY = wind_GenN_NZ_NY['Total Gen'].sum()
    wind_GenN_NZ_PJM = wind_GenN_NZ_PJM['Total Gen'].sum()
    wind_GenN_NZ_SERC = wind_GenN_NZ_SERC['Total Gen'].sum()
    wind_GenN_NZ_SPP = wind_GenN_NZ_SPP['Total Gen'].sum()
    dac_GenN_NZ_MISO = dac_GenN_NZ_MISO['Total Gen'].sum()
    dac_GenN_NZ_NE = dac_GenN_NZ_NE['Total Gen'].sum()
    dac_GenN_NZ_NY = dac_GenN_NZ_NY['Total Gen'].sum()
    dac_GenN_NZ_PJM = dac_GenN_NZ_PJM['Total Gen'].sum()
    dac_GenN_NZ_SERC = dac_GenN_NZ_SERC['Total Gen'].sum()
    dac_GenN_NZ_SPP = dac_GenN_NZ_SPP['Total Gen'].sum()

    CC_GenN_NZ = CC_GenN_NZ_MISO + CC_GenN_NZ_NE + CC_GenN_NZ_NY + CC_GenN_NZ_PJM + CC_GenN_NZ_SERC + CC_GenN_NZ_SPP
    CCCCS_GenN_NZ = CCCCS_GenN_NZ_MISO + CCCCS_GenN_NZ_NE + CCCCS_GenN_NZ_NY + CCCCS_GenN_NZ_PJM + CCCCS_GenN_NZ_SERC + CCCCS_GenN_NZ_SPP
    nuclear_GenN_NZ = nuclear_GenN_NZ_MISO + nuclear_GenN_NZ_NE + nuclear_GenN_NZ_NY + nuclear_GenN_NZ_PJM + nuclear_GenN_NZ_SERC + nuclear_GenN_NZ_SPP
    wind_GenN_NZ = wind_GenN_NZ_MISO + wind_GenN_NZ_NE + wind_GenN_NZ_NY + wind_GenN_NZ_PJM + wind_GenN_NZ_SERC + wind_GenN_NZ_SPP
    solar_GenN_NZ = solar_GenN_NZ_MISO + solar_GenN_NZ_NE + solar_GenN_NZ_NY + solar_GenN_NZ_PJM + solar_GenN_NZ_SERC + solar_GenN_NZ_SPP
    dac_GenN_NZ = dac_GenN_NZ_MISO + dac_GenN_NZ_NE + dac_GenN_NZ_NY + dac_GenN_NZ_PJM + dac_GenN_NZ_SERC + dac_GenN_NZ_SPP

    CoalCCS_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CC_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Combined Cycle')]
    CCCCS_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    battery_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Hydrogen')]
    nuclear_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Nuclear')]
    dac_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2020 = resultsGenN_NE2020[resultsGenN_NE2020['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2020 = resultsGenN_NE2020[resultsGenN_NE2020['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2020_MISO = CoalCCS_GenN_NE2020.loc[CoalCCS_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    battery_GenN_NE2020_MISO = battery_GenN_NE2020.loc[battery_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    hydrogen_GenN_NE2020_MISO = hydrogen_GenN_NE2020.loc[hydrogen_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    CoalCCS_GenN_NE2020_SERC = CoalCCS_GenN_NE2020.loc[CoalCCS_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    battery_GenN_NE2020_SERC = battery_GenN_NE2020.loc[battery_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    hydrogen_GenN_NE2020_SERC = hydrogen_GenN_NE2020.loc[hydrogen_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    CoalCCS_GenN_NE2020_NE = CoalCCS_GenN_NE2020.loc[CoalCCS_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    battery_GenN_NE2020_NE = battery_GenN_NE2020.loc[battery_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    hydrogen_GenN_NE2020_NE = hydrogen_GenN_NE2020.loc[hydrogen_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    CoalCCS_GenN_NE2020_NY = CoalCCS_GenN_NE2020.loc[CoalCCS_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    battery_GenN_NE2020_NY = battery_GenN_NE2020.loc[battery_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    hydrogen_GenN_NE2020_NY = hydrogen_GenN_NE2020.loc[hydrogen_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    CoalCCS_GenN_NE2020_PJM = CoalCCS_GenN_NE2020.loc[CoalCCS_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    battery_GenN_NE2020_PJM = battery_GenN_NE2020.loc[battery_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    hydrogen_GenN_NE2020_PJM = hydrogen_GenN_NE2020.loc[hydrogen_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    CoalCCS_GenN_NE2020_SPP = CoalCCS_GenN_NE2020.loc[CoalCCS_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    battery_GenN_NE2020_SPP = battery_GenN_NE2020.loc[battery_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    hydrogen_GenN_NE2020_SPP = hydrogen_GenN_NE2020.loc[hydrogen_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    CoalCCS_GenN_NE2020 = CoalCCS_GenN_NE2020['Total Gen'].sum()
    battery_GenN_NE2020 = battery_GenN_NE2020['Total Gen'].sum()
    hydrogen_GenN_NE2020 = hydrogen_GenN_NE2020['Total Gen'].sum()
    CCCCS_GenN_NE2020_MISO = CCCCS_GenN_NE2020.loc[CCCCS_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    CCCCS_GenN_NE2020_NE = CCCCS_GenN_NE2020.loc[CCCCS_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    CCCCS_GenN_NE2020_NY = CCCCS_GenN_NE2020.loc[CCCCS_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    CCCCS_GenN_NE2020_PJM = CCCCS_GenN_NE2020.loc[CCCCS_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    CCCCS_GenN_NE2020_SERC = CCCCS_GenN_NE2020.loc[CCCCS_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    CCCCS_GenN_NE2020_SPP = CCCCS_GenN_NE2020.loc[CCCCS_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    CC_GenN_NE2020_MISO = CC_GenN_NE2020.loc[CC_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    CC_GenN_NE2020_NE = CC_GenN_NE2020.loc[CC_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    CC_GenN_NE2020_NY = CC_GenN_NE2020.loc[CC_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    CC_GenN_NE2020_PJM = CC_GenN_NE2020.loc[CC_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    CC_GenN_NE2020_SERC = CC_GenN_NE2020.loc[CC_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    CC_GenN_NE2020_SPP = CC_GenN_NE2020.loc[CC_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    nuclear_GenN_NE2020_MISO = nuclear_GenN_NE2020.loc[nuclear_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    nuclear_GenN_NE2020_NE = nuclear_GenN_NE2020.loc[nuclear_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    nuclear_GenN_NE2020_NY = nuclear_GenN_NE2020.loc[nuclear_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    nuclear_GenN_NE2020_PJM = nuclear_GenN_NE2020.loc[nuclear_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    nuclear_GenN_NE2020_SERC = nuclear_GenN_NE2020.loc[nuclear_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    nuclear_GenN_NE2020_SPP = nuclear_GenN_NE2020.loc[nuclear_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    solar_GenN_NE2020_MISO = solar_GenN_NE2020.loc[solar_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    solar_GenN_NE2020_NE = solar_GenN_NE2020.loc[solar_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    solar_GenN_NE2020_NY = solar_GenN_NE2020.loc[solar_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    solar_GenN_NE2020_PJM = solar_GenN_NE2020.loc[solar_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    solar_GenN_NE2020_SERC = solar_GenN_NE2020.loc[solar_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    solar_GenN_NE2020_SPP = solar_GenN_NE2020.loc[solar_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    wind_GenN_NE2020_MISO = wind_GenN_NE2020.loc[wind_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    wind_GenN_NE2020_NE = wind_GenN_NE2020.loc[wind_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    wind_GenN_NE2020_NY = wind_GenN_NE2020.loc[wind_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    wind_GenN_NE2020_PJM = wind_GenN_NE2020.loc[wind_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    wind_GenN_NE2020_SERC = wind_GenN_NE2020.loc[wind_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    wind_GenN_NE2020_SPP = wind_GenN_NE2020.loc[wind_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]
    dac_GenN_NE2020_MISO = dac_GenN_NE2020.loc[dac_GenN_NE2020['GAMS Symbol'].str.contains('MISO')]
    dac_GenN_NE2020_NE = dac_GenN_NE2020.loc[dac_GenN_NE2020['GAMS Symbol'].str.contains('NE')]
    dac_GenN_NE2020_NY = dac_GenN_NE2020.loc[dac_GenN_NE2020['GAMS Symbol'].str.contains('NY')]
    dac_GenN_NE2020_PJM = dac_GenN_NE2020.loc[dac_GenN_NE2020['GAMS Symbol'].str.contains('PJM')]
    dac_GenN_NE2020_SERC = dac_GenN_NE2020.loc[dac_GenN_NE2020['GAMS Symbol'].str.contains('SERC')]
    dac_GenN_NE2020_SPP = dac_GenN_NE2020.loc[dac_GenN_NE2020['GAMS Symbol'].str.contains('SPP')]

    CoalCCS_GenN_NE2020_SERC = CoalCCS_GenN_NE2020_SERC['Total Gen'].sum()
    battery_GenN_NE2020_SERC = battery_GenN_NE2020_SERC['Total Gen'].sum()
    hydrogen_GenN_NE2020_SERC = hydrogen_GenN_NE2020_SERC['Total Gen'].sum()
    CoalCCS_GenN_NE2020_NY = CoalCCS_GenN_NE2020_NY['Total Gen'].sum()
    battery_GenN_NE2020_NY = battery_GenN_NE2020_NY['Total Gen'].sum()
    hydrogen_GenN_NE2020_NY = hydrogen_GenN_NE2020_NY['Total Gen'].sum()
    CoalCCS_GenN_NE2020_MISO = CoalCCS_GenN_NE2020_MISO['Total Gen'].sum()
    battery_GenN_NE2020_MISO = battery_GenN_NE2020_MISO['Total Gen'].sum()
    hydrogen_GenN_NE2020_MISO = hydrogen_GenN_NE2020_MISO['Total Gen'].sum()
    CoalCCS_GenN_NE2020_PJM = CoalCCS_GenN_NE2020_PJM['Total Gen'].sum()
    battery_GenN_NE2020_PJM = battery_GenN_NE2020_PJM['Total Gen'].sum()
    hydrogen_GenN_NE2020_PJM = hydrogen_GenN_NE2020_PJM['Total Gen'].sum()
    CoalCCS_GenN_NE2020_SPP = CoalCCS_GenN_NE2020_SPP['Total Gen'].sum()
    battery_GenN_NE2020_SPP = battery_GenN_NE2020_SPP['Total Gen'].sum()
    hydrogen_GenN_NE2020_SPP = hydrogen_GenN_NE2020_SPP['Total Gen'].sum()
    CoalCCS_GenN_NE2020_NE = CoalCCS_GenN_NE2020_NE['Total Gen'].sum()
    battery_GenN_NE2020_NE = battery_GenN_NE2020_NE['Total Gen'].sum()
    hydrogen_GenN_NE2020_NE = hydrogen_GenN_NE2020_NE['Total Gen'].sum()

    CCCCS_GenN_NE2020_MISO = CCCCS_GenN_NE2020_MISO['Total Gen'].sum()
    CCCCS_GenN_NE2020_NE = CCCCS_GenN_NE2020_NE['Total Gen'].sum()
    CCCCS_GenN_NE2020_NY = CCCCS_GenN_NE2020_NY['Total Gen'].sum()
    CCCCS_GenN_NE2020_PJM = CCCCS_GenN_NE2020_PJM['Total Gen'].sum()
    CCCCS_GenN_NE2020_SERC = CCCCS_GenN_NE2020_SERC['Total Gen'].sum()
    CCCCS_GenN_NE2020_SPP = CCCCS_GenN_NE2020_SPP['Total Gen'].sum()
    CC_GenN_NE2020_MISO = CC_GenN_NE2020_MISO['Total Gen'].sum() - CCCCS_GenN_NE2020_MISO
    CC_GenN_NE2020_NE = CC_GenN_NE2020_NE['Total Gen'].sum() - CCCCS_GenN_NE2020_NE
    CC_GenN_NE2020_NY = CC_GenN_NE2020_NY['Total Gen'].sum() - CCCCS_GenN_NE2020_NY
    CC_GenN_NE2020_PJM = CC_GenN_NE2020_PJM['Total Gen'].sum() - CCCCS_GenN_NE2020_PJM
    CC_GenN_NE2020_SERC = CC_GenN_NE2020_SERC['Total Gen'].sum() - CCCCS_GenN_NE2020_SERC
    CC_GenN_NE2020_SPP = CC_GenN_NE2020_SPP['Total Gen'].sum() - CCCCS_GenN_NE2020_SPP
    nuclear_GenN_NE2020_MISO = nuclear_GenN_NE2020_MISO['Total Gen'].sum()
    nuclear_GenN_NE2020_NE = nuclear_GenN_NE2020_NE['Total Gen'].sum()
    nuclear_GenN_NE2020_NY = nuclear_GenN_NE2020_NY['Total Gen'].sum()
    nuclear_GenN_NE2020_PJM = nuclear_GenN_NE2020_PJM['Total Gen'].sum()
    nuclear_GenN_NE2020_SERC = nuclear_GenN_NE2020_SERC['Total Gen'].sum()
    nuclear_GenN_NE2020_SPP = nuclear_GenN_NE2020_SPP['Total Gen'].sum()
    solar_GenN_NE2020_MISO = solar_GenN_NE2020_MISO['Total Gen'].sum()
    solar_GenN_NE2020_NE = solar_GenN_NE2020_NE['Total Gen'].sum()
    solar_GenN_NE2020_NY = solar_GenN_NE2020_NY['Total Gen'].sum()
    solar_GenN_NE2020_PJM = solar_GenN_NE2020_PJM['Total Gen'].sum()
    solar_GenN_NE2020_SERC = solar_GenN_NE2020_SERC['Total Gen'].sum()
    solar_GenN_NE2020_SPP = solar_GenN_NE2020_SPP['Total Gen'].sum()
    wind_GenN_NE2020_MISO = wind_GenN_NE2020_MISO['Total Gen'].sum()
    wind_GenN_NE2020_NE = wind_GenN_NE2020_NE['Total Gen'].sum()
    wind_GenN_NE2020_NY = wind_GenN_NE2020_NY['Total Gen'].sum()
    wind_GenN_NE2020_PJM = wind_GenN_NE2020_PJM['Total Gen'].sum()
    wind_GenN_NE2020_SERC = wind_GenN_NE2020_SERC['Total Gen'].sum()
    wind_GenN_NE2020_SPP = wind_GenN_NE2020_SPP['Total Gen'].sum()
    dac_GenN_NE2020_MISO = dac_GenN_NE2020_MISO['Total Gen'].sum()
    dac_GenN_NE2020_NE = dac_GenN_NE2020_NE['Total Gen'].sum()
    dac_GenN_NE2020_NY = dac_GenN_NE2020_NY['Total Gen'].sum()
    dac_GenN_NE2020_PJM = dac_GenN_NE2020_PJM['Total Gen'].sum()
    dac_GenN_NE2020_SERC = dac_GenN_NE2020_SERC['Total Gen'].sum()
    dac_GenN_NE2020_SPP = dac_GenN_NE2020_SPP['Total Gen'].sum()

    CC_GenN_NE2020 = CC_GenN_NE2020_MISO + CC_GenN_NE2020_NE + CC_GenN_NE2020_NY + CC_GenN_NE2020_PJM + CC_GenN_NE2020_SERC + CC_GenN_NE2020_SPP
    CCCCS_GenN_NE2020 = CCCCS_GenN_NE2020_MISO + CCCCS_GenN_NE2020_NE + CCCCS_GenN_NE2020_NY + CCCCS_GenN_NE2020_PJM + CCCCS_GenN_NE2020_SERC + CCCCS_GenN_NE2020_SPP
    nuclear_GenN_NE2020 = nuclear_GenN_NE2020_MISO + nuclear_GenN_NE2020_NE + nuclear_GenN_NE2020_NY + nuclear_GenN_NE2020_PJM + nuclear_GenN_NE2020_SERC + nuclear_GenN_NE2020_SPP
    wind_GenN_NE2020 = wind_GenN_NE2020_MISO + wind_GenN_NE2020_NE + wind_GenN_NE2020_NY + wind_GenN_NE2020_PJM + wind_GenN_NE2020_SERC + wind_GenN_NE2020_SPP
    solar_GenN_NE2020 = solar_GenN_NE2020_MISO + solar_GenN_NE2020_NE + solar_GenN_NE2020_NY + solar_GenN_NE2020_PJM + solar_GenN_NE2020_SERC + solar_GenN_NE2020_SPP
    dac_GenN_NE2020 = dac_GenN_NE2020_MISO + dac_GenN_NE2020_NE + dac_GenN_NE2020_NY + dac_GenN_NE2020_PJM + dac_GenN_NE2020_SERC + dac_GenN_NE2020_SPP

    CoalCCS_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CC_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Combined Cycle')]
    CCCCS_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    battery_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Hydrogen')]
    nuclear_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Nuclear')]
    dac_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2030 = resultsGenN_NE2030[resultsGenN_NE2030['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2030 = resultsGenN_NE2030[resultsGenN_NE2030['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2030_MISO = CoalCCS_GenN_NE2030.loc[CoalCCS_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    battery_GenN_NE2030_MISO = battery_GenN_NE2030.loc[battery_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    hydrogen_GenN_NE2030_MISO = hydrogen_GenN_NE2030.loc[hydrogen_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    CoalCCS_GenN_NE2030_SERC = CoalCCS_GenN_NE2030.loc[CoalCCS_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    battery_GenN_NE2030_SERC = battery_GenN_NE2030.loc[battery_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    hydrogen_GenN_NE2030_SERC = hydrogen_GenN_NE2030.loc[hydrogen_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    CoalCCS_GenN_NE2030_NE = CoalCCS_GenN_NE2030.loc[CoalCCS_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    battery_GenN_NE2030_NE = battery_GenN_NE2030.loc[battery_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    hydrogen_GenN_NE2030_NE = hydrogen_GenN_NE2030.loc[hydrogen_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    CoalCCS_GenN_NE2030_NY = CoalCCS_GenN_NE2030.loc[CoalCCS_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    battery_GenN_NE2030_NY = battery_GenN_NE2030.loc[battery_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    hydrogen_GenN_NE2030_NY = hydrogen_GenN_NE2030.loc[hydrogen_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    CoalCCS_GenN_NE2030_PJM = CoalCCS_GenN_NE2030.loc[CoalCCS_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    battery_GenN_NE2030_PJM = battery_GenN_NE2030.loc[battery_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    hydrogen_GenN_NE2030_PJM = hydrogen_GenN_NE2030.loc[hydrogen_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    CoalCCS_GenN_NE2030_SPP = CoalCCS_GenN_NE2030.loc[CoalCCS_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    battery_GenN_NE2030_SPP = battery_GenN_NE2030.loc[battery_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    hydrogen_GenN_NE2030_SPP = hydrogen_GenN_NE2030.loc[hydrogen_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    CoalCCS_GenN_NE2030 = CoalCCS_GenN_NE2030['Total Gen'].sum()
    battery_GenN_NE2030 = battery_GenN_NE2030['Total Gen'].sum()
    hydrogen_GenN_NE2030 = hydrogen_GenN_NE2030['Total Gen'].sum()
    CC_GenN_NE2030_MISO = CC_GenN_NE2030.loc[CC_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    CC_GenN_NE2030_NE = CC_GenN_NE2030.loc[CC_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    CC_GenN_NE2030_NY = CC_GenN_NE2030.loc[CC_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    CC_GenN_NE2030_PJM = CC_GenN_NE2030.loc[CC_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    CC_GenN_NE2030_SERC = CC_GenN_NE2030.loc[CC_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    CC_GenN_NE2030_SPP = CC_GenN_NE2030.loc[CC_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    CCCCS_GenN_NE2030_MISO = CCCCS_GenN_NE2030.loc[CCCCS_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    CCCCS_GenN_NE2030_NE = CCCCS_GenN_NE2030.loc[CCCCS_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    CCCCS_GenN_NE2030_NY = CCCCS_GenN_NE2030.loc[CCCCS_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    CCCCS_GenN_NE2030_PJM = CCCCS_GenN_NE2030.loc[CCCCS_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    CCCCS_GenN_NE2030_SERC = CCCCS_GenN_NE2030.loc[CCCCS_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    CCCCS_GenN_NE2030_SPP = CCCCS_GenN_NE2030.loc[CCCCS_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    nuclear_GenN_NE2030_MISO = nuclear_GenN_NE2030.loc[nuclear_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    nuclear_GenN_NE2030_NE = nuclear_GenN_NE2030.loc[nuclear_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    nuclear_GenN_NE2030_NY = nuclear_GenN_NE2030.loc[nuclear_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    nuclear_GenN_NE2030_PJM = nuclear_GenN_NE2030.loc[nuclear_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    nuclear_GenN_NE2030_SERC = nuclear_GenN_NE2030.loc[nuclear_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    nuclear_GenN_NE2030_SPP = nuclear_GenN_NE2030.loc[nuclear_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    solar_GenN_NE2030_MISO = solar_GenN_NE2030.loc[solar_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    solar_GenN_NE2030_NE = solar_GenN_NE2030.loc[solar_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    solar_GenN_NE2030_NY = solar_GenN_NE2030.loc[solar_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    solar_GenN_NE2030_PJM = solar_GenN_NE2030.loc[solar_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    solar_GenN_NE2030_SERC = solar_GenN_NE2030.loc[solar_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    solar_GenN_NE2030_SPP = solar_GenN_NE2030.loc[solar_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    wind_GenN_NE2030_MISO = wind_GenN_NE2030.loc[wind_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    wind_GenN_NE2030_NE = wind_GenN_NE2030.loc[wind_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    wind_GenN_NE2030_NY = wind_GenN_NE2030.loc[wind_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    wind_GenN_NE2030_PJM = wind_GenN_NE2030.loc[wind_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    wind_GenN_NE2030_SERC = wind_GenN_NE2030.loc[wind_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    wind_GenN_NE2030_SPP = wind_GenN_NE2030.loc[wind_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]
    dac_GenN_NE2030_MISO = dac_GenN_NE2030.loc[dac_GenN_NE2030['GAMS Symbol'].str.contains('MISO')]
    dac_GenN_NE2030_NE = dac_GenN_NE2030.loc[dac_GenN_NE2030['GAMS Symbol'].str.contains('NE')]
    dac_GenN_NE2030_NY = dac_GenN_NE2030.loc[dac_GenN_NE2030['GAMS Symbol'].str.contains('NY')]
    dac_GenN_NE2030_PJM = dac_GenN_NE2030.loc[dac_GenN_NE2030['GAMS Symbol'].str.contains('PJM')]
    dac_GenN_NE2030_SERC = dac_GenN_NE2030.loc[dac_GenN_NE2030['GAMS Symbol'].str.contains('SERC')]
    dac_GenN_NE2030_SPP = dac_GenN_NE2030.loc[dac_GenN_NE2030['GAMS Symbol'].str.contains('SPP')]

    CoalCCS_GenN_NE2030_SERC = CoalCCS_GenN_NE2030_SERC['Total Gen'].sum()
    battery_GenN_NE2030_SERC = battery_GenN_NE2030_SERC['Total Gen'].sum()
    hydrogen_GenN_NE2030_SERC = hydrogen_GenN_NE2030_SERC['Total Gen'].sum()
    CoalCCS_GenN_NE2030_NY = CoalCCS_GenN_NE2030_NY['Total Gen'].sum()
    battery_GenN_NE2030_NY = battery_GenN_NE2030_NY['Total Gen'].sum()
    hydrogen_GenN_NE2030_NY = hydrogen_GenN_NE2030_NY['Total Gen'].sum()
    CoalCCS_GenN_NE2030_MISO = CoalCCS_GenN_NE2030_MISO['Total Gen'].sum()
    battery_GenN_NE2030_MISO = battery_GenN_NE2030_MISO['Total Gen'].sum()
    hydrogen_GenN_NE2030_MISO = hydrogen_GenN_NE2030_MISO['Total Gen'].sum()
    CoalCCS_GenN_NE2030_PJM = CoalCCS_GenN_NE2030_PJM['Total Gen'].sum()
    battery_GenN_NE2030_PJM = battery_GenN_NE2030_PJM['Total Gen'].sum()
    hydrogen_GenN_NE2030_PJM = hydrogen_GenN_NE2030_PJM['Total Gen'].sum()
    CoalCCS_GenN_NE2030_SPP = CoalCCS_GenN_NE2030_SPP['Total Gen'].sum()
    battery_GenN_NE2030_SPP = battery_GenN_NE2030_SPP['Total Gen'].sum()
    hydrogen_GenN_NE2030_SPP = hydrogen_GenN_NE2030_SPP['Total Gen'].sum()
    CoalCCS_GenN_NE2030_NE = CoalCCS_GenN_NE2030_NE['Total Gen'].sum()
    battery_GenN_NE2030_NE = battery_GenN_NE2030_NE['Total Gen'].sum()
    hydrogen_GenN_NE2030_NE = hydrogen_GenN_NE2030_NE['Total Gen'].sum()
    CCCCS_GenN_NE2030_MISO = CCCCS_GenN_NE2030_MISO['Total Gen'].sum()
    CCCCS_GenN_NE2030_NE = CCCCS_GenN_NE2030_NE['Total Gen'].sum()
    CCCCS_GenN_NE2030_NY = CCCCS_GenN_NE2030_NY['Total Gen'].sum()
    CCCCS_GenN_NE2030_PJM = CCCCS_GenN_NE2030_PJM['Total Gen'].sum()
    CCCCS_GenN_NE2030_SERC = CCCCS_GenN_NE2030_SERC['Total Gen'].sum()
    CCCCS_GenN_NE2030_SPP = CCCCS_GenN_NE2030_SPP['Total Gen'].sum()
    CC_GenN_NE2030_MISO = CC_GenN_NE2030_MISO['Total Gen'].sum() - CCCCS_GenN_NE2030_MISO
    CC_GenN_NE2030_NE = CC_GenN_NE2030_NE['Total Gen'].sum() - CCCCS_GenN_NE2030_NE
    CC_GenN_NE2030_NY = CC_GenN_NE2030_NY['Total Gen'].sum() - CCCCS_GenN_NE2030_NY
    CC_GenN_NE2030_PJM = CC_GenN_NE2030_PJM['Total Gen'].sum() - CCCCS_GenN_NE2030_PJM
    CC_GenN_NE2030_SERC = CC_GenN_NE2030_SERC['Total Gen'].sum() - CCCCS_GenN_NE2030_SERC
    CC_GenN_NE2030_SPP = CC_GenN_NE2030_SPP['Total Gen'].sum() - CCCCS_GenN_NE2030_SPP
    nuclear_GenN_NE2030_MISO = nuclear_GenN_NE2030_MISO['Total Gen'].sum()
    nuclear_GenN_NE2030_NE = nuclear_GenN_NE2030_NE['Total Gen'].sum()
    nuclear_GenN_NE2030_NY = nuclear_GenN_NE2030_NY['Total Gen'].sum()
    nuclear_GenN_NE2030_PJM = nuclear_GenN_NE2030_PJM['Total Gen'].sum()
    nuclear_GenN_NE2030_SERC = nuclear_GenN_NE2030_SERC['Total Gen'].sum()
    nuclear_GenN_NE2030_SPP = nuclear_GenN_NE2030_SPP['Total Gen'].sum()
    solar_GenN_NE2030_MISO = solar_GenN_NE2030_MISO['Total Gen'].sum()
    solar_GenN_NE2030_NE = solar_GenN_NE2030_NE['Total Gen'].sum()
    solar_GenN_NE2030_NY = solar_GenN_NE2030_NY['Total Gen'].sum()
    solar_GenN_NE2030_PJM = solar_GenN_NE2030_PJM['Total Gen'].sum()
    solar_GenN_NE2030_SERC = solar_GenN_NE2030_SERC['Total Gen'].sum()
    solar_GenN_NE2030_SPP = solar_GenN_NE2030_SPP['Total Gen'].sum()
    wind_GenN_NE2030_MISO = wind_GenN_NE2030_MISO['Total Gen'].sum()
    wind_GenN_NE2030_NE = wind_GenN_NE2030_NE['Total Gen'].sum()
    wind_GenN_NE2030_NY = wind_GenN_NE2030_NY['Total Gen'].sum()
    wind_GenN_NE2030_PJM = wind_GenN_NE2030_PJM['Total Gen'].sum()
    wind_GenN_NE2030_SERC = wind_GenN_NE2030_SERC['Total Gen'].sum()
    wind_GenN_NE2030_SPP = wind_GenN_NE2030_SPP['Total Gen'].sum()
    dac_GenN_NE2030_MISO = dac_GenN_NE2030_MISO['Total Gen'].sum()
    dac_GenN_NE2030_NE = dac_GenN_NE2030_NE['Total Gen'].sum()
    dac_GenN_NE2030_NY = dac_GenN_NE2030_NY['Total Gen'].sum()
    dac_GenN_NE2030_PJM = dac_GenN_NE2030_PJM['Total Gen'].sum()
    dac_GenN_NE2030_SERC = dac_GenN_NE2030_SERC['Total Gen'].sum()
    dac_GenN_NE2030_SPP = dac_GenN_NE2030_SPP['Total Gen'].sum()

    CC_GenN_NE2030 = CC_GenN_NE2030_MISO + CC_GenN_NE2030_NE + CC_GenN_NE2030_NY + CC_GenN_NE2030_PJM + CC_GenN_NE2030_SERC + CC_GenN_NE2030_SPP
    CCCCS_GenN_NE2030 = CCCCS_GenN_NE2030_MISO + CCCCS_GenN_NE2030_NE + CCCCS_GenN_NE2030_NY + CCCCS_GenN_NE2030_PJM + CCCCS_GenN_NE2030_SERC + CCCCS_GenN_NE2030_SPP
    nuclear_GenN_NE2030 = nuclear_GenN_NE2030_MISO + nuclear_GenN_NE2030_NE + nuclear_GenN_NE2030_NY + nuclear_GenN_NE2030_PJM + nuclear_GenN_NE2030_SERC + nuclear_GenN_NE2030_SPP
    wind_GenN_NE2030 = wind_GenN_NE2030_MISO + wind_GenN_NE2030_NE + wind_GenN_NE2030_NY + wind_GenN_NE2030_PJM + wind_GenN_NE2030_SERC + wind_GenN_NE2030_SPP
    solar_GenN_NE2030 = solar_GenN_NE2030_MISO + solar_GenN_NE2030_NE + solar_GenN_NE2030_NY + solar_GenN_NE2030_PJM + solar_GenN_NE2030_SERC + solar_GenN_NE2030_SPP
    dac_GenN_NE2030 = dac_GenN_NE2030_MISO + dac_GenN_NE2030_NE + dac_GenN_NE2030_NY + dac_GenN_NE2030_PJM + dac_GenN_NE2030_SERC + dac_GenN_NE2030_SPP

    CoalCCS_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CC_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Combined Cycle')]
    CCCCS_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    battery_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Hydrogen')]
    nuclear_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Nuclear')]
    dac_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2040 = resultsGenN_NE2040[resultsGenN_NE2040['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2040 = resultsGenN_NE2040[resultsGenN_NE2040['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2040_MISO = CoalCCS_GenN_NE2040.loc[CoalCCS_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    battery_GenN_NE2040_MISO = battery_GenN_NE2040.loc[battery_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    hydrogen_GenN_NE2040_MISO = hydrogen_GenN_NE2040.loc[hydrogen_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    CoalCCS_GenN_NE2040_SERC = CoalCCS_GenN_NE2040.loc[CoalCCS_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    battery_GenN_NE2040_SERC = battery_GenN_NE2040.loc[battery_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    hydrogen_GenN_NE2040_SERC = hydrogen_GenN_NE2040.loc[hydrogen_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    CoalCCS_GenN_NE2040_NE = CoalCCS_GenN_NE2040.loc[CoalCCS_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    battery_GenN_NE2040_NE = battery_GenN_NE2040.loc[battery_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    hydrogen_GenN_NE2040_NE = hydrogen_GenN_NE2040.loc[hydrogen_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    CoalCCS_GenN_NE2040_NY = CoalCCS_GenN_NE2040.loc[CoalCCS_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    battery_GenN_NE2040_NY = battery_GenN_NE2040.loc[battery_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    hydrogen_GenN_NE2040_NY = hydrogen_GenN_NE2040.loc[hydrogen_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    CoalCCS_GenN_NE2040_PJM = CoalCCS_GenN_NE2040.loc[CoalCCS_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    battery_GenN_NE2040_PJM = battery_GenN_NE2040.loc[battery_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    hydrogen_GenN_NE2040_PJM = hydrogen_GenN_NE2040.loc[hydrogen_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    CoalCCS_GenN_NE2040_SPP = CoalCCS_GenN_NE2040.loc[CoalCCS_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    battery_GenN_NE2040_SPP = battery_GenN_NE2040.loc[battery_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    hydrogen_GenN_NE2040_SPP = hydrogen_GenN_NE2040.loc[hydrogen_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    CoalCCS_GenN_NE2040 = CoalCCS_GenN_NE2040['Total Gen'].sum()
    battery_GenN_NE2040 = battery_GenN_NE2040['Total Gen'].sum()
    hydrogen_GenN_NE2040 = hydrogen_GenN_NE2040['Total Gen'].sum()
    CC_GenN_NE2040_MISO = CC_GenN_NE2040.loc[CC_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    CC_GenN_NE2040_NE = CC_GenN_NE2040.loc[CC_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    CC_GenN_NE2040_NY = CC_GenN_NE2040.loc[CC_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    CC_GenN_NE2040_PJM = CC_GenN_NE2040.loc[CC_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    CC_GenN_NE2040_SERC = CC_GenN_NE2040.loc[CC_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    CC_GenN_NE2040_SPP = CC_GenN_NE2040.loc[CC_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    CCCCS_GenN_NE2040_MISO = CCCCS_GenN_NE2040.loc[CCCCS_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    CCCCS_GenN_NE2040_NE = CCCCS_GenN_NE2040.loc[CCCCS_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    CCCCS_GenN_NE2040_NY = CCCCS_GenN_NE2040.loc[CCCCS_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    CCCCS_GenN_NE2040_PJM = CCCCS_GenN_NE2040.loc[CCCCS_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    CCCCS_GenN_NE2040_SERC = CCCCS_GenN_NE2040.loc[CCCCS_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    CCCCS_GenN_NE2040_SPP = CCCCS_GenN_NE2040.loc[CCCCS_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    nuclear_GenN_NE2040_MISO = nuclear_GenN_NE2040.loc[nuclear_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    nuclear_GenN_NE2040_NE = nuclear_GenN_NE2040.loc[nuclear_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    nuclear_GenN_NE2040_NY = nuclear_GenN_NE2040.loc[nuclear_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    nuclear_GenN_NE2040_PJM = nuclear_GenN_NE2040.loc[nuclear_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    nuclear_GenN_NE2040_SERC = nuclear_GenN_NE2040.loc[nuclear_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    nuclear_GenN_NE2040_SPP = nuclear_GenN_NE2040.loc[nuclear_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    solar_GenN_NE2040_MISO = solar_GenN_NE2040.loc[solar_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    solar_GenN_NE2040_NE = solar_GenN_NE2040.loc[solar_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    solar_GenN_NE2040_NY = solar_GenN_NE2040.loc[solar_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    solar_GenN_NE2040_PJM = solar_GenN_NE2040.loc[solar_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    solar_GenN_NE2040_SERC = solar_GenN_NE2040.loc[solar_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    solar_GenN_NE2040_SPP = solar_GenN_NE2040.loc[solar_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    wind_GenN_NE2040_MISO = wind_GenN_NE2040.loc[wind_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    wind_GenN_NE2040_NE = wind_GenN_NE2040.loc[wind_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    wind_GenN_NE2040_NY = wind_GenN_NE2040.loc[wind_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    wind_GenN_NE2040_PJM = wind_GenN_NE2040.loc[wind_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    wind_GenN_NE2040_SERC = wind_GenN_NE2040.loc[wind_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    wind_GenN_NE2040_SPP = wind_GenN_NE2040.loc[wind_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]
    dac_GenN_NE2040_MISO = dac_GenN_NE2040.loc[dac_GenN_NE2040['GAMS Symbol'].str.contains('MISO')]
    dac_GenN_NE2040_NE = dac_GenN_NE2040.loc[dac_GenN_NE2040['GAMS Symbol'].str.contains('NE')]
    dac_GenN_NE2040_NY = dac_GenN_NE2040.loc[dac_GenN_NE2040['GAMS Symbol'].str.contains('NY')]
    dac_GenN_NE2040_PJM = dac_GenN_NE2040.loc[dac_GenN_NE2040['GAMS Symbol'].str.contains('PJM')]
    dac_GenN_NE2040_SERC = dac_GenN_NE2040.loc[dac_GenN_NE2040['GAMS Symbol'].str.contains('SERC')]
    dac_GenN_NE2040_SPP = dac_GenN_NE2040.loc[dac_GenN_NE2040['GAMS Symbol'].str.contains('SPP')]

    CoalCCS_GenN_NE2040_SERC = CoalCCS_GenN_NE2040_SERC['Total Gen'].sum()
    battery_GenN_NE2040_SERC = battery_GenN_NE2040_SERC['Total Gen'].sum()
    hydrogen_GenN_NE2040_SERC = hydrogen_GenN_NE2040_SERC['Total Gen'].sum()
    CoalCCS_GenN_NE2040_NY = CoalCCS_GenN_NE2040_NY['Total Gen'].sum()
    battery_GenN_NE2040_NY = battery_GenN_NE2040_NY['Total Gen'].sum()
    hydrogen_GenN_NE2040_NY = hydrogen_GenN_NE2040_NY['Total Gen'].sum()
    CoalCCS_GenN_NE2040_MISO = CoalCCS_GenN_NE2040_MISO['Total Gen'].sum()
    battery_GenN_NE2040_MISO = battery_GenN_NE2040_MISO['Total Gen'].sum()
    hydrogen_GenN_NE2040_MISO = hydrogen_GenN_NE2040_MISO['Total Gen'].sum()
    CoalCCS_GenN_NE2040_PJM = CoalCCS_GenN_NE2040_PJM['Total Gen'].sum()
    battery_GenN_NE2040_PJM = battery_GenN_NE2040_PJM['Total Gen'].sum()
    hydrogen_GenN_NE2040_PJM = hydrogen_GenN_NE2040_PJM['Total Gen'].sum()
    CoalCCS_GenN_NE2040_SPP = CoalCCS_GenN_NE2040_SPP['Total Gen'].sum()
    battery_GenN_NE2040_SPP = battery_GenN_NE2040_SPP['Total Gen'].sum()
    hydrogen_GenN_NE2040_SPP = hydrogen_GenN_NE2040_SPP['Total Gen'].sum()
    CoalCCS_GenN_NE2040_NE = CoalCCS_GenN_NE2040_NE['Total Gen'].sum()
    battery_GenN_NE2040_NE = battery_GenN_NE2040_NE['Total Gen'].sum()
    hydrogen_GenN_NE2040_NE = hydrogen_GenN_NE2040_NE['Total Gen'].sum()
    CCCCS_GenN_NE2040_MISO = CCCCS_GenN_NE2040_MISO['Total Gen'].sum()
    CCCCS_GenN_NE2040_NE = CCCCS_GenN_NE2040_NE['Total Gen'].sum()
    CCCCS_GenN_NE2040_NY = CCCCS_GenN_NE2040_NY['Total Gen'].sum()
    CCCCS_GenN_NE2040_PJM = CCCCS_GenN_NE2040_PJM['Total Gen'].sum()
    CCCCS_GenN_NE2040_SERC = CCCCS_GenN_NE2040_SERC['Total Gen'].sum()
    CCCCS_GenN_NE2040_SPP = CCCCS_GenN_NE2040_SPP['Total Gen'].sum()
    CC_GenN_NE2040_MISO = CC_GenN_NE2040_MISO['Total Gen'].sum() - CCCCS_GenN_NE2040_MISO
    CC_GenN_NE2040_NE = CC_GenN_NE2040_NE['Total Gen'].sum() - CCCCS_GenN_NE2040_NE
    CC_GenN_NE2040_NY = CC_GenN_NE2040_NY['Total Gen'].sum() - CCCCS_GenN_NE2040_NY
    CC_GenN_NE2040_PJM = CC_GenN_NE2040_PJM['Total Gen'].sum() - CCCCS_GenN_NE2040_PJM
    CC_GenN_NE2040_SERC = CC_GenN_NE2040_SERC['Total Gen'].sum() - CCCCS_GenN_NE2040_SERC
    CC_GenN_NE2040_SPP = CC_GenN_NE2040_SPP['Total Gen'].sum() - CCCCS_GenN_NE2040_SPP
    nuclear_GenN_NE2040_MISO = nuclear_GenN_NE2040_MISO['Total Gen'].sum()
    nuclear_GenN_NE2040_NE = nuclear_GenN_NE2040_NE['Total Gen'].sum()
    nuclear_GenN_NE2040_NY = nuclear_GenN_NE2040_NY['Total Gen'].sum()
    nuclear_GenN_NE2040_PJM = nuclear_GenN_NE2040_PJM['Total Gen'].sum()
    nuclear_GenN_NE2040_SERC = nuclear_GenN_NE2040_SERC['Total Gen'].sum()
    nuclear_GenN_NE2040_SPP = nuclear_GenN_NE2040_SPP['Total Gen'].sum()
    solar_GenN_NE2040_MISO = solar_GenN_NE2040_MISO['Total Gen'].sum()
    solar_GenN_NE2040_NE = solar_GenN_NE2040_NE['Total Gen'].sum()
    solar_GenN_NE2040_NY = solar_GenN_NE2040_NY['Total Gen'].sum()
    solar_GenN_NE2040_PJM = solar_GenN_NE2040_PJM['Total Gen'].sum()
    solar_GenN_NE2040_SERC = solar_GenN_NE2040_SERC['Total Gen'].sum()
    solar_GenN_NE2040_SPP = solar_GenN_NE2040_SPP['Total Gen'].sum()
    wind_GenN_NE2040_MISO = wind_GenN_NE2040_MISO['Total Gen'].sum()
    wind_GenN_NE2040_NE = wind_GenN_NE2040_NE['Total Gen'].sum()
    wind_GenN_NE2040_NY = wind_GenN_NE2040_NY['Total Gen'].sum()
    wind_GenN_NE2040_PJM = wind_GenN_NE2040_PJM['Total Gen'].sum()
    wind_GenN_NE2040_SERC = wind_GenN_NE2040_SERC['Total Gen'].sum()
    wind_GenN_NE2040_SPP = wind_GenN_NE2040_SPP['Total Gen'].sum()
    dac_GenN_NE2040_MISO = dac_GenN_NE2040_MISO['Total Gen'].sum()
    dac_GenN_NE2040_NE = dac_GenN_NE2040_NE['Total Gen'].sum()
    dac_GenN_NE2040_NY = dac_GenN_NE2040_NY['Total Gen'].sum()
    dac_GenN_NE2040_PJM = dac_GenN_NE2040_PJM['Total Gen'].sum()
    dac_GenN_NE2040_SERC = dac_GenN_NE2040_SERC['Total Gen'].sum()
    dac_GenN_NE2040_SPP = dac_GenN_NE2040_SPP['Total Gen'].sum()

    CC_GenN_NE2040 = CC_GenN_NE2040_MISO + CC_GenN_NE2040_NE + CC_GenN_NE2040_NY + CC_GenN_NE2040_PJM + CC_GenN_NE2040_SERC + CC_GenN_NE2040_SPP
    CCCCS_GenN_NE2040 = CCCCS_GenN_NE2040_MISO + CCCCS_GenN_NE2040_NE + CCCCS_GenN_NE2040_NY + CCCCS_GenN_NE2040_PJM + CCCCS_GenN_NE2040_SERC + CCCCS_GenN_NE2040_SPP
    nuclear_GenN_NE2040 = nuclear_GenN_NE2040_MISO + nuclear_GenN_NE2040_NE + nuclear_GenN_NE2040_NY + nuclear_GenN_NE2040_PJM + nuclear_GenN_NE2040_SERC + nuclear_GenN_NE2040_SPP
    wind_GenN_NE2040 = wind_GenN_NE2040_MISO + wind_GenN_NE2040_NE + wind_GenN_NE2040_NY + wind_GenN_NE2040_PJM + wind_GenN_NE2040_SERC + wind_GenN_NE2040_SPP
    solar_GenN_NE2040 = solar_GenN_NE2040_MISO + solar_GenN_NE2040_NE + solar_GenN_NE2040_NY + solar_GenN_NE2040_PJM + solar_GenN_NE2040_SERC + solar_GenN_NE2040_SPP
    dac_GenN_NE2040 = dac_GenN_NE2040_MISO + dac_GenN_NE2040_NE + dac_GenN_NE2040_NY + dac_GenN_NE2040_PJM + dac_GenN_NE2040_SERC + dac_GenN_NE2040_SPP

    CoalCCS_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CC_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Combined Cycle')]
    CCCCS_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    battery_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Hydrogen')]
    nuclear_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Nuclear')]
    dac_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2050 = resultsGenN_NE2050[resultsGenN_NE2050['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2050 = resultsGenN_NE2050[resultsGenN_NE2050['GAMS Symbol'].str.contains('wind')]

    CC_GenN_NE2050_MISO = CC_GenN_NE2050.loc[CC_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    CC_GenN_NE2050_NE = CC_GenN_NE2050.loc[CC_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    CC_GenN_NE2050_NY = CC_GenN_NE2050.loc[CC_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    CC_GenN_NE2050_PJM = CC_GenN_NE2050.loc[CC_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    CC_GenN_NE2050_SERC = CC_GenN_NE2050.loc[CC_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    CC_GenN_NE2050_SPP = CC_GenN_NE2050.loc[CC_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    CCCCS_GenN_NE2050_MISO = CCCCS_GenN_NE2050.loc[CCCCS_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    CCCCS_GenN_NE2050_NE = CCCCS_GenN_NE2050.loc[CCCCS_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    CCCCS_GenN_NE2050_NY = CCCCS_GenN_NE2050.loc[CCCCS_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    CCCCS_GenN_NE2050_PJM = CCCCS_GenN_NE2050.loc[CCCCS_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    CCCCS_GenN_NE2050_SERC = CCCCS_GenN_NE2050.loc[CCCCS_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    CCCCS_GenN_NE2050_SPP = CCCCS_GenN_NE2050.loc[CCCCS_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    nuclear_GenN_NE2050_MISO = nuclear_GenN_NE2050.loc[nuclear_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    nuclear_GenN_NE2050_NE = nuclear_GenN_NE2050.loc[nuclear_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    nuclear_GenN_NE2050_NY = nuclear_GenN_NE2050.loc[nuclear_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    nuclear_GenN_NE2050_PJM = nuclear_GenN_NE2050.loc[nuclear_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    nuclear_GenN_NE2050_SERC = nuclear_GenN_NE2050.loc[nuclear_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    nuclear_GenN_NE2050_SPP = nuclear_GenN_NE2050.loc[nuclear_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    solar_GenN_NE2050_MISO = solar_GenN_NE2050.loc[solar_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    solar_GenN_NE2050_NE = solar_GenN_NE2050.loc[solar_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    solar_GenN_NE2050_NY = solar_GenN_NE2050.loc[solar_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    solar_GenN_NE2050_PJM = solar_GenN_NE2050.loc[solar_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    solar_GenN_NE2050_SERC = solar_GenN_NE2050.loc[solar_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    solar_GenN_NE2050_SPP = solar_GenN_NE2050.loc[solar_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    wind_GenN_NE2050_MISO = wind_GenN_NE2050.loc[wind_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    wind_GenN_NE2050_NE = wind_GenN_NE2050.loc[wind_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    wind_GenN_NE2050_NY = wind_GenN_NE2050.loc[wind_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    wind_GenN_NE2050_PJM = wind_GenN_NE2050.loc[wind_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    wind_GenN_NE2050_SERC = wind_GenN_NE2050.loc[wind_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    wind_GenN_NE2050_SPP = wind_GenN_NE2050.loc[wind_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    dac_GenN_NE2050_MISO = dac_GenN_NE2050.loc[dac_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    dac_GenN_NE2050_NE = dac_GenN_NE2050.loc[dac_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    dac_GenN_NE2050_NY = dac_GenN_NE2050.loc[dac_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    dac_GenN_NE2050_PJM = dac_GenN_NE2050.loc[dac_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    dac_GenN_NE2050_SERC = dac_GenN_NE2050.loc[dac_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    dac_GenN_NE2050_SPP = dac_GenN_NE2050.loc[dac_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]

    CoalCCS_GenN_NE2050_MISO = CoalCCS_GenN_NE2050.loc[CoalCCS_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    battery_GenN_NE2050_MISO = battery_GenN_NE2050.loc[battery_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    hydrogen_GenN_NE2050_MISO = hydrogen_GenN_NE2050.loc[hydrogen_GenN_NE2050['GAMS Symbol'].str.contains('MISO')]
    CoalCCS_GenN_NE2050_SERC = CoalCCS_GenN_NE2050.loc[CoalCCS_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    battery_GenN_NE2050_SERC = battery_GenN_NE2050.loc[battery_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    hydrogen_GenN_NE2050_SERC = hydrogen_GenN_NE2050.loc[hydrogen_GenN_NE2050['GAMS Symbol'].str.contains('SERC')]
    CoalCCS_GenN_NE2050_NE = CoalCCS_GenN_NE2050.loc[CoalCCS_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    battery_GenN_NE2050_NE = battery_GenN_NE2050.loc[battery_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    hydrogen_GenN_NE2050_NE = hydrogen_GenN_NE2050.loc[hydrogen_GenN_NE2050['GAMS Symbol'].str.contains('NE')]
    CoalCCS_GenN_NE2050_NY = CoalCCS_GenN_NE2050.loc[CoalCCS_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    battery_GenN_NE2050_NY = battery_GenN_NE2050.loc[battery_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    hydrogen_GenN_NE2050_NY = hydrogen_GenN_NE2050.loc[hydrogen_GenN_NE2050['GAMS Symbol'].str.contains('NY')]
    CoalCCS_GenN_NE2050_PJM = CoalCCS_GenN_NE2050.loc[CoalCCS_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    battery_GenN_NE2050_PJM = battery_GenN_NE2050.loc[battery_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    hydrogen_GenN_NE2050_PJM = hydrogen_GenN_NE2050.loc[hydrogen_GenN_NE2050['GAMS Symbol'].str.contains('PJM')]
    CoalCCS_GenN_NE2050_SPP = CoalCCS_GenN_NE2050.loc[CoalCCS_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    battery_GenN_NE2050_SPP = battery_GenN_NE2050.loc[battery_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]
    hydrogen_GenN_NE2050_SPP = hydrogen_GenN_NE2050.loc[hydrogen_GenN_NE2050['GAMS Symbol'].str.contains('SPP')]

    CoalCCS_GenN_NE2050 = CoalCCS_GenN_NE2050['Total Gen'].sum()
    battery_GenN_NE2050 = battery_GenN_NE2050['Total Gen'].sum()
    hydrogen_GenN_NE2050 = hydrogen_GenN_NE2050['Total Gen'].sum()
    CoalCCS_GenN_NE2050_SERC = CoalCCS_GenN_NE2050_SERC['Total Gen'].sum()
    battery_GenN_NE2050_SERC = battery_GenN_NE2050_SERC['Total Gen'].sum()
    hydrogen_GenN_NE2050_SERC = hydrogen_GenN_NE2050_SERC['Total Gen'].sum()
    CoalCCS_GenN_NE2050_NY = CoalCCS_GenN_NE2050_NY['Total Gen'].sum()
    battery_GenN_NE2050_NY = battery_GenN_NE2050_NY['Total Gen'].sum()
    hydrogen_GenN_NE2050_NY = hydrogen_GenN_NE2050_NY['Total Gen'].sum()
    CoalCCS_GenN_NE2050_MISO = CoalCCS_GenN_NE2050_MISO['Total Gen'].sum()
    battery_GenN_NE2050_MISO = battery_GenN_NE2050_MISO['Total Gen'].sum()
    hydrogen_GenN_NE2050_MISO = hydrogen_GenN_NE2050_MISO['Total Gen'].sum()
    CoalCCS_GenN_NE2050_PJM = CoalCCS_GenN_NE2050_PJM['Total Gen'].sum()
    battery_GenN_NE2050_PJM = battery_GenN_NE2050_PJM['Total Gen'].sum()
    hydrogen_GenN_NE2050_PJM = hydrogen_GenN_NE2050_PJM['Total Gen'].sum()
    CoalCCS_GenN_NE2050_SPP = CoalCCS_GenN_NE2050_SPP['Total Gen'].sum()
    battery_GenN_NE2050_SPP = battery_GenN_NE2050_SPP['Total Gen'].sum()
    hydrogen_GenN_NE2050_SPP = hydrogen_GenN_NE2050_SPP['Total Gen'].sum()
    CoalCCS_GenN_NE2050_NE = CoalCCS_GenN_NE2050_NE['Total Gen'].sum()
    battery_GenN_NE2050_NE = battery_GenN_NE2050_NE['Total Gen'].sum()
    hydrogen_GenN_NE2050_NE = hydrogen_GenN_NE2050_NE['Total Gen'].sum()
    CCCCS_GenN_NE2050_MISO = CCCCS_GenN_NE2050_MISO['Total Gen'].sum()
    CCCCS_GenN_NE2050_NE = CCCCS_GenN_NE2050_NE['Total Gen'].sum()
    CCCCS_GenN_NE2050_NY = CCCCS_GenN_NE2050_NY['Total Gen'].sum()
    CCCCS_GenN_NE2050_PJM = CCCCS_GenN_NE2050_PJM['Total Gen'].sum()
    CCCCS_GenN_NE2050_SERC = CCCCS_GenN_NE2050_SERC['Total Gen'].sum()
    CCCCS_GenN_NE2050_SPP = CCCCS_GenN_NE2050_SPP['Total Gen'].sum()
    CC_GenN_NE2050_MISO = CC_GenN_NE2050_MISO['Total Gen'].sum() - CCCCS_GenN_NE2050_MISO
    CC_GenN_NE2050_NE = CC_GenN_NE2050_NE['Total Gen'].sum() - CCCCS_GenN_NE2050_NE
    CC_GenN_NE2050_NY = CC_GenN_NE2050_NY['Total Gen'].sum() - CCCCS_GenN_NE2050_NY
    CC_GenN_NE2050_PJM = CC_GenN_NE2050_PJM['Total Gen'].sum() - CCCCS_GenN_NE2050_PJM
    CC_GenN_NE2050_SERC = CC_GenN_NE2050_SERC['Total Gen'].sum() - CCCCS_GenN_NE2050_SERC
    CC_GenN_NE2050_SPP = CC_GenN_NE2050_SPP['Total Gen'].sum() - CCCCS_GenN_NE2050_SPP
    nuclear_GenN_NE2050_MISO = nuclear_GenN_NE2050_MISO['Total Gen'].sum()
    nuclear_GenN_NE2050_NE = nuclear_GenN_NE2050_NE['Total Gen'].sum()
    nuclear_GenN_NE2050_NY = nuclear_GenN_NE2050_NY['Total Gen'].sum()
    nuclear_GenN_NE2050_PJM = nuclear_GenN_NE2050_PJM['Total Gen'].sum()
    nuclear_GenN_NE2050_SERC = nuclear_GenN_NE2050_SERC['Total Gen'].sum()
    nuclear_GenN_NE2050_SPP = nuclear_GenN_NE2050_SPP['Total Gen'].sum()
    solar_GenN_NE2050_MISO = solar_GenN_NE2050_MISO['Total Gen'].sum()
    solar_GenN_NE2050_NE = solar_GenN_NE2050_NE['Total Gen'].sum()
    solar_GenN_NE2050_NY = solar_GenN_NE2050_NY['Total Gen'].sum()
    solar_GenN_NE2050_PJM = solar_GenN_NE2050_PJM['Total Gen'].sum()
    solar_GenN_NE2050_SERC = solar_GenN_NE2050_SERC['Total Gen'].sum()
    solar_GenN_NE2050_SPP = solar_GenN_NE2050_SPP['Total Gen'].sum()
    wind_GenN_NE2050_MISO = wind_GenN_NE2050_MISO['Total Gen'].sum()
    wind_GenN_NE2050_NE = wind_GenN_NE2050_NE['Total Gen'].sum()
    wind_GenN_NE2050_NY = wind_GenN_NE2050_NY['Total Gen'].sum()
    wind_GenN_NE2050_PJM = wind_GenN_NE2050_PJM['Total Gen'].sum()
    wind_GenN_NE2050_SERC = wind_GenN_NE2050_SERC['Total Gen'].sum()
    wind_GenN_NE2050_SPP = wind_GenN_NE2050_SPP['Total Gen'].sum()
    dac_GenN_NE2050_MISO = dac_GenN_NE2050_MISO['Total Gen'].sum()
    dac_GenN_NE2050_NE = dac_GenN_NE2050_NE['Total Gen'].sum()
    dac_GenN_NE2050_NY = dac_GenN_NE2050_NY['Total Gen'].sum()
    dac_GenN_NE2050_PJM = dac_GenN_NE2050_PJM['Total Gen'].sum()
    dac_GenN_NE2050_SERC = dac_GenN_NE2050_SERC['Total Gen'].sum()
    dac_GenN_NE2050_SPP = dac_GenN_NE2050_SPP['Total Gen'].sum()

    CC_GenN_NE2050 = CC_GenN_NE2050_MISO + CC_GenN_NE2050_NE + CC_GenN_NE2050_NY + CC_GenN_NE2050_PJM + CC_GenN_NE2050_SERC + CC_GenN_NE2050_SPP
    CCCCS_GenN_NE2050 = CCCCS_GenN_NE2050_MISO + CCCCS_GenN_NE2050_NE + CCCCS_GenN_NE2050_NY + CCCCS_GenN_NE2050_PJM + CCCCS_GenN_NE2050_SERC + CCCCS_GenN_NE2050_SPP
    nuclear_GenN_NE2050 = nuclear_GenN_NE2050_MISO + nuclear_GenN_NE2050_NE + nuclear_GenN_NE2050_NY + nuclear_GenN_NE2050_PJM + nuclear_GenN_NE2050_SERC + nuclear_GenN_NE2050_SPP
    wind_GenN_NE2050 = wind_GenN_NE2050_MISO + wind_GenN_NE2050_NE + wind_GenN_NE2050_NY + wind_GenN_NE2050_PJM + wind_GenN_NE2050_SERC + wind_GenN_NE2050_SPP
    solar_GenN_NE2050 = solar_GenN_NE2050_MISO + solar_GenN_NE2050_NE + solar_GenN_NE2050_NY + solar_GenN_NE2050_PJM + solar_GenN_NE2050_SERC + solar_GenN_NE2050_SPP
    dac_GenN_NE2050 = dac_GenN_NE2050_MISO + dac_GenN_NE2050_NE + dac_GenN_NE2050_NY + dac_GenN_NE2050_PJM + dac_GenN_NE2050_SERC + dac_GenN_NE2050_SPP

    # Graph Generation - existing and new separate:
    Coal_GenE_all = np.around(np.divide([Coal_GenE_NZ, Coal_GenE_NE2050, Coal_GenE_NE2040,
                                         Coal_GenE_NE2030, Coal_GenE_NE2020], 1000), decimals=1)
    CC_GenE_all = np.around(np.divide([CC_GenE_NZ, CC_GenE_NE2050, CC_GenE_NE2040,
                                       CC_GenE_NE2030, CC_GenE_NE2020], 1000), decimals=1)
    CCCCS_GenE_all = np.around(np.divide([CCCCS_GenE_NZ, CCCCS_GenE_NE2050, CCCCS_GenE_NE2040,
                                          CCCCS_GenE_NE2030, CCCCS_GenE_NE2020], 1000), decimals=1)
    OG_GenE_all = np.around(np.divide([OG_GenE_NZ, OG_GenE_NE2050, OG_GenE_NE2040,
                                       OG_GenE_NE2030, OG_GenE_NE2020], 1000), decimals=1)
    CT_GenE_all = np.around(np.divide([CT_GenE_NZ, CT_GenE_NE2050, CT_GenE_NE2040,
                                       CT_GenE_NE2030, CT_GenE_NE2020], 1000), decimals=1)
    nuclear_GenE_all = np.around(np.divide([nuclear_GenE_NZ, nuclear_GenE_NE2050, nuclear_GenE_NE2040,
                                            nuclear_GenE_NE2030, nuclear_GenE_NE2020], 1000), decimals=1)
    wind_GenE_all = np.around(np.divide([wind_GenE_NZ, wind_GenE_NE2050, wind_GenE_NE2040,
                                         wind_GenE_NE2030, wind_GenE_NE2020], 1000), decimals=1)
    solar_GenE_all = np.around(np.divide([solar_GenE_NZ, solar_GenE_NE2050, solar_GenE_NE2040,
                                          solar_GenE_NE2030, solar_GenE_NE2020], 1000), decimals=1)
    battery_GenE_all = np.around(np.divide([battery_GenE_NZ, battery_GenE_NE2050, battery_GenE_NE2040,
                                            battery_GenE_NE2030, battery_GenE_NE2020], 1000), decimals=1)
    hydrogen_GenE_all = np.around(np.divide([hydrogen_GenE_NZ, hydrogen_GenE_NE2050, hydrogen_GenE_NE2040,
                                             hydrogen_GenE_NE2030, hydrogen_GenE_NE2020], 1000), decimals=1)
    pump_GenE_all = np.around(np.divide([pump_GenE_NZ, pump_GenE_NE2050, pump_GenE_NE2040,
                                         pump_GenE_NE2030, pump_GenE_NE2020], 1000), decimals=1)
    dac_GenE_all = np.around(np.divide([dac_GenE_NZ, dac_GenE_NE2050, dac_GenE_NE2040,
                                        dac_GenE_NE2030, dac_GenE_NE2020], 1000), decimals=1)
    others_GenE_all = np.around(np.divide([Others_GenE_NZ, Others_GenE_NE2050, Others_GenE_NE2040,
                                           Others_GenE_NE2030, Others_GenE_NE2020], 1000), decimals=1)

    CC_GenN_all = np.around(np.divide([CC_GenN_NZ, CC_GenN_NE2050, CC_GenN_NE2040,
                                       CC_GenN_NE2030, CC_GenN_NE2020], 1000), decimals=1)
    CCCCS_GenN_all = np.around(np.divide([CCCCS_GenN_NZ, CCCCS_GenN_NE2050, CCCCS_GenN_NE2040,
                                          CCCCS_GenN_NE2030, CCCCS_GenN_NE2020], 1000), decimals=1)
    nuclear_GenN_all = np.around(np.divide([nuclear_GenN_NZ, nuclear_GenN_NE2050, nuclear_GenN_NE2040,
                                            nuclear_GenN_NE2030, nuclear_GenN_NE2020], 1000), decimals=1)
    wind_GenN_all = np.around(np.divide([wind_GenN_NZ, wind_GenN_NE2050, wind_GenN_NE2040,
                                         wind_GenN_NE2030, wind_GenN_NE2020], 1000), decimals=1)
    solar_GenN_all = np.around(np.divide([solar_GenN_NZ, solar_GenN_NE2050, solar_GenN_NE2040,
                                          solar_GenN_NE2030, solar_GenN_NE2020], 1000), decimals=1)
    battery_GenN_all = np.around(np.divide([battery_GenN_NZ, battery_GenN_NE2050, battery_GenN_NE2040,
                                            battery_GenN_NE2030, battery_GenN_NE2020], 1000), decimals=1)
    hydrogen_GenN_all = np.around(np.divide([hydrogen_GenN_NZ, hydrogen_GenN_NE2050, hydrogen_GenN_NE2040,
                                             hydrogen_GenN_NE2030, hydrogen_GenN_NE2020], 1000), decimals=1)
    dac_GenN_all = np.around(np.divide([dac_GenN_NZ, dac_GenN_NE2050, dac_GenN_NE2040,
                                        dac_GenN_NE2030, dac_GenN_NE2020], 1000), decimals=1)

    #
    dac_Gen_all = np.around(np.divide([dac_GenE_NZ + dac_GenN_NZ, dac_GenE_NE2050 + dac_GenN_NE2050,
                                       dac_GenE_NE2040 + dac_GenN_NE2040, dac_GenE_NE2030 + dac_GenN_NE2030,
                                       dac_GenE_NE2020 + dac_GenN_NE2020], 1000), decimals=1)
    Coal_Gen_all = np.around(np.divide([Coal_GenE_NZ + CoalCCS_GenN_NZ, Coal_GenE_NE2050 + CoalCCS_GenN_NE2050,
                                        Coal_GenE_NE2040 + CoalCCS_GenN_NE2040, Coal_GenE_NE2030 + CoalCCS_GenN_NE2030,
                                        Coal_GenE_NE2020 + CoalCCS_GenN_NE2020], 1000), decimals=1)
    CC_Gen_all = np.around(np.divide([CC_GenE_NZ + CC_GenN_NZ, CC_GenE_NE2050 + CC_GenN_NE2050, CC_GenE_NE2040 + CC_GenN_NE2040,
                                      CC_GenE_NE2030 + CC_GenN_NE2030, CC_GenE_NE2020 + CC_GenN_NE2020], 1000), decimals=1)
    CT_Gen_all = np.around(np.divide([CT_GenE_NZ, CT_GenE_NE2050, CT_GenE_NE2040, CT_GenE_NE2030, CT_GenE_NE2020], 1000), decimals=1)
    CCCCS_Gen_all = np.around(np.divide([CCCCS_GenE_NZ + CCCCS_GenN_NZ, CCCCS_GenE_NE2050 + CCCCS_GenN_NE2050,
                                         CCCCS_GenE_NE2040 + CCCCS_GenN_NE2040, CCCCS_GenE_NE2030 + CCCCS_GenN_NE2030,
                                         CCCCS_GenE_NE2020 + CCCCS_GenN_NE2020], 1000), decimals=1)
    OG_Gen_all = np.around(np.divide([OG_GenE_NZ, OG_GenE_NE2050, OG_GenE_NE2040, OG_GenE_NE2030, OG_GenE_NE2020], 1000), decimals=1)
    nuclear_Gen_all = np.around(np.divide([nuclear_GenE_NZ + nuclear_GenN_NZ, nuclear_GenE_NE2050 + nuclear_GenN_NE2050,
                                           nuclear_GenE_NE2040 + nuclear_GenN_NE2040, nuclear_GenE_NE2030 + nuclear_GenN_NE2030,
                                           nuclear_GenE_NE2020 + nuclear_GenN_NE2020], 1000), decimals=1)
    # nuclear_Gen_new = np.around(np.divide([nuclear_GenN_NZ, nuclear_GenN_NE2050,nuclear_GenN_NE2040,
    #                                       nuclear_GenN_NE2030,nuclear_GenN_NE2020], 1000),decimals=1)
    # nuclear_Gen_existing = np.around(np.divide([nuclear_GenE_NZ, nuclear_GenE_NE2050,nuclear_GenE_NE2040,
    #                                            nuclear_GenE_NE2030,nuclear_GenE_NE2020], 1000),decimals=1)
    wind_Gen_all = np.around(np.divide([wind_GenE_NZ + wind_GenN_NZ, wind_GenE_NE2050 + wind_GenN_NE2050,
                                        wind_GenE_NE2040 + wind_GenN_NE2040, wind_GenE_NE2030 + wind_GenN_NE2030,
                                        wind_GenE_NE2020 + wind_GenN_NE2020], 1000), decimals=1)
    solar_Gen_all = np.around(np.divide([solar_GenE_NZ + solar_GenN_NZ, solar_GenE_NE2050 + solar_GenN_NE2050,
                                         solar_GenE_NE2040 + solar_GenN_NE2040, solar_GenE_NE2030 + solar_GenN_NE2030,
                                         solar_GenE_NE2020 + solar_GenN_NE2020], 1000), decimals=1)
    battery_Gen_all = np.around(np.divide([battery_GenE_NZ + battery_GenN_NZ, battery_GenE_NE2050 + battery_GenN_NE2050,
                                           battery_GenE_NE2040 + battery_GenN_NE2040, battery_GenE_NE2030 + battery_GenN_NE2030,
                                           battery_GenE_NE2020 + battery_GenN_NE2020], 1000), decimals=1)
    hydrogen_Gen_all = np.around(np.divide([hydrogen_GenE_NZ + hydrogen_GenN_NZ, hydrogen_GenE_NE2050 + hydrogen_GenN_NE2050,
                                            hydrogen_GenE_NE2040 + hydrogen_GenN_NE2040, hydrogen_GenE_NE2030 + hydrogen_GenN_NE2030,
                                            hydrogen_GenE_NE2020 + hydrogen_GenN_NE2020], 1000), decimals=1)
    pump_Gen_all = np.around(np.divide([pump_GenE_NZ, pump_GenE_NE2050, pump_GenE_NE2040, pump_GenE_NE2030, pump_GenE_NE2020], 1000), decimals=1)
    others_Gen_all = np.around(np.divide([Others_GenE_NZ, Others_GenE_NE2050, Others_GenE_NE2040, Others_GenE_NE2030, Others_GenE_NE2020], 1000), decimals=1)

    # DAC gen by region:
    dac_Gen_MISO = np.around(np.divide([dac_GenN_NZ_MISO, dac_GenN_NE2050_MISO, dac_GenN_NE2040_MISO,
                                        dac_GenN_NE2030_MISO, dac_GenN_NE2050_MISO], 1000), decimals=1)
    dac_Gen_NE = np.around(np.divide([dac_GenN_NZ_NE, dac_GenN_NE2050_NE, dac_GenN_NE2040_NE,
                                      dac_GenN_NE2030_NE, dac_GenN_NE2050_NE], 1000), decimals=1)
    dac_Gen_NY = np.around(np.divide([dac_GenN_NZ_NY, dac_GenN_NE2050_NY, dac_GenN_NE2040_NY,
                                      dac_GenN_NE2030_NY, dac_GenN_NE2050_NY], 1000), decimals=1)
    dac_Gen_PJM = np.around(np.divide([dac_GenN_NZ_PJM, dac_GenN_NE2050_PJM, dac_GenN_NE2040_PJM,
                                       dac_GenN_NE2030_PJM, dac_GenN_NE2050_PJM], 1000), decimals=1)
    dac_Gen_SERC = np.around(np.divide([dac_GenN_NZ_SERC, dac_GenN_NE2050_SERC, dac_GenN_NE2040_SERC,
                                        dac_GenN_NE2030_SERC, dac_GenN_NE2050_SERC], 1000), decimals=1)
    dac_Gen_SPP = np.around(np.divide([dac_GenN_NZ_SPP, dac_GenN_NE2050_SPP, dac_GenN_NE2040_SPP,
                                       dac_GenN_NE2030_SPP, dac_GenN_NE2050_SPP], 1000), decimals=1)

    # Graph generation by load zones:
    # SERC:
    dac_Gen_all_SERC = np.around(np.divide([dac_GenE_NZ_SERC + dac_GenN_NZ_SERC, dac_GenE_NE2050_SERC + dac_GenN_NE2050_SERC,
                                            dac_GenE_NE2040_SERC + dac_GenN_NE2040_SERC, dac_GenE_NE2030_SERC + dac_GenN_NE2030_SERC,
                                            dac_GenE_NE2020_SERC + dac_GenN_NE2020_SERC], 1000), decimals=1)
    Coal_Gen_all_SERC = np.around(np.divide([Coal_GenE_NZ_SERC + CoalCCS_GenN_NZ_SERC, Coal_GenE_NE2050_SERC + CoalCCS_GenN_NE2050_SERC,
                                             Coal_GenE_NE2040_SERC + CoalCCS_GenN_NE2040_SERC, Coal_GenE_NE2030_SERC + CoalCCS_GenN_NE2030_SERC,
                                             Coal_GenE_NE2020_SERC + CoalCCS_GenN_NE2020_SERC], 1000), decimals=1)
    CC_Gen_all_SERC = np.around(np.divide([CC_GenE_NZ_SERC + CC_GenN_NZ_SERC, CC_GenE_NE2050_SERC + CC_GenN_NE2050_SERC, CC_GenE_NE2040_SERC + CC_GenN_NE2040_SERC,
                                           CC_GenE_NE2030_SERC + CC_GenN_NE2030_SERC, CC_GenE_NE2020_SERC + CC_GenN_NE2020_SERC], 1000), decimals=1)
    CT_Gen_all_SERC = np.around(np.divide([CT_GenE_NZ_SERC, CT_GenE_NE2050_SERC, CT_GenE_NE2040_SERC, CT_GenE_NE2030_SERC, CT_GenE_NE2020_SERC], 1000), decimals=1)
    CCCCS_Gen_all_SERC = np.around(np.divide([CCCCS_GenE_NZ_SERC + CCCCS_GenN_NZ_SERC, CCCCS_GenE_NE2050_SERC + CCCCS_GenN_NE2050_SERC,
                                              CCCCS_GenE_NE2040_SERC + CCCCS_GenN_NE2040_SERC, CCCCS_GenE_NE2030_SERC + CCCCS_GenN_NE2030_SERC,
                                              CCCCS_GenE_NE2020_SERC + CCCCS_GenN_NE2020_SERC], 1000), decimals=1)
    OG_Gen_all_SERC = np.around(np.divide([OG_GenE_NZ_SERC, OG_GenE_NE2050_SERC, OG_GenE_NE2040_SERC, OG_GenE_NE2030_SERC, OG_GenE_NE2020_SERC], 1000), decimals=1)
    nuclear_Gen_new_SERC = np.around(np.divide([nuclear_GenN_NZ_SERC, nuclear_GenN_NE2050_SERC, nuclear_GenN_NE2040_SERC,
                                                nuclear_GenN_NE2030_SERC, nuclear_GenN_NE2020_SERC], 1000), decimals=1)
    nuclear_Gen_existing_SERC = np.around(np.divide([nuclear_GenE_NZ_SERC, nuclear_GenE_NE2050_SERC, nuclear_GenE_NE2040_SERC,
                                                     nuclear_GenE_NE2030_SERC, nuclear_GenE_NE2020_SERC], 1000), decimals=1)
    wind_Gen_all_SERC = np.around(np.divide([wind_GenE_NZ_SERC + wind_GenN_NZ_SERC, wind_GenE_NE2050_SERC + wind_GenN_NE2050_SERC,
                                             wind_GenE_NE2040_SERC + wind_GenN_NE2040_SERC, wind_GenE_NE2030_SERC + wind_GenN_NE2030_SERC,
                                             wind_GenE_NE2020_SERC + wind_GenN_NE2020_SERC], 1000), decimals=1)
    solar_Gen_all_SERC = np.around(np.divide([solar_GenE_NZ_SERC + solar_GenN_NZ_SERC, solar_GenE_NE2050_SERC + solar_GenN_NE2050_SERC,
                                              solar_GenE_NE2040_SERC + solar_GenN_NE2040_SERC, solar_GenE_NE2030_SERC + solar_GenN_NE2030_SERC,
                                              solar_GenE_NE2020_SERC + solar_GenN_NE2020_SERC], 1000), decimals=1)
    battery_Gen_all_SERC = np.around(np.divide([battery_GenE_NZ_SERC + battery_GenN_NZ_SERC, battery_GenE_NE2050_SERC + battery_GenN_NE2050_SERC,
                                                battery_GenE_NE2040_SERC + battery_GenN_NE2040_SERC, battery_GenE_NE2030_SERC + battery_GenN_NE2030_SERC,
                                                battery_GenE_NE2020_SERC + battery_GenN_NE2020_SERC], 1000), decimals=1)
    hydrogen_Gen_all_SERC = np.around(np.divide([hydrogen_GenE_NZ_SERC + hydrogen_GenN_NZ_SERC, hydrogen_GenE_NE2050_SERC + hydrogen_GenN_NE2050_SERC,
                                                 hydrogen_GenE_NE2040_SERC + hydrogen_GenN_NE2040_SERC, hydrogen_GenE_NE2030_SERC + hydrogen_GenN_NE2030_SERC,
                                                 hydrogen_GenE_NE2020_SERC + hydrogen_GenN_NE2020_SERC], 1000), decimals=1)
    pump_Gen_all_SERC = np.around(np.divide([pump_GenE_NZ_SERC, pump_GenE_NE2050_SERC, pump_GenE_NE2040_SERC, pump_GenE_NE2030_SERC, pump_GenE_NE2020_SERC], 1000), decimals=1)
    others_Gen_all_SERC = np.around(np.divide([Others_GenE_NZ_SERC, Others_GenE_NE2050_SERC, Others_GenE_NE2040_SERC, Others_GenE_NE2030_SERC, Others_GenE_NE2020_SERC], 1000), decimals=1)

    # MISO:
    dac_Gen_all_MISO = np.around(np.divide([dac_GenE_NZ_MISO + dac_GenN_NZ_MISO, dac_GenE_NE2050_MISO + dac_GenN_NE2050_MISO,
                                            dac_GenE_NE2040_MISO + dac_GenN_NE2040_MISO, dac_GenE_NE2030_MISO + dac_GenN_NE2030_MISO,
                                            dac_GenE_NE2020_MISO + dac_GenN_NE2020_MISO], 1000), decimals=1)
    Coal_Gen_all_MISO = np.around(np.divide([Coal_GenE_NZ_MISO + CoalCCS_GenN_NZ_MISO, Coal_GenE_NE2050_MISO + CoalCCS_GenN_NE2050_MISO,
                                             Coal_GenE_NE2040_MISO + CoalCCS_GenN_NE2040_MISO, Coal_GenE_NE2030_MISO + CoalCCS_GenN_NE2030_MISO,
                                             Coal_GenE_NE2020_MISO + CoalCCS_GenN_NE2020_MISO], 1000), decimals=1)
    CC_Gen_all_MISO = np.around(np.divide([CC_GenE_NZ_MISO + CC_GenN_NZ_MISO, CC_GenE_NE2050_MISO + CC_GenN_NE2050_MISO, CC_GenE_NE2040_MISO + CC_GenN_NE2040_MISO,
                                           CC_GenE_NE2030_MISO + CC_GenN_NE2030_MISO, CC_GenE_NE2020_MISO + CC_GenN_NE2020_MISO], 1000), decimals=1)
    CT_Gen_all_MISO = np.around(np.divide([CT_GenE_NZ_MISO, CT_GenE_NE2050_MISO, CT_GenE_NE2040_MISO, CT_GenE_NE2030_MISO, CT_GenE_NE2020_MISO], 1000), decimals=1)
    CCCCS_Gen_all_MISO = np.around(np.divide([CCCCS_GenE_NZ_MISO + CCCCS_GenN_NZ_MISO, CCCCS_GenE_NE2050_MISO + CCCCS_GenN_NE2050_MISO,
                                              CCCCS_GenE_NE2040_MISO + CCCCS_GenN_NE2040_MISO, CCCCS_GenE_NE2030_MISO + CCCCS_GenN_NE2030_MISO,
                                              CCCCS_GenE_NE2020_MISO + CCCCS_GenN_NE2020_MISO], 1000), decimals=1)
    OG_Gen_all_MISO = np.around(np.divide([OG_GenE_NZ_MISO, OG_GenE_NE2050_MISO, OG_GenE_NE2040_MISO, OG_GenE_NE2030_MISO, OG_GenE_NE2020_MISO], 1000), decimals=1)

    nuclear_Gen_new_MISO = np.around(np.divide([nuclear_GenN_NZ_MISO, nuclear_GenN_NE2050_MISO, nuclear_GenN_NE2040_MISO,
                                                nuclear_GenN_NE2030_MISO, nuclear_GenN_NE2020_MISO], 1000), decimals=1)
    nuclear_Gen_existing_MISO = np.around(np.divide([nuclear_GenE_NZ_MISO, nuclear_GenE_NE2050_MISO, nuclear_GenE_NE2040_MISO,
                                                     nuclear_GenE_NE2030_MISO, nuclear_GenE_NE2020_MISO], 1000), decimals=1)
    wind_Gen_all_MISO = np.around(np.divide([wind_GenE_NZ_MISO + wind_GenN_NZ_MISO, wind_GenE_NE2050_MISO + wind_GenN_NE2050_MISO,
                                             wind_GenE_NE2040_MISO + wind_GenN_NE2040_MISO, wind_GenE_NE2030_MISO + wind_GenN_NE2030_MISO,
                                             wind_GenE_NE2020_MISO + wind_GenN_NE2020_MISO], 1000), decimals=1)
    solar_Gen_all_MISO = np.around(np.divide([solar_GenE_NZ_MISO + solar_GenN_NZ_MISO, solar_GenE_NE2050_MISO + solar_GenN_NE2050_MISO,
                                              solar_GenE_NE2040_MISO + solar_GenN_NE2040_MISO, solar_GenE_NE2030_MISO + solar_GenN_NE2030_MISO,
                                              solar_GenE_NE2020_MISO + solar_GenN_NE2020_MISO], 1000), decimals=1)
    battery_Gen_all_MISO = np.around(np.divide([battery_GenE_NZ_MISO + battery_GenN_NZ_MISO, battery_GenE_NE2050_MISO + battery_GenN_NE2050_MISO,
                                                battery_GenE_NE2040_MISO + battery_GenN_NE2040_MISO, battery_GenE_NE2030_MISO + battery_GenN_NE2030_MISO,
                                                battery_GenE_NE2020_MISO + battery_GenN_NE2020_MISO], 1000), decimals=1)
    hydrogen_Gen_all_MISO = np.around(np.divide([hydrogen_GenE_NZ_MISO + hydrogen_GenN_NZ_MISO, hydrogen_GenE_NE2050_MISO + hydrogen_GenN_NE2050_MISO,
                                                 hydrogen_GenE_NE2040_MISO + hydrogen_GenN_NE2040_MISO, hydrogen_GenE_NE2030_MISO + hydrogen_GenN_NE2030_MISO,
                                                 hydrogen_GenE_NE2020_MISO + hydrogen_GenN_NE2020_MISO], 1000), decimals=1)
    pump_Gen_all_MISO = np.around(np.divide([pump_GenE_NZ_MISO, pump_GenE_NE2050_MISO, pump_GenE_NE2040_MISO, pump_GenE_NE2030_MISO, pump_GenE_NE2020_MISO], 1000), decimals=1)
    others_Gen_all_MISO = np.around(np.divide([Others_GenE_NZ_MISO, Others_GenE_NE2050_MISO, Others_GenE_NE2040_MISO, Others_GenE_NE2030_MISO, Others_GenE_NE2020_MISO], 1000), decimals=1)

    # NE:
    dac_Gen_all_NE = np.around(np.divide([dac_GenE_NZ_NE + dac_GenN_NZ_NE, dac_GenE_NE2050_NE + dac_GenN_NE2050_NE,
                                          dac_GenE_NE2040_NE + dac_GenN_NE2040_NE, dac_GenE_NE2030_NE + dac_GenN_NE2030_NE,
                                          dac_GenE_NE2020_NE + dac_GenN_NE2020_NE], 1000), decimals=1)
    Coal_Gen_all_NE = np.around(np.divide([Coal_GenE_NZ_NE + CoalCCS_GenN_NZ_NE, Coal_GenE_NE2050_NE + CoalCCS_GenN_NE2050_NE,
                                           Coal_GenE_NE2040_NE + CoalCCS_GenN_NE2040_NE, Coal_GenE_NE2030_NE + CoalCCS_GenN_NE2030_NE,
                                           Coal_GenE_NE2020_NE + CoalCCS_GenN_NE2020_NE], 1000), decimals=1)
    CC_Gen_all_NE = np.around(np.divide([CC_GenE_NZ_NE + CC_GenN_NZ_NE, CC_GenE_NE2050_NE + CC_GenN_NE2050_NE, CC_GenE_NE2040_NE + CC_GenN_NE2040_NE,
                                         CC_GenE_NE2030_NE + CC_GenN_NE2030_NE, CC_GenE_NE2020_NE + CC_GenN_NE2020_NE], 1000), decimals=1)
    CT_Gen_all_NE = np.around(np.divide([CT_GenE_NZ_NE, CT_GenE_NE2050_NE, CT_GenE_NE2040_NE, CT_GenE_NE2030_NE, CT_GenE_NE2020_NE], 1000), decimals=1)
    CCCCS_Gen_all_NE = np.around(np.divide([CCCCS_GenE_NZ_NE + CCCCS_GenN_NZ_NE, CCCCS_GenE_NE2050_NE + CCCCS_GenN_NE2050_NE,
                                            CCCCS_GenE_NE2040_NE + CCCCS_GenN_NE2040_NE, CCCCS_GenE_NE2030_NE + CCCCS_GenN_NE2030_NE,
                                            CCCCS_GenE_NE2020_NE + CCCCS_GenN_NE2020_NE], 1000), decimals=1)
    OG_Gen_all_NE = np.around(np.divide([OG_GenE_NZ_NE, OG_GenE_NE2050_NE, OG_GenE_NE2040_NE, OG_GenE_NE2030_NE, OG_GenE_NE2020_NE], 1000), decimals=1)

    nuclear_Gen_new_NE = np.around(np.divide([nuclear_GenN_NZ_NE, nuclear_GenN_NE2050_NE, nuclear_GenN_NE2040_NE,
                                              nuclear_GenN_NE2030_NE, nuclear_GenN_NE2020_NE], 1000), decimals=1)
    nuclear_Gen_existing_NE = np.around(np.divide([nuclear_GenE_NZ_NE, nuclear_GenE_NE2050_NE, nuclear_GenE_NE2040_NE,
                                                   nuclear_GenE_NE2030_NE, nuclear_GenE_NE2020_NE], 1000), decimals=1)
    wind_Gen_all_NE = np.around(np.divide([wind_GenE_NZ_NE + wind_GenN_NZ_NE, wind_GenE_NE2050_NE + wind_GenN_NE2050_NE,
                                           wind_GenE_NE2040_NE + wind_GenN_NE2040_NE, wind_GenE_NE2030_NE + wind_GenN_NE2030_NE,
                                           wind_GenE_NE2020_NE + wind_GenN_NE2020_NE], 1000), decimals=1)
    solar_Gen_all_NE = np.around(np.divide([solar_GenE_NZ_NE + solar_GenN_NZ_NE, solar_GenE_NE2050_NE + solar_GenN_NE2050_NE,
                                            solar_GenE_NE2040_NE + solar_GenN_NE2040_NE, solar_GenE_NE2030_NE + solar_GenN_NE2030_NE,
                                            solar_GenE_NE2020_NE + solar_GenN_NE2020_NE], 1000), decimals=1)
    battery_Gen_all_NE = np.around(np.divide([battery_GenE_NZ_NE + battery_GenN_NZ_NE, battery_GenE_NE2050_NE + battery_GenN_NE2050_NE,
                                              battery_GenE_NE2040_NE + battery_GenN_NE2040_NE, battery_GenE_NE2030_NE + battery_GenN_NE2030_NE,
                                              battery_GenE_NE2020_NE + battery_GenN_NE2020_NE], 1000), decimals=1)
    hydrogen_Gen_all_NE = np.around(np.divide([hydrogen_GenE_NZ_NE + hydrogen_GenN_NZ_NE, hydrogen_GenE_NE2050_NE + hydrogen_GenN_NE2050_NE,
                                               hydrogen_GenE_NE2040_NE + hydrogen_GenN_NE2040_NE, hydrogen_GenE_NE2030_NE + hydrogen_GenN_NE2030_NE,
                                               hydrogen_GenE_NE2020_NE + hydrogen_GenN_NE2020_NE], 1000), decimals=1)
    pump_Gen_all_NE = np.around(np.divide([pump_GenE_NZ_NE, pump_GenE_NE2050_NE, pump_GenE_NE2040_NE, pump_GenE_NE2030_NE, pump_GenE_NE2020_NE], 1000), decimals=1)
    others_Gen_all_NE = np.around(np.divide([Others_GenE_NZ_NE, Others_GenE_NE2050_NE, Others_GenE_NE2040_NE, Others_GenE_NE2030_NE, Others_GenE_NE2020_NE], 1000), decimals=1)

    # NY:
    dac_Gen_all_NY = np.around(np.divide([dac_GenE_NZ_NY + dac_GenN_NZ_NY, dac_GenE_NE2050_NY + dac_GenN_NE2050_NY,
                                          dac_GenE_NE2040_NY + dac_GenN_NE2040_NY, dac_GenE_NE2030_NY + dac_GenN_NE2030_NY,
                                          dac_GenE_NE2020_NY + dac_GenN_NE2020_NY], 1000), decimals=1)
    Coal_Gen_all_NY = np.around(np.divide([Coal_GenE_NZ_NY + CoalCCS_GenN_NZ_NY, Coal_GenE_NE2050_NY + CoalCCS_GenN_NE2050_NY,
                                           Coal_GenE_NE2040_NY + CoalCCS_GenN_NE2040_NY, Coal_GenE_NE2030_NY + CoalCCS_GenN_NE2030_NY,
                                           Coal_GenE_NE2020_NY + CoalCCS_GenN_NE2020_NY], 1000), decimals=1)
    CC_Gen_all_NY = np.around(np.divide([CC_GenE_NZ_NY + CC_GenN_NZ_NY, CC_GenE_NE2050_NY + CC_GenN_NE2050_NY, CC_GenE_NE2040_NY + CC_GenN_NE2040_NY,
                                         CC_GenE_NE2030_NY + CC_GenN_NE2030_NY, CC_GenE_NE2020_NY + CC_GenN_NE2020_NY], 1000), decimals=1)
    CT_Gen_all_NY = np.around(np.divide([CT_GenE_NZ_NY, CT_GenE_NE2050_NY, CT_GenE_NE2040_NY, CT_GenE_NE2030_NY, CT_GenE_NE2020_NY], 1000), decimals=1)
    CCCCS_Gen_all_NY = np.around(np.divide([CCCCS_GenE_NZ_NY + CCCCS_GenN_NZ_NY, CCCCS_GenE_NE2050_NY + CCCCS_GenN_NE2050_NY,
                                            CCCCS_GenE_NE2040_NY + CCCCS_GenN_NE2040_NY, CCCCS_GenE_NE2030_NY + CCCCS_GenN_NE2030_NY,
                                            CCCCS_GenE_NE2020_NY + CCCCS_GenN_NE2020_NY], 1000), decimals=1)
    OG_Gen_all_NY = np.around(np.divide([OG_GenE_NZ_NY, OG_GenE_NE2050_NY, OG_GenE_NE2040_NY, OG_GenE_NE2030_NY, OG_GenE_NE2020_NY], 1000), decimals=1)

    nuclear_Gen_new_NY = np.around(np.divide([nuclear_GenN_NZ_NY, nuclear_GenN_NE2050_NY, nuclear_GenN_NE2040_NY,
                                              nuclear_GenN_NE2030_NY, nuclear_GenN_NE2020_NY], 1000), decimals=1)
    nuclear_Gen_existing_NY = np.around(np.divide([nuclear_GenE_NZ_NY, nuclear_GenE_NE2050_NY, nuclear_GenE_NE2040_NY,
                                                   nuclear_GenE_NE2030_NY, nuclear_GenE_NE2020_NY], 1000), decimals=1)
    wind_Gen_all_NY = np.around(np.divide([wind_GenE_NZ_NY + wind_GenN_NZ_NY, wind_GenE_NE2050_NY + wind_GenN_NE2050_NY,
                                           wind_GenE_NE2040_NY + wind_GenN_NE2040_NY, wind_GenE_NE2030_NY + wind_GenN_NE2030_NY,
                                           wind_GenE_NE2020_NY + wind_GenN_NE2020_NY], 1000), decimals=1)
    solar_Gen_all_NY = np.around(np.divide([solar_GenE_NZ_NY + solar_GenN_NZ_NY, solar_GenE_NE2050_NY + solar_GenN_NE2050_NY,
                                            solar_GenE_NE2040_NY + solar_GenN_NE2040_NY, solar_GenE_NE2030_NY + solar_GenN_NE2030_NY,
                                            solar_GenE_NE2020_NY + solar_GenN_NE2020_NY], 1000), decimals=1)
    battery_Gen_all_NY = np.around(np.divide([battery_GenE_NZ_NY + battery_GenN_NZ_NY, battery_GenE_NE2050_NY + battery_GenN_NE2050_NY,
                                              battery_GenE_NE2040_NY + battery_GenN_NE2040_NY, battery_GenE_NE2030_NY + battery_GenN_NE2030_NY,
                                              battery_GenE_NE2020_NY + battery_GenN_NE2020_NY], 1000), decimals=1)
    hydrogen_Gen_all_NY = np.around(np.divide([hydrogen_GenE_NZ_NY + hydrogen_GenN_NZ_NY, hydrogen_GenE_NE2050_NY + hydrogen_GenN_NE2050_NY,
                                               hydrogen_GenE_NE2040_NY + hydrogen_GenN_NE2040_NY, hydrogen_GenE_NE2030_NY + hydrogen_GenN_NE2030_NY,
                                               hydrogen_GenE_NE2020_NY + hydrogen_GenN_NE2020_NY], 1000), decimals=1)
    pump_Gen_all_NY = np.around(np.divide([pump_GenE_NZ_NY, pump_GenE_NE2050_NY, pump_GenE_NE2040_NY, pump_GenE_NE2030_NY, pump_GenE_NE2020_NY], 1000), decimals=1)
    others_Gen_all_NY = np.around(np.divide([Others_GenE_NZ_NY, Others_GenE_NE2050_NY, Others_GenE_NE2040_NY, Others_GenE_NE2030_NY, Others_GenE_NE2020_NY], 1000), decimals=1)

    # PJM:
    dac_Gen_all_PJM = np.around(np.divide([dac_GenE_NZ_PJM + dac_GenN_NZ_PJM, dac_GenE_NE2050_PJM + dac_GenN_NE2050_PJM,
                                           dac_GenE_NE2040_PJM + dac_GenN_NE2040_PJM, dac_GenE_NE2030_PJM + dac_GenN_NE2030_PJM,
                                           dac_GenE_NE2020_PJM + dac_GenN_NE2020_PJM], 1000), decimals=1)
    Coal_Gen_all_PJM = np.around(np.divide([Coal_GenE_NZ_PJM + CoalCCS_GenN_NZ_PJM, Coal_GenE_NE2050_PJM + CoalCCS_GenN_NE2050_PJM,
                                            Coal_GenE_NE2040_PJM + CoalCCS_GenN_NE2040_PJM, Coal_GenE_NE2030_PJM + CoalCCS_GenN_NE2030_PJM,
                                            Coal_GenE_NE2020_PJM + CoalCCS_GenN_NE2020_PJM], 1000), decimals=1)
    CC_Gen_all_PJM = np.around(np.divide([CC_GenE_NZ_PJM + CC_GenN_NZ_PJM, CC_GenE_NE2050_PJM + CC_GenN_NE2050_PJM, CC_GenE_NE2040_PJM + CC_GenN_NE2040_PJM,
                                          CC_GenE_NE2030_PJM + CC_GenN_NE2030_PJM, CC_GenE_NE2020_PJM + CC_GenN_NE2020_PJM], 1000), decimals=1)
    CT_Gen_all_PJM = np.around(np.divide([CT_GenE_NZ_PJM, CT_GenE_NE2050_PJM, CT_GenE_NE2040_PJM, CT_GenE_NE2030_PJM, CT_GenE_NE2020_PJM], 1000), decimals=1)
    CCCCS_Gen_all_PJM = np.around(np.divide([CCCCS_GenE_NZ_PJM + CCCCS_GenN_NZ_PJM, CCCCS_GenE_NE2050_PJM + CCCCS_GenN_NE2050_PJM,
                                             CCCCS_GenE_NE2040_PJM + CCCCS_GenN_NE2040_PJM, CCCCS_GenE_NE2030_PJM + CCCCS_GenN_NE2030_PJM,
                                             CCCCS_GenE_NE2020_PJM + CCCCS_GenN_NE2020_PJM], 1000), decimals=1)
    OG_Gen_all_PJM = np.around(np.divide([OG_GenE_NZ_PJM, OG_GenE_NE2050_PJM, OG_GenE_NE2040_PJM, OG_GenE_NE2030_PJM, OG_GenE_NE2020_PJM], 1000), decimals=1)

    nuclear_Gen_new_PJM = np.around(np.divide([nuclear_GenN_NZ_PJM, nuclear_GenN_NE2050_PJM, nuclear_GenN_NE2040_PJM,
                                               nuclear_GenN_NE2030_PJM, nuclear_GenN_NE2020_PJM], 1000), decimals=1)
    nuclear_Gen_existing_PJM = np.around(np.divide([nuclear_GenE_NZ_PJM, nuclear_GenE_NE2050_PJM, nuclear_GenE_NE2040_PJM,
                                                    nuclear_GenE_NE2030_PJM, nuclear_GenE_NE2020_PJM], 1000), decimals=1)
    wind_Gen_all_PJM = np.around(np.divide([wind_GenE_NZ_PJM + wind_GenN_NZ_PJM, wind_GenE_NE2050_PJM + wind_GenN_NE2050_PJM,
                                            wind_GenE_NE2040_PJM + wind_GenN_NE2040_PJM, wind_GenE_NE2030_PJM + wind_GenN_NE2030_PJM,
                                            wind_GenE_NE2020_PJM + wind_GenN_NE2020_PJM], 1000), decimals=1)
    solar_Gen_all_PJM = np.around(np.divide([solar_GenE_NZ_PJM + solar_GenN_NZ_PJM, solar_GenE_NE2050_PJM + solar_GenN_NE2050_PJM,
                                             solar_GenE_NE2040_PJM + solar_GenN_NE2040_PJM, solar_GenE_NE2030_PJM + solar_GenN_NE2030_PJM,
                                             solar_GenE_NE2020_PJM + solar_GenN_NE2020_PJM], 1000), decimals=1)
    battery_Gen_all_PJM = np.around(np.divide([battery_GenE_NZ_PJM + battery_GenN_NZ_PJM, battery_GenE_NE2050_PJM + battery_GenN_NE2050_PJM,
                                               battery_GenE_NE2040_PJM + battery_GenN_NE2040_PJM, battery_GenE_NE2030_PJM + battery_GenN_NE2030_PJM,
                                               battery_GenE_NE2020_PJM + battery_GenN_NE2020_PJM], 1000), decimals=1)
    hydrogen_Gen_all_PJM = np.around(np.divide([hydrogen_GenE_NZ_PJM + hydrogen_GenN_NZ_PJM, hydrogen_GenE_NE2050_PJM + hydrogen_GenN_NE2050_PJM,
                                                hydrogen_GenE_NE2040_PJM + hydrogen_GenN_NE2040_PJM, hydrogen_GenE_NE2030_PJM + hydrogen_GenN_NE2030_PJM,
                                                hydrogen_GenE_NE2020_PJM + hydrogen_GenN_NE2020_PJM], 1000), decimals=1)
    pump_Gen_all_PJM = np.around(np.divide([pump_GenE_NZ_PJM, pump_GenE_NE2050_PJM, pump_GenE_NE2040_PJM, pump_GenE_NE2030_PJM, pump_GenE_NE2020_PJM], 1000), decimals=1)
    others_Gen_all_PJM = np.around(np.divide([Others_GenE_NZ_PJM, Others_GenE_NE2050_PJM, Others_GenE_NE2040_PJM, Others_GenE_NE2030_PJM, Others_GenE_NE2020_PJM], 1000), decimals=1)

    # SPP:
    dac_Gen_all_SPP = np.around(np.divide([dac_GenE_NZ_SPP + dac_GenN_NZ_SPP, dac_GenE_NE2050_SPP + dac_GenN_NE2050_SPP,
                                           dac_GenE_NE2040_SPP + dac_GenN_NE2040_SPP, dac_GenE_NE2030_SPP + dac_GenN_NE2030_SPP,
                                           dac_GenE_NE2020_SPP + dac_GenN_NE2020_SPP], 1000), decimals=1)
    Coal_Gen_all_SPP = np.around(np.divide([Coal_GenE_NZ_SPP + CoalCCS_GenN_NZ_SPP, Coal_GenE_NE2050_SPP + CoalCCS_GenN_NE2050_SPP,
                                            Coal_GenE_NE2040_SPP + CoalCCS_GenN_NE2040_SPP, Coal_GenE_NE2030_SPP + CoalCCS_GenN_NE2030_SPP,
                                            Coal_GenE_NE2020_SPP + CoalCCS_GenN_NE2020_SPP], 1000), decimals=1)
    CC_Gen_all_SPP = np.around(np.divide([CC_GenE_NZ_SPP + CC_GenN_NZ_SPP, CC_GenE_NE2050_SPP + CC_GenN_NE2050_SPP, CC_GenE_NE2040_SPP + CC_GenN_NE2040_SPP,
                                          CC_GenE_NE2030_SPP + CC_GenN_NE2030_SPP, CC_GenE_NE2020_SPP + CC_GenN_NE2020_SPP], 1000), decimals=1)
    CT_Gen_all_SPP = np.around(np.divide([CT_GenE_NZ_SPP, CT_GenE_NE2050_SPP, CT_GenE_NE2040_SPP, CT_GenE_NE2030_SPP, CT_GenE_NE2020_SPP], 1000), decimals=1)
    CCCCS_Gen_all_SPP = np.around(np.divide([CCCCS_GenE_NZ_SPP + CCCCS_GenN_NZ_SPP, CCCCS_GenE_NE2050_SPP + CCCCS_GenN_NE2050_SPP,
                                             CCCCS_GenE_NE2040_SPP + CCCCS_GenN_NE2040_SPP, CCCCS_GenE_NE2030_SPP + CCCCS_GenN_NE2030_SPP,
                                             CCCCS_GenE_NE2020_SPP + CCCCS_GenN_NE2020_SPP], 1000), decimals=1)
    OG_Gen_all_SPP = np.around(np.divide([OG_GenE_NZ_SPP, OG_GenE_NE2050_SPP, OG_GenE_NE2040_SPP, OG_GenE_NE2030_SPP, OG_GenE_NE2020_SPP], 1000), decimals=1)

    nuclear_Gen_new_SPP = np.around(np.divide([nuclear_GenN_NZ_SPP, nuclear_GenN_NE2050_SPP, nuclear_GenN_NE2040_SPP,
                                               nuclear_GenN_NE2030_SPP, nuclear_GenN_NE2020_SPP], 1000), decimals=1)
    nuclear_Gen_existing_SPP = np.around(np.divide([nuclear_GenE_NZ_SPP, nuclear_GenE_NE2050_SPP, nuclear_GenE_NE2040_SPP,
                                                    nuclear_GenE_NE2030_SPP, nuclear_GenE_NE2020_SPP], 1000), decimals=1)
    wind_Gen_all_SPP = np.around(np.divide([wind_GenE_NZ_SPP + wind_GenN_NZ_SPP, wind_GenE_NE2050_SPP + wind_GenN_NE2050_SPP,
                                            wind_GenE_NE2040_SPP + wind_GenN_NE2040_SPP, wind_GenE_NE2030_SPP + wind_GenN_NE2030_SPP,
                                            wind_GenE_NE2020_SPP + wind_GenN_NE2020_SPP], 1000), decimals=1)
    solar_Gen_all_SPP = np.around(np.divide([solar_GenE_NZ_SPP + solar_GenN_NZ_SPP, solar_GenE_NE2050_SPP + solar_GenN_NE2050_SPP,
                                             solar_GenE_NE2040_SPP + solar_GenN_NE2040_SPP, solar_GenE_NE2030_SPP + solar_GenN_NE2030_SPP,
                                             solar_GenE_NE2020_SPP + solar_GenN_NE2020_SPP], 1000), decimals=1)
    battery_Gen_all_SPP = np.around(np.divide([battery_GenE_NZ_SPP + battery_GenN_NZ_SPP, battery_GenE_NE2050_SPP + battery_GenN_NE2050_SPP,
                                               battery_GenE_NE2040_SPP + battery_GenN_NE2040_SPP, battery_GenE_NE2030_SPP + battery_GenN_NE2030_SPP,
                                               battery_GenE_NE2020_SPP + battery_GenN_NE2020_SPP], 1000), decimals=1)
    hydrogen_Gen_all_SPP = np.around(np.divide([hydrogen_GenE_NZ_SPP + hydrogen_GenN_NZ_SPP, hydrogen_GenE_NE2050_SPP + hydrogen_GenN_NE2050_SPP,
                                                hydrogen_GenE_NE2040_SPP + hydrogen_GenN_NE2040_SPP, hydrogen_GenE_NE2030_SPP + hydrogen_GenN_NE2030_SPP,
                                                hydrogen_GenE_NE2020_SPP + hydrogen_GenN_NE2020_SPP], 1000), decimals=1)
    pump_Gen_all_SPP = np.around(np.divide([pump_GenE_NZ_SPP, pump_GenE_NE2050_SPP, pump_GenE_NE2040_SPP, pump_GenE_NE2030_SPP, pump_GenE_NE2020_SPP], 1000), decimals=1)
    others_Gen_all_SPP = np.around(np.divide([Others_GenE_NZ_SPP, Others_GenE_NE2050_SPP, Others_GenE_NE2040_SPP, Others_GenE_NE2030_SPP, Others_GenE_NE2020_SPP], 1000), decimals=1)

    # Load:
    load_serc_NZ = resultsLoad_NZ.SERC.sum() / 1000000
    load_ny_NZ = resultsLoad_NZ.NY.sum() / 1000000
    load_ne_NZ = resultsLoad_NZ.NE.sum() / 1000000
    load_miso_NZ = resultsLoad_NZ.MISO.sum() / 1000000
    load_pjm_NZ = resultsLoad_NZ.PJM.sum() / 1000000
    load_spp_NZ = resultsLoad_NZ.SPP.sum() / 1000000
    load_tot_NZ = load_serc_NZ + load_ny_NZ + load_ne_NZ + load_miso_NZ + load_pjm_NZ + load_spp_NZ

    load_serc_NE2020 = resultsLoad_NE2020.SERC.sum() / 1000000
    load_ny_NE2020 = resultsLoad_NE2020.NY.sum() / 1000000
    load_ne_NE2020 = resultsLoad_NE2020.NE.sum() / 1000000
    load_miso_NE2020 = resultsLoad_NE2020.MISO.sum() / 1000000
    load_pjm_NE2020 = resultsLoad_NE2020.PJM.sum() / 1000000
    load_spp_NE2020 = resultsLoad_NE2020.SPP.sum() / 1000000
    load_tot_NE2020 = load_serc_NE2020 + load_ny_NE2020 + load_ne_NE2020 \
                      + load_miso_NE2020 + load_pjm_NE2020 + load_spp_NE2020

    load_serc_NE2030 = resultsLoad_NE2030.SERC.sum() / 1000000
    load_ny_NE2030 = resultsLoad_NE2030.NY.sum() / 1000000
    load_ne_NE2030 = resultsLoad_NE2030.NE.sum() / 1000000
    load_miso_NE2030 = resultsLoad_NE2030.MISO.sum() / 1000000
    load_pjm_NE2030 = resultsLoad_NE2030.PJM.sum() / 1000000
    load_spp_NE2030 = resultsLoad_NE2030.SPP.sum() / 1000000
    load_tot_NE2030 = load_serc_NE2030 + load_ny_NE2030 + load_ne_NE2030 \
                      + load_miso_NE2030 + load_pjm_NE2030 + load_spp_NE2030

    load_serc_NE2040 = resultsLoad_NE2040.SERC.sum() / 1000000
    load_ny_NE2040 = resultsLoad_NE2040.NY.sum() / 1000000
    load_ne_NE2040 = resultsLoad_NE2040.NE.sum() / 1000000
    load_miso_NE2040 = resultsLoad_NE2040.MISO.sum() / 1000000
    load_pjm_NE2040 = resultsLoad_NE2040.PJM.sum() / 1000000
    load_spp_NE2040 = resultsLoad_NE2040.SPP.sum() / 1000000
    load_tot_NE2040 = load_serc_NE2040 + load_ny_NE2040 + load_ne_NE2040 \
                      + load_miso_NE2040 + load_pjm_NE2040 + load_spp_NE2040

    load_serc_NE2050 = resultsLoad_NE2050.SERC.sum() / 1000000
    load_ny_NE2050 = resultsLoad_NE2050.NY.sum() / 1000000
    load_ne_NE2050 = resultsLoad_NE2050.NE.sum() / 1000000
    load_miso_NE2050 = resultsLoad_NE2050.MISO.sum() / 1000000
    load_pjm_NE2050 = resultsLoad_NE2050.PJM.sum() / 1000000
    load_spp_NE2050 = resultsLoad_NE2050.SPP.sum() / 1000000
    load_tot_NE2050 = load_serc_NE2050 + load_ny_NE2050 + load_ne_NE2050 \
                      + load_miso_NE2050 + load_pjm_NE2050 + load_spp_NE2050

    load_tot = [load_tot_NZ,load_tot_NE2050,load_tot_NE2040,load_tot_NE2030,load_tot_NE2020]
    load_serc = [load_serc_NZ, load_serc_NE2050, load_serc_NE2040, load_serc_NE2030, load_serc_NE2020]
    load_miso = [load_miso_NZ, load_miso_NE2050, load_miso_NE2040, load_miso_NE2030, load_miso_NE2020]
    load_ne = [load_ne_NZ, load_ne_NE2050, load_ne_NE2040, load_ne_NE2030, load_ne_NE2020]
    load_ny = [load_ny_NZ, load_ny_NE2050, load_ny_NE2040, load_ny_NE2030, load_ny_NE2020]
    load_pjm = [load_pjm_NZ, load_pjm_NE2050, load_pjm_NE2040, load_pjm_NE2030, load_pjm_NE2020]
    load_spp = [load_spp_NZ, load_spp_NE2050, load_spp_NE2040, load_spp_NE2030, load_spp_NE2020]

    return (dac_Gen_all, Coal_Gen_all, CT_Gen_all, OG_Gen_all, CC_Gen_all, CCCCS_Gen_all,
            nuclear_Gen_all, wind_Gen_all, solar_Gen_all, pump_Gen_all, battery_Gen_all, hydrogen_Gen_all,
            others_Gen_all, dac_Gen_MISO, dac_Gen_NE, dac_Gen_NY, dac_Gen_PJM, dac_Gen_SERC, dac_Gen_SPP,
            dac_Gen_all_SERC, Coal_Gen_all_SERC, CT_Gen_all_SERC, OG_Gen_all_SERC, CC_Gen_all_SERC, CCCCS_Gen_all_SERC,
            nuclear_Gen_new_SERC, nuclear_Gen_existing_SERC, wind_Gen_all_SERC, solar_Gen_all_SERC, pump_Gen_all_SERC,
            battery_Gen_all_SERC, hydrogen_Gen_all_SERC, others_Gen_all_SERC, dac_Gen_all_MISO, Coal_Gen_all_MISO,
            CT_Gen_all_MISO, OG_Gen_all_MISO, CC_Gen_all_MISO, CCCCS_Gen_all_MISO, nuclear_Gen_new_MISO, nuclear_Gen_existing_MISO,
            wind_Gen_all_MISO, solar_Gen_all_MISO, pump_Gen_all_MISO, battery_Gen_all_MISO, hydrogen_Gen_all_MISO, others_Gen_all_MISO,
            dac_Gen_all_NE, Coal_Gen_all_NE, CT_Gen_all_NE, OG_Gen_all_NE, CC_Gen_all_NE, CCCCS_Gen_all_NE, nuclear_Gen_new_NE,
            nuclear_Gen_existing_NE, wind_Gen_all_NE, solar_Gen_all_NE, pump_Gen_all_NE, battery_Gen_all_NE, hydrogen_Gen_all_NE,
            others_Gen_all_NE, dac_Gen_all_NY, Coal_Gen_all_NY, CT_Gen_all_NY, OG_Gen_all_NY, CC_Gen_all_NY, CCCCS_Gen_all_NY,
            nuclear_Gen_new_NY, nuclear_Gen_existing_NY, wind_Gen_all_NY, solar_Gen_all_NY, pump_Gen_all_NY, battery_Gen_all_NY,
            hydrogen_Gen_all_NY, others_Gen_all_NY, dac_Gen_all_PJM, Coal_Gen_all_PJM, CT_Gen_all_PJM, OG_Gen_all_PJM, CC_Gen_all_PJM,
            CCCCS_Gen_all_PJM, nuclear_Gen_new_PJM, nuclear_Gen_existing_PJM, wind_Gen_all_PJM, solar_Gen_all_PJM, pump_Gen_all_PJM,
            battery_Gen_all_PJM, hydrogen_Gen_all_PJM, others_Gen_all_PJM, dac_Gen_all_SPP, Coal_Gen_all_SPP, CT_Gen_all_SPP,
            OG_Gen_all_SPP, CC_Gen_all_SPP, CCCCS_Gen_all_SPP, nuclear_Gen_new_SPP, nuclear_Gen_existing_SPP, wind_Gen_all_SPP,
            solar_Gen_all_SPP, pump_Gen_all_SPP, battery_Gen_all_SPP, hydrogen_Gen_all_SPP, others_Gen_all_SPP,
            load_tot,load_serc,load_miso,load_ne,load_ny,load_pjm,load_spp)
