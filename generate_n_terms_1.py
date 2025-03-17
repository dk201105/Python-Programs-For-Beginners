#write a program to generate n terms of (1,8,27,64)
n=int(input("Enter n: "))
for i in range(1,n+1):
    print(i**3, end=" ")
