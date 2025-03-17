#factorial function
def fact(a):
    if a==1 or a==0:
        return 1
    else:
        fact=1
        for i in range(1,a-1):
            fact*=i
        return fact

n=int(input("Enter n: "))
r=int(input("Enter r: "))
nPr= fact(n)/fact(n-r)
print("Permutation: ",nPr)
nCr=fact(n)/(fact(n-r)*fact(r))
print("Combination: ",nCr)