#counting number of odd and even number
n=int(input("Enter number of digits to be counted: "))
o=0
e=0
for i in range(0,n):
    number=int(input("Enter number: "))
    if number%2==0:
        e+=1
    else:
        o+=1

print("The number of odd numbers: ", o)
print("The number of even numbers:", e)