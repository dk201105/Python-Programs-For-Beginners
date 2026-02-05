# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 11:40:55 2025

@author: 23csc11
"""

import pandas as pd

data = {
    'Day': ['Monday', 'Monday', 'Tuesday', 'Tuesday', 'Wednesday', 'Wednesday'],
    'City': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Temperature': [25, 28, 30, 32, 24, 26]
}

df_temp = pd.DataFrame(data)

print("Data Frame used:\n", df_temp)

city_means = df_temp.groupby('City')['Temperature'].mean()
print("\nAverage temperature per city:\n", city_means)

df_temp['City_Mean'] = df_temp.groupby('City')['Temperature'].transform('mean')

df_temp['Deviation'] = df_temp['Temperature'] - df_temp['City_Mean']

print("\nFinal DataFrame with Deviation:\n", df_temp)

pivot = df_temp.pivot(index="Day", columns="City", values="Temperature")

print("\nPivoted table is:\n", pivot)
