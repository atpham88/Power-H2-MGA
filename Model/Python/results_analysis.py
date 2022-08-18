'''
An Pham
Create result figures
'''

import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as PathEffects
from scipy.interpolate import griddata
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from palettable.wesanderson import Margot1_5
from palettable.colorbrewer.qualitative import *

from cfigures_gen_hours import gen_hours_figures
from cfigures_cap import cap_figures
from cfigures_gen import gen_figures

case_to_run = 3
elect_demand = 1
co2EmsCapInFinalYear = -724.6662647

m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\"
save_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Draft\\"

if case_to_run == 1:
    case_name = "reference"
elif case_to_run == 2:
    case_name = "lNuclearCCS"
elif case_to_run == 3:
    case_name = "lH2"
elif case_to_run == 4:
    case_name = "lTrans"

if elect_demand == 1:
    high_elect = ""
elif elect_demand == 2:
    high_elect = "HE"

if elect_demand == 1:
    resultsDir_NZ_temp = 'Results_EI_NetZero_0_TrueREFERENCE'
    resultsDir_NE2020_temp = 'Results_EI_NegativeNEin2020_-724_TrueREFERENCE'
    resultsDir_NE2030_temp = 'Results_EI_NegativeNEin2030_-724_TrueREFERENCE'
    resultsDir_NE2040_temp = 'Results_EI_NegativeNEin2040_-724_TrueREFERENCE'
    resultsDir_NE2050_temp = 'Results_EI_NegativeNEin2050_-724_TrueREFERENCE'
    resultsDir_other_NZ = 'Results_EI_NetZero_DACS2020_'+case_name+'_TrueREFERENCE'+'\\2050CO2Cap0\\CE\\'
    resultsDir_other_NE2020 = 'Results_EI_Negative-724_DACS2020NEin2020_' + case_name + '_TrueREFERENCE'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2030 = 'Results_EI_Negative-724_DACS2020NEin2030_' + case_name + '_TrueREFERENCE'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2040 = 'Results_EI_Negative-724_DACS2020NEin2040_' + case_name + '_TrueREFERENCE'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2050_1 = 'Results_EI_Negative-724_DACS2020NEin2050_' + case_name + '_TrueREFERENCE'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2050_2 = 'Results_EI_Negative-724_DACS2020NEin2050_' + case_name + '_TrueREFERENCE' + '\\2060CO2Cap-724\\CE\\'
elif elect_demand == 2:
    resultsDir_NZ_temp = 'Results_EI_NetZero_0_TrueHIGH'
    resultsDir_NE2020_temp = 'Results_EI_NegativeNEin2020_-724_TrueHIGH'
    resultsDir_NE2030_temp = 'Results_EI_NegativeNEin2030_-724_TrueHIGH'
    resultsDir_NE2040_temp = 'Results_EI_NegativeNEin2040_-724_TrueHIGH'
    resultsDir_NE2050_temp = 'Results_EI_NegativeNEin2050_-724_TrueHIGH'
    resultsDir_other_NZ = 'Results_EI_NetZero_DACS2020_' + case_name + '_TrueHIGH'+'\\2050CO2Cap0\\CE\\'
    resultsDir_other_NE2020 = 'Results_EI_Negative-724_DACS2020NEin2020_' + case_name + '_TrueHIGH'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2030 = 'Results_EI_Negative-724_DACS2020NEin2030_' + case_name + '_TrueHIGH'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2040 = 'Results_EI_Negative-724_DACS2020NEin2040_' + case_name + '_TrueHIGH'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2050_1 = 'Results_EI_Negative-724_DACS2020NEin2050_' + case_name + '_TrueHIGH'+'\\2050CO2Cap-724\\CE\\'
    resultsDir_other_NE2050_2 = 'Results_EI_Negative-724_DACS2020NEin2050_' + case_name + '_TrueHIGH' + '\\2060CO2Cap-724\\CE\\'

resultsDir_NZ = resultsDir_NZ_temp + case_name
resultsDir_NE2020 = resultsDir_NE2020_temp + case_name
resultsDir_NE2030 = resultsDir_NE2030_temp + case_name
resultsDir_NE2040 = resultsDir_NE2040_temp + case_name
resultsDir_NE2050 = resultsDir_NE2050_temp + case_name

# %% Calculate DAC CFs:
# DAC capacity in 2050:
(CC_CE_all, CCCCS_CE_all, nuclear_CE_all, wind_CE_all, solar_CE_all, battery_CE_all, hydrogen_CE_all, dac_CE_all,
 CC_CE_SERC, CCCCS_CE_SERC, nuclear_CE_SERC, wind_CE_SERC, solar_CE_SERC, battery_CE_SERC, hydrogen_CE_SERC, dac_CE_SERC,
 CC_CE_MISO, CCCCS_CE_MISO, nuclear_CE_MISO, wind_CE_MISO, solar_CE_MISO, battery_CE_MISO, hydrogen_CE_MISO, dac_CE_MISO,
 CC_CE_PJM, CCCCS_CE_PJM, nuclear_CE_PJM, wind_CE_PJM, solar_CE_PJM, battery_CE_PJM, hydrogen_CE_PJM, dac_CE_PJM,
 CC_CE_SPP, CCCCS_CE_SPP, nuclear_CE_SPP, wind_CE_SPP, solar_CE_SPP, battery_CE_SPP, hydrogen_CE_SPP, dac_CE_SPP,
 CC_CE_NY, CCCCS_CE_NY, nuclear_CE_NY, wind_CE_NY, solar_CE_NY, battery_CE_NY, hydrogen_CE_NY, dac_CE_NY,
 CC_CE_NE, CCCCS_CE_NE, nuclear_CE_NE, wind_CE_NE, solar_CE_NE, battery_CE_NE, hydrogen_CE_NE, dac_CE_NE) \
    = cap_figures(m_dir, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030,
                  resultsDir_other_NE2040,resultsDir_other_NE2050_2)



# %% Storage profiles:
(dac_Gen_all, Coal_Gen_all, CC_Gen_all, CCCCS_Gen_all, wind_Gen_all,solar_Gen_all, battery_Gen_all, hydrogen_Gen_all,
 dac_CO2_all, coal_CO2_all, cc_CO2_all, ccccs_CO2_all,
 bw_NZ, bw_NE2020, bw_NE2030, bw_NE2040, bw_NE2050) = gen_hours_figures(m_dir, resultsDir_other_NZ, resultsDir_other_NE2020,
                                                                        resultsDir_other_NE2030, resultsDir_other_NE2040,
                                                                        resultsDir_other_NE2050_2)

dac_gen = dac_Gen_all.sum(axis=1)*1000
dac_cap_NZ = sum(dac_CE_all[0]*bw_NZ['block_c'])
dac_cap_NE2020 = sum(dac_CE_all[1]*bw_NE2020['block_c'])
dac_cap_NE2030 = sum(dac_CE_all[2]*bw_NE2030['block_c'])
dac_cap_NE2040 = sum(dac_CE_all[3]*bw_NE2040['block_c'])
dac_cap_NE2050 = sum(dac_CE_all[4]*bw_NE2050['block_c'])

dac_cap = np.around([dac_cap_NZ, dac_cap_NE2050, dac_cap_NE2040, dac_cap_NE2030, dac_cap_NE2020])

dac_cf = dac_gen/dac_cap

# Graph CO2 emission:
barWidth = 0.1
ind = np.arange(5)

fig, ax = plt.subplots(figsize=(19, 9))
ax.bar(ind, coal_CO2_all, color='dimgray', width=barWidth, edgecolor='white', label='Coal')
ax.bar(ind+barWidth, cc_CO2_all, color='silver', width=barWidth, edgecolor='white', label='CC')
ax.bar(ind+barWidth*2, ccccs_CO2_all, color='lightpink', width=barWidth, edgecolor='white', label='CCCCS')
ax.bar(ind+barWidth*3, dac_CO2_all, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('CO2 Emission (Million tons)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CO2_ ' + case_name + '_' + high_elect, dpi=300)

# Graph DAC generation:
fig, ax = plt.subplots(figsize=(19, 9))
ax.plot(dac_Gen_all[1,:], color='black', label='DAC Gen - NES in 2020')
ax.plot(hydrogen_Gen_all[1,:], color='lightpink', label='H2 Gen - NES in 2020')
ax.plot(battery_Gen_all[1,:], color='saddlebrown',  label='Battery Gen - NES in 2020')
ax.autoscale()
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_genDAC_ ' + case_name + '_' + high_elect, dpi=300)