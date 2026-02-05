# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:29:05 2025

@author: 23csc11
"""

import pandas as pd

def get_bmi_category(row):
    w = row["Weight(in kg)"]
    h = row["Height(in m)"]

    if h <= 0:
        return "Invalid Data"
    bmi = w/(h*h)
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <=24.9:
        return "Normal"
    elif bmi>=25.0 and bmi<=29.9:
        return "Overweight"
    else:
        return "Obese"
    
df_data={
        "Name":["Divya", "Priyan", "Johanna", "Michell", "Ananya", "Abdur", "Anton"],
        "Height(in m)": [1.65, 1.61, 1.71, 1.63, 1.72, 1.63, 1.70],
        "Weight(in kg)": [65, 45, 72, 52, 66, 75, 48]
}

df = pd.DataFrame(df_data)

print("Original Dataframe:\n", df)

df["Category"] = df.apply(get_bmi_category, axis=1)

print("\nDataframe with BMI category added:\n",df)