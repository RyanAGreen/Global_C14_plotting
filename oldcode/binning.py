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

IScontrol = pd.read_fwf(ISpath + "IScontrol.txt",header=None,infer_nrows=1000)
IScontrol = f.organizedata(IScontrol)


# 2D Optimal No IS change (0.04 % of minimization) improvement of 18%, 0.49
# IS_2D optimal
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/Powell2Dinversion.txt",header=None,infer_nrows=1000)
twoD_optimal = f.organizedata(twoD_optimal)

# 2D optimal IS change (0.1 % of minimization) improvement of  58%, 1.16
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/ISPowell2Dinversion.txt",header=None,infer_nrows=1000)
IStwoD_optimal = f.organizedata(IStwoD_optimal)
df = IStwoD_optimal
for i in range(len(df['ADratio'])):
    if df['ADratio'][i] <= 1 :
        df['PgCO2'][i] = (1-df['ADratio'][i])*(df['Crate'][i]*100)
        df['PgHCO3'][i] = df['ADratio'][i]*(df['Crate'][i]*100)
        df['PgH2CO3'][i] = df['ADratio'][i]*0
    else :
        df['PgCO2'][i] = (1-df['ADratio'][i])*0
        df['PgHCO3'][i] = (2-df['ADratio'][i])*(df['Crate'][i]*100)
        df['PgH2CO3'][i] = (df['ADratio'][i]-1)*(df['Crate'][i]*100)
df.PgH2CO3.sum() + df.PgHCO3.sum() + df.PgCO2.sum()
df.PgCO2[4]
df.PgHCO3[4]
df.PgH2CO3[4]
df.ADratio[4]
df.Crate[4]
df.ADratio[200]

for val in df['ADratio']:
    test =[]
    if val <= 1 :
        test.append('less than 1')
    else :
        test.append('greater than 1')
print(test)
df.ADratio[200] <=1

both_1D = f.read1Dboth(NoISpath)
ISboth_1D = f.read1Dboth(ISpath)
oneD = both_1D[1]
IS1D = ISboth_1D[10]


# pulses = f.binning(oneD)
totalCO2 = f.totalCO2(oneD)
totalCO2.TotalCO2.sum()

print(totalCO2.TotalCO2.sum())
# pulses1 = f.binning(IS1D)
totalCO21 = f.totalCO2(IS1D)
print(totalCO21.TotalCO2.sum())

pulses2 = f.binning(twoD_optimal)
totalCO22 = f.totalCO2(twoD_optimal)
print(pulses2,totalCO22.TotalCO2.sum())

pulses3 = f.binning(IStwoD_optimal)
totalCO23 = f.totalCO2(IStwoD_optimal)
print(pulses3,totalCO23.TotalCO2.sum())
