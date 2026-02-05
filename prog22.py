# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:30:01 2025

@author: 23csc11
"""

import pandas as pd
import matplotlib.pyplot as plt

company_sales = pd.read_csv("company_sales.csv")
print(company_sales)

plt.plot(company_sales["facecream"], label = "facecream")
plt.plot(company_sales["facewash"], label = "facewash")
plt.plot(company_sales["toothpaste"], label = "toothpaste")
plt.plot(company_sales["shampoo"], label = "shampoo")
plt.plot(company_sales["bathingsoap"], label = "bathingsoap")
plt.plot(company_sales["moisturizer"], label = "moisturizer")

plt.axis([0, 20, 0, 15000])

plt.legend()

plt.show()

plt.scatter(company_sales['month_number'], company_sales['facecream'], label='Face Cream')
plt.scatter(company_sales['month_number'], company_sales['facewash'], label='Face Wash')
plt.title("Face Product Sales")
plt.legend()
plt.show()

minimum = company_sales.sum(axis=0)
print(minimum[1:7].min())

month1 = company_sales["bathingsoap"].idxmax()
month2 = company_sales["moisturizer"].idxmin()

print(company_sales.iloc[month1], "\n\n", company_sales.iloc[month2])

print("\nTotal sale of all products of all months:",company_sales["total_profit"].sum())