#sum of series 1^2...n^2
n=int(input("Enter the end number of the series: "))
i=1
sum=0
while(i<=n):
    sum=sum+(i**2)
    i+=1
    
print("The sum of the squares of the given series is:", sum)
    