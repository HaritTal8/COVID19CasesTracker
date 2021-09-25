# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:28:18 2021

@author: HARIT
"""

from matplotlib import pyplot as plt
import pandas as pd

dataFrameAllStates = pd.read_csv("us-counties.csv")

unique_states = dataFrameAllStates['state'].unique()

last_date = dataFrameAllStates['date'].max()
dataFrameLastDate = dataFrameAllStates[dataFrameAllStates['date'] == last_date]
sereis_last_date = dataFrameLastDate.groupby('state')['cases'].sum()
sereis_last_date = sereis_last_date.nlargest(10)

for state in sereis_last_date.index:

    dataFrame_State = dataFrameAllStates[dataFrameAllStates['state'] == state].copy()
    dataFrame_State ['date'] = pd.to_datetime( dataFrame_State['date'])
    
    series_State_total = dataFrame_State.groupby('date')['cases'].sum()
    series_State_difference = series_State_total.diff()
    
    plt.plot(series_State_difference.index, series_State_difference.values, label = state)
    
plt.legend()
plt.show()
