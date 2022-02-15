# need to make proxy legend
# make histogram for ALK:DIC ratio and Crate in bottom panel
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#cd ~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/
import functions as f
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

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
CO2obs['Ccum'] = 0


#d14C observations
d14C = pd.read_csv("~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/IntCalSmoothed.txt",header=None)
D14C = d14C.rename(columns = {0:'year',3:'D14C'})
D14C['year'] = D14C['year'].apply(f.fix)
D14C['Crate'] = 0
D14C['Ccum'] = 0

#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)
controlscore,controlmean = f.score(control,control)

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)
IScontrolscore,IScontrolmean = f.score(IScontrol,IScontrol)

# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# 2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/2Doptimal.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

#2D optimal smooth
twoD_smoothed = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_smoothed = f.organizedata(twoD_smoothed)

CO2_only = pd.read_fwf(NoISpath + "2Druns/2DCO2only.txt",header=None,infer_nrows=1000)
CO2_only = f.organizedata(CO2_only)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/IS_2Doptimal.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)
#2D optimal smooth
IStwoD_smoothed = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_smoothed = f.organizedata(IStwoD_smoothed)

ISCO2_only = pd.read_fwf(ISpath + "2Druns/IS2DCO2only.txt",header=None,infer_nrows=1000)
ISCO2_only = f.organizedata(ISCO2_only)

both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)

# 1D fan
fan_before1 = both_1D[3]
fan_after1 = both_1D[5]
fan_before2 = both_1D[2]
fan_after2 = both_1D[6]
fan_before3 = both_1D[1]
fan_after3 = both_1D[7]
fan_before4 = both_1D[0]
fan_after4 = both_1D[8]

# IS 1D fan
ISfan_before1 = ISboth_1D[10]
ISfan_after1 = ISboth_1D[12]
ISfan_before2 = ISboth_1D[9]
ISfan_after2 = ISboth_1D[13]
ISfan_before3 = ISboth_1D[8]
ISfan_after3 = ISboth_1D[14]
ISfan_before4 = ISboth_1D[7]
ISfan_after4 = ISboth_1D[15]


# No IS change both constraints 1D inversion optimal. AD 0.4
both_1D = both_1D[4]
# IS change both constraints 1D inversion optimal. AD 1.1
ISboth_1D = ISboth_1D[11]

#colors
colors_fan = ['darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','darkgray','saddlebrown','black','#e41a1c','#ff7f00','#984ea3','#f781bf']
colors = ['saddlebrown','black','#e41a1c','#ff7f00','#984ea3','#f781bf']
colors2 = ['white','white','#e41a1c','#ff7f00','#984ea3','#f781bf']
# colors1 = ['darkgray','black','#66c2a5','#fc8d62','#8da0cb','#e78ac3']
# colors2 = ['darkgray','black','#7fc97f','#beaed4','#fdc086','#ffff99']
# colors3 = ['darkgray','black','#1b9e77','#d95f02','#7570b3','#e7298a']
# colors4 = ['darkgray','black','#a6cee3','#1f78b4','#b2df8a','#33a02c']
# colors5 = ['darkgray','black','#8dd3c7','#ffffb3','#bebada','#fb8072']

#only difference is the observations so I can plot in loop
D14C_atm = [D14C,control,CO2_only,both_1D,twoD_optimal,twoD_smoothed]
IS_D14C_atm = [D14C,control,ISCO2_only,ISboth_1D,IStwoD_optimal,IStwoD_smoothed]
CO2_atm = [fan_before1,fan_before2,fan_before3,fan_before4,fan_after1,fan_after2,fan_after3,fan_after4,CO2obs,control,CO2_only,both_1D,twoD_optimal,twoD_smoothed]
IS_CO2_atm = [ISfan_before1,ISfan_before2,ISfan_before3,ISfan_before4,ISfan_after1,ISfan_after2,ISfan_after3,ISfan_after4,CO2obs,control,ISCO2_only,ISboth_1D,IStwoD_optimal,IStwoD_smoothed]

#
# labels = ['Observation data','Control','CO$_2$ only','1D dual constraint','2D dual constraint']
# # ISlabels with original control run
# ISlabels = ['Observation data','Control with changed IS','CO$_2$ only','1D dual constraint','2D dual constraint']
#ISlabels = ['Observation data','Control with changed IS','CO2 only 4% improvement','Optimal 1D CO$_2$ inversion 57% improvement','Optimal 1D  ∆$^{14}$C inversion 53% improvement','Optimal 2D inversion 58% improvement']
#labels = ['Observation data','Control','CO2 only {:.0f}% improvement'.format(CO2_onlyscore),'Optimal 1D CO$_2$ inversion {:.0f}% improvement'.format(CO2_optimalscore),'Optimal 1D  ∆$^1$$^4$C inversion {:.0f}% improvement'.format(D14C_optimalscore),'Optimal 2D inversion (A:D mean of {:1.2f}) {:.0f}% improvement'.format(twoD_optimalratio,twoD_optimalscore)]
linestyles_fan = ['-','-','-','-','-','-','-','-','-','--','-','-','-','-']
linewidths_fan = ['2','2','2','2','2','2','2','2','2.5','2.5','2.5','2.5','2.5','2.5']
linestyles = ['-','--','-','-','-','-']
linewidths = ['2.5','2.5','2.5','2.5','2.5','2.5']
linewidths2 = ['2.5','2.5','2.5','2.5','2.5','2.5']
alpha = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1]
alpha2 = [0,0,1,1,1,1]
colorsAD = f.ADcolors(twoD_smoothed)
IScolorsAD = f.ADcolors(IStwoD_smoothed)

# make figure
fig, ax = plt.subplots(3,2,sharex=True,sharey='row',figsize=(10,8))
ax=ax.flatten()
ax4 = ax[4].twinx()
ax5 = ax[5].twinx()

ax4.sharey(ax5)
plt.rcParams["font.weight"] = "bold"

for i in range(len(D14C_atm)):
    # plot atmospheric D14C for no IS change
    ax[0].plot(D14C_atm[i].year,D14C_atm[i].D14C,linewidth=linewidths[i],ls=linestyles[i],color = colors[i])
    # plot Crate for no IS change
    ax[4].plot(D14C_atm[i].year,D14C_atm[i].Crate,linewidth=linewidths2[i],ls=linestyles[i],color = colors2[i])
    ax4.plot(D14C_atm[i].year,D14C_atm[i].Ccum,alpha=0.00001,linewidth=linewidths[i],ls=linestyles[i],color = colors2[i])
    ax4.hlines(y=D14C_atm[i].Ccum[200],linestyle='solid',lw=2.5,color=colors2[i],xmin=-1, xmax=21,alpha = alpha2[i])
    # plot atmospheric D14C for IS change
    ax[1].plot(IS_D14C_atm[i].year,IS_D14C_atm[i].D14C,linewidth=linewidths[i],ls=linestyles[i],color = colors[i])
    # plot Crate for IS change
    ax[5].plot(IS_D14C_atm[i].year,IS_D14C_atm[i].Crate,linewidth=linewidths2[i],ls=linestyles[i],color = colors2[i])
    ax5.plot(IS_D14C_atm[i].year,IS_D14C_atm[i].Ccum, alpha=0.00001,linewidth=linewidths[i],ls=linestyles[i],color = colors2[i])
    ax5.hlines(y=IS_D14C_atm[i].Ccum[200],linestyle='solid',lw=2.5,color=colors2[i],xmin=-1, xmax=21,alpha = alpha2[i])

for i in range(len(CO2_atm)):
    # plot atmospheric CO2 for no IS change
    ax[2].plot(CO2_atm[i].year,CO2_atm[i].CO2,linewidth=linewidths_fan[i],ls=linestyles_fan[i],color = colors_fan[i],alpha = alpha[i])
    # plot atmospheric CO2 for IS change
    ax[3].plot(IS_CO2_atm[i].year,IS_CO2_atm[i].CO2,linewidth=linewidths_fan[i],ls=linestyles_fan[i],color = colors_fan[i],alpha = alpha[i])

ax[4].bar(twoD_optimal.year, twoD_optimal.Crate,width=0.1, color = colorsAD,zorder=2)
ax[5].bar(IStwoD_optimal.year, IStwoD_optimal.Crate,width=0.1,color = IScolorsAD,zorder=2)

for i in range(4):
    for axis in ['top','left','right','bottom']:
        ax[i].spines[axis].set_linewidth(3)
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
    ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray')
    ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray')
    ax[i].grid()
for i in range(4,6):
    for axis in ['top','left','right','bottom']:
        ax[i].spines[axis].set_linewidth(3)
    ax[i].tick_params(bottom=True, top=True, left=True, right=False)
    ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
    ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray',zorder=0)
    ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray',zorder=0)
    ax[i].grid()

#ax4.get_shared_x_axes().join(ax4, ax5)
for i in range(2):
    ax[i].text(18.5,515,'LGM',fontsize='x-small')
    ax[i].text(15.8,515,'HS1',fontsize='x-small')
    ax[i].text(11.9,515,'YD',fontsize='x-small')
    ax[i].text(4.9,515,'Holocene',fontsize='x-small')

ax4.spines['right'].set_linewidth(3)
ax4.tick_params(bottom=False, top=False, left=False, right=True)
ax4.tick_params(axis='both', direction="in", length=7, width=3, color="black")

ax5.spines['right'].set_linewidth(3)
ax5.tick_params(bottom=False, top=False, left=False, right=True)
ax5.tick_params(axis='both', direction="in", length=7, width=3, color="black")

ax[4].set_xlim(0,20)
ax[5].set_xlim(0,20)
ax[2].set_ylim(175,350)
#ax1.set_ylim(175,300)
ax[0].set_ylim(-75,500)
#ax[1].set_ylim(-50,500)
ax[0].set_title('No change in IS',fontweight='bold',pad=20)
ax[1].set_title('Change in IS',fontweight='bold',pad=20)

# making legends
control_legend = mlines.Line2D([], [], color='black', linestyle ='dashed',lw=2.5,label = 'Control run')
observations_legend = mlines.Line2D([], [], color='saddlebrown', linestyle ='solid',lw=2.5,label = 'Observations')
CO2only_legend = mlines.Line2D([], [], color='#e41a1c', linestyle ='solid',lw=2.5,label = 'CO$_2$ addition')
oneD_legend = mlines.Line2D([], [], color='#ff7f00', linestyle ='solid',lw=2.5,label = 'Optimal 1D inversion')
twoD_legend = mlines.Line2D([], [], color='#984ea3', linestyle ='solid',lw=2.5,label = '2D inversion')
oneDrange_legend = mlines.Line2D([], [], color='darkgray', linestyle ='solid',alpha=0.5,lw=2.5,label = 'Range of 1D inversion runs')
CO2 = mpatches.Patch(color='#377eb8', label='CO$_2$')
bicarb = mpatches.Patch(color='#ffff33', label='HCO$_3$$^{-}$')
carb = mpatches.Patch(color='#4daf4a', label='H$_2$CO$_{3}$$^{-}$')
plt.subplots_adjust(bottom=0.3, wspace=0.33)
ax[5].legend(handles=[control_legend,observations_legend,CO2only_legend,oneD_legend,oneDrange_legend,twoD_legend,CO2,bicarb,carb],ncol=2,bbox_to_anchor=(0.7, -0.2),frameon=False)

# labeling
#ax0.set_ylabel('Atmospheric CO$_2$ (ppm)',fontweight='bold',fontsize=14)
ax[2].set_ylabel('Atmospheric CO$_2$ \n (ppm)',fontweight='bold',fontsize=10)
ax[0].set_ylabel('Atmospheric ∆$^{14}$C \n (‰)',fontweight='bold',fontsize=10)
#ax[1].set_ylabel('Atmospheric ∆$^{14}$C (‰)',fontweight='bold',fontsize=14)
#ax[3].set_ylabel('Rate of carbon addition (pgC/yr)',fontweight='bold',fontsize=14)
ax[4].set_ylabel('Rate of addition \n (pgC/yr)',fontweight='bold',fontsize=10)
ax5.set_ylabel('Total carbon added \n (pgC)',fontweight='bold',fontsize=10)

ax[4].set_xlabel('Time before present (kyrBP)',fontweight='bold',fontsize=10)
ax[5].set_xlabel('Time before present (kyrBP)',fontweight='bold',fontsize=10)
#
#
#plt.tight_layout()

plt.show()
