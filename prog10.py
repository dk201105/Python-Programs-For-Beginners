# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:02:57 2025

@author: 23csc11
"""

import numpy as np

pay_bill_dtype = np.dtype([
    ('employee_id', 'i4'),
    ('name', 'U20'),
    ('BP', 'f8'),    
    ('DA', 'f8'),    
    ('HRA', 'f8'),   
    ('CCA', 'f8'),   
])

pay_data = np.array([
    (1001, 'Alice Smith', 50000.00, 15000.00, 10000.00, 2500.00),
    (1002, 'Bob Johnson', 65000.00, 19500.00, 12000.00, 3000.00),
], dtype=pay_bill_dtype)

total_salary = (pay_data['BP'] + pay_data['DA'] + pay_data['HRA'] + pay_data['CCA'])
IT = 0.05 * total_salary
gross_pay = total_salary - IT

final_dtype = pay_bill_dtype.descr + [
    ('Total_Salary', 'f8'),
    ('IT', 'f8'),
    ('Gross_Pay', 'f8')
]

final_pay_bill = np.empty(pay_data.shape, dtype=final_dtype)

for name in pay_bill_dtype.names:
    final_pay_bill[name] = pay_data[name]
    
print("Intial salary table:\n",final_pay_bill)

final_pay_bill['Total_Salary'] = total_salary
final_pay_bill['IT'] = IT
final_pay_bill['Gross_Pay'] = gross_pay

print("\nFinal salary table:\n", final_pay_bill)