# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:20:24 2026

@author: 23csc11
"""

import pandas as pd
import matplotlib.pyplot as plt 

flights = pd.read_csv("flights.csv")

print("Display the summary statistics for the entire dataset\n",flights.describe())

year_sums = flights.groupby('year')['passengers'].sum()
max_yr, min_yr = year_sums.idxmax(), year_sums.idxmin()
print("Maximum number of flyers\n", max_yr)
print("Minimum number of flyers\n", min_yr)

for year in flights['year'].unique():
    subset = flights[flights['year'] == year]
    plt.plot(subset['month'].astype(str), subset['passengers'], label=year)
plt.title("Monthly Passengers by Year")
plt.show()

min_row = flights.loc[flights['passengers'].idxmin()]
print("Which year and which month has minimum number of passengers?\n",min_row)

year_totals = flights.groupby('year')['passengers'].sum()
plt.scatter(year_totals.index, year_totals.values)
plt.title("Total Passengers per Year")
plt.show()
