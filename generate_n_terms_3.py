#write a program to generate n terms of (-2,-4,-6,-8,-10,-12)
n=int(input("Enter number of digits to be shown: "))
for i in range(0,-(n*2),-2):
    print(i,end=" ")
