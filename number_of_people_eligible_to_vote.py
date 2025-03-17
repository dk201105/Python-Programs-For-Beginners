n=int(input("Enter number of people: "))
i=0
c=0
while(i<n):
    age=int(input("Enter age: "))
    if age>=18:
        print("This person is eligible to vote")
        c+=1
    else:
        print("This person is not eligible to vote")
    i+=1
print("The number of people eligible to vote: ",c)