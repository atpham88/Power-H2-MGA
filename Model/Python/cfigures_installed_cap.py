import pandas as pd
import numpy as np

def installed_cap_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2):
    # read in new capacity investment solution:
    resultsCE_NZ = pd.read_csv(m_dir2+resultsDir_other_NZ + 'genFleetAfterCE2050.csv')
    resultsCE_NE2020 = pd.read_csv(m_dir2+resultsDir_other_NE2020 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2030 = pd.read_csv(m_dir2+resultsDir_other_NE2030 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2040 = pd.read_csv(m_dir2+resultsDir_other_NE2040 + 'genFleetAfterCE2050.csv')
    resultsCE_NE2050 = pd.read_csv(m_dir2 + resultsDir_other_NE2050_2 + 'genFleetAfterCE2060.csv')

    resultsCE_NZ = resultsCE_NZ[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2020 = resultsCE_NE2020[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2030 = resultsCE_NE2030[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2040 = resultsCE_NE2040[['PlantType', 'Capacity (MW)', 'region']]
    resultsCE_NE2050 = resultsCE_NE2050[['PlantType', 'Capacity (MW)', 'region']]

    Coal_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Coal Steam']
    CC_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Combined Cycle']
    CCCCS_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Combined Cycle CCS']
    CT_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Combustion Turbine']
    OG_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'O/G Steam']
    bio_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Biomass']
    battery_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Batter')]
    hydrogen_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Hydrogen']
    nuclear_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Nuclear']
    dac_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'DAC']
    solarN_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('solar')]
    solarE_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Solar PV']
    windN_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('wind')]
    windE_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Onshore Wind']
    pump_Cap_NZ = resultsCE_NZ.loc[resultsCE_NZ['PlantType'] == 'Pumped Storage']
    Other1_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Flywheels')]
    Other2_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Fossil Waste')]
    Other3_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Fuel Cell')]
    Other4_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('IGCC')]
    Other5_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Landfill Gas')]
    Other6_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_Cap_NZ = resultsCE_NZ[resultsCE_NZ['PlantType'].str.contains('Tires')]
    Other_NZ = Other1_Cap_NZ + Other2_Cap_NZ + Other3_Cap_NZ + Other4_Cap_NZ + Other5_Cap_NZ \
               + Other6_Cap_NZ + Other7_Cap_NZ + Other8_Cap_NZ

    # NE2020:
    Coal_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Coal Steam']
    CC_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Combined Cycle']
    CCCCS_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Combined Cycle CCS']
    CT_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Combustion Turbine']
    OG_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'O/G Steam']
    bio_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Biomass']
    battery_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Batter')]
    hydrogen_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Hydrogen']
    nuclear_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Nuclear']
    dac_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'DAC']
    solarN_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('solar')]
    solarE_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Solar PV']
    windN_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('wind')]
    windE_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Onshore Wind']
    pump_Cap_NE2020 = resultsCE_NE2020.loc[resultsCE_NE2020['PlantType'] == 'Pumped Storage']
    Other1_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Flywheels')]
    Other2_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Fossil Waste')]
    Other3_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Fuel Cell')]
    Other4_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('IGCC')]
    Other5_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Landfill Gas')]
    Other6_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_Cap_NE2020 = resultsCE_NE2020[resultsCE_NE2020['PlantType'].str.contains('Tires')]
    Other_NE2020 = Other1_Cap_NE2020 + Other2_Cap_NE2020 + Other3_Cap_NE2020 + Other4_Cap_NE2020 \
                   + Other5_Cap_NE2020 + Other6_Cap_NE2020 + Other7_Cap_NE2020 + Other8_Cap_NE2020

    # NE2030:
    Coal_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Coal Steam']
    CC_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Combined Cycle']
    CCCCS_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Combined Cycle CCS']
    CT_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Combustion Turbine']
    OG_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'O/G Steam']
    bio_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Biomass']
    battery_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Batter')]
    hydrogen_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Hydrogen']
    nuclear_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Nuclear']
    dac_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'DAC']
    solarN_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('solar')]
    solarE_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Solar PV']
    windN_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('wind')]
    windE_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Onshore Wind']
    pump_Cap_NE2030 = resultsCE_NE2030.loc[resultsCE_NE2030['PlantType'] == 'Pumped Storage']
    Other1_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Flywheels')]
    Other2_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Fossil Waste')]
    Other3_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Fuel Cell')]
    Other4_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('IGCC')]
    Other5_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Landfill Gas')]
    Other6_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_Cap_NE2030 = resultsCE_NE2030[resultsCE_NE2030['PlantType'].str.contains('Tires')]
    Other_NE2030 = Other1_Cap_NE2030 + Other2_Cap_NE2030 + Other3_Cap_NE2030 + Other4_Cap_NE2030 \
                   + Other5_Cap_NE2030 + Other6_Cap_NE2030 + Other7_Cap_NE2030 + Other8_Cap_NE2030

    # NE 2040:
    Coal_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Coal Steam']
    CC_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Combined Cycle']
    CCCCS_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Combined Cycle CCS']
    CT_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Combustion Turbine']
    OG_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'O/G Steam']
    bio_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Biomass']
    battery_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Batter')]
    hydrogen_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Hydrogen']
    nuclear_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Nuclear']
    dac_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'DAC']
    solarN_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('solar')]
    solarE_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Solar PV']
    windN_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('wind')]
    windE_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Onshore Wind']
    pump_Cap_NE2040 = resultsCE_NE2040.loc[resultsCE_NE2040['PlantType'] == 'Pumped Storage']
    Other1_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Flywheels')]
    Other2_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Fossil Waste')]
    Other3_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Fuel Cell')]
    Other4_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('IGCC')]
    Other5_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Landfill Gas')]
    Other6_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_Cap_NE2040 = resultsCE_NE2040[resultsCE_NE2040['PlantType'].str.contains('Tires')]
    Other_NE2040 = Other1_Cap_NE2040 + Other2_Cap_NE2040 + Other3_Cap_NE2040 + Other4_Cap_NE2040 \
                   + Other5_Cap_NE2040 + Other6_Cap_NE2040 + Other7_Cap_NE2040 + Other8_Cap_NE2040

    # NE 2050:
    Coal_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Coal Steam']
    CC_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Combined Cycle']
    CCCCS_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Combined Cycle CCS']
    CT_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Combustion Turbine']
    OG_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'O/G Steam']
    bio_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Biomass']
    battery_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Batter')]
    hydrogen_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Hydrogen']
    nuclear_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Nuclear']
    dac_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'DAC']
    solarN_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('solar')]
    solarE_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Solar PV']
    windN_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('wind')]
    windE_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Onshore Wind']
    pump_Cap_NE2050 = resultsCE_NE2050.loc[resultsCE_NE2050['PlantType'] == 'Pumped Storage']
    Other1_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Flywheels')]
    Other2_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Fossil Waste')]
    Other3_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Fuel Cell')]
    Other4_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('IGCC')]
    Other5_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Landfill Gas')]
    Other6_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Municipal Solid Waste')]
    Other7_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Non-Fossil Waste')]
    Other8_Cap_NE2050 = resultsCE_NE2050[resultsCE_NE2050['PlantType'].str.contains('Tires')]
    Other_NE2050 = Other1_Cap_NE2050 + Other2_Cap_NE2050 + Other3_Cap_NE2050 + Other4_Cap_NE2050 \
                   + Other5_Cap_NE2050 + Other6_Cap_NE2050 + Other7_Cap_NE2050 + Other8_Cap_NE2050

    dac_Cap_NZ = dac_Cap_NZ['Capacity (MW)'].sum()
    dac_Cap_NE2050 = dac_Cap_NE2050['Capacity (MW)'].sum()
    dac_Cap_NE2040 = dac_Cap_NE2040['Capacity (MW)'].sum()
    dac_Cap_NE2030 = dac_Cap_NE2030['Capacity (MW)'].sum()
    dac_Cap_NE2020 = dac_Cap_NE2020['Capacity (MW)'].sum()

    dac_Cap_all = np.around(np.divide([dac_Cap_NZ, dac_Cap_NE2050, dac_Cap_NE2040,
                                      dac_Cap_NE2030, dac_Cap_NE2020], 1000), decimals=1)

    Coal_Cap_NZ = Coal_Cap_NZ['Capacity (MW)'].sum()
    Coal_Cap_NE2050 = Coal_Cap_NE2050['Capacity (MW)'].sum()
    Coal_Cap_NE2040 = Coal_Cap_NE2040['Capacity (MW)'].sum()
    Coal_Cap_NE2030 = Coal_Cap_NE2030['Capacity (MW)'].sum()
    Coal_Cap_NE2020 = Coal_Cap_NE2020['Capacity (MW)'].sum()

    coal_Cap_all = np.around(np.divide([Coal_Cap_NZ, Coal_Cap_NE2050, Coal_Cap_NE2040,
                                       Coal_Cap_NE2030, Coal_Cap_NE2020], 1000), decimals=1)

    CC_Cap_NZ = CC_Cap_NZ['Capacity (MW)'].sum()
    CC_Cap_NE2050 = CC_Cap_NE2050['Capacity (MW)'].sum()
    CC_Cap_NE2040 = CC_Cap_NE2040['Capacity (MW)'].sum()
    CC_Cap_NE2030 = CC_Cap_NE2030['Capacity (MW)'].sum()
    CC_Cap_NE2020 = CC_Cap_NE2020['Capacity (MW)'].sum()

    CC_Cap_all = np.around(np.divide([CC_Cap_NZ, CC_Cap_NE2050, CC_Cap_NE2040,
                                        CC_Cap_NE2030, CC_Cap_NE2020], 1000), decimals=1)

    CCCCS_Cap_NZ = CCCCS_Cap_NZ['Capacity (MW)'].sum()
    CCCCS_Cap_NE2050 = CCCCS_Cap_NE2050['Capacity (MW)'].sum()
    CCCCS_Cap_NE2040 = CCCCS_Cap_NE2040['Capacity (MW)'].sum()
    CCCCS_Cap_NE2030 = CCCCS_Cap_NE2030['Capacity (MW)'].sum()
    CCCCS_Cap_NE2020 = CCCCS_Cap_NE2020['Capacity (MW)'].sum()

    CCCCS_Cap_all = np.around(np.divide([CCCCS_Cap_NZ, CCCCS_Cap_NE2050, CCCCS_Cap_NE2040,
                                        CCCCS_Cap_NE2030, CCCCS_Cap_NE2020], 1000), decimals=1)

    CT_Cap_NZ = CT_Cap_NZ['Capacity (MW)'].sum()
    CT_Cap_NE2050 = CT_Cap_NE2050['Capacity (MW)'].sum()
    CT_Cap_NE2040 = CT_Cap_NE2040['Capacity (MW)'].sum()
    CT_Cap_NE2030 = CT_Cap_NE2030['Capacity (MW)'].sum()
    CT_Cap_NE2020 = CT_Cap_NE2020['Capacity (MW)'].sum()

    CT_Cap_all = np.around(np.divide([CT_Cap_NZ, CT_Cap_NE2050, CT_Cap_NE2040,
                                        CT_Cap_NE2030, CT_Cap_NE2020], 1000), decimals=1)

    OG_Cap_NZ = OG_Cap_NZ['Capacity (MW)'].sum()
    OG_Cap_NE2050 = OG_Cap_NE2050['Capacity (MW)'].sum()
    OG_Cap_NE2040 = OG_Cap_NE2040['Capacity (MW)'].sum()
    OG_Cap_NE2030 = OG_Cap_NE2030['Capacity (MW)'].sum()
    OG_Cap_NE2020 = OG_Cap_NE2020['Capacity (MW)'].sum()

    OG_Cap_all = np.around(np.divide([OG_Cap_NZ, OG_Cap_NE2050, OG_Cap_NE2040,
                                     OG_Cap_NE2030, OG_Cap_NE2020], 1000), decimals=1)

    bio_Cap_NZ = bio_Cap_NZ['Capacity (MW)'].sum()
    bio_Cap_NE2050 = bio_Cap_NE2050['Capacity (MW)'].sum()
    bio_Cap_NE2040 = bio_Cap_NE2040['Capacity (MW)'].sum()
    bio_Cap_NE2030 = bio_Cap_NE2030['Capacity (MW)'].sum()
    bio_Cap_NE2020 = bio_Cap_NE2020['Capacity (MW)'].sum()

    bio_Cap_all = np.around(np.divide([bio_Cap_NZ, bio_Cap_NE2050, bio_Cap_NE2040,
                                     bio_Cap_NE2030, bio_Cap_NE2020], 1000), decimals=1)

    battery_Cap_NZ = battery_Cap_NZ['Capacity (MW)'].sum()
    battery_Cap_NE2050 = battery_Cap_NE2050['Capacity (MW)'].sum()
    battery_Cap_NE2040 = battery_Cap_NE2040['Capacity (MW)'].sum()
    battery_Cap_NE2030 = battery_Cap_NE2030['Capacity (MW)'].sum()
    battery_Cap_NE2020 = battery_Cap_NE2020['Capacity (MW)'].sum()

    bat_Cap_all = np.around(np.divide([battery_Cap_NZ, battery_Cap_NE2050, battery_Cap_NE2040,
                                       battery_Cap_NE2030, battery_Cap_NE2020], 1000), decimals=1)

    hydrogen_Cap_NZ = hydrogen_Cap_NZ['Capacity (MW)'].sum()
    hydrogen_Cap_NE2050 = hydrogen_Cap_NE2050['Capacity (MW)'].sum()
    hydrogen_Cap_NE2040 = hydrogen_Cap_NE2040['Capacity (MW)'].sum()
    hydrogen_Cap_NE2030 = hydrogen_Cap_NE2030['Capacity (MW)'].sum()
    hydrogen_Cap_NE2020 = hydrogen_Cap_NE2020['Capacity (MW)'].sum()

    h2_Cap_all = np.around(np.divide([hydrogen_Cap_NZ, hydrogen_Cap_NE2050, hydrogen_Cap_NE2040,
                                       hydrogen_Cap_NE2030, hydrogen_Cap_NE2020], 1000), decimals=1)

    nuclear_Cap_NZ = nuclear_Cap_NZ['Capacity (MW)'].sum()
    nuclear_Cap_NE2050 = nuclear_Cap_NE2050['Capacity (MW)'].sum()
    nuclear_Cap_NE2040 = nuclear_Cap_NE2040['Capacity (MW)'].sum()
    nuclear_Cap_NE2030 = nuclear_Cap_NE2030['Capacity (MW)'].sum()
    nuclear_Cap_NE2020 = nuclear_Cap_NE2020['Capacity (MW)'].sum()

    nuclear_Cap_all = np.around(np.divide([nuclear_Cap_NZ, nuclear_Cap_NE2050, nuclear_Cap_NE2040,
                                            nuclear_Cap_NE2030, nuclear_Cap_NE2020], 1000), decimals=1)

    windN_Cap_NZ = windN_Cap_NZ['Capacity (MW)'].sum()
    windN_Cap_NE2050 = windN_Cap_NE2050['Capacity (MW)'].sum()
    windN_Cap_NE2040 = windN_Cap_NE2040['Capacity (MW)'].sum()
    windN_Cap_NE2030 = windN_Cap_NE2030['Capacity (MW)'].sum()
    windN_Cap_NE2020 = windN_Cap_NE2020['Capacity (MW)'].sum()

    windE_Cap_NZ = windE_Cap_NZ['Capacity (MW)'].sum()
    windE_Cap_NE2050 = windE_Cap_NE2050['Capacity (MW)'].sum()
    windE_Cap_NE2040 = windE_Cap_NE2040['Capacity (MW)'].sum()
    windE_Cap_NE2030 = windE_Cap_NE2030['Capacity (MW)'].sum()
    windE_Cap_NE2020 = windE_Cap_NE2020['Capacity (MW)'].sum()

    wind_Cap_all = np.around(np.divide([windN_Cap_NZ + windE_Cap_NZ, windN_Cap_NE2050 + windE_Cap_NE2050,
                                        windN_Cap_NE2040 + windE_Cap_NE2040,
                                        windN_Cap_NE2030 + windE_Cap_NE2030,
                                        windN_Cap_NE2020 + windE_Cap_NE2020], 1000), decimals=1)

    solarN_Cap_NZ = solarN_Cap_NZ['Capacity (MW)'].sum()
    solarN_Cap_NE2050 = solarN_Cap_NE2050['Capacity (MW)'].sum()
    solarN_Cap_NE2040 = solarN_Cap_NE2040['Capacity (MW)'].sum()
    solarN_Cap_NE2030 = solarN_Cap_NE2030['Capacity (MW)'].sum()
    solarN_Cap_NE2020 = solarN_Cap_NE2020['Capacity (MW)'].sum()

    solarE_Cap_NZ = solarE_Cap_NZ['Capacity (MW)'].sum()
    solarE_Cap_NE2050 = solarE_Cap_NE2050['Capacity (MW)'].sum()
    solarE_Cap_NE2040 = solarE_Cap_NE2040['Capacity (MW)'].sum()
    solarE_Cap_NE2030 = solarE_Cap_NE2030['Capacity (MW)'].sum()
    solarE_Cap_NE2020 = solarE_Cap_NE2020['Capacity (MW)'].sum()

    solar_Cap_all = np.around(np.divide([solarN_Cap_NZ+solarE_Cap_NZ, solarN_Cap_NE2050+solarE_Cap_NE2050,
                                         solarN_Cap_NE2040 + solarE_Cap_NE2040,
                                         solarN_Cap_NE2030 + solarE_Cap_NE2030,
                                         solarN_Cap_NE2020 + solarE_Cap_NE2020], 1000), decimals=1)

    pump_Cap_NZ = pump_Cap_NZ['Capacity (MW)'].sum()
    pump_Cap_NE2050 = pump_Cap_NE2050['Capacity (MW)'].sum()
    pump_Cap_NE2040 = pump_Cap_NE2040['Capacity (MW)'].sum()
    pump_Cap_NE2030 = pump_Cap_NE2030['Capacity (MW)'].sum()
    pump_Cap_NE2020 = pump_Cap_NE2020['Capacity (MW)'].sum()

    pump_Cap_all = np.around(np.divide([pump_Cap_NZ, pump_Cap_NE2050, pump_Cap_NE2040,
                                            pump_Cap_NE2030, pump_Cap_NE2020], 1000), decimals=1)

    Other_NZ = Other_NZ['Capacity (MW)'].sum()
    Other_NE2050 = Other_NE2050['Capacity (MW)'].sum()
    Other_NE2040 = Other_NE2040['Capacity (MW)'].sum()
    Other_NE2030 = Other_NE2030['Capacity (MW)'].sum()
    Other_NE2020 = Other_NE2020['Capacity (MW)'].sum()

    other_Cap_all = np.around(np.divide([Other_NZ, Other_NE2050, Other_NE2040,
                                        Other_NE2030, Other_NE2020], 1000), decimals=1)


    return (dac_Cap_all, coal_Cap_all, CC_Cap_all, CCCCS_Cap_all, CT_Cap_all, OG_Cap_all, bio_Cap_all,
            bat_Cap_all,h2_Cap_all, nuclear_Cap_all, wind_Cap_all, solar_Cap_all, pump_Cap_all, other_Cap_all)
