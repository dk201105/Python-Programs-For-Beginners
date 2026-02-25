# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:42:52 2026

@author: 23CSC11
"""

import pandas as pd
#import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.cluster import KMeans

df = pd.read_csv("Diamonds.csv")   # <-- change file name if needed

print("First 5 rows of dataset:")
print(df.head())

# Multiple Regression

X = df.drop("price", axis=1)
y = df["price"]

categorical_cols = ["cut", "color", "clarity"]
numerical_cols = ["carat", "depth", "table", "x", "y", "z"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

X_processed = preprocessor.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
cv_scores = cross_val_score(model, X_processed, y, cv=5, scoring="r2")

print("\n--- Multiple Linear Regression Results ---")
print("R-squared:", r2)
print("Mean Squared Error:", mse)
print("Cross Validation R2:", cv_scores.mean())

# K-Means Clustering

features = df[["carat", "depth", "table", "x", "y", "z", "price"]]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(scaled_features)

cluster_avg_price = df.groupby("cluster")["price"].mean()

print("\n--- K-Means Clustering Results ---")
print("Average price per cluster:")
print(cluster_avg_price)