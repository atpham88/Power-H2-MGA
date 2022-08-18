import pandas as pd
import numpy as np

def gen_load_figures(m_dir, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
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