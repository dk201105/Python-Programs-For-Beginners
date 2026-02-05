# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 11:43:44 2025

@author: 23csc11
"""

import pandas as pd
import numpy as np

list= [3.5, 7.2, np.nan ,12.1, 5.3, np.nan, 9.0]
print("\nOriginal list:", list)

series1= pd.Series(list)
mean = series1.mean()
series1[2]=mean
series1[5]=mean
print("\nThe mean is:", mean)
print("\nGenerated list\n",series1)
print("\nThe number of unique values is:", series1.nunique())

a = series1.sort_values(ascending=False).reset_index(drop=True)
print("\nSorted Series:\n", a)

