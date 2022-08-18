import pandas as pd
import numpy as np

def gen_hours_figures(m_dir, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2):

    # read in block weights:
    bw_NZ = pd.read_csv(m_dir + resultsDir_other_NZ + 'hoursCEByBlock2050.csv')
    bw_NE2020 = pd.read_csv(m_dir + resultsDir_other_NE2020 + 'hoursCEByBlock2050.csv')
    bw_NE2030 = pd.read_csv(m_dir + resultsDir_other_NE2030 + 'hoursCEByBlock2050.csv')
    bw_NE2040 = pd.read_csv(m_dir + resultsDir_other_NE2040 + 'hoursCEByBlock2050.csv')
    bw_NE2050 = pd.read_csv(m_dir + resultsDir_other_NE2050_2 + 'hoursCEByBlock2060.csv')

    bw_value_NZ = pd.read_csv(m_dir + resultsDir_other_NZ + 'blockWeightsCE2050.csv')
    bw_value_NE2020 = pd.read_csv(m_dir + resultsDir_other_NE2020 + 'blockWeightsCE2050.csv')
    bw_value_NE2030 = pd.read_csv(m_dir + resultsDir_other_NE2030 + 'blockWeightsCE2050.csv')
    bw_value_NE2040 = pd.read_csv(m_dir + resultsDir_other_NE2040 + 'blockWeightsCE2050.csv')
    bw_value_NE2050 = pd.read_csv(m_dir + resultsDir_other_NE2050_2 + 'blockWeightsCE2050.csv')

    bw_NZ['block_c'] = [int(x)+1 if len(x) == 1 else 0 for x in bw_NZ['block']]
    bw_NZ_u = bw_NZ.drop_duplicates('block_c',keep='last')
    bw_NZ_3 = bw_NZ_u['block_c'].max()
    bw_NZ_u = bw_NZ_u.loc[bw_NZ_u['block_c'] != bw_NZ_u['block_c'].max()]
    bw_NZ_2 = bw_NZ_u['block_c'].max()
    bw_NZ_u = bw_NZ_u.loc[bw_NZ_u['block_c'] != bw_NZ_u['block_c'].max()]
    bw_NZ_1 = bw_NZ_u['block_c'].max()
    bw_NZ_u = bw_NZ_u.loc[bw_NZ_u['block_c'] != bw_NZ_u['block_c'].max()]
    bw_NZ_0 = bw_NZ_u['block_c'].max()

    bw_NZ['block0'] = [1 if x == str(bw_NZ_0-1) else 0 for x in bw_NZ['block']]
    bw_NZ['block0'] = bw_NZ['block0'] * bw_value_NZ['blockWeight'][0]
    bw_NZ['block1'] = [1 if x == str(bw_NZ_1-1) else 0 for x in bw_NZ['block']]
    bw_NZ['block1'] = bw_NZ['block1'] * bw_value_NZ['blockWeight'][1]
    bw_NZ['block2'] = [1 if x == str(bw_NZ_2-1) else 0 for x in bw_NZ['block']]
    bw_NZ['block2'] = bw_NZ['block2'] * bw_value_NZ['blockWeight'][2]
    bw_NZ['block3'] = [1 if x == str(bw_NZ_3-1) else 0 for x in bw_NZ['block']]
    bw_NZ['block3'] = bw_NZ['block3'] * bw_value_NZ['blockWeight'][3]

    bw_NZ['block_c'] = bw_NZ['block0'] + bw_NZ['block1'] + bw_NZ['block2'] + bw_NZ['block3']
    bw_NZ['block_c'] = [1 if x == 0 else x for x in bw_NZ['block_c']]

    bw_NE2020['block_c'] = [int(x) + 1 if len(x) == 1 else 0 for x in bw_NE2020['block']]
    bw_NE2020_u = bw_NE2020.drop_duplicates('block_c', keep='last')
    bw_NE2020_3 = bw_NE2020_u['block_c'].max()
    bw_NE2020_u = bw_NE2020_u.loc[bw_NE2020_u['block_c'] != bw_NE2020_u['block_c'].max()]
    bw_NE2020_2 = bw_NE2020_u['block_c'].max()
    bw_NE2020_u = bw_NE2020_u.loc[bw_NE2020_u['block_c'] != bw_NE2020_u['block_c'].max()]
    bw_NE2020_1 = bw_NE2020_u['block_c'].max()
    bw_NE2020_u = bw_NE2020_u.loc[bw_NE2020_u['block_c'] != bw_NE2020_u['block_c'].max()]
    bw_NE2020_0 = bw_NE2020_u['block_c'].max()

    bw_NE2020['block0'] = [1 if x == str(bw_NE2020_0 - 1) else 0 for x in bw_NE2020['block']]
    bw_NE2020['block0'] = bw_NE2020['block0'] * bw_value_NE2020['blockWeight'][0]
    bw_NE2020['block1'] = [1 if x == str(bw_NE2020_1 - 1) else 0 for x in bw_NE2020['block']]
    bw_NE2020['block1'] = bw_NE2020['block1'] * bw_value_NE2020['blockWeight'][1]
    bw_NE2020['block2'] = [1 if x == str(bw_NE2020_2 - 1) else 0 for x in bw_NE2020['block']]
    bw_NE2020['block2'] = bw_NE2020['block2'] * bw_value_NE2020['blockWeight'][2]
    bw_NE2020['block3'] = [1 if x == str(bw_NE2020_3 - 1) else 0 for x in bw_NE2020['block']]
    bw_NE2020['block3'] = bw_NE2020['block3'] * bw_value_NE2020['blockWeight'][3]

    bw_NE2020['block_c'] = bw_NE2020['block0'] + bw_NE2020['block1'] + bw_NE2020['block2'] + bw_NE2020['block3']
    bw_NE2020['block_c'] = [1 if x == 0 else x for x in bw_NE2020['block_c']]

    bw_NE2030['block_c'] = [int(x) + 1 if len(x) == 1 else 0 for x in bw_NE2030['block']]
    bw_NE2030_u = bw_NE2030.drop_duplicates('block_c', keep='last')
    bw_NE2030_3 = bw_NE2030_u['block_c'].max()
    bw_NE2030_u = bw_NE2030_u.loc[bw_NE2030_u['block_c'] != bw_NE2030_u['block_c'].max()]
    bw_NE2030_2 = bw_NE2030_u['block_c'].max()
    bw_NE2030_u = bw_NE2030_u.loc[bw_NE2030_u['block_c'] != bw_NE2030_u['block_c'].max()]
    bw_NE2030_1 = bw_NE2030_u['block_c'].max()
    bw_NE2030_u = bw_NE2030_u.loc[bw_NE2030_u['block_c'] != bw_NE2030_u['block_c'].max()]
    bw_NE2030_0 = bw_NE2030_u['block_c'].max()

    bw_NE2030['block0'] = [1 if x == str(bw_NE2030_0 - 1) else 0 for x in bw_NE2030['block']]
    bw_NE2030['block0'] = bw_NE2030['block0'] * bw_value_NE2030['blockWeight'][0]
    bw_NE2030['block1'] = [1 if x == str(bw_NE2030_1 - 1) else 0 for x in bw_NE2030['block']]
    bw_NE2030['block1'] = bw_NE2030['block1'] * bw_value_NE2030['blockWeight'][1]
    bw_NE2030['block2'] = [1 if x == str(bw_NE2030_2 - 1) else 0 for x in bw_NE2030['block']]
    bw_NE2030['block2'] = bw_NE2030['block2'] * bw_value_NE2030['blockWeight'][2]
    bw_NE2030['block3'] = [1 if x == str(bw_NE2030_3 - 1) else 0 for x in bw_NE2030['block']]
    bw_NE2030['block3'] = bw_NE2030['block3'] * bw_value_NE2030['blockWeight'][3]

    bw_NE2030['block_c'] = bw_NE2030['block0'] + bw_NE2030['block1'] + bw_NE2030['block2'] + bw_NE2030['block3']
    bw_NE2030['block_c'] = [1 if x == 0 else x for x in bw_NE2030['block_c']]

    bw_NE2040['block_c'] = [int(x) + 1 if len(x) == 1 else 0 for x in bw_NE2040['block']]
    bw_NE2040_u = bw_NE2040.drop_duplicates('block_c', keep='last')
    bw_NE2040_3 = bw_NE2040_u['block_c'].max()
    bw_NE2040_u = bw_NE2040_u.loc[bw_NE2040_u['block_c'] != bw_NE2040_u['block_c'].max()]
    bw_NE2040_2 = bw_NE2040_u['block_c'].max()
    bw_NE2040_u = bw_NE2040_u.loc[bw_NE2040_u['block_c'] != bw_NE2040_u['block_c'].max()]
    bw_NE2040_1 = bw_NE2040_u['block_c'].max()
    bw_NE2040_u = bw_NE2040_u.loc[bw_NE2040_u['block_c'] != bw_NE2040_u['block_c'].max()]
    bw_NE2040_0 = bw_NE2040_u['block_c'].max()

    bw_NE2040['block0'] = [1 if x == str(bw_NE2040_0 - 1) else 0 for x in bw_NE2040['block']]
    bw_NE2040['block0'] = bw_NE2040['block0'] * bw_value_NE2040['blockWeight'][0]
    bw_NE2040['block1'] = [1 if x == str(bw_NE2040_1 - 1) else 0 for x in bw_NE2040['block']]
    bw_NE2040['block1'] = bw_NE2040['block1'] * bw_value_NE2040['blockWeight'][1]
    bw_NE2040['block2'] = [1 if x == str(bw_NE2040_2 - 1) else 0 for x in bw_NE2040['block']]
    bw_NE2040['block2'] = bw_NE2040['block2'] * bw_value_NE2040['blockWeight'][2]
    bw_NE2040['block3'] = [1 if x == str(bw_NE2040_3 - 1) else 0 for x in bw_NE2040['block']]
    bw_NE2040['block3'] = bw_NE2040['block3'] * bw_value_NE2040['blockWeight'][3]

    bw_NE2040['block_c'] = bw_NE2040['block0'] + bw_NE2040['block1'] + bw_NE2040['block2'] + bw_NE2040['block3']
    bw_NE2040['block_c'] = [1 if x == 0 else x for x in bw_NE2040['block_c']]

    bw_NE2050['block_c'] = [int(x) + 1 if len(x) == 1 else 0 for x in bw_NE2050['block']]
    bw_NE2050_u = bw_NE2050.drop_duplicates('block_c', keep='last')
    bw_NE2050_3 = bw_NE2050_u['block_c'].max()
    bw_NE2050_u = bw_NE2050_u.loc[bw_NE2050_u['block_c'] != bw_NE2050_u['block_c'].max()]
    bw_NE2050_2 = bw_NE2050_u['block_c'].max()
    bw_NE2050_u = bw_NE2050_u.loc[bw_NE2050_u['block_c'] != bw_NE2050_u['block_c'].max()]
    bw_NE2050_1 = bw_NE2050_u['block_c'].max()
    bw_NE2050_u = bw_NE2050_u.loc[bw_NE2050_u['block_c'] != bw_NE2050_u['block_c'].max()]
    bw_NE2050_0 = bw_NE2050_u['block_c'].max()

    bw_NE2050['block0'] = [1 if x == str(bw_NE2050_0 - 1) else 0 for x in bw_NE2050['block']]
    bw_NE2050['block0'] = bw_NE2050['block0'] * bw_value_NE2050['blockWeight'][0]
    bw_NE2050['block1'] = [1 if x == str(bw_NE2050_1 - 1) else 0 for x in bw_NE2050['block']]
    bw_NE2050['block1'] = bw_NE2050['block1'] * bw_value_NE2050['blockWeight'][1]
    bw_NE2050['block2'] = [1 if x == str(bw_NE2050_2 - 1) else 0 for x in bw_NE2050['block']]
    bw_NE2050['block2'] = bw_NE2050['block2'] * bw_value_NE2050['blockWeight'][2]
    bw_NE2050['block3'] = [1 if x == str(bw_NE2050_3 - 1) else 0 for x in bw_NE2050['block']]
    bw_NE2050['block3'] = bw_NE2050['block3'] * bw_value_NE2050['blockWeight'][3]

    bw_NE2050['block_c'] = bw_NE2050['block0'] + bw_NE2050['block1'] + bw_NE2050['block2'] + bw_NE2050['block3']
    bw_NE2050['block_c'] = [1 if x == 0 else x for x in bw_NE2050['block_c']]


    # read in gen solution:
    resultsGenE_NZ = pd.read_csv(m_dir + resultsDir_other_NZ + 'vGenCE2050.csv')
    resultsGenE_NE2020 = pd.read_csv(m_dir + resultsDir_other_NE2020 + 'vGenCE2050.csv')
    resultsGenE_NE2030 = pd.read_csv(m_dir + resultsDir_other_NE2030 + 'vGenCE2050.csv')
    resultsGenE_NE2040 = pd.read_csv(m_dir + resultsDir_other_NE2040 + 'vGenCE2050.csv')
    resultsGenE_NE2050 = pd.read_csv(m_dir + resultsDir_other_NE2050_2 + 'vGenCE2060.csv')

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
    planttypeE_NZ = pd.read_csv(m_dir + resultsDir_other_NZ + 'genFleetForCE2050.csv')
    planttypeE_NZ = planttypeE_NZ[['PlantType', 'region', 'Heat Rate (Btu/kWh)','CO2EmRate(lb/MMBtu)']]
    resultsGenE_NZ['PlantType'] = planttypeE_NZ['PlantType']
    resultsGenE_NZ['region'] = planttypeE_NZ['region']
    resultsGenE_NZ['Hr'] = planttypeE_NZ['Heat Rate (Btu/kWh)']
    resultsGenE_NZ['CO2r'] = planttypeE_NZ['CO2EmRate(lb/MMBtu)']

    planttypeE_NE2020 = pd.read_csv(m_dir + resultsDir_other_NE2020 + 'genFleetForCE2050.csv')
    planttypeE_NE2020 = planttypeE_NE2020[['PlantType', 'region', 'Heat Rate (Btu/kWh)','CO2EmRate(lb/MMBtu)']]
    resultsGenE_NE2020['PlantType'] = planttypeE_NE2020['PlantType']
    resultsGenE_NE2020['region'] = planttypeE_NE2020['region']
    resultsGenE_NE2020['Hr'] = planttypeE_NE2020['Heat Rate (Btu/kWh)']
    resultsGenE_NE2020['CO2r'] = planttypeE_NE2020['CO2EmRate(lb/MMBtu)']

    planttypeE_NE2030 = pd.read_csv(m_dir + resultsDir_other_NE2030 + 'genFleetForCE2050.csv')
    planttypeE_NE2030 = planttypeE_NE2030[['PlantType', 'region', 'Heat Rate (Btu/kWh)','CO2EmRate(lb/MMBtu)']]
    resultsGenE_NE2030['PlantType'] = planttypeE_NE2030['PlantType']
    resultsGenE_NE2030['region'] = planttypeE_NE2030['region']
    resultsGenE_NE2030['Hr'] = planttypeE_NE2030['Heat Rate (Btu/kWh)']
    resultsGenE_NE2030['CO2r'] = planttypeE_NE2030['CO2EmRate(lb/MMBtu)']

    planttypeE_NE2040 = pd.read_csv(m_dir + resultsDir_other_NE2040 + 'genFleetForCE2050.csv')
    planttypeE_NE2040 = planttypeE_NE2040[['PlantType', 'region', 'Heat Rate (Btu/kWh)','CO2EmRate(lb/MMBtu)']]
    resultsGenE_NE2040['PlantType'] = planttypeE_NE2040['PlantType']
    resultsGenE_NE2040['region'] = planttypeE_NE2040['region']
    resultsGenE_NE2040['Hr'] = planttypeE_NE2040['Heat Rate (Btu/kWh)']
    resultsGenE_NE2040['CO2r'] = planttypeE_NE2040['CO2EmRate(lb/MMBtu)']

    planttypeE_NE2050 = pd.read_csv(m_dir + resultsDir_other_NE2050_2 + 'genFleetForCE2060.csv')
    planttypeE_NE2050 = planttypeE_NE2050[['PlantType', 'region', 'Heat Rate (Btu/kWh)','CO2EmRate(lb/MMBtu)']]
    resultsGenE_NE2050['PlantType'] = planttypeE_NE2050['PlantType']
    resultsGenE_NE2050['region'] = planttypeE_NE2050['region']
    resultsGenE_NE2050['Hr'] = planttypeE_NE2050['Heat Rate (Btu/kWh)']
    resultsGenE_NE2050['CO2r'] = planttypeE_NE2050['CO2EmRate(lb/MMBtu)']

    Coal_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Coal Steam']
    CC_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Combined Cycle CCS']
    battery_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Hydrogen']
    dac_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'DAC']
    solarN_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('solar')]
    solarE_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Solar PV']
    windN_GenE_NZ = resultsGenE_NZ[resultsGenE_NZ['PlantType'].str.contains('wind')]
    windE_GenE_NZ = resultsGenE_NZ.loc[resultsGenE_NZ['PlantType'] == 'Onshore Wind']

    Coal_EiE_NZ = Coal_GenE_NZ['Hr']*Coal_GenE_NZ['CO2r']/(2000)
    Coal_GenE_NZ = Coal_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    Coal_GenE_agg_NZ = Coal_GenE_NZ.multiply(np.array(bw_NZ['block_c']), axis='columns')
    Coal_GenE_agg_NZ = Coal_GenE_agg_NZ.sum(axis=1)
    Coal_Em_NZ = sum(Coal_GenE_agg_NZ*Coal_EiE_NZ)
    Coal_GenE_NZ = Coal_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')

    CCCCS_EiE_NZ = CCCCS_GenE_NZ['Hr'] * CCCCS_GenE_NZ['CO2r'] / (2000)
    CCCCS_GenE_NZ = CCCCS_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CCCCS_GenE_agg_NZ = CCCCS_GenE_NZ.multiply(np.array(bw_NZ['block_c']), axis='columns')
    CCCCS_GenE_agg_NZ = CCCCS_GenE_agg_NZ.sum(axis=1)
    CCCCS_Em_NZ = sum(CCCCS_GenE_agg_NZ*CCCCS_EiE_NZ)
    CCCCS_GenE_NZ = CCCCS_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')

    CC_EiE_NZ = CC_GenE_NZ['Hr'] * CC_GenE_NZ['CO2r'] / (2000)
    CC_GenE_NZ = CC_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CC_GenE_agg_NZ = CC_GenE_NZ.multiply(np.array(bw_NZ['block_c']), axis='columns')
    CC_GenE_agg_NZ = CC_GenE_agg_NZ.sum(axis=1)
    CC_Em_NZ = sum(CC_GenE_agg_NZ * CC_EiE_NZ)
    CC_GenE_NZ = CC_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')

    battery_GenE_NZ = battery_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    battery_GenE_NZ = battery_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')
    hydrogen_GenE_NZ = hydrogen_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    hydrogen_GenE_NZ = hydrogen_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')

    dac_EiE_NZ = dac_GenE_NZ['Hr'] * dac_GenE_NZ['CO2r'] / (2000)
    dac_GenE_NZ = dac_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'region', 'Hr', 'CO2r'], axis=1)
    dac_GenE_agg_NZ = dac_GenE_NZ.multiply(np.array(bw_NZ['block_c']), axis='columns')
    dac_GenE_agg_NZ = dac_GenE_agg_NZ.sum(axis=1)
    dac_Em_NZ = sum(dac_GenE_agg_NZ * dac_EiE_NZ)
    dac_GenE_NZ = dac_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')

    solarN_GenE_NZ = solarN_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarN_GenE_NZ = solarN_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')
    solarE_GenE_NZ = solarE_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarE_GenE_NZ = solarE_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')
    windN_GenE_NZ = windN_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windN_GenE_NZ = windN_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')
    windE_GenE_NZ = windE_GenE_NZ.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windE_GenE_NZ = windE_GenE_NZ.sum().multiply(np.array(bw_NZ['block_c']), axis='index')
    solar_GenE_NZ = solarN_GenE_NZ + solarE_GenE_NZ
    wind_GenE_NZ = windN_GenE_NZ + windE_GenE_NZ

    Coal_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Coal Steam']
    CC_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Combined Cycle CCS']
    battery_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Hydrogen']
    dac_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'DAC']
    solarN_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('solar')]
    solarE_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Solar PV']
    windN_GenE_NE2020 = resultsGenE_NE2020[resultsGenE_NE2020['PlantType'].str.contains('wind')]
    windE_GenE_NE2020 = resultsGenE_NE2020.loc[resultsGenE_NE2020['PlantType'] == 'Onshore Wind']

    Coal_EiE_NE2020 = Coal_GenE_NE2020['Hr'] * Coal_GenE_NE2020['CO2r'] / (2000)
    Coal_GenE_NE2020 = Coal_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    Coal_GenE_agg_NE2020 = Coal_GenE_NE2020.multiply(np.array(bw_NE2020['block_c']), axis='columns')
    Coal_GenE_agg_NE2020 = Coal_GenE_agg_NE2020.sum(axis=1)
    Coal_Em_NE2020 = sum(Coal_GenE_agg_NE2020 * Coal_EiE_NE2020)
    Coal_GenE_NE2020 = Coal_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')

    CCCCS_EiE_NE2020 = CCCCS_GenE_NE2020['Hr'] * CCCCS_GenE_NE2020['CO2r'] / (2000)
    CCCCS_GenE_NE2020 = CCCCS_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CCCCS_GenE_agg_NE2020 = CCCCS_GenE_NE2020.multiply(np.array(bw_NE2020['block_c']), axis='columns')
    CCCCS_GenE_agg_NE2020 = CCCCS_GenE_agg_NE2020.sum(axis=1)
    CCCCS_Em_NE2020 = sum(CCCCS_GenE_agg_NE2020 * CCCCS_EiE_NE2020)
    CCCCS_GenE_NE2020 = CCCCS_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')

    CC_EiE_NE2020 = CC_GenE_NE2020['Hr'] * CC_GenE_NE2020['CO2r'] / (2000)
    CC_GenE_NE2020 = CC_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CC_GenE_agg_NE2020 = CC_GenE_NE2020.multiply(np.array(bw_NE2020['block_c']), axis='columns')
    CC_GenE_agg_NE2020 = CC_GenE_agg_NE2020.sum(axis=1)
    CC_Em_NE2020 = sum(CC_GenE_agg_NE2020 * CC_EiE_NE2020)
    CC_GenE_NE2020 = CC_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')

    battery_GenE_NE2020 = battery_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    battery_GenE_NE2020 = battery_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')
    hydrogen_GenE_NE2020 = hydrogen_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    hydrogen_GenE_NE2020 = hydrogen_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')

    dac_EiE_NE2020 = dac_GenE_NE2020['Hr'] * dac_GenE_NE2020['CO2r'] / (2000)
    dac_GenE_NE2020 = dac_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'region', 'Hr', 'CO2r'], axis=1)
    dac_GenE_agg_NE2020 = dac_GenE_NE2020.multiply(np.array(bw_NE2020['block_c']), axis='columns')
    dac_GenE_agg_NE2020 = dac_GenE_agg_NE2020.sum(axis=1)
    dac_Em_NE2020 = sum(dac_GenE_agg_NE2020 * dac_EiE_NE2020)
    dac_GenE_NE2020 = dac_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')

    solarN_GenE_NE2020 = solarN_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarN_GenE_NE2020 = solarN_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')
    solarE_GenE_NE2020 = solarE_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarE_GenE_NE2020 = solarE_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')
    windN_GenE_NE2020 = windN_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windN_GenE_NE2020 = windN_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')
    windE_GenE_NE2020 = windE_GenE_NE2020.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windE_GenE_NE2020 = windE_GenE_NE2020.sum().multiply(np.array(bw_NE2020['block_c']), axis='index')
    solar_GenE_NE2020 = solarN_GenE_NE2020 + solarE_GenE_NE2020
    wind_GenE_NE2020 = windN_GenE_NE2020 + windE_GenE_NE2020

    Coal_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Coal Steam']
    CC_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Combined Cycle CCS']
    battery_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Hydrogen']
    dac_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'DAC']
    solarN_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('solar')]
    solarE_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Solar PV']
    windN_GenE_NE2030 = resultsGenE_NE2030[resultsGenE_NE2030['PlantType'].str.contains('wind')]
    windE_GenE_NE2030 = resultsGenE_NE2030.loc[resultsGenE_NE2030['PlantType'] == 'Onshore Wind']

    Coal_EiE_NE2030 = Coal_GenE_NE2030['Hr'] * Coal_GenE_NE2030['CO2r'] / (2000)
    Coal_GenE_NE2030 = Coal_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    Coal_GenE_agg_NE2030 = Coal_GenE_NE2030.multiply(np.array(bw_NE2030['block_c']), axis='columns')
    Coal_GenE_agg_NE2030 = Coal_GenE_agg_NE2030.sum(axis=1)
    Coal_Em_NE2030 = sum(Coal_GenE_agg_NE2030 * Coal_EiE_NE2030)
    Coal_GenE_NE2030 = Coal_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')

    CCCCS_EiE_NE2030 = CCCCS_GenE_NE2030['Hr'] * CCCCS_GenE_NE2030['CO2r'] / (2000)
    CCCCS_GenE_NE2030 = CCCCS_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CCCCS_GenE_agg_NE2030 = CCCCS_GenE_NE2030.multiply(np.array(bw_NE2030['block_c']), axis='columns')
    CCCCS_GenE_agg_NE2030 = CCCCS_GenE_agg_NE2030.sum(axis=1)
    CCCCS_Em_NE2030 = sum(CCCCS_GenE_agg_NE2030 * CCCCS_EiE_NE2030)
    CCCCS_GenE_NE2030 = CCCCS_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')

    CC_EiE_NE2030 = CC_GenE_NE2030['Hr'] * CC_GenE_NE2030['CO2r'] / (2000)
    CC_GenE_NE2030 = CC_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CC_GenE_agg_NE2030 = CC_GenE_NE2030.multiply(np.array(bw_NE2030['block_c']), axis='columns')
    CC_GenE_agg_NE2030 = CC_GenE_agg_NE2030.sum(axis=1)
    CC_Em_NE2030 = sum(CC_GenE_agg_NE2030 * CC_EiE_NE2030)
    CC_GenE_NE2030 = CC_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')

    battery_GenE_NE2030 = battery_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    battery_GenE_NE2030 = battery_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')
    hydrogen_GenE_NE2030 = hydrogen_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    hydrogen_GenE_NE2030 = hydrogen_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')

    dac_EiE_NE2030 = dac_GenE_NE2030['Hr'] * dac_GenE_NE2030['CO2r'] / (2000)
    dac_GenE_NE2030 = dac_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'region', 'Hr', 'CO2r'], axis=1)
    dac_GenE_agg_NE2030 = dac_GenE_NE2030.multiply(np.array(bw_NE2030['block_c']), axis='columns')
    dac_GenE_agg_NE2030 = dac_GenE_agg_NE2030.sum(axis=1)
    dac_Em_NE2030 = sum(dac_GenE_agg_NE2030 * dac_EiE_NE2030)
    dac_GenE_NE2030 = dac_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')

    solarN_GenE_NE2030 = solarN_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarN_GenE_NE2030 = solarN_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')
    solarE_GenE_NE2030 = solarE_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarE_GenE_NE2030 = solarE_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')
    windN_GenE_NE2030 = windN_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windN_GenE_NE2030 = windN_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')
    windE_GenE_NE2030 = windE_GenE_NE2030.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windE_GenE_NE2030 = windE_GenE_NE2030.sum().multiply(np.array(bw_NE2030['block_c']), axis='index')
    solar_GenE_NE2030 = solarN_GenE_NE2030 + solarE_GenE_NE2030
    wind_GenE_NE2030 = windN_GenE_NE2030 + windE_GenE_NE2030

    Coal_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Coal Steam']
    CC_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Combined Cycle CCS']
    battery_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Hydrogen']
    dac_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'DAC']
    solarN_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('solar')]
    solarE_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Solar PV']
    windN_GenE_NE2040 = resultsGenE_NE2040[resultsGenE_NE2040['PlantType'].str.contains('wind')]
    windE_GenE_NE2040 = resultsGenE_NE2040.loc[resultsGenE_NE2040['PlantType'] == 'Onshore Wind']

    Coal_EiE_NE2040 = Coal_GenE_NE2040['Hr'] * Coal_GenE_NE2040['CO2r'] / (2000)
    Coal_GenE_NE2040 = Coal_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    Coal_GenE_agg_NE2040 = Coal_GenE_NE2040.multiply(np.array(bw_NE2040['block_c']), axis='columns')
    Coal_GenE_agg_NE2040 = Coal_GenE_agg_NE2040.sum(axis=1)
    Coal_Em_NE2040 = sum(Coal_GenE_agg_NE2040 * Coal_EiE_NE2040)
    Coal_GenE_NE2040 = Coal_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')

    CCCCS_EiE_NE2040 = CCCCS_GenE_NE2040['Hr'] * CCCCS_GenE_NE2040['CO2r'] / (2000)
    CCCCS_GenE_NE2040 = CCCCS_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CCCCS_GenE_agg_NE2040 = CCCCS_GenE_NE2040.multiply(np.array(bw_NE2040['block_c']), axis='columns')
    CCCCS_GenE_agg_NE2040 = CCCCS_GenE_agg_NE2040.sum(axis=1)
    CCCCS_Em_NE2040 = sum(CCCCS_GenE_agg_NE2040 * CCCCS_EiE_NE2040)
    CCCCS_GenE_NE2040 = CCCCS_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')

    CC_EiE_NE2040 = CC_GenE_NE2040['Hr'] * CC_GenE_NE2040['CO2r'] / (2000)
    CC_GenE_NE2040 = CC_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CC_GenE_agg_NE2040 = CC_GenE_NE2040.multiply(np.array(bw_NE2040['block_c']), axis='columns')
    CC_GenE_agg_NE2040 = CC_GenE_agg_NE2040.sum(axis=1)
    CC_Em_NE2040 = sum(CC_GenE_agg_NE2040 * CC_EiE_NE2040)
    CC_GenE_NE2040 = CC_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')

    battery_GenE_NE2040 = battery_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    battery_GenE_NE2040 = battery_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')
    hydrogen_GenE_NE2040 = hydrogen_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    hydrogen_GenE_NE2040 = hydrogen_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')

    dac_EiE_NE2040 = dac_GenE_NE2040['Hr'] * dac_GenE_NE2040['CO2r'] / (2000)
    dac_GenE_NE2040 = dac_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'region', 'Hr', 'CO2r'], axis=1)
    dac_GenE_agg_NE2040 = dac_GenE_NE2040.multiply(np.array(bw_NE2040['block_c']), axis='columns')
    dac_GenE_agg_NE2040 = dac_GenE_agg_NE2040.sum(axis=1)
    dac_Em_NE2040 = sum(dac_GenE_agg_NE2040 * dac_EiE_NE2040)
    dac_GenE_NE2040 = dac_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')

    solarN_GenE_NE2040 = solarN_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarN_GenE_NE2040 = solarN_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')
    solarE_GenE_NE2040 = solarE_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarE_GenE_NE2040 = solarE_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')
    windN_GenE_NE2040 = windN_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windN_GenE_NE2040 = windN_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')
    windE_GenE_NE2040 = windE_GenE_NE2040.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windE_GenE_NE2040 = windE_GenE_NE2040.sum().multiply(np.array(bw_NE2040['block_c']), axis='index')
    solar_GenE_NE2040 = solarN_GenE_NE2040 + solarE_GenE_NE2040
    wind_GenE_NE2040 = windN_GenE_NE2040 + windE_GenE_NE2040

    Coal_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Coal Steam']
    CC_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Combined Cycle']
    CCCCS_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Combined Cycle CCS']
    battery_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('Batter')]
    hydrogen_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Hydrogen']
    nuclear_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Nuclear']
    dac_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'DAC']
    solarN_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('solar')]
    solarE_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Solar PV']
    windN_GenE_NE2050 = resultsGenE_NE2050[resultsGenE_NE2050['PlantType'].str.contains('wind')]
    windE_GenE_NE2050 = resultsGenE_NE2050.loc[resultsGenE_NE2050['PlantType'] == 'Onshore Wind']

    Coal_EiE_NE2050 = Coal_GenE_NE2050['Hr'] * Coal_GenE_NE2050['CO2r'] / (2000)
    Coal_GenE_NE2050 = Coal_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    Coal_GenE_agg_NE2050 = Coal_GenE_NE2050.multiply(np.array(bw_NE2050['block_c']), axis='columns')
    Coal_GenE_agg_NE2050 = Coal_GenE_agg_NE2050.sum(axis=1)
    Coal_Em_NE2050 = sum(Coal_GenE_agg_NE2050 * Coal_EiE_NE2050)
    Coal_GenE_NE2050 = Coal_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')

    CCCCS_EiE_NE2050 = CCCCS_GenE_NE2050['Hr'] * CCCCS_GenE_NE2050['CO2r'] / (2000)
    CCCCS_GenE_NE2050 = CCCCS_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CCCCS_GenE_agg_NE2050 = CCCCS_GenE_NE2050.multiply(np.array(bw_NE2050['block_c']), axis='columns')
    CCCCS_GenE_agg_NE2050 = CCCCS_GenE_agg_NE2050.sum(axis=1)
    CCCCS_Em_NE2050 = sum(CCCCS_GenE_agg_NE2050 * CCCCS_EiE_NE2050)
    CCCCS_GenE_NE2050 = CCCCS_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')

    CC_EiE_NE2050 = CC_GenE_NE2050['Hr'] * CC_GenE_NE2050['CO2r'] / (2000)
    CC_GenE_NE2050 = CC_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    CC_GenE_agg_NE2050 = CC_GenE_NE2050.multiply(np.array(bw_NE2050['block_c']), axis='columns')
    CC_GenE_agg_NE2050 = CC_GenE_agg_NE2050.sum(axis=1)
    CC_Em_NE2050 = sum(CC_GenE_agg_NE2050 * CC_EiE_NE2050)
    CC_GenE_NE2050 = CC_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')

    battery_GenE_NE2050 = battery_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    battery_GenE_NE2050 = battery_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')
    hydrogen_GenE_NE2050 = hydrogen_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    hydrogen_GenE_NE2050 = hydrogen_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')

    dac_EiE_NE2050 = dac_GenE_NE2050['Hr'] * dac_GenE_NE2050['CO2r'] / (2000)
    dac_GenE_NE2050 = dac_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'region', 'Hr', 'CO2r'], axis=1)
    dac_GenE_agg_NE2050 = dac_GenE_NE2050.multiply(np.array(bw_NE2050['block_c']), axis='columns')
    dac_GenE_agg_NE2050 = dac_GenE_agg_NE2050.sum(axis=1)
    dac_Em_NE2050 = sum(dac_GenE_agg_NE2050 * dac_EiE_NE2050)
    dac_GenE_NE2050 = dac_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')

    solarN_GenE_NE2050 = solarN_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarN_GenE_NE2050 = solarN_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')
    solarE_GenE_NE2050 = solarE_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    solarE_GenE_NE2050 = solarE_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')
    windN_GenE_NE2050 = windN_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windN_GenE_NE2050 = windN_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')
    windE_GenE_NE2050 = windE_GenE_NE2050.drop(['Unit', 'PlantType', 'region', 'Hr', 'CO2r'], axis=1)
    windE_GenE_NE2050 = windE_GenE_NE2050.sum().multiply(np.array(bw_NE2050['block_c']), axis='index')
    solar_GenE_NE2050 = solarN_GenE_NE2050 + solarE_GenE_NE2050
    wind_GenE_NE2050 = windN_GenE_NE2050 + windE_GenE_NE2050

    # New:
    resultsGenN_NZ = pd.read_csv(m_dir + resultsDir_other_NZ + 'vGentechCE2050.csv')
    resultsGenN_NE2020 = pd.read_csv(m_dir + resultsDir_other_NE2020 + 'vGentechCE2050.csv')
    resultsGenN_NE2030 = pd.read_csv(m_dir + resultsDir_other_NE2030 + 'vGentechCE2050.csv')
    resultsGenN_NE2040 = pd.read_csv(m_dir + resultsDir_other_NE2040 + 'vGentechCE2050.csv')
    resultsGenN_NE2050 = pd.read_csv(m_dir + resultsDir_other_NE2050_2 + 'vGentechCE2060.csv')

    resultsGenN_NZ.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NZ = resultsGenN_NZ.T
    resultsGenN_NZ.columns = resultsGenN_NZ.iloc[0]
    resultsGenN_NZ = resultsGenN_NZ.drop(resultsGenN_NZ.index[0])
    resultsGenN_NZ = resultsGenN_NZ.reset_index()
    resultsGenN_NZ.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    resultsGenN_NE2020.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2020 = resultsGenN_NE2020.T
    resultsGenN_NE2020.columns = resultsGenN_NE2020.iloc[0]
    resultsGenN_NE2020 = resultsGenN_NE2020.drop(resultsGenN_NE2020.index[0])
    resultsGenN_NE2020 = resultsGenN_NE2020.reset_index()
    resultsGenN_NE2020.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    resultsGenN_NE2030.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2030 = resultsGenN_NE2030.T
    resultsGenN_NE2030.columns = resultsGenN_NE2030.iloc[0]
    resultsGenN_NE2030 = resultsGenN_NE2030.drop(resultsGenN_NE2030.index[0])
    resultsGenN_NE2030 = resultsGenN_NE2030.reset_index()
    resultsGenN_NE2030.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    resultsGenN_NE2040.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2040 = resultsGenN_NE2040.T
    resultsGenN_NE2040.columns = resultsGenN_NE2040.iloc[0]
    resultsGenN_NE2040 = resultsGenN_NE2040.drop(resultsGenN_NE2040.index[0])
    resultsGenN_NE2040 = resultsGenN_NE2040.reset_index()
    resultsGenN_NE2040.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    resultsGenN_NE2050.rename(columns={'Unnamed: 0': 'hour'}, inplace=True)
    resultsGenN_NE2050 = resultsGenN_NE2050.T
    resultsGenN_NE2050.columns = resultsGenN_NE2050.iloc[0]
    resultsGenN_NE2050 = resultsGenN_NE2050.drop(resultsGenN_NE2050.index[0])
    resultsGenN_NE2050 = resultsGenN_NE2050.reset_index()
    resultsGenN_NE2050.rename(columns={'index': 'GAMS Symbol'}, inplace=True)

    CoalCCS_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CCCCS_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    CC_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Combined Cycle')]
    battery_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('Hydrogen')]
    dac_GenN_NZ = resultsGenN_NZ.loc[resultsGenN_NZ['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NZ = resultsGenN_NZ[resultsGenN_NZ['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NZ = resultsGenN_NZ[resultsGenN_NZ['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NZ = CoalCCS_GenN_NZ.drop('GAMS Symbol', axis=1)
    CoalCCS_GenN_NZ = CoalCCS_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))
    CCCCS_GenN_NZ = CCCCS_GenN_NZ.drop('GAMS Symbol', axis=1)
    CCCCS_GenN_NZ = CCCCS_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))
    CC_GenN_NZ = CC_GenN_NZ.drop('GAMS Symbol', axis=1)
    CC_GenN_NZ = CC_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c'])) - CCCCS_GenN_NZ
    battery_GenN_NZ = battery_GenN_NZ.drop('GAMS Symbol', axis=1)
    battery_GenN_NZ = battery_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))
    hydrogen_GenN_NZ = hydrogen_GenN_NZ.drop('GAMS Symbol', axis=1)
    hydrogen_GenN_NZ = hydrogen_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))
    dac_GenN_NZ = dac_GenN_NZ.drop('GAMS Symbol', axis=1)
    dac_GenN_NZ = dac_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))
    solar_GenN_NZ = solar_GenN_NZ.drop('GAMS Symbol', axis=1)
    solar_GenN_NZ = solar_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))
    wind_GenN_NZ = wind_GenN_NZ.drop('GAMS Symbol', axis=1)
    wind_GenN_NZ = wind_GenN_NZ.sum().multiply(np.array(bw_NZ['block_c']))

    CoalCCS_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CCCCS_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    CC_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Combined Cycle')]
    battery_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('Hydrogen')]
    dac_GenN_NE2020 = resultsGenN_NE2020.loc[resultsGenN_NE2020['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2020 = resultsGenN_NE2020[resultsGenN_NE2020['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2020 = resultsGenN_NE2020[resultsGenN_NE2020['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2020 = CoalCCS_GenN_NE2020.drop('GAMS Symbol', axis=1)
    CoalCCS_GenN_NE2020 = CoalCCS_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))
    CCCCS_GenN_NE2020 = CCCCS_GenN_NE2020.drop('GAMS Symbol', axis=1)
    CCCCS_GenN_NE2020 = CCCCS_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))
    CC_GenN_NE2020 = CC_GenN_NE2020.drop('GAMS Symbol', axis=1)
    CC_GenN_NE2020 = CC_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c'])) - CCCCS_GenN_NE2020
    battery_GenN_NE2020 = battery_GenN_NE2020.drop('GAMS Symbol', axis=1)
    battery_GenN_NE2020 = battery_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))
    hydrogen_GenN_NE2020 = hydrogen_GenN_NE2020.drop('GAMS Symbol', axis=1)
    hydrogen_GenN_NE2020 = hydrogen_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))
    dac_GenN_NE2020 = dac_GenN_NE2020.drop('GAMS Symbol', axis=1)
    dac_GenN_NE2020 = dac_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))
    solar_GenN_NE2020 = solar_GenN_NE2020.drop('GAMS Symbol', axis=1)
    solar_GenN_NE2020 = solar_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))
    wind_GenN_NE2020 = wind_GenN_NE2020.drop('GAMS Symbol', axis=1)
    wind_GenN_NE2020 = wind_GenN_NE2020.sum().multiply(np.array(bw_NE2020['block_c']))

    CoalCCS_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CCCCS_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    CC_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Combined Cycle')]
    battery_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('Hydrogen')]
    dac_GenN_NE2030 = resultsGenN_NE2030.loc[resultsGenN_NE2030['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2030 = resultsGenN_NE2030[resultsGenN_NE2030['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2030 = resultsGenN_NE2030[resultsGenN_NE2030['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2030 = CoalCCS_GenN_NE2030.drop('GAMS Symbol', axis=1)
    CoalCCS_GenN_NE2030 = CoalCCS_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))
    CCCCS_GenN_NE2030 = CCCCS_GenN_NE2030.drop('GAMS Symbol', axis=1)
    CCCCS_GenN_NE2030 = CCCCS_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))
    CC_GenN_NE2030 = CC_GenN_NE2030.drop('GAMS Symbol', axis=1)
    CC_GenN_NE2030 = CC_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c'])) - CCCCS_GenN_NE2030
    battery_GenN_NE2030 = battery_GenN_NE2030.drop('GAMS Symbol', axis=1)
    battery_GenN_NE2030 = battery_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))
    hydrogen_GenN_NE2030 = hydrogen_GenN_NE2030.drop('GAMS Symbol', axis=1)
    hydrogen_GenN_NE2030 = hydrogen_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))
    dac_GenN_NE2030 = dac_GenN_NE2030.drop('GAMS Symbol', axis=1)
    dac_GenN_NE2030 = dac_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))
    solar_GenN_NE2030 = solar_GenN_NE2030.drop('GAMS Symbol', axis=1)
    solar_GenN_NE2030 = solar_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))
    wind_GenN_NE2030 = wind_GenN_NE2030.drop('GAMS Symbol', axis=1)
    wind_GenN_NE2030 = wind_GenN_NE2030.sum().multiply(np.array(bw_NE2030['block_c']))

    CoalCCS_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CCCCS_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    CC_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Combined Cycle')]
    battery_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('Hydrogen')]
    dac_GenN_NE2040 = resultsGenN_NE2040.loc[resultsGenN_NE2040['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2040 = resultsGenN_NE2040[resultsGenN_NE2040['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2040 = resultsGenN_NE2040[resultsGenN_NE2040['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2040 = CoalCCS_GenN_NE2040.drop('GAMS Symbol', axis=1)
    CoalCCS_GenN_NE2040 = CoalCCS_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))
    CCCCS_GenN_NE2040 = CCCCS_GenN_NE2040.drop('GAMS Symbol', axis=1)
    CCCCS_GenN_NE2040 = CCCCS_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))
    CC_GenN_NE2040 = CC_GenN_NE2040.drop('GAMS Symbol', axis=1)
    CC_GenN_NE2040 = CC_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c'])) - CCCCS_GenN_NE2040
    battery_GenN_NE2040 = battery_GenN_NE2040.drop('GAMS Symbol', axis=1)
    battery_GenN_NE2040 = battery_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))
    hydrogen_GenN_NE2040 = hydrogen_GenN_NE2040.drop('GAMS Symbol', axis=1)
    hydrogen_GenN_NE2040 = hydrogen_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))
    dac_GenN_NE2040 = dac_GenN_NE2040.drop('GAMS Symbol', axis=1)
    dac_GenN_NE2040 = dac_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))
    solar_GenN_NE2040 = solar_GenN_NE2040.drop('GAMS Symbol', axis=1)
    solar_GenN_NE2040 = solar_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))
    wind_GenN_NE2040 = wind_GenN_NE2040.drop('GAMS Symbol', axis=1)
    wind_GenN_NE2040 = wind_GenN_NE2040.sum().multiply(np.array(bw_NE2040['block_c']))

    CoalCCS_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Coal Steam CCS')]
    CCCCS_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Combined Cycle CCS')]
    CC_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Combined Cycle')]
    battery_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Battery Storage')]
    hydrogen_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('Hydrogen')]
    dac_GenN_NE2050 = resultsGenN_NE2050.loc[resultsGenN_NE2050['GAMS Symbol'].str.contains('DAC')]
    solar_GenN_NE2050 = resultsGenN_NE2050[resultsGenN_NE2050['GAMS Symbol'].str.contains('solar')]
    wind_GenN_NE2050 = resultsGenN_NE2050[resultsGenN_NE2050['GAMS Symbol'].str.contains('wind')]

    CoalCCS_GenN_NE2050 = CoalCCS_GenN_NE2050.drop('GAMS Symbol', axis=1)
    CoalCCS_GenN_NE2050 = CoalCCS_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))
    CCCCS_GenN_NE2050 = CCCCS_GenN_NE2050.drop('GAMS Symbol', axis=1)
    CCCCS_GenN_NE2050 = CCCCS_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))
    CC_GenN_NE2050 = CC_GenN_NE2050.drop('GAMS Symbol', axis=1)
    CC_GenN_NE2050 = CC_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c'])) - CCCCS_GenN_NE2050
    battery_GenN_NE2050 = battery_GenN_NE2050.drop('GAMS Symbol', axis=1)
    battery_GenN_NE2050 = battery_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))
    hydrogen_GenN_NE2050 = hydrogen_GenN_NE2050.drop('GAMS Symbol', axis=1)
    hydrogen_GenN_NE2050 = hydrogen_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))
    dac_GenN_NE2050 = dac_GenN_NE2050.drop('GAMS Symbol', axis=1)
    dac_GenN_NE2050 = dac_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))
    solar_GenN_NE2050 = solar_GenN_NE2050.drop('GAMS Symbol', axis=1)
    solar_GenN_NE2050 = solar_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))
    wind_GenN_NE2050 = wind_GenN_NE2050.drop('GAMS Symbol', axis=1)
    wind_GenN_NE2050 = wind_GenN_NE2050.sum().multiply(np.array(bw_NE2050['block_c']))

    #
    dac_Gen_all = np.around(np.divide([dac_GenE_NZ + dac_GenN_NZ, dac_GenE_NE2050 + dac_GenN_NE2050,
                                       dac_GenE_NE2040 + dac_GenN_NE2040, dac_GenE_NE2030 + dac_GenN_NE2030,
                                       dac_GenE_NE2020 + dac_GenN_NE2020], 1000), decimals=1)
    Coal_Gen_all = np.around(np.divide([Coal_GenE_NZ + CoalCCS_GenN_NZ, Coal_GenE_NE2050 + CoalCCS_GenN_NE2050,
                                        Coal_GenE_NE2040 + CoalCCS_GenN_NE2040, Coal_GenE_NE2030 + CoalCCS_GenN_NE2030,
                                        Coal_GenE_NE2020 + CoalCCS_GenN_NE2020], 1000), decimals=1)
    CC_Gen_all = np.around(np.divide([CC_GenE_NZ + CC_GenN_NZ, CC_GenE_NE2050 + CC_GenN_NE2050, CC_GenE_NE2040 + CC_GenN_NE2040,
                                      CC_GenE_NE2030 + CC_GenN_NE2030, CC_GenE_NE2020 + CC_GenN_NE2020], 1000), decimals=1)
    CCCCS_Gen_all = np.around(np.divide([CCCCS_GenE_NZ + CCCCS_GenN_NZ, CCCCS_GenE_NE2050 + CCCCS_GenN_NE2050,
                                         CCCCS_GenE_NE2040 + CCCCS_GenN_NE2040, CCCCS_GenE_NE2030 + CCCCS_GenN_NE2030,
                                         CCCCS_GenE_NE2020 + CCCCS_GenN_NE2020], 1000), decimals=1)
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


    # New resource emission rate:
    ei_dac = 549.332  # (tons captured per GWh of DAC)
    ei_coal = 97.03675
    ei_cc = 378.5985
    ei_ccccs = 36.7115

    dacN_CO2_NZ = sum(dac_GenN_NZ) * ei_dac
    coalN_CO2_NZ = sum(CoalCCS_GenN_NZ) * ei_coal
    ccN_CO2_NZ = sum(CC_GenN_NZ) * ei_cc
    ccccsN_CO2_NZ = sum(CCCCS_GenN_NZ) * ei_ccccs

    dac_CO2_NZ = dacN_CO2_NZ + dac_Em_NZ
    coal_CO2_NZ = coalN_CO2_NZ + Coal_Em_NZ
    cc_CO2_NZ = CC_Em_NZ + ccN_CO2_NZ
    ccccs_CO2_NZ = CCCCS_Em_NZ + ccccsN_CO2_NZ

    dacN_CO2_NE2020 = sum(dac_GenN_NE2020) * ei_dac
    coalN_CO2_NE2020 = sum(CoalCCS_GenN_NE2020) * ei_coal
    ccN_CO2_NE2020 = sum(CC_GenN_NE2020) * ei_cc
    ccccsN_CO2_NE2020 = sum(CCCCS_GenN_NE2020) * ei_ccccs

    dac_CO2_NE2020 = dacN_CO2_NE2020 + dac_Em_NE2020
    coal_CO2_NE2020 = coalN_CO2_NE2020 + Coal_Em_NE2020
    cc_CO2_NE2020 = CC_Em_NE2020 + ccN_CO2_NE2020
    ccccs_CO2_NE2020 = CCCCS_Em_NE2020 + ccccsN_CO2_NE2020

    dacN_CO2_NE2030 = sum(dac_GenN_NE2030) * ei_dac
    coalN_CO2_NE2030 = sum(CoalCCS_GenN_NE2030) * ei_coal
    ccN_CO2_NE2030 = sum(CC_GenN_NE2030) * ei_cc
    ccccsN_CO2_NE2030 = sum(CCCCS_GenN_NE2030) * ei_ccccs

    dac_CO2_NE2030 = dacN_CO2_NE2030 + dac_Em_NE2030
    coal_CO2_NE2030 = coalN_CO2_NE2030 + Coal_Em_NE2030
    cc_CO2_NE2030 = CC_Em_NE2030 + ccN_CO2_NE2030
    ccccs_CO2_NE2030 = CCCCS_Em_NE2030 + ccccsN_CO2_NE2030

    dacN_CO2_NE2040 = sum(dac_GenN_NE2040) * ei_dac
    coalN_CO2_NE2040 = sum(CoalCCS_GenN_NE2040) * ei_coal
    ccN_CO2_NE2040 = sum(CC_GenN_NE2040) * ei_cc
    ccccsN_CO2_NE2040 = sum(CCCCS_GenN_NE2040) * ei_ccccs

    dac_CO2_NE2040 = dacN_CO2_NE2040 + dac_Em_NE2040
    coal_CO2_NE2040 = coalN_CO2_NE2040 + Coal_Em_NE2040
    cc_CO2_NE2040 = CC_Em_NE2040 + ccN_CO2_NE2040
    ccccs_CO2_NE2040 = CCCCS_Em_NE2040 + ccccsN_CO2_NE2040

    dacN_CO2_NE2050 = sum(dac_GenN_NE2050) * ei_dac
    coalN_CO2_NE2050 = sum(CoalCCS_GenN_NE2050) * ei_coal
    ccN_CO2_NE2050 = sum(CC_GenN_NE2050) * ei_cc
    ccccsN_CO2_NE2050 = sum(CCCCS_GenN_NE2050) * ei_ccccs

    dac_CO2_NE2050 = dacN_CO2_NE2050 + dac_Em_NE2050
    coal_CO2_NE2050 = coalN_CO2_NE2050 + Coal_Em_NE2050
    cc_CO2_NE2050 = CC_Em_NE2050 + ccN_CO2_NE2050
    ccccs_CO2_NE2050 = CCCCS_Em_NE2050 + ccccsN_CO2_NE2050

    dac_CO2_all = np.around(np.divide([dac_CO2_NZ, dac_CO2_NE2050,dac_CO2_NE2040, dac_CO2_NE2030, dac_CO2_NE2020], 1000000), decimals=1)
    coal_CO2_all = np.around(np.divide([coal_CO2_NZ, coal_CO2_NE2050, coal_CO2_NE2040, coal_CO2_NE2030, coal_CO2_NE2020], 1000000), decimals=1)
    cc_CO2_all = np.around(np.divide([cc_CO2_NZ, cc_CO2_NE2050, cc_CO2_NE2040, cc_CO2_NE2030, cc_CO2_NE2020], 1000000), decimals=1)
    ccccs_CO2_all = np.around(np.divide([ccccs_CO2_NZ, ccccs_CO2_NE2050, ccccs_CO2_NE2040, ccccs_CO2_NE2030, ccccs_CO2_NE2020], 1000000), decimals=1)

    return (dac_Gen_all, Coal_Gen_all, CC_Gen_all, CCCCS_Gen_all, wind_Gen_all,solar_Gen_all, battery_Gen_all, hydrogen_Gen_all,
            dac_CO2_all, coal_CO2_all, cc_CO2_all, ccccs_CO2_all, bw_NZ, bw_NE2020, bw_NE2030, bw_NE2040, bw_NE2050)
