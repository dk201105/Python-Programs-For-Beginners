l=[1,2,35,34,76,34,87,34,12,34,76,98,56,98,4,54,34,6,54,234,565,65,7,43,5635,63453]
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
        
print("The even number list is", l1, "The odd number list is", l2)