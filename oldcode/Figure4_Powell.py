# still need to decide on colors for the observational data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
#cd ~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/
import functions as f

# read in data

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'
obspath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/observations/'

# marchitto
mar = pd.read_fwf(obspath + 'Marchitto.txt',sep='\t')
mar = mar.drop([0])
mar = mar.rename(columns={"D14C": "D14CintNP","Cal.Age":"year"})

chen = pd.read_csv(obspath + 'Chen2020.txt',sep='\t',header=0,skiprows=110)
# Stott
Stott = chen[chen['water.depth']==617]
Stott = Stott[Stott['ref.']=='Stott et al. (2009)']

# Chen
Chen = chen[chen['water.depth']==627]

# Rafter
Rafter = chen[chen['ref.']=='Rafter et al. (2018)']

GoCobs_fromChen = [Stott,Rafter,Chen]


for i in range(3):
    GoCobs_fromChen[i] = GoCobs_fromChen[i].rename(columns = {'cal.age':'year','benthic.D14C':'D14CintNP'})
    GoCobs_fromChen[i] = GoCobs_fromChen[i][GoCobs_fromChen[i]['year']<20000]
    GoCobs_fromChen[i]['year'] = GoCobs_fromChen[i]['year'].apply(f.fix)


#control should be same as Hain 2014
control = pd.read_fwf(NoISpath + "control.txt",header=None,infer_nrows=1000)
control = f.organizedata(control)
controlscore,controlmean = f.score(control,control)

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)
IScontrolscore,IScontrolmean = f.score(IScontrol,IScontrol)


# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

CO2_only = pd.read_fwf(NoISpath + "2Druns/2DCO2only.txt",header=None,infer_nrows=1000)
CO2_only = f.organizedata(CO2_only)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)

ISCO2_only = pd.read_fwf(ISpath + "2Druns/IS2DCO2only.txt",header=None,infer_nrows=1000)
ISCO2_only = f.organizedata(ISCO2_only)

both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)

# 1D D14C inversion
# improvement of .82%, 0.8
both_1D = both_1D[4]
# improvement of 53%, 1.1
ISboth_1D = ISboth_1D[11]

D14C_NP = [mar,GoCobs_fromChen[0],GoCobs_fromChen[1],GoCobs_fromChen[2],control,CO2_only,both_1D,twoD_optimal]
IS_D14C_NP = [mar,GoCobs_fromChen[0],GoCobs_fromChen[1],GoCobs_fromChen[2],IScontrol,ISCO2_only,ISboth_1D,IStwoD_optimal]

#colors
colors = ['brown','brown','brown','brown','black','#e41a1c','#ff7f00','#984ea3']
# colors1 = ['darkgray','black','#66c2a5','#fc8d62','#8da0cb','#e78ac3']
# colors2 = ['darkgray','black','#7fc97f','#beaed4','#fdc086','#ffff99']
# colors3 = ['darkgray','black','#1b9e77','#d95f02','#7570b3','#e7298a']
# colors4 = ['darkgray','black','#a6cee3','#1f78b4','#b2df8a','#33a02c']
# colors5 = ['darkgray','black','#8dd3c7','#ffffb3','#bebada','#fb8072']

labels = ['Marchitto et al. 2007 (benthic)','Stott et al. 2009 (benthic)','Rafter et al. 2018 (benthic and planktic)','Chen et al. 2020 (coral)', 'Control','CO2 only','1D dual constraint','2D dual constraint']
ISlabels = ['Marchitto et al. 2007 (benthic)','Stott et al. 2009 (benthic)','Rafter et al. 2018 (benthic and planktic)','Chen et al. 2020 (coral)','Control with changed IS','CO2 only','1D dual constraint','2D dual constraint']
#labels = ['Observation data','Control','CO2 only {:.0f}% improvement'.format(CO2_onlyscore),'Optimal 1D CO$_2$ inversion {:.0f}% improvement'.format(CO2_optimalscore),'Optimal 1D  ???$^1$$^4$C inversion {:.0f}% improvement'.format(D14C_optimalscore),'Optimal 2D inversion (A:D mean of {:1.2f}) {:.0f}% improvement'.format(twoD_optimalratio,twoD_optimalscore)]
#linestyles = ['-','-.','--',':','--','-','-','-','-']
linestyles = ['-','-','-','-','--','-','-','-','-']
linewidths = ['2','2','2','2','2','2.5','2.5','2.5','2.5']
markers = ['s','s','s','^']
# Stott benthic
# Marchitto benthic
# Rafter Benthic and Planktonic
# Chen Coral


fig,ax = plt.subplots(2,1,sharex=True)
plt.rcParams["font.weight"] = "bold"
for i in range(4):
    ax[0].plot(D14C_NP[i].year,D14C_NP[i].D14CintNP,linewidth=linewidths[i],ls=linestyles[i],marker=markers[i],color = colors[i],label= labels[i])
    ax[1].plot(IS_D14C_NP[i].year,IS_D14C_NP[i].D14CintNP,linewidth=linewidths[i],ls=linestyles[i],marker=markers[i],color = colors[i],label= ISlabels[i])
    ax[0].plot(D14C_NP[i+4].year,D14C_NP[i+4].D14CintNP,linewidth=linewidths[i+4],ls=linestyles[i+4],color = colors[i+4],label= labels[i+4])
    ax[1].plot(IS_D14C_NP[i+4].year,IS_D14C_NP[i+4].D14CintNP,linewidth=linewidths[i+4],ls=linestyles[i+4],color = colors[i+4],label= ISlabels[i+4])

for i in range(2):
    for axis in ['top','left','right','bottom']:
        ax[i].spines[axis].set_linewidth(3)
    ax[i].tick_params(bottom=True, top=True, left=True, right=True)
    ax[i].tick_params(axis='both', direction="in", length=7, width=3, color="black")
    ax[i].grid()
    ax[i].axvspan(11.6, 12.9, alpha=0.4, color='darkgray')
    ax[i].axvspan(14.5, 18, alpha=0.4, color='darkgray')

ax[0].text(18.5,260,'LGM',fontsize='x-small')
ax[0].text(15.9,260,'HS1',fontsize='x-small')
ax[0].text(11.9,260,'YD',fontsize='x-small')
ax[0].text(4.9,260,'Holocene',fontsize='x-small')

ax[0].set_title('No change in IS',fontweight='bold')
ax[1].set_title('Change in IS',fontweight='bold')
ax[0].set_ylabel('Intermediate North Pacific ???$^{14}$C \n (???)',fontweight='bold',fontsize=10)
ax[1].set_ylabel('Intermediate North Pacific ???$^{14}$C \n (???)',fontweight='bold',fontsize=10)
ax[1].set_xlabel('Time before present (kyrBP)',fontweight='bold',fontsize=10)
ax[1].set_xlim(0,20)
ax[0].set_ylim(-650,250)
ax[1].set_ylim(-650,250)
ax[0].legend(loc='lower left',ncol=2)
#ax[1].legend(loc='best')
plt.show()
