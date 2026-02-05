# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:30:01 2026

@author: 23csc11
"""

import pandas as pd
import matplotlib.pyplot as plt 

crashes = pd.read_csv("car_crashes.csv")
print(crashes.columns)

sample_states = crashes.head(5)
plt.plot(sample_states['states'], sample_states['speeding'], marker='x', color='purple')
plt.title("Speeding-related Crashes (5 States)")
plt.show()

plt.figure(figsize=(12,5))
plt.scatter(crashes['states'], crashes['not_distracted'])
plt.xticks(rotation=90)
plt.title("Crashes vs Not Distracted Driving")
plt.show()

high_ins = crashes.loc[crashes['ins_premium'].idxmax(), 'states']
print(high_ins)

safe_drivers = crashes[(crashes['speeding'] < 4) & (crashes['not_distracted'] > 0)] 
print(safe_drivers)

