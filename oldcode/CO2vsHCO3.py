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


# 2D Optimal No IS change
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change
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

colors_fan = ['#e41a1c','darkgray','darkgray','darkgray','darkgray','#ff7f00','#984ea3']
IScolors_fan = ['darkgray','darkgray','#ff7f00','#984ea3']
alpha = [1,0.5,0.5,0.5,0.5,1,1]
ISalpha = [0.5,0.5,1,1]
noIS = [both_1D[0],fan_after[0],fan_after[1],fan_after[2],fan_after[3],both_1D_optimal,twoD_optimal]
IS = [ISboth_1D[9],ISboth_1D[11],ISboth_1D_optimal,IStwoD_optimal]

for i in range(len(noIS)):
    noIS[i] = f.decompose(noIS[i])
for i in range(len(IS)):
    IS[i] = f.decompose(IS[i])
all = noIS + IS
allcolors = colors_fan + IScolors_fan
allalpha = alpha + ISalpha

fig,ax = plt.subplots(2)
for i in range(len(all)):
    ax[0].plot(all[i].PgHCO3.sum(),all[i].PgCO2.sum(),alpha=allalpha[i],color = allcolors[i],marker='o',markeredgecolor='k', linewidth=2, markersize=10)
    ax[1].plot(all[i].Ccum[200],all[i].PgCO2.sum(),alpha=allalpha[i],color = allcolors[i],marker='o',markeredgecolor='k', linewidth=2, markersize=10)
ax[0].set_xlabel('Total pure HCO$_3$$^{-}$ added')
ax[0].set_ylabel('Total pure CO$_2$ added')
ax[1].set_xlabel('Total carbon added')
ax[1].set_ylabel('Total pure CO$_2$ added')


plt.tight_layout()
#plt.savefig('HCO3vsCO2.pdf')
plt.show()
