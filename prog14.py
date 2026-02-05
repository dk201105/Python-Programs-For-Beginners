# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 12:19:05 2025

@author: 23csc11
"""
import pandas as pd

dict= {"January":5000, "February":6200, "March":5800, "April":5200, "May":6100}
sales = pd.Series(dict)

print("Original Sales Table=\n",sales)

sales.index = [f"{month} 2024" for month in sales.index]

print("\nModified Sales Table=\n",sales)

max = sales.argmax()
print("\nThe maximum sales month is:",max)

sales2= sales["February 2024":"March 2024"]
print("\n",sales2)