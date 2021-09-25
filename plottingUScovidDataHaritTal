# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:27:56 2021

@author: HARIT
"""

from matplotlib import pyplot as plt
import pandas as pd

dataFrameAllStates = pd.read_csv("us-counties.csv")
dataFrame_California = dataFrameAllStates[dataFrameAllStates['state'] == 'California'].copy()
dataFrame_California ['date'] = pd.to_datetime( dataFrame_California['date'])

series_California_total = dataFrame_California.groupby('date')['cases'].sum()
series_California_difference = series_California_total.diff()

plt.plot(series_California_difference.index, series_California_difference.values)

plt.xlabel("Date")
plt.ylabel("New Cases")
plt.title("California New Cases Per Day")

plt.show()
