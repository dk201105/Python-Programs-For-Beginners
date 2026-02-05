# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 11:31:40 2025

@author: 23csc11
"""
import pandas as pd
import numpy as np

data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Price': [50, np.nan, 80, 40],
    'Stock': [20, 15, np.nan, 10]
}

df_prod = pd.DataFrame(data)

mean_price = df_prod['Price'].mean()
df_prod['Price'] = df_prod['Price'].fillna(mean_price)

print("Replaced Price NaN with mean price:\n",df_prod)

min_stock = df_prod['Stock'].min()
df_prod['Stock'] = df_prod['Stock'].fillna(min_stock)

print("\nReplaced Stock NaN with minimum stock value:\n",df_prod)

df_prod['Value'] = df_prod['Price'] * df_prod['Stock']

print("\nAdded Value Column:\n", df_prod)
