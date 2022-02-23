import numpy as np
import pandas as pd
import functions as f

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

models = [both_1D_optimal,twoD_optimal,ISboth_1D_optimal,IStwoD_optimal]
CO2 = []
HCO3 =[]
H2CO3 =[]
Ccum = []

for i in range(len(models)):
    models[i] = f.decompose(models[i])
    CO2.append(models[i].PgCO2.sum())
    HCO3.append(models[i].PgHCO3.sum())
    H2CO3.append(models[i].PgH2CO3.sum())
    Ccum.append(models[i].Ccum[200])
    
