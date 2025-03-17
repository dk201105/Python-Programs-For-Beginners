# permutation combintation recursion

"""
Created on Wed Oct  4 10:35:50 2023

@author: 23csc11
"""

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return(n*fact(n-1))
    
n=int(input("Enter n: "))
r=int(input("Enter r: "))

nr=n-r

f1= fact(n)
f2= fact(r)
f3= fact(nr)

permutation= f1/f3
combination= f1/(f2*f3)

print("Permutation= ", permutation)
print("Combination= ", combination)
    