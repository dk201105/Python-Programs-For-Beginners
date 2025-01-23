n=int(input("Enter number: "))
sum=0
c=0
while n!=0:
    sum+=n%10
    n//=10
    c+=1
print("Sum=",sum,"Count=", c)