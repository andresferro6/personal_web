# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:55:32 2020

@author: AndresFerro
"""

import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

pg = wb.DataReader('PG', data_source = 'yahoo', start = '1995-1-1')['Close']

pg_return = np.log(pg / pg.shift(1))
pg_return.dropna(inplace = True)
pg_return.plot()

avg_return = pg_return.mean()
avg_return_anual = avg_return * 250