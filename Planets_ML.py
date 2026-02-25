# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 01:12:57 2026

@author: 23CSC11
"""

import pandas as pd
#import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("planets.csv") 

print("First 5 rows:")
print(df.head())

df["orbital_period"] = pd.to_numeric(df["orbital_period"], errors="coerce")
df["mass"] = pd.to_numeric(df["mass"], errors="coerce")
df["distance"] = pd.to_numeric(df["distance"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["number"] = pd.to_numeric(df["number"], errors="coerce")

# Remove rows with missing values
df = df.dropna()

# SIMPLE LINEAR REGRESSION
X = df[["orbital_period"]]
y = df["mass"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred = lr_model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\n--- Simple Linear Regression ---")
print("R-squared:", r2)
print("Mean Squared Error:", mse)

# MULTIPLE LINEAR REGRESSION
X_multi = df[["orbital_period", "distance", "year", "number"]]
y_multi = df["mass"]

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

mlr_model = LinearRegression()
mlr_model.fit(X_train_m, y_train_m)

y_pred_m = mlr_model.predict(X_test_m)

r2_multi = r2_score(y_test_m, y_pred_m)
mse_multi = mean_squared_error(y_test_m, y_pred_m)

print("\n--- Multiple Linear Regression ---")
print("R-squared:", r2_multi)
print("Mean Squared Error:", mse_multi)

# Comparison
print("\n--- Model Comparison ---")
print("Simple LR R2:", r2)
print("Multiple LR R2:", r2_multi)
print("Simple LR MSE:", mse)
print("Multiple LR MSE:", mse_multi)

