#sine series

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return(n*fact(n-1))
    
s=0    
x=int(input("Enter x:"))
n=int(input("Enter number of terms: "))
for i in range(1,n+1, 2):
    s+=x**1/(fact(i))
print(s)
    
    