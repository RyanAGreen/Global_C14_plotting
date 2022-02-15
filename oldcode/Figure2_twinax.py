import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#cd ~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/
import functions as f

#plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')

# read in data

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

#CO2 observations
# CO2obs = pd.read_csv("/home/RyanGreen/CYCLOPS/OUTPUT/Pleist/Project1/observations/IceCoreCO2.txt",engine='openpyxl',header=None)
CO2obs = pd.read_csv('~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/IceCoreCO2.txt',sep='\t',header=69,skiprows=68)
CO2obs = CO2obs.rename(columns = {'age_gas_calBP':'year','co2_ppm':'CO2'})
CO2obs['year'] = CO2obs['year'].apply(f.fix)
CO2obs['Crate'] = 0

#d14C observations
d14C = pd.read_csv("~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/IntCalSmoothed.txt",header=None)
D14C = d14C.rename(columns = {0:'year',3:'D14C'})
D14C['year'] = D14C['year'].apply(f.fix)

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)
controlscore,controlmean = f.score(control,control)

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)
IScontrolscore,IScontrolmean = f.score(IScontrol,IScontrol)

# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/2Doptimal.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/IS_2Doptimal.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)

D14C1D = f.readD14C(NoISpath)
ISD14C1D = f.readD14C(ISpath)
CO21D = f.readCO2(NoISpath)
ISCO21D = f.readCO2(ISpath)

# 1D D14C inversion
# improvement of .82%, 0.8
D14C1D_optimal = D14C1D[8]
# improvement of 53%, 1.1
ISD14C1D_optimal = ISD14C1D[11]

#1D CO2 inversion
# # improvement of -10%, 0.0
CO21D_optimal = CO21D[0]
# improvement of 57%, 0.9
ISCO21D_optimal = ISCO21D[11]

# improvement of -7%, 0.0
CO2_only = D14C1D[0]
# improvement of 4%, 0.0
ISCO2_only = ISD14C1D[0]

#colors
colors = ['darkgray','black','#e41a1c','#377eb8','#4daf4a','#984ea3']
colors1 = ['darkgray','black','#66c2a5','#fc8d62','#8da0cb','#e78ac3']
colors2 = ['darkgray','black','#7fc97f','#beaed4','#fdc086','#ffff99']
colors3 = ['darkgray','black','#1b9e77','#d95f02','#7570b3','#e7298a']
colors4 = ['darkgray','black','#a6cee3','#1f78b4','#b2df8a','#33a02c']
colors5 = ['darkgray','black','#8dd3c7','#ffffb3','#bebada','#fb8072']

D14C_atm = [D14C,control,CO2_only,D14C1D_optimal,CO21D_optimal,twoD_optimal]
IS_D14C_atm = [D14C,IScontrol,ISCO2_only,ISD14C1D_optimal,ISCO21D_optimal,IStwoD_optimal]

CO2_atm = [CO2obs,control,CO2_only,D14C1D_optimal,CO21D_optimal,twoD_optimal]
IS_CO2_atm = [CO2obs,IScontrol,ISCO2_only,ISD14C1D_optimal,ISCO21D_optimal,IStwoD_optimal]


labels = ['Observation data','Control','CO2 only -7% improvement','Optimal 1D CO$_2$ inversion -10% improvement','Optimal 1D  ∆$^{14}$C inversion 0.82% improvement','Optimal 2D inversion 18% improvement']
ISlabels = ['Observation data','Control with changed IS','CO2 only 4% improvement','Optimal 1D CO$_2$ inversion 57% improvement','Optimal 1D  ∆$^{14}$C inversion 53% improvement','Optimal 2D inversion 58% improvement']
#labels = ['Observation data','Control','CO2 only {:.0f}% improvement'.format(CO2_onlyscore),'Optimal 1D CO$_2$ inversion {:.0f}% improvement'.format(CO2_optimalscore),'Optimal 1D  ∆$^1$$^4$C inversion {:.0f}% improvement'.format(D14C_optimalscore),'Optimal 2D inversion (A:D mean of {:1.2f}) {:.0f}% improvement'.format(twoD_optimalratio,twoD_optimalscore)]
linestyles = ['-','--','-','-','-','-']
linewidths = ['1','1','2.5','2.5','2.5','2.5']


# make figure
fig, ax = plt.subplots(2,2,sharex=True,sharey='row')
ax=ax.flatten()
ax0 = ax[0].twinx()
ax1 = ax[1].twinx()
plt.rcParams["font.weight"] = "bold"
# for i in range(0,4,2):
#     for axis in ['top','left','right','bottom']:
#         ax[i].spines[axis].set_linewidth(3)
# for i in range(1,4,2):
#     for axis in ['top','left','right','bottom']:
#         ax[i].spines[axis].set_linewidth(3)
# ax[0].tick_params(bottom=True, top=True, left=True, right=False)
# ax[0].tick_params(axis='both', direction="in", length=7, width=3, color="black")
# ax0.tick_params(bottom=True, top=True, left=False, right=True)
# ax0.tick_params(axis='both', direction="in", length=7, width=3, color="black")
# ax[1].tick_params(bottom=True, top=True, left=True, right=True)
# ax[1].tick_params(axis='both', direction="in", length=7, width=3, color="black")


for i in range(6):
    # plot atmospheric D14C for no IS change
    ax[0].plot(D14C_atm[i].year,D14C_atm[i].D14C,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label= labels[i])
    # plot atmospheric CO2 for no IS change
    ax0.plot(CO2_atm[i].year,CO2_atm[i].CO2,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label= labels[i])
    # plot Crate for no IS change
    ax[2].plot(CO2_atm[i].year,CO2_atm[i].Crate,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label= labels[i])
    # plot atmospheric D14C for IS change
    ax[1].plot(IS_D14C_atm[i].year,IS_D14C_atm[i].D14C,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label= ISlabels[i])
    # plot atmospheric CO2 for IS change
    ax1.plot(IS_CO2_atm[i].year,IS_CO2_atm[i].CO2,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label= ISlabels[i])
    # plot Crate for IS change
    ax[3].plot(IS_CO2_atm[i].year,IS_CO2_atm[i].Crate,linewidth=linewidths[i],ls=linestyles[i],color = colors[i],label= ISlabels[i])


ax[2].set_xlim(0,20)
ax[3].set_xlim(0,20)
#ax0.set_ylim(175,300)
#ax1.set_ylim(175,300)
#ax[0].set_ylim(-50,500)
#ax[1].set_ylim(-50,500)
ax[2].legend(loc='best')

# labeling
#ax0.set_ylabel('Atmospheric CO$_2$ (ppm)',fontweight='bold',fontsize=14)
ax1.set_ylabel('Atmospheric CO$_2$ (ppm)',fontweight='bold',fontsize=14)
ax[0].set_ylabel('Atmospheric ∆$^{14}$C (‰)',fontweight='bold',fontsize=14)
#ax[1].set_ylabel('Atmospheric ∆$^{14}$C (‰)',fontweight='bold',fontsize=14)
#ax[3].set_ylabel('Rate of carbon addition (pgC/yr)',fontweight='bold',fontsize=14)
ax[2].set_ylabel('Rate of carbon addition (pgC/yr)',fontweight='bold',fontsize=14)
ax[3].set_xlabel('Time before present (kyrBP)',fontweight='bold',fontsize=14)
ax[2].set_xlabel('Time before present (kyrBP)',fontweight='bold',fontsize=14)


plt.tight_layout()

plt.show()
