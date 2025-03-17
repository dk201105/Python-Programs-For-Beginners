min_temp=100
n=int(input("Enter the number of elements: "))

for i in range(0,n):
    temp=int(input("Enter temp: "))
    if temp<min_temp:
        min_temp=temp
        print(min_temp)
        
print(min_temp)