#prime number checking
n=int(input("Enter Number:"))
c=0
for i in range(2,(n//2)+1):
    if n%i==0:
        c=1
        break
if c==1:
    print("This is not a prime number")
else:
    print("This is a prime number")