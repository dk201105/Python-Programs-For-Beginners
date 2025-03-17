#fibonacci series 
n=int(input("Enter n: "))
a=0
b=1
print(a,b, end=" ")
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(c, end=" ")