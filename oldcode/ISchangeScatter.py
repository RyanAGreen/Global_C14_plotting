# this code will plot the CYCLOPS experiments with range of Initial States
# would like to try this with the Powell method

#cd ~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.path as mpath
import matplotlib.lines as mlines
import functions as f

path = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/VariableIS_5/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)


inc = np.linspace(1,1.055,12)
VariableIS_2Druns = []
VariableIS_2Druns_scores = []
VariableIS_2Druns_ratios = []
counter = 0
for i in range(12):
    data = pd.read_fwf(path + "2Dinversion_IS_{:.3f}.txt".format(inc[i]),header=None,infer_nrows=1000)
    data = f.organizedata(data)
    data['permilinc'] = counter
    counter+= 7
    VariableIS_2Druns.append(data)
    score,ratio = f.score(data,control)
    VariableIS_2Druns_scores.append(score)
    VariableIS_2Druns_ratios.append(ratio)
# VariableIS_2Druns_ratios[6]
np.min(VariableIS_2Druns_scores) # optimal rn is 0.04 (31% improvement)
VariableIS_2Druns_scores
test = VariableIS_2Druns[9]

# plotting

plt.rcParams["font.weight"] = "bold"
fig,ax = plt.subplots(2,sharex=True)

ax1 = ax[0].twinx()
for i in range(12):
    ax[1].plot(VariableIS_2Druns[i]['permilinc'][0],VariableIS_2Druns_scores[i],color='#984ea3',marker='o',markeredgecolor='k', linewidth=2, markersize=10)
    ax[0].plot(VariableIS_2Druns[i]['permilinc'][0],VariableIS_2Druns[i]['Ccum'].iloc[-1],color='#984ea3',marker='o',markeredgecolor='k', linewidth=2, markersize=10)
    ax1.plot(VariableIS_2Druns[i]['permilinc'][0],VariableIS_2Druns_ratios[i],color='#984ea3',marker='^',markeredgecolor='k', linewidth=2, markersize=10)

for i in range(2):
    for axis in ['top','bottom','left','right']:
        ax[i].spines[axis].set_linewidth(3.5)
    ax[i].tick_params(axis='y',labelsize='large')
    ax[i].tick_params(axis='x',labelsize='large')
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis="both", direction="in", length=7, width=3, color="black")
ax[0].tick_params(bottom=True, top=True, left=True, right=False)

for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(3.5)
ax1.tick_params(axis='y',labelsize='large')
ax1.tick_params(axis='x',labelsize='large')
ax1.tick_params(bottom=False, top=False, left=False, right=True)
ax1.tick_params(axis="both", direction="in", length=7, width=3, color="black")

ax[1].set_xlabel('Change in ∆$^{14}$C initial state (‰)',fontweight='bold',fontsize=12)
ax1.set_ylabel('ALK:DIC ratio',fontweight='bold',fontsize=12)
ax[0].set_ylabel('Total carbon added (PgC)',fontweight='bold',fontsize=12)
ax[1].set_ylabel('Total error score (%)',fontweight='bold',fontsize=12)
adratio = mlines.Line2D([], [], color='#984ea3', marker='^', linestyle='None',markersize=5, label = 'ALK:DIC ratio')
ccum = mlines.Line2D([], [], color='#984ea3', marker='o', linestyle='None',markersize=5, label = 'Total carbon added')
ax[0].legend(handles=[ccum,adratio],frameon=False,loc='best')
ax[1].hlines(y=100,linestyle='dashed',color='k',xmin=-20, xmax=120)
ax[1].set_ylim(0,200)
ax[0].set_ylim(0,5000)
ax[1].set_xlim(0,75)

plt.show()
