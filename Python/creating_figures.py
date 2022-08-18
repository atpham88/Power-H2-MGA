'''
An Pham
Create capacity investment and cost figures
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

from cfigures_cap import cap_figures
from cfigures_installed_cap import installed_cap_figures
from cfigures_cap_2050 import cap_figures_2050
#from cfigures_costs import cost_figures
from cfigures_gen import gen_figures
from cfigures_flow import flow_figures
from cfigures_transline import transline_figures
from cfigures_resite import resite_figures
from wind_deployment import widep_figures

case_to_run = 1
elect_demand = 1
co2EmsCapInFinalYear = -724.6662647

m_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Results Summary\\"
m_dir2 = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\"
save_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Draft\\"
shapefile_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\REEDS\\Shapefiles\\"
merra_dir = "C:\\Users\\atpha\\Documents\\Postdocs\\Projects\\NETs\\Model\\EI-CE\\Python\\Data\\MERRA\\"

if case_to_run == 1: case_name = "reference"
elif case_to_run == 2: case_name = "lNuclearCCS"
elif case_to_run == 3: case_name = "lH2"
elif case_to_run == 4: case_name = "lTrans"

if elect_demand == 1: high_elect = ""
elif elect_demand == 2: high_elect = "HE"

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

# %% Graph Cost:
#(NZ_tot_cost, NE2050_tot_cost, NE2040_tot_cost, NE2030_tot_cost, NE2020_tot_cost,
# NZ_cap_cost, NE2050_cap_cost, NE2040_cap_cost, NE2030_cap_cost, NE2020_cap_cost,
# NZ_ope_cost, NE2050_ope_cost, NE2040_ope_cost, NE2030_ope_cost, NE2020_ope_cost,
# NE2020_aba_cost, NE2030_aba_cost, NE2040_aba_cost, NE2050_aba_cost,
# NZ_trans_cost, NE2050_trans_cost, NE2040_trans_cost, NE2030_trans_cost, NE2020_trans_cost) \
#    = cost_figures(m_dir, resultsDir_NZ, resultsDir_NE2020, resultsDir_NE2030,
#                   resultsDir_NE2040, resultsDir_NE2050, co2EmsCapInFinalYear)
#
#x = np.array([2030, 2040, 2050])

# Total cost:
#fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
#plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.3)
#plt.axvline(x=2030, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2040, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2050, color='lightgrey', linestyle=':', alpha=0.5)
#plt.plot(x, NZ_tot_cost, 'o-', linewidth=2, label="NZS", color='darkgrey', alpha=0.7)
#plt.plot(x, NE2050_tot_cost, 'o-', linewidth=2, label="NES in 2050", linestyle='-', color='saddlebrown', alpha=0.7)
#plt.plot(x, NE2040_tot_cost, 'o-', linewidth=2, label="NES in 2040", linestyle='-', color='lightpink')
#plt.plot(x, NE2030_tot_cost, 'o-', linewidth=2, label="NES in 2030", linestyle='-', color='deepskyblue', alpha=0.7)
#plt.plot(x, NE2020_tot_cost, 'o-', linewidth=2, label="NES in 2020", linestyle='-', color='olivedrab', alpha=0.7)
#plt.xticks([2030, 2040, 2050], fontsize=17)
#plt.yticks(fontsize=17)
#plt.xlabel('Years', fontsize=20)
#plt.ylabel('Total Costs (Billion $)', fontsize=20)
#plt.legend(fontsize=17, loc='upper left')
#plt.show()
#fig.savefig(save_dir + 'tot_Cost_ ' + case_name + '_' + high_elect, dpi=300)

# Cap cost:
#fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
#plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.3)
#plt.axvline(x=2030, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2040, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2050, color='lightgrey', linestyle=':', alpha=0.5)
#plt.plot(x, NZ_cap_cost, 'o-', linewidth=2, label="NZS", color='darkgrey', alpha=0.7)
#plt.plot(x, NE2050_cap_cost, 'o-', linewidth=2, label="NES in 2050", linestyle='-', color='saddlebrown', alpha=0.7)
#plt.plot(x, NE2040_cap_cost, 'o-', linewidth=2, label="NES in 2040", linestyle='-', color='lightpink')
#plt.plot(x, NE2030_cap_cost, 'o-', linewidth=2, label="NES in 2030", linestyle='-', color='deepskyblue', alpha=0.7)
#plt.plot(x, NE2020_cap_cost, 'o-', linewidth=2, label="NES in 2020", linestyle='-', color='olivedrab', alpha=0.7)
#plt.xticks([2030, 2040, 2050], fontsize=17)
#plt.yticks(fontsize=17)
#plt.xlabel('Years', fontsize=20)
#plt.ylabel('Total Capital Costs (Billion $)', fontsize=20)
#plt.legend(fontsize=17, loc='upper left')
#plt.show()
#fig.savefig(save_dir + 'cap_Cost_ ' + case_name + '_' + high_elect, dpi=300)

# Operating cost:
#fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
#plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.3)
#plt.axvline(x=2030, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2040, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2050, color='lightgrey', linestyle=':', alpha=0.5)
#plt.plot(x, NZ_ope_cost, 'o-', linewidth=2, label="NZS", color='darkgrey', alpha=0.7)
#plt.plot(x, NE2050_ope_cost, 'o-', linewidth=2, label="NES in 2050", linestyle='-', color='saddlebrown', alpha=0.7)
#plt.plot(x, NE2040_ope_cost, 'o-', linewidth=2, label="NES in 2040", linestyle='-', color='lightpink')
#plt.plot(x, NE2030_ope_cost, 'o-', linewidth=2, label="NES in 2030", linestyle='-', color='deepskyblue', alpha=0.7)
#plt.plot(x, NE2020_ope_cost, 'o-', linewidth=2, label="NES in 2020", linestyle='-', color='olivedrab', alpha=0.7)
#plt.xticks([2030, 2040, 2050], fontsize=17)
#plt.yticks(fontsize=17)
#plt.xlabel('Years', fontsize=20)
#plt.ylabel('Total Operating Costs (Billion $)', fontsize=20)
#plt.legend(fontsize=17, loc='upper left')
#plt.show()
#fig.savefig(save_dir + 'ope_Cost_ ' + case_name + '_' + high_elect, dpi=300)

# Abatement Cost:
#abatement_cost = {'NES in 2050': NE2050_aba_cost, 'NES in 2040': NE2040_aba_cost, 'NES in 2030': NE2030_aba_cost, 'NES in 2020': NE2020_aba_cost}
#decarb_path = list(abatement_cost.keys())
#aba_cost = list(abatement_cost.values())

#fig, ax = plt.subplots(figsize=(10, 6.5), tight_layout=True)
#plt.bar(decarb_path, aba_cost, color='skyblue', width=0.4)
#ax.text(decarb_path[0], NE2050_aba_cost*1.02, str(int(np.around(NE2050_aba_cost, decimals=0))), va='center', fontsize=14)
#ax.text(decarb_path[1], NE2040_aba_cost*1.02, str(int(np.around(NE2040_aba_cost, decimals=0))), va='center', fontsize=14)
#ax.text(decarb_path[2], NE2030_aba_cost*1.022, str(int(np.around(NE2030_aba_cost, decimals=0))), va='center', fontsize=14)
#ax.text(decarb_path[3], NE2020_aba_cost*1.025, str(int(np.around(NE2020_aba_cost, decimals=0))), va='center', fontsize=14)
#plt.ylabel("Abatement Cost in 2050 ($/ton of CO2)", fontsize=20)
#plt.xticks(fontsize=17)
#plt.yticks(fontsize=17)
#plt.show()
#fig.savefig(save_dir + 'aba_Cost_ ' + case_name + '_' + high_elect, dpi=300)

# Trans cap cost:
#fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
#plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.3)
#plt.axvline(x=2030, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2040, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2050, color='lightgrey', linestyle=':', alpha=0.5)
#plt.plot(x, NZ_trans_cost, 'o-', linewidth=2, label="NZS", color='darkgrey', alpha=0.7)
#plt.plot(x, NE2050_trans_cost, 'o-', linewidth=2, label="NES in 2050", linestyle='-', color='saddlebrown', alpha=0.7)
#plt.plot(x, NE2040_trans_cost, 'o-', linewidth=2, label="NES in 2040", linestyle='-', color='lightpink')
#plt.plot(x, NE2030_trans_cost, 'o-', linewidth=2, label="NES in 2030", linestyle='-', color='deepskyblue', alpha=0.7)
#plt.plot(x, NE2020_trans_cost, 'o-', linewidth=2, label="NES in 2020", linestyle='-', color='olivedrab', alpha=0.7)
#plt.xticks([2030, 2040, 2050], fontsize=17)
#plt.yticks(fontsize=17)
#plt.xlabel('Years', fontsize=20)
#plt.ylabel('Transmission Capital Costs (Billion $)', fontsize=20)
#plt.legend(fontsize=17, loc='upper left')
#plt.show()
#fig.savefig(save_dir + 'trans_Cost_ ' + case_name + '_' + high_elect, dpi=300)

# Resource Cap cost:
#fig, ax = plt.subplots(figsize=(10, 6), tight_layout=True)
##plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.3)
#plt.axvline(x=2030, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2040, color='lightgrey', linestyle=':', alpha=0.5)
#plt.axvline(x=2050, color='lightgrey', linestyle=':', alpha=0.5)
#plt.plot(x, NZ_cap_cost-NZ_trans_cost, 'o-', linewidth=2, label="NZS", color='darkgrey', alpha=0.7)
#plt.plot(x, NE2050_cap_cost-NE2050_trans_cost, 'o-', linewidth=2, label="NES in 2050", linestyle='-', color='saddlebrown', alpha=0.7)
#plt.plot(x, NE2040_cap_cost-NE2040_trans_cost, 'o-', linewidth=2, label="NES in 2040", linestyle='-', color='lightpink')
#plt.plot(x, NE2030_cap_cost-NE2030_trans_cost, 'o-', linewidth=2, label="NES in 2030", linestyle='-', color='deepskyblue', alpha=0.7)
#plt.plot(x, NE2020_cap_cost-NE2020_trans_cost, 'o-', linewidth=2, label="NES in 2020", linestyle='-', color='olivedrab', alpha=0.7)
#plt.xticks([2030, 2040, 2050], fontsize=17)
#plt.yticks(fontsize=17)
##plt.xlabel('Years', fontsize=20)
#plt.ylabel('Resource Capital Costs (Billion $)', fontsize=20)
#plt.legend(fontsize=17, loc='upper left')
#plt.show()
#fig.savefig(save_dir + 'resourceCap_Cost_ ' + case_name + '_' + high_elect, dpi=300)

# %% Capacity figures:
(CC_CE_all, CCCCS_CE_all, nuclear_CE_all, wind_CE_all, solar_CE_all, battery_CE_all, hydrogen_CE_all, dac_CE_all,
    CC_CE_SERC, CCCCS_CE_SERC, nuclear_CE_SERC, wind_CE_SERC, solar_CE_SERC, battery_CE_SERC, hydrogen_CE_SERC, dac_CE_SERC,
    CC_CE_MISO, CCCCS_CE_MISO, nuclear_CE_MISO, wind_CE_MISO, solar_CE_MISO, battery_CE_MISO, hydrogen_CE_MISO, dac_CE_MISO,
    CC_CE_PJM, CCCCS_CE_PJM, nuclear_CE_PJM, wind_CE_PJM, solar_CE_PJM, battery_CE_PJM, hydrogen_CE_PJM, dac_CE_PJM,
    CC_CE_SPP, CCCCS_CE_SPP, nuclear_CE_SPP, wind_CE_SPP, solar_CE_SPP, battery_CE_SPP, hydrogen_CE_SPP, dac_CE_SPP,
    CC_CE_NY, CCCCS_CE_NY, nuclear_CE_NY, wind_CE_NY, solar_CE_NY, battery_CE_NY, hydrogen_CE_NY, dac_CE_NY,
    CC_CE_NE, CCCCS_CE_NE, nuclear_CE_NE, wind_CE_NE, solar_CE_NE, battery_CE_NE, hydrogen_CE_NE, dac_CE_NE) \
    = cap_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2)

barWidth = 0.1
ind = np.arange(5)

fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_all, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_all, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_all, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_all, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_all, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_all, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_all, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_all, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('Capacity Investment 2020-2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_ ' + case_name + '_' + high_elect, dpi=300)

# SERC:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_SERC, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_SERC, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_SERC, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_SERC, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_SERC, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_SERC, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_SERC, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_SERC, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('SERC Capacity Investments by 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_SERC' + case_name + '_' + high_elect, dpi=300)

# MISO:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_MISO, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_MISO, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_MISO, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_MISO, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_MISO, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_MISO, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_MISO, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_MISO, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('MISO Capacity Investments by 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_MISO' + case_name + '_' + high_elect, dpi=300)

# PJM:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_PJM, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_PJM, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_PJM, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_PJM, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_PJM, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_PJM, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_PJM, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_PJM, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('PJM Capacity Investments by 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_PJM' + case_name + '_' + high_elect, dpi=300)

# SPP:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_SPP, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_SPP, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_SPP, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_SPP, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_SPP, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_SPP, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_SPP, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_SPP, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('SPP Capacity Investments by 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_SPP' + case_name + '_' + high_elect, dpi=300)

# NY:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_NY, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_NY, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_NY, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_NY, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_NY, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_NY, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_NY, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_NY, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('NY Capacity Investments by 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_NY' + case_name + '_' + high_elect, dpi=300)

# NE:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_NE, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_NE, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_NE, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_NE, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_NE, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_NE, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_NE, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_NE, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('NE Capacity Investments by 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_NE' + case_name + '_' + high_elect, dpi=300)

# graph installed capacity:
(dac_Cap_all, coal_Cap_all, CC_Cap_all, CCCCS_Cap_all, CT_Cap_all, OG_Cap_all, bio_Cap_all,
            bat_Cap_all,h2_Cap_all, nuclear_Cap_all, wind_Cap_all, solar_Cap_all, pump_Cap_all, other_Cap_all) \
    = installed_cap_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                            resultsDir_other_NE2050_2)

barWidth = 0.4
ind = np.arange(5)

fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Cap_all, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, coal_Cap_all, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Cap_all, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=coal_Cap_all)
ax.bar(ind, OG_Cap_all, color='darkred', width=barWidth, label='O/G Steam', bottom=coal_Cap_all+CT_Cap_all)
ax.bar(ind, CC_Cap_all, color='gainsboro', width=barWidth, label='NGCC', bottom=coal_Cap_all+OG_Cap_all+CT_Cap_all)
ax.bar(ind, CCCCS_Cap_all, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all)
ax.bar(ind, nuclear_Cap_all, color='lightpink', width=barWidth, label='Nuclear', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all)
ax.bar(ind, wind_Cap_all, color='skyblue', width=barWidth, label='Wind', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all+nuclear_Cap_all)
ax.bar(ind, solar_Cap_all, color='goldenrod', width=barWidth, label='Solar', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all+nuclear_Cap_all+wind_Cap_all)
ax.bar(ind, pump_Cap_all, color='aqua', width=barWidth, label='Pump Storage', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all+nuclear_Cap_all+wind_Cap_all+solar_Cap_all)
ax.bar(ind, bat_Cap_all, color='darkolivegreen', width=barWidth, label='Battery', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all+nuclear_Cap_all+wind_Cap_all+solar_Cap_all+pump_Cap_all)
ax.bar(ind, h2_Cap_all, color='lightseagreen', width=barWidth, label='H2', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all+nuclear_Cap_all+wind_Cap_all+solar_Cap_all+pump_Cap_all+bat_Cap_all)
ax.bar(ind, other_Cap_all, color='mediumpurple', width=barWidth, label='Others', bottom=coal_Cap_all+CC_Cap_all+OG_Cap_all+CT_Cap_all+CCCCS_Cap_all+nuclear_Cap_all+wind_Cap_all+solar_Cap_all+pump_Cap_all+bat_Cap_all+h2_Cap_all)
ax.autoscale()
plt.ylabel('EI Installed Capacity (GW)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_InCap_ ' + case_name + '_' + high_elect, dpi=300)

# %% Capacity figures in 2050:
(CC_CE_all, CCCCS_CE_all, nuclear_CE_all, wind_CE_all, solar_CE_all, battery_CE_all, hydrogen_CE_all, dac_CE_all,
    CC_CE_SERC, CCCCS_CE_SERC, nuclear_CE_SERC, wind_CE_SERC, solar_CE_SERC, battery_CE_SERC, hydrogen_CE_SERC, dac_CE_SERC,
    CC_CE_MISO, CCCCS_CE_MISO, nuclear_CE_MISO, wind_CE_MISO, solar_CE_MISO, battery_CE_MISO, hydrogen_CE_MISO, dac_CE_MISO,
    CC_CE_PJM, CCCCS_CE_PJM, nuclear_CE_PJM, wind_CE_PJM, solar_CE_PJM, battery_CE_PJM, hydrogen_CE_PJM, dac_CE_PJM,
    CC_CE_SPP, CCCCS_CE_SPP, nuclear_CE_SPP, wind_CE_SPP, solar_CE_SPP, battery_CE_SPP, hydrogen_CE_SPP, dac_CE_SPP,
    CC_CE_NY, CCCCS_CE_NY, nuclear_CE_NY, wind_CE_NY, solar_CE_NY, battery_CE_NY, hydrogen_CE_NY, dac_CE_NY,
    CC_CE_NE, CCCCS_CE_NE, nuclear_CE_NE, wind_CE_NE, solar_CE_NE, battery_CE_NE, hydrogen_CE_NE, dac_CE_NE) \
    = cap_figures_2050(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_2)

barWidth = 0.1
ind = np.arange(5)

fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_all, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_all, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_all, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_all, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_all, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_all, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_all, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_all, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('Capacity Investment in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_2050_ ' + case_name + '_' + high_elect, dpi=300)

# SERC:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_SERC, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_SERC, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_SERC, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_SERC, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_SERC, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_SERC, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_SERC, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_SERC, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('SERC Capacity Investments in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_SERC_2050' + case_name + '_' + high_elect, dpi=300)

# MISO:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_MISO, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_MISO, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_MISO, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_MISO, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_MISO, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_MISO, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_MISO, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_MISO, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('MISO Capacity Investments in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_MISO_2050' + case_name + '_' + high_elect, dpi=300)

# PJM:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_PJM, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_PJM, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_PJM, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_PJM, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_PJM, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_PJM, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_PJM, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_PJM, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('PJM Capacity Investments in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_PJM_2050' + case_name + '_' + high_elect, dpi=300)

# SPP:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_SPP, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_SPP, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_SPP, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_SPP, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_SPP, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_SPP, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_SPP, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_SPP, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('SPP Capacity Investments in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_SPP_2050' + case_name + '_' + high_elect, dpi=300)

# NY:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_NY, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_NY, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_NY, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_NY, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_NY, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_NY, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_NY, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_NY, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('NY Capacity Investments in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_NY_2050' + case_name + '_' + high_elect, dpi=300)

# NE:
fig, ax = plt.subplots(figsize=(19, 9))
plt.axvline(x=ind[0]+barWidth*9, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*9.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, CC_CE_NE, color='dimgray', width=barWidth, edgecolor='white', label='NGCC')
ax.bar(ind+barWidth, CCCCS_CE_NE, color='silver', width=barWidth, edgecolor='white', label='NGCC \n CCS')
ax.bar(ind+barWidth*2, nuclear_CE_NE, color='lightpink', width=barWidth, edgecolor='white', label='Nuclear')
ax.bar(ind+barWidth*3, wind_CE_NE, color='skyblue', width=barWidth, edgecolor='white', label='Wind')
ax.bar(ind+barWidth*4, solar_CE_NE, color='goldenrod', width=barWidth, edgecolor='white', label='Solar')
ax.bar(ind+barWidth*5, battery_CE_NE, color='darkolivegreen', width=barWidth, edgecolor='white', label='Battery')
ax.bar(ind+barWidth*6, hydrogen_CE_NE, color='lightseagreen', width=barWidth, edgecolor='white', label='H2')
ax.bar(ind+barWidth*7, -dac_CE_NE, color='saddlebrown', width=barWidth, edgecolor='white', label='DACS')
ax.autoscale()
plt.ylabel('NE Capacity Investments in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_CE_NE_2050' + case_name + '_' + high_elect, dpi=300)


# %% Graph generation:
(dac_Gen_all, Coal_Gen_all, CT_Gen_all, OG_Gen_all, CC_Gen_all, CCCCS_Gen_all,
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
 load_tot,load_serc,load_miso,load_ne,load_ny,load_pjm,load_spp) \
    = gen_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030,
                  resultsDir_other_NE2040, resultsDir_other_NE2050_2)

barWidth = 0.4
ind = np.arange(5)

fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all)
ax.bar(ind, OG_Gen_all, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all+CT_Gen_all)
ax.bar(ind, CC_Gen_all, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all+OG_Gen_all+CT_Gen_all)
ax.bar(ind, CCCCS_Gen_all, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all)
ax.bar(ind, nuclear_Gen_all, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all)
ax.bar(ind, wind_Gen_all, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all+nuclear_Gen_all)
ax.bar(ind, solar_Gen_all, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all+nuclear_Gen_all+wind_Gen_all)
ax.bar(ind, pump_Gen_all, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all+nuclear_Gen_all+wind_Gen_all+solar_Gen_all)
ax.bar(ind, battery_Gen_all, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all+nuclear_Gen_all+wind_Gen_all+solar_Gen_all+pump_Gen_all)
ax.bar(ind, hydrogen_Gen_all, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all+nuclear_Gen_all+wind_Gen_all+solar_Gen_all+pump_Gen_all+battery_Gen_all)
ax.bar(ind, others_Gen_all, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all+CC_Gen_all+OG_Gen_all+CT_Gen_all+CCCCS_Gen_all+nuclear_Gen_all+wind_Gen_all+solar_Gen_all+pump_Gen_all+battery_Gen_all+hydrogen_Gen_all)
ax.plot(ind, load_tot, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('EI Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_ ' + case_name + '_' + high_elect, dpi=300)

# Graph generation by load zones
# SERC:
fig, ax = plt.subplots(figsize=(12, 6))
barWidth = 0.4
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all_SERC, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all_SERC, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all_SERC, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all_SERC)
ax.bar(ind, OG_Gen_all_SERC, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all_SERC+CT_Gen_all_SERC)
ax.bar(ind, CC_Gen_all_SERC, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC)
ax.bar(ind, CCCCS_Gen_all_SERC, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC)
ax.bar(ind, nuclear_Gen_new_SERC+nuclear_Gen_existing_SERC, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC)
ax.bar(ind, wind_Gen_all_SERC, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC+nuclear_Gen_existing_SERC+nuclear_Gen_new_SERC)
ax.bar(ind, solar_Gen_all_SERC, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC+nuclear_Gen_existing_SERC+nuclear_Gen_new_SERC+wind_Gen_all_SERC)
ax.bar(ind, pump_Gen_all_SERC, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC+nuclear_Gen_existing_SERC+nuclear_Gen_new_SERC+wind_Gen_all_SERC+solar_Gen_all_SERC)
ax.bar(ind, battery_Gen_all_SERC, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC+nuclear_Gen_existing_SERC+nuclear_Gen_new_SERC+wind_Gen_all_SERC+solar_Gen_all_SERC+pump_Gen_all_SERC)
ax.bar(ind, hydrogen_Gen_all_SERC, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC+nuclear_Gen_existing_SERC+nuclear_Gen_new_SERC+wind_Gen_all_SERC+solar_Gen_all_SERC+pump_Gen_all_SERC+battery_Gen_all_SERC)
ax.bar(ind, others_Gen_all_SERC, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all_SERC+CC_Gen_all_SERC+OG_Gen_all_SERC+CT_Gen_all_SERC+CCCCS_Gen_all_SERC+nuclear_Gen_existing_SERC+nuclear_Gen_new_SERC+wind_Gen_all_SERC+solar_Gen_all_SERC+pump_Gen_all_SERC+battery_Gen_all_SERC+hydrogen_Gen_all_SERC)
ax.plot(ind, load_serc, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('SERC Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_SERC ' + case_name + '_' + high_elect, dpi=300)

# MISO:
fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all_MISO, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all_MISO, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all_MISO, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all_MISO)
ax.bar(ind, OG_Gen_all_MISO, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all_MISO+CT_Gen_all_MISO)
ax.bar(ind, CC_Gen_all_MISO, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO)
ax.bar(ind, CCCCS_Gen_all_MISO, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO)
ax.bar(ind, nuclear_Gen_new_MISO+nuclear_Gen_existing_MISO, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO)
ax.bar(ind, wind_Gen_all_MISO, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO+nuclear_Gen_existing_MISO+nuclear_Gen_new_MISO)
ax.bar(ind, solar_Gen_all_MISO, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO+nuclear_Gen_existing_MISO+nuclear_Gen_new_MISO+wind_Gen_all_MISO)
ax.bar(ind, pump_Gen_all_MISO, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO+nuclear_Gen_existing_MISO+nuclear_Gen_new_MISO+wind_Gen_all_MISO+solar_Gen_all_MISO)
ax.bar(ind, battery_Gen_all_MISO, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO+nuclear_Gen_existing_MISO+nuclear_Gen_new_MISO+wind_Gen_all_MISO+solar_Gen_all_MISO+pump_Gen_all_MISO)
ax.bar(ind, hydrogen_Gen_all_MISO, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO+nuclear_Gen_existing_MISO+nuclear_Gen_new_MISO+wind_Gen_all_MISO+solar_Gen_all_MISO+pump_Gen_all_MISO+battery_Gen_all_MISO)
ax.bar(ind, others_Gen_all_MISO, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all_MISO+CC_Gen_all_MISO+OG_Gen_all_MISO+CT_Gen_all_MISO+CCCCS_Gen_all_MISO+nuclear_Gen_existing_MISO+nuclear_Gen_new_MISO+wind_Gen_all_MISO+solar_Gen_all_MISO+pump_Gen_all_MISO+battery_Gen_all_MISO+hydrogen_Gen_all_MISO)
ax.plot(ind, load_miso, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('MISO Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_MISO ' + case_name + '_' + high_elect, dpi=300)

# NE:
fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all_NE, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all_NE, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all_NE, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all_NE)
ax.bar(ind, OG_Gen_all_NE, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all_NE+CT_Gen_all_NE)
ax.bar(ind, CC_Gen_all_NE, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE)
ax.bar(ind, CCCCS_Gen_all_NE, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE)
ax.bar(ind, nuclear_Gen_new_NE+nuclear_Gen_existing_NE, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE)
ax.bar(ind, wind_Gen_all_NE, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE+nuclear_Gen_existing_NE+nuclear_Gen_new_NE)
ax.bar(ind, solar_Gen_all_NE, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE+nuclear_Gen_existing_NE+nuclear_Gen_new_NE+wind_Gen_all_NE)
ax.bar(ind, pump_Gen_all_NE, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE+nuclear_Gen_existing_NE+nuclear_Gen_new_NE+wind_Gen_all_NE+solar_Gen_all_NE)
ax.bar(ind, battery_Gen_all_NE, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE+nuclear_Gen_existing_NE+nuclear_Gen_new_NE+wind_Gen_all_NE+solar_Gen_all_NE+pump_Gen_all_NE)
ax.bar(ind, hydrogen_Gen_all_NE, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE+nuclear_Gen_existing_NE+nuclear_Gen_new_NE+wind_Gen_all_NE+solar_Gen_all_NE+pump_Gen_all_NE+battery_Gen_all_NE)
ax.bar(ind, others_Gen_all_NE, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all_NE+CC_Gen_all_NE+OG_Gen_all_NE+CT_Gen_all_NE+CCCCS_Gen_all_NE+nuclear_Gen_existing_NE+nuclear_Gen_new_NE+wind_Gen_all_NE+solar_Gen_all_NE+pump_Gen_all_NE+battery_Gen_all_NE+hydrogen_Gen_all_NE)
ax.plot(ind, load_ne, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('ISONE Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_NE ' + case_name + '_' + high_elect, dpi=300)

# NY:
fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all_NY, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all_NY, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all_NY, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all_NY)
ax.bar(ind, OG_Gen_all_NY, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all_NY+CT_Gen_all_NY)
ax.bar(ind, CC_Gen_all_NY, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY)
ax.bar(ind, CCCCS_Gen_all_NY, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY)
ax.bar(ind, nuclear_Gen_new_NY+nuclear_Gen_existing_NY, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY)
ax.bar(ind, wind_Gen_all_NY, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY+nuclear_Gen_existing_NY+nuclear_Gen_new_NY)
ax.bar(ind, solar_Gen_all_NY, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY+nuclear_Gen_existing_NY+nuclear_Gen_new_NY+wind_Gen_all_NY)
ax.bar(ind, pump_Gen_all_NY, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY+nuclear_Gen_existing_NY+nuclear_Gen_new_NY+wind_Gen_all_NY+solar_Gen_all_NY)
ax.bar(ind, battery_Gen_all_NY, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY+nuclear_Gen_existing_NY+nuclear_Gen_new_NY+wind_Gen_all_NY+solar_Gen_all_NY+pump_Gen_all_NY)
ax.bar(ind, hydrogen_Gen_all_NY, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY+nuclear_Gen_existing_NY+nuclear_Gen_new_NY+wind_Gen_all_NY+solar_Gen_all_NY+pump_Gen_all_NY+battery_Gen_all_NY)
ax.bar(ind, others_Gen_all_NY, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all_NY+CC_Gen_all_NY+OG_Gen_all_NY+CT_Gen_all_NY+CCCCS_Gen_all_NY+nuclear_Gen_existing_NY+nuclear_Gen_new_NY+wind_Gen_all_NY+solar_Gen_all_NY+pump_Gen_all_NY+battery_Gen_all_NY+hydrogen_Gen_all_NY)
ax.plot(ind, load_ny, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('NYISO Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_NY ' + case_name + '_' + high_elect, dpi=300)

# PJM:
fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all_PJM, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all_PJM, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all_PJM, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all_PJM)
ax.bar(ind, OG_Gen_all_PJM, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all_PJM+CT_Gen_all_PJM)
ax.bar(ind, CC_Gen_all_PJM, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM)
ax.bar(ind, CCCCS_Gen_all_PJM, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM)
ax.bar(ind, nuclear_Gen_new_PJM+nuclear_Gen_existing_PJM, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM)
ax.bar(ind, wind_Gen_all_PJM, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM+nuclear_Gen_existing_PJM+nuclear_Gen_new_PJM)
ax.bar(ind, solar_Gen_all_PJM, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM+nuclear_Gen_existing_PJM+nuclear_Gen_new_PJM+wind_Gen_all_PJM)
ax.bar(ind, pump_Gen_all_PJM, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM+nuclear_Gen_existing_PJM+nuclear_Gen_new_PJM+wind_Gen_all_PJM+solar_Gen_all_PJM)
ax.bar(ind, battery_Gen_all_PJM, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM+nuclear_Gen_existing_PJM+nuclear_Gen_new_PJM+wind_Gen_all_PJM+solar_Gen_all_PJM+pump_Gen_all_PJM)
ax.bar(ind, hydrogen_Gen_all_PJM, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM+nuclear_Gen_existing_PJM+nuclear_Gen_new_PJM+wind_Gen_all_PJM+solar_Gen_all_PJM+pump_Gen_all_PJM+battery_Gen_all_PJM)
ax.bar(ind, others_Gen_all_PJM, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all_PJM+CC_Gen_all_PJM+OG_Gen_all_PJM+CT_Gen_all_PJM+CCCCS_Gen_all_PJM+nuclear_Gen_existing_PJM+nuclear_Gen_new_PJM+wind_Gen_all_PJM+solar_Gen_all_PJM+pump_Gen_all_PJM+battery_Gen_all_PJM+hydrogen_Gen_all_PJM)
ax.plot(ind, load_pjm, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('PJM Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_PJM ' + case_name + '_' + high_elect, dpi=300)

# SPP:
fig, ax = plt.subplots(figsize=(12, 6))
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
ax.bar(ind, dac_Gen_all_SPP, color='saddlebrown', width=barWidth, label='DACS')
ax.bar(ind, Coal_Gen_all_SPP, color='black', width=barWidth, label='Coal Steam CCS')
ax.bar(ind, CT_Gen_all_SPP, color='darkgrey', width=barWidth, label='Combustion Turbine', bottom=Coal_Gen_all_SPP)
ax.bar(ind, OG_Gen_all_SPP, color='darkred', width=barWidth, label='O/G Steam', bottom=Coal_Gen_all_SPP+CT_Gen_all_SPP)
ax.bar(ind, CC_Gen_all_SPP, color='gainsboro', width=barWidth, label='NGCC', bottom=Coal_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP)
ax.bar(ind, CCCCS_Gen_all_SPP, color='lightsteelblue', width=barWidth, label='NGCC CCS', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP)
ax.bar(ind, nuclear_Gen_new_SPP+nuclear_Gen_existing_SPP, color='lightpink', width=barWidth, label='Nuclear', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP)
ax.bar(ind, wind_Gen_all_SPP, color='skyblue', width=barWidth, label='Wind', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP+nuclear_Gen_existing_SPP+nuclear_Gen_new_SPP)
ax.bar(ind, solar_Gen_all_SPP, color='goldenrod', width=barWidth, label='Solar', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP+nuclear_Gen_existing_SPP+nuclear_Gen_new_SPP+wind_Gen_all_SPP)
ax.bar(ind, pump_Gen_all_SPP, color='aqua', width=barWidth, label='Pump Storage', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP+nuclear_Gen_existing_SPP+nuclear_Gen_new_SPP+wind_Gen_all_SPP+solar_Gen_all_SPP)
ax.bar(ind, battery_Gen_all_SPP, color='darkolivegreen', width=barWidth, label='Battery', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP+nuclear_Gen_existing_SPP+nuclear_Gen_new_SPP+wind_Gen_all_SPP+solar_Gen_all_SPP+pump_Gen_all_SPP)
ax.bar(ind, hydrogen_Gen_all_SPP, color='lightseagreen', width=barWidth, label='H2', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP+nuclear_Gen_existing_SPP+nuclear_Gen_new_SPP+wind_Gen_all_SPP+solar_Gen_all_SPP+pump_Gen_all_SPP+battery_Gen_all_SPP)
ax.bar(ind, others_Gen_all_SPP, color='mediumpurple', width=barWidth, label='Others', bottom=Coal_Gen_all_SPP+CC_Gen_all_SPP+OG_Gen_all_SPP+CT_Gen_all_SPP+CCCCS_Gen_all_SPP+nuclear_Gen_existing_SPP+nuclear_Gen_new_SPP+wind_Gen_all_SPP+solar_Gen_all_SPP+pump_Gen_all_SPP+battery_Gen_all_SPP+hydrogen_Gen_all_SPP)
ax.plot(ind, load_spp, color='black', label='Load', marker='D', markersize=10, markeredgewidth=3, linestyle='None', markerfacecolor='None')
ax.autoscale()
plt.ylabel('SPP Generation (Thousand GWh)', fontsize=20)
plt.yticks(fontsize=16)
plt.legend(fontsize=17)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels(('NZS', 'NES \n in 2050', 'NES \n in 2040', 'NES \nin 2030', 'NES \nin 2020'), fontsize=17)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Gen_SPP ' + case_name + '_' + high_elect, dpi=300)

# Graph DAC gen by region:
fig, ax = plt.subplots(figsize=(19, 9))
barWidth = 0.1
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
plt.axvline(x=ind[0]+barWidth*7.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*7.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*7.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*7.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind, dac_Gen_MISO, color='skyblue', width=barWidth, edgecolor='white', label='MISO')
ax.bar(ind+barWidth, dac_Gen_NE, color='darkolivegreen', width=barWidth, edgecolor='white', label='ISONE')
ax.bar(ind+barWidth*2, dac_Gen_NY, color='lightpink', width=barWidth, edgecolor='white', label='NYISO')
ax.bar(ind+barWidth*3, dac_Gen_PJM, color='goldenrod', width=barWidth, edgecolor='white', label='PJM')
ax.bar(ind+barWidth*4, dac_Gen_SERC, color='saddlebrown', width=barWidth, edgecolor='white', label='SERC')
ax.bar(ind+barWidth*5, dac_Gen_SPP, color='lightseagreen', width=barWidth, edgecolor='white', label='SPP')
ax.autoscale()
plt.ylabel('DACS Generation in 2050 (Thousand GWh)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3.5)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_DAC_Gen_2050' + case_name + '_' + high_elect, dpi=300)

# %% Graph Flows:
(netFlow_miso_all, netFlow_ne_all, netFlow_ny_all, netFlow_pjm_all, netFlow_serc_all, netFlow_spp_all) \
    = flow_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_1, resultsDir_other_NE2050_2)

fig, ax = plt.subplots(figsize=(19, 9))
barWidth = 0.1
ind = np.arange(5)
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
plt.axvline(x=ind[0]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind+barWidth, netFlow_miso_all, color='skyblue', width=barWidth, edgecolor='white', label='MISO')
ax.bar(ind+barWidth*2, netFlow_ne_all, color='darkolivegreen', width=barWidth, edgecolor='white', label='ISONE')
ax.bar(ind+barWidth*3, netFlow_ny_all, color='lightpink', width=barWidth, edgecolor='white', label='NYISO')
ax.bar(ind+barWidth*4, netFlow_pjm_all, color='goldenrod', width=barWidth, edgecolor='white', label='PJM')
ax.bar(ind+barWidth*5, netFlow_serc_all, color='saddlebrown', width=barWidth, edgecolor='white', label='SERC')
ax.bar(ind+barWidth*6, netFlow_spp_all, color='lightseagreen', width=barWidth, edgecolor='white', label='SPP')
ax.autoscale()
plt.ylabel('Net Power Flows in 2050 (GWh)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Flow_2050' + case_name + '_' + high_elect, dpi=300)

# %% Graph Transmission Lines Built:
(pRegionShapes, loadregions, miso_serc, pjm_serc, ne_ny, pjm_ny, pjm_miso, spp_miso) \
    = transline_figures(shapefile_dir, m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030, resultsDir_other_NE2040,
                 resultsDir_other_NE2050_1, resultsDir_other_NE2050_2)

# Map:
fig, ax = plt.subplots()
cln = 'region'
ax.set_aspect('equal')
pRegionShapes.plot(ax=ax, column=cln, cmap=Set3_6.mpl_colormap, figsize=(200, 100),
                   edgecolors='black', linewidth=0.3)
                   #legend='True', legend_kwds=dict(loc='lower right', fontsize=9))
plt.axis('on')
for idx, row in loadregions.iterrows():
    fnt = 10
    txt=plt.annotate(s=row[cln], xy=(loadregions.geometry.centroid.x[idx],loadregions.geometry.centroid.y[idx]),
                 horizontalalignment='center', fontsize=8, wrap=True, color='k')
    txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
ax.autoscale()
minx, miny, maxx, maxy = pRegionShapes.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_Basemap', dpi=300)

(pRegionShapes, loadregions, miso_serc, pjm_serc, ne_ny, pjm_ny, pjm_miso, spp_miso) \
    = transline_figures(shapefile_dir,m_dir2,resultsDir_other_NZ, resultsDir_other_NE2020,
                        resultsDir_other_NE2030, resultsDir_other_NE2040,resultsDir_other_NE2050_1,
                        resultsDir_other_NE2050_2)

fig, ax = plt.subplots(figsize=(19, 9))
barWidth = 0.1
ind = np.arange(5)
plt.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.08)
plt.axvline(x=ind[0]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[1]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[2]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
plt.axvline(x=ind[3]+barWidth*8.5, color='black', linewidth=1, linestyle='-', alpha=1)
ax.bar(ind+barWidth, miso_serc, color='skyblue', width=barWidth, edgecolor='white', label='MISO-SERC')
ax.bar(ind+barWidth*2, pjm_serc, color='darkolivegreen', width=barWidth, edgecolor='white', label='PJM-SERC')
ax.bar(ind+barWidth*3, ne_ny, color='lightpink', width=barWidth, edgecolor='white', label='ISONE-NYISO')
ax.bar(ind+barWidth*4, pjm_ny, color='goldenrod', width=barWidth, edgecolor='white', label='PJM-NYISO')
ax.bar(ind+barWidth*5, pjm_miso, color='saddlebrown', width=barWidth, edgecolor='white', label='PJM-MISO')
ax.bar(ind+barWidth*6, spp_miso, color='lightseagreen', width=barWidth, edgecolor='white', label='SPP-MISO')
ax.autoscale()
plt.ylabel('Transmission Capacity Built in 2050 (GW)', fontsize=26)
plt.yticks(fontsize=21)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=22)
ax.set_xticks(ind+barWidth*3)
ax.set_xticklabels(('NZS', 'NES in 2050', 'NES in 2040', 'NES in 2030', 'NES in 2020'), fontsize=23)
fig.tight_layout()
plt.show()
fig.savefig(save_dir + '_LineCap_2050' + case_name + '_' + high_elect, dpi=300)

# %% Wind and solar capacity expansion:
(wind_cf, solar_cf) = resite_figures(merra_dir)

geometry = [Point(xy) for xy in zip(wind_cf.lon, wind_cf.lat)]
wind_cf = gpd.GeoDataFrame(wind_cf, crs="EPSG:4326", geometry=geometry)
solar_cf = gpd.GeoDataFrame(solar_cf, crs="EPSG:4326", geometry=geometry)

latlonGpd_wind_join = gpd.sjoin(wind_cf, pRegionShapes, how="inner", op='intersects')

# Map of renewable sites:
fig, ax = plt.subplots()
cln = 'region'
#ax.set_aspect('equal')
wind_cf.plot(ax=ax, column='wind_cf', cmap='viridis_r', markersize=5, legend='True', label="Wind capacity factor")

loadregions.plot(ax=ax, facecolor="none",figsize=(200, 100),
                   edgecolors='black', linewidth=0.7)
                   #legend='True', legend_kwds=dict(loc='lower right', fontsize=9))
plt.axis('on')
f = plt.gcf()
cax = f.get_axes()[1]
cax.set_ylabel("Wind capacity factor")
for idx, row in loadregions.iterrows():
    fnt = 10
    txt=plt.annotate(s=row[cln], xy=(loadregions.geometry.centroid.x[idx],loadregions.geometry.centroid.y[idx]),
                 horizontalalignment='center', fontsize=8, wrap=True, color='k')
    txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
#ax.autoscale()
#sm = plt.cm.ScalarMappable(cmap='rainbow', norm=plt.Normalize(vmin=latlonGpd_join['wind_cf'].min(), vmax=latlonGpd_join['wind_cf'].max()))
#cbar_axis = inset_axes(latlonGpd_join, width='10%', height='5%',loc='lower right')
#plt.colorbar(sm, cax=cbar_axis, orientation='horizontal', pad=0.02)
#latlonGpd_join.text(x=-74, y=28, s='Wind capacity factors', fontsize=9.8)
minx, miny, maxx, maxy = pRegionShapes.total_bounds
plt.xlim(minx, maxx)
plt.ylim(miny, maxy)
fig.tight_layout()
plt.show()

fig.savefig(save_dir + '_WindMap_MERRA', dpi=300)

# %% Wind deployment:
(wind_CE_NZ, solar_CE_NZ, wind_CE_NE2020, solar_CE_NE2020, wind_CE_NE2030, solar_CE_NE2030,
 wind_CE_NE2040, solar_CE_NE2040, wind_CE_NE2050, solar_CE_NE2050) = \
    widep_figures(m_dir2, resultsDir_other_NZ, resultsDir_other_NE2020, resultsDir_other_NE2030,
                resultsDir_other_NE2040, resultsDir_other_NE2050_2)

geometry = [Point(xy) for xy in zip(wind_CE_NE2050.lon, wind_CE_NE2050.lat)]
windDep_cf = gpd.GeoDataFrame(wind_CE_NE2050, crs="EPSG:4326", geometry=geometry)

# Map of renewable sites:
fig, ax = plt.subplots()
cln = 'region'
#ax.set_aspect('equal')
windDep_cf.plot(ax=ax, column='Capacity (MW)', cmap='viridis_r', markersize=20, legend='True', label="Wind capacity factor")

loadregions.plot(ax=ax, facecolor="none",figsize=(200, 100),
                   edgecolors='black', linewidth=0.7)
                   #legend='True', legend_kwds=dict(loc='lower right', fontsize=9))
plt.axis('on')
f = plt.gcf()
cax = f.get_axes()[1]
cax.set_ylabel("Wind Deployment (MW)")
for idx, row in loadregions.iterrows():
    fnt = 10
    txt=plt.annotate(s=row[cln], xy=(loadregions.geometry.centroid.x[idx],loadregions.geometry.centroid.y[idx]),
                 horizontalalignment='center', fontsize=8, wrap=True, color='k')
    txt.set_path_effects([PathEffects.withStroke(linewidth=4, foreground='w')])
#ax.autoscale()
#sm = plt.cm.ScalarMappable(cmap='rainbow', norm=plt.Normalize(vmin=latlonGpd_join['wind_cf'].min(), vmax=latlonGpd_join['wind_cf'].max()))
#cbar_axis = inset_axes(latlonGpd_join, width='10%', height='5%',loc='lower right')
#plt.colorbar(sm, cax=cbar_axis, orientation='horizontal', pad=0.02)
#latlonGpd_join.text(x=-74, y=28, s='Wind capacity factors', fontsize=9.8)
minx, miny, maxx, maxy = pRegionShapes.total_bounds
plt.xlim(minx, maxx)
plt.ylim(miny, maxy)
fig.tight_layout()
plt.show()

fig.savefig(save_dir + '_WindDep_NE2040', dpi=300)

