#armstrong number checking
n=int(input("Enter the number: "))
temp=n
r=0
sum=0
while n!=0:
    r=n%10
    n//=10
    sum+=(r**3)
    
if temp == sum:
    print("This is an armstrong number")
else:
    print("Not an armstrong number")
    