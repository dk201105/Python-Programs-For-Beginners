#sum of series (1^2/1.....n^2/n)
n=int(input("Enter last term of series: "))
sum=0
for i in range(1,n+1):
    sum=sum+(i**2)/i
    print("sum=",sum)
    