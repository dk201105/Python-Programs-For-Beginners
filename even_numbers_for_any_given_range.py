#print only even numbers for the given range
r=int(input("Enter end number of range: "))
for i in range(1,r+1):
    if(i%2==0):
        print(i, end=" ")
    else:
        continue

