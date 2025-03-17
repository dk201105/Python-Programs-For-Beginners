#write a program to generate n terms of (-6,-3,0,3,6,9,12...n)
n=int(input("Enter number of digits to be shown: "))
for i in range(-2,n+1):
    print(i*3, end=" ")
