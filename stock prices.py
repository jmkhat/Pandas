# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = datetime.datetime(2014,1,1)
end = datetime.datetime(2017,1,1)
df=web.DataReader("XOM",'google',start,end)

print(df.head())
df['Adj Close'].plot()

plt.show()