import numpy as np
n=int(input("Enter the number of employees:"))
bp=[]
da=[]
hra=[]
cca=[]
total=[]
for i in range (0,n):
   sl=int(input("Enter the salary of the employee:"))
   d = sl*(10/100)
   h = sl*(5/100)
   total_p=(sl+d+d+h)
   total.append(total_p)
   da.append(d)
   bp.append(sl)
   hra.append(h)
   cca.append(d)
emp_sl = np.array(bp)
emp_da = np.array(da)
emp_hra = np.array(hra)
emp_cca = np.array(cca)
total_salary = np.array(total)

print("\nBasic Pay:", emp_sl, "\n")
print("DA:", emp_da, "\n")
print("HRA:", emp_hra, "\n")
print("CCA:", emp_cca, "\n")
print("Total Salary:", total_salary, "\n")

grid = np.column_stack([emp_sl, emp_da, emp_hra, emp_cca, total_salary])

print("Pay Matrix:\n",grid)
 
print("\nEmployee with the highest salary:\n", np.argmax(total_salary)+1)
print("\nAverage Salary:\n", np.mean(total_salary))
print("\nLowest HRA:\n", np.argmin(emp_hra)+1)
print("\nTotal Expenditure:\n", np.sum(total_salary))


