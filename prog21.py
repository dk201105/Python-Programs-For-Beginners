# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:06:30 2025

@author: 23csc11
"""

import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("iris.csv")
print(iris)

avg = iris.groupby("species")["petal_length"].mean()
print(avg)

plt.plot(avg)
plt.show()

for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], label=species)
plt.legend()
plt.title("Sepal Dimensions")
plt.show()

longest = iris["petal_length"].idxmax()
print("\nLongest petal:\n",iris.iloc[longest])

widest = iris["petal_width"].idxmax()
print("\nWidest petal:\n", iris.iloc[widest])

print("\nMean sepal length by species:\n",iris.groupby("species")["sepal_length"].mean())
print("\nMean petal length by species:\n",iris.groupby("species")["petal_length"].mean())

print("\nCount by species:\n",iris.groupby("species")["species"].count())

