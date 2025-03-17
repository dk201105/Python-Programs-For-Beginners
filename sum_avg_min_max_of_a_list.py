l=[12,32,45,65,34,65,34,76,98,67,89,2354,3467,346,234,563]
sum=0
temp=0
for i in l:
    sum+=i
    avg=sum/len(l)
    for i in (0,len(l)-1):
        if l[i-1]>l[i]:
            temp=l[i]
            

print(sum, avg, temp)