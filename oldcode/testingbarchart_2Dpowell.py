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

# read in data

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)
# IStwoD_optimal.ADratio[140:180]
# test3[-5]
colorsAD = f.ADcolors(twoD_optimal)
IScolorsAD = f.ADcolors(IStwoD_optimal)

fig,ax = plt.subplots(2)
ax[0].bar(twoD_optimal.year, twoD_optimal.Crate,width=0.1, color = colorsAD)
ax[1].bar(IStwoD_optimal.year, IStwoD_optimal.Crate,width=0.1,color = IScolorsAD)
# plt.xlim(7,9)

CO2 = mpatches.Patch(color='#018571', label='CO$_2$ (ALK:DIC < 0.7)')
bicarb = mpatches.Patch(color='#80cdc1', label='HCO$_3$$^{-}$ (0.7 < ALK:DIC < 1.3)')
carb = mpatches.Patch(color='#dfc27d', label='H$_2$CO$_{3}$$^{2-}$ (ALK:DIC > 1.3)')
ax[0].legend(handles=[CO2,bicarb,carb])
ax[0].set_title('Powell2D')
plt.show()
