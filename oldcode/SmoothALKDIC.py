import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.path as mpath
import matplotlib.lines as mlines
import functions as f
from collections import Counter

ISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/ISchange/'
NoISpath = '~/Desktop/UCSC/Mathis_work/1stProject/DataAnalysis/Manuscript/Plotting/modeldata/NoISchange/'

# 2D Optimal No IS change (0.04 % of minimization)
twoD_optimal = pd.read_fwf(NoISpath + "2Druns/2Doptimal.txt",header=None,infer_nrows=1000)
twoD_optimal = twoD_optimal.rename(columns = {0:'year',1:'Crate',2:'Ccum',3:'CO2',4:'D14C',5:'ADratio',6:'D14Cerror',7:'CO2error',8:'totalerror',9:'CO2offset',10:'D14CintNP'})

# 2D optimal IS change (0.1 % of minimization)
IStwoD_optimal = pd.read_fwf(ISpath + "2Druns/IS_2Doptimal.txt",header=None,infer_nrows=1000)
IStwoD_optimal = IStwoD_optimal.rename(columns = {0:'year',1:'Crate',2:'Ccum',3:'CO2',4:'D14C',5:'ADratio',6:'D14Cerror',7:'CO2error',8:'totalerror',9:'CO2offset',10:'D14CintNP'})

twoD_optimal['mov_avg'] = twoD_optimal['ADratio'].rolling(5).mean()
IStwoD_optimal['mov_avg'] = IStwoD_optimal['ADratio'].rolling(5).mean()
twoD_optimal['mov_avg'] = twoD_optimal['mov_avg'].fillna(0)
IStwoD_optimal['mov_avg'] = IStwoD_optimal['mov_avg'].fillna(0)

smoothedCadd = twoD_optimal[['Crate','mov_avg']]
smoothedCadd
ISsmoothedCadd = IStwoD_optimal[['Crate','mov_avg']]
smoothedCadd.astype('float')
smoothedCadd.to_csv('smoothedCadd.txt', header=None, index=None, sep='\t')
ISsmoothedCadd.to_csv('ISsmoothedCadd.txt', header=None, index=None, sep='\t')
