# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 12:56:10 2025

@author: 23csc11
"""
import pandas as pd

emp_age = {"Alice": 25, "Bob": 30, "Carol": 28, "Dave": 35, "Eve": 40}
emp_dept = {"Alice": "HR", "Bob": "IT", "Carol": "Finance", "Dave":"IT", "Eve":"HR"}
emp_salary = {"Alice":50000, "Bob":60000, "Carol":70000, "Dave":80000, "Eve": 55000}

emp_DF = pd.DataFrame({"Age": emp_age,
              "Department": emp_dept,
              "Salary": emp_salary})

print(emp_DF)

avg_salary = emp_DF.groupby('Department')['Salary'].mean()
print("\nAverage Salary per Dept:\n", avg_salary)

emp_DF['Bonus'] = emp_DF['Salary'] * 0.10

print("\nBonus of 10% added:\n", emp_DF)

it_older_30 = emp_DF[(emp_DF['Age'] > 30) & (emp_DF['Department'] == 'IT')]
print("\nEmployees > 30 in IT:\n", it_older_30)
