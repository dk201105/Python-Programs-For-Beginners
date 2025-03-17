#counting number of odd and even number
n=int(input("Enter number of digits to be counted: "))
n=0
p=0
for i in range(0,n+1):
    number=int(input("Enter number: "))
    if "-" in str(number):
        n+=1
    else:
        p+=1
        

print("The number of negative numbers: ", n)
print("The number of positive numbers:", p)

