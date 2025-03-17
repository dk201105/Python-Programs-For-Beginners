#finding the factorial of a number
n=int(input("Enter n: "))
f=1
for i in range(1,n+1):
    f*=i
print("Factorial of the given number is: ", f)
    