#sum of series 1^3...n^3
n=int(input("Enter the end number of the series: "))
e=int(input("Enter the exponent: "))
i=1
sum=0
while(i<=n):
    sum=sum+(i**e)
    i+=1
    
print("The sum of the", e,"th terms of the given series is:", sum)
