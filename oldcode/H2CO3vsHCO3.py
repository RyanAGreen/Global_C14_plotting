import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import functions as f
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches


# read in data

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

# CO2obs = pd.read_csv("/home/RyanGreen/CYCLOPS/OUTPUT/Pleist/Project1/observations/IceCoreCO2.txt",engine='openpyxl',header=None)
CO2obs = pd.read_csv('~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/IceCoreCO2.txt',sep='\t',header=69,skiprows=68)
CO2obs = CO2obs.rename(columns = {'age_gas_calBP':'year','co2_ppm':'CO2'})
CO2obs['year'] = CO2obs['year'].apply(f.fix)

# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)

both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)

# No IS change both constraints 1D inversion optimal. AD 0.1
both_1D_optimal = both_1D[1]
# IS change both constraints 1D inversion optimal. AD 1.0
ISboth_1D_optimal = ISboth_1D[10]

fan_before = [] # no need for fan before because 0.1
fan_after = []
ISfan_before = []
ISfan_after = []
for i in range(1,6):
    fan_after.append(both_1D[1+i])
    ISfan_before.append(ISboth_1D[10-i])
    ISfan_after.append(ISboth_1D[10+i])

colors_fan = ['darkgray','darkgray','darkgray','darkgray','darkgray','#ff7f00','#984ea3']
IScolors_fan = ['darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','#ff7f00','#984ea3']
alpha = [0.5,0.5,0.5,0.5,0.5,1,1]
ISalpha = [0.5,0.5,0.5,0.5,0.5,0.5,1,1]
noIS = [both_1D[0],fan_after[0],fan_after[1],fan_after[2],fan_after[3],both_1D_optimal,twoD_optimal]
IS = [ISboth_1D[9],ISboth_1D[11],ISboth_1D[12],ISboth_1D[13],ISboth_1D[14],ISboth_1D[15],ISboth_1D_optimal,IStwoD_optimal]

for i in range(len(noIS)):
    noIS[i] = f.decompose(noIS[i])
for i in range(len(IS)):
    IS[i] = f.decompose(IS[i])
    # all[i] = f.decompose(all[i])
all = noIS + IS
allcolors = colors_fan + IScolors_fan
allalpha = alpha + ISalpha

fig,ax = plt.subplots(3)
for i in range(len(noIS)):
    ax[0].plot(noIS[i].PgHCO3.sum(),noIS[i].PgH2CO3.sum(),alpha=alpha[i],color = colors_fan[i],marker='o',markeredgecolor='k', linewidth=2, markersize=10)
for i in range(len(IS)):
    ax[1].plot(IS[i].PgHCO3.sum(),IS[i].PgH2CO3.sum(),alpha=ISalpha[i],color = IScolors_fan[i],marker='o',markeredgecolor='k', linewidth=2, markersize=10)
for i in range(len(all)):
    ax[2].plot(all[i].PgHCO3.sum(),all[i].PgH2CO3.sum(),alpha=allalpha[i],color = allcolors[i],marker='o',markeredgecolor='k', linewidth=2, markersize=10)
# for i in range(len(noIS)):
#     ax[1].plot(noIS[i].year,noIS[i].CO2,alpha=alpha[i],color = colors_fan[i])
# for i in range(len(IS)):
#     ax[3].plot(IS[i].year,IS[i].CO2,alpha=ISalpha[i],color = IScolors_fan[i])
# for i in range(len(all)):
#     ax[5].plot(all[i].year,all[i].CO2,alpha=allalpha[i],color = allcolors[i])

# ax[5].plot(CO2obs.year,CO2obs.CO2,color = 'r')
# ax[5].set_xlim(0,20)



plt.show()
