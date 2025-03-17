n=100
c=0
for i in range(0,n):
    if i%3==0:
        print(i, end=" ")
        c+=1
print("")
print("Number of numbers divisible by 3 are", c)