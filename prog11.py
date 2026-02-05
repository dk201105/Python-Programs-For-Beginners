# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:03:42 2025

@author: 23csc11
"""

import numpy as np

students_dtype = np.dtype([
    ('roll_no', 'i4'),
    ('name', 'U15'),
    ('maths', 'f8'),
    ('science', 'f8'),
    ('english', 'f8')
])

students = np.array([
    (101, 'Arjun', 85.5, 92.0, 78.5),
    (106, 'Bhavna', 70.0, 88.0, 95.0),
    (103, 'Chirag', 95.0, 75.5, 80.0),
    (105, 'Deepa', 60.5, 68.0, 72.5),
    (102, 'Eshan', 92.0, 92.0, 92.0),
    (104, 'Fiona', 78.0, 80.5, 85.0),
    (107, 'Ganesh', 92.0, 92.0, 92.0),
], dtype=students_dtype)

print("Initial Data:")
print(students)

print("\na. Average Marks:")
print(f"Average Mathematics: {students['maths'].mean():.2f}")
print(f"Average Science: {students['science'].mean():.2f}")
print(f"Average English: {students['english'].mean():.2f}")

total_marks = students['maths'] + students['science'] + students['english']

new_dtype_11 = students_dtype.descr + [('total', 'f8')]
new_students = np.empty(students.shape, dtype=new_dtype_11)

for name in students_dtype.names:
    new_students[name] = students[name]
    
new_students['total'] = total_marks

print("\nb. Data with Total Marks Added:")
print(new_students)

max_total = new_students['total'].max()
highest_scorers = new_students[new_students['total'] == max_total]

print("\nc. Student(s) with Highest Total Marks:")
print(f"Highest Total Marks Scored: {max_total:.2f}")
print(highest_scorers[['name', 'total']])

sorted_students = np.sort(new_students, order='roll_no')

print("\nd. Array Sorted by Roll Number (Ascending):")
print(sorted_students)
