# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 12:41:31 2025

@author: 23csc11
"""

import pandas as pd

list1 = [15,20,35,50,70]
list2 = [5,10,15,20,25]
series1 = pd.Series(list1)
series2 = pd.Series(list2)

print("\nThe original series are:\n", series1, "\n", series2)

print("\nDivision of Series1 and Series2\n",series1/series2)

series3 = series1>30

print("\nSeries1>30\n",series3)

series4 = (series1*series2)

print("\n(Series1*Series2)>400\n",series4[series4>400])