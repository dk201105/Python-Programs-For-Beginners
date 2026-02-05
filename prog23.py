# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:54:11 2025

@author: 23csc11
"""

import pandas as pd
import matplotlib.pyplot as plt

planets = pd.read_csv("Planets.csv")
print(planets)

print("Year in which the distance found is maximum for each method column:\n",planets.groupby("method")["year"].max())

print("Summary statistics for the entire database:\n",planets.describe())

mean = planets.groupby("year")["orbital_period"].mean()
print(mean)

plt.plot(mean)
plt.show()

plt.scatter(planets['number'], planets['mass'], alpha=0.5)
plt.xlabel("Number of Planets in System")
plt.ylabel("Mass")
plt.show()

greater = planets[(planets["distance"] > 70) & (planets["year"] > 1999)]
print("Details of planets whose distance is greater than 70 and the year is before 1999", greater)

